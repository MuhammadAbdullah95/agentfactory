### Core Concept

Atomicity means all operations in a transaction succeed together or fail together -- no partial changes. For any multi-step database operation (like transferring budget between categories), you wrap everything in try/except with commit on success and rollback on failure.

### Continuity Bridge

- From Chapter 7: mistakes could be mitigated with backups.
- From Chapter 8: failures often meant rerunning scripts.
- Now in Chapter 9: failed multi-step writes can corrupt persistent state without rollback discipline.

### Key Mental Models

- **All-or-nothing guarantee**: A budget transfer has two steps: debit one category, credit another. Without atomicity, a crash between steps leaves money missing. With atomicity, both happen or neither does -- the database never shows an inconsistent state.
- **Try/except as non-negotiable**: Every database write operation should be wrapped in try/except. Commit failures can happen for many reasons (foreign key violations, constraint errors, network drops). Without rollback, the session is left in a broken state.

### Critical Patterns

- Basic transaction pattern: `try: ... session.commit()` / `except: session.rollback()`
- Single create with error handling: add object, commit, catch exceptions, rollback on failure
- Read-modify-write: query existing record, modify attributes, commit the change
- Multi-step atomic operation: create paired records (debit + credit), commit both in one transaction
- Bulk operations: delete or update multiple records atomically
- Savepoints for batch processing: `session.begin_nested()` to roll back individual items without aborting the entire batch

### Common Mistakes

- Skipping try/except because "it's just one operation" -- even single operations can fail (duplicate key, invalid foreign key)
- Calling `session.commit()` without a rollback path -- if commit raises an exception, the session is corrupted
- Confusing transaction safety with input validation -- transactions prevent partial writes, but they commit wrong values if your logic is wrong

### Connections

- **Builds on**: CRUD operations (Lesson 3) and relationships (Lesson 4) -- transactions protect multi-table operations
- **Leads to**: Cloud deployment with Neon (Lesson 6) where transactions become even more critical with network latency and concurrent users
