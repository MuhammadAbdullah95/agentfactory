---
sidebar_position: 3
title: "Models as Code"
chapter: 9
lesson: 2
duration_minutes: 25
description: "Define SQLAlchemy models as Python classes that become database tables"
keywords: ["SQLAlchemy", "ORM", "models", "Column", "Integer", "String", "Float", "Date", "primary key", "ForeignKey"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Model Definition"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Remember"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can identify the parts of a SQLAlchemy model: Base, tablename, Column, types"

  - name: "Column Type Mapping"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can select correct Column type for given data (Integer for IDs, String for text, Float for money)"

  - name: "Table Structure Prediction"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can predict what database table will be created from a Python model class"

  - name: "Foreign Key Understanding"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can explain what ForeignKey does and why it prevents orphaned data"

learning_objectives:
  - objective: "Define SQLAlchemy models as Python classes"
    proficiency_level: "A1"
    bloom_level: "Remember"
    assessment_method: "Student writes a valid model class with tablename, id, and at least one other column"

  - objective: "Map Column types (Integer, String, Float, Date) to Python data types"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student correctly chooses Column types for a given requirement (email=String, price=Float)"

  - objective: "Understand how Python classes become database tables"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Student can describe what SQLAlchemy does when it reads a model class"

  - objective: "Predict table structure from model code"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Given a model class, student correctly lists table name, column names, and which are required"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (Base class, Column decorator, data types, primary key, ForeignKey) - appropriate for A1-A2"

differentiation:
  extension_for_advanced: "Add Relationship back_populates syntax; discuss cascade delete behavior"
  remedial_for_struggling: "Focus only on single Expense model; skip Category and ForeignKey until next lesson"
---
# Models as Code

In L1, you learned why databases beat CSV files: relationships, queries, transactions, persistence. Now the practical question: how do you CREATE a database table?

Answer: You write a Python class. SQLAlchemy reads your class and creates the actual table.

This is Principle 2 in action: Code as Universal Interface. You never write SQL by hand. Your Python class IS your table definition.

## The Simplest Model

Here's a complete, working model:

```python
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    amount = Column(Float)
```

**What happens when you run this code:**

- SQLAlchemy reads your `Expense` class
- It sees `__tablename__ = 'expenses'` and knows to create a table called `expenses`
- It sees three `Column()` definitions and creates three columns
- `id` is special: `primary_key=True` means it auto-increments (1, 2, 3...)
- `description` holds text (no length limit by default)
- `amount` holds decimal numbers

**Output: The table SQLAlchemy creates**

```
Table: expenses
├── id: Integer, primary key, auto-increments
├── description: String, can be null
└── amount: Float, can be null
```

You wrote Python. SQLAlchemy generated the database structure. That's the ORM (Object-Relational Mapper) pattern.

## Understanding Column Types

Every Column needs a type. Here's what each type stores:

| Python Type  | Column Type    | What It Stores          | Example                           |
| ------------ | -------------- | ----------------------- | --------------------------------- |
| `int`      | `Integer`    | Whole numbers           | `id = Column(Integer)`          |
| `str`      | `String(50)` | Text up to N characters | `name = Column(String(50))`     |
| `float`    | `Float`      | Decimal numbers         | `price = Column(Float)`         |
| `bool`     | `Boolean`    | True or False           | `is_active = Column(Boolean)`   |
| `datetime` | `DateTime`   | Date and time           | `created_at = Column(DateTime)` |
| `date`     | `Date`       | Date only (no time)     | `expense_date = Column(Date)`   |

### Column Constraints

Beyond type, columns can have constraints:

```python
Column(String(100), nullable=False)   # Required field (can't be empty)
Column(String(100), unique=True)      # No duplicates allowed
Column(Float, default=0.0)            # Default value if not specified
Column(Integer, primary_key=True)     # Unique identifier for each row
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

**What this creates:**

```
Table: users
├── id: Integer, primary key, auto-increments
├── email: String(100), unique, required
├── name: String(100), required
└── created_at: DateTime, defaults to current time
```

**Why these constraints matter:**

- `unique=True` on email: No two users can have the same email
- `nullable=False`: Every user MUST have an email and name
- `default=datetime.utcnow`: Timestamp auto-generated when row created

### Model 2: Category

```python
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    color = Column(String(7), default='#FF6B6B')
```

**Output: Table structure**

```
Table: categories
├── id: Integer, primary key, auto-increments
├── name: String(50), unique, required
└── color: String(7), defaults to '#FF6B6B'
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
    amount = Column(Float, nullable=False)
    date = Column(Date, default=date.today)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
```

**Output: Table structure**

```
Table: expenses
├── id: Integer, primary key, auto-increments
├── user_id: Integer, required (points to users.id)
├── category_id: Integer, required (points to categories.id)
├── description: String(200), required
├── amount: Float, required
├── date: Date, defaults to today
└── created_at: DateTime, defaults to current time
```

Notice `user_id` and `category_id`. These are the foreign keys we discussed in L1.

## Foreign Keys: Connecting Tables

`ForeignKey('users.id')` is the magic that connects tables.

**What it means:**

```python
user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
```

This says: "The `user_id` column must contain a value that EXISTS in the `users` table's `id` column."

**Why this matters:**

```
Without ForeignKey:
- You could add expense with user_id=999
- No user 999 exists
- Orphaned data: expense belongs to nobody

With ForeignKey:
- Try to add expense with user_id=999
- Database checks: Does user 999 exist?
- Error: "Foreign key constraint violation"
- Data integrity preserved
```

**The database enforces your business rule**: Every expense must belong to a real user.

## Putting It All Together

Here's the complete Budget Tracker models file:

```python
from datetime import datetime, date, timezone
from sqlalchemy import Column, Integer, String, Float, DateTime, Date, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    color = Column(String(7), default='#FF6B6B')

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, default=date.today)
    created_at = Column(DateTime, default=datetime.utcnow)
```

**Output: Three connected tables**

```
Budget Tracker Database:
├── users (id, email, name, created_at)
├── categories (id, name, color)
└── expenses (id, user_id→users, category_id→categories, description, amount, date, created_at)

Relationships:
- expenses.user_id points to users.id
- expenses.category_id points to categories.id
```

This is the entire data layer for Budget Tracker. Python classes. No SQL. SQLAlchemy handles the translation.

## Why Models Win: The Schema Clarity Insight

In L1, you saw the Braintrust experiment: bash achieved only 52.7% accuracy on structured queries despite generating sophisticated commands. The root cause was that bash had to *guess* at field names, data types, and relationships.

Look at what your models provide that bash never had:

- `amount = Column(Float, nullable=False)` — every tool knows this is a required decimal number
- `user_id = Column(Integer, ForeignKey('users.id'))` — every tool knows this links to the users table
- `date = Column(Date, default=date.today)` — every tool knows this is a calendar date, not a string

Your SQLAlchemy models don't just define storage. They **describe the data** to everything that touches it — the database engine, your Python code, and any AI agent that reads your schema. This is Principle 2 (Code as Universal Interface) at its deepest level.

Schema clarity is why SQL wins. Your models provide it.

## What Happens Next

You've defined the structure. Three interconnected tables with primary keys, foreign keys, and relationships. But a database with no data is just an empty box. In L3, you'll actually populate these tables, run queries, and see real data flowing through your Budget Tracker.

| Lesson | What You Learn                    | What You Add to Your Skill            |
| ------ | --------------------------------- | ------------------------------------- |
| L2 (now) | Define models as Python classes | Model definition patterns             |
| L3     | Create records, read them back   | CRUD operations                       |
| L4     | Navigate between tables          | Relationship and join patterns        |
| L5     | Guarantee multi-step safety      | Transaction patterns                  |
| L6     | Deploy to the cloud              | Neon and production configuration     |
| L7     | Combine SQL + bash patterns      | Hybrid tool choice framework          |
| L8     | Bring it all together            | Complete working application          |

Models define structure. CRUD operations populate and read that structure. Everything that follows depends on getting these models right.

## Try With AI

### Prompt 1: Read the Code

**What you're learning:** Translating Python model definitions to table structures.

```
Given this model:

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    in_stock = Column(Boolean, default=True)

Predict:
- What table gets created?
- What columns does it have?
- Which columns are required vs optional?
- What is the default value for in_stock?
- If I try to add a product without a name, what happens?
```

Check the response. Can you trace from Python to table structure?

### Prompt 2: Write Models from Requirements

**What you're learning:** Designing models from business requirements.

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

After AI responds, verify: Does the model have all the constraints? Are the types correct?

### Prompt 3: Update Your Skill

**What you're learning:** Building documentation as you learn.

```
Add to my /database-deployment skill:

## Model Definition Pattern

Create a section that includes:
1. Template for Base and declarative_base setup
2. Column types table (Integer, String, Float, Boolean, DateTime, Date)
3. Key constraints and when to use each (primary_key, unique, nullable, default)
4. When to use ForeignKey

Use the Budget Tracker User, Category, Expense models as examples.
Format as markdown I can paste into my SKILL.md file.
```

After AI responds, update your `/database-deployment/SKILL.md` with the model definition patterns.

### Checkpoint

Before moving to L3:

- [ ] You understand: Python class becomes database table
- [ ] You can name the 3 Budget Tracker models (User, Category, Expense)
- [ ] You know which Column type to use for: text, numbers, dates, true/false
- [ ] You understand what ForeignKey does (enforces that referenced row exists)
- [ ] You've updated your `/database-deployment` skill with model patterns

Ready for L3: CRUD operations (Create, Read, Update, Delete).
