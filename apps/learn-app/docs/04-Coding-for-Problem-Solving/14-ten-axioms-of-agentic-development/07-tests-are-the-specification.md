---
sidebar_position: 7
title: "Axiom VII: Tests Are the Specification"
description: "Test-Driven Generation (TDG) transforms tests from verification tools into precise specifications that AI implements, making the implementation disposable and the test permanent"
keywords: ["TDG", "Test-Driven Generation", "TDD", "pytest", "specification", "verification", "test pyramid", "fixtures", "parametrize"]
chapter: 14
lesson: 7
duration_minutes: 25

# HIDDEN SKILLS METADATA
skills:
  - name: "Test-Driven Generation Workflow"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can write failing pytest tests that define correct behavior, prompt AI with those tests, and evaluate whether generated implementations pass the specification"

  - name: "Test as Specification Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can distinguish between tests that specify behavior (what) and tests that specify implementation (how), designing tests that remain valid across multiple correct implementations"

  - name: "Test Pyramid Strategy"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can explain unit, integration, and E2E testing levels and allocate appropriate coverage across the pyramid for an agentic workflow"

  - name: "Anti-Pattern Recognition in Testing"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Critical Thinking"
    measurable_at_this_level: "Student can identify testing anti-patterns (circular AI testing, implementation coupling, happy-path-only, post-implementation testing) and explain why each undermines the TDG workflow"

learning_objectives:
  - objective: "Apply the TDG workflow to define behavior through tests before prompting AI for implementation"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Given a feature requirement, student writes failing pytest tests that unambiguously specify correct behavior, then prompts AI and evaluates the result against their tests"

  - objective: "Distinguish TDG from TDD and explain why TDG is transformative for AI-era development"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can articulate three key differences (implementation disposability, generation vs writing, specification precision) and explain why each matters when working with AI"

  - objective: "Design tests that specify behavior without coupling to implementation details"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student writes tests that would pass for multiple valid implementations of the same behavior, using pytest fixtures, parametrize, and proper assertion strategies"

  - objective: "Evaluate testing strategies using the test pyramid and identify anti-patterns"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student can categorize tests into pyramid levels, identify when coverage is imbalanced, and recognize anti-patterns that undermine TDG effectiveness"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (TDG workflow, TDG vs TDD distinction, tests-as-specification, test pyramid, pytest patterns, coverage metrics, anti-patterns) at upper limit of B1 range (5-7) ✓"

differentiation:
  extension_for_advanced: "Design a full TDG pipeline for a multi-module project: write integration tests that define module boundaries, use property-based testing (Hypothesis) to generate edge cases, and measure specification completeness through mutation testing"
  remedial_for_struggling: "Focus on one concrete example: write 3 pytest tests for a calculator function (add, edge cases, errors), prompt AI for implementation, verify it passes. Emphasize the rhythm: test first, generate second, verify third"
---

# Axiom VII: Tests Are the Specification

You ask your AI assistant to write a function that calculates shipping costs. It returns clean, well-documented code. The function handles domestic orders perfectly. You deploy it. Three days later, customer support floods with complaints: international orders are charged zero shipping. The function looked correct. It ran without errors. It even had a docstring explaining what it did. But nobody defined what "correct" actually meant for international orders, so the AI made a reasonable assumption that happened to be wrong.

Now imagine an alternative: before asking the AI for any implementation, you write five tests. One test asserts domestic orders get standard rates. Another asserts international orders get a surcharge. A third tests free shipping thresholds. A fourth tests invalid inputs. A fifth tests boundary conditions. You hand these tests to the AI and say: "Write the implementation that passes all five." The AI generates code. You run the tests. Two fail. You tell the AI: "Tests 3 and 5 are failing. Fix the implementation." It regenerates. All five pass. You accept the code.

The difference is not that you tested after the fact. The difference is that **your tests were the specification**. They defined correctness before any implementation existed. The implementation was generated to match the specification, not the other way around.

## The Problem Without This Axiom

When you skip tests-first development with AI, you fall into a predictable failure pattern:

**You describe what you want in natural language.** "Write a function that calculates shipping costs based on weight, destination, and order total." This feels precise, but it is ambiguous. What are the weight brackets? What counts as "international"? What is the free shipping threshold? Does it return a float, a Decimal, or an integer in cents?

**The AI fills in the gaps with assumptions.** It picks reasonable defaults. Weight brackets at 1kg, 5kg, 10kg. International means non-US. Free shipping above $50. Returns a float. Each assumption is plausible. Some are wrong for your business.

**You verify by reading the code.** You scan the implementation, check the logic, and convince yourself it looks right. But reading code is not the same as running it. Your eyes skip edge cases. You miss the off-by-one error at the 5kg boundary. You overlook the case where `destination` is `None`.

**Bugs appear in production.** The code that "looked right" fails on real data. Now you are debugging generated code you did not write, trying to understand the AI's assumptions, fixing issues that would never have existed if correctness had been defined upfront.

This pattern is not unique to AI. It is the oldest problem in software development: **ambiguous specifications produce correct-looking code that does the wrong thing**. But AI amplifies the problem because it generates plausible code faster than you can verify it by reading.

## The Axiom Defined

> **Test-Driven Generation (TDG):** Write tests FIRST that define correct behavior, then prompt AI: "Write the implementation that passes these tests." Tests are the specification. The implementation is disposable.

This axiom transforms tests from a verification tool into a specification language. Tests are not something you write after the code to check it works. Tests are the precise, executable definition of what "works" means.

Three consequences follow:

1. **Tests are permanent. Implementations are disposable.** If the AI generates bad code, you do not debug it. You throw it away and regenerate. The tests remain unchanged because they define the requirement, not the solution.

2. **Tests are precise where natural language is ambiguous.** "Calculate shipping costs" is vague. `assert calculate_shipping(weight=5.0, destination="UK", total=45.99) == 12.50` is unambiguous. The test says exactly what the function must return for exactly those inputs.

3. **Tests enable parallel generation.** You can ask the AI to generate ten different implementations. Run all ten against your tests. Keep the one that passes. This is selection, not debugging.

## From Principle to Axiom

In Chapter 4, you learned **Principle 3: Verification as Core Step**. That principle taught you to verify every action an agent takes, to never trust output without checking it, and to build verification into your workflow rather than treating it as optional cleanup.

Axiom VII takes that principle and sharpens it into a specific practice:

| Principle 3 | Axiom VII |
|---|---|
| Verify that actions succeeded | Define what "success" means before the action |
| Check work after it is done | Specify correct behavior before generation |
| Verification is reactive | Specification is proactive |
| "Did this work?" | "What does working look like?" |
| Catches errors | Prevents errors from being accepted |

The principle says: always verify. The axiom says: **design through verification**. Write the verification first, and it becomes the specification that guides generation.

This distinction matters in practice. A developer who follows Principle 3 might generate code, then write tests to check it. A developer who follows Axiom VII writes tests first, then generates code that must pass them. The first developer is verifying. The second developer is specifying.

## TDG: The AI-Era Testing Workflow

Test-Driven Generation adapts the classic TDD cycle for AI-powered development. Here is how the two compare:

### TDD (Traditional)

```
Write failing test → Write implementation → Refactor → Repeat
```

In TDD, you write both the test and the implementation yourself. The test guides your implementation decisions. Refactoring improves code quality while keeping tests green.

### TDG (AI-Era)

```
Write failing test → Prompt AI with test + types → Run tests → Accept or Regenerate
```

In TDG, you write the test yourself but the AI generates the implementation. If tests fail, you do not debug. You regenerate. The implementation is disposable because you can always get another one. The test is permanent because it encodes your requirements.

### The TDG Workflow in Detail

**Step 1: Write Failing Tests**

Define what correct behavior looks like. Be specific about inputs, outputs, edge cases, and error conditions:

```python
# test_shipping.py
import pytest
from shipping import calculate_shipping


class TestDomesticShipping:
    """Domestic orders: flat rate by weight bracket."""

    def test_lightweight_domestic(self):
        result = calculate_shipping(weight_kg=0.5, destination="US", order_total=25.00)
        assert result == 5.99

    def test_medium_weight_domestic(self):
        result = calculate_shipping(weight_kg=3.0, destination="US", order_total=25.00)
        assert result == 9.99

    def test_heavy_domestic(self):
        result = calculate_shipping(weight_kg=12.0, destination="US", order_total=25.00)
        assert result == 14.99


class TestInternationalShipping:
    """International orders: domestic rate + surcharge."""

    def test_international_surcharge(self):
        result = calculate_shipping(weight_kg=2.0, destination="UK", order_total=30.00)
        # Domestic medium rate (9.99) + international surcharge (8.00)
        assert result == 17.99

    def test_canada_is_international(self):
        result = calculate_shipping(weight_kg=1.0, destination="CA", order_total=20.00)
        assert result == 13.99  # 5.99 + 8.00


class TestFreeShipping:
    """Orders above threshold get free shipping."""

    def test_free_shipping_threshold(self):
        result = calculate_shipping(weight_kg=5.0, destination="US", order_total=75.00)
        assert result == 0.00

    def test_below_threshold_not_free(self):
        result = calculate_shipping(weight_kg=5.0, destination="US", order_total=74.99)
        assert result == 9.99

    def test_international_no_free_shipping(self):
        """Free shipping does not apply to international orders."""
        result = calculate_shipping(weight_kg=1.0, destination="UK", order_total=100.00)
        assert result == 13.99


class TestEdgeCases:
    """Invalid inputs and boundary conditions."""

    def test_zero_weight_raises(self):
        with pytest.raises(ValueError, match="Weight must be positive"):
            calculate_shipping(weight_kg=0, destination="US", order_total=25.00)

    def test_negative_weight_raises(self):
        with pytest.raises(ValueError, match="Weight must be positive"):
            calculate_shipping(weight_kg=-1.0, destination="US", order_total=25.00)

    def test_empty_destination_raises(self):
        with pytest.raises(ValueError, match="Destination required"):
            calculate_shipping(weight_kg=2.0, destination="", order_total=25.00)

    def test_negative_total_raises(self):
        with pytest.raises(ValueError, match="Order total cannot be negative"):
            calculate_shipping(weight_kg=2.0, destination="US", order_total=-10.00)
```

Notice what these tests accomplish: they define the weight brackets (under 1kg, 1-5kg, over 5kg), the international surcharge amount, the free shipping threshold, and all error conditions. Someone reading these tests knows exactly what the function must do without seeing any implementation.

**Step 2: Prompt AI with Tests + Types**

Give the AI your tests and any type annotations that constrain the solution:

```
Here are my pytest tests for a shipping calculator (see test_shipping.py above).

Write the implementation in shipping.py that passes all these tests.

Constraints:
- Function signature: calculate_shipping(weight_kg: float, destination: str, order_total: float) -> float
- Use only standard library
- Raise ValueError for invalid inputs with the exact messages tested
```

**Step 3: Run Tests on AI Output**

```bash
pytest test_shipping.py -v
```

If all tests pass, the implementation matches your specification. If some fail, you have two options: regenerate the entire implementation, or show the AI the failing tests and ask it to fix only those cases.

**Step 4: Accept or Regenerate**

If tests pass: accept the implementation. It conforms to your specification. You do not need to read it line by line (though you may want to check for obvious inefficiencies).

If tests fail: do not debug the generated code. Tell the AI which tests fail and ask for a new implementation. The tests are right. The implementation is wrong. Regenerate.

```
Tests 8 and 9 are failing. The international orders should NOT get free shipping
even when order_total exceeds 75.00. Fix the implementation.
```

This is the power of TDG: **you never argue with the AI about correctness.** The tests define correctness. Either the code passes or it does not.

## Writing Effective Specifications (Tests)

Good TDG tests are specifications, not implementation checks. The distinction is critical.

### Specify Behavior, Not Implementation

A **behavior specification** says what the function must do:

```python
def test_sorted_output():
    result = find_top_customers(orders, limit=3)
    assert result == ["Alice", "Bob", "Carol"]
```

An **implementation check** says how the function must work:

```python
def test_uses_heapq():
    """BAD: Tests implementation detail, not behavior."""
    with patch("heapq.nlargest") as mock_heap:
        find_top_customers(orders, limit=3)
        mock_heap.assert_called_once()
```

The first test remains valid whether the function uses sorting, a heap, or a linear scan. The second test breaks if you refactor the internals, even if behavior is preserved. In TDG, implementation-coupled tests are especially harmful because they prevent the AI from choosing the best approach.

### Use pytest Fixtures for Shared State

When multiple tests need the same setup, use fixtures to keep tests focused on assertions:

```python
import pytest
from datetime import date
from task_manager import TaskManager, Task


@pytest.fixture
def manager():
    """Fresh TaskManager with sample tasks."""
    mgr = TaskManager()
    mgr.add(Task(title="Write spec", due=date(2025, 6, 1), priority="high"))
    mgr.add(Task(title="Run tests", due=date(2025, 6, 2), priority="medium"))
    mgr.add(Task(title="Deploy", due=date(2025, 6, 3), priority="low"))
    return mgr


class TestFiltering:
    def test_filter_by_priority(self, manager):
        high = manager.filter(priority="high")
        assert len(high) == 1
        assert high[0].title == "Write spec"

    def test_filter_by_date_range(self, manager):
        tasks = manager.filter(due_before=date(2025, 6, 2))
        assert len(tasks) == 1
        assert tasks[0].title == "Write spec"

    def test_filter_no_match_returns_empty(self, manager):
        result = manager.filter(priority="critical")
        assert result == []
```

Fixtures define the world your tests operate in. When you send these to the AI, the fixture tells it exactly what data structures and setup the implementation must support.

### Use Parametrize for Specification Tables

When a function has many input-output pairs, `pytest.mark.parametrize` expresses the specification as a table:

```python
import pytest


@pytest.mark.parametrize("input_text,expected", [
    ("hello world", "Hello World"),           # Basic case
    ("HELLO WORLD", "Hello World"),           # All caps
    ("hello", "Hello"),                        # Single word
    ("", ""),                                  # Empty string
    ("hello   world", "Hello   World"),       # Multiple spaces preserved
    ("hello-world", "Hello-World"),           # Hyphenated
    ("hello\nworld", "Hello\nWorld"),          # Newline preserved
    ("123abc", "123Abc"),                      # Leading digits
])
def test_title_case(input_text, expected):
    from text_utils import to_title_case
    assert to_title_case(input_text) == expected
```

This is a specification table. It says: "For these exact inputs, produce these exact outputs." The AI can implement any algorithm it wants as long as it matches the table. This pattern works especially well for data transformation functions where business rules are complex.

### Use Markers for Test Categories

Organize tests by category so you can run subsets:

```python
import pytest


@pytest.mark.unit
def test_parse_single_line():
    from parser import parse_config
    result = parse_config("key=value")
    assert result == {"key": "value"}


@pytest.mark.integration
def test_parse_file(tmp_path):
    config_file = tmp_path / "config.ini"
    config_file.write_text("host=localhost\nport=5432")
    from parser import parse_config_file
    result = parse_config_file(config_file)
    assert result == {"host": "localhost", "port": "5432"}


@pytest.mark.slow
def test_parse_large_file(tmp_path):
    config_file = tmp_path / "large.ini"
    config_file.write_text("\n".join(f"key{i}=val{i}" for i in range(10000)))
    from parser import parse_config_file
    result = parse_config_file(config_file)
    assert len(result) == 10000
```

Run specific categories: `pytest -m unit` for fast feedback, `pytest -m integration` for thorough checks.

## The Test Pyramid

Not all tests are created equal. The test pyramid organizes tests by scope and cost:

```
         /\
        /  \        E2E Tests (few)
       / E2E\       Full system, real dependencies
      /------\      Slow, expensive, high confidence
     /        \
    /Integration\   Integration Tests (some)
   /            \   Multiple components, real I/O
  /--------------\  Medium speed, medium confidence
 /                \
/    Unit Tests    \ Unit Tests (many)
/                    \ Single function, no I/O
/--------------------\ Fast, cheap, focused
```

| Level | What It Tests | Speed | Cost | When to Use |
|---|---|---|---|---|
| **Unit** | Single function, pure logic | Milliseconds | Free | Every function with business logic |
| **Integration** | Components working together | Seconds | Low | API endpoints, database queries |
| **E2E** | Full system behavior | Minutes | High | Critical user workflows |

### TDG at Each Level

**Unit tests** are your primary TDG specification. They define individual function behavior precisely:

```python
def test_discount_calculation():
    assert apply_discount(price=100.0, discount_pct=10) == 90.0
```

**Integration tests** define how components interact:

```python
def test_order_creates_invoice(db_session):
    order = create_order(db_session, items=[{"sku": "A1", "qty": 2}])
    invoice = get_invoice(db_session, order_id=order.id)
    assert invoice.total == order.total
    assert invoice.status == "pending"
```

**E2E tests** define user-visible behavior:

```python
def test_checkout_flow(client):
    client.post("/cart/add", json={"sku": "A1", "qty": 1})
    response = client.post("/checkout", json={"payment": "card"})
    assert response.status_code == 200
    assert response.json()["order_status"] == "confirmed"
```

For TDG, aim for this distribution: **70% unit, 20% integration, 10% E2E**. Unit tests are the most effective specifications because they are precise, fast, and independent.

### Coverage as a Metric

Code coverage measures how much of your implementation is exercised by tests. For TDG work, target **80% minimum coverage**:

```bash
pytest --cov=shipping --cov-report=term-missing
```

Coverage tells you where your specification has gaps. If a branch is not covered, it means you have not specified what should happen in that case, and the AI's assumption is unverified.

But coverage is a floor, not a ceiling. 100% line coverage does not mean your specification is complete. A function can have every line executed but still be wrong for inputs you did not test. Coverage catches omissions. Good test design catches incorrect behavior.

## Anti-Patterns

These patterns undermine TDG. Recognize and avoid them:

| Anti-Pattern | Why It Fails | TDG Alternative |
|---|---|---|
| **Testing after implementation** | Tests confirm what code does, not what it should do. You test the AI's assumptions instead of your requirements. | Write tests first. The tests define requirements. |
| **Tests coupled to implementation** | Mocking internals, checking call order, asserting private state. Tests break on any refactor, preventing regeneration. | Test inputs and outputs only. Any correct implementation should pass. |
| **No tests ("it's just a script")** | Without specification, you cannot regenerate. Every bug requires manual debugging of code you did not write. | Even scripts need specs. Three tests beat zero tests. |
| **AI-generated tests for AI-generated code** | Circular logic: the same assumptions that produce wrong code produce wrong tests. Neither catches the other's errors. | You write tests (the specification). AI writes implementation (the solution). |
| **Happy-path-only testing** | Only testing the expected case. Edge cases, error conditions, and boundary values are unspecified. AI handles them however it wants. | Test the sad path. Test boundaries. Test invalid inputs. |
| **Overly rigid assertions** | Asserting exact floating-point values, exact string formatting, exact timestamps. Tests fail on valid implementations. | Use `pytest.approx()`, pattern matching, and relative assertions where appropriate. |

### The Circular Testing Trap

The most dangerous anti-pattern deserves special attention. When you ask AI to generate both the implementation and the tests, you get circular validation:

```
You: "Write a function to calculate tax and tests for it."
AI: [Writes function that uses 7% rate]
AI: [Writes tests that assert 7% rate]
```

The tests pass. Everything looks correct. But you never specified what the tax rate should be. The AI assumed 7%. If your business requires 8.5%, both the code and the tests are wrong, and neither catches the other.

In TDG, **you are the specification authority**. You decide what correct means. The AI is the implementation engine. It figures out how to achieve what you specified. Never delegate both roles to the AI.

## Safety Note

TDG does not replace security review or performance testing. Tests specify functional correctness: given these inputs, produce these outputs. They do not automatically catch:

- **Security vulnerabilities**: SQL injection, path traversal, authentication bypass. These require security-specific testing (SAST tools, penetration testing).
- **Performance issues**: An implementation that passes all functional tests might be O(n^2) when O(n) is required. Add explicit performance assertions for critical paths.
- **Concurrency bugs**: Race conditions may not manifest in sequential test execution. Use stress testing for concurrent code.
- **Resource leaks**: Memory leaks, file handle leaks, connection pool exhaustion. Requires runtime monitoring (Axiom X).

TDG gives you functional correctness. Combine it with Axiom IX (Verification is a Pipeline) and Axiom X (Observability) for comprehensive quality assurance.

## Try With AI

### Prompt 1: Your First TDG Cycle (Experiencing the Workflow)

```
I want to practice Test-Driven Generation. Here is my specification as pytest tests:

```python
import pytest
from converter import temperature_convert

def test_celsius_to_fahrenheit():
    assert temperature_convert(0, "C", "F") == 32.0

def test_fahrenheit_to_celsius():
    assert temperature_convert(212, "F", "C") == 100.0

def test_celsius_to_kelvin():
    assert temperature_convert(0, "C", "K") == 273.15

def test_invalid_unit_raises():
    with pytest.raises(ValueError, match="Unknown unit"):
        temperature_convert(100, "C", "X")

def test_below_absolute_zero_raises():
    with pytest.raises(ValueError, match="below absolute zero"):
        temperature_convert(-300, "C", "K")
```

Write the implementation in converter.py that passes all 5 tests.
Do NOT modify the tests. The tests are the specification.
```

**What you're learning:** The core TDG rhythm. You wrote the specification (tests). The AI generates the implementation. You run the tests to verify. If they pass, you accept. If they fail, you regenerate. Notice how the tests precisely define behavior (including error messages) without dictating how the conversion is calculated internally.

### Prompt 2: Specification Design (Writing Tests That Specify, Not Constrain)

```
I need to build a function called `summarize_scores(scores: list[int]) -> dict` that takes a
list of student test scores (0-100) and returns a summary dictionary.

Help me write pytest tests that SPECIFY the behavior without constraining the implementation.
I want to test:
- Normal case (mix of scores)
- Empty list (edge case)
- All same scores
- Invalid scores (negative, above 100)
- Single score

For each test, explain:
1. What behavior am I specifying?
2. Why is this a behavior test, not an implementation test?
3. What implementation freedom does the AI retain?

Do NOT write the implementation yet. I want to understand specification design first.
```

**What you're learning:** The difference between specifying behavior and constraining implementation. Good TDG tests say "given this input, produce this output" without saying "use this algorithm" or "call this internal method." You are learning to leave implementation freedom for the AI while being precise about what correctness means.

### Prompt 3: TDG for Your Domain (Applying to Real Work)

```
I'm building [describe a real feature you need: a pricing calculator, a data validator,
a text parser, a scheduling function, etc.].

Help me apply Test-Driven Generation:

1. First, ask me 5 clarifying questions about the expected behavior:
   - What are the inputs and their types?
   - What are the outputs?
   - What are the edge cases?
   - What errors should be raised and when?
   - What are the business rules?

2. Based on my answers, write a complete pytest test file that serves as the specification.
   Include: fixtures for test data, parametrize for rule tables, edge case tests, error tests.

3. Then generate the implementation that passes all tests.

4. Finally, suggest 3 additional tests I might have missed that would make my specification
   more complete.

Walk me through each step so I understand the TDG process for my specific domain.
```

**What you're learning:** Applying TDG to your own problems. The clarifying questions teach you what information a specification needs. The test file shows you how to structure a complete specification. The additional tests reveal gaps in your thinking. This is the skill that transfers: learning to think in specifications rather than implementations, regardless of what you are building.

---

*Next: Axiom VIII explores how version control provides the persistent memory layer that stores both your specifications and the implementations they generate.*
