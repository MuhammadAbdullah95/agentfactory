---
sidebar_position: 5
title: "Axiom V: Types Are Guardrails"
chapter: 14
lesson: 5
duration_minutes: 25
description: "Type systems prevent errors before they happen. In the AI era, types give AI a specification to generate against and catch hallucinations at compile time."
keywords: ["type safety", "Python type hints", "Pydantic", "Pyright", "dataclasses", "type checking", "AI code generation", "guardrails"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Python Type Annotation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can annotate Python functions with correct type hints including parameters, return types, and container types"

  - name: "Type-Driven AI Collaboration"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can explain how type annotations constrain AI-generated code and identify type errors in AI output before execution"

  - name: "Boundary vs Internal Type Design"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can distinguish when to use dataclasses (internal types) vs Pydantic models (boundary validation) and justify the choice"

learning_objectives:
  - objective: "Annotate Python functions and data structures with complete type hints"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student can write a function with typed parameters, return type, and generic container types that passes Pyright strict mode"

  - objective: "Explain why types matter more in AI-assisted development than in traditional coding"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can identify three specific failure modes that types prevent in AI-generated code (hallucinated methods, wrong return types, interface mismatches)"

  - objective: "Choose between dataclasses and Pydantic models based on the type's role in the system"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Given a set of data structures, student can correctly classify each as internal (dataclass) or boundary (Pydantic) and explain the trade-offs"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (type hints, Pyright strict mode, Pydantic validation, dataclass vs Pydantic distinction, generics/protocols, the Any anti-pattern) within comfortable A2-B1 range (5-7)"

differentiation:
  extension_for_advanced: "Implement a Protocol-based plugin system where AI generates new plugins that must satisfy the Protocol interface, demonstrating how structural typing constrains AI output without inheritance."
  remedial_for_struggling: "Focus on annotating a single function with basic types (str, int, list[str]) and running Pyright to see the error messages. Build confidence with simple types before introducing Pydantic or generics."
---

# Axiom V: Types Are Guardrails

You ask your AI assistant to write a function that fetches user profiles from an API. It generates clean, readable code. The variable names make sense. The logic looks right. You run it and get a cryptic error: `AttributeError: 'dict' object has no attribute 'email'`. The function returns a dictionary, but your code treats it like an object with attributes. The AI hallucinated an interface that doesn't exist.

Now imagine the same scenario, but with type annotations. You defined `UserProfile` as a dataclass with an `email: str` field. You typed the function's return as `UserProfile`. Before you even ran the code, your type checker flagged the error: the API function returns `dict[str, Any]`, not `UserProfile`. The hallucination was caught at development time, not at runtime in front of users.

This is the difference types make. In traditional development, types prevent human mistakes. In AI-assisted development, types prevent something more dangerous: **confident errors from a system that never doubts itself**.

## The Problem Without This Axiom

Without type annotations, AI-generated code operates in a world of implicit assumptions:

- A function returns "something"---but what shape is that something?
- A parameter accepts "data"---but what structure does that data have?
- A method exists on an object---but does it really, or did the AI invent it?

When humans write untyped code, they usually have mental models of what each variable contains. When AI writes untyped code, it has **token probabilities**---patterns that look plausible but may not correspond to reality. The AI doesn't know your codebase. It doesn't know which methods actually exist on your objects. It generates what *looks* right based on training data.

Without types, the only way to catch these errors is to run the code and observe failures. That means:
- Errors surface late (runtime, not development time)
- Errors are cryptic (`NoneType has no attribute 'items'`)
- Errors may be silent (wrong value, correct type---no crash, just wrong behavior)
- Each fix triggers another AI generation cycle, compounding the problem

Types shift error detection from runtime to development time. They turn implicit assumptions into explicit contracts. And critically, they give AI a **specification to generate against**---not a vague intent, but a precise description of what goes in, what comes out, and what's guaranteed.

## The Axiom Defined

> **Axiom V: Types Are Guardrails.** Type systems prevent errors before they happen. In the AI era, types are essential because they give AI a specification to generate against and catch hallucinations at compile time.

Types are not bureaucracy. They are not "extra work for no benefit." They are the **code-level equivalent of a specification**---a machine-verifiable contract that constrains what valid code looks like.

When you write `def get_user(user_id: int) -> UserProfile`, you have stated:
- **What goes in**: an integer (not a string, not a UUID object, not None)
- **What comes out**: a UserProfile (not a dict, not None, not a tuple)
- **What's guaranteed**: if this function returns without raising, you have a valid UserProfile

This contract is enforced by the type checker before your code ever runs. No test needed. No manual review needed. The machine verifies it automatically, every time.

## From Principle to Axiom

In Chapter 4, you learned **Principle 6: Constraints and Safety**---the insight that boundaries enable capability. You saw how permission models, sandboxing, and approval workflows create the safety that lets you give AI more autonomy. The paradox: **more constraints lead to more freedom**, because you trust the system enough to let it operate.

Axiom V applies the same insight at the code level:

| Principle 6 (Workflow Level) | Axiom V (Code Level) |
|------------------------------|----------------------|
| Permission models constrain AI actions | Type annotations constrain AI-generated code |
| Sandbox environments isolate risk | Type checkers isolate errors before execution |
| Destructive operations require approval | Type mismatches require correction before running |
| Trust builds through verified safety | Trust builds through verified type correctness |

Principle 6 says "don't let AI delete files without permission." Axiom V says "don't let AI return a `dict` where a `UserProfile` is expected." Both are guardrails. Both prevent damage. Both enable confident collaboration by making boundaries explicit and machine-enforced.

The constraint is the same: **explicit boundaries, automatically enforced, enabling greater autonomy**. At the workflow level, this is permissions and sandboxing. At the code level, this is types and type checking.

## Types in Python: The Discipline Stack

Python is dynamically typed---it doesn't require type annotations. But "doesn't require" doesn't mean "shouldn't have." Python's type system is opt-in, and the return on that opt-in is enormous.

The Python type discipline stack has three layers, each building on the last:

### Layer 1: Type Hints (The Annotations)

Type hints are Python's built-in syntax for declaring types:

```python
from dataclasses import dataclass


def calculate_total(prices: list[float], tax_rate: float) -> float:
    """Calculate total price with tax applied."""
    subtotal = sum(prices)
    return subtotal * (1 + tax_rate)


@dataclass
class Task:
    title: str
    description: str
    priority: int
    completed: bool = False

    def mark_complete(self) -> None:
        self.completed = True
```

Type hints alone don't enforce anything at runtime---Python ignores them during execution. But they serve two critical purposes:

1. **Documentation that never goes stale**: Unlike comments, type hints are part of the code structure. They can't drift from reality without the type checker flagging it.
2. **Machine-readable specification**: Type checkers and AI systems can read these annotations to understand what code expects and provides.

### Layer 2: Pyright in Strict Mode (The Enforcer)

Pyright is a static type checker that reads your annotations and finds errors before you run anything. In strict mode, it requires complete annotations and catches subtle bugs:

```python
# pyright: strict

def process_tasks(tasks: list[Task]) -> list[str]:
    """Return titles of completed tasks."""
    results: list[str] = []
    for task in tasks:
        if task.completed:
            results.append(task.title)
    return results


# Pyright catches this error BEFORE runtime:
def bad_example(tasks: list[Task]) -> list[str]:
    results = []
    for task in tasks:
        # Error: "priority" is int, not str
        # Cannot append int to list[str]
        results.append(task.priority)  # Type error caught!
    return results
```

To enable Pyright strict mode, add a `pyrightconfig.json` to your project:

```json
{
  "typeCheckingMode": "strict",
  "pythonVersion": "3.12"
}
```

Strict mode means Pyright will reject:
- Functions without return type annotations
- Variables with ambiguous types
- Operations that might fail on certain types
- Missing None checks for optional values

### Layer 3: Pydantic (The Validator)

Pydantic adds **runtime validation** on top of static types. Where Pyright catches errors at development time, Pydantic catches errors when external data enters your system:

```python
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    """Validates incoming API request data."""

    title: str = Field(min_length=1, max_length=200)
    description: str = Field(default="")
    priority: int = Field(ge=1, le=5)


# Pydantic validates at runtime:
try:
    task = TaskCreate(title="", priority=10)
except Exception as e:
    # ValidationError:
    # title: String should have at least 1 character
    # priority: Input should be less than or equal to 5
    print(e)


# Valid data passes through cleanly:
task = TaskCreate(title="Deploy feature", priority=3)
print(task.title)  # "Deploy feature" - validated and typed
```

The three layers work together:

| Layer | What It Does | When It Catches Errors |
|-------|-------------|----------------------|
| Type Hints | Declare contracts | Never (documentation only) |
| Pyright | Verify contracts statically | Development time (before running) |
| Pydantic | Validate data at boundaries | Runtime (when data arrives) |

## Types and AI: Why They're Non-Negotiable

Here is the core insight of this axiom: **Types matter more with AI-generated code than with human-written code.** Here's why.

### AI Hallucination: Methods That Don't Exist

AI can confidently generate calls to methods that don't exist on your objects:

```python
# AI generates this (looks reasonable):
def get_active_tasks(manager: TaskManager) -> list[Task]:
    return manager.get_active()  # Does this method exist?


# With types, Pyright catches it immediately:
# Error: "TaskManager" has no attribute "get_active"
# Did you mean "get_tasks"?
```

Without types, this error only surfaces at runtime. With types, it surfaces the instant the AI generates the code.

### AI Confusion: Wrong Return Types

AI can misunderstand what a function should return:

```python
# You asked for "a function that finds a user by email"
# AI generates:
def find_user(email: str) -> dict[str, str]:
    # Returns a dictionary...
    return {"name": "Alice", "email": email}


# But your codebase expects:
def find_user(email: str) -> User | None:
    # Returns a User object or None if not found
    ...
```

If you typed the function signature first, the AI generates against your type. If you didn't, the AI guesses---and may guess wrong.

### AI Interface Drift: Wrong Assumptions About Your Code

AI doesn't have access to your full codebase context when generating code. It makes assumptions about interfaces:

```python
# AI assumes your database module works like this:
from db import get_connection

def save_task(task: Task) -> bool:
    conn = get_connection()
    conn.execute("INSERT INTO tasks ...", task.to_dict())
    conn.commit()
    return True


# But your actual db module exposes:
from db import get_session

def save_task(task: Task) -> Task:
    session = get_session()
    session.add(task)
    session.flush()
    return task  # Returns the task with generated ID
```

With typed imports and function signatures, the type checker catches every mismatch: wrong function name, wrong parameter types, wrong return type.

### The Pattern: Types as AI Specification

The pattern is clear. When you work with AI:

1. **Define types first** (the specification)
2. **Let AI generate implementations** (constrained by types)
3. **Type checker verifies** (catches hallucinations automatically)

This is the same pattern as Principle 6's permission model, applied to code:

```
Principle 6: Define permissions → AI operates → Safety system verifies
Axiom V:     Define types     → AI generates → Type checker verifies
```

## Dataclasses vs Pydantic: Internal Types vs Boundary Types

A common question: when do you use `@dataclass` and when do you use Pydantic's `BaseModel`? The answer depends on where the data lives in your system.

| Characteristic | Dataclass | Pydantic BaseModel |
|---------------|-----------|-------------------|
| **Purpose** | Internal data structures | External data validation |
| **Validation** | None (trusts the caller) | Full (validates all input) |
| **Performance** | Faster (no validation overhead) | Slower (validates on creation) |
| **Where used** | Inside your system boundaries | At system boundaries (APIs, files, user input) |
| **Mutability** | Mutable by default | Immutable by default |
| **Serialization** | Manual (or `asdict()`) | Built-in `.model_dump()`, `.model_dump_json()` |
| **Error handling** | None (garbage in, garbage out) | Rich validation errors |

### When to Use Each

**Use dataclasses for internal domain objects:**

```python
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    """Internal representation - trusted data only."""

    id: int
    title: str
    created_at: datetime
    tags: list[str] = field(default_factory=list)
    completed: bool = False
```

**Use Pydantic for boundaries where external data enters:**

```python
from pydantic import BaseModel, Field
from datetime import datetime


class TaskCreateRequest(BaseModel):
    """API request validation - untrusted data."""

    title: str = Field(min_length=1, max_length=200)
    tags: list[str] = Field(default_factory=list, max_length=10)
    priority: int = Field(ge=1, le=5, default=3)


class TaskResponse(BaseModel):
    """API response serialization."""

    id: int
    title: str
    created_at: datetime
    completed: bool
```

**The conversion pattern---boundary to internal:**

```python
def create_task(request: TaskCreateRequest) -> Task:
    """Convert validated boundary type to internal type."""
    return Task(
        id=generate_id(),
        title=request.title,
        created_at=datetime.now(),
        tags=request.tags,
        completed=False,
    )
```

The rule is simple: **Pydantic at the edges, dataclasses at the core.** Data entering your system gets validated. Data inside your system is already trusted.

## Anti-Patterns: How Types Get Undermined

Knowing what to do matters less if you don't recognize what to avoid. These are the common patterns that destroy type safety:

| Anti-Pattern | Why It's Harmful | What to Do Instead |
|-------------|-----------------|-------------------|
| `dict[str, Any]` everywhere | Loses all type information; any key/value accepted | Define a dataclass or TypedDict for the structure |
| Functions without return types | Caller doesn't know what to expect; AI can't constrain output | Always annotate return type, even if `-> None` |
| Comments as type docs (`# returns list of users`) | Comments drift from reality; not machine-checkable | Use actual type hints: `-> list[User]` |
| Disabling type checker ("too strict") | Removes the entire safety net | Fix the types; strictness IS the value |
| `# type: ignore` on every line | Silences real errors alongside noise | Fix root causes; use ignore only for genuine false positives |
| Untyped AI output shipped directly | Hallucinations reach production unchecked | Type-annotate AI code, run Pyright before committing |

### The `Any` Anti-Pattern in Detail

`Any` is Python's escape hatch from the type system. It means "I don't know the type, and I don't want the checker to care." Every `Any` in your code is a hole in your guardrails:

```python
from typing import Any


# BAD: Any disables all checking
def process_data(data: Any) -> Any:
    return data["result"]["items"][0]["name"]
    # No checking: data might not have "result"
    # No checking: "items" might not be a list
    # No checking: elements might not have "name"


# GOOD: Explicit types enable full checking
@dataclass
class ProcessedResult:
    name: str


@dataclass
class ResultItem:
    name: str


@dataclass
class ApiResponse:
    result: ResultData


@dataclass
class ResultData:
    items: list[ResultItem]


def process_data(data: ApiResponse) -> str:
    return data.result.items[0].name
    # Every access is checked
    # Every type is known
    # Errors caught before runtime
```

Yes, the typed version requires more structure. That structure IS the specification. When you give this to an AI, it knows exactly what `data` contains, what operations are valid, and what the function must return.

## Generics and Protocols: Flexible but Safe

Types don't mean rigid. Python supports generics (parameterized types) and protocols (structural typing) for code that's both flexible and safe.

### Generics: One Implementation, Many Types

```python
from typing import TypeVar

T = TypeVar("T")


def first_or_none(items: list[T]) -> T | None:
    """Return first item or None if empty. Works with any type."""
    return items[0] if items else None


# Works with any list - fully typed:
task: Task | None = first_or_none([task1, task2])
name: str | None = first_or_none(["alice", "bob"])
count: int | None = first_or_none([1, 2, 3])
```

### Protocols: Duck Typing with Safety

Protocols define what an object must look like without requiring inheritance:

```python
from typing import Protocol


class Completable(Protocol):
    """Anything that can be marked complete."""

    completed: bool

    def mark_complete(self) -> None: ...


def complete_all(items: list[Completable]) -> int:
    """Mark all items complete. Returns count."""
    count = 0
    for item in items:
        if not item.completed:
            item.mark_complete()
            count += 1
    return count


# Any class with 'completed' and 'mark_complete()' works:
@dataclass
class Task:
    title: str
    completed: bool = False

    def mark_complete(self) -> None:
        self.completed = True


@dataclass
class Milestone:
    name: str
    completed: bool = False

    def mark_complete(self) -> None:
        self.completed = True


# Both work with complete_all() - no inheritance needed:
complete_all([Task("Write tests"), Milestone("v1.0")])
```

Protocols are particularly powerful with AI: you define the interface (Protocol), and AI generates implementations that must satisfy it. The type checker verifies conformance automatically.

## Try With AI

Use these prompts to explore type systems hands-on with your AI assistant. Each targets a different skill in the type discipline stack.

### Prompt 1: Type the Untyped

```
Here's a Python function without type annotations. Help me add complete type hints,
then explain what errors Pyright strict mode would catch if the types were wrong:

def process_users(users, filter_fn, limit):
    results = []
    for user in users:
        if filter_fn(user):
            results.append({"name": user.name, "score": user.calculate_score()})
        if len(results) >= limit:
            break
    return results

Walk me through your reasoning:
1. What type should each parameter be?
2. What does the return type look like?
3. Should we use TypedDict for the dict, or a dataclass?
4. What would Pyright catch if someone called this with wrong argument types?
```

**What you're learning**: How to read untyped code and infer the correct types from usage patterns. You're practicing the skill of converting implicit assumptions into explicit, machine-checkable contracts---the core discipline that makes AI collaboration safe.

### Prompt 2: Pydantic Boundary Design

```
I'm building an API endpoint that accepts task creation requests.
The request has: title (required, 1-200 chars), description (optional),
priority (1-5, default 3), tags (list of strings, max 5 tags, each max 50 chars),
and due_date (optional ISO format date string).

Help me design:
1. A Pydantic model for the request validation
2. A dataclass for the internal Task representation
3. A conversion function from request to internal type
4. A Pydantic model for the API response

For each model, explain WHY certain fields have validators vs plain types.
What would happen if I used a plain dataclass for the API request instead of Pydantic?
Show me what invalid data would look like and how Pydantic catches it.
```

**What you're learning**: The boundary-vs-internal type distinction in practice. You're developing the judgment to know where validation belongs (edges of your system) versus where trust is appropriate (inside your system)---and understanding the consequences of getting this wrong.

### Prompt 3: AI-Proof Your Interface

```
I want to define a typed interface that constrains AI-generated code.
Here's my scenario: I have a plugin system where each plugin must:
- Have a name (string)
- Have a version (tuple of 3 ints)
- Implement an execute() method that takes a dict of string keys and returns a Result
- Implement a validate() method that takes the same dict and returns True/False

Help me:
1. Define a Protocol for this plugin interface
2. Write one example plugin that satisfies the Protocol
3. Write a plugin runner that accepts any Completable-conforming plugin
4. Show me what happens when AI generates a plugin that DOESN'T satisfy the Protocol
   (what errors does Pyright show?)

Then explain: How does this Protocol act as a "specification" that constrains
what AI can generate? How is this different from documentation or comments?
```

**What you're learning**: How to use Protocols as machine-enforced specifications for AI-generated code. You're learning to design interfaces that AI must satisfy---turning type annotations into guardrails that catch hallucinations before they reach production.

## Safety Note

Types are a safety net, not a guarantee. They catch a large class of errors (wrong types, missing attributes, interface mismatches) but they don't catch logical errors (correct types, wrong values). A function that returns `int` when it should return `float` will be caught. A function that returns `42` when it should return `7` will not.

Use types as one layer in your verification stack: types catch structural errors, tests catch logical errors, and code review catches design errors. No single layer is sufficient. Together, they form the defense-in-depth that makes AI collaboration safe.

When in doubt, type it. The cost of adding a type annotation is seconds. The cost of debugging a type error at runtime---especially one introduced by AI-generated code you thought was correct---is hours.
