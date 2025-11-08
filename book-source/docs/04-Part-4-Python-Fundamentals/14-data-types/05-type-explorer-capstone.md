---
title: "Building a Type Explorer — Capstone Integration"
chapter: 14
lesson: 5
duration_minutes: 50

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Integrating Core Data Types"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can build a complete program using all core types (int, float, str, bool, None) in a single project"

  - name: "Type Validation and Conversion"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can use isinstance() to validate types and handle conversion errors safely"

  - name: "AI-Guided Program Improvement"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can ask AI for code review, identify improvements, and apply feedback to extend a working program"

learning_objectives:
  - objective: "Build a working interactive program that demonstrates all core data types from Chapter 14"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Complete type explorer program that runs without errors and displays all five core types"

  - objective: "Apply type hints throughout a complete program to specify data intent"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Every function and variable in the type explorer includes appropriate type hints"

  - objective: "Use type validation techniques (isinstance(), type()) to explore type characteristics"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Program demonstrates type checking, type inspection, and truthy/falsy conversion"

  - objective: "Collaborate with AI to review, improve, and extend the type explorer"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student asks AI for code review, identifies at least two improvements, and applies one to their program"

cognitive_load:
  new_concepts: 6
  assessment: "6 new concepts (program integration, type validation, type conversion, error handling, function organization, AI code review) within B1 limit of 10 ✓"

differentiation:
  extension_for_advanced: "Add a user input section that converts strings to numbers safely. Create a function that asks the user for their age as text, converts it to int with error handling, and validates it's a reasonable age. Then extend the type explorer to demonstrate what happens when conversion fails."
  remedial_for_struggling: "Start with just 2 types (int and str). Build those functions first. Test them thoroughly. Then add one type at a time (float, bool, None). Celebrate each success before adding the next. Quality over speed."

# Generation metadata
generated_by: "lesson-writer v1.0"
source_spec: "specs/part-4-chapter-14/spec.md"
source_plan: "specs/part-4-chapter-14/plan.md"
created: "2025-11-08"
last_modified: "2025-11-08"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "1.0.0"
---

# Building a Type Explorer — Capstone Integration

## Welcome to Your Capstone Project

You've spent Lessons 1-4 learning Python's core data types one at a time:

- **Lesson 1**: Variables and type hints (the foundation)
- **Lesson 2**: Integers and floats (numbers)
- **Lesson 3**: Strings and booleans (text and decisions)
- **Lesson 4**: Collections awareness and None (everything else)

Now it's time to **integrate everything into a working program** that brings all these concepts together.

In this capstone lesson, you'll build an **interactive type explorer**—a program that demonstrates how each data type works, validates types, and shows why type hints matter. This is a real Python program (~70 lines) that you can run, modify, and extend.

By the end, you'll understand not just individual types, but how types work together in a complete program. You'll also learn how to collaborate with AI to review and improve your code.

---

## Project Overview: What Your Type Explorer Does

Your type explorer program will:

1. **Display each core type** with a clear example
2. **Show what `type()` returns** (type inspection)
3. **Validate types with `isinstance()`** (type checking)
4. **Demonstrate truthy/falsy conversion** (boolean context)
5. **Organize code in functions** (one function per type)
6. **Use type hints throughout** (specifications in code)

When you run it, you'll see output like:

```
Welcome to the Python Type Explorer!
Let's explore Python's core data types together.

=== Exploring Integer (int) ===
Example: age = 25
Type: <class 'int'>
Is this an int? True

=== Exploring Float (float) ===
[... and so on for each type]
```

The program teaches concepts through demonstration, not just explanation. **You'll learn by running it, understanding it, and then improving it with AI assistance.**

---

## Building the Type Explorer Step by Step

Here's the complete program you'll build. Don't panic if it looks long—we'll walk through each part and explain what's happening.

### Complete Type Explorer Program

```python
"""
Interactive Type Explorer
Demonstrates core data types: int, float, str, bool, None
Uses type hints to describe intent clearly
Validates types before operations
"""


def explore_integer() -> None:
    """Explore the int type with user."""
    print("\n=== Exploring Integer (int) ===")
    age: int = 25
    print(f"Example: age = {age}")
    print(f"Type: {type(age)}")
    print(f"Is this an int? {isinstance(age, int)}")


def explore_float() -> None:
    """Explore the float type with user."""
    print("\n=== Exploring Float (float) ===")
    temperature: float = 98.6
    print(f"Example: temperature = {temperature}")
    print(f"Type: {type(temperature)}")
    print(f"Is this a float? {isinstance(temperature, float)}")


def explore_string() -> None:
    """Explore the str type with user."""
    print("\n=== Exploring String (str) ===")
    name: str = "Alex"
    print(f"Example: name = '{name}'")
    print(f"Type: {type(name)}")
    print(f"Is this a string? {isinstance(name, str)}")


def explore_boolean() -> None:
    """Explore the bool type with user."""
    print("\n=== Exploring Boolean (bool) ===")
    is_student: bool = True
    print(f"Example: is_student = {is_student}")
    print(f"Type: {type(is_student)}")
    print(f"Is this a bool? {isinstance(is_student, bool)}")

    # Truthy/falsy demonstration
    print("\nTruthy/Falsy Examples:")
    print(f"bool(0) = {bool(0)}")  # False
    print(f"bool(1) = {bool(1)}")  # True
    print(f"bool('') = {bool('')}")  # False
    print(f"bool('hello') = {bool('hello')}")  # True


def explore_none() -> None:
    """Explore the None type with user."""
    print("\n=== Exploring None ===")
    value: None = None
    print(f"Example: value = {value}")
    print(f"Type: {type(value)}")
    print(f"Is this None? {value is None}")


def main() -> None:
    """Run the interactive type explorer."""
    print("Welcome to the Python Type Explorer!")
    print("Let's explore Python's core data types together.")

    explore_integer()
    explore_float()
    explore_string()
    explore_boolean()
    explore_none()

    print("\n=== Summary ===")
    print("You've now explored all core Python types:")
    print("  - int: Whole numbers (counting)")
    print("  - float: Decimal numbers (measuring)")
    print("  - str: Text (words and characters)")
    print("  - bool: True/False (decisions)")
    print("  - None: No value (placeholders)")


if __name__ == "__main__":
    main()
```

**Specification: Create an interactive program that demonstrates core data types using functions, type hints, and type validation techniques**

**AI Prompt Used:**
"Create a Python program that explores five core data types (int, float, str, bool, None). Use separate functions for each type. Each function should show an example, use type() to display the type, and use isinstance() to validate it. Include type hints for all functions. Organize code with a main() function."

**Generated Code:** [Complete code shown above]

**Validation Steps:**
- ✓ All five functions created (explore_integer, explore_float, explore_string, explore_boolean, explore_none)
- ✓ Each function has type hints (-> None)
- ✓ Each function uses type() and isinstance() to explore types
- ✓ All variables have type hints (age: int, temperature: float, etc.)
- ✓ main() function organizes execution
- ✓ Program includes docstrings for clarity
- ✓ Program runs without errors

---

## Code Walkthrough: Understanding Each Part

Let's break down the key sections and understand how they work together.

### Section 1: The Docstring and Imports

```python
"""
Interactive Type Explorer
Demonstrates core data types: int, float, str, bool, None
Uses type hints to describe intent clearly
Validates types before operations
"""
```

This is a **module docstring**. It explains what the entire program does. When someone (or an AI) reads this file, they immediately understand the purpose.

### Section 2: Function Structure and Type Hints

Each `explore_*` function follows the same pattern:

```python
def explore_integer() -> None:
    """Explore the int type with user."""
    # Function body
```

Let's decode this:

- **`def explore_integer()`** — Defines a function named `explore_integer`
- **`-> None`** — Type hint saying this function returns **nothing** (None)
- **`"""Explore the int type with user."""`** — Docstring explaining what the function does

When you see `-> None`, it means the function performs actions (like printing) but doesn't return a value.

### Section 3: Type Inspection and Validation

Inside each explore function, you'll see:

```python
age: int = 25
print(f"Example: age = {age}")
print(f"Type: {type(age)}")
print(f"Is this an int? {isinstance(age, int)}")
```

**What's happening:**

1. **`age: int = 25`** — Variable with type hint (from Lesson 1)
2. **`type(age)`** — Returns the actual type (from Lesson 2)
3. **`isinstance(age, int)`** — Checks if `age` is an int, returns True/False (from Lesson 2)

This demonstrates the three ways to work with types:

- **Type hints** tell you what you intend (specification)
- **`type()`** tells you what Python sees (inspection)
- **`isinstance()`** validates types before operations (validation)

### Section 4: Truthy/Falsy Demonstration

```python
print("\nTruthy/Falsy Examples:")
print(f"bool(0) = {bool(0)}")      # False
print(f"bool(1) = {bool(1)}")      # True
print(f"bool('') = {bool('')}")    # False
print(f"bool('hello') = {bool('hello')}")  # True
```

This shows **how Python converts different types to boolean**. From Lesson 3, you learned that in boolean contexts (like `if` statements), Python evaluates truthiness:

- `0` is falsy (means False)
- Any non-zero number is truthy (means True)
- Empty string `""` is falsy
- Non-empty string is truthy

### Section 5: main() Function and Entry Point

```python
def main() -> None:
    """Run the interactive type explorer."""
    print("Welcome to the Python Type Explorer!")
    # Call all explore functions
    explore_integer()
    explore_float()
    # ... etc

if __name__ == "__main__":
    main()
```

The `if __name__ == "__main__":` pattern is a Python idiom that means **"Only run this if I'm the main program, not if I'm imported as a module."**

This is professional practice: it lets other programs import your code without automatically running it.

---

## Running Your Type Explorer

### Step 1: Create the File

Create a new file called `type_explorer.py` in your text editor or IDE.

### Step 2: Copy the Complete Program

Copy the entire program from the "Complete Type Explorer Program" section above into your file.

### Step 3: Save and Run

Open a terminal and run:

```bash
python type_explorer.py
```

You should see output like:

```
Welcome to the Python Type Explorer!
Let's explore Python's core data types together.

=== Exploring Integer (int) ===
Example: age = 25
Type: <class 'int'>
Is this an int? True

=== Exploring Float (float) ===
Example: temperature = 98.6
Type: <class 'float'>
Is this a float? True

[... more output for str, bool, None]

=== Summary ===
You've now explored all core Python types:
  - int: Whole numbers (counting)
  - float: Decimal numbers (measuring)
  - str: Text (words and characters)
  - bool: True/False (decisions)
  - None: No value (placeholders)
```

### Step 4: Experiment and Modify

Now that it works, **modify it**:

- Change `age = 25` to `age = 100` and run again. Notice how the output updates.
- Change `name = "Alex"` to `name = "Your Name"` and run again.
- Try adding a new variable in one of the functions and use `isinstance()` to validate it.

This is how you learn programming: **make, run, modify, observe**.

---

## Integration Summary: How This Capstone Brings Everything Together

Let's see how each lesson's concepts show up in your type explorer:

### From Lesson 1: Variables and Type Hints

Every variable in the program uses type hints:

```python
age: int = 25
temperature: float = 98.6
name: str = "Alex"
is_student: bool = True
value: None = None
```

**Integration**: You're not just using type hints—you're using them consistently in a real program. Type hints are now **your standard way of declaring variables**.

### From Lesson 2: Integers and Floats, type() and isinstance()

Your program demonstrates:

```python
print(f"Type: {type(age)}")
print(f"Is this an int? {isinstance(age, int)}")
```

**Integration**: You're using `type()` and `isinstance()` for their intended purposes: inspection and validation.

### From Lesson 3: Strings and Booleans

Your string function shows:

```python
name: str = "Alex"
print(f"Example: name = '{name}'")
```

And your boolean function demonstrates truthy/falsy conversion:

```python
print(f"bool(0) = {bool(0)}")  # False
print(f"bool('hello') = {bool('hello')}")  # True
```

**Integration**: Types aren't isolated concepts—they interact. Empty strings are falsy. Non-empty strings are truthy. Numbers interact with boolean logic.

### From Lesson 4: Collections and None

Your None function shows:

```python
value: None = None
print(f"Is this None? {value is None}")
```

**Integration**: None is a real type that you'll use constantly as a placeholder value.

### New Integration: Function Organization

The capstone teaches a new pattern: **organizing code in functions**. Each explore function is focused on one type. The `main()` function orchestrates them. This is how real Python programs are structured.

---

## Common Questions About Your Type Explorer

**Q: Why does `explore_integer()` return `-> None`?**

A: It doesn't return a value; it just prints to the screen. The `-> None` type hint tells Python and AI collaborators, "Don't expect this function to give you back data. It performs actions (printing) instead."

**Q: What's the difference between `type()` and `isinstance()`?**

A: `type()` answers "What **is** this?" (returns the exact type). `isinstance()` answers "Is this **compatible with** X?" (returns True/False). You'll use both.

**Q: Why does the truthy/falsy section exist in the boolean function?**

A: Because `bool` is special. Unlike `int`, `float`, or `str`, booleans have a conversion function (`bool()`) that converts anything to True/False based on Python's truthiness rules. Understanding this is crucial for control flow (Lesson coming in Chapter 15).

**Q: Can I run this on Windows/Mac/Linux?**

A: Yes! Python 3.14+ works identically on all platforms. The `python type_explorer.py` command works the same everywhere.

---

## Try With AI

Now that you've built a working type explorer, let's collaborate with AI to review it, understand it deeper, and extend it.

**Using Claude Code, Gemini CLI, or ChatGPT (web):**

### Prompt Set

**Prompt 1: Code Review and Type Hints Validation**

Copy this prompt and paste it into your AI tool:

```
I built a Python program called a type explorer that demonstrates
core data types. Here's my program:

[Paste your complete type_explorer.py code here]

Review my code for:
1. Am I using type hints correctly everywhere?
2. What types am I demonstrating (int, float, str, bool, None)?
3. Are there any errors or issues?
4. Is the code well-organized?
```

**Expected outcome:** AI identifies correct type hint usage, confirms all five types are covered, and flags any syntax errors. You'll also get feedback on code clarity.

**Prompt 2: Explore Improvements and Extensions**

```
How could I improve my type explorer program? What additions
would help someone understand types better? Consider:

1. Could I add more examples for each type?
2. Could I demonstrate type conversions (like int("25"))?
3. Could I add error handling?
4. What operations could I show for each type?

What would be your top 3 recommendations for making this program
more educational?
```

**Expected outcome:** AI suggests concrete improvements like adding arithmetic operations for numbers, string methods for strings, or safe conversion examples. You'll get ideas for extending your program.

**Prompt 3: Type Conversion with Error Handling**

```
Add type conversion to my type explorer. Create a new function that:

1. Takes user input as a string
2. Attempts to convert it to an integer
3. Handles errors if conversion fails
4. Uses type hints and isinstance() validation

Show me a function I can add to my type explorer that demonstrates
safe type conversion.
```

**Expected outcome:** AI provides a function that converts strings to numbers safely using try/except (error handling). This teaches defensive programming—a real-world practice.

**Prompt 4: Reflection — Why Types Matter (Stretch)**

```
After building and running my type explorer, I'm thinking about
why types matter in Python. Help me understand:

1. What did I learn about types by building this program?
2. How does understanding types help me write better Python code?
3. How will type knowledge help me in Chapter 15 (Operators)?
4. When I work with AI assistants, why is knowing about types important?

Explain as if teaching a friend who just learned types.
```

**Expected outcome:** AI connects type concepts to broader programming principles. You'll see how understanding types is foundational for every Python concept that follows. This builds confidence for Chapter 15 (Operators).

### Safety & Ethics Note

When asking AI to improve your code, always understand what changes it suggests before copying them. Type exploration is foundational—take time to understand each change. If AI suggests something you don't recognize, ask "Explain this line by line" before using it. This builds your judgment about code quality, not just your ability to use AI.

### Next Self-Directed Variation

After working through these prompts:

1. **Build one improvement**: Pick one suggestion from Prompt 2 and add it to your type explorer
2. **Test it**: Run your modified program and see the new behavior
3. **Document it**: Add a comment explaining what your new feature does
4. **Reflect**: Ask your AI: "Does this addition help teach types better? Why or why not?"

This practice turns you from someone following instructions into someone **designing educational code**. That's the capstone skill: creating programs that teach concepts, not just executing pre-written code.

