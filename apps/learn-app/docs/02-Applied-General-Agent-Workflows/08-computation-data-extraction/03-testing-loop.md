---
sidebar_position: 4
title: "The Testing Loop"
chapter: 7
lesson: 3
duration_minutes: 30
description: "Implement zero-trust debugging with exit codes and test data verification"
keywords:
  [
    "exit codes",
    "verification",
    "zero-trust",
    "debugging",
    "test data",
    "echo $?",
  ]

skills:
  - name: "Creating Test Data for Verification"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Testing"
    measurable_at_this_level: "Student creates test.txt with known expected output and uses it to verify script"

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
    assessment_method: "Student creates test file with known sum and verifies calc.py produces correct result"

  - objective: "Interpret exit codes to diagnose script failures"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student uses echo $? to check script success and can explain code meanings"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (exit codes, $? variable, test data, verification workflow, zero-trust philosophy, debugging loop) within A2 limit"

differentiation:
  extension_for_advanced: "Research other exit codes (127=command not found, 130=Ctrl+C), write verification script"
  remedial_for_struggling: "Focus only on: create test file with known answer, run script, compare result"
---

# The Testing Loop

Your script runs. No errors. No red text. The terminal returns to the prompt without complaint.

But here is the question that separates professionals from amateurs: **Did it produce the right answer?**

In Lesson 2, you built `calc.py`—a script that reads numbers from stdin and calculates their sum. You ran it, saw output, and moved on. But how do you know the sum was correct? You trusted the script because it ran without crashing. That trust is dangerous.

This lesson introduces the Zero-Trust Testing Loop—a verification workflow that catches bugs before they cost you money, reputation, or hours of debugging. By the end, you will never again assume a script works just because it ran.

## The Trap of Silent Success

Consider this scenario. You have a folder of expense receipts. You pipe them through your calculation script:

```bash
cat receipts/*.txt | python calc.py
# Output: Total: 847.50
```

You submit $847.50 for reimbursement. But the actual total was $947.50—one receipt had a formatting issue your script silently skipped. You are now $100 short, and worse, your finance team questions your attention to detail.

The script did not crash. It returned exit code 0 (success). It produced output. It was wrong.

This is why verification is Principle 3 in the Seven Principles: **"Verification as Core Step."** Never trust output—prove it.

## Creating Test Data with Known Answers

The verification loop starts with something radical: **test data where you already know the answer.**

Before running your script on real data, create a file where you can calculate the expected result by hand:

```bash
# Step 1: Create test data with a KNOWN answer
echo -e "10\n20\n30" > test.txt
```

Look at that file. Three numbers: 10, 20, 30. What is their sum?

You do not need a calculator. You do not need Python. **The sum is 60.**

This is your ground truth. When you run your script against this file, the only acceptable output is 60. Any other number means your script has a bug.

```bash
# Step 2: Run the script against test data
cat test.txt | python calc.py
# Output: Total: 60.00
```

The output matches your expectation. Now—and only now—can you begin to trust this script.

## Understanding Exit Codes

Every command in Bash produces two types of output:

1. **Standard output** (stdout): The text you see on screen
2. **Exit code**: A hidden number indicating success or failure

The exit code is stored in a special variable called `$?`. Check it immediately after any command:

```bash
# Run a successful command
cat test.txt | python calc.py
# Output: Total: 60.00

# Check the exit code
echo $?
# Output: 0
```

Exit code 0 means "the command ran without crashing." Any non-zero exit code indicates an error:

| Exit Code | Meaning                                     |
| --------- | ------------------------------------------- |
| 0         | Success—command completed without crashing  |
| 1         | General error—something went wrong          |
| 2         | Misuse of command—wrong arguments or syntax |
| 127       | Command not found—typo or missing program   |
| 130       | Interrupted by Ctrl+C                       |

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

Create a deliberately buggy script to see this:

```python
# buggy_calc.py - A script with a bug
import sys

total = 0
for line in sys.stdin:
    try:
        # BUG: Subtracting first number instead of adding
        if total == 0:
            total = float(line.strip())
        else:
            total -= float(line.strip())  # Wrong operation!
    except ValueError:
        pass

print(f"Total: {total:.2f}")
```

Run it against your test data:

```bash
cat test.txt | python buggy_calc.py
# Output: Total: -40.00
echo $?
# Output: 0
```

The exit code is 0. The script "succeeded." But -40 is catastrophically wrong—the correct answer is 60.

Exit codes catch crashes. They do not catch logic errors. **You must verify the output itself.**

## The Complete Verification Workflow

The Zero-Trust Testing Loop has four steps:

**Step 1: Create Test Data with Known Answer**

```bash
# Simple test case
echo -e "10\n20\n30" > test_simple.txt
# Expected: 60

# Edge case: single number
echo "42" > test_single.txt
# Expected: 42

# Edge case: includes zero
echo -e "5\n0\n5" > test_zero.txt
# Expected: 10
```

**Step 2: Run Script Against Test Data**

```bash
cat test_simple.txt | python calc.py
# Output: Total: 60.00
```

**Step 3: Check Exit Code**

```bash
echo $?
# Output: 0
```

**Step 4: Verify Output Matches Expectation**

Compare the output (60.00) to your pre-calculated answer (60). They match.

Only after passing all four steps should you run the script on real data.

## Multiple Test Cases Catch More Bugs

A single test is better than no tests. Multiple tests are better than one. Each test case probes a different potential failure:

```bash
# Test case 1: Basic addition
echo -e "1\n2\n3" > test1.txt
cat test1.txt | python calc.py
# Expected: 6.00
# Output: Total: 6.00 (PASS)

# Test case 2: Decimal precision
echo -e "0.1\n0.2" > test2.txt
cat test2.txt | python calc.py
# Expected: 0.30
# Output: Total: 0.30 (PASS)

# Test case 3: Large numbers
echo -e "1000000\n2000000" > test3.txt
cat test3.txt | python calc.py
# Expected: 3000000.00
# Output: Total: 3000000.00 (PASS)

# Test case 4: Negative numbers
echo -e "100\n-50" > test4.txt
cat test4.txt | python calc.py
# Expected: 50.00
# Output: Total: 50.00 (PASS)
```

Each test targets a specific concern:

- Test 1: Does basic addition work?
- Test 2: Does decimal handling work?
- Test 3: Does it handle large numbers without overflow?
- Test 4: Does it handle negative numbers?

## Debugging with the Verification Loop

When a test fails, the verification loop becomes your debugging workflow:

```bash
# Test fails!
cat test_decimals.txt | python calc.py
# Expected: 0.30
# Output: Total: 0.29 (FAIL - off by 0.01!)
```

Now you have actionable information:

- The script runs (exit code 0)
- The output is wrong (0.29 instead of 0.30)
- The error is small (0.01 difference)
- The error relates to decimal precision

This points you toward floating-point precision issues—a specific, debuggable problem.

Without test data, you might have used this script for months before noticing the accumulated 1-cent errors adding up to real money.

## The Zero-Trust Philosophy

Zero-trust debugging embodies a mindset: **Assume everything is broken until proven otherwise.**

This is especially critical when working with AI-generated code. When you ask an AI to write a calculation script, it will produce plausible-looking code. It might even explain confidently how it works. But the AI does not run the code. It does not verify the output. It does not know if the math is correct.

You must verify. Every time.

The workflow:

1. **AI generates code**: The script looks reasonable
2. **You create test data**: Numbers with known sums
3. **You run and verify**: Does output match expectation?
4. **You check exit codes**: Did the script crash silently?
5. **Trust is earned**: Only after verification

This applies to code from any source—AI, colleagues, Stack Overflow, or your past self at 2 AM. Trust is earned through verification, not granted through origin.

## Connecting to the Seven Principles

The Zero-Trust Testing Loop embodies two core principles:

**Principle 3: Verification as Core Step**

Every operation should be verified before trusting its output. The testing loop makes verification systematic and repeatable. You do not "check" your script—you prove it with test data.

**Principle 7: Observability**

Exit codes make program behavior visible. Without checking `$?`, errors hide in silence. With exit codes, failures announce themselves. Your debugging becomes data-driven rather than guess-driven.

These principles compound. Verification (P3) produces evidence. Observability (P7) makes that evidence accessible. Together, they create a debugging workflow that catches problems early and provides clear diagnostic information.

## Practice: Build Your Test Suite

Create a test suite for your `calc.py` script:

```bash
# Create test directory
mkdir -p ~/calc-tests
cd ~/calc-tests

# Test 1: Basic integers
echo -e "10\n20\n30" > test_basic.txt
# Expected: 60.00

# Test 2: Single number
echo "42" > test_single.txt
# Expected: 42.00

# Test 3: Decimals
echo -e "1.5\n2.5" > test_decimals.txt
# Expected: 4.00

# Test 4: Many numbers
echo -e "1\n2\n3\n4\n5\n6\n7\n8\n9\n10" > test_many.txt
# Expected: 55.00

# Test 5: Negative numbers
echo -e "100\n-25\n-25" > test_negative.txt
# Expected: 50.00

# Run all tests
for f in test_*.txt; do
    echo "Testing $f:"
    cat "$f" | python ~/calc.py
    echo "Exit code: $?"
    echo "---"
done
```

Run this suite every time you modify `calc.py`. If any test fails, you have caught a bug before it reached real data.

## Try With AI

### Prompt 1: Understanding Exit Codes

```
Explain what `echo $?` shows in Bash.

I ran a command and then typed `echo $?` and it showed `0`.
Then I ran a different command and `echo $?` showed `127`.

What do these numbers mean? What are common exit codes I should know about?
```

**What you are learning:** AI teaches the meaning of exit codes—the hidden status indicators that reveal whether commands succeeded or failed.

### Prompt 2: Exit Code Limitations

```
My Python script exits with code 0 but produces the wrong total.

The script runs without errors, `echo $?` shows 0, but when I check the
output against test data I calculated by hand, the number is wrong.

Why doesn't the exit code catch this? What's the difference between
"the script ran successfully" and "the script produced correct output"?
```

**What you are learning:** You teach AI (and reinforce for yourself) the critical distinction between "did not crash" and "produced correct results"—exit codes catch crashes, not logic errors.

### Prompt 3: Collaborative Debugging

```
Help me debug this script. It should sum numbers from stdin.

Here's my test: I created a file with 10, 20, 30 (one per line).
The expected sum is 60.
But my script outputs 50.

Here's the script:
[paste your script]

Walk me through how to find the bug using print statements
and test data verification.
```

**What you are learning:** Collaborative debugging where you provide the verification framework (test data with known answers) and AI helps identify where the logic diverges from expectation.
