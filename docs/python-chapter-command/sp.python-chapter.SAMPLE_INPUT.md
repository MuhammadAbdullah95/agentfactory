---
title: Python Chapter Design Command - Sample Input Template (v2.0)
description: Example inputs for /sp.python-chapter command invocation with technical review workflow
date: 2025-11-08
updated: 2025-11-08
status: Updated for mandatory technical reviews, Python 3.14.0, type hints as core
---

# `/sp.python-chapter` — Sample Input Template

This document shows example inputs you can provide when invoking the Python chapter design command.

You can provide context **inline in your prompt** OR **interactively via Q&A**. Both work equally well.

---

## CRITICAL: Technical Review Workflow (v2.0)

**NEW** — This version includes mandatory technical reviews:

1. **After `/sp.plan` + `/sp.tasks`**: Review plan.md/tasks.md for structure and pedagogy
2. **After lesson-writer completion**: Run technical-reviewer subagent for validation
3. **PASS verdict required**: Before publishing to production

**Command automatically suggests**:
```
After plan complete:
→ Review plan.md for proficiency progression (A1→A2→B1 CEFR levels)

After tasks complete:
→ Review tasks.md for acceptance criteria and dependencies

After all lessons written:
→ /invoke technical-reviewer chapter-${N}
→ Validation checks:
  ✓ Python 3.14.0 (not 3.13)
  ✓ Type hints in ALL code
  ✓ "Try With AI": 4 prompts + Expected outcome
  ✓ No gatekeeping/dual-path comments
  ✓ Metadata consistency
→ PASS = publication ready
→ FAIL = fix and re-review
```

---

## Two Input Styles

### Style A: Inline Context (All Context in Prompt)
Provide your context directly in the prompt. Command reads it and processes immediately, then initiates automatic review gates.

### Style B: Interactive Q&A (Context via Responses)
Command asks 4 questions. You respond with your context. Same result, different interaction style. Review gates triggered automatically after each phase.

---

## Quick Start: Two Input Styles

### Style A: Inline Context (Recommended)

**You type:**
```
/sp.python-chapter ch-13-intro-python

Write Chapter 13: Introduction to Modern Python in Part 4

Core Context & Guiding Philosophy:

This chapter must reflect modern AIDD principles:
- AI-Driven Learning: Students use Claude Code or Gemini CLI as coding partners
- Focus on reasoning and problem-solving, NOT syntax memorization
- AIDD-First: Clarify what you want BEFORE writing code
- Validation-First: Test understanding, not just memorize

Existing Teaching Materials - This is old reference review and get the best ignore irrelevat aspects:
@context/13_chap12_to_29_specs/Lesson_01_Introduction_to_Python.md
@context/13_chap12_to_29_specs/readme.md

Additional Guidance:
- Target: Absolute beginners (no coding experience)
- Scope: Introduction fundamentals only (not Chapter 14's Data Types)
- Length: 3-4 lessons maximum
- Emphasis: Your first Python program + AIDD thinking
```

**Command processes:**
1. Extracts chapter 13
2. Reads chapter-index.md → "Introduction to Python"
3. Parses your guiding philosophy
4. Identifies materials: Lesson_01_Introduction_to_Python
5. Understands guidance: beginners, fundamentals, 3-4 lessons
6. Asks 4 questions **informed by your context**
7. Generates spec/plan/tasks respecting your philosophy

---

### Style B: Interactive Q&A

**You type:**
```bash
/sp.python-chapter 13
```

**Command responds:**
```
Reading specs/book/chapter-index.md...
Found: Chapter 13 - "Introduction to Python"

Checking context/13_chap12_to_29_specs/...
Found: Lesson_01_Introduction_to_Python materials

Q1: Who are we teaching?
```

**You respond:**
```
Absolute beginner — no coding experience
```

**Command continues:**
```
Q2: What's the ONE core focus for THIS chapter?
```

**You respond (with guiding philosophy):**
```
Introduction to modern Python with AIDD thinking:
- Use Claude Code or Gemini CLI as partners
- Focus on reasoning, not syntax memorization
- Apply specification-first thinking
- Practice validation-first learning
```

[Continue with Q3 and Q4...]

---

## Detailed Example: Chapter 13 (Style A: Inline Context)

---

## Sample User Responses (Copy & Adapt)

### Response Template for Q1: Target Audience

**Question**: "Who are we teaching?"

**Sample Response (Absolute Beginner)**:
```
Absolute beginner — no coding experience, might be nervous about Python
```

**Sample Response (Beginner with Some Coding)**:
```
Beginner with some coding — tried JavaScript, ready to learn Python specifically
```

**Sample Response (Intermediate)**:
```
Intermediate — comfortable with basic programming, wants Python depth
```

---

### Response Template for Q2: Core Focus for THIS Chapter

**Question**: "What's the ONE core focus for THIS chapter?"

**For Chapter 13 (Introduction to Python)**:
```
Just the basics: Python syntax, how to write and run code, your first program
```

Alternative:
```
Core: Introduction concepts + basic data (strings, numbers)
```

**For Chapter 14 (Data Types)**:
```
Data types focus: int, float, str, bool, type system in Python 3.13+
```

**For Chapter 17 (Control Flow and Loops)**:
```
Control flow: if/elif/else, for loops, while loops, break/continue
```

**For Chapter 20 (Module and Functions)**:
```
Functions: defining functions, parameters, return values, scope
```

---

### Response Template for Q3: What Can Students BUILD

**Question**: "What can students actually BUILD after THIS chapter?"

**For Chapter 13 (Introduction)**:
```
A simple Python script: "Hello, World!" and a script that asks for their name and greets them
```

Alternative:
```
Write and run their first Python program that demonstrates basic syntax
```

**For Chapter 14 (Data Types)**:
```
A script that stores information (name, age, email) and displays it back to the user
```

**For Chapter 17 (Control Flow)**:
```
A simple game or quiz that uses if/else logic and loops
```

**For Chapter 20 (Functions)**:
```
A calculator function that takes two numbers and returns their sum/product
```

---

### Response Template for Q4: Context Materials to Use

**Question**: "From context materials, which aspects fit THIS chapter?"

**Option A: Use Existing Context**:
```
Yes, use existing materials:
- Use the lesson structure from Lesson_01_Introduction_to_Python.md
- Use the code examples provided
- Use the learning outcomes already identified
- Build on the "Try It" exercises from context
```

**Option B: Selective Use**:
```
Yes, but selectively:
- Use code examples from Lesson_01_Introduction_to_Python
- Skip the advanced concepts
- Keep the "What it is" explanations clear
- Adapt the exercises for absolute beginners
```

**Option C: Start Fresh**:
```
No, start fresh:
- Create new lesson structure
- Use Python 3.13+ best practices
- Design exercises for [your target audience]
- Build toward [specific outcome]
```

---

## Full Sample Invocation (Chapter 13)

### You Invoke
```
/sp.python-chapter 13
```

### Command Processes (Internally)
- Reads chapter-index.md → Gets "Introduction to Python"
- Checks context folder → Finds Introduction lesson materials
- Asks you 4 questions

### You Respond (Complete Example)

**Q1: Who are we teaching?**
```
Absolute beginner — no coding experience. They're nervous about Python but motivated to learn.
```

**Q2: What's the ONE core focus for THIS chapter?**
```
Just introduction: getting Python installed, understanding what code is, writing first program.
Don't add data types — that's Chapter 14.
```

**Q3: What can they BUILD after?**
```
By the end, they should write and run their first Python script that:
1. Displays "Hello, World!"
2. Asks for their name
3. Prints a personalized greeting

That's their success criterion.
```

**Q4: From context materials, what fits?**
```
Yes, use the existing Lesson_01_Introduction_to_Python materials:
- Keep the lesson structure
- Use the provided code examples
- Adapt for absolute beginners (simpler language)
- Include the "Try It" hands-on activities
- Keep it short (not overwhelming)
```

---

## Command Output

After your responses, the command generates:

```
specs/part-5-chapter-13/
├── spec.md
│   ├─ Chapter title: "Introduction to Python"
│   ├─ Target audience: Absolute beginner
│   ├─ Core focus: Introduction basics
│   ├─ Success criteria: Can write & run first program
│   ├─ Learning objectives: 3-4 testable outcomes
│   ├─ Concepts taught: ~5 (within beginner limit)
│   └─ Lesson structure: 2-3 lessons
│
├── plan.md
│   ├─ Lesson 1: [Introduction to Python concept]
│   │   ├─ What it is
│   │   ├─ Code idea
│   │   ├─ Try it (hands-on)
│   │   └─ Why it matters (AIDD thinking)
│   │
│   ├─ Lesson 2: [Next concept]
│   │   └─ [Same structure]
│   │
│   └─ Code examples with pedagogical purpose
│
└── tasks.md
    ├─ Implementation checklist
    ├─ Acceptance criteria per lesson
    └─ Validation steps
```

---

## Sample Invocations for All Chapters

### Chapter 12: Python UV (Package Manager)
```
/sp.python-chapter 12
→ Q2 Response: "Just Python UV package manager basics — how to create environments and install packages"
→ Q3 Response: "Students can create a Python environment and install a package using UV"
```

### Chapter 14: Data Types
```
/sp.python-chapter 14
→ Q2 Response: "Data types: int, float, str, bool with type hints (`: int`, `: str`). How Python stores info with modern syntax"
→ Q3 Response: "Build a script that stores user data with type hints and displays it using f-strings"
```

### Chapter 17: Control Flow and Loops
```
/sp.python-chapter 17
→ Q2 Response: "Control flow: if/elif/else statements and for/while loops"
→ Q3 Response: "Build a simple quiz game that uses if/else and loops"
```

### Chapter 20: Module and Functions
```
/sp.python-chapter 20
→ Q2 Response: "Functions: defining, calling, parameters, return values, scope"
→ Q3 Response: "Write functions that calculate (sum, average) and reuse them in a program"
```

### Chapter 24: Object-Oriented Programming Part I
```
/sp.python-chapter 24
→ Q2 Response: "OOP basics: classes, objects, attributes, methods. How to organize code with OOP"
→ Q3 Response: "Create a simple class (like Dog or Car) with attributes and methods"
```

---

## Key Guidelines When Providing Input

### ✅ DO:
- **Be specific** about target audience (absolute beginner, beginner, intermediate)
- **Pick ONE focus** (don't add extras)
- **Describe real outcomes** (what they'll actually build)
- **Reference context** (if you want to use existing materials)
- **Honor chapter boundaries** (don't pull Ch 14 content into Ch 13)

### ❌ DON'T:
- **Override chapter title** (it's from chapter-index.md)
- **Add unrelated concepts** (stick to the chapter's focus)
- **Require future chapters** (outcome must use THIS chapter only)
- **Cross boundaries** (don't mix Ch 13 + Ch 14 content)
- **Assume complexity** (let the command ask, then you answer)

---

## Example: What NOT To Do

### ❌ Bad Input (Too Broad)
```
Q2 Response: "Introduction to Python, plus data types, plus functions, plus OOP"
→ Command rejects: "Too many concepts. Pick ONE focus."
```

### ❌ Bad Input (Forward Reference)
```
Q3 Response: "Students will build a Django web app"
→ Command rejects: "Requires knowledge from Ch 30+ (frameworks). Build using Ch 13 concepts only."
```

### ❌ Bad Input (Vague Outcome)
```
Q3 Response: "Students understand Python"
→ Command rejects: "Not testable. What BUILDS do they make?"
```

---

## Real Workflow Example

### You Type:
```
/sp.python-chapter 13
```

### Command Responds:
```
Reading specs/book/chapter-index.md, Part 5...
Found: Chapter 13 - "Introduction to Python"

Checking context/13_chap12_to_29_specs/...
Found: Lesson_01_Introduction_to_Python.md
Found: Lesson_01_Introduction_to_Python.ipynb

Now I have 4 questions to design this chapter:

Q1: Who are we teaching? (pick ONE)
  - Absolute beginner (no coding)
  - Beginner (some coding)
  - Intermediate (comfortable with basics)
```

### You Respond:
```
Absolute beginner — no coding experience, might be nervous.
```

### Command Continues:
```
Q2: What's the ONE core focus for THIS chapter?
  (Remember: Don't pull in Ch 14 "Data Types" or Ch 20 "Functions")
```

### You Respond:
```
Just introduction: Python syntax, how to write code, first program.
```

### Command Continues:
```
Q3: What can students BUILD after THIS chapter?
  (Must be doable with Ch 13 concepts alone)
```

### You Respond:
```
A script that asks for their name and prints a greeting.
```

### Command Continues:
```
Q4: From context (Lesson_01_Introduction_to_Python), what fits?
```

### You Respond:
```
Yes, use it. Keep lesson structure, use examples, adapt for absolute beginners.
```

### Command Generates:
```
✅ Creating specs/part-5-chapter-13/spec.md
✅ Creating specs/part-5-chapter-13/plan.md
✅ Creating specs/part-5-chapter-13/tasks.md

CRITICAL VALIDATION:
✓ All concepts in Chapter 13 (not Ch 14+)
✓ No prerequisite violations
✓ Chapter title matches chapter-index.md
✓ Scope matches your intent
✓ Context was filtered appropriately

Ready for lesson writer! 🚀
```

---

## Copy-Paste Template

Use this template when responding to the command:

```
Q1: Who are we teaching?
[YOUR ANSWER]

Q2: What's the ONE core focus for THIS chapter?
[YOUR ANSWER - Single focus only]

Q3: What can students BUILD after?
[YOUR ANSWER - Testable outcome using THIS chapter's concepts]

Q4: From context materials, what fits?
[YOUR ANSWER - Use existing / Use selectively / Start fresh]
```

---

## Questions?

- **"Can I include concepts from Chapter 14?"**
  No — respect chapter boundaries. Chapter 13 teaches Introduction only.

- **"Can I skip context materials and start fresh?"**
  Yes — Q4 option: "Start fresh" is always available.

- **"Can I make the chapter more advanced?"**
  Yes — adjust Q1: Pick "Intermediate" instead of "Absolute beginner"

- **"What if the outcome is too complex?"**
  Simplify Q3: Make it testable using ONLY this chapter's concepts.

---

## v2.0 Updates (Nov 8, 2025)

**Technical Review Integration**
- Mandatory technical-reviewer subagent after lesson-writer completion
- PASS verdict required before publication
- Catches metadata contradictions, consistency issues early
- Prevents rework of multiple lessons

**Python 3.14.0 Standard**
- All examples use latest stable release from https://www.python.org/downloads/
- No version inconsistencies across chapters

**Type Hints as Core**
- Type hints in ALL code examples (not optional)
- Treated as specifications: `name: str` documents intent
- Essential for AIDD and AI-native thinking
- Integrated from Chapter 13 onwards

**"Try With AI" Format**
- Exactly 4 prompts per lesson (not 3, not 5)
- Each includes "Expected outcome"
- Consistent student experience across all chapters
- Progressive complexity: Concept → Application → Synthesis → Why It Matters

**Rules 6 & 7 Integration**
- Rule 6: Troubleshooting is AI partnership (ask "What does this mean?" not memorize)
- Rule 7: Standardized "Try With AI" format (4 prompts, Expected outcome, final substantive section)
- Scales better than traditional guides
- Honors professional development practices

**CEFR Proficiency Progression**
- A1 (Recognition) → A2 (Simple Application) → B1 (Independent Application)
- International standard (40+ countries, 40+ languages)
- Enables portable credentials and institutional integration

---

**Ready to design a Python chapter? Pick a chapter number (12-29) and invoke:**
```bash
/sp.python-chapter ${N}
```

**The command will**:
1. Extract chapter metadata from chapter-index.md
2. Ask you 4 context questions
3. Auto-run `/sp.specify` → `/sp.plan` → `/sp.tasks`
4. Suggest technical reviews at each gate
5. After lesson-writer completion, require technical-reviewer PASS verdict
6. Deliver publication-ready content

**All chapters automatically receive**:
- ✅ Python 3.14.0 standard
- ✅ Type hints as core feature
- ✅ "Try With AI" format (4 prompts, Expected outcome)
- ✅ CEFR A1/A2/B1 proficiency progression
- ✅ Bloom's cognitive taxonomy alignment
- ✅ DigComp digital competence mapping
- ✅ Technical review validation
- ✅ Constitutional alignment (100%)

**No manual quality gates needed. Reviews are built-in.**
