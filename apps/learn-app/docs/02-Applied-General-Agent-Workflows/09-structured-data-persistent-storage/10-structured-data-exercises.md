---
title: "Structured Data Practice Exercises"
sidebar_position: 10
chapter: 9
lesson: 9
duration_minutes: 120

primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Hands-on practice applying Lessons 0-8 concepts through 15 guided exercises across data modeling, CRUD, relationships, transactions, cloud deployment, and hybrid verification"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Database Application Building"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can design SQLAlchemy models, implement CRUD operations, and configure relationships for a multi-table application"

  - name: "Database Debugging"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can identify and fix common database bugs including wrong types, missing constraints, broken relationships, and transaction safety holes"

  - name: "Production Database Deployment"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can deploy a SQLAlchemy application to Neon PostgreSQL with proper security, connection pooling, and hybrid verification"

learning_objectives:
  - objective: "Build database applications from requirements using SQLAlchemy models, CRUD operations, and relationships"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student completes Build exercises (1.1, 2.1, 3.1, 4.1, 5.1, 6.1) producing working database applications"

  - objective: "Diagnose and fix database bugs across models, CRUD operations, relationships, and transactions"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student completes Debug exercises (1.2, 2.2, 3.2, 4.2, 5.2, 6.2) identifying root causes and applying correct fixes"

  - objective: "Deploy and verify database applications in production using Neon PostgreSQL and hybrid verification patterns"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student completes capstone projects integrating all patterns with cloud deployment and verification"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (build pattern, debug pattern, hybrid verification) — exercises reinforce existing L0-L8 knowledge through application"

differentiation:
  extension_for_advanced: "Complete all 3 capstone projects; attempt Debug exercises before reading the bug list"
  remedial_for_struggling: "Start with Module 1 only; use Build exercises exclusively before attempting Debug exercises"
---

# Structured Data Practice Exercises

You've learned every piece of the database puzzle. SQLAlchemy models that define data as Python classes. CRUD operations wrapped in proper session management. Relationships that let you navigate between tables without writing JOINs. Transactions that protect multi-step operations from partial failure. Neon PostgreSQL for production deployment with connection pooling and environment variables. Hybrid SQL+bash verification that catches errors no single tool would find. You built a complete Budget Tracker that ties all of these together. That's a powerful toolkit — but the gap between building one application in a guided lesson and designing a database solution from a set of messy requirements is where most people discover what they actually know.

These 15 exercises close that gap. Each module gives you two exercises: a **Build** exercise where you create a working database application from realistic requirements, and a **Debug** exercise where you find and fix bugs in broken code. Three skills run through every exercise: **data modeling** (translating real-world entities into SQLAlchemy models with correct types, constraints, and relationships), **database debugging** (finding bugs that don't crash — wrong column types, missing constraints, broken relationships, transaction safety holes), and **production deployment** (configuring Neon PostgreSQL with proper security, pooling, and hybrid verification).

The difference between knowing SQLAlchemy patterns and being a database developer is practice. Every exercise uses realistic scenarios — a library catalog, a recipe book, a music library, a game inventory system — with the edge cases that break naive implementations: nullable columns that should be required, relationships missing `back_populates`, transactions without rollback, and connection strings with hardcoded credentials. By the end, you'll have built and debugged more database applications than most people encounter in their first year of development.

:::info Download Exercise Files
**[Download Structured Data Exercises (ZIP)](https://github.com/panaversity/claude-code-structured-data-exercises/releases/latest/download/structured-data-exercises.zip)**

After downloading, unzip the file. Each exercise has its own folder with an `INSTRUCTIONS.md` and any starter files you need.

If the download link doesn't work, visit the [repository releases page](https://github.com/panaversity/claude-code-structured-data-exercises/releases) directly.
:::

---

## How to Use These Exercises

The workflow for every exercise is the same:

1. **Open the exercise folder** from the `claude-code-structured-data-exercises/` directory
2. **Read the INSTRUCTIONS.md** inside the folder — it describes the starter files, the database schema (if provided), and your task
3. **Read the walkthrough below** for context on what you're practicing and why
4. **Start Claude Code** and point it at the exercise folder
5. **Work through the exercise** — for Build exercises, create new code from requirements; for Debug exercises, find and fix bugs in broken code
6. **Reflect** using the questions provided — compare your approach with what you expected and identify what surprised you

You don't need to complete all 15 in one sitting. Work through one module at a time. Each module builds on the workflows from specific chapter lessons.

---

## Tool Guide

- **Claude Code** — Required for all exercises. Every exercise involves writing or debugging Python database code. You'll use SQLAlchemy, session management, and SQL queries.
- **Python 3.x** with `sqlalchemy` installed. Verify with: `python3 -c "import sqlalchemy; print(sqlalchemy.__version__)"`
- **For Modules 5-6:** A Neon PostgreSQL account (free tier). You'll also need `psycopg2-binary` and `python-dotenv` installed.

---

## Key Differences from Chapter Lessons

In Lessons 0-8, you learned each pattern in isolation with guided walkthroughs using the Budget Tracker. These exercises are different in three ways:

- **No step-by-step instructions.** The exercises describe the scenario, the data model, and the goal. You decide the approach, write the prompts, and handle edge cases yourself.
- **Build + Debug pairing.** Every module has a Build exercise (create a working application) and a Debug exercise (find and fix bugs in broken code). Debugging someone else's database code develops different skills than writing your own — you learn to read models critically, trace relationship navigation, and spot transaction safety holes that don't produce exceptions.
- **Increasing independence.** Modules 1-2 provide starter prompts to scaffold your learning. Modules 3-6 remove the scaffolding. Capstones remove everything — you design the entire database application from requirements.

By Module 6, you should be able to face a new database requirement and instinctively reach for the right pattern without needing to review the chapter lessons.

---

## The Database Development Framework

Use this for every exercise:

1. **Model** — Define the data structure. What are the entities? What are their attributes? What types and constraints does each column need? This is the foundation — wrong types or missing constraints create bugs that surface much later.
2. **Connect** — Establish database connection. For development, use `sqlite:///:memory:` or a local SQLite file. For production exercises, configure Neon with environment variables and connection pooling.
3. **Operate** — Implement CRUD with session management. Every database operation needs a session. Use context managers (`with Session(engine) as session:`) to prevent resource leaks. Push filtering to the database, not Python.
4. **Protect** — Add transaction safety. Any operation that modifies multiple records needs try/except with commit/rollback. Single operations are already atomic; multi-step operations need explicit protection.
5. **Verify** — Test and check results. Query the database after writes to confirm data persisted correctly. For production, use hybrid SQL+bash verification to cross-check critical numbers.
6. **Deploy** — Move to production. Swap `sqlite:///:memory:` for a Neon connection string stored in `.env`. Add `pool_pre_ping=True` for connection health checks. Verify with the Neon dashboard.

This framework applies to any domain where data needs persistent, structured storage: customer databases, inventory systems, booking platforms, or any application where "if it's structured data, it belongs in a database." Notice that Model comes before Connect — getting the data structure right before writing any database code saves hours of rework.

---

## Assessment Rubric

For each exercise, evaluate yourself on:

| Criteria | Beginner (1) | Developing (2) | Proficient (3) | Advanced (4) |
|---|:---:|:---:|:---:|:---:|
| **Data Modeling** | Models missing types or constraints | Correct types but missing relationships | Full model with types, constraints, and relationships | Models include indexes, defaults, and cascade rules |
| **Session Management** | No context manager; manual open/close | Context manager but no error handling | Context manager with try/except on writes | Session factory pattern with proper scoping |
| **Relationship Design** | No relationships; manual foreign key queries | One-sided relationships without back_populates | Bidirectional relationships with correct navigation | Cascade rules, lazy loading choices, and join optimization |
| **Transaction Safety** | No transaction boundaries | Try/except but no rollback | Proper commit/rollback on multi-step operations | Transaction isolation levels and retry logic |
| **Debugging Accuracy** | Identifies fewer than half the bugs | Identifies most bugs but fixes introduce new issues | Identifies and fixes all bugs cleanly | Explains root cause, fixes bug, and adds prevention |

---

## Module 1: Data Modeling

> **Core Skill:** Translating real-world requirements into SQLAlchemy models with correct types, constraints, and table structure (Lessons 1-2)
>
> Lessons 1-2 taught you to define models as Python classes and choose the right column types. These exercises push those skills into scenarios where the requirements are ambiguous and the data model decisions have consequences — a wrong type or missing constraint surfaces as a bug much later, long after you've forgotten the modeling decision that caused it.

### Exercise 1.1 — Library Catalog (Build)

**Build:** Data Modeling — Design models for a library system from requirements

**The Problem:**
Open the `module-1-data-modeling/exercise-1.1-library-catalog/` folder. You'll find `requirements.txt` — a plain-English description of what a small library needs to track: books (title, author, ISBN, publication year, genre), members (name, email, membership date), and loans (which member borrowed which book, checkout date, due date, return date). Some books have multiple authors. Some members have overdue books. The library wants to answer questions like "Which books are currently checked out?" and "Which members have overdue loans?"

**Your Task:**
Design SQLAlchemy models for all three entities. Choose the right column types for each attribute (String vs. Integer vs. Date, nullable vs. required, unique constraints). Create the database, populate it with the sample data provided in `sample-data.json`, and write queries that answer the library's questions. Verify by checking that your query results match the expected answers in `expected-queries.txt`.

**What You'll Learn:**

- How to translate English requirements into column types and constraints — "ISBN" means unique String, "publication year" means Integer not Date, "return date" could be NULL (book still checked out)
- That modeling decisions are design decisions: should "multiple authors" be a comma-separated String, a separate Author table, or a many-to-many join table? Each choice has trade-offs
- Why constraints prevent bugs: a `nullable=False` on `checkout_date` catches the error of creating a loan without recording when it was checked out

**Starter Prompt (Intentionally Vague):**

> "Make a database for a library."

**Better Prompt (Build Toward This):**

After reading the requirements and sample data: "Create SQLAlchemy models for a library system with three tables: Book (title, author, isbn as unique string, publication_year as integer, genre), Member (name, email as unique, membership_date), and Loan (foreign keys to book and member, checkout_date as required, due_date as required, return_date as nullable — null means not yet returned). Use sqlite:///:memory: for now. Populate with the data from sample-data.json and write queries for: (1) all currently checked-out books, (2) all members with overdue loans, (3) the most borrowed book."

**Reflection Questions:**

1. Which column type decision was hardest? Did you change any types after seeing the sample data?
2. How did you handle the "multiple authors" requirement? What would break if a book had 5 authors?
3. If the library added a "reservations" feature (members can reserve books that are checked out), how would your model change?

---

### Exercise 1.2 — Broken Pet Store (Debug)

**Debug:** Data Modeling — Fix 6 bugs in pet store models

**The Problem:**
Open the `module-1-data-modeling/exercise-1.2-broken-pet-store/` folder. You'll find `models.py` — SQLAlchemy models for a pet store database with three tables: Pet, Owner, and Visit (vet visits). The models were written by someone who made 6 specific mistakes: a price column using Integer instead of Float (truncating $29.99 to $29), a required column marked nullable (owners can be created without names), a String column with a too-short max length (breed names get silently truncated), a Date column storing dates as strings ("2024-03-15" instead of a proper Date object), a missing unique constraint on email (allowing duplicate owner registrations), and a foreign key pointing to a non-existent table name.

**Your Task:**
Run the provided `test_models.py` script which attempts to create the database and insert sample data. Some tests will fail immediately (the foreign key error). Others will succeed but produce wrong results (the Integer price truncation). Find all 6 bugs, fix them in `models.py`, and run the test script until all tests pass with correct data.

**What You'll Learn:**

- That model bugs create two categories of failure: crashes (wrong table name) and silent data corruption (Integer truncating decimals) — the second category is far more dangerous
- How to read test failures as diagnostic clues: a foreign key error tells you exactly which relationship is broken; a wrong price tells you to check the column type
- Why defensive modeling matters: every missing constraint is a bug waiting to happen when real data arrives

**Starter Prompt (Intentionally Vague):**

> "The pet store database has bugs. Fix them."

**Better Prompt (Build Toward This):**

After running `python3 test_models.py` and seeing the failures: "The test_models.py script reveals bugs in models.py. Start with the crash-level failures (the foreign key error prevents table creation). Fix that first, then re-run. For remaining tests that pass but produce wrong results, compare actual vs. expected values — if a price shows 29 instead of 29.99, check the column type. Find and fix all 6 bugs one at a time, re-running tests after each fix."

**Reflection Questions:**

1. Which bug would have caused the most damage in production — the one that crashed, or the one that silently truncated prices?
2. How many of the 6 bugs would a code review catch by reading the models alone, without running any tests?
3. What naming convention or comment style would have prevented the foreign key table name error?

---

## Module 2: CRUD Operations

> **Core Skill:** Implementing Create, Read, Update, Delete with proper session management (Lesson 3)
>
> Lesson 3 taught you to create and read data using sessions. These exercises push those skills into scenarios with more operations, more edge cases, and data coming from external sources (CSV files) rather than hardcoded values.

### Exercise 2.1 — Recipe Book (Build)

**Build:** CRUD Operations — Implement CRUD for a recipe database with CSV import

**The Problem:**
Open the `module-2-crud-operations/exercise-2.1-recipe-book/` folder. You'll find `recipes.csv` — a file with 30 recipes containing name, category (Breakfast, Lunch, Dinner, Dessert), prep time in minutes, difficulty (Easy, Medium, Hard), and ingredients as a semicolon-separated list. You also have `requirements.txt` describing the operations the recipe book needs: add a recipe, search by category, search by ingredient, update prep time, delete a recipe, and list all recipes sorted by difficulty.

**Your Task:**
Build SQLAlchemy models for the recipe data, import all 30 recipes from the CSV, and implement all six CRUD operations as Python functions. Verify each operation: after adding a recipe, query to confirm it exists; after updating prep time, query to confirm the new value; after deleting, query to confirm it's gone. Run the verification script in `verify-operations.py` to confirm all operations work correctly.

**What You'll Learn:**

- How to import external data (CSV) into a database — including handling the semicolon-separated ingredients field, which requires deciding between a single text column or a separate ingredients table
- That each CRUD operation needs its own session management pattern: creates need `add` + `commit`, reads need `query` + `filter`, updates need `query` + modify + `commit`, deletes need `query` + `delete` + `commit`
- Why verification after every write operation is non-negotiable: a commit can succeed (no exception) but the data might not match what you intended if a type coercion happened silently

**Starter Prompt (Intentionally Vague):**

> "Build a recipe database from this CSV."

**Better Prompt (Build Toward This):**

After examining the CSV format: "Create a SQLAlchemy model for Recipe with columns: name (unique string), category (string), prep_time_minutes (integer), difficulty (string), ingredients (text — store the semicolon-separated list as-is for now). Import all 30 recipes from recipes.csv. Then implement 6 functions: add_recipe(), search_by_category(), search_by_ingredient(), update_prep_time(), delete_recipe(), list_by_difficulty(). Each function should use a context-managed session. Verify each function by calling it and printing results."

**Reflection Questions:**

1. How did you handle the ingredients field — one text column or a separate table? What queries become easier or harder with each approach?
2. What happens if you try to add a recipe with a name that already exists? Does your code handle that gracefully or crash?
3. Which CRUD operation was most complex to implement? Which was most likely to have a subtle bug?

---

### Exercise 2.2 — Broken Task Manager (Debug)

**Debug:** CRUD Operations — Fix 5 CRUD bugs

**The Problem:**
Open the `module-2-crud-operations/exercise-2.2-broken-task-manager/` folder. You'll find `task_manager.py` — a complete task management application with create, read, update, complete, and delete operations. The application runs without crashing, but 5 operations produce wrong results: creating a task doesn't set the default status to "pending" (it's NULL), reading tasks filters by wrong column (filtering on `id` instead of `status`), updating a task description commits before modifying (the old description persists), completing a task sets `completed_at` but doesn't change `status` to "done", and deleting a task uses `session.query(Task).delete()` without a filter (deleting ALL tasks instead of one).

**Your Task:**
Run `test_task_manager.py` which exercises each operation and checks the result. Five tests will fail. For each failure, trace through the code in `task_manager.py` to find the line causing the wrong behavior. Fix all 5 bugs and verify that all tests pass.

**What You'll Learn:**

- That CRUD bugs are ordering bugs (commit before modify), logic bugs (filter on wrong column), and completeness bugs (update one field but forget the related field) — not syntax errors
- How to trace a wrong result back to a specific line: if the status is NULL, find where the default should be set; if the wrong tasks are returned, check the filter clause
- Why "the application runs" is not evidence of correctness — every bug in this exercise produces a result, just the wrong one

**Reflection Questions:**

1. Which bug was hardest to find from the test output alone? Did you need to read the source code, or could you diagnose it from the test failure message?
2. The "delete all instead of one" bug is catastrophic. How would you prevent this class of error in your own code?
3. If you wrote this task manager from scratch, which of these 5 bugs would you have likely introduced yourself? What does that tell you about your coding habits?

---

## Module 3: Relationships & Navigation

> **Core Skill:** Configuring and navigating one-to-many and many-to-many relationships (Lesson 4)
>
> Lesson 4 taught you to define relationships with `relationship()` and `back_populates` for the Budget Tracker. These exercises push those skills into more complex relationship topologies — a music library with Artist, Album, and Track creates a chain of relationships where navigation patterns matter.

### Exercise 3.1 — Music Library (Build)

**Build:** Relationships — Add relationships to Artist/Album/Track models

**The Problem:**
Open the `module-3-relationships/exercise-3.1-music-library/` folder. You'll find `models_starter.py` — SQLAlchemy models for Artist, Album, and Track with correct columns and foreign keys but NO relationships defined. You also have `sample-data.json` with 5 artists, 12 albums, and 40 tracks, plus `queries.txt` describing 8 queries the music library needs to support: "all albums by an artist," "all tracks on an album," "the artist who made a given track," "all tracks by an artist across all albums," "albums released in a given year," "the longest track on each album," "artists with more than 2 albums," and "total duration of an artist's discography."

**Your Task:**
Add `relationship()` declarations to all three models with correct `back_populates`. Import the sample data. Then write all 8 queries. Some queries (like "all albums by an artist") use relationship navigation directly. Others (like "total duration of an artist's discography") require navigating through two relationship levels: artist.albums, then for each album, album.tracks. Verify each query against `expected-results.txt`.

**What You'll Learn:**

- How relationship chains work: to get from Artist to Track, you navigate artist.albums, then album.tracks — there's no direct artist.tracks shortcut unless you create one
- That some queries are easier with relationship navigation and others are easier with explicit joins and filters — learning to choose the right approach for each question is the real skill
- Why `back_populates` matters: without it, adding a track to an album doesn't update the album's track list until you refresh, creating confusing bugs during data import

**Reflection Questions:**

1. Which of the 8 queries was easiest with relationship navigation? Which one made you wish you could write raw SQL instead?
2. When navigating from Artist to Track, did you use nested loops (`for album in artist.albums: for track in album.tracks`) or a single query with joins? What are the trade-offs?
3. If the library added a "Playlist" feature (playlists contain tracks from any album), what type of relationship would that require, and how would it differ from the Artist-Album-Track chain?

---

### Exercise 3.2 — Broken Blog (Debug)

**Debug:** Relationships — Fix relationship configuration bugs

**The Problem:**
Open the `module-3-relationships/exercise-3.2-broken-blog/` folder. You'll find `blog.py` — a blog application with User, Post, and Comment models. The models have foreign keys and relationships defined, but the relationships are broken in 5 ways: `back_populates` names don't match between the two sides of a relationship, one relationship references the wrong model class name, a cascade rule is missing (deleting a post leaves orphan comments), a `lazy` loading option prevents accessing comments in a common query pattern, and one foreign key column has the wrong type (String instead of Integer, causing silent join failures).

**Your Task:**
Run `test_blog.py` which creates users, posts, and comments, then tests relationship navigation. Some tests crash immediately (wrong model reference). Others return empty lists where data should exist (silent join failures from type mismatch). Find all 5 bugs and fix them. After each fix, re-run the tests to confirm the specific relationship now works without breaking others.

**What You'll Learn:**

- That relationship bugs produce two failure modes: crashes (wrong model name, mismatched back_populates) and silent empty results (type mismatch on foreign keys causes joins to find zero matches)
- How to diagnose "empty results" bugs: if `post.comments` returns an empty list but comments exist in the database, the join condition is failing — check foreign key types match
- Why cascade rules matter for data integrity: without `cascade='all, delete-orphan'`, deleting a post leaves comment rows pointing to a non-existent post

**Reflection Questions:**

1. The type mismatch bug (String foreign key vs. Integer primary key) produced no error — just empty results. How long would this bug survive in production before someone noticed?
2. Which relationship bug would a linter or type checker have caught? Which ones require running the code to discover?
3. After fixing all 5 bugs, what would you add to `test_blog.py` to prevent these same bugs from reappearing after future code changes?

---

## Module 4: Transaction Safety

> **Core Skill:** Protecting multi-step operations with commit/rollback boundaries (Lesson 5)
>
> Lesson 5 taught you atomicity — all-or-nothing transactions for the Budget Tracker. These exercises push transaction safety into scenarios where the consequences of partial failure are severe and obvious: a game where items vanish, a bank where money disappears.

### Exercise 4.1 — Game Inventory Trading (Build)

**Build:** Transactions — Implement atomic item trades between players

**The Problem:**
Open the `module-4-transactions/exercise-4.1-game-inventory/` folder. You'll find `game_models.py` — models for Player (name, gold balance) and InventoryItem (name, value, owner foreign key) — and `setup_data.py` which creates 4 players with various items and gold balances. The game needs a trading system: Player A offers an item and some gold to Player B in exchange for one of Player B's items. A trade involves 4 database operations: remove item from A's inventory, add item to B's inventory, deduct gold from A, add gold to B. If ANY of these fails (insufficient gold, item doesn't exist, player not found), NONE should happen.

**Your Task:**
Implement a `trade()` function that executes all 4 operations inside a transaction with proper commit/rollback. Test with the 5 trade scenarios in `test-trades.txt`: a valid trade, a trade where the buyer has insufficient gold, a trade where the item doesn't exist, a trade where one player is not found, and a trade that violates a unique constraint. After each trade (successful or failed), verify that both players' inventories and gold balances are correct — no items vanished, no gold was duplicated.

**What You'll Learn:**

- That without transactions, a failed trade can leave the database in an impossible state: Player A's item is removed but Player B never receives it — the item vanishes
- How to structure try/except/finally blocks around multi-step database operations so that any exception triggers a complete rollback
- Why testing the failure cases is as important as testing the success case: the whole point of transactions is that failures leave the database unchanged

**Reflection Questions:**

1. In the "insufficient gold" scenario, at what point in the 4-step trade does the failure occur? What state would the database be in without the rollback?
2. Did you validate all preconditions (sufficient gold, item exists, player exists) before starting the transaction, or did you rely on the database to raise exceptions? What are the trade-offs of each approach?
3. If two trades happen simultaneously (Player A trades with B while Player B trades with C), could they conflict? What database feature prevents that?

---

### Exercise 4.2 — Broken Bank (Debug)

**Debug:** Transactions — Find and fix transaction safety holes

**The Problem:**
Open the `module-4-transactions/exercise-4.2-broken-bank/` folder. You'll find `bank.py` — a banking application with Account model and functions for deposit, withdraw, and transfer. The transfer function moves money between two accounts but has 4 transaction safety bugs: the debit and credit happen in separate sessions (so a crash between them loses money), there's no check for sufficient funds before the debit (overdrawing is possible), the rollback in the except block is called on the wrong session object, and a commit happens after the debit but before the credit (violating atomicity).

**Your Task:**
Run `test_bank.py` which simulates normal transfers and failure scenarios. The normal transfer appears to work, but the failure scenarios reveal the bugs: a simulated crash between debit and credit shows money disappearing, an overdraft test shows negative balances, and a rollback test shows the wrong session being rolled back. Find all 4 bugs, fix them, and verify that every failure scenario leaves both account balances unchanged.

**What You'll Learn:**

- That transaction bugs are invisible during success — they only manifest during failures, which is exactly when you need them most
- How "separate sessions" breaks atomicity: if the debit commits in session 1 and the credit fails in session 2, rolling back session 2 doesn't undo session 1's commit
- Why testing the failure path is the only way to verify transaction safety — a transfer that succeeds proves nothing about what happens when it fails

**Reflection Questions:**

1. The "commit after debit but before credit" bug is the classic atomicity violation. Why did the normal transfer test NOT catch it?
2. How many of the 4 bugs would be caught by code review alone, without running the failure tests?
3. If this bank application were in production, how would you discover these bugs? What monitoring would detect money appearing or disappearing?

---

## Module 5: Cloud Deployment & Security

> **Core Skill:** Deploying SQLAlchemy applications to Neon PostgreSQL with proper configuration (Lessons 6-7)
>
> Lessons 6-7 taught you to connect to Neon, manage credentials with .env files, configure connection pooling, and verify deployment with hybrid SQL+bash patterns. These exercises push those skills into realistic deployment and troubleshooting scenarios.

### Exercise 5.1 — Contact Book Deploy (Build)

**Build:** Cloud Deployment — Configure a working app for Neon PostgreSQL

**The Problem:**
Open the `module-5-cloud-deployment/exercise-5.1-contact-book-deploy/` folder. You'll find `contact_book.py` — a working contact management application that uses `sqlite:///:memory:`. The app has Contact and Group models with a many-to-many relationship, full CRUD operations, and a search function. It works perfectly on local SQLite. Your task is to deploy it to Neon PostgreSQL without changing any application logic — only the database connection and configuration.

**Your Task:**
Create a Neon project (free tier). Configure the connection string in a `.env` file. Modify the engine creation to use the Neon connection string with `pool_size=5`, `max_overflow=10`, `pool_pre_ping=True`, and `connect_args={"sslmode": "require"}`. Add `load_dotenv()` at startup. Create a `.gitignore` that excludes `.env`. Run the application against Neon and verify: create 5 contacts in 2 groups, search by name, search by group, delete a contact and verify cascade behavior. Confirm data persists by stopping and restarting the application.

**What You'll Learn:**

- That deploying to production is a configuration change, not a code rewrite — the same SQLAlchemy models and CRUD operations work on SQLite and PostgreSQL
- Why each pool setting matters: `pool_pre_ping` prevents stale connections after Neon's auto-pause, `sslmode` encrypts data in transit, `pool_size` controls resource usage
- The `.env` + `.gitignore` pattern as non-negotiable security: one accidental commit of credentials gives anyone database access

**Reflection Questions:**

1. What failed on the first attempt to connect to Neon? Was it credentials, SSL, or pool configuration?
2. How did you verify that data persists? Did you restart the application and query, or did you check the Neon dashboard?
3. If you needed to switch from Neon to another PostgreSQL provider (Supabase, Railway), how many lines of code would change?

---

### Exercise 5.2 — Connection Doctor (Debug)

**Debug:** Cloud Deployment — Diagnose 5 different connection failure scenarios

**The Problem:**
Open the `module-5-cloud-deployment/exercise-5.2-connection-doctor/` folder. You'll find 5 Python scripts (`scenario-1.py` through `scenario-5.py`), each attempting to connect to a PostgreSQL database and failing for a different reason. Each script has a `.env` file with intentionally broken configuration. The failures are: wrong password, wrong hostname, missing SSL mode (Neon requires SSL), expired/stale connection pool (no `pool_pre_ping`), and a connection string with the database driver misspelled (`postgresql+psycopg3` instead of `postgresql+psycopg2`).

**Your Task:**
Run each script, read the error message, diagnose the root cause, and fix the `.env` or connection configuration. For each scenario, document: the exact error message, what it means, where the fix lives (`.env` vs. Python code), and the corrected configuration. Compile your findings into `DIAGNOSIS.md` as a troubleshooting reference.

**What You'll Learn:**

- That database connection errors have diagnostic messages that point directly to the cause — "password authentication failed" means wrong password, "could not translate host name" means wrong hostname
- How to build a systematic troubleshooting checklist: credentials, hostname, SSL, driver, pool settings — check each one in order
- That documenting your fixes creates a reusable troubleshooting guide you'll reference every time a connection fails in the future

**Reflection Questions:**

1. Which error message was most helpful (pointed directly to the fix)? Which was most misleading?
2. How long did each diagnosis take? Did the time decrease as you worked through more scenarios?
3. If a connection fails in production at 3am, which of these 5 scenarios is most likely? What monitoring would alert you before users notice?

---

## Module 6: Hybrid Verification & Tool Selection

> **Core Skill:** Using SQL+bash cross-checks and choosing the right tool for each query (Lessons 7-8)
>
> Lessons 7-8 taught you hybrid verification patterns and tool choice based on the Braintrust research. These exercises push those skills into scenarios where choosing the wrong tool or skipping verification produces plausible but wrong answers.

### Exercise 6.1 — Expense Audit (Build)

**Build:** Hybrid Verification — Build SQL+bash cross-check pipeline

**The Problem:**
Open the `module-6-hybrid-verification/exercise-6.1-expense-audit/` folder. You'll find `expenses.db` — a pre-populated SQLite database with 200 expense records across 5 categories, and `expenses-export.csv` — a CSV export of the same data. The two sources SHOULD match, but they don't. Three records were modified in the database after the CSV was exported: one amount was updated, one category was changed, and one record was deleted from the database but still exists in the CSV.

**Your Task:**
Build a hybrid verification pipeline that cross-checks the SQL database against the CSV export. Write a SQL query that summarizes total spending per category from the database. Write a bash/Python script that calculates the same totals from the CSV. Compare the two sets of totals and identify which categories have discrepancies. Then drill into those categories to find the specific records that differ. Document all 3 discrepancies in `AUDIT-REPORT.md` with the exact record, what changed, and which source is authoritative.

**What You'll Learn:**

- That cross-checking with two independent tools catches errors that either tool alone would miss — the SQL query can't know about deleted records still in the CSV, and the CSV can't know about updated records in the database
- How to structure an audit: start with aggregate comparisons (category totals), then drill into discrepancies at the record level
- Why "which source is authoritative" is a business decision, not a technical one — the database is more current, but the CSV might be the audited record

**Reflection Questions:**

1. Which discrepancy was hardest to find — the updated amount, the changed category, or the deleted record? Why?
2. If both sources showed the same totals, would that prove they contain identical records? (Hint: think about offsetting errors.)
3. In what business scenario would you trust the CSV over the database? When would you trust the database?

---

### Exercise 6.2 — Wrong Tool, Wrong Answer (Debug/Analysis)

**Debug/Analysis:** Tool Selection — Analyze 5 wrong-tool scenarios

**The Problem:**
Open the `module-6-hybrid-verification/exercise-6.2-wrong-tool/` folder. You'll find 5 scenarios, each with a question, a tool choice, and the output produced. Each scenario used the WRONG tool for the job, producing an answer that looks plausible but is wrong. The scenarios are: (1) calculating compound interest with bash (floating-point precision loss), (2) querying structured database data with grep on a CSV export (missed quoted fields), (3) summing financial records with awk (currency symbol parsing failure), (4) finding duplicate records with sort|uniq (case-sensitivity missed "alice" vs "Alice"), and (5) joining two datasets with paste (row alignment broke when one file had blank lines).

**Your Task:**
For each scenario, analyze: what question was being asked, why the chosen tool produced the wrong answer, what the right tool would have been, and what the correct answer is. Implement the correct solution for each using the right tool. Write your analysis in `TOOL-ANALYSIS.md` with a one-paragraph explanation per scenario and the correct command/script.

**What You'll Learn:**

- That plausible wrong answers are more dangerous than obvious errors — a compound interest calculation that's off by $47 looks reasonable but compounds into a large difference over time
- The tool selection framework from Lesson 7: bash for file operations, Python for computation, SQL for structured queries, hybrid for verification
- How each tool's weakness creates a specific failure mode: bash can't do decimals, grep can't parse CSV, awk chokes on currency symbols

**The Extension:** Create a one-page "Tool Selection Cheat Sheet" that maps question types to recommended tools. Include the failure mode for each wrong-tool pairing (e.g., "bash + decimal math = precision loss").

**Reflection Questions:**

1. Which wrong-tool scenario produced the most plausible wrong answer? Would you have caught it without comparing to the correct answer?
2. Is there any scenario where the "wrong" tool could have been made to work with enough effort? When is it better to switch tools vs. work around a tool's limitations?
3. How does this analysis connect to the Braintrust research from Lesson 7? Which of these 5 scenarios mirrors the SQL vs. bash accuracy gap?

---

## Module 7: Capstone Projects

> **Choose one (or more). Build a real database application from requirements — no starter prompts provided.**

Capstones are different from the exercises above. There are no guided prompts — you design the entire database application yourself. Each project requires applying all the skills from Modules 1-6 together: modeling entities, implementing CRUD, configuring relationships, protecting transactions, deploying to Neon, and verifying with hybrid patterns. Where module exercises test individual skills, capstones test your ability to orchestrate those skills into a complete, deployed application.

The progression across capstones is intentional: Capstone A is a guided integration project with clear requirements and expected output. Capstone B is a real-world migration problem where the data is messy and the schema decisions are yours. Capstone C is a forensics challenge where you inherit a broken application and must fix it under pressure. Each capstone demands more judgment and less scaffolding than the last.

### Capstone A — Student Grade Portal

**Integration:** Build a complete grade tracking system from requirements to deployment.

Open the `module-7-capstone/capstone-A-student-portal/` folder. You'll find `requirements.md` describing a grade tracking system for a small school: Students (name, email, enrollment date), Courses (name, code, credits, instructor), and Enrollments (student + course + grade, with constraints like grade must be A-F or NULL for in-progress). The system needs to answer: "What's this student's GPA?", "Who's failing this course?", "Which courses has this student completed?", and "What's the class average for each course?"

Take this through the complete Database Development Framework:

1. **Model** — Design all three tables with correct types, constraints, foreign keys, and relationships
2. **Connect** — Start with SQLite for development, switch to Neon for deployment
3. **Operate** — Implement CRUD for students, courses, and enrollments; implement GPA calculation
4. **Protect** — Enrollment changes (add/drop courses, grade updates) need transaction safety
5. **Verify** — Cross-check GPA calculations with manual computation on sample data
6. **Deploy** — Deploy to Neon with proper security, pooling, and connection handling

**Deliverables:**

- `models.py` — SQLAlchemy models for Student, Course, Enrollment
- `operations.py` — All CRUD operations with session management
- `queries.py` — GPA calculation, failing students, class averages
- `deploy.py` — Neon connection configuration
- `VERIFICATION.md` — How you verified GPA calculations are correct
- `test_grade_portal.py` — Tests covering all operations and edge cases

---

### Capstone B — CSV Migration

**Real-world:** Migrate 500 rows of messy CSV data into a normalized database.

Open the `module-7-capstone/capstone-B-csv-migration/` folder. You'll find `legacy-data.csv` — a 500-row export from a spreadsheet-based inventory system for a small retail store. The data is in a single flat table with denormalized data: product name, category, supplier name, supplier email, supplier phone, price, quantity, last ordered date, and notes. The same supplier appears on many rows with slightly different formatting ("Acme Corp", "ACME CORP.", "Acme Corporation"). Dates use 4 different formats. Some prices include currency symbols, some don't. Notes contain commas that break naive CSV parsing.

**Your Task:**
Design a normalized database schema (Products, Suppliers, Categories), clean and migrate all 500 rows, and verify the migration is lossless. The hardest part isn't the code — it's the data cleaning decisions: are "Acme Corp" and "ACME CORP." the same supplier? How do you handle rows with missing supplier info? What do you do with products that have a category that appears only once?

**Deliverables:**

- `models.py` — Normalized schema with proper relationships
- `migrate.py` — Script that reads CSV, cleans data, and populates database
- `verify_migration.py` — Script that proves no data was lost or corrupted
- `MIGRATION-REPORT.md` — Decisions made, data quality issues found, row counts before/after
- `CLEANING-LOG.md` — Every data cleaning decision with before/after examples

---

### Capstone C — Disaster Recovery

**Forensics:** Fix 8+ bugs in a broken Budget Tracker application.

Open the `module-7-capstone/capstone-C-disaster-recovery/` folder. You'll find `budget_tracker.py` — a complete Budget Tracker application that was "working last week" but now has 8+ bugs introduced during a hasty refactoring. The application has User, Expense, and Category models, CRUD operations, transaction-protected transfers between categories, and a Neon deployment configuration. It's broken at every level: model bugs (wrong types, missing constraints), CRUD bugs (wrong session management), relationship bugs (missing back_populates), transaction bugs (no rollback), and deployment bugs (hardcoded credentials, missing pool settings).

**Your Task:**
Get the application working again. Run `test_budget_tracker.py` to see the full list of failures. Triage the bugs by severity — start with crashes, then fix silent data corruption, then fix security issues. Document every bug you find, how you found it, and how you fixed it. Your `RECOVERY-REPORT.md` should read like a postmortem: what went wrong, what the impact would have been, and what process change would prevent it.

**Deliverables:**

- Fixed `budget_tracker.py` with all bugs resolved
- `RECOVERY-REPORT.md` — Postmortem with: each bug, severity, fix, and prevention
- `test_budget_tracker.py` — Updated tests (if needed) that verify all fixes
- All tests passing with correct results

---

## What's Next

You've built, debugged, and deployed database applications across 15 exercises — from simple model design to multi-table systems with transaction safety and hybrid verification. The Database Development Framework (Model, Connect, Operate, Protect, Verify, Deploy) applies to any domain where data needs persistent, structured storage: customer databases, inventory systems, booking platforms, or any application where relationships between data matter.

The three skills you practiced — modeling data as code, debugging silent database errors, and deploying to production with proper security — are the exact skills that separate someone who can follow a database tutorial from someone who can build a database application from requirements. Up next is the Chapter Quiz, where you'll test your understanding of every pattern from Lessons 0-8. The exercises you just completed prepare you well — you've applied every concept, not just read about it. And looking at the bigger picture, you now have four tools in your Part 2 toolkit: bash for file operations, Python for computation, SQL for structured queries, and hybrid patterns for verification. That's a complete foundation for the autonomous agent workflows coming in the chapters ahead.
