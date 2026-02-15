---
sidebar_position: 8
title: "Hybrid Patterns — When Tools Work Together"
chapter: 9
lesson: 7
duration_minutes: 30
description: "Use SQL as the primary path and independent verification as a selective reliability layer for high-stakes outputs"
keywords: ["hybrid verification", "SQL primary", "independent check", "tool selection", "risk-based verification"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Risk-Based Tool Selection"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can justify when hybrid verification is worth extra cost"

  - name: "Independent Verification Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can design a second-path check that is actually independent"

learning_objectives:
  - objective: "Differentiate true independent checks from same-path re-checks"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can identify non-independent verification anti-patterns"

  - objective: "Implement a safe hybrid verification workflow"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student builds SQL primary query plus independent non-shell-injection-prone check"

---

# Hybrid Patterns — When Tools Work Together

> **Continuity bridge**
> - From Chapter 7: bash gave you reliable file discovery and ops.
> - From Chapter 8: Python gave you deterministic computation and parser discipline.
> - Now in Chapter 9: SQL is primary for structured persistence; independent verification is a risk-based escalation.

**Principle anchor:** P3 (Verification as Core Step) is now operational policy, not just debugging advice.

## Failure Hook

A query can be syntactically valid and still wrong:

- wrong date boundary
- missing join condition
- category filter typo
- timezone mismatch

In low-stakes exploration, you correct and move on.
In high-stakes reporting, a plausible wrong answer is a production incident.

## Why Single-Path Answers Fail

A single SQL path is usually correct and efficient, but it is still one path.

Hybrid pattern means:

1. SQL is your primary structured-query engine.
2. A second independent path checks result plausibility.
3. You use this only when error cost justifies overhead.

## Benchmark Context (Initial vs Follow-Up)

Use benchmark numbers as directional evidence, not dogma:

- Initial public snapshot: SQL strongly outperformed bash-only for structured querying.
- Follow-up work: tooling/eval fixes and hybrid behavior showed value in independent verification for reliability.

Operational rule for this chapter:

- Default: SQL only.
- Escalate: SQL + independent verification for financial/audit/automated downstream decisions.

## New Primitive: Verification Independence

Not all "double checks" are independent.

| Check style | Independent? | Why |
|---|---|---|
| Re-running same SQL query | No | Same logic, same failure mode |
| SQL query + SQL checksum from same predicate | Weak | Still same semantic path |
| SQL result + recomputation from raw source ledger | Yes | Different path, different failure modes |
| SQL result + independent `csv.DictReader` recomputation | Yes | Different execution/data path with robust CSV parsing |

## Minimal Working Win

Question: "How much did user 1 spend in Food for 2024-01?"

### Step 1: Primary SQL path

```python
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from sqlalchemy import select, func
from sqlalchemy.orm import Session


def sql_food_total(engine, user_id: int, year: int, month: int) -> Decimal:
    start = date(year, month, 1)
    end = date(year + (month == 12), (month % 12) + 1, 1)

    with Session(engine) as session:
        value = session.execute(
            select(func.sum(Expense.amount))
            .join(Category)
            .where(
                Expense.user_id == user_id,
                Category.name == "Food",
                Expense.date >= start,
                Expense.date < end,
            )
        ).scalar_one_or_none()

    return (value or Decimal("0")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

### Step 2: Independent verification path (robust quoted CSV parsing)

Assume you have a raw ledger CSV (`raw_ledger.csv`) from your import pipeline.

```python
import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


def verify_from_raw_csv(csv_path: Path, year: int, month: int) -> Decimal:
    # Independent logic path from SQL query.
    # csv module handles quoted commas safely.
    month_prefix = f"{year}-{month:02d}"
    total = Decimal("0")

    with csv_path.open("r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("category") != "Food":
                continue
            if not row.get("date", "").startswith(month_prefix):
                continue
            total += Decimal(row["amount"])

    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

### Step 3: Compare with mismatch policy

```python
from decimal import Decimal

TOLERANCE = Decimal("0.01")


def verified_food_total(engine, raw_csv_path: Path, user_id: int, year: int, month: int):
    sql_total = sql_food_total(engine, user_id, year, month)
    raw_total = verify_from_raw_csv(raw_csv_path, year, month)

    if abs(sql_total - raw_total) <= TOLERANCE:
        return {"status": "verified", "value": sql_total}

    # Explicit mismatch policy
    return {
        "status": "mismatch",
        "sql_value": sql_total,
        "raw_value": raw_total,
        "tolerance": TOLERANCE,
        "action": "hold report, investigate join/date/category filters before publish",
    }
```

## Guardrails

1. **Do not call this hybrid** if both paths reuse identical predicates and data projection.
2. **Do not parse quoted CSV with naive split logic** (`awk -F,`, `line.split(",")`).
3. **Do not run hybrid on every query**; use risk-based escalation.
4. **Do not publish high-stakes reports on mismatch**; stop and investigate.
5. **Do not convert money to float** in verification paths.

## Tool Choice Framework (Finalized for Part 2)

| Task shape | Primary tool | Escalation |
|---|---|---|
| File discovery / ops | Bash | Add Python for parsing/computation |
| Deterministic computation | Python | Add tests/fixtures |
| Structured persistent query | SQL (SQLAlchemy) | Add hybrid only if error cost high |
| Financial/audit output | SQL + independent verify | Mandatory mismatch policy |

## What Breaks Next

You now have all primitives. Next lesson removes scaffolding: you must integrate correctness, persistence, and verification choices in one capstone without over-engineering.

Next lesson forces one production-style integration decision: prove CRUD, transactions, and verification can coexist without hidden precision drift.

## Try With AI

### Prompt 1 — Debug

```text
Given a SQL monthly total query, design a truly independent verification path.
Reject approaches that are not independent and explain why.
```

### Prompt 2 — Decide

```text
For each scenario, choose SQL-only or SQL+hybrid and justify:
1) ad-hoc dashboard exploration
2) payroll export
3) investor-facing monthly report
4) internal prototype query
```

### Prompt 3 — Prove

```text
Create a mismatch policy for high-stakes financial reporting:
- who gets alerted
- what gets blocked
- what evidence is collected
- what must be fixed before release
```

## Checkpoint

- [ ] I can explain why re-running the same SQL is not independent verification.
- [ ] I can implement a robust quoted-CSV verification path.
- [ ] I can choose hybrid only when risk justifies cost.
- [ ] I can define and enforce a mismatch handling policy.
