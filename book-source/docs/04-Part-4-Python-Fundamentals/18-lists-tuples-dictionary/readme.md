# Chapter 18: Lists, Tuples, and Dictionary

**Part 4: Python Fundamentals**
**Target Audience**: Intermediate learners (CEFR A2-B1)
**Prerequisites**: Chapters 1-17 (especially Ch 13: Python Intro, Ch 14: Data Types, Ch 17: Control Flow & Loops)
**Estimated Time**: 44 hours (11 lessons × 4 hours each)

---

## Chapter Overview

This chapter teaches Python's three foundational collection structures: **lists** (mutable sequences), **tuples** (immutable sequences), and **dictionaries** (key-value mappings). You'll learn when to use each structure, how to manipulate them effectively, and how to combine them in real-world applications.

By the end of this chapter, you'll build a complete **Data Processing Pipeline** that ingests CSV data, filters it with comprehensions, aggregates statistics with dictionaries, and outputs formatted reports—demonstrating how all three structures work together in production code.

---

## What You'll Learn

### Core Concepts (46+ unique concepts across 11 lessons)

**Lists** (Lessons 1-5):
- Creating and accessing lists with type hints
- Indexing, slicing, and length operations
- Mutation methods: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`
- Sorting and reversing: `sort()` vs `sorted()`, `reverse()` vs `[::-1]`
- List comprehensions with filtering
- Aliasing vs copying

**Tuples** (Lesson 6):
- Immutability as a design guarantee
- Single-element tuple syntax `(1,)`
- Unpacking for multiple assignment
- Using tuples as dict keys (hashable property)
- When to choose tuples over lists

**Dictionaries** (Lessons 7-9):
- Key-value mappings with union types
- CRUD operations: create, read, update, delete
- Safe access with `.get()` and `in` operator
- Iteration: `.keys()`, `.values()`, `.items()`
- Dict comprehensions for transformation
- Accumulator patterns for aggregation

**Architectural Thinking** (Lessons 10-11):
- Decision matrix: When to use which structure
- Performance implications (O(1) vs O(n))
- Mutability vs immutability trade-offs
- Integration patterns in real applications

---

## Learning Progression (CEFR A1 → A2 → B1)

This chapter follows a graduated complexity progression:

| Lessons | CEFR Level | Bloom's Taxonomy | Focus |
|---------|------------|------------------|-------|
| 1 | A1 (Foundation) | Understand | Recognition and explanation |
| 2-3 | A2 (Basic) | Apply | Guided practice with scaffolding |
| 4-6, 8 | A2-B1 (Transitional) | Apply/Analyze | Independent application |
| 5, 7, 9-11 | B1 (Intermediate) | Apply/Analyze/Create | Design thinking and integration |

**Cognitive Load Management**: Each lesson introduces **maximum 7 new concepts** (intermediate A2-B1 limit). Lesson 11 (Capstone) introduces **0 new concepts**, focusing purely on integration.

---

## Lesson Structure

### 1. Introduction to Collections
**File**: `01-introduction-to-collections.md`
**CEFR**: A1 | **Concepts**: 5 | **Duration**: 3.5-4 hours

Learn why Python has three collection types, what problems each solves, and when to use which. Introduces the foundational concepts: sequences, mappings, mutability, and type hints.

---

### 2. Lists Part 1 — Creation and Basic Operations
**File**: `02-lists-creation-and-basics.md`
**CEFR**: A2 | **Concepts**: 6 | **Duration**: 3.5-4 hours

Master list literals, type hints (`list[T]`), indexing (positive/negative), slicing, `len()`, and the critical difference between aliasing and copying.

---

### 3. Lists Part 2 — Mutability and Modification
**File**: `03-lists-mutability-and-modification.md`
**CEFR**: A2-B1 | **Concepts**: 7 | **Duration**: 3.5-4 hours

Deep dive into mutation methods: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`. Understand the distinction between methods (in-place) vs functions (return new).

---

### 4. Lists Part 3 — Sorting and Advanced Methods
**File**: `04-lists-sorting-and-advanced-methods.md`
**CEFR**: B1 | **Concepts**: 7 | **Duration**: 3.5-4 hours

Learn `sort()` vs `sorted()`, `reverse()` vs `[::-1]`, `count()`, `index()`, and `copy()`. Understand when to use in-place methods vs functional approaches.

---

### 5. List Comprehensions — Transforming Data
**File**: `05-list-comprehensions.md`
**CEFR**: B1 | **Concepts**: 6 | **Duration**: 3.5-4 hours

Master comprehension syntax `[expr for item in iterable if condition]`. Learn when comprehensions improve readability (vs when loops are clearer). Practice filtering and transformation patterns.

---

### 6. Tuples — Immutable Sequences
**File**: `06-tuples-immutable-sequences.md`
**CEFR**: A2-B1 | **Concepts**: 7 | **Duration**: 3.5-4 hours

Understand immutability as a design guarantee. Learn tuple literals, single-element syntax `(1,)`, unpacking, and using tuples as dict keys. Discover when immutability prevents bugs.

---

### 7. Dictionaries Part 1 — Key-Value Mappings
**File**: `07-dicts-key-value-basics.md`
**CEFR**: A2 | **Concepts**: 6 | **Duration**: 3.5-4 hours

Create dictionaries with union types (`dict[str, str | int]`), access values with bracket notation, use `.get()` for safe access, and check key existence with `in`.

---

### 8. Dictionaries Part 2 — CRUD Operations
**File**: `08-dicts-crud-operations.md`
**CEFR**: A2-B1 | **Concepts**: 7 | **Duration**: 3.5-4 hours

Perform Create, Read, Update, Delete operations on dictionaries. Learn `del`, `.pop()`, `.clear()`, `.keys()`, `.values()`, `.items()`. Master safe deletion patterns.

---

### 9. Dictionaries Part 3 — Iteration and Comprehensions
**File**: `09-dicts-iteration-and-comprehensions.md`
**CEFR**: B1 | **Concepts**: 7 | **Duration**: 3.5-4 hours

Iterate dictionaries with `.items()`, transform data with dict comprehensions, build accumulators for aggregation (word frequency, category counts), and work with nested dictionaries.

---

### 10. Choosing the Right Structure
**File**: `10-choosing-the-right-structure.md`
**CEFR**: B1 | **Concepts**: 7 (synthesis, no new) | **Duration**: 4-5 hours

Develop architectural thinking: decision matrix for choosing lists vs tuples vs dicts. Understand performance implications, mutability needs, and anti-patterns. Practice justifying structure choices.

---

### 11. Capstone — Data Processing Pipeline
**File**: `11-capstone-data-processing-pipeline.md`
**CEFR**: B1 | **Concepts**: 0 (integration only) | **Duration**: 4-5 hours

Build a complete data pipeline: ingest CSV → parse into `list[dict]` → filter with comprehensions → aggregate with dicts → output formatted report. Demonstrates all three structures working together.

---

## Learning Objectives (Aligned with CEFR & Bloom's Taxonomy)

By completing this chapter, you will:

1. **LO-001** (A2 - Understand): Explain the differences between lists, tuples, and dicts, and when to use each
2. **LO-002** (A2 - Apply): Create and manipulate lists with indexing, slicing, and mutation methods
3. **LO-003** (B1 - Apply): Choose the appropriate collection structure based on requirements (order, mutability, lookup)
4. **LO-004** (A2-B1 - Apply): Use list and dict methods correctly (`.append()`, `.pop()`, `.get()`, `.items()`)
5. **LO-005** (B1 - Apply): Write list and dict comprehensions for filtering and transformation
6. **LO-006** (B1 - Create): Build a complete data processing pipeline integrating all three structures
7. **LO-007** (B1 - Analyze): Debug collection-related errors with AI partnership (KeyError, IndexError, aliasing bugs)

---

## Success Metrics (Evals)

This chapter defines 10 measurable success criteria:

- **EVAL-001**: 75%+ identify correct structure for given scenario (quiz)
- **EVAL-002**: 70%+ write valid list comprehension with filter (exercise)
- **EVAL-003**: 80%+ use `.get()` vs bracket notation correctly (code review)
- **EVAL-004**: 70%+ explain aliasing vs copying with examples (written)
- **EVAL-005**: 75%+ choose tuple vs list with justification (scenario)
- **EVAL-006**: 80%+ build capstone pipeline (project submission)
- **EVAL-007**: 70%+ complete 10+ lesson sequence (engagement)
- **EVAL-008**: Grade 7-8 reading level maintained (Flesch-Kincaid)
- **EVAL-009**: 75%+ use type hints correctly (code examples)
- **EVAL-010**: 80%+ validate code with AI partnership (reflection)

---

## Prerequisites

**Required Knowledge** (from Chapters 1-17):
- Variables and type hints (Ch 13, 14)
- Basic data types: int, float, str, bool (Ch 14)
- Control flow: if/elif/else (Ch 17)
- Loops: for, while, range() (Ch 17)
- Type hints syntax (introduced in Ch 14)

**Not Required** (taught in later chapters):
- Functions (Ch 20) - Capstone uses complete examples for observation only
- Exceptions (Ch 21) - Basic error handling shown inline
- File I/O (Ch 22) - CSV data provided as strings
- OOP (Ch 24-26) - Not used

---

## Tools & Environment

**Python Version**: 3.14+ (modern type hints: `list[T]`, `dict[K,V]`, `X | None`)

**AI Companions**:
- **ChatGPT web** (recommended for beginners)
- **Claude Code CLI** (for intermediate learners)
- **Gemini CLI** (alternative)

**Testing**: All code examples validated on Python 3.14.0

---

## Pedagogical Approach

### AI-Native Learning Pattern (4 Steps)
1. **Describe intent** to your AI companion
2. **Explore** with AI-generated examples
3. **Validate** code correctness (run and test)
4. **Learn from errors** (debugging with AI)

### CoLearning Elements (Throughout)
- 💬 **AI Colearning Prompt**: Discussion questions for AI conversation
- 🎓 **Instructor Commentary**: Insights on professional practice
- 🚀 **CoLearning Challenge**: Extension exercises with AI partnership
- ✨ **Teaching Tip**: Claude Code workflow suggestions

### Graduated Teaching (Constitution Principle 13)
- **Book teaches foundations**: Core concepts explained directly (mutability, type hints, syntax)
- **AI companion explores**: Complex scenarios, edge cases, debugging
- **AI orchestration**: Capstone integration project (60-80 line pipeline)

---

## Technical Standards

**Type Hints**: Modern Python 3.10+ syntax
- ✅ `list[int]` (not `typing.List[int]`)
- ✅ `dict[str, int]` (not `typing.Dict[str, int]`)
- ✅ `tuple[int, int]` (not `typing.Tuple[int, int]`)
- ✅ `str | None` (not `typing.Optional[str]`)

**Code Quality**:
- All examples tested and runnable
- No hardcoded secrets or security anti-patterns
- Clear variable names (no single letters except loop counters)
- Consistent PEP 8 style

**Reading Level**: Grade 7-9 (average 9.0 Flesch-Kincaid, acceptable for intermediate learners)

---

## Chapter Philosophy

This chapter follows the **specification-first, evals-first** workflow:

1. **Evals defined first**: 10 success metrics before content outline
2. **Specification-driven**: Complete spec → plan → tasks → implement → validate
3. **Constitutional alignment**: 17 core principles applied rigorously
4. **Research-grounded**: CEFR, Bloom's, DigComp, Cognitive Load Theory
5. **Validation-before-trust**: All code tested, all claims verified

Students learn **architectural thinking** alongside syntax: not just "how to create a list," but "when is a list the right choice vs a tuple or dict?"

---

## Related Chapters

**Prerequisites**:
- Chapter 13: Introduction to Python
- Chapter 14: Data Types
- Chapter 17: Control Flow and Loops

**Next Steps**:
- Chapter 19: Sets, Frozen Sets, and Garbage Collection
- Chapter 20: Modules and Functions (learn to write `def` syntax)
- Chapter 21: Exception Handling (robust error handling)
- Chapter 22: I/O and File Handling (read/write CSV files)

**Integration**:
- Part 5: Spec-Driven Development (apply collections in projects)
- Part 10-13: AI-Native Development (collections in production systems)

---

## Validation Status

✅ **READY FOR PUBLICATION** (2025-11-09)

- All 11 lessons implemented and validated
- Code examples tested on Python 3.14.0
- CEFR proficiency progression verified
- Cognitive load limits enforced
- Constitutional alignment confirmed
- ADRs created for architectural decisions

**Validation Report**: See `specs/001-part-4-chapter-18/VALIDATION-REPORT.md` for complete details.

---

## Contact & Feedback

For questions, corrections, or feedback on this chapter:
- **Issues**: Report via project issue tracker
- **Discussions**: Community forum for pedagogical questions
- **Contributions**: Follow contribution guidelines in project root

---

**Ready to master Python collections?** Start with Lesson 1 and build your way to the capstone pipeline! 🚀
