---
sidebar_position: 4
title: "The Testing Loop"
chapter: 8
lesson: 3
duration_minutes: 25
description: "Implement zero-trust debugging with exit codes and test data verification"
keywords:
  [
    "exit codes",
    "verification",
    "zero-trust",
    "debugging",
    "test data",
    "echo $?",
    "error handling",
  ]

skills:
  - name: "Creating Test Data for Verification"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Testing"
    measurable_at_this_level: "Student creates test file with known expected output and uses it to verify script"

  - name: "Interpreting Exit Codes"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Debugging"
    measurable_at_this_level: "Student checks $? after commands and interprets 0=success, non-zero=failure"

learning_objectives:
  - objective: "Create test data and verify script outputs"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates test file with known sum and verifies sum.py produces correct result"

  - objective: "Interpret exit codes to diagnose script failures"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student uses echo $? to check script success and can explain code meanings"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (exit codes, $? variable, test data, verification workflow, zero-trust philosophy) within A2 limit"

differentiation:
  extension_for_advanced: "Research other exit codes (127=command not found, 130=Ctrl+C), write verification script"
  remedial_for_struggling: "Focus only on: create test file with known answer, run script, compare result"
---

# The Testing Loop

Your script runs. No errors. No red text. The terminal returns to the prompt without complaint.

But here is the question that separates professionals from amateurs: **Did it produce the right answer?**

In Lesson 2, you built `sum.py` - a script that reads numbers from stdin and calculates their sum. You ran it, saw output, and moved on. But how do you know the sum was correct? You trusted the script because it ran without crashing. That trust is dangerous.

This lesson introduces the Zero-Trust Testing Loop - a verification workflow that catches bugs before they cost you money, reputation, or hours of debugging. By the end, you will never again assume a script works just because it ran.

## The Trap of Silent Success

Consider this scenario. You have a list of monthly expenses. You pipe them through your sum script:

```bash
cat expenses.txt | python sum.py
# Output: Total: 847.50
```

You report $847.50 in expenses. But the actual total was $947.50 - one line had a typo your script silently skipped. You are now $100 off, and your budget is wrong.

The script did not crash. It returned exit code 0 (success). It produced output. It was wrong.

This is why verification is Principle 3 in the Seven Principles: **"Verification as Core Step."** Never trust output - prove it.

## Creating Test Data with Known Answers

The verification loop starts with something radical: **test data where you already know the answer.**

Before running your script on real expenses, create a test file where you can calculate the expected result by hand:

```bash
# Create test data with a KNOWN answer
echo -e "10\n20\n30" > test_numbers.txt
```

Look at that file. Three numbers: 10, 20, 30. What is their sum?

You do not need a calculator. You do not need Python. **The sum is 60.**

This is your ground truth. When you run your script against this file, the only acceptable output is 60. Any other number means your script has a bug.

```bash
# Run the script against test data
cat test_numbers.txt | python sum.py
# Expected Output: Total: 60
```

The output matches your expectation. Now - and only now - can you begin to trust this script.

## Understanding Exit Codes

Every command in Bash produces two types of output:

1. **Standard output** (stdout): The text you see on screen
2. **Exit code**: A hidden number indicating success or failure

The exit code is stored in a special variable called `$?`. Check it immediately after any command:

```bash
# Run a successful command
cat test_numbers.txt | python sum.py
# Output: Total: 60

# Check the exit code
echo $?
# Output: 0
```

Exit code 0 means "the command ran without crashing." Any non-zero exit code indicates an error:

| Exit Code | Meaning                                      |
| --------- | -------------------------------------------- |
| 0         | Success - command completed without crashing |
| 1         | General error - something went wrong         |
| 2         | Misuse of command - wrong arguments or syntax|
| 127       | Command not found - typo or missing program  |
| 130       | Interrupted by Ctrl+C                        |

Try triggering different exit codes:

```bash
# Command not found
python nonexistent_script.py
# Output: python: can't open file 'nonexistent_script.py': [Errno 2] No such file or directory
echo $?
# Output: 2

# Syntax error in Python
echo "print(1/0)" | python
# Output: ZeroDivisionError: division by zero
echo $?
# Output: 1
```

## The Critical Insight: Exit Code 0 Does Not Mean Correct

Here is the most important lesson in this chapter.

**Exit code 0 means "the script ran without crashing." It does NOT mean "the script produced the correct answer."**

Create a deliberately buggy sum script to see this:

```python
# buggy_sum.py - A script with a silent bug
import sys

total = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    # BUG: Silently skipping lines that start with digits > 5
    if line[0] in '6789':
        continue  # Silent failure - the bug!
    total += float(line)

print(f"Total: {total}")
```

Now test with data that triggers the bug:

```bash
echo -e "10\n60\n30" > test_with_60.txt

cat test_with_60.txt | python buggy_sum.py
# Output: Total: 40.0
echo $?
# Output: 0
```

The exit code is 0. The script "succeeded." But 40 is catastrophically wrong - the correct answer is 100. The script silently skipped the number 60 because it starts with '6'.

Exit codes catch crashes. They do not catch logic errors. **You must verify the output itself.**

## The Complete Verification Workflow

The Zero-Trust Testing Loop has four steps:

**Step 1: Create Test Data with Known Answer**

```bash
# Simple test case - small numbers
echo -e "10\n20\n30" > test_simple.txt
# Expected: 60

# Edge case: decimal numbers
echo -e "10.5\n20.3\n9.2" > test_decimals.txt
# Expected: 40.0

# Edge case: mixed positive and negative
echo -e "100\n-30\n-20" > test_mixed.txt
# Expected: 50
```

**Step 2: Run Script Against Test Data**

```bash
cat test_simple.txt | python sum.py
# Output: Total: 60
```

**Step 3: Check Exit Code**

```bash
echo $?
# Output: 0
```

**Step 4: Verify Output Matches Expectation**

Compare the output (60) to your pre-calculated answer (60). They match.

Only after passing all four steps should you run the script on real expenses.

## Multiple Test Cases Catch More Bugs

A single test is better than no tests. Multiple tests are better than one. Each test case probes a different potential failure:

```bash
# Test case 1: Basic positive numbers
echo -e "10\n20\n30" > test1.txt
cat test1.txt | python sum.py
# Expected: 60
# Output: Total: 60 (PASS)

# Test case 2: Decimal numbers
echo -e "10.5\n20.5" > test2.txt
cat test2.txt | python sum.py
# Expected: 31.0
# Output: Total: 31.0 (PASS)

# Test case 3: Negative numbers
echo -e "100\n-25\n-25" > test3.txt
cat test3.txt | python sum.py
# Expected: 50
# Output: Total: 50.0 (PASS)

# Test case 4: Zero
echo -e "0\n0\n0" > test4.txt
cat test4.txt | python sum.py
# Expected: 0
# Output: Total: 0.0 (PASS)

# Test case 5: Single number
echo "42.5" > test5.txt
cat test5.txt | python sum.py
# Expected: 42.5
# Output: Total: 42.5 (PASS)
```

Each test targets a specific concern:

- Test 1: Does basic addition work?
- Test 2: Does it handle decimals?
- Test 3: Does it handle negative numbers?
- Test 4: Does it handle zeros correctly?
- Test 5: Does it work with a single input?

## Debugging with the Verification Loop

When a test fails, the verification loop becomes your debugging workflow:

```bash
# Test fails!
echo -e "10\n60\n30" > test_bug.txt
cat test_bug.txt | python buggy_sum.py
# Expected: 100
# Output: Total: 40.0 (FAIL - something is wrong!)
```

Now you have actionable information:

- The script runs (exit code 0)
- The output is wrong (40 instead of 100)
- The error pattern is clear (60 was skipped)
- Investigation: Why would 60 be skipped?

This points you toward a specific, debuggable problem.

Without test data, you might have used this buggy script for months before noticing calculations were wrong.

## The Zero-Trust Philosophy

Zero-trust debugging embodies a mindset: **Assume everything is broken until proven otherwise.**

This is especially critical when working with general agents. When you ask Claude Code to sum your expenses, it writes a script and runs it - you learned this pattern in the previous lesson. The agent sees the output. The exit code is 0. Everything looks fine.

But here's the catch: **exit code 0 does not mean correct**. The agent ran the code successfully, but that buggy script from earlier also ran successfully. The agent cannot verify that $40 should have been $100 unless it has test data with known answers.

You must verify. Every time.

The workflow when using a general agent:

1. **Agent generates and runs code**: The script executes, output appears
2. **You check the result**: Does the number make sense?
3. **For critical calculations, you verify**: Create test data with known totals
4. **Trust is earned**: Only after verification against ground truth

This applies to code from any source - your general agent, colleagues, Stack Overflow, or your past self at 2 AM. Trust is earned through verification, not granted through origin.

## Connecting to the Seven Principles

The Zero-Trust Testing Loop embodies two core principles:

**Principle 3: Verification as Core Step**

Every operation should be verified before trusting its output. The testing loop makes verification systematic and repeatable. You do not "check" your script - you prove it with test data.

**Principle 7: Observability**

Exit codes make program behavior visible. Without checking `$?`, errors hide in silence. With exit codes, failures announce themselves. Your debugging becomes data-driven rather than guess-driven.

These principles compound. Verification (P3) produces evidence. Observability (P7) makes that evidence accessible. Together, they create a debugging workflow that catches problems early and provides clear diagnostic information.

## New Command: Exit Codes with $?

You already know `mkdir -p` from previous chapter. This lesson introduces a new concept: **exit codes**.

| Command | What It Does | Example |
|---------|-------------|---------|
| `echo $?` | Prints the exit code of the last command | `echo $?` → `0` (success) |

### The $? Variable

`$?` is a special shell variable that holds the exit code of the most recent command. You must check it immediately after the command you care about - running any other command will overwrite it.

```bash
python sum.py < test.txt   # Run the script
echo $?                     # Check exit code (0 = success)
```

Every command returns an exit code: `0` means success, any other number means failure.

## Practice: Build Your Test Suite

Create a test suite for your sum script:

```bash
# Create test directory
mkdir -p ~/sum-tests
cd ~/sum-tests

# Test 1: Simple sum
echo -e "10\n20\n30" > test_simple.txt
# Expected: 60

# Test 2: Decimals
echo -e "10.5\n20.5\n19.0" > test_decimals.txt
# Expected: 50.0

# Test 3: Negative numbers
echo -e "100\n-50\n-30" > test_negative.txt
# Expected: 20

# Run all tests
for f in test_*.txt; do
    echo "Testing $f:"
    expected=""
    case $f in
        test_simple.txt) expected="60" ;;
        test_decimals.txt) expected="50.0" ;;
        test_negative.txt) expected="20" ;;
    esac
    result=$(cat "$f" | python ~/sum.py)
    echo "  $result (expected Total: $expected)"
    echo "  Exit code: $?"
    echo "---"
done
```

Run this suite every time you modify your script. If any test fails, you have caught a bug before it reaches real data.

## Try With AI

### Prompt 1: Understanding Exit Codes

```
Explain what `echo $?` shows in Bash.

I ran a command and then typed `echo $?` and it showed `0`.
Then I ran a different command and `echo $?` showed `127`.

What do these numbers mean? What are common exit codes I should know about?
```

**What you are learning:** AI teaches the meaning of exit codes - the hidden status indicators that reveal whether commands succeeded or failed.

### Prompt 2: Exit Code Limitations

```
My Python script exits with code 0 but produces the wrong total.

The script sums numbers from stdin. It runs without errors,
`echo $?` shows 0, but when I check the output against test data
I calculated by hand, the number is wrong.

Why doesn't the exit code catch this? What's the difference between
"the script ran successfully" and "the script produced correct output"?
```

**What you are learning:** You teach AI (and reinforce for yourself) the critical distinction between "did not crash" and "produced correct results" - exit codes catch crashes, not logic errors.

### Prompt 3: Collaborative Debugging

```
Help me debug this number-summing script. It should sum all numbers
from stdin.

Here's my test: I created a file with numbers 10, 20, 30.
The expected sum is 60.
But my script outputs 40.

Here's the script:
[paste your script]

The file has numbers on separate lines.
Walk me through how to find and fix the bug.
```

**What you are learning:** Collaborative debugging where you provide the verification framework (test file with known answers) and AI helps identify where the logic diverges from expectation.
