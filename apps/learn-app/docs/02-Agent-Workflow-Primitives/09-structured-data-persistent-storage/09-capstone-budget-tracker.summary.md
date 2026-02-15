### Core Concept

The capstone integrates every pattern from the chapter -- models, CRUD, relationships, transactions, and Neon deployment -- into a single working Budget Tracker application. No new concepts are introduced; this lesson proves that all the pieces work together as a production-ready system.

### Key Mental Models

- **Integration over accumulation**: Knowing individual patterns (models, sessions, transactions) is not the same as combining them into a working application. The capstone forces you to see how models feed into CRUD, which depends on relationships, which is protected by transactions, which runs on Neon.
- **Reusable skill as career asset**: The `/database-deployment` skill you have been building is not specific to Budget Tracker. The same models/sessions/relationships/transactions/pooling patterns apply to any project needing persistent, queryable, relational data.

### Critical Patterns

- Application structure: imports and engine setup, model definitions, CRUD functions (create/read/update/delete), relationship queries (monthly summary, by-category grouping, top expenses), atomic transactions (budget transfers), utilities (init, seed, test connection)
- Every CRUD function follows the same shape: `with Session(engine) as session: try: ... session.commit() except: ... return error`
- Complex queries combine joins, aggregation (`func.sum`, `func.count`), grouping (`group_by`), and filtering using `select()` with `.where()` -- all through SQLAlchemy 2.0, no raw SQL
- The `transfer_budget()` function creates paired expense records (negative debit, positive credit) atomically

### Common Mistakes

- Running the application without a `.env` file containing `DATABASE_URL` -- the app raises ValueError immediately
- Not calling `Base.metadata.create_all(engine)` before operations -- tables must exist before you can write to them
- Forgetting that `session.flush()` gets IDs without committing, needed when creating related records in the same session

### Connections

- **Builds on**: Every lesson in Chapter 9 (L0 through L7) -- each function maps directly to a lesson
- **Leads to**: The chapter quiz (Lesson 9) for assessing mastery, then future chapters where you add web interfaces and version control on top of this database foundation
