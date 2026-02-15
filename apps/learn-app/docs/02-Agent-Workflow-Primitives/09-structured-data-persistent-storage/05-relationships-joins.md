---
sidebar_position: 5
title: "Relationships & Joins"
chapter: 9
lesson: 4
duration_minutes: 30
description: "Connect your tables with relationships so SQLAlchemy handles the joins for you"
keywords: ["SQLAlchemy", "relationship", "ForeignKey", "back_populates", "join", "cascade", "one-to-many", "lazy loading"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Relationship Definition"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can define bidirectional relationships using relationship() and back_populates"

  - name: "Relationship Querying"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can access related data through Python attributes (user.expenses, expense.user)"

  - name: "SQLAlchemy 2.0 Query Style"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can write queries using select() with .scalars() instead of legacy session.query()"

  - name: "Join Operations"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student understands that SQLAlchemy infers joins from relationships"

  - name: "Cascade Behavior"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can explain what cascade='all, delete-orphan' does when parent is deleted"

  - name: "AI Collaboration for Queries"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can iterate with AI to build and refine relationship queries"

learning_objectives:
  - objective: "Define relationships between models using SQLAlchemy relationship()"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student writes model code with working bidirectional relationship"

  - objective: "Use back_populates to establish bi-directional relationships"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student explains why both sides need relationship() with matching back_populates"

  - objective: "Query related data using select() and relationship attributes (SQLAlchemy 2.0 style)"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student retrieves related objects using select().where() and relationship attributes"

  - objective: "Handle foreign key constraints and cascade delete"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student predicts what happens when a parent record is deleted with cascade enabled"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (ForeignKey review, relationship(), back_populates, cascade, lazy loading, join inference, orphan handling) - appropriate for A2 with AI assistance in L4"

differentiation:
  extension_for_advanced: "Explore cascade options (cascade='save-update, merge'); implement many-to-many with association table"
  remedial_for_struggling: "Focus on User ↔ Expense relationship only; skip cascade configuration initially"
---
# Relationships & Joins

In L3, you created categories and expenses as separate records. But they're connected: every expense belongs to a category and a user.

This is where many systems become fragile: if relationships are wrong, queries look valid but return wrong truth.

In raw SQL, you'd write JOIN statements. With SQLAlchemy, you define relationships once, and then access connected data like Python attributes. No JOIN syntax needed.

## The Relationship Problem

You have three tables with foreign keys:

```
users
├── id (PK)
├── email
└── name

categories
├── id (PK)
├── name
└── color

expenses
├── id (PK)
├── user_id (FK → users.id)
├── category_id (FK → categories.id)
├── description
└── amount
```

The foreign keys create connections. But to USE those connections in Python, you need relationships.

**Without relationships:**

```python
from sqlalchemy import select

# To get a user's expenses, you'd write:
expenses = session.execute(
    select(Expense).where(Expense.user_id == user.id)
).scalars().all()
```

**With relationships:**

```python
# Just access the attribute:
expenses = user.expenses
```

Same result. Less code. SQLAlchemy handles the query.

## Defining Relationships

Add `relationship()` to your models. Here's the User model with a relationship to expenses:

```python
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)

    # Relationship: One user has many expenses
    expenses = relationship("Expense", back_populates="user")
```

**Output:**

```
No SQL generated yet - relationship() is configuration.
SQLAlchemy now knows: User.expenses will return Expense objects.
```

And the Expense model needs the other side:

```python
class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)

    # Relationships
    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")
```

**Output:**

```
Expense.user points back to User object.
Expense.category points back to Category object.
Both directions connected via back_populates.
```

Let's decode this:

| Part                             | Meaning                                                           |
| -------------------------------- | ----------------------------------------------------------------- |
| `relationship("Expense", ...)` | This User connects to Expense objects                             |
| `back_populates="user"`        | The Expense model has an attribute called `user` pointing back  |
| `relationship("User", ...)`    | This Expense connects to a User object                            |
| `back_populates="expenses"`    | The User model has an attribute called `expenses` pointing back |

**Bidirectional**: Both sides know about each other. Change one, the other reflects it.

## Complete Models with Relationships

Here's the full Budget Tracker model setup:

```python
from sqlalchemy import Column, Integer, String, Numeric, Date, DateTime, ForeignKey, create_engine, select
from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import datetime, date, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    color = Column(String(7), default="#FF6B6B")

    expenses = relationship("Expense", back_populates="category", cascade="all, delete-orphan")

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    date = Column(Date, default=date.today)

    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")
```

**Output:**

```
Three connected models:
- User has many Expenses (user.expenses)
- Category has many Expenses (category.expenses)
- Expense belongs to one User (expense.user)
- Expense belongs to one Category (expense.category)
```

## Using Relationships in Queries

With relationships defined, access related data through attributes:

### From User to Expenses

```python
with Session(engine) as session:
    user = session.execute(
        select(User).where(User.email == 'alice@example.com')
    ).scalars().first()

    # Access all expenses through relationship
    print(f"{user.name}'s expenses:")
    for expense in user.expenses:
        print(f"  ${expense.amount:.2f}: {expense.description}")
```

**Output:**

```
Alice's expenses:
  $52.50: Groceries
  $18.75: Lunch
  $45.00: Gas

SQLAlchemy generated: SELECT * FROM expenses WHERE user_id = 1
You didn't write the query - the relationship did.
```

### From Expense to User

```python
with Session(engine) as session:
    expense = session.execute(
        select(Expense).where(Expense.id == 1)
    ).scalars().first()

    # Access user through relationship
    print(f"Expense by: {expense.user.name}")
    print(f"Category: {expense.category.name}")
```

**Output:**

```
Expense by: Alice
Category: Food

Both directions work. One query, related objects available.
```

### Computing with Related Data

```python
with Session(engine) as session:
    user = session.execute(
        select(User).where(User.name == 'Alice')
    ).scalars().first()

    # Calculate total spending
    total = sum(expense.amount for expense in user.expenses)
    print(f"Total spending: ${total:.2f}")

    # Group by category
    by_category = {}
    for expense in user.expenses:
        cat = expense.category.name
        by_category[cat] = by_category.get(cat, 0) + expense.amount

    print("\nBy category:")
    for cat, amount in by_category.items():
        print(f"  {cat}: ${amount:.2f}")
```

**Output:**

```
Total spending: $116.25

By category:
  Food: $71.25
  Transportation: $45.00
```

## When You Actually Need join()

Relationships let you navigate data you already have. But sometimes you need to filter on related tables:

```python
with Session(engine) as session:
    # Find all expenses in the "Food" category
    food_expenses = session.execute(
        select(Expense).join(Category).where(Category.name == 'Food')
    ).scalars().all()

    for expense in food_expenses:
        print(f"${expense.amount}: {expense.description}")
```

**Output:**

```
$52.50: Groceries
$18.75: Lunch

SQLAlchemy inferred the join from the relationship.
You didn't write: ON expenses.category_id = categories.id
```

**When to use `.join()` vs relationship attributes:**

| Situation                     | Approach                                            |
| ----------------------------- | --------------------------------------------------- |
| Navigate from object you have | `user.expenses` (relationship)                    |
| Filter query on related table | `select(Expense).join(Category).where(Category.name == 'Food')` |
| Complex multi-table query     | `select()` with `.join()` and `.where()` conditions              |

## Cascade: What Happens on Delete?

When you delete a user, what happens to their expenses? Three options:

| Option          | What Happens                     | Use When                    |
| --------------- | -------------------------------- | --------------------------- |
| Error (default) | Delete blocked if children exist | Protect data from accidents |
| Set NULL        | Children's FK becomes NULL       | Keep orphaned records       |
| Cascade delete  | Children deleted too             | Clean removal               |

The `cascade="all, delete-orphan"` setting means:

```python
class User(Base):
    # ...
    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")
```

**What this does:**

- If user is deleted → all their expenses are deleted too
- If an expense is removed from `user.expenses` list → it's deleted from database

```python
from sqlalchemy import func

with Session(engine) as session:
    alice = session.execute(
        select(User).where(User.name == 'Alice')
    ).scalars().first()
    expense_count = len(alice.expenses)
    print(f"Alice has {expense_count} expenses")

    # Delete Alice
    session.delete(alice)
    session.commit()

    # Check expenses
    remaining = session.execute(
        select(func.count()).select_from(Expense)
    ).scalar()
    print(f"Expenses remaining: {remaining}")
```

**Output:**

```
Alice has 3 expenses
Expenses remaining: 0

All of Alice's expenses were deleted with her.
```

**Without cascade**, that delete would either:

- Fail with foreign key constraint error
- Leave orphaned expenses with invalid user_id

## Working With AI on Relationship Queries

A productive loop is: ask for a relationship-based draft, then refine constraints (sorting, missing-user behavior, output format).

```python
with Session(engine) as session:
    user = session.execute(
        select(User).where(User.name == "Alice")
    ).scalars().first()

    if not user:
        return []

    totals = {}
    for expense in user.expenses:
        cat = expense.category.name
        totals[cat] = totals.get(cat, 0) + expense.amount

    return sorted(totals.items(), key=lambda x: x[1], reverse=True)
```

Use AI for the first draft, then tighten correctness and output requirements yourself.

## What Comes Next

You can now navigate linked data. Next you must protect linked updates, because one mid-operation failure can leave your system logically broken.

## Try With AI

### Prompt 1: Predict Relationship Behavior

**What you're learning:** Understanding how relationships connect data.

```
Given this SQLAlchemy 2.0 code:

from sqlalchemy import select

user = session.execute(
    select(User).where(User.email == 'bob@example.com')
).scalars().first()
category_totals = {}
for expense in user.expenses:
    cat = expense.category.name
    category_totals[cat] = category_totals.get(cat, 0) + expense.amount
print(category_totals)

And this data:
- User: Bob (id=2)
- Categories: Food (id=1), Entertainment (id=2)
- Expenses:
  - id=5, user_id=2, category_id=1, amount=25.00, description="Lunch"
  - id=6, user_id=2, category_id=1, amount=30.00, description="Dinner"
  - id=7, user_id=2, category_id=2, amount=50.00, description="Concert"

1. What does category_totals contain at the end?
2. How many database queries does this code execute?
3. What would happen if Bob had no expenses?
```

### Prompt 2: Build a Relationship Query

**What you're learning:** Constructing queries that use relationships.

```
Write SQLAlchemy 2.0-style code to find all expenses in the "Food" category,
sorted by amount (highest first).

Requirements:
1. Use select(Expense).join(Category).where() to filter by category name
2. Return only expenses (not categories)
3. Order by amount descending
4. Print: description, amount, and the user's name who made each expense

Use the Budget Tracker models (User, Category, Expense) with relationships.
Use session.execute(select(...)).scalars() — not the legacy session.query() style.
```

### Prompt 3: Update Your Skill

**What you're learning:** Documenting relationship patterns for reuse.

```
Add to my /database-deployment skill:

## Relationships & Joins

Include:
1. How to define relationship() and back_populates (both sides)
2. When to use cascade="all, delete-orphan"
3. How to query through relationships (user.expenses)
4. When to use join() explicitly: select(Expense).join(Category).where(...)
5. SQLAlchemy 2.0 query style: session.execute(select(Model).where(...)).scalars()

Use Budget Tracker examples:
- User ↔ Expense (one-to-many)
- Category ↔ Expense (one-to-many)

All query examples must use SQLAlchemy 2.0 style (select() + execute()),
not the legacy session.query() pattern.

Format as markdown for SKILL.md.
```

After each prompt, verify:
- Prompt 1: Does your manual trace match the predicted behavior?
- Prompt 2: Is the solution fully SQLAlchemy 2.0 style (`select` + `execute`)?
- Prompt 3: Are the documented patterns reusable outside Budget Tracker?

**Safety reminder:** Cascade delete is powerful. In production, always test cascade behavior on non-production data first. A misconfigured cascade can delete more data than intended.

### Checkpoint

Before moving to L5:

- [ ] You understand: `relationship()` connects models bidirectionally
- [ ] You can access related data through attributes (`user.expenses`)
- [ ] You understand: `back_populates` links both sides of a relationship
- [ ] You know when to use `.join()` vs relationship attributes
- [ ] You can explain what `cascade="all, delete-orphan"` does
- [ ] You've iterated with AI to build a relationship query (Prompt 2)
- [ ] You've documented relationship patterns in your `/database-deployment` skill

Ready for L5: Transactions and safe multi-operation updates.
