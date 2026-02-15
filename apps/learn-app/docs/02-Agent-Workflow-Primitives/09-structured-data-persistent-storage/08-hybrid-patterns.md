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

> **Chapter 8 callback:** In Chapter 8, you already used "verify before trust" for computation. Here, you apply the same discipline to persistent structured queries.

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
| SQL result + post-export awk check with separate filter logic | Usually yes | Independent parsing/filtering path |

## Minimal Working Win

Question: "How much did user 1 spend in Food for 2024-01?"

### Step 1: Primary SQL path

```python
from datetime import date
from sqlalchemy import select, func
from sqlalchemy.orm import Session


def sql_food_total(engine, user_id: int, year: int, month: int) -> float:
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

    return float(value or 0)
```

### Step 2: Independent verification path (safe subprocess)

Assume you have a raw ledger CSV (`raw_ledger.csv`) from your import pipeline.

```python
import subprocess
from pathlib import Path


def verify_from_raw_csv(csv_path: Path, year: int, month: int) -> float:
    # Intentionally separate logic from SQL path: parse raw ledger rows with awk.
    # No shell=True. No command interpolation.
    month_prefix = f"{year}-{month:02d}"

    awk_program = (
        'BEGIN {FS=","} '
        'NR>1 && $2=="Food" && index($3, prefix)==1 {sum += $1} '
        'END {printf "%.2f", sum}'
    )

    result = subprocess.run(
        ["awk", "-v", f"prefix={month_prefix}", awk_program, str(csv_path)],
        capture_output=True,
        text=True,
        check=True,
    )

    return float(result.stdout.strip() or 0)
```

### Step 3: Compare with mismatch policy

```python

def verified_food_total(engine, raw_csv_path: Path, user_id: int, year: int, month: int):
    sql_total = sql_food_total(engine, user_id, year, month)
    raw_total = verify_from_raw_csv(raw_csv_path, year, month)

    if abs(sql_total - raw_total) <= 0.01:
        return {"status": "verified", "value": sql_total}

    # Explicit mismatch policy
    return {
        "status": "mismatch",
        "sql_value": sql_total,
        "raw_value": raw_total,
        "action": "hold report, investigate join/date/category filters before publish",
    }
```

## Guardrails

1. **Do not call this hybrid** if both paths reuse identical predicates and data projection.
2. **Do not use shell interpolation** with user input.
3. **Do not run hybrid on every query**; use risk-based escalation.
4. **Do not publish high-stakes reports on mismatch**; stop and investigate.

## Tool Choice Framework (Finalized for Part 2)

| Task shape | Primary tool | Escalation |
|---|---|---|
| File discovery / ops | Bash | Add Python for parsing/computation |
| Deterministic computation | Python | Add tests/fixtures |
| Structured persistent query | SQL (SQLAlchemy) | Add hybrid only if error cost high |
| Financial/audit output | SQL + independent verify | Mandatory mismatch policy |

## What Breaks Next

You now have all primitives. Next lesson removes scaffolding: you must integrate correctness, persistence, and verification choices in one capstone without over-engineering.

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
- [ ] I can implement a no-`shell=True` verification command path.
- [ ] I can choose hybrid only when risk justifies cost.
- [ ] I can define and enforce a mismatch handling policy.
