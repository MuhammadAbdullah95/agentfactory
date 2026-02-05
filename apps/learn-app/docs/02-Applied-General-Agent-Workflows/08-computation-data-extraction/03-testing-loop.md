---
sidebar_position: 4
title: "The Testing Loop"
chapter: 8
lesson: 3
layer: L2
duration_minutes: 25
description: "Watch Claude Code verify its own work with test data, then learn why exit code 0 doesn't mean correct"
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
  - name: "Directing Verification Workflows"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Quality Assurance"
    measurable_at_this_level: "Student can direct Claude Code to verify script output against known test data"

  - name: "Understanding Exit Codes"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Debugging"
    measurable_at_this_level: "Student can explain why exit code 0 means 'didn't crash' not 'correct answer'"

  - name: "Zero-Trust Verification Pattern"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Apply"
    digcomp_area: "Critical Thinking"
    measurable_at_this_level: "Student applies the pattern: create known data, run script, compare to expected"

learning_objectives:
  - objective: "Direct Claude Code to create test data and verify script correctness"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student prompts agent to test sum.py with known-answer data"

  - objective: "Explain the difference between 'exit code 0' and 'correct output'"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can identify when a script runs successfully but produces wrong results"

  - objective: "Apply zero-trust verification to new scripts"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student uses verification pattern on a different calculation script"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (verification workflow, exit codes, test data, zero-trust mindset) within A2 limit"

differentiation:
  extension_for_advanced: "Research other exit codes (127=not found, 130=Ctrl+C), write automated test scripts"
  remedial_for_struggling: "Focus on the conversation pattern: 'verify this with test data where I know the answer'"
---

# The Testing Loop

The agent created sum.py. It ran without errors. You saw output. But here's the question that separates professionals from amateurs:

**Did it produce the right answer?**

Most people trust output because it appeared. No red text, no error messages, so it must be correct. This assumption has cost companies millions and caused countless bugs that lurked for months before discovery.

You're going to learn a different approach: Zero-Trust Verification. You don't trust output - you prove it.

## The Problem

You have sum.py from Lesson 2. You ran it:

```bash
cat expenses.txt | python sum.py
# Output: Total: 186.38
```

No errors. Exit code 0. Output appeared. But how do you know 186.38 is correct?

Maybe there's a bug that silently skips certain numbers. Maybe the floating-point math is wrong. Maybe the script works on your test data but fails on edge cases.

You need verification.

## The Conversation

Open Claude Code and ask for verification:

```
You: I have sum.py that sums numbers from stdin. I want to verify it works
correctly. Create test data with numbers I can add in my head - like 10, 20, 30
(expected: 60) - and verify the script produces the right answer.
```

Watch what Claude Code does:

```
Claude Code: Smart approach - verifying with known data. Let me create test
cases and check the results.

[Creates: test_simple.txt with contents: 10, 20, 30]

[Runs: cat test_simple.txt | python sum.py]
Total: 60.0

Result matches expected (60). Exit code: 0

Let me also test decimals to make sure float handling works:

[Creates: test_decimals.txt with contents: 10.5, 20.5, 19.0]

[Runs: cat test_decimals.txt | python sum.py]
Total: 50.0

Result matches expected (50). Exit code: 0

And negative numbers:

[Creates: test_negative.txt with contents: 100, -30, -20]

[Runs: cat test_negative.txt | python sum.py]
Total: 50.0

Result matches expected (50). Exit code: 0

All tests pass. The script handles:
✓ Simple integers
✓ Decimal numbers
✓ Negative numbers

Your sum.py is verified for these cases.
```

The agent didn't just run the script. It created test data with known answers, ran the script, and compared output to expectation.

## What Just Happened?

You witnessed **Principle 3: Verification as Core Step** in action.

The agent understood something crucial: you don't verify by hoping. You verify by creating situations where you already know the answer.

- Test data: 10, 20, 30
- Expected answer: 60 (you can add this in your head)
- Actual output: 60.0
- Verdict: Correct

If the script had output 40, you'd know immediately something was wrong. The test data made the bug visible.

### Why Exit Code 0 Isn't Enough

The agent checked exit codes, but notice it also compared output to expected values. Here's why both matter:

**Exit code 0** means: "The script ran without crashing."

It does NOT mean: "The script produced correct results."

A script can exit with code 0 and be completely wrong. Consider this buggy version:

```python
# buggy_sum.py - Has a silent bug
import sys

total = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    # BUG: Skipping lines that start with digits > 5
    if line[0] in '6789':
        continue  # Silent failure!
    total += float(line)

print(f"Total: {total}")
```

Run it:

```bash
echo -e "10\n60\n30" | python buggy_sum.py
# Output: Total: 40.0
# Exit code: 0
```

Exit code 0. No errors. But 40 is wrong - the answer should be 100. The script silently skipped "60" because it starts with '6'.

**Exit codes catch crashes. They don't catch logic errors.**

## The Agent's Toolkit: Exit Codes and $?

Every command in Bash produces an exit code. You can check it with `$?`:

```bash
# Run a command
cat test_simple.txt | python sum.py
# Output: Total: 60.0

# Check exit code
echo $?
# Output: 0
```

Common exit codes:

| Exit Code | Meaning |
|-----------|---------|
| 0 | Success - command completed without crashing |
| 1 | General error - something went wrong |
| 2 | Misuse of command - wrong arguments |
| 127 | Command not found - typo or missing program |
| 130 | Interrupted by Ctrl+C |

The agent ran `echo $?` after each test to confirm no crashes. But it also compared output to expected values - because exit code 0 alone doesn't prove correctness.

### Reading $? Immediately

Important: `$?` holds the exit code of the **most recent** command. If you run another command first, you'll get that command's exit code instead:

```bash
python sum.py < test.txt   # Run the script
echo "Done"                 # This overwrites $? with echo's exit code
echo $?                     # Shows 0 (from echo), not from sum.py!
```

Check `$?` immediately after the command you care about.

## The Pattern

Here's the verification prompt pattern:

```
"Verify [tool] works correctly. Create test data with a known answer [X]
and check that output matches."
```

This pattern works because:

1. **Known answer first.** You calculate the expected result before running the tool.
2. **Simple test data.** Numbers you can add in your head (10+20+30=60).
3. **Multiple cases.** Test integers, decimals, negatives, edge cases.
4. **Comparison.** Output must match expectation exactly.

### Pattern Variations

| What You're Testing | The Prompt |
|---------------------|------------|
| Sum script | "Verify sum.py with test data 10, 20, 30 (expected: 60)" |
| Average script | "Verify average.py with test data 10, 20, 30 (expected: 20)" |
| Max script | "Verify max.py with test data 10, 50, 30 (expected: 50)" |
| Filter script | "Verify filter.py keeps only numbers > 20 from 10, 30, 50 (expected: 30, 50)" |

The tool changes. The verification pattern stays the same.

## The Zero-Trust Philosophy

This approach embodies a mindset: **Assume everything is broken until proven otherwise.**

When you ask Claude Code to sum your expenses, it writes a script and runs it. The agent sees output. Exit code is 0. Everything looks fine.

But the agent cannot verify that $186.38 is correct for YOUR expenses unless it has test data with known answers. The agent ran code - it didn't validate business logic.

**You must verify. Every time.**

The workflow when using a General Agent:

1. **Agent generates and runs code** - Script executes, output appears
2. **You request verification** - "Test this with known data"
3. **Agent creates test cases** - Simple data with calculable answers
4. **Comparison proves correctness** - Output matches expectation

This applies to code from any source - your General Agent, colleagues, Stack Overflow, or your past self at 2 AM. Trust is earned through verification, not granted through origin.

## Try It Yourself

Ask Claude Code to verify a script with edge cases:

```
Verify sum.py handles these edge cases:
1. Empty file (expected: 0)
2. Single number: just "42.5" (expected: 42.5)
3. Numbers with extra whitespace
4. File with blank lines mixed in
```

Watch how the agent creates test data for each case and checks results.

**Expected behavior:**

- Empty file should output `Total: 0` or `Total: 0.0`
- Single number should work (not require multiple inputs)
- Whitespace should be stripped correctly
- Blank lines should be skipped

If any test fails, you've discovered a bug before it hit real data.

## Connecting to the Seven Principles

This lesson demonstrated two core principles:

**Principle 3: Verification as Core Step**

Every operation should be verified before trusting its output. The testing loop makes verification systematic and repeatable. You don't "check" your script - you prove it with test data.

**Principle 7: Observability**

Exit codes make program behavior visible. Without checking `$?`, errors hide in silence. But observability goes beyond exit codes - you made the script's correctness visible by comparing output to known answers.

These principles compound. Verification (P3) produces evidence. Observability (P7) makes that evidence accessible. Together, they create a debugging workflow that catches problems early.

---

## Try With AI

### Prompt 1: Discover Edge Cases

```
What edge cases might break a script that sums numbers from stdin?
Think about unusual inputs: empty files, non-numeric lines, very large
numbers, special characters. List cases I should test.
```

**What you're learning:** Defensive thinking. The agent helps you anticipate failure modes you might not have considered. This makes your verification more thorough.

### Prompt 2: Automate Verification

```
I have 5 test cases for sum.py. Help me write a simple bash script that
runs all tests and reports which passed and which failed. Each test should
compare actual output to expected output.
```

**What you're learning:** Test automation. Instead of manually running tests, you create a script that runs them all. This is how professionals ensure code stays correct over time.

### Prompt 3: Debug a Failure

```
My sum.py gives wrong output on this test:
- Input: 10, 60, 30
- Expected: 100
- Actual: 40

The script works fine on other inputs. Exit code is 0.
Help me find the bug. What could cause 60 to be skipped?
```

**What you're learning:** Root cause analysis. You present a specific failure with evidence (expected vs. actual). The agent helps you reason about what could cause that exact symptom. This is collaborative debugging at its best.
