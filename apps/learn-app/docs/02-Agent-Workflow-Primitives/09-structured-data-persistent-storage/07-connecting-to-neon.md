---
sidebar_position: 7
title: "Connecting to Neon"
chapter: 9
lesson: 6
duration_minutes: 25
description: "Deploy your Budget Tracker to Neon PostgreSQL with secure connection strings, environment variables, and production-ready connection pooling"
keywords: ["Neon", "PostgreSQL", "serverless", "cloud database", "connection string", "environment variables", "connection pooling", "psycopg2", "dotenv", "production"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Serverless Database Understanding"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can explain what serverless databases are and why they scale automatically"

  - name: "Connection String Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can parse and configure database connection strings with correct driver syntax"

  - name: "Environment Variable Security"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can store secrets in .env files and prevent accidental git commits"

  - name: "Connection Pooling Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can configure SQLAlchemy engine with pooling parameters for cloud databases"

  - name: "Cloud Database Troubleshooting"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can diagnose common connection errors and apply fixes"

learning_objectives:
  - objective: "Create a Neon PostgreSQL serverless database account and project"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student successfully creates Neon account and retrieves connection string"

  - objective: "Configure environment variables to store database credentials securely"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates .env file with DATABASE_URL and adds .env to .gitignore"

  - objective: "Connect SQLAlchemy to Neon using the psycopg2 driver with SSL"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student's code successfully executes SELECT 1 against Neon database"

  - objective: "Configure connection pooling for production reliability"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student's engine includes pool_size, max_overflow, pool_pre_ping, and pool_recycle"

  - objective: "Troubleshoot common Neon connection errors"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Given an error message, student identifies cause and applies correct fix"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (serverless databases, connection strings, environment variables, connection pooling, SSL requirement) - appropriate for A2 students with L5 transaction knowledge"

differentiation:
  extension_for_advanced: "Explore database branching for dev/prod separation, read replicas for scaling, connection pooling math (Neon limits, pool_size optimization)"
  remedial_for_struggling: "Focus on: Create account -> Get connection string -> Connect in code. Skip pooling details initially."
---
# Connecting to Neon

> **Chapter 8 callback:** Local scripts gave you deterministic outputs; they did not give you shared, always-on persistence.

In L5, you built transactions that keep your Budget Tracker data consistent. Transfers succeed completely or fail completely. Your database is safe from corruption.

But consistency without persistence is still a dead end. SQLite in-memory mode erases everything on restart.

The solution: Move from local SQLite to a cloud database. Neon gives you a PostgreSQL database that runs 24/7, auto-scales with traffic, and costs nothing for learning.

## What is Neon?

Neon is a **serverless PostgreSQL database**. Serverless means you don't manage servers. Neon handles scaling, backups, and availability automatically.

| Feature               | SQLite (what you have now) | Neon (what you're getting)    |
| --------------------- | -------------------------- | ----------------------------- |
| **Location**    | Local file or memory       | Cloud (always available)      |
| **Users**       | Single process only        | Multiple users simultaneously |
| **Persistence** | Dies on restart            | Always running                |
| **Backups**     | None (manual only)         | Automatic                     |
| **Scaling**     | Fixed                      | Auto-scales with traffic      |
| **Cost**        | $0                         | $0 (free tier)                |

Neon also offers features you don't need yet but will appreciate later:

- **Auto-pause**: Scales to zero when idle (no cost when not in use)
- **Database branching**: Create copies of your database like Git branches
- **Read replicas**: Scale read-heavy workloads

For learning: Neon's free tier includes up to 100 projects, 0.5 GB storage per project, and shared compute. More than enough for learning.

## Step 1: Create Your Neon Account

1. Go to [neon.tech](https://neon.tech)
2. Sign up (GitHub login is fastest)
3. Create a new project:
   - Name: `budget-tracker` (or anything you remember)
   - Region: Choose closest to you (lower latency)
   - Database: Keep default `neondb`
4. Wait about 30 seconds for provisioning

Your project is ready when you see the dashboard.

## Step 2: Get Your Connection String

In the Neon dashboard:

1. Click your project
2. Go to the **Connection Details** section
3. Find the connection string selector
4. Select: **Python** and **psycopg2**
5. Copy the connection string

It looks like this:

```
postgresql+psycopg2://alice:secretpass123@ep-cool-breeze-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
```

Let's break down what each part means:

```
postgresql+psycopg2://alice:secretpass123@ep-cool-breeze-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
│                    │     │             │                                              │      │
│                    │     │             │                                              │      └─ SSL required (Neon enforces encryption)
│                    │     │             │                                              └─ Database name
│                    │     │             └─ Host (your Neon endpoint)
│                    │     └─ Password (keep this secret!)
│                    └─ Username
└─ Driver (psycopg2 = PostgreSQL driver for Python)
```

**Important**: This string contains your password. Treat it like a password.

## Step 3: Store Credentials Securely

Never put passwords directly in code. Use environment variables.

**Install python-dotenv** (if not already installed):

```bash
uv add python-dotenv psycopg2-binary
```

Or with pip:

```bash
pip install python-dotenv psycopg2-binary
```

**Create `.env` file** in your project root:

```env
DATABASE_URL=postgresql+psycopg2://alice:secretpass123@ep-cool-breeze-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
```

**Load in Python**:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Read .env file

database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise ValueError("DATABASE_URL not set in .env file")

print("Database URL loaded successfully")
```

**Output:**

```
Database URL loaded successfully
```

**Add `.env` to `.gitignore`** (critical for security):

```bash
echo ".env" >> .gitignore
```

Verify it's ignored:

```bash
git status
# .env should NOT appear in "Untracked files"
```

**Why this matters**: If you commit `.env` to GitHub, anyone can access your database. Bots scan public repos for exposed credentials. Don't be that person.

## Step 4: Configure Connection Pooling

Neon limits concurrent connections. Without pooling, every query opens a new connection (slow, hits limits fast). With pooling, you reuse connections (fast, respects limits).

Here's the production-ready engine configuration:

```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set in .env file")

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,           # Keep 5 connections ready
    max_overflow=10,       # Allow 10 more during traffic spikes
    pool_pre_ping=True,    # Test connection before using it
    pool_recycle=3600,     # Recreate connections after 1 hour
)
```

What each parameter does:

| Parameter         | Value | Purpose                                                  |
| ----------------- | ----- | -------------------------------------------------------- |
| `pool_size`     | 5     | Warm connections always ready (no wait time)             |
| `max_overflow`  | 10    | Extra connections during high traffic (temporary)        |
| `pool_pre_ping` | True  | Verify connection works before using it                  |
| `pool_recycle`  | 3600  | Refresh stale connections (Neon pauses idle connections) |

Total maximum connections: `pool_size + max_overflow = 15`

**Why `pool_pre_ping=True` is critical**: Neon auto-pauses idle databases after 5 minutes. When you reconnect, stale connections fail. `pool_pre_ping` tests each connection before use and automatically replaces dead ones.

## Step 5: Test Your Connection

Before deploying your models, verify the connection works:

```python
from sqlalchemy import text

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
```

**Output (success):**

```
Connection successful!
```

**Output (common failures):**

```
Connection failed: could not connect to server: Connection timed out
Connection failed: FATAL: password authentication failed for user "alice"
Connection failed: No module named 'psycopg2'
```

If you see errors, jump to the Troubleshooting section below.

## Step 6: Deploy Your Models

Once connected, create your tables in Neon:

```python
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# ... your User, Category, Expense models from previous lessons ...

# Create all tables in Neon
Base.metadata.create_all(engine)
print("Tables created in Neon!")
```

**Output:**

```
Tables created in Neon!
```

**Verify in Neon dashboard**:

1. Go to your project
2. Click **SQL Editor**
3. Run:

```sql
SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';
```

**Output:**

```
table_name
----------
users
categories
expenses
```

Your Budget Tracker now runs on a real cloud database.

## Troubleshooting Common Errors

### Error: `could not connect to server`

**Cause**: Connection string is wrong, or network blocks the connection.

**Fix**:

1. Go to Neon dashboard
2. Copy connection string again (ensure you selected psycopg2)
3. Update your `.env` file
4. Try from a different network (some corporate firewalls block database ports)

### Error: `No module named 'psycopg2'`

**Cause**: PostgreSQL driver not installed.

**Fix**:

```bash
uv add psycopg2-binary
# OR
pip install psycopg2-binary
```

### Error: `FATAL: password authentication failed`

**Cause**: Password in connection string is wrong.

**Fix**:

1. Go to Neon dashboard
2. Click "Reset password" for your database user
3. Copy the new connection string
4. Update `.env`

### Error: `server closed the connection unexpectedly`

**Cause**: Connection went stale (Neon paused your database).

**Fix**: Ensure `pool_pre_ping=True` in your engine configuration. This detects dead connections and replaces them automatically.

### Error: `remaining connection slots are reserved`

**Cause**: Too many open connections (hit Neon's limit).

**Fix**:

1. Reduce `pool_size` (try 3 instead of 5)
2. Ensure you're closing sessions properly (`with Session(engine) as session:`)
3. Check for connection leaks (sessions opened but never closed)

## Working With AI on Connection Issues

Use AI as a structured diagnostic assistant, not as a guess machine.

Example loop:
1. Start with the exact error text.
2. Ask for an ordered checklist (DNS/host, credentials, SSL, firewall/VPN, Neon project state).
3. Report results after each check.
4. Ask for the next most likely cause only after each elimination.

For timeout errors, this process often isolates network policy issues (VPN/firewall/port restrictions) quickly.

## What Comes Next

Your system now persists in production. Next you must decide when a single SQL answer is enough and when independent verification is worth extra cost.

## Try With AI

### Prompt 1: Parse Connection String

**What you're learning:** Understanding the components of database URLs.

```
Given this connection string:
postgresql+psycopg2://alice:Pass123@ep-main-789.us-west-1.aws.neon.tech/mybudget?sslmode=require

Answer these questions:
1. What's the username?
2. What's the password? (hint: don't share this in real projects)
3. What's the database host?
4. What's the database name?
5. Why is sslmode=require at the end?
6. What does postgresql+psycopg2 mean?

For each answer, explain why that component matters.
```

### Prompt 2: Deploy Budget Tracker to Neon

**What you're learning:** Real cloud deployment workflow.

```
Help me complete these steps to deploy my Budget Tracker to Neon:

1. I've created a Neon account and project
2. I have my connection string
3. I need to:
   - Create .env file with DATABASE_URL
   - Add .env to .gitignore
   - Install psycopg2-binary
   - Update my engine with connection pooling
   - Test connection with SELECT 1
   - Run Base.metadata.create_all(engine)
   - Verify tables exist in Neon dashboard

Give me the exact commands and code for each step.
After each step, tell me how to verify it worked.
```

### Prompt 3: Deploy Verification

**What you're learning:** Proving your cloud database actually persists.

```
Help me verify my Neon deployment is truly persistent:

1. Write a Python script (script_a.py) that:
   - Connects to my Neon database
   - Creates a Category called "Verification Test" with color "#000000"
   - Prints "Data written" and exits

2. Write a SEPARATE Python script (script_b.py) that:
   - Connects to the SAME Neon database
   - Queries for a Category named "Verification Test"
   - Prints the result (or "Not found")

3. Show me how to run script_a.py, wait 10 seconds, then run script_b.py

If script_b.py finds the data, my cloud database works.
If not, something is wrong with my connection.
```

After each prompt, validate with evidence:
- Prompt 1: Can you parse every component of your own `DATABASE_URL`?
- Prompt 2: Are `users`, `categories`, and `expenses` visible in Neon SQL Editor?
- Prompt 3: Does `script_b.py` read the record created by `script_a.py`?

**Security reminder:** Never commit `.env` files. Never share connection strings in chat logs, screenshots, or code reviews. Rotate passwords if you accidentally expose them.

### Checkpoint

Before moving to L7 (Hybrid Patterns):

- [ ] Neon account created with budget-tracker project
- [ ] Connection string copied from Neon dashboard
- [ ] `.env` file created with `DATABASE_URL`
- [ ] `.env` added to `.gitignore` (verified with `git status`)
- [ ] `psycopg2-binary` installed
- [ ] Engine configured with connection pooling (5 parameters)
- [ ] Connection tested (`SELECT 1` succeeds)
- [ ] Tables created in Neon (`Base.metadata.create_all(engine)`)
- [ ] Tables verified in Neon SQL Editor
- [ ] You can correlate app-side failures with dashboard-side signals (project state, connection errors, table visibility)
- [ ] Documented patterns in `/database-deployment` skill

Your Budget Tracker now persists data forever in the cloud. Ready for the capstone.
