---
sidebar_position: 9
title: "Capstone - Budget Tracker Complete App"
chapter: 9
lesson: 8
duration_minutes: 40
description: "Build and run the complete Budget Tracker application integrating models, CRUD operations, relationships, transactions, and Neon deployment"
keywords: ["capstone", "budget tracker", "SQLAlchemy", "Neon", "complete application", "integration", "CRUD", "transactions", "relationships", "production"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Full Application Integration"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can combine all chapter patterns into a working multi-table application"

  - name: "Code Reading and Comprehension"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can read production code and explain what each function does"

  - name: "Production Python Application"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can execute complete Python applications with database backends"

  - name: "Skill Documentation"
    proficiency_level: "A2"
    category: "Soft"
    bloom_level: "Create"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student can finalize and document reusable technical skills"

  - name: "Database Application Testing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can verify database operations work correctly through testing"

learning_objectives:
  - objective: "Build complete multi-table Budget Tracker application integrating all chapter patterns"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student runs complete budget-tracker.py and sees all operations succeed"

  - objective: "Implement all CRUD operations plus complex queries in a single application"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student can explain and modify each CRUD function"

  - objective: "Use relationships, transactions, and error handling together"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student successfully executes transfer_budget and explains atomicity"

  - objective: "Deploy and test application on Neon"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Application runs against Neon database with visible results"

  - objective: "Refine and own the /database-deployment skill"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student finalizes skill documentation with complete example and decision guide"

cognitive_load:
  new_concepts: 0
  assessment: "0 new concepts - this lesson integrates 8 previously taught concepts (Models, Sessions, Relationships, Transactions, Queries, Pooling, Error Handling, Testing) into one working application"

differentiation:
  extension_for_advanced: "Add features: spending trends visualization, budget limits with alerts, recurring expenses, multi-user support with authentication"
  remedial_for_struggling: "Start with basic CRUD only (create expense, list expenses); skip monthly summaries and category grouping until core works"
---
# Capstone - Budget Tracker Complete App

Throughout this chapter, you learned every piece of the database puzzle:

- **L0**: Understood why databases beat CSV files
- **L1**: Created your `/database-deployment` skill scaffold
- **L2**: Defined models as Python classes
- **L3**: Built CRUD operations (Create, Read, Update, Delete)
- **L4**: Connected tables with relationships and joins
- **L5**: Protected data integrity with transactions
- **L6**: Deployed to Neon with connection pooling
- **L7**: Learned hybrid SQL + bash verification patterns

Now you put it all together: one complete Budget Tracker that you can run, extend, and reuse.

## Why This Architecture Works

This architecture works because schema clarity removes guesswork: models define structure, queries stay explicit, and transactions protect consistency.

Looking back across Part 2, each tool has a clear role:

| Data Task | Best Tool | Why | Learned In |
|-----------|-----------|-----|------------|
| File manipulation | Bash | Native, fast, universal | File Processing |
| Computation | Python | Deterministic, decimal-safe | Computation & Data Extraction |
| Structured queries | SQL (SQLAlchemy) | Schema-aware, 100% accuracy | This chapter |
| Exploration + verification | Hybrid (SQL + bash) | Self-checking, catches edge cases | L7 (Hybrid Patterns) |

### Tool Escalation Ladder (Chapter 7 -> 8 -> 9)

1. **Bash** for files and text workflows (Chapter 7)
2. **Python** for deterministic computation and robust parsing (Chapter 8)
3. **SQL (SQLAlchemy)** for schema-aware structured queries (Chapter 9)
4. **Hybrid** for high-stakes verification where wrong answers are costly

In production, this means agents query schema-aware data instead of guessing from text files. L7 added verification; L8 integrates everything.

## What You're Building

The complete Budget Tracker includes these features:

| Feature                        | Implementation                             | Lesson Origin      |
| ------------------------------ | ------------------------------------------ | ------------------ |
| **User accounts**        | User model with email, name                | L2 (Models)        |
| **Expense categories**   | Category model with colors                 | L2 (Models)        |
| **Individual expenses**  | Expense model with foreign keys            | L2 (Models)        |
| **Create expenses**      | `create_expense()` with error handling     | L3 (CRUD)          |
| **List expenses**        | `read_expenses()` with filtering           | L3 (CRUD)          |
| **Update expenses**      | `update_expense()` with validation         | L3 (CRUD)          |
| **Delete expenses**      | `delete_expense()` safely                  | L3 (CRUD)          |
| **Spending by category** | `get_expenses_by_category()` with joins    | L4 (Relationships) |
| **Monthly summaries**    | `get_monthly_summary()` with aggregation   | L4 (Relationships) |
| **Budget transfers**     | `transfer_budget()` atomic transaction     | L5 (Transactions)  |
| **Cloud persistence**    | Neon with connection pooling               | L6 (Neon)          |

**Tech stack**: SQLAlchemy ORM + Neon PostgreSQL + Python. No web framework yet. That comes in later chapters.

## The Complete Application

Here's the full `budget-tracker-complete.py`. Every section maps directly to a lesson you've completed.

### Section 1: Imports and Setup (L6)

```python
"""
Complete Budget Tracker Application using SQLAlchemy ORM and Neon PostgreSQL
"""

import os
from datetime import datetime, date, timezone
from dotenv import load_dotenv
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Numeric,
    DateTime,
    Date,
    ForeignKey,
    func,
    select,
    text,
)
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy.pool import QueuePool

# Load environment variables
load_dotenv()

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in .env file")

# Engine with connection pooling
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_recycle=3600,
    pool_pre_ping=True,
    echo=False  # Set to True for SQL debugging
)

Base = declarative_base()
```

This section combines L2 foundations with L6 deployment setup.

### Section 2: Models (L2)

```python
class User(Base):
    """User account for budget tracking."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationship: User has many expenses
    expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"


class Category(Base):
    """Budget categories (Food, Transportation, Entertainment, etc.)."""
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    color = Column(String(7), default="#FF6B6B")

    # Relationship: Category has many expenses
    expenses = relationship("Expense", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Category(name='{self.name}')>"


class Expense(Base):
    """Individual expense entry."""
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Numeric(10, 2), nullable=False)
    date = Column(Date, default=date.today)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships: Expense belongs to User and Category
    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")

    def __repr__(self):
        return f"<Expense(${self.amount:.2f}, '{self.description}')>"
```

This section is your L2/L4 data model in final form.

### Section 3: CRUD Operations (L3)

```python
def create_expense(user_id, description, amount, category_id, expense_date=None):
    """Create a new expense."""
    with Session(engine) as session:
        try:
            expense = Expense(
                user_id=user_id,
                description=description,
                amount=amount,
                category_id=category_id,
                date=expense_date or date.today()
            )
            session.add(expense)
            session.commit()
            return {"success": True, "id": expense.id}
        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}


def read_expenses(user_id, category_id=None):
    """Get expenses for a user, optionally filtered by category."""
    with Session(engine) as session:
        stmt = select(Expense).where(Expense.user_id == user_id)
        if category_id:
            stmt = stmt.where(Expense.category_id == category_id)
        return session.execute(stmt.order_by(Expense.date.desc())).scalars().all()


def update_expense(expense_id, **kwargs):
    """Update an expense. Allowed: description, amount, category_id, date."""
    allowed_fields = {'description', 'amount', 'category_id', 'date'}
    updates = {k: v for k, v in kwargs.items() if k in allowed_fields}

    with Session(engine) as session:
        try:
            expense = session.execute(
                select(Expense).where(Expense.id == expense_id)
            ).scalars().first()
            if not expense:
                return {"success": False, "error": "Expense not found"}

            for field, value in updates.items():
                setattr(expense, field, value)

            session.commit()
            return {"success": True}
        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}


def delete_expense(expense_id):
    """Delete an expense."""
    with Session(engine) as session:
        try:
            expense = session.execute(
                select(Expense).where(Expense.id == expense_id)
            ).scalars().first()
            if not expense:
                return {"success": False, "error": "Expense not found"}

            session.delete(expense)
            session.commit()
            return {"success": True}
        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}
```

This section applies L3 CRUD patterns with L5-style safety.

### Section 4: Relationship Queries (L4)

```python
def get_monthly_summary(user_id, year, month):
    """Get spending summary grouped by category for a specific month."""
    with Session(engine) as session:
        # Calculate date range
        if month == 12:
            next_month = date(year + 1, 1, 1)
        else:
            next_month = date(year, month + 1, 1)
        current_month = date(year, month, 1)

        # Query: sum amount by category with join
        stmt = select(
            Category.name,
            func.sum(Expense.amount).label('total'),
            func.count(Expense.id).label('count')
        ).join(Expense).where(
            (Expense.user_id == user_id) &
            (Expense.date >= current_month) &
            (Expense.date < next_month)
        ).group_by(Category.name)
        results = session.execute(stmt).all()

        return [
            {"category": name, "total": float(total or 0), "count": count}
            for name, total, count in results
        ]


def get_expenses_by_category(user_id):
    """Get all expenses grouped by category."""
    with Session(engine) as session:
        categories = session.execute(select(Category)).scalars().all()

        result = {}
        for category in categories:
            expenses = session.execute(
                select(Expense).where(
                    (Expense.user_id == user_id) &
                    (Expense.category_id == category.id)
                )
            ).scalars().all()

            result[category.name] = {
                "count": len(expenses),
                "total": sum(e.amount for e in expenses),
                "expenses": [
                    {"id": e.id, "description": e.description,
                     "amount": e.amount, "date": e.date.isoformat()}
                    for e in expenses
                ]
            }

        return result


def get_top_expenses(user_id, limit=10):
    """Get the highest-value expenses."""
    with Session(engine) as session:
        return session.execute(
            select(Expense).where(
                Expense.user_id == user_id
            ).order_by(Expense.amount.desc()).limit(limit)
        ).scalars().all()
```

This section is the L4 query layer: joins, grouping, and aggregations.

### Section 5: Transactions (L5)

```python
def transfer_budget(user_id, from_category_id, to_category_id, amount):
    """
    Atomic operation: Move budget from one category to another.
    Creates two expense entries: negative in source, positive in destination.
    Both succeed or both fail.
    """
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

            # Create BOTH transactions atomically
            from_expense = Expense(
                user_id=user_id,
                category_id=from_category_id,
                description=f"Transfer to {to_cat.name}",
                amount=-amount
            )
            to_expense = Expense(
                user_id=user_id,
                category_id=to_category_id,
                description=f"Transfer from {from_cat.name}",
                amount=amount
            )

            session.add(from_expense)
            session.add(to_expense)
            session.commit()  # Both succeed or both fail

            return {"success": True}
        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}
```

This section is the L5 atomic transaction pattern in production form.

### Section 6: Utilities and Main

```python
def init_database():
    """Create all tables in database."""
    Base.metadata.create_all(engine)
    print("Database initialized")


def seed_data():
    """Add sample data for testing."""
    with Session(engine) as session:
        if session.execute(select(func.count()).select_from(User)).scalar() > 0:
            print("Database already has data, skipping seed")
            return

        user = User(email="alice@example.com", name="Alice Smith")
        session.add(user)

        categories = [
            Category(name="Food", color="#FF6B6B"),
            Category(name="Transportation", color="#4ECDC4"),
            Category(name="Entertainment", color="#95E1D3"),
            Category(name="Utilities", color="#F38181"),
        ]
        session.add_all(categories)
        session.flush()

        expenses = [
            Expense(user_id=user.id, category_id=categories[0].id,
                    description="Groceries", amount=52.50, date=date(2024, 1, 15)),
            Expense(user_id=user.id, category_id=categories[0].id,
                    description="Lunch", amount=18.75, date=date(2024, 1, 16)),
            Expense(user_id=user.id, category_id=categories[1].id,
                    description="Gas", amount=45.00, date=date(2024, 1, 17)),
            Expense(user_id=user.id, category_id=categories[2].id,
                    description="Movie tickets", amount=30.00, date=date(2024, 1, 18)),
        ]
        session.add_all(expenses)
        session.commit()
        print("Sample data added")


def test_connection():
    """Test database connection."""
    try:
        with Session(engine) as session:
            session.execute(text("SELECT 1"))
            print("Database connection successful")
            return True
    except Exception as e:
        print(f"Connection failed: {e}")
        return False


if __name__ == "__main__":
    init_database()
    if not test_connection():
        exit(1)
    seed_data()

    user_id = 1

    # Create new expense
    print("\nCreating new expense...")
    result = create_expense(user_id, "Dinner", 45.75, 1)
    print(f"Result: {result}")

    # List expenses
    print("\nAll expenses:")
    expenses = read_expenses(user_id)
    for e in expenses:
        print(f"  ${e.amount:.2f} | {e.category.name} | {e.description}")

    # Monthly summary
    print("\nMonthly Summary (January 2024):")
    summary = get_monthly_summary(user_id, 2024, 1)
    for item in summary:
        print(f"  {item['category']:15} | Count: {item['count']:2} | ${item['total']:.2f}")

    print("\nAll operations completed successfully!")
```

## Running the Application

**Prerequisites** (from L6):

1. Neon account with project created
2. `.env` file with `DATABASE_URL`
3. Dependencies installed

**Install dependencies**:

```bash
pip install sqlalchemy psycopg2-binary python-dotenv
```

Or with uv:

```bash
uv add sqlalchemy psycopg2-binary python-dotenv
```

**Run the application**:

```bash
python budget-tracker-complete.py
```

**Output:**

```
Database initialized
Database connection successful
Sample data added

Creating new expense...
Result: {'success': True, 'id': 5}
All operations completed successfully!
```

If you see this output, your complete Budget Tracker is working.

## Testing Your Understanding

Run this short self-test:

1. Create a second user.
2. Add one expense for that user with `create_expense()`.
3. Query that user's expenses with `read_expenses()`.
4. Verify the record appears with the expected amount and category.

## Working With AI on Your Budget Tracker

At this point, the workflow is practical debugging:

1. Confirm transaction inputs (user/category IDs, amount).
2. Confirm commit path executes.
3. Confirm no exception is swallowed before rollback.
4. Re-query database state after operation.

This loop catches most "success but no data" issues quickly.

## Try With AI

### Prompt 1: Understand the Code

```
Read the complete budget-tracker-complete.py code.

Answer these questions:
1. What does transfer_budget() do? Why does it create TWO expenses?
2. Why does it use try/except? What happens if an error occurs?
3. What happens if you try to transfer from a category that doesn't exist?
4. How many expenses can a single user have? (Hint: look at the relationship)
5. How would you add a "notes" field to expenses?

For each answer, point to the specific line of code that proves your answer.
```

After AI explains, verify: Can you trace through `transfer_budget()` line by line and explain what each line does?

### Prompt 2: Run and Verify

```
Help me run the Budget Tracker application:

1. I have my .env file with DATABASE_URL from L6
2. Walk me through:
   - Installing dependencies (pip or uv)
   - Running python budget-tracker-complete.py
   - Verifying the output matches expected
   - Checking Neon dashboard for the data

If I get errors:
- Connection failed? → Check DATABASE_URL format
- No module 'psycopg2'? → Install psycopg2-binary
- Import error? → Install sqlalchemy

Report back with the exact output you see.
```

After completing, verify: Do you see "All operations completed successfully!" in your terminal?

### Prompt 3: Finalize Your Skill

```
My /database-deployment skill has grown throughout this chapter. Help me finalize it.

Add these sections:
1. **Complete Example**: budget-tracker-complete.py as reference
2. **Decision Guide**:
   - When to use models (defining structure)
   - When to use relationships (connected data)
   - When transactions are critical (data integrity)
   - When to use pooling (production deployments)
3. **Troubleshooting**: Common errors I learned to fix
4. **Chapter Checklist**: All the skills I mastered

End with: "This skill is production-ready for any SQLAlchemy + Neon project."
```

After AI responds, verify: Could you use this skill to build a completely different database application (not Budget Tracker)?

## Checkpoint: Chapter Complete

Before finishing this chapter, verify your mastery:

- [ ] I understand every function in budget-tracker-complete.py
- [ ] I can run the app on Neon (or explain exactly where I got stuck)
- [ ] I can add a new function (e.g., `get_spending_by_month_chart()`)
- [ ] I can modify a model (e.g., add `notes` field to Expense)
- [ ] My `/database-deployment` skill is finalized with complete example
- [ ] I can explain why transactions matter (atomic = all or nothing)
- [ ] I can explain why pooling matters (connection reuse, cloud limits)

This capstone proves you can build and ship a complete SQLAlchemy + Neon workflow. More importantly, you now have a reusable skill template for future database projects.

**Next up**: The [Chapter Quiz](./11-chapter-quiz.md) to test your mastery of everything you've learned — from models and CRUD to hybrid verification patterns.
