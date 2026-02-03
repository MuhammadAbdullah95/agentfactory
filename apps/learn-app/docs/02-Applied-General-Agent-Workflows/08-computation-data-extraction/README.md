---
sidebar_position: 1
title: "Chapter 8: Computation & Data Extraction Workflow"
description: "Build Unix-styled Python utilities that integrate with Bash for accurate calculations and data extraction"
---

# Chapter 8: Computation & Data Extraction Workflow

> "If it's math, it belongs in a script. Period."

## What You'll Build

By the end of this chapter, you'll have a personal toolbox of reusable utilities:

```bash
# Your workflow by chapter end:
find receipts/ -name "*.txt" | xargs cat | add-up
# Extracts dollar amounts from messy text, sums them with 100% accuracy
```

You'll transform from someone who asks AI to "do math in your head" (risky!) to someone who builds and verifies calculation tools that work every time.

## Prerequisites

**From Chapter 3 (Seven Principles)**:

- You understand ALL Seven Principles conceptually
- You know why "Bash is the Key" matters (Principle 1)
- You know why "Verification as Core Step" prevents failures (Principle 3)

**From Chapter 6 (Business Workflows)**:

- You can navigate directories (`cd`, `ls`, `pwd`)
- You've run basic Bash commands
- You understand the pipe operator (`|`) conceptually

**Technical Requirements**:

- Python 3.x installed (type `python3 --version` to check)
- Unix-like terminal (macOS, Linux, or WSL on Windows)
- Access to Claude Code or similar AI assistant

## Chapter Structure

| Lesson | Title                     | Duration | Key Skill                            |
| ------ | ------------------------- | -------- | ------------------------------------ |
| 1      | The Accuracy Gap          | 20 min   | Recognize when Bash math fails       |
| 2      | Single-Purpose Utility    | 25 min   | Build stdin-reading Python script    |
| 3      | The Testing Loop          | 30 min   | Verify with exit codes and test data |
| 4      | Personal Toolbox          | 20 min   | Create persistent aliases            |
| 5      | Data Wrangling            | 35 min   | Extract data with regex              |
| 6      | Capstone: Digital Shoebox | 40 min   | Orchestrate complete workflow        |

**Total Duration**: 170 minutes (~3 hours)

## Seven Principles in Action

This chapter applies the principles you learned in Chapter 3:

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
- Build a Python script that reads from stdin and calculates sums

**Lesson 3-4**: Verification & Persistence

- Learn zero-trust debugging with exit codes
- Transform scripts into personal commands via aliases

**Lesson 5**: Data Extraction

- Use regex to extract dollar amounts from messy text
- Process multiple files with `find` and `xargs`

**Lesson 6**: Capstone

- Orchestrate everything into a real-world "Digital Shoebox" workflow
- Calculate totals from a folder of receipt files

## Quick Start for Chapter 6 Graduates

Already comfortable with terminal basics? Here's what's new:

```bash
# Bash math FAILS with decimals (you'll discover why)
echo $((1.2 + 2.3))  # Error!

# Python script reads from stdin (you'll build this)
echo -e "1.2\n2.3" | python calc.py
# Output: Total: 3.50

# Regex extracts amounts from messy text (you'll learn this)
echo "Lunch: $14.50, Tip: $3.00" | python calc.py
# Output: Total: $17.50
```

## Ready to Start?

Begin with [Lesson 1: The Accuracy Gap](./01-accuracy-gap.md) to discover why precision matters.
