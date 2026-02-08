---
sidebar_position: 4
title: "Creating & Reading Data"
chapter: 9
lesson: 3
duration_minutes: 25
description: "Create and query database records using SQLAlchemy sessions - your conversation with the database"
keywords: ["SQLAlchemy", "session", "CRUD", "create", "read", "query", "filter", "add", "commit", "context manager"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Session Management"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can explain what a session does and use context manager pattern (with Session)"

  - name: "Record Creation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can create new records using session.add() and session.commit()"

  - name: "Basic Querying"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can retrieve records using session.query().all() and session.query().filter().first()"

  - name: "Query Filtering"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can filter query results using .filter() with basic conditions"

  - name: "Database Error Handling"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student understands that invalid data causes exceptions and sessions auto-rollback on error"

learning_objectives:
  - objective: "Establish SQLAlchemy sessions and database connections"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student explains what Engine, Session, and context manager do in their own words"

  - objective: "Create new records using session.add() and session.commit()"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student writes working code to create a Category and an Expense"

  - objective: "Read records with session.query() and filtering"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student writes queries that retrieve all records and filtered subsets"

  - objective: "Handle basic database errors"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student explains what happens when invalid data is added and how to catch it"

cognitive_load:
  new_concepts: 6
  assessment: "6 new concepts (Engine, Session, context manager, session.add, session.query, filter syntax) - appropriate for A2 with heavy scaffolding"

differentiation:
  extension_for_advanced: "Add multiple query patterns: filter with AND/OR, order_by, limit, offset for pagination"
  remedial_for_struggling: "Simplify to: Create one record, query all records (skip filters initially)"
---
# Creating & Reading Data

In L2, you defined three models: User, Category, Expense. Python classes that become database tables.

But here's the thing: defining a table doesn't put data in it. You have an empty database with a perfect structure. Now you need to actually CREATE records and READ them back.

This is where sessions come in. A session is your conversation with the database. You open it, ask questions or make changes, and close it. Think of it like a phone call: you dial (open session), talk (run queries), and hang up (close session).

## Setting Up: Engine and Session

Before you can talk to a database, you need two things:

**1. Engine**: The connection to your database

```python
from sqlalchemy import create_engine

# For learning, use SQLite in memory (no setup needed)
engine = create_engine('sqlite:///:memory:')
```

**Output:**

```
Engine created: points to in-memory SQLite database
No files, no servers - data lives in RAM for this lesson
```

**2. Tables Created**: Tell SQLAlchemy to build the actual tables

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# ... your model classes here (User, Category, Expense) ...

# Create all tables from your models
Base.metadata.create_all(engine)
```

**Output:**

```
CREATE TABLE users (id INTEGER PRIMARY KEY, email VARCHAR(100), ...)
CREATE TABLE categories (id INTEGER PRIMARY KEY, name VARCHAR(50), ...)
CREATE TABLE expenses (id INTEGER PRIMARY KEY, user_id INTEGER, ...)

Three empty tables now exist in the database.
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

**Output:**

```
INSERT INTO categories (name, color) VALUES ('Food', '#FF6B6B')

category.id is now 1 (auto-assigned by database)
Session closes automatically at end of 'with' block
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

**Output:**

```
INSERT INTO categories (name, color) VALUES ('Food', '#FF6B6B')
INSERT INTO categories (name, color) VALUES ('Transportation', '#4ECDC4')
INSERT INTO categories (name, color) VALUES ('Entertainment', '#95E1D3')

3 categories created with ids 1, 2, 3
```

## Reading Records (READ)

The pattern for reading data: `session.query(Model).method()`

### Get All Records

```python
with Session(engine) as session:
    all_categories = session.query(Category).all()

    for cat in all_categories:
        print(f"{cat.id}: {cat.name}")
```

**Output:**

```
1: Food
2: Transportation
3: Entertainment

all_categories is a Python list of Category objects
```

### Get One Record by Condition

```python
with Session(engine) as session:
    food = session.query(Category).filter(
        Category.name == 'Food'
    ).first()

    print(f"Found: {food.name}, color: {food.color}")
```

**Output:**

```
Found: Food, color: #FF6B6B

.first() returns the first match or None if nothing found
```

### Filter with Conditions

```python
with Session(engine) as session:
    # Find expenses >= $50
    big_expenses = session.query(Expense).filter(
        Expense.amount >= 50
    ).all()

    print(f"Found {len(big_expenses)} expenses over $50")
```

**Output:**

```
Found 2 expenses over $50

.filter() accepts comparison operators: ==, !=, >, <, >=, <=
```

### Multiple Filters (AND)

```python
with Session(engine) as session:
    # Food expenses over $20
    food_expenses = session.query(Expense).filter(
        Expense.category_id == 1,
        Expense.amount > 20
    ).all()
```

**Output:**

```
SELECT * FROM expenses WHERE category_id = 1 AND amount > 20

Multiple conditions in filter() are ANDed together
```

### Ordering Results

```python
with Session(engine) as session:
    # Newest expenses first
    recent = session.query(Expense).order_by(
        Expense.date.desc()
    ).all()
```

**Output:**

```
SELECT * FROM expenses ORDER BY date DESC

.desc() = descending (newest first)
.asc() = ascending (oldest first, default)
```

### Limiting Results

```python
with Session(engine) as session:
    # Get first 5 expenses only
    first_five = session.query(Expense).limit(5).all()
```

**Output:**

```
SELECT * FROM expenses LIMIT 5

Useful for pagination or "top N" queries
```

## .all() vs .first(): When to Use Each

| Method       | Returns             | Use When                   |
| ------------ | ------------------- | -------------------------- |
| `.all()`   | List (may be empty) | Expecting multiple results |
| `.first()` | One object or None  | Expecting one result       |

```python
with Session(engine) as session:
    # .all() - always a list
    categories = session.query(Category).all()
    print(type(categories))  # <class 'list'>
    print(len(categories))   # 3

    # .first() - one object or None
    food = session.query(Category).filter(
        Category.name == 'Food'
    ).first()
    print(type(food))        # <class 'Category'> or NoneType
```

**Output:**

```
<class 'list'>
3
<class '__main__.Category'>
```

**Safety tip**: When using `.first()`, always check for None:

```python
food = session.query(Category).filter(Category.name == 'Pizza').first()

if food:
    print(f"Found: {food.name}")
else:
    print("Category not found")
```

## Error Handling

What happens when you try to add invalid data?

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
        # Session auto-rollbacks - no partial data saved
```

**Output:**

```
Error: FOREIGN KEY constraint failed

The expense was NOT saved.
Session automatically rolled back all changes.
```

**Key insight**: The `with` block handles cleanup. If an error occurs:

1. Changes are rolled back (nothing saved)
2. Session closes properly
3. Your database stays consistent

## Complete Example: Budget Tracker CRUD

Here's a working example that creates and reads Budget Tracker data:

```python
from datetime import date
from sqlalchemy import create_engine
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
    for cat in session.query(Category).all():
        print(f"  {cat.id}: {cat.name}")

    # Expenses over $50
    print("\nExpenses over $50:")
    big = session.query(Expense).filter(Expense.amount > 50).all()
    for exp in big:
        print(f"  ${exp.amount}: {exp.description}")
```

**Output:**

```
Categories:
  1: Food
  2: Transport

Expenses over $50:
  $52.5: Groceries
```

## What Happens Next

In this lesson, you mastered Create and Read operations. But data is never static. Expenses change. Users update their categories. That's where L4 comes in.

| Lesson | What You Learn                   | What You Add to Your Skill            |
| ------ | -------------------------------- | ------------------------------------- |
| L3 (now) | Create and Read records        | CRUD Create/Read patterns             |
| L4     | Connect tables with relationships | Foreign keys and navigation patterns  |
| L5     | Make operations atomic and safe  | Transaction patterns and error handling |
| L6     | Deploy to the cloud              | Connection pooling and Neon setup     |
| L7     | Combine SQL + bash for hybrid patterns | Tool choice framework              |
| L8     | Build the complete Budget Tracker | Capstone integration                  |

Each lesson builds on the previous one. You can Create and Read. Next, you'll connect tables so you can answer questions like "Show me all expenses for User 1" without writing complex filter logic.

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

1. session.query(Expense).filter(Expense.category_id == 1).all()
   How many results? What are they?

2. session.query(Expense).filter(Expense.amount >= 50).first()
   What single record is returned?

3. session.query(Category).filter(Category.name == 'Shopping').first()
   What is returned and why?
```

After AI responds, trace through each query yourself. Do your predictions match?

### Prompt 2: Write CRUD Code

**What you're learning:** Writing Create and Read operations.

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

After AI responds, check: Does the code use `with Session(engine)`? Does it `commit()` after creating?

### Prompt 3: Update Your Skill

**What you're learning:** Documenting patterns as you learn.

```
Add to my /database-deployment skill:

## CRUD Operations: Create & Read

Include these patterns with examples:
1. Session context manager pattern (with Session as session)
2. Create single record (session.add + commit)
3. Create multiple records (session.add_all + commit)
4. Query all (.query().all())
5. Query with filter (.query().filter().first())
6. Error handling (try/except around commit)

Use Budget Tracker examples (Category, Expense).
Format as markdown for SKILL.md.
```

After AI responds, paste the section into your `/database-deployment/SKILL.md` file.

**Safety reminder:** When working with real databases, always verify your queries on a small dataset first. A query without a filter (like `.all()` on millions of rows) can crash your program or overload your database.

### Checkpoint

Before moving to L4:

- [ ] You understand: Session = conversation with database
- [ ] You can create records (session.add + session.commit)
- [ ] You can query all records (session.query().all())
- [ ] You can filter records (session.query().filter())
- [ ] You know the difference between .all() (list) and .first() (one or None)
- [ ] You understand: Errors auto-rollback, no partial saves
- [ ] You've written CRUD code (Prompt 2)
- [ ] You've updated your /database-deployment skill with CRUD patterns

Ready for L4: Update & Delete operations, plus relationships.
