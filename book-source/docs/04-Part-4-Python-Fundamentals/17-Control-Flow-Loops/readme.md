# Chapter 17: Control Flow and Loops

## Introduction

Programs don't just execute code in a straight line. They make decisions, repeat actions, and jump based on conditions. In this chapter, you'll learn how programs **control their flow**—how they choose between different paths and repeat code efficiently.

Control flow is the foundation of every program. Your email app decides whether to mark messages as spam. Your game decides when the player wins. Your banking app decides whether to approve a transaction. All of these require **conditionals** (making decisions) and **loops** (repeating actions).

By the end of this chapter, you'll be able to write programs that make decisions and automate repetitive tasks—the two core skills of programming.

## What You'll Learn

In this chapter, you'll master:

### Conditionals (Making Decisions)

- **Lesson 1: Understanding Decisions** — Recognize when programs need to make choices and how Boolean values (True/False) control behavior
- **Lesson 2: If and Else** — Write binary decisions (if this happens, do this; otherwise, do that)
- **Lesson 3: Multiple Choices with Elif** — Handle multiple possibilities with elif chains
- **Lesson 4: Nesting Conditions** — Combine conditions to test multiple requirements simultaneously

### Loops (Repeating Actions)

- **Lesson 5: For Loops Basics** — Repeat code a known number of times using for loops and range()
- **Lesson 6: While Loops** — Repeat code until a condition changes (and avoid infinite loops)
- **Lesson 7: Controlling Loops** — Exit loops early with break or skip iterations with continue

## Skills You'll Develop

By the end of this chapter, you'll be able to:

- Recognize real-world scenarios where programs need to decide or repeat
- Write conditional logic from plain English specifications with AI assistance
- Trace code mentally to predict program behavior
- Write for and while loops for different repetition patterns
- Prevent infinite loops and control loop behavior
- Use comparison and logical operators to test conditions
- Apply control flow to real problems with your AI partner

## Prerequisites

Before starting this chapter, make sure you understand:

- **Chapter 13: Introduction to Python** — How to execute code in the REPL
- **Chapter 15: Operators, Keywords, and Variables** — Comparison operators (>, <, ==, !=) and logical operators (and, or, not)
- **Chapter 16: Strings and Type Casting** — F-strings for output and type hints

## Context: Why Control Flow Matters

Control flow is the bridge between static data and dynamic behavior. With variables and data types (Chapters 13-16), you can store information. With control flow, you can act on that information.

Every real program needs:
1. **Conditionals** to make decisions based on data
2. **Loops** to process multiple items or repeat actions

This chapter teaches both, preparing you for data structures (Chapter 18) where you'll loop through lists, dictionaries, and sets to process real-world data.

## Learning Path

The chapter progresses from understanding to application:

1. **Lesson 1** — Foundation: Understand how conditions work
2. **Lessons 2-3** — Application: Write conditionals for decisions
3. **Lesson 4** — Complexity: Combine conditions for advanced logic
4. **Lesson 5** — Application: Write loops for fixed repetition
5. **Lesson 6** — Complexity: Write loops for condition-based repetition
6. **Lesson 7** — Mastery: Control loop behavior with break/continue

Each lesson builds on the previous, with heavy scaffolding and AI partnership throughout.

## How to Use This Chapter

**Read actively**: Don't just read the explanations. Predict what code will do BEFORE running it.

**Trace code**: Use the "mental execution" technique taught in each lesson to predict output.

**Use AI as a partner**: Each lesson includes "Try With AI" activities. Your AI helps you understand concepts and validate your code.

**Practice**: Write code for every example. Modify examples to test your understanding.

**Ask questions**: If you're unsure about a concept, use the "Try With AI" prompts to explore deeper.

## Key Concepts

### From Lessons 1-4 (Conditionals)

- **Boolean values** (True/False) — The foundation of all decisions
- **Comparison operators** (>, <, ==, !=, >=, <=) — Test relationships between values
- **if/else pattern** — Binary choice (two possible paths)
- **elif chains** — Multiple choices in sequence
- **Nesting** — Testing multiple conditions together
- **Indentation** — Python's way of marking code blocks

### From Lessons 5-7 (Loops)

- **for loops** — Repeat code N times when you know the count
- **range()** function — Generate numbers for loops
- **Loop variables** — Change each time through the loop
- **while loops** — Repeat code until a condition changes
- **Infinite loops** — The danger of loops that never stop
- **break and continue** — Control loop behavior dynamically

## Integration with Other Chapters

**Prepares You For:**
- **Chapter 18: Lists and Collections** — Loops iterate over lists to process data
- **Chapter 20: Functions** — Control flow inside functions
- **Chapter 21: Error Handling** — Conditionals in try/except blocks

**Builds On:**
- **Chapter 15: Operators** — Comparison and logical operators power conditions
- **Chapter 16: Type Casting** — Type hints in conditional code

## Challenge Yourself

By the end of this chapter, you should be able to write a program like this (from scratch with AI assistance):

```python
# Ask for a number between 1-10 until valid
attempts: int = 0
while True:
    user_input: str = input("Enter a number 1-10: ")
    attempts += 1

    if not user_input.isdigit():
        print("Please enter a number")
        continue

    number: int = int(user_input)
    if number < 1 or number > 10:
        print("Must be between 1-10")
        continue

    break

print(f"You entered {number} after {attempts} attempts")
```

This uses conditionals (if), loops (while), and loop control (continue, break)—all the skills from this chapter.

## Notes for Learners

- **Indentation is non-negotiable**: Python cares deeply about spacing. This takes practice.
- **Off-by-one errors**: `range(5)` gives 0-4, not 1-5. This trips up many beginners.
- **Infinite loops happen**: If your program freezes, you probably have an infinite loop. This is fixable.
- **Break vs Continue confuses everyone**: Use the decision framework in Lesson 7.

## Next Steps

After completing this chapter:

1. **Practice more**: Write loops for real problems (countdown, multiplication tables, etc.)
2. **Combine concepts**: Use conditionals INSIDE loops to filter or validate data
3. **Move to lists**: Chapter 18 teaches loops + lists together
4. **Ask your AI**: Use the "Try With AI" section in each lesson to explore variations

---

**Ready to start?** Begin with Lesson 1: Understanding Decisions.
