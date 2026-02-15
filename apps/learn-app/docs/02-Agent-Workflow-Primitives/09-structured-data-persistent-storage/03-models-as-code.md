---
sidebar_position: 3
title: "Models as Code"
chapter: 9
lesson: 2
duration_minutes: 25
description: "Define SQLAlchemy models as Python classes that become database tables"
keywords: ["SQLAlchemy", "ORM", "models", "Column", "Integer", "String", "Numeric", "Float", "Date", "primary key", "ForeignKey"]
---
# Models as Code

> **Continuity bridge**
> - From Chapter 7: bash handled files, not typed structure.
> - From Chapter 8: Python handled parsing and computation.
> - Now in Chapter 9: models encode schema and constraints so structure is enforced.

In L0, you learned why databases beat CSV files. In L1, you built your skill scaffold. Now you hit the core engineering move: turning requirements into schema.

Answer: you write a Python class, and SQLAlchemy turns it into a table.

**Principle anchor:** P2 (Code as Universal Interface). Your model code is the contract every tool follows.

## The Simplest Model

Here's a complete, working model:

```python
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Numeric(10, 2))
```

This class creates an `expenses` table with exact-decimal money support. You write Python, SQLAlchemy generates relational schema.

## Understanding Column Types

Every Column needs a type. Here's what each type stores:

| Python Type     | Column Type       | What It Stores              | Example                              |
| --------------- | ----------------- | --------------------------- | ------------------------------------ |
| `int`         | `Integer`       | Whole numbers               | `id = Column(Integer)`             |
| `str`         | `String(50)`    | Text up to N characters     | `name = Column(String(50))`        |
| `Decimal`     | `Numeric(10,2)` | Exact decimals (money)      | `price = Column(Numeric(10, 2))`   |
| `float`       | `Float`         | Approximate decimals        | `weight = Column(Float)`           |
| `bool`        | `Boolean`       | True or False               | `is_active = Column(Boolean)`      |
| `datetime`    | `DateTime`      | Date and time               | `created_at = Column(DateTime)`    |
| `date`        | `Date`          | Date only (no time)         | `date = Column(Date)`              |

:::caution Why not Float for money?
`Float` is approximate (`0.1 + 0.2` drift). Budget systems need exact arithmetic, so use `Numeric(10, 2)` for money.
:::

### Column Constraints

Beyond type, columns can have constraints:

```python
Column(String(100), nullable=False)     # Required field (can't be empty)
Column(String(100), unique=True)        # No duplicates allowed
Column(Numeric(10, 2), default=0.00)    # Default value if not specified
Column(Integer, primary_key=True)       # Unique identifier for each row
```

**Key insight**: By default, columns CAN be null (empty). Add `nullable=False` to make a field required.

## Building Budget Tracker Models

Let's build the three models for our Budget Tracker. Each represents a real-world entity.

### Model 1: User

```python
from datetime import datetime, timezone

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
```

- `unique=True` on email: No two users can have the same email
- `nullable=False`: Every user MUST have an email and name
- `default=lambda: datetime.now(timezone.utc)`: Timestamp auto-generated when row created

### Model 2: Category

```python
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    color = Column(String(7), default='#FF6B6B')
```

Categories are simple: a name (like "Food" or "Transport") and a color for UI display.

### Model 3: Expense

```python
from datetime import date

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    date = Column(Date, default=date.today)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
```

Notice `user_id` and `category_id`. These are the foreign keys we discussed in L1.

## Foreign Keys: Connecting Tables

`ForeignKey('users.id')` is the magic that connects tables.

**What it means:**

```python
user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
```

This says: "The `user_id` column must contain a value that EXISTS in the `users` table's `id` column."

**The database enforces your business rule**: Every expense must belong to a real user.

## Why Models Win: The Schema Clarity Insight

Your models provide something that text-based tools like grep never have — **schema clarity**. The database knows exactly what each field is, what type it holds, and how tables connect.

- `amount = Column(Numeric(10, 2), nullable=False)` — every tool knows this is a required exact decimal
- `user_id = Column(Integer, ForeignKey('users.id'))` — every tool knows this links to the users table
- `date = Column(Date, default=date.today)` — every tool knows this is a calendar date, not a string

Your SQLAlchemy models don't just define storage. They **describe the data** to everything that touches it — the database engine, your Python code, and any AI agent that reads your schema. This is Principle 2 (Code as Universal Interface) at its deepest level.

Schema clarity is why SQL wins. Your models provide it.

## What Comes Next

Your schema now has rules, types, and constraints. In the next lesson, the danger shifts: write paths can appear to work while silently failing under bad session discipline.

Next lesson: you validate every create/read path under explicit session and rollback discipline.

## Try With AI

### Prompt 1: Read the Code

```
Given this model:

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    in_stock = Column(Boolean, default=True)

Predict:
- What table gets created?
- What columns does it have?
- Which columns are required vs optional?
- What is the default value for in_stock?
- If I try to add a product without a name, what happens?
```

### Prompt 2: Model from Requirements

```
I need a model for a "BlogPost" with these requirements:
- id: auto-increment primary key
- title: required, text up to 200 characters
- content: required, text (no limit)
- author_id: required, must point to an authors table
- published: true/false, defaults to False
- created_at: timestamp, auto-generated
- updated_at: timestamp, auto-generated

Write the SQLAlchemy model class following the Budget Tracker pattern from this lesson.
Include the necessary imports.
```

### Prompt 3: Break Something on Purpose

```
Take the User model from this lesson:

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)

What happens if I:
1. Remove nullable=False from email and try to add a User with no email?
2. Remove unique=True and add two users with the same email?
3. Change String(100) to Integer and try to store "alice@example.com"?

For each change, predict: Will SQLAlchemy allow it? Will the database allow it?
Then show me the actual error messages I'd see.
```

### Checkpoint

Before moving to L3:

- [ ] You understand: Python class becomes database table
- [ ] You can name the 3 Budget Tracker models (User, Category, Expense)
- [ ] You know which Column type to use for: text, numbers, dates, true/false
- [ ] You can explain why money uses `Numeric(10, 2)` instead of `Float`
- [ ] You understand what ForeignKey does (enforces that referenced row exists)
- [ ] You've broken and fixed a model constraint (Prompt 3)
- [ ] You can evolve models in small, reversible steps (one schema change + one verification cycle at a time)
