---
sidebar_position: 9
title: "Capstone - Budget Tracker Complete App"
chapter: 9
lesson: 8
duration_minutes: 40
description: "Integrate schema, CRUD, relationships, transactions, Neon deployment, and selective high-stakes verification in one complete application"
keywords: ["capstone", "SQLAlchemy", "Neon", "transactions", "aggregation", "verification", "operational checklist"]

# HIDDEN SKILLS METADATA
skills:
  - name: "System Integration"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can integrate all chapter primitives into one coherent app"

  - name: "Operational Judgment"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can decide when to use SQL-only vs hybrid verification"

learning_objectives:
  - objective: "Build and run a complete Neon-backed budget tracker"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student can execute app end-to-end and validate outputs"

  - objective: "Use efficient query shapes for summary analytics"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student replaces N+1 style with grouped/joined query patterns"

  - objective: "Apply high-stakes mismatch policy before publishing critical outputs"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student blocks report publication on verification mismatch"

---

# Capstone - Budget Tracker Complete App

> **Continuity bridge**
> - From Chapter 7: bash gave you operational control over files and workflows.
> - From Chapter 8: Python gave you deterministic computation and verified parsing.
> - Now in Chapter 9: SQLAlchemy + Neon turns that into persistent, relational, multi-user systems.

**Principle anchor:** P4 (Small, Reversible Decomposition) is the capstone strategy: integrate one reliable layer at a time and keep evidence at each boundary.

## Failure Hook

A budget app that "works on my machine" is not enough if it:

- loses data on restart
- returns plausible but wrong summaries
- commits half-failed transfers
- cannot be trusted for high-stakes reports

This capstone closes those failure modes.

## Architecture (Final)

You will combine:

1. **Models** for schema clarity
2. **CRUD** for safe writes/reads
3. **Relationships** for connected queries
4. **Transactions** for all-or-nothing updates
5. **Neon deployment** for persistence and concurrency
6. **Selective hybrid verification** for high-stakes outputs

## Core Application

### 1) Setup + Models

```python
import os
from datetime import date, datetime, timezone
from decimal import Decimal
from dotenv import load_dotenv
from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    create_engine,
    func,
    select,
    text,
)
from sqlalchemy.orm import Session, declarative_base, relationship
from sqlalchemy.pool import QueuePool

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set")

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=False,
)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    color = Column(String(7), default="#FF6B6B")

    expenses = relationship("Expense", back_populates="category", cascade="all, delete-orphan")


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    date = Column(Date, default=date.today)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")
```

### 2) CRUD + Transaction Safety

```python
def create_expense(user_id: int, category_id: int, description: str, amount: Decimal, when: date):
    with Session(engine) as session:
        try:
            row = Expense(
                user_id=user_id,
                category_id=category_id,
                description=description,
                amount=amount,
                date=when,
            )
            session.add(row)
            session.commit()
            return {"success": True, "id": row.id}
        except Exception as exc:
            session.rollback()
            return {"success": False, "error": str(exc)}


def get_expense(expense_id: int):
    with Session(engine) as session:
        row = session.execute(
            select(Expense).where(Expense.id == expense_id)
        ).scalars().first()
        return row


def update_expense_description(expense_id: int, new_description: str):
    with Session(engine) as session:
        try:
            row = session.execute(
                select(Expense).where(Expense.id == expense_id)
            ).scalars().first()
            if not row:
                return {"success": False, "error": "Expense not found"}

            row.description = new_description
            session.commit()
            return {"success": True}
        except Exception as exc:
            session.rollback()
            return {"success": False, "error": str(exc)}


def delete_expense(expense_id: int):
    with Session(engine) as session:
        try:
            row = session.execute(
                select(Expense).where(Expense.id == expense_id)
            ).scalars().first()
            if not row:
                return {"success": False, "error": "Expense not found"}

            session.delete(row)
            session.commit()
            return {"success": True}
        except Exception as exc:
            session.rollback()
            return {"success": False, "error": str(exc)}


def transfer_budget(user_id: int, from_category_id: int, to_category_id: int, amount: Decimal):
    """Atomic transfer: create two balancing entries or none."""
    with Session(engine) as session:
        try:
            from_cat = session.execute(
                select(Category).where(Category.id == from_category_id)
            ).scalars().first()
            to_cat = session.execute(
                select(Category).where(Category.id == to_category_id)
            ).scalars().first()

            if not from_cat or not to_cat:
                raise ValueError("Category not found")

            debit = Expense(
                user_id=user_id,
                category_id=from_category_id,
                description=f"Transfer to {to_cat.name}",
                amount=-amount,
            )
            credit = Expense(
                user_id=user_id,
                category_id=to_category_id,
                description=f"Transfer from {from_cat.name}",
                amount=amount,
            )

            session.add_all([debit, credit])
            session.commit()
            return {"success": True}
        except Exception as exc:
            session.rollback()
            return {"success": False, "error": str(exc)}
```

### CRUD Evidence Matrix (Required)

| Capability | Evidence function | Proof artifact |
|---|---|---|
| Create | `create_expense()` | returned id + DB row exists |
| Read | `get_expense()` | row returned with expected fields |
| Update | `update_expense_description()` | before/after query diff |
| Delete | `delete_expense()` | post-delete query returns `None` |
| Multi-step write safety | `transfer_budget()` | success and forced-failure rollback traces |

### 3) Optimized Query Pattern (No N+1)

Avoid querying expenses category-by-category in loops. Use grouped query once.

```python
def monthly_summary(user_id: int, year: int, month: int):
    start = date(year, month, 1)
    end = date(year + (month == 12), (month % 12) + 1, 1)

    with Session(engine) as session:
        rows = session.execute(
            select(
                Category.name.label("category"),
                func.count(Expense.id).label("count"),
                func.sum(Expense.amount).label("total"),
            )
            .join(Expense, Expense.category_id == Category.id)
            .where(
                Expense.user_id == user_id,
                Expense.date >= start,
                Expense.date < end,
            )
            .group_by(Category.name)
            .order_by(func.sum(Expense.amount).desc())
        ).all()

    return [
        {
            "category": r.category,
            "count": int(r.count),
            "total": (r.total or Decimal("0")).quantize(Decimal("0.01")),
        }
        for r in rows
    ]
```

## High-Stakes Verification Path

Use this only when publishing financial or audit-sensitive output.

### Policy

- SQL summary is primary.
- Independent path recomputes totals from raw imported ledger CSV.
- If mismatch > `Decimal("0.01")`, **block release** and investigate.

```python
from pathlib import Path
import csv
from decimal import Decimal


def verify_monthly_summary_from_raw(raw_csv: Path, year: int, month: int):
    prefix = f"{year}-{month:02d}"
    totals = {}

    with raw_csv.open("r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row["date"].startswith(prefix):
                continue
            cat = row["category"]
            amount = Decimal(row["amount"])
            totals[cat] = totals.get(cat, Decimal("0")) + amount

    return totals


def verify_or_block(sql_summary, raw_totals):
    tolerance = Decimal("0.01")
    sql_map = {
        r["category"]: Decimal(r["total"]).quantize(Decimal("0.01"))
        for r in sql_summary
    }

    categories = sorted(set(sql_map) | set(raw_totals))
    mismatches = []
    for c in categories:
        a = sql_map.get(c, Decimal("0")).quantize(Decimal("0.01"))
        b = raw_totals.get(c, Decimal("0")).quantize(Decimal("0.01"))
        delta = abs(a - b)
        if delta > tolerance:
            mismatches.append(
                {"category": c, "sql": str(a), "raw": str(b), "delta": str(delta)}
            )

    if mismatches:
        return {
            "status": "blocked",
            "reason": "verification_mismatch",
            "tolerance": str(tolerance),
            "mismatches": mismatches,
        }

    return {"status": "verified"}
```

## Run Sequence

1. Initialize schema
2. Seed user/categories
3. Write a few expenses
4. Generate monthly summary
5. If report is high-stakes, run verification and apply policy

```python
def init_db():
    Base.metadata.create_all(engine)


def test_connection():
    with Session(engine) as session:
        session.execute(text("SELECT 1"))


if __name__ == "__main__":
    init_db()
    test_connection()
    print("Budget Tracker initialized")
```

## Guardrails

- Never mark a report "verified" without mismatch policy result.
- Never claim production-readiness without rollback-tested write paths.
- Never hardcode credentials.
- Never use non-independent checks and call them hybrid.

## Operational Checklist (Required Before "Production-Ready")

- [ ] **Correctness:** key summary queries match known fixtures.
- [ ] **Safety:** all multi-step writes have explicit rollback paths.
- [ ] **Observability:** SQL debugging path documented (`echo=True` / logs).
- [ ] **Rollback drills:** at least one deliberate failure test executed.
- [ ] **Connection reliability:** pooling + pre-ping validated on Neon.
- [ ] **Verification policy:** mismatch blocks high-stakes report release.

### Release-Ready Evidence Bundle (Example Output)

```json
{
  "happy_path_run": "pass",
  "crud_matrix": "pass",
  "rollback_failure_drill": "pass",
  "neon_connection_resilience": "pass",
  "verification_policy_result": "verified"
}
```

## What Breaks Next

You can now build persistent, queryable, integrity-safe applications.

What breaks next is not syntax. It is operational discipline at scale: testing strategy, migrations, and long-lived change management.

Next chapter pressure-tests this app-style thinking under broader automation constraints, where good code alone is not enough.

## Try With AI

### Prompt 1 — Explain

```text
Read my capstone code and identify where integrity is guaranteed,
where it is assumed, and where it is still vulnerable.
```

### Prompt 2 — Optimize

```text
Find one N+1 pattern or inefficient query shape in my app and rewrite it
into a grouped/joined query with the same output contract.
```

### Prompt 3 — Verify

```text
Design a high-stakes verification runbook for monthly financial reports,
including mismatch triage steps and release gates.
```

## Checkpoint: Chapter Complete

- [ ] I can run app startup against Neon successfully.
- [ ] I can explain each model and write path.
- [ ] I can produce monthly summaries with optimized query shape.
- [ ] I can block report publication on verification mismatch.
- [ ] I can justify when hybrid verification is required vs optional.
