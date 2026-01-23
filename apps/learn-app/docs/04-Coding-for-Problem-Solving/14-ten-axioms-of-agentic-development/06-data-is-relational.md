---
sidebar_position: 6
title: "Axiom VI: Data is Relational"
description: "Why structured data follows relational patterns, SQL as the universal data language, and how to choose between SQLite and PostgreSQL for agentic development"
keywords: ["SQL", "relational database", "SQLite", "PostgreSQL", "ORM", "SQLModel", "data modeling", "schema", "migrations", "agentic development"]
chapter: 14
lesson: 6
duration_minutes: 22

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding Relational Data Modeling"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain why structured data naturally follows relational patterns and identify entities, attributes, and relationships in a domain"

  - name: "Choosing SQL Databases for Agent Work"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can apply the SQLite vs PostgreSQL decision framework to determine the appropriate database for a given project scope"

  - name: "Writing SQL as Agent-Readable Specifications"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Understand"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can explain why SQL schemas serve as type definitions for data and why AI agents work effectively with SQL as a constrained, declarative language"

learning_objectives:
  - objective: "Explain why SQL has endured for 50+ years and why it remains the default for structured persistent data"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can articulate at least three properties of SQL (declarative, optimized, relational) that make it durable and superior to ad-hoc alternatives for structured data"

  - objective: "Apply the SQLite vs PostgreSQL decision framework to real project scenarios"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Given a project description (single-user CLI tool, multi-user web app, embedded device), student can recommend the correct database with reasoning"

  - objective: "Identify anti-patterns in data persistence and explain their consequences"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student can recognize at least three anti-patterns (JSON-as-database, no migrations, no parameterization) and explain what goes wrong in each case"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (relational model, SQL declarative language, SQLite vs PostgreSQL tradeoffs, ORM layering, migrations, SQL injection) within A2-B1 range (5-7 concepts)"

differentiation:
  extension_for_advanced: "Explore database normalization forms (1NF through 3NF), write a migration script using Alembic, compare query plans between indexed and non-indexed queries"
  remedial_for_struggling: "Focus on the single concrete example: one Task table in SQLite, insert a row, query it back. Understand that SQL is just a language for talking to structured data"
---

# Axiom VI: Data is Relational

Your agent project is going well. You started with a JSON file to store tasks -- simple, readable, gets the job done. Twenty tasks later, it still works fine. Two hundred tasks later, you notice the file takes a moment to load. Two thousand tasks later, you need to find all tasks assigned to a specific person that are overdue -- and you realize you are loading the entire file into memory, looping through every record, checking conditions manually. Your "database" is a flat list pretending to be a data system.

Then you add a second entity -- projects that contain tasks. Now you need to express relationships: which tasks belong to which project? You duplicate project names inside each task record. When a project name changes, you hunt through every task to update it. You forget one. Your data is now inconsistent, and your JSON file cannot tell you that anything is wrong.

This is the moment every developer encounters. The data outgrew the format. The relationships were always there -- you just did not have a system that understood them. This axiom provides the system.

## The Problem Without This Axiom

Without recognizing that structured data is inherently relational, developers fall into predictable traps:

**The JSON Graveyard**: Projects accumulate JSON files -- `tasks.json`, `users.json`, `projects.json` -- with no way to express relationships between them. Cross-referencing requires loading everything into memory and writing custom lookup code for every query. There are no constraints, no validation, no guarantees that referenced entities exist.

**The Flat File Spiral**: Data starts in CSV or plain text. As complexity grows, developers invent ad-hoc query languages, build custom indexing, implement their own transaction logic. They are slowly, painfully reinventing a database -- badly.

**The NoSQL Trap**: Developers reach for document stores (MongoDB, Firebase) as their first database because the API feels familiar -- just store objects. But when the data IS relational (users have projects, projects have tasks, tasks have assignees), fighting the relational nature of the data creates complexity that a relational database handles natively.

Each of these paths leads to the same destination: a system that cannot answer basic questions about its own data without heroic effort from the developer.

## The Axiom Defined

> **Axiom VI: Structured data follows relational patterns. SQL is the default for persistent structured data. SQLite for single-user, PostgreSQL for multi-user. Use an ORM only when it doesn't obscure the SQL.**

This axiom makes three claims:

1. **Structured data is relational by nature.** When you have entities with attributes and connections between them, you have relational data -- whether or not you store it relationally.
2. **SQL is the default choice.** Not the only choice, but the one you should deviate from consciously with good reason.
3. **The ORM serves you, not the reverse.** If your ORM hides the SQL so completely that you cannot reason about what queries execute, it has become an obstacle.

## From Principle to Axiom

In Part 1, Chapter 4, you learned **Principle 5: Persisting State in Files** -- the general durability rule that work products must survive beyond a single session. Files provide durable, inspectable, version-controllable state.

Axiom VI refines this principle for a specific category of state: **structured data with relationships**. The distinction matters:

| State Type | Storage | Why |
|-----------|---------|-----|
| Knowledge, documentation, specs | Markdown files | Human-readable, version-controlled, AI-parseable |
| Configuration | YAML/TOML files | Declarative, mergeable, environment-specific |
| Structured entities with relationships | SQL database | Queryable, constrained, normalized, concurrent-safe |
| Binary assets | File system | Git LFS or object storage for large files |

Principle 5 tells you to persist state. Axiom VI tells you HOW to persist structured data: relationally, with SQL, using the right engine for the job.

## Why SQL Endures

SQL was first described by Edgar Codd at IBM in 1970 and formalized into a language by the mid-1970s. Over fifty years later, it remains the dominant language for structured data. This longevity is not nostalgia -- it reflects fundamental properties that alternatives have not surpassed.

### The Lindy Effect

The Lindy Effect suggests that the longer a non-perishable technology has survived, the longer its expected remaining lifespan. SQL has survived:

- The rise and fall of object databases (1990s)
- The XML database movement (early 2000s)
- The NoSQL revolution (2010s)
- The NewSQL emergence (2015s)
- The graph database wave (2020s)

Each of these alternatives found legitimate niches. None displaced SQL for general-purpose structured data. The reason is architectural: SQL makes the right tradeoffs for most data.

### Why SQL Works

| Property | What It Means | Why It Matters |
|----------|---------------|----------------|
| **Declarative** | You say WHAT you want, not HOW to get it | The database optimizer chooses the execution strategy |
| **Relational** | Data is organized into related tables | Reflects how real-world entities connect |
| **Constrained** | Schema enforces structure, types, and relationships | Invalid data is rejected before it enters the system |
| **Optimized** | Decades of query planner research | Complex queries execute efficiently without manual tuning |
| **Transactional** | ACID guarantees (Atomicity, Consistency, Isolation, Durability) | Data is never left in a half-updated state |
| **Universal** | One language across SQLite, PostgreSQL, MySQL, SQL Server | Skills transfer between databases |

The declarative nature deserves emphasis. When you write:

```sql
SELECT tasks.title, projects.name
FROM tasks
JOIN projects ON tasks.project_id = projects.id
WHERE tasks.status = 'overdue'
ORDER BY tasks.due_date;
```

You have not specified HOW to find this data. You have not said "scan the tasks array, for each task look up the project, filter by status, then sort." You described the RESULT you want, and the database figures out the fastest path to deliver it. This is the same declarative philosophy behind CSS, HTML, and configuration files -- and it is why AI agents work so effectively with SQL.

## Relational Thinking: Entities and Relationships

Before writing SQL, you need to think relationally. This means identifying three things:

### 1. Entities (Tables)

An entity is a distinct "thing" in your domain. In a task management system:

- **Task** -- a unit of work to be completed
- **Project** -- a collection of related tasks
- **User** -- a person who creates or is assigned tasks

Each entity becomes a table.

### 2. Attributes (Columns)

Each entity has properties:

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    due_date TEXT,
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    project_id INTEGER REFERENCES projects(id),
    assignee_id INTEGER REFERENCES users(id)
);
```

Notice the constraints built into the schema: `NOT NULL` means the field is required, `DEFAULT` provides sensible initial values, `REFERENCES` declares relationships. The schema IS documentation -- it tells you and your AI agent exactly what this data looks like.

### 3. Relationships (Foreign Keys)

Relationships connect entities:

- A Task **belongs to** a Project (many-to-one)
- A Task **is assigned to** a User (many-to-one)
- A Project **has many** Tasks (one-to-many)
- A User **has many** assigned Tasks (one-to-many)

These relationships are expressed through foreign keys -- columns that reference another table's primary key. The database enforces referential integrity: you cannot assign a task to a project that does not exist.

```sql
-- This will FAIL if project_id 999 doesn't exist in projects table
INSERT INTO tasks (title, status, project_id)
VALUES ('Write tests', 'pending', 999);
-- Error: FOREIGN KEY constraint failed
```

Compare this to JSON, where nothing prevents you from writing `"project_id": 999` even if no such project exists. The relational database catches the error. The JSON file silently accepts it.

## The SQLite / PostgreSQL Decision

The axiom specifies two databases. Here is when to use each:

| Factor | SQLite | PostgreSQL |
|--------|--------|------------|
| **Writers** | Single process | Many concurrent users |
| **Deployment** | Embedded in your application | Separate server process |
| **Setup** | Zero configuration (just a file) | Requires installation and configuration |
| **Size** | Up to ~1 TB practical | Petabytes with proper architecture |
| **Concurrency** | Single-writer, multiple readers | Full MVCC concurrent access |
| **Use case** | CLI tools, mobile apps, prototypes, embedded | Web apps, APIs, multi-user systems |
| **Backup** | Copy the file | pg_dump or streaming replication |
| **AI agent work** | Local projects, personal tools | Production deployments |

### The Decision Framework

Ask these three questions:

1. **How many processes write to this database simultaneously?**
   - One process: SQLite
   - Multiple processes: PostgreSQL

2. **Does this need to run as a network service?**
   - No (CLI tool, desktop app, local agent): SQLite
   - Yes (web API, shared service): PostgreSQL

3. **Is this a prototype or production?**
   - Prototype: SQLite (migrate to PostgreSQL later if needed)
   - Production multi-user: PostgreSQL from the start

### SQLite in Practice

SQLite is not a toy database. It is the most widely deployed database engine in the world -- present in every smartphone, every web browser, and most operating systems. For single-user applications, it is often the BETTER choice: no server to maintain, no connection strings to manage, no separate backup system to configure.

```python
import sqlite3

# Create or connect to database (just a file)
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create schema
cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        created_at TEXT NOT NULL DEFAULT (datetime('now'))
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'pending',
        due_date TEXT,
        project_id INTEGER REFERENCES projects(id),
        created_at TEXT NOT NULL DEFAULT (datetime('now'))
    )
""")

# Insert data with parameterized queries (SAFE)
cursor.execute(
    "INSERT INTO projects (name) VALUES (?)",
    ("Agent Factory",)
)
project_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO tasks (title, status, project_id) VALUES (?, ?, ?)",
    ("Design database schema", "in_progress", project_id)
)

conn.commit()

# Query with JOIN -- the relational power
cursor.execute("""
    SELECT tasks.title, tasks.status, projects.name
    FROM tasks
    JOIN projects ON tasks.project_id = projects.id
    WHERE tasks.status != 'completed'
    ORDER BY tasks.created_at DESC
""")

for row in cursor.fetchall():
    print(f"[{row[1]}] {row[0]} (Project: {row[2]})")

conn.close()
```

This is 40 lines of Python. No external services, no configuration files, no Docker containers. The database is a single file (`tasks.db`) that you can copy, back up, or inspect with any SQLite tool. Yet it gives you relational integrity, declarative queries, and efficient indexed access.

### PostgreSQL in Practice

When your application serves multiple users concurrently, PostgreSQL provides the concurrency model that SQLite cannot:

```python
import psycopg2

# Connect to PostgreSQL server
conn = psycopg2.connect(
    host="localhost",
    dbname="taskmanager",
    user="app_user",
    password="secure_password"
)

cursor = conn.cursor()

# Same SQL -- the language transfers directly
cursor.execute("""
    SELECT tasks.title, tasks.status, projects.name
    FROM tasks
    JOIN projects ON tasks.project_id = projects.id
    WHERE tasks.status != 'completed'
    ORDER BY tasks.created_at DESC
""")

for row in cursor.fetchall():
    print(f"[{row[1]}] {row[0]} (Project: {row[2]})")

conn.close()
```

Notice that the SQL is identical. The query you wrote for SQLite works in PostgreSQL. The connection setup differs -- PostgreSQL requires a host, credentials, and a running server -- but the data language is the same. This is the universality of SQL: learn it once, apply it everywhere.

## SQL and AI: A Perfect Match

Here is why this axiom matters especially in the age of AI agents: SQL is one of the languages AI understands best.

### Why AI Excels at SQL

**Constrained vocabulary**: SQL has approximately 30 keywords that matter (`SELECT`, `FROM`, `WHERE`, `JOIN`, `INSERT`, `UPDATE`, `DELETE`, `CREATE`, `ALTER`, `DROP`, etc.). Compare this to a general-purpose language with thousands of library functions. A constrained language means less ambiguity and fewer hallucination opportunities.

**Declarative semantics**: SQL describes WHAT, not HOW. This maps directly to natural language intent. "Show me all overdue tasks assigned to Maria" translates almost word-for-word to:

```sql
SELECT * FROM tasks
WHERE status = 'overdue'
AND assignee_id = (SELECT id FROM users WHERE name = 'Maria');
```

**Schema as context**: When you give an AI agent your schema, it knows exactly what data exists, what types each column holds, and how tables relate. The schema IS the type system for your data:

```sql
-- This schema tells the AI everything it needs to write correct queries
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    owner_id INTEGER NOT NULL REFERENCES users(id)
);

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('pending', 'in_progress', 'completed')),
    project_id INTEGER NOT NULL REFERENCES projects(id),
    assignee_id INTEGER REFERENCES users(id)
);
```

An AI agent reading this schema can immediately write valid queries, generate correct INSERT statements, and understand the domain model -- without any additional documentation.

### SQL is Verifiable

Unlike generated Python or JavaScript, SQL queries can be verified mechanically:

1. **Syntax check**: Does the query parse?
2. **Schema check**: Do the referenced tables and columns exist?
3. **Type check**: Are comparisons between compatible types?
4. **Result check**: Does `EXPLAIN` show a reasonable query plan?

This makes SQL ideal for AI-generated code: you can validate correctness without running the query against production data.

## ORMs: When to Use, When to Avoid

An ORM (Object-Relational Mapper) bridges the gap between your programming language's objects and your database's tables. In Python, SQLModel (built on SQLAlchemy) is the recommended choice for agentic development:

```python
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional
from datetime import datetime

class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    status: str = Field(default="pending")
    due_date: Optional[datetime] = None
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)

# Create database and tables
engine = create_engine("sqlite:///tasks.db")
SQLModel.metadata.create_all(engine)

# Use the ORM
with Session(engine) as session:
    project = Project(name="Agent Factory")
    session.add(project)
    session.commit()
    session.refresh(project)

    task = Task(
        title="Design database schema",
        status="in_progress",
        project_id=project.id
    )
    session.add(task)
    session.commit()

    # Query -- still readable, maps to SQL concepts
    statement = select(Task).where(Task.status != "completed")
    results = session.exec(statement)
    for task in results:
        print(f"[{task.status}] {task.title}")
```

### The ORM Rule

The axiom says: **"Use an ORM only when it doesn't obscure the SQL."**

This means:

| Use the ORM When | Avoid the ORM When |
|-------------------|---------------------|
| CRUD operations (Create, Read, Update, Delete) | Complex analytical queries with multiple JOINs |
| Type safety matters (Python type hints on models) | Performance-critical paths where you need query plan control |
| Schema definition (models as documentation) | You cannot explain what SQL the ORM generates |
| Migrations (Alembic integrates with SQLAlchemy) | The ORM syntax is more complex than raw SQL |

The test is simple: **Can you explain the SQL that your ORM code generates?** If yes, the ORM is adding value (type safety, schema management, migration support). If no, write the SQL directly.

```python
# Good: ORM for simple CRUD (the SQL is obvious)
task = session.get(Task, task_id)
task.status = "completed"
session.commit()

# Better as raw SQL: Complex reporting query
cursor.execute("""
    SELECT
        projects.name,
        COUNT(tasks.id) AS total_tasks,
        COUNT(CASE WHEN tasks.status = 'completed' THEN 1 END) AS done,
        ROUND(100.0 * COUNT(CASE WHEN tasks.status = 'completed' THEN 1 END)
              / COUNT(tasks.id), 1) AS percent_complete
    FROM projects
    LEFT JOIN tasks ON tasks.project_id = projects.id
    GROUP BY projects.id
    ORDER BY percent_complete DESC
""")
```

## Migrations: Schema Evolution Over Time

Databases evolve. You add columns, rename tables, create indexes. **Migrations** are versioned scripts that transform your schema from one state to the next -- like version control for your database structure.

Without migrations, schema changes are manual commands run against production databases with no record, no rollback, and no reproducibility. With migrations, every schema change is:

- **Versioned**: Each migration has a sequence number
- **Reversible**: Each migration defines both "upgrade" and "downgrade"
- **Reproducible**: Run all migrations to recreate the database from scratch
- **Auditable**: Git tracks who changed the schema and when

In the Python ecosystem, **Alembic** (built on SQLAlchemy) handles migrations:

```python
# alembic/versions/001_add_priority_to_tasks.py
"""Add priority column to tasks table"""

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('tasks', sa.Column('priority', sa.Integer(), nullable=True))
    op.create_index('ix_tasks_priority', 'tasks', ['priority'])

def downgrade():
    op.drop_index('ix_tasks_priority', 'tasks')
    op.drop_column('tasks', 'priority')
```

This migration adds a `priority` column and an index. If something goes wrong, `downgrade()` reverses it cleanly. The migration file lives in version control alongside your code -- schema and application evolve together.

## Anti-Patterns

| Anti-Pattern | What Goes Wrong | The Fix |
|-------------|-----------------|---------|
| **JSON files as database** | No queries, no relations, no constraints, loads everything into memory | Use SQLite -- same simplicity, relational power |
| **NoSQL as default** | Fighting relational data with document model, denormalization headaches | Start relational. Move to NoSQL only for genuinely non-relational data (logs, events, documents) |
| **Raw string SQL** | SQL injection vulnerabilities, crashes on special characters | Always use parameterized queries (`?` placeholders) |
| **No migrations** | Manual schema changes, inconsistent environments, no rollback | Use Alembic or equivalent migration tool |
| **Ignoring indexes** | Queries slow to a crawl as data grows (full table scans) | Index columns used in WHERE, JOIN, and ORDER BY |
| **Over-normalization** | Dozens of tables for simple domains, JOIN-heavy queries for basic reads | Normalize to 3NF, denormalize consciously with measured justification |

### The SQL Injection Example

This is the single most dangerous anti-pattern. Never construct SQL by string concatenation:

```python
# DANGEROUS -- SQL injection vulnerability
user_input = "'; DROP TABLE tasks; --"
cursor.execute(f"SELECT * FROM tasks WHERE title = '{user_input}'")
# Executes: SELECT * FROM tasks WHERE title = ''; DROP TABLE tasks; --'
# Your tasks table is now gone.

# SAFE -- parameterized query
cursor.execute("SELECT * FROM tasks WHERE title = ?", (user_input,))
# The database treats user_input as DATA, never as SQL commands.
# No injection possible.
```

Parameterized queries are not optional. They are a non-negotiable safety requirement. Every database library supports them. There is no excuse for string-concatenated SQL in any codebase.

## Safety Note

SQL injection remains one of the most common and damaging security vulnerabilities in production software. The OWASP Top 10 has listed injection attacks as a critical risk for over two decades.

**The rule is absolute**: Never interpolate user-provided values into SQL strings. Always use parameterized queries (also called prepared statements). This applies regardless of whether you use raw SQL or an ORM -- if you ever write raw queries, use parameter placeholders (`?` for SQLite, `%s` for PostgreSQL with psycopg2, or `:name` for named parameters).

Your AI agent should be instructed to follow this rule as well. When asking an AI to generate database code, include in your prompt: "All queries must use parameterized statements. No string interpolation for user input."

## Try With AI

Use these prompts to build practical understanding of relational data modeling and SQL for agent development.

### Prompt 1: Schema Design (Relational Thinking)

```
I'm building a task management system with these requirements:
- Users can create projects
- Projects contain tasks
- Tasks have a title, status (pending/in_progress/completed), priority (1-5), and due date
- Tasks can be assigned to users
- Users can belong to multiple projects (many-to-many)

Design the SQLite schema for me. For each table, explain:
1. Why each column exists
2. What constraints protect data integrity
3. How foreign keys express relationships

Then show me 3 example queries that demonstrate the relational power:
- All overdue tasks for a specific user across all their projects
- Project completion percentages
- Users with no tasks assigned

Use CREATE TABLE statements with full constraints.
```

**What you're learning**: Relational thinking -- how to decompose a domain into entities, identify relationships, and express constraints that prevent invalid data. The many-to-many relationship (users-to-projects) requires a junction table, which is a fundamental pattern you will use repeatedly.

### Prompt 2: JSON-to-SQL Migration (Recognizing the Problem)

```
I have this JSON file that stores my project data:

{
  "tasks": [
    {"id": 1, "title": "Design API", "project": "Backend", "assignee": "Alice", "status": "done"},
    {"id": 2, "title": "Write tests", "project": "Backend", "assignee": "Bob", "status": "pending"},
    {"id": 3, "title": "Deploy", "project": "Backend", "assignee": "Alice", "status": "pending"},
    {"id": 4, "title": "UI mockup", "project": "Frontend", "assignee": "Carol", "status": "in_progress"}
  ]
}

Show me:
1. Three questions I CANNOT efficiently answer with this JSON structure
2. The normalized SQL schema that fixes these problems
3. The migration script (Python + sqlite3) that reads the JSON and populates the database
4. The SQL queries that answer those three questions easily

Explain what I gain by moving to SQL and what (if anything) I lose.
```

**What you're learning**: The concrete costs of non-relational storage and the practical process of migrating to SQL. You are also learning to recognize when your data has outgrown its format -- a judgment you will apply repeatedly as projects evolve.

### Prompt 3: AI-Readable Schema (SQL as Specification)

```
I want to build an AI agent that can answer natural language questions about my task database.
The agent will receive my SQL schema as context and translate questions into queries.

Here's my schema:
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT UNIQUE);
CREATE TABLE projects (id INTEGER PRIMARY KEY, name TEXT NOT NULL, owner_id INTEGER REFERENCES users(id));
CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL, status TEXT CHECK(status IN ('pending','active','done')), project_id INTEGER REFERENCES projects(id), assignee_id INTEGER REFERENCES users(id));

Act as that agent. I'll ask natural language questions and you translate to SQL:
1. "Who has the most unfinished tasks?"
2. "Which projects have no active tasks?"
3. "What percentage of Alice's tasks are done?"

For each, show the SQL and explain how the schema constraints helped you write correct queries.
Then tell me: what would happen if I gave you a JSON blob instead of a schema? How would
your confidence in generating correct queries change?
```

**What you're learning**: Why SQL schemas serve as precise specifications for AI agents. The constrained vocabulary, explicit types, and declared relationships give AI enough context to generate correct queries with high confidence. This is the practical application of Axiom VI to agentic development -- your schema becomes the interface contract between your application and your AI collaborator.

## Connecting Forward

This axiom establishes how structured data lives in your systems. The next axiom -- **Tests Are the Specification** -- addresses how you verify that your code (including your database interactions) behaves correctly. Together, they form a powerful pair: your schema defines what valid data looks like, and your tests prove that your application respects those definitions.

In Parts 5 and 6, when you build agent APIs with FastAPI and SQLModel, you will apply Axiom VI directly: defining schemas that serve as both database structure and API documentation, writing migrations that evolve your data model safely, and letting AI agents interact with your data through the universal language of SQL.
