---
sidebar_position: 3
title: "Axiom III: Programs Over Scripts"
description: "Production work requires proper programs with types, tests, error handling, and CI integration. Scripts are for exploration; programs are for shipping."
keywords: ["programs over scripts", "type annotations", "pytest", "pyright", "ruff", "uv", "Python discipline", "CI/CD", "agentic development", "production code"]
chapter: 14
lesson: 3
duration_minutes: 22

# HIDDEN SKILLS METADATA
skills:
  - name: "Distinguishing Scripts from Programs"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify at least five structural differences between a script and a program (types, tests, error handling, CLI interface, package structure) and explain why each matters"

  - name: "Applying the Python Discipline Stack"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can describe the role of uv (dependency management), pyright (type checking), ruff (linting/formatting), and pytest (testing) and explain how they form a verification pipeline"

  - name: "Evaluating Code Readiness for Production"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Safety"
    measurable_at_this_level: "Given a code sample, student can assess whether it meets program-level quality (types, error handling, tests, packaging) or remains at script level, and recommend specific improvements"

learning_objectives:
  - objective: "Distinguish programs from scripts using five structural criteria"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can list and explain: type annotations, error handling, test coverage, CLI interface, and package structure as the five markers of a program"

  - objective: "Apply the Python discipline stack (uv, pyright, ruff, pytest) to evaluate code quality"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student can describe what each tool catches and how they form layers of verification that prevent different classes of defects"

  - objective: "Explain why AI-generated code requires program-level discipline"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can articulate three reasons: types catch hallucinated APIs, tests prevent drift, CI enforces standards across sessions"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (script-program continuum, type annotations, error handling discipline, discipline stack tools, AI-code verification, decision framework) within A2-B1 range (5-7)"

differentiation:
  extension_for_advanced: "Research how pyright strict mode catches more subtle type errors than basic mode; explore how pre-commit hooks automate the discipline stack before every commit"
  remedial_for_struggling: "Focus on one concrete transformation: take a 10-line script and add type hints and one test, then observe what pyright and pytest catch"
---

# Axiom III: Programs Over Scripts

Last Tuesday, you wrote a quick Python script to rename 200 image files in a folder. Fifteen lines. No imports beyond `os` and `re`. It worked perfectly on the first run, and you felt productive.

Then your colleague asked: "Can I use that for our client deliverables?" Suddenly you needed to handle files with spaces in their names, log which files were renamed, skip files that already matched the pattern, and report errors instead of crashing silently. Your 15-line script grew to 80 lines of tangled if-statements. A week later, the script renamed a client's final deliverable incorrectly, and nobody knew why because there were no logs, no tests, and no way to reproduce the issue.

This is the script-to-program boundary. Crossing it without recognizing you've crossed it is one of the most common sources of production failures in AI-era development.

## The Problem Without This Axiom

Without "Programs Over Scripts," developers fall into a dangerous pattern: they write quick scripts, those scripts work for the immediate problem, and then those scripts quietly become production infrastructure. Nobody announces "this script is now load-bearing code." It just happens, one convenience at a time.

The consequences compound:

- A data processing script runs in production for months. One day the input format changes slightly. The script crashes at 2 AM with no error message beyond `KeyError: 'timestamp'`. Nobody knows what it expected or why.
- An AI agent generates a utility function. It works for the test case. Three weeks later, it fails on edge cases the AI never considered. There are no tests to reveal this, and no type annotations to show what the function actually expects.
- A deployment script uses hardcoded paths. It works on the author's machine. On the CI server, it fails silently and deploys a broken build.

The root cause is the same every time: code that grew beyond script-level complexity while retaining script-level discipline.

## The Axiom Defined

> **Axiom III: Production work requires proper programs, not ad-hoc scripts. Programs have types, tests, error handling, and CI integration. Scripts are for exploration; programs are for shipping.**

This axiom draws a clear line: scripts serve exploration and experimentation; programs serve reliability and collaboration. Both are valuable. The failure mode is not writing scripts. The failure mode is shipping scripts as if they were programs.

## From Principle to Axiom

In Chapter 3, you learned **Principle 2: Code as Universal Interface** -- the idea that code solves problems precisely where prose fails. Code is unambiguous. Code is executable. Code is the language machines understand natively.

Axiom III builds on that foundation: if code is your universal interface, then the **quality** of that code determines the reliability of your interface. A vague specification is bad. A vague program is worse, because it compiles and runs -- giving the false appearance of correctness while hiding fragility beneath the surface.

Principle 2 says: *use code to solve problems*.
Axiom III says: *make that code worthy of the problems it solves*.

The principle is about choosing the right medium. The axiom is about discipline within that medium.

## The Script-to-Program Continuum

Scripts and programs are not binary categories. They exist on a continuum, and code naturally moves along it as its responsibilities grow. The key is recognizing when your code has moved far enough that script-level practices become dangerous.

| Dimension | Script | Program |
|-----------|--------|---------|
| **Purpose** | Explore, prototype, one-off task | Reliable, repeatable, shared |
| **Type annotations** | None or minimal | Complete on all public interfaces |
| **Error handling** | Bare `except` or crash-and-fix | Specific exceptions with recovery |
| **Tests** | Manual verification ("it printed the right thing") | Automated test suite (pytest) |
| **CLI interface** | Hardcoded values, `sys.argv[1]` | Typed CLI (typer/click/argparse) |
| **Dependencies** | `pip install` globally | Locked in `pyproject.toml` (uv) |
| **Configuration** | Magic strings in source | Typed config objects or env vars |
| **Documentation** | Comments (maybe) | Docstrings, README, usage examples |
| **CI/CD** | None | Linted, type-checked, tested on every push |

### When Does a Script Become a Program?

A script should become a program when any of these conditions become true:

1. **Someone else will run it.** If another human (or an automated system) depends on your code, it needs to communicate its expectations through types and handle failures gracefully.
2. **It will run more than once.** One-off scripts can crash and you re-run them with a fix. Repeated execution requires reliability.
3. **It processes important data.** If the input or output matters (client files, financial records, deployment artifacts), silent failures are unacceptable.
4. **It grew beyond 50 lines.** This is not a strict threshold, but complexity compounds. Beyond 50 lines, you cannot hold the full logic in your head while debugging.
5. **An AI generated it.** AI-generated code deserves extra scrutiny because you did not write it line-by-line. Types and tests become your verification layer.

## A Script Becomes a Program: Concrete Example

Here is a real progression. First, the script version -- quick, functional, fragile:

```python
# rename_images.py (SCRIPT version)
import os
import re

folder = "/Users/me/photos"
for f in os.listdir(folder):
    if f.endswith(".jpg"):
        new_name = re.sub(r'\s+', '_', f.lower())
        os.rename(
            os.path.join(folder, f),
            os.path.join(folder, new_name)
        )
        print(f"Renamed: {f} -> {new_name}")
```

This works. It also has no error handling, no way to preview changes, no protection against overwriting files, no tests, no type information, and hardcoded paths. When it fails, it fails silently or mid-operation, leaving your folder in an inconsistent state.

Now, the program version:

```python
# src/image_renamer/cli.py (PROGRAM version)
"""Batch rename image files with safe, reversible operations."""

from pathlib import Path
from dataclasses import dataclass
import re
import logging
import typer

app = typer.Typer(help="Safely rename image files in a directory.")
logger = logging.getLogger(__name__)


@dataclass
class RenameOperation:
    """Represents a single file rename with before/after state."""
    source: Path
    destination: Path

    @property
    def would_overwrite(self) -> bool:
        return self.destination.exists()


def normalize_filename(name: str) -> str:
    """Convert filename to lowercase with underscores.

    Args:
        name: Original filename (without extension).

    Returns:
        Normalized filename safe for all operating systems.
    """
    normalized = re.sub(r'\s+', '_', name.lower())
    normalized = re.sub(r'[^\w\-.]', '', normalized)
    return normalized


def plan_renames(folder: Path, extensions: tuple[str, ...] = (".jpg", ".png")) -> list[RenameOperation]:
    """Generate rename operations without executing them.

    Args:
        folder: Directory containing files to rename.
        extensions: File extensions to process.

    Returns:
        List of planned rename operations.

    Raises:
        FileNotFoundError: If folder does not exist.
        NotADirectoryError: If folder is not a directory.
    """
    if not folder.exists():
        raise FileNotFoundError(f"Directory not found: {folder}")
    if not folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder}")

    operations: list[RenameOperation] = []
    for file_path in sorted(folder.iterdir()):
        if file_path.suffix.lower() in extensions:
            new_stem = normalize_filename(file_path.stem)
            new_name = f"{new_stem}{file_path.suffix.lower()}"
            destination = file_path.parent / new_name
            if destination != file_path:
                operations.append(RenameOperation(source=file_path, destination=destination))

    return operations


def execute_renames(operations: list[RenameOperation], dry_run: bool = False) -> tuple[int, int]:
    """Execute planned rename operations.

    Args:
        operations: List of rename operations to execute.
        dry_run: If True, log but do not rename.

    Returns:
        Tuple of (successful_count, skipped_count).
    """
    successful = 0
    skipped = 0

    for op in operations:
        if op.would_overwrite:
            logger.warning("Skipping %s: destination %s already exists", op.source.name, op.destination.name)
            skipped += 1
            continue

        if dry_run:
            logger.info("[DRY RUN] Would rename: %s -> %s", op.source.name, op.destination.name)
        else:
            try:
                op.source.rename(op.destination)
                logger.info("Renamed: %s -> %s", op.source.name, op.destination.name)
                successful += 1
            except OSError as e:
                logger.error("Failed to rename %s: %s", op.source.name, e)
                skipped += 1

    return successful, skipped


@app.command()
def rename(
    folder: Path = typer.Argument(..., help="Directory containing images to rename"),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Preview changes without renaming"),
    extensions: str = typer.Option(".jpg,.png", help="Comma-separated file extensions to process"),
) -> None:
    """Rename image files to normalized lowercase with underscores."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    ext_tuple = tuple(e.strip() if e.startswith(".") else f".{e.strip()}" for e in extensions.split(","))
    operations = plan_renames(folder, ext_tuple)

    if not operations:
        typer.echo("No files to rename.")
        raise typer.Exit()

    typer.echo(f"Found {len(operations)} file(s) to rename.")
    successful, skipped = execute_renames(operations, dry_run=dry_run)

    if not dry_run:
        typer.echo(f"Done: {successful} renamed, {skipped} skipped.")


if __name__ == "__main__":
    app()
```

And the tests that verify it:

```python
# tests/test_renamer.py
from pathlib import Path
from image_renamer.cli import normalize_filename, plan_renames, execute_renames, RenameOperation


def test_normalize_removes_spaces() -> None:
    assert normalize_filename("My Photo Name") == "my_photo_name"


def test_normalize_removes_special_chars() -> None:
    assert normalize_filename("photo (1) [final]") == "photo_1_final"


def test_normalize_collapses_multiple_spaces() -> None:
    assert normalize_filename("too   many    spaces") == "too_many_spaces"


def test_plan_renames_skips_already_normalized(tmp_path: Path) -> None:
    (tmp_path / "already_normal.jpg").touch()
    operations = plan_renames(tmp_path)
    assert len(operations) == 0


def test_plan_renames_finds_files_needing_rename(tmp_path: Path) -> None:
    (tmp_path / "My Photo.jpg").touch()
    (tmp_path / "Another File.PNG").touch()
    operations = plan_renames(tmp_path, extensions=(".jpg", ".png"))
    assert len(operations) == 2


def test_plan_renames_raises_on_missing_directory() -> None:
    import pytest
    with pytest.raises(FileNotFoundError):
        plan_renames(Path("/nonexistent/path"))


def test_execute_skips_overwrites(tmp_path: Path) -> None:
    source = tmp_path / "My Photo.jpg"
    destination = tmp_path / "my_photo.jpg"
    source.touch()
    destination.touch()  # Already exists

    op = RenameOperation(source=source, destination=destination)
    successful, skipped = execute_renames([op])
    assert successful == 0
    assert skipped == 1


def test_execute_dry_run_does_not_rename(tmp_path: Path) -> None:
    source = tmp_path / "My Photo.jpg"
    source.touch()

    op = RenameOperation(source=source, destination=tmp_path / "my_photo.jpg")
    execute_renames([op], dry_run=True)
    assert source.exists()  # Not renamed
```

Notice what changed:

| Aspect | Script | Program |
|--------|--------|---------|
| Errors | Crashes on missing folder | Raises specific exceptions with context |
| Safety | Can overwrite files | Checks for conflicts, skips with warning |
| Preview | No way to see what will happen | `--dry-run` flag shows planned changes |
| Types | None | Full annotations on all functions |
| Testing | "I ran it and it looked right" | 7 automated tests covering edge cases |
| Interface | Edit source code to change folder | CLI with `--help`, arguments, options |
| Logging | `print()` | Structured logging with levels |

## The Python Discipline Stack

Python is flexible enough to be used as both a scripting language and a systems programming language. The discipline stack is what transforms Python from "quick and loose" into "verified and reliable." Four tools form the foundation:

| Tool | Role | What It Catches |
|------|------|-----------------|
| **uv** | Dependency management | Wrong versions, missing packages, environment conflicts |
| **pyright** | Static type checker | Wrong argument types, missing attributes, incompatible returns |
| **ruff** | Linter and formatter | Unused imports, style violations, common bugs, inconsistent formatting |
| **pytest** | Test runner | Logic errors, edge cases, regressions after changes |

These tools form layers of verification, each catching a different class of defect:

```
Layer 4: pytest     → Does the logic produce correct results?
Layer 3: pyright    → Do the types align across function boundaries?
Layer 2: ruff       → Does the code follow consistent patterns?
Layer 1: uv         → Are the dependencies resolved and reproducible?
```

### How They Work Together

A minimal `pyproject.toml` that activates the full stack:

```toml
[project]
name = "image-renamer"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["typer>=0.9.0"]

[project.scripts]
image-renamer = "image_renamer.cli:app"

[tool.pyright]
pythonVersion = "3.12"
typeCheckingMode = "standard"

[tool.ruff]
target-version = "py312"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]

[tool.pytest.ini_options]
testpaths = ["tests"]
```

Running the full stack:

```bash
# Install dependencies in an isolated environment
uv sync

# Check types (catches mismatched arguments, wrong return types)
uv run pyright src/

# Lint and format (catches style issues, common bugs)
uv run ruff check src/ tests/
uv run ruff format src/ tests/

# Run tests (catches logic errors)
uv run pytest
```

Each tool catches problems the others miss. Pyright will not tell you that your rename logic is wrong -- that requires tests. Pytest will not tell you that you are passing a `str` where a `Path` is expected -- that requires pyright. Ruff will not tell you either of those things, but it will catch the unused import and the inconsistent formatting that make code harder to read and maintain.

## Why AI-Generated Code Requires Program Discipline

When you write code yourself, you build a mental model of how it works as you type each line. You know the assumptions, the edge cases you considered, and the shortcuts you took deliberately. AI-generated code has none of this implicit understanding. You receive finished output with no trace of the reasoning behind it.

This creates three specific risks that program discipline addresses:

### 1. Types Catch Hallucinated APIs

AI models sometimes generate code that calls functions or methods that do not exist, or passes arguments in the wrong order. Type checking catches this immediately:

```python
# AI generated this -- looks reasonable
from pathlib import Path

def process_files(directory: str) -> list[str]:
    path = Path(directory)
    return path.list_files()  # pyright error: "Path" has no attribute "list_files"
```

Without pyright, this code would crash at runtime when a user first triggers that code path -- possibly in production, possibly weeks later. With pyright, you catch it before you ever run the code.

### 2. Tests Prevent Drift

AI does not remember previous sessions. Each time you ask it to modify code, it works from the current file content without understanding the history of decisions that shaped it. Tests encode your expectations permanently:

```python
def test_normalize_preserves_hyphens() -> None:
    """This test exists because a previous AI edit removed hyphens.
    Hyphens are valid in filenames and should be preserved."""
    assert normalize_filename("my-photo-name") == "my-photo-name"
```

When a future AI edit accidentally changes `normalize_filename` to strip hyphens, this test fails immediately. The test is your memory; the AI has none.

### 3. CI Enforces Standards Across Sessions

You might forget to run pyright before committing. The AI certainly will not remind you. CI (Continuous Integration) enforces the discipline stack on every push, regardless of who or what wrote the code:

```yaml
# .github/workflows/check.yml
name: Verify
on: [push, pull_request]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv sync
      - run: uv run pyright src/
      - run: uv run ruff check .
      - run: uv run pytest
```

This pipeline does not care whether a human or an AI wrote the code. It applies the same standards to both. Code that fails any check does not merge. This is your safety net against AI-generated code that looks correct but contains subtle issues.

## Anti-Patterns: Scripts Masquerading as Programs

Recognizing these patterns helps you catch code that has outgrown its script-level discipline:

| Anti-Pattern | Why It Fails | Program Alternative |
|--------------|--------------|---------------------|
| Jupyter notebooks as production code | No tests, no types, cell execution order matters, hidden state between cells | Extract logic into modules, test independently |
| `def process(data):` (no type hints) | Callers cannot verify they pass correct types; AI cannot validate its own output | `def process(data: list[Record]) -> Summary:` |
| Bare `except Exception:` | Hides real errors, makes debugging impossible | Catch specific exceptions: `except FileNotFoundError:` |
| `DB_HOST = "localhost"` in source | Breaks in any environment besides your machine | `DB_HOST = os.environ["DB_HOST"]` or typed config |
| "It's too simple to test" | Simple code becomes complex code; tests document expected behavior | Even one test proves the function works and prevents regressions |
| `python my_script.py input.csv` | No `--help`, no validation, no discoverability | `typer` or `argparse` with typed arguments |
| `pip install` in global environment | Different projects conflict; "works on my machine" syndrome | `uv` with locked `pyproject.toml` |

### The "Too Simple to Test" Trap

This anti-pattern deserves special attention because it sounds reasonable. A function that adds two numbers does not need a test. But production code is never that simple for long. The function that "just renames files" eventually needs to handle Unicode filenames, skip hidden files, preserve file permissions, and log operations. Each addition is "too simple to test" individually, but together they create untested complexity.

The cost of adding a test is low. The cost of debugging production failures in untested code is high. Write the test.

## The Decision Framework

When you sit down to write code -- or when an AI generates code for you -- ask these questions in order:

```
1. Will this code run more than once?
   YES → It needs tests.

2. Will someone else read or run this code?
   YES → It needs types and docstrings.

3. Does this code handle external input (files, APIs, user input)?
   YES → It needs specific error handling.

4. Will this code run in CI or production?
   YES → It needs all of the above, plus packaging (pyproject.toml).

5. Did an AI generate this code?
   YES → Apply extra scrutiny. Run pyright. Add tests for edge cases
         the AI may not have considered.
```

If you answered YES to any question, your code has moved past the script boundary. Apply program discipline proportional to the number of YES answers.

## Try With AI

### Prompt 1: Transform a Script into a Program

```
Here is a Python script I wrote to [describe your actual script -- processing CSV data,
calling an API, generating reports, etc.]:

[paste your script here]

Help me transform this into a proper program. Specifically:
1. Add type annotations to all functions
2. Replace bare except blocks with specific exceptions
3. Add a typer CLI interface so I can pass arguments
4. Write 3-5 pytest tests covering the main logic and one edge case
5. Create a pyproject.toml with pyright and ruff configuration

Walk me through each change and explain what class of bug it prevents.
```

**What you're learning**: The mechanical process of applying program discipline to existing code. By watching the transformation step-by-step, you internalize which changes catch which categories of bugs, and you develop an intuition for what "production-ready" looks like compared to "it works on my machine."

### Prompt 2: Audit AI-Generated Code

```
I asked an AI to generate this Python function:

```python
def fetch_user_data(user_id):
    import requests
    resp = requests.get(f"http://api.example.com/users/{user_id}")
    data = resp.json()
    return {"name": data["name"], "email": data["email"], "age": data["age"]}
```

Audit this code against the "Programs Over Scripts" axiom. For each issue you find:
1. Name the specific anti-pattern
2. Explain what could go wrong in production
3. Show the fixed version with proper types, error handling, and structure

Then write 3 pytest tests that would catch the most dangerous failure modes.
```

**What you're learning**: Critical evaluation of AI-generated code. You are building the skill of reading code skeptically -- identifying missing error handling, absent type information, and implicit assumptions. This is the core verification skill for AI-era development: the AI generates, you verify.

### Prompt 3: Design a Discipline Stack for Your Project

```
I'm starting a new Python project that will [describe your project:
a CLI tool for file processing / an API client / a data pipeline / etc.].

Help me set up the complete Python discipline stack from scratch:
1. Project structure (src layout with pyproject.toml)
2. uv configuration for dependency management
3. pyright configuration (what strictness level and why)
4. ruff rules (which rule sets to enable for my use case)
5. pytest setup with a single example test
6. A pre-commit hook or Makefile that runs all four tools in sequence

Explain WHY each configuration choice matters -- don't just give me the config,
help me understand what each setting protects against.
```

**What you're learning**: Setting up verification infrastructure from the ground up. Understanding the "why" behind each tool configuration builds judgment about when to be strict (public APIs, shared code) versus lenient (prototypes, experiments). You are learning to create environments where bad code cannot survive.

## Safety Note

The "Programs Over Scripts" axiom is about production code. It is explicitly not about exploration. When you are experimenting with a new idea, prototyping a concept, or running a one-time data transformation, scripts are the right tool. The axiom does not say "never write scripts." It says "do not ship scripts as programs."

The danger is not writing a quick script. The danger is the moment that quick script becomes load-bearing infrastructure without anyone applying program discipline. Recognize that moment. When it arrives, stop and apply types, tests, error handling, and packaging before the script accumulates dependencies and expectations it was never built to handle.
