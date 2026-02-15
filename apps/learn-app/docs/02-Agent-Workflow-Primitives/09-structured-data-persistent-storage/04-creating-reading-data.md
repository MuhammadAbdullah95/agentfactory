---
sidebar_position: 4
title: "Creating & Reading Data"
chapter: 9
lesson: 3
duration_minutes: 25
description: "Create and query database records using SQLAlchemy sessions - your conversation with the database"
keywords: ["SQLAlchemy", "session", "CRUD", "create", "read", "query", "filter", "add", "commit", "context manager"]
---
# Creating & Reading Data

> **Continuity bridge**
> - From Chapter 7: workflows were file operations.
> - From Chapter 8: scripts computed deterministic answers.
> - Now in Chapter 9: you must persist and query those answers safely through sessions.

**Principle anchor:** P3 (Verification as Core Step). Writes are not trusted until commit and post-check.

In L2, you defined three models: User, Category, Expense. Python classes that become database tables.

But schema alone is inert. You now need to prove data can be written, queried, and trusted.

This is where sessions come in. A session is your conversation with the database. You open it, ask questions or make changes, and close it. Think of it like a phone call: you dial (open session), talk (run queries), and hang up (close session).

## Setting Up: Engine and Session

Before you can talk to a database, you need two things:

**1. Engine**: The connection to your database

```python
from sqlalchemy import create_engine, event

# For learning, use SQLite in memory (no setup needed)
engine = create_engine('sqlite:///:memory:')

# Important: SQLite does NOT enforce foreign keys unless explicitly enabled.
@event.listens_for(engine, "connect")
def _enable_sqlite_fk(dbapi_connection, _connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
```

**2. Tables Created**: Tell SQLAlchemy to build the actual tables

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# ... your model classes here (User, Category, Expense) ...

# Create all tables from your models
Base.metadata.create_all(engine)
```

**3. Session**: Your conversation tool

```python
from sqlalchemy.orm import Session

# You'll use: with Session(engine) as session:
```

Now you're ready to create and read data.

## Creating Records (CREATE)

The pattern for adding data is always the same:

```python
with Session(engine) as session:
    # 1. Create Python object
    category = Category(name='Food', color='#FF6B6B')

    # 2. Tell session to track it
    session.add(category)

    # 3. Save to database
    session.commit()
```

Let's break this down:

| Step          | Code                                 | What It Does                               |
| ------------- | ------------------------------------ | ------------------------------------------ |
| Open session  | `with Session(engine) as session:` | Start conversation with database           |
| Create object | `Category(name='Food', ...)`       | Make a Python object (not in database yet) |
| Track it      | `session.add(category)`            | Tell session "I want to save this"         |
| Save          | `session.commit()`                 | Actually write to database                 |
| Close         | (automatic)                          | End of `with` block closes session       |

**Creating multiple records at once:**

```python
with Session(engine) as session:
    categories = [
        Category(name='Food', color='#FF6B6B'),
        Category(name='Transportation', color='#4ECDC4'),
        Category(name='Entertainment', color='#95E1D3'),
    ]
    session.add_all(categories)  # add_all for lists
    session.commit()
```

## Reading Records (READ)

Reading data uses the `select()` function. You build a query with `select()`, execute it with `session.execute()`, and extract results with `.scalars()`:

```python
from sqlalchemy import select

result = session.execute(select(Model)).scalars().all()
```

> **Note:** Older tutorials use `session.query()`. This still works but `select()` is the recommended 2.0 approach. All examples in this course use the modern `select()` pattern.

### Get All Records

```python
from sqlalchemy import select

with Session(engine) as session:
    all_categories = session.execute(select(Category)).scalars().all()

    for cat in all_categories:
        print(f"{cat.id}: {cat.name}")
```

### Get One Record by Condition

```python
from sqlalchemy import select

with Session(engine) as session:
    food = session.execute(
        select(Category).where(Category.name == 'Food')
    ).scalars().first()

    print(f"Found: {food.name}, color: {food.color}")
```

### Filter with Conditions

```python
from sqlalchemy import select

with Session(engine) as session:
    # Find expenses >= $50
    big_expenses = session.execute(
        select(Expense).where(Expense.amount >= 50)
    ).scalars().all()

    print(f"Found {len(big_expenses)} expenses over $50")
```

## Optional Extension: Useful Query Variations

Use these once core create/read flow is stable:

```python
# AND filters
select(Expense).where(Expense.category_id == 1, Expense.amount > 20)

# ORDER BY
select(Expense).order_by(Expense.date.desc())

# LIMIT
select(Expense).limit(5)
```

Rule of thumb:
- `.scalars().all()` when you expect a list
- `.scalars().first()` when you expect one row or `None`

## Error Handling

What happens when you try to add invalid data?

This example assumes foreign key checks are enabled for SQLite as shown in the setup section above.

```python
with Session(engine) as session:
    try:
        # This will fail if user 999 doesn't exist
        expense = Expense(
            user_id=999,  # No user with id=999
            category_id=1,
            description="Test",
            amount=50.00
        )
        session.add(expense)
        session.commit()  # Error happens here!

    except Exception as e:
        print(f"Error: {e}")
        session.rollback()  # Explicit rollback keeps session state clean
```

**Key insight**: `with Session(...)` guarantees session closure. It does not replace explicit rollback in your exception path.

1. `rollback()` resets the failed transaction state
2. Session closes properly at block exit
3. Database remains consistent

## Complete Example: Budget Tracker CRUD

Here's a working example that creates and reads Budget Tracker data:

```python
from datetime import date
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

# ... (models defined: User, Category, Expense) ...

# Setup
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# CREATE: Add sample data
with Session(engine) as session:
    # Create user
    user = User(email='alice@example.com', name='Alice')
    session.add(user)

    # Create categories
    categories = [
        Category(name='Food', color='#FF6B6B'),
        Category(name='Transport', color='#4ECDC4'),
    ]
    session.add_all(categories)
    session.flush()  # Get IDs without committing

    # Create expenses
    expenses = [
        Expense(
            user_id=user.id,
            category_id=categories[0].id,
            description='Groceries',
            amount=52.50,
            date=date(2024, 1, 15)
        ),
        Expense(
            user_id=user.id,
            category_id=categories[1].id,
            description='Gas',
            amount=45.00,
            date=date(2024, 1, 16)
        ),
    ]
    session.add_all(expenses)
    session.commit()

# READ: Query the data
with Session(engine) as session:
    # All categories
    print("Categories:")
    for cat in session.execute(select(Category)).scalars():
        print(f"  {cat.id}: {cat.name}")

    # Expenses over $50
    print("\nExpenses over $50:")
    big = session.execute(
        select(Expense).where(Expense.amount > 50)
    ).scalars().all()
    for exp in big:
        print(f"  ${exp.amount}: {exp.description}")
```

## What Comes Next

You can now write and read safely. Next comes the harder step: relationship design, where one wrong link can produce plausible but incorrect analytics.

Next lesson: you will prove that joins and relationship mappings are either correct by design or dangerously misleading.

## Try With AI

### Prompt 1: Predict Query Results

**What you're learning:** Understanding how queries filter data.

```
Given this database state:
- Categories: Food (id=1), Transport (id=2), Entertainment (id=3)
- Expenses:
  - id=1, category_id=1, amount=52.50, description="Groceries"
  - id=2, category_id=1, amount=18.75, description="Lunch"
  - id=3, category_id=2, amount=45.00, description="Gas"
  - id=4, category_id=3, amount=30.00, description="Movie"

Predict the output of each query:

1. session.execute(select(Expense).where(Expense.category_id == 1)).scalars().all()
   How many results? What are they?

2. session.execute(select(Expense).where(Expense.amount >= 50)).scalars().first()
   What single record is returned?

3. session.execute(select(Category).where(Category.name == 'Shopping')).scalars().first()
   What is returned and why?
```

### Prompt 2: Implement CRUD Code

```
Write SQLAlchemy code to:

1. Create a new Category named "Utilities" with color "#F38181"

2. Create an Expense:
   - user_id: 1
   - category_id: 4 (Utilities)
   - description: "Electric bill"
   - amount: 125.00

3. Query all expenses with amount > 100

4. Query the "Utilities" category by name

Use the session context manager pattern from this lesson.
Show the expected output for each operation.
```

### Prompt 3: Refine Skill Patterns

```
Add to my /database-deployment skill:

## CRUD Operations: Create & Read

Include these patterns with examples:
1. Session context manager pattern (with Session as session)
2. Create single record (session.add + commit)
3. Create multiple records (session.add_all + commit)
4. Query all (select() with .scalars().all())
5. Query with filter (select().where() with .scalars().first())
6. Error handling (try/except around commit)

Use Budget Tracker examples (Category, Expense).
Format as markdown for SKILL.md.
```

After each prompt, verify the result yourself:
- Prompt 1: Do your predicted query outputs match?
- Prompt 2: Does the code use `with Session(engine)` and `commit()` for writes?
- Prompt 3: Add the refined section to `/database-deployment/SKILL.md`.

**Safety reminder:** When working with real databases, always verify your queries on a small dataset first. A query without a filter (like `.all()` on millions of rows) can crash your program or overload your database.

### Checkpoint

Before moving to L4:

- [ ] You understand: Session = conversation with database
- [ ] You can create records (session.add + session.commit)
- [ ] You can query all records (select() with .scalars().all())
- [ ] You can filter records (select().where() with .scalars().first())
- [ ] You know the difference between .all() (list) and .first() (one or None)
- [ ] You understand: rollback must be explicit before reusing failed session logic
- [ ] You can turn on query observability (`echo=True`/SQL logging) when debugging unexpected results
- [ ] You've written CRUD code (Prompt 2)
- [ ] You've updated your /database-deployment skill with CRUD patterns

Ready for L4: Relationships and joins.
