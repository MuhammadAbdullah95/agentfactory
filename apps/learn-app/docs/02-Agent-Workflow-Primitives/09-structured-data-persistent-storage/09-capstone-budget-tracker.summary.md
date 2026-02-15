### Core Concept

The capstone integrates every pattern from the chapter -- models, CRUD, relationships, transactions, and Neon deployment -- into a single working Budget Tracker application. No new concepts are introduced; this lesson proves that all the pieces work together as a production-ready system.

### Continuity Bridge

- From Chapter 7: operations and diagnostics become reusable runbook habits.
- From Chapter 8: deterministic computation and parser correctness remain non-negotiable.
- Now in Chapter 9: persistence, transactional safety, and verification policy are integrated in one release-ready path.

### Key Mental Models

- **Integration over accumulation**: Knowing individual patterns (models, sessions, transactions) is not the same as combining them into a working application. The capstone forces you to see how models feed into CRUD, which depends on relationships, which is protected by transactions, which runs on Neon.
- **Continuity bridge in action**: Chapter 7 gave operational bash control, Chapter 8 gave verified computation, and Chapter 9 fuses both into persistent relational systems with explicit release gates.
- **Reusable skill as career asset**: The `/database-deployment` skill you have been building is not specific to Budget Tracker. The same models/sessions/relationships/transactions/pooling patterns apply to any project needing persistent, queryable, relational data.

### Critical Patterns

- Application structure: imports and engine setup, model definitions, CRUD functions (create/read/update/delete), relationship queries (monthly summary), atomic transactions (budget transfers), utilities (init/test connection)
- Explicit CRUD evidence matrix: each operation has a proof artifact (create id, read result, update diff, delete absence, rollback drill)
- Every CRUD function follows the same shape: `with Session(engine) as session: try: ... session.commit() except: ... return error`
- Complex queries combine joins, aggregation (`func.sum`, `func.count`), grouping (`group_by`), and filtering using `select()` with `.where()` -- all through SQLAlchemy 2.0
- High-stakes verification is `Decimal`-first with explicit tolerance (`Decimal("0.01")`)
- The `transfer_budget()` function creates paired expense records (negative debit, positive credit) atomically

### Common Mistakes

- Running the application without a `.env` file containing `DATABASE_URL` -- the app raises ValueError immediately
- Not calling `Base.metadata.create_all(engine)` before operations -- tables must exist before you can write to them
- Using `float` in financial verification logic instead of `Decimal`
- Marking release-ready without evidence bundle outputs (CRUD, rollback, connectivity, verification policy)

### Connections

- **Builds on**: Chapter 7 (operations), Chapter 8 (verified computation), and every Chapter 9 lesson L0-L7
- **Leads to**: The chapter quiz (Lesson 9) for assessing mastery, then future chapters where you add web interfaces and version control on top of this database foundation
