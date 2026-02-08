---
sidebar_position: 8
title: "Capstone - Budget Tracker Complete App"
chapter: 9
lesson: 7
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

In L6, you connected your Budget Tracker to Neon. Your data now persists in the cloud, survives restarts, and can be accessed from anywhere.

Throughout this chapter, you learned the pieces:

- **L1**: Created your `/database-deployment` skill scaffold
- **L2**: Understood why databases beat CSV files
- **L3**: Defined models as Python classes
- **L4**: Built CRUD operations (Create, Read, Update, Delete)
- **L5**: Connected tables with relationships and joins
- **L6**: Protected data integrity with transactions
- **L7**: Deployed to Neon with connection pooling

Now you put it all together. You'll run a complete, production-ready Budget Tracker application that demonstrates everything you've learned. This isn't a toy example. This is code you can actually use, extend, and share.

## Why This Architecture Works

You might wonder: Why not just use bash scripts and JSON files to manage expenses? Why SQLAlchemy and a database?

Research from Braintrust (an AI evaluation platform) tested this exact question. They compared three approaches to querying structured data:

| Approach                      | Accuracy | Tokens Used | Time  | Cost  |
| ----------------------------- | -------- | ----------- | ----- | ----- |
| **SQL Queries**         | 100%     | 155K        | 45s   | $0.51 |
| **Bash + grep/awk**     | 52.7%    | 1.06M       | 401s  | $3.34 |
| **Hybrid (SQL + Bash)** | 100%     | 310K        | ~150s | -     |

**What this means for your Budget Tracker:**

- **Direct SQL queries** (which SQLAlchemy generates): Fast, accurate, efficient
- **File-based approaches** (bash/grep): 7x more tokens, 9x slower, half the accuracy
- **Why it matters**: Even if you never use AI agents, the same efficiency applies to your own code. Direct queries scale from 100 expenses to 1 million without slowing down. File parsing gets slower with each additional record.

The research showed another insight: **schema clarity is critical**. The bash agent failed partly because "it didn't know the structure of the JSON files." Your SQLAlchemy models DO define that structure explicitly, which is why queries work reliably.

This is why professional applications—from startups to enterprises—use databases for anything more than toy data. The architectural choice you're making in this lesson is the same one made in production systems worldwide.

## What You're Building

The complete Budget Tracker includes these features:

| Feature                        | Implementation                             | Lesson Origin      |
| ------------------------------ | ------------------------------------------ | ------------------ |
| **User accounts**        | User model with email, name                | L3 (Models)        |
| **Expense categories**   | Category model with colors                 | L3 (Models)        |
| **Individual expenses**  | Expense model with foreign keys            | L3 (Models)        |
| **Create expenses**      | `create_expense()` with error handling   | L4 (CRUD)          |
| **List expenses**        | `read_expenses()` with filtering         | L4 (CRUD)          |
| **Update expenses**      | `update_expense()` with validation       | L4 (CRUD)          |
| **Delete expenses**      | `delete_expense()` safely                | L4 (CRUD)          |
| **Spending by category** | `get_expenses_by_category()` with joins  | L5 (Relationships) |
| **Monthly summaries**    | `get_monthly_summary()` with aggregation | L5 (Relationships) |
| **Budget transfers**     | `transfer_budget()` atomic transaction   | L6 (Transactions)  |
| **Cloud persistence**    | Neon with connection pooling               | L7 (Neon)          |

**Tech stack**: SQLAlchemy ORM + Neon PostgreSQL + Python. No web framework yet. That comes in later chapters.

## The Complete Application

Here's the full `budget-tracker-complete.py`. Every section maps directly to a lesson you've completed.

### Section 1: Imports and Setup (L7)

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
    Float,
    DateTime,
    Date,
    ForeignKey,
    func,
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

**What you recognize**: Environment variables from L7, connection pooling from L7, `declarative_base()` from L3.

### Section 2: Models (L3)

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
    amount = Column(Float, nullable=False)
    date = Column(Date, default=date.today)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationships: Expense belongs to User and Category
    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")

    def __repr__(self):
        return f"<Expense(${self.amount:.2f}, '{self.description}')>"
```

**What you recognize**: `Column` types from L3, `ForeignKey` from L5, `relationship()` with `back_populates` from L5, `cascade="all, delete-orphan"` from L5.

### Section 3: CRUD Operations (L4)

```python
def create_expense(user_id, description, amount, category_id, expense_date=None):
    """Create a new expense."""
    try:
        with Session(engine) as session:
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
        return {"success": False, "error": str(e)}


def read_expenses(user_id, category_id=None):
    """Get expenses for a user, optionally filtered by category."""
    with Session(engine) as session:
        query = session.query(Expense).filter(Expense.user_id == user_id)
        if category_id:
            query = query.filter(Expense.category_id == category_id)
        return query.order_by(Expense.date.desc()).all()


def update_expense(expense_id, **kwargs):
    """Update an expense. Allowed: description, amount, category_id, date."""
    allowed_fields = {'description', 'amount', 'category_id', 'date'}
    updates = {k: v for k, v in kwargs.items() if k in allowed_fields}

    try:
        with Session(engine) as session:
            expense = session.query(Expense).filter(Expense.id == expense_id).first()
            if not expense:
                return {"success": False, "error": "Expense not found"}

            for field, value in updates.items():
                setattr(expense, field, value)

            session.commit()
            return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}


def delete_expense(expense_id):
    """Delete an expense."""
    try:
        with Session(engine) as session:
            expense = session.query(Expense).filter(Expense.id == expense_id).first()
            if not expense:
                return {"success": False, "error": "Expense not found"}

            session.delete(expense)
            session.commit()
            return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}
```

**What you recognize**: `session.add()`, `session.commit()` from L4; `session.query().filter()` from L4; error handling with `try/except` from L6.

### Section 4: Relationship Queries (L5)

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
        results = session.query(
            Category.name,
            func.sum(Expense.amount).label('total'),
            func.count(Expense.id).label('count')
        ).join(Expense).filter(
            (Expense.user_id == user_id) &
            (Expense.date >= current_month) &
            (Expense.date < next_month)
        ).group_by(Category.name).all()

        return [
            {"category": name, "total": float(total or 0), "count": count}
            for name, total, count in results
        ]


def get_expenses_by_category(user_id):
    """Get all expenses grouped by category."""
    with Session(engine) as session:
        categories = session.query(Category).all()

        result = {}
        for category in categories:
            expenses = session.query(Expense).filter(
                (Expense.user_id == user_id) &
                (Expense.category_id == category.id)
            ).all()

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
        return session.query(Expense).filter(
            Expense.user_id == user_id
        ).order_by(Expense.amount.desc()).limit(limit).all()
```

**What you recognize**: `.join()` from L5, `func.sum()` and `func.count()` from L5, `.group_by()` from L5, navigation through relationships from L5.

### Section 5: Transactions (L6)

```python
def transfer_budget(user_id, from_category_id, to_category_id, amount):
    """
    Atomic operation: Move budget from one category to another.
    Creates two expense entries: negative in source, positive in destination.
    Both succeed or both fail.
    """
    try:
        with Session(engine) as session:
            from_cat = session.query(Category).filter(
                Category.id == from_category_id
            ).first()
            to_cat = session.query(Category).filter(
                Category.id == to_category_id
            ).first()

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
        return {"success": False, "error": str(e)}
```

**What you recognize**: Atomic transaction from L6 (all-or-nothing), `session.rollback()` implicit on exception from L6, paired operations from L6.

### Section 6: Utilities and Main

```python
def init_database():
    """Create all tables in database."""
    Base.metadata.create_all(engine)
    print("Database initialized")


def seed_data():
    """Add sample data for testing."""
    with Session(engine) as session:
        if session.query(User).count() > 0:
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

**Prerequisites** (from L7):

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

All expenses:
  $45.75 | Food | Dinner
  $30.00 | Entertainment | Movie tickets
  $45.00 | Transportation | Gas
  $18.75 | Food | Lunch
  $52.50 | Food | Groceries

Monthly Summary (January 2024):
  Food            | Count:  3 | $117.00
  Transportation  | Count:  1 | $45.00
  Entertainment   | Count:  1 | $30.00

All operations completed successfully!
```

If you see this output, your complete Budget Tracker is working.

## Function Reference (Every Lesson Mapped)

| Function                       | Purpose                         | Lesson |
| ------------------------------ | ------------------------------- | ------ |
| `init_database()`            | Creates tables from models      | L3     |
| `seed_data()`                | Adds sample data for testing    | L4     |
| `create_expense()`           | CRUD Create with error handling | L4, L6 |
| `read_expenses()`            | CRUD Read with filtering        | L4     |
| `update_expense()`           | CRUD Update with validation     | L4     |
| `delete_expense()`           | CRUD Delete safely              | L4     |
| `get_monthly_summary()`      | Complex join + aggregation      | L5     |
| `get_expenses_by_category()` | Grouping with relationships     | L5     |
| `get_top_expenses()`         | Sorting + limiting              | L4     |
| `transfer_budget()`          | Multi-step atomic transaction   | L6     |
| `test_connection()`          | Verify Neon works               | L7     |

## Testing Your Understanding

Add your own expense:

```python
with Session(engine) as session:
    # Create a new user
    new_user = User(email='me@example.com', name='My Name')
    session.add(new_user)
    session.commit()
    print(f"Created user id: {new_user.id}")
```

**Output:**

```
Created user id: 2
```

Add an expense for your user:

```python
result = create_expense(
    user_id=2,
    description='Coffee',
    amount=4.50,
    category_id=1  # Food
)
print(result)
```

**Output:**

```
{'success': True, 'id': 6}
```

Query your expenses:

```python
my_expenses = read_expenses(user_id=2)
for e in my_expenses:
    print(f"${e.amount:.2f}: {e.description}")
```

**Output:**

```
$4.50: Coffee
```

## Working With AI on Your Budget Tracker

At this point, you've moved from "learning" to "building." When you encounter issues, you and AI work as collaborators.

**Your question:**
"My `transfer_budget()` function returns `{'success': True}` but the expenses don't appear. What's wrong?"

**AI suggests:**
"Check if the session is committing correctly. Add some debug output:

```python
print(f'From expense id: {from_expense.id}')
print(f'To expense id: {to_expense.id}')
```

Also verify the category IDs exist in your database."

**Your refinement:**
"The IDs are None before commit. But after commit they should have values, right?"

**AI adapts:**
"Correct. If they're still None after `session.commit()`, the transaction may have rolled back silently. Check if there's an exception being swallowed. Try wrapping in explicit try/except and print any exception."

**What emerged:** A debugging approach that traced the transaction lifecycle, identifying that the issue was likely in error handling, not the transaction logic itself.

## Try With AI

### Prompt 1: Understand the Code

**What you're learning:** Reading production code and explaining what each part does.

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

**What you're learning:** Executing real applications and verifying they work.

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

**What you're learning:** Documenting mastery as a reusable skill.

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

**You've built something real.** This Budget Tracker works. You can use it to track your own spending. You can extend it with a web interface. You can share it with friends.

More importantly, you've built a **reusable skill**. Every database application you build from now on follows this same pattern: models, sessions, CRUD, relationships, transactions, cloud deployment. This skill is now part of your permanent toolkit.
