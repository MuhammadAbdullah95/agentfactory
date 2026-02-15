### Core Concept

A session is your conversation with the database. You open it (context manager), make changes or ask questions, and close it. Creating records uses `session.add()` + `session.commit()`; reading uses `select()` + `session.execute()` with filtering, ordering, and limiting.

### Continuity Bridge

- From Chapter 7: operations were file-level and immediate.
- From Chapter 8: outputs were deterministic but ephemeral.
- Now in Chapter 9: session discipline determines whether writes become trustworthy persistent state.

### Key Mental Models

- **Session as phone call**: Open (dial), talk (queries/changes), close (hang up). The `with Session(engine) as session:` pattern handles opening and closing automatically, even if errors occur.
- **Database-side filtering over Python loops**: Always push filtering to the database with `.where()` instead of loading all records and looping in Python. The database returns only matching rows, which is vastly more efficient.

### Critical Patterns

- Engine + table creation: `create_engine('sqlite:///:memory:')` then `Base.metadata.create_all(engine)`
- Single record creation: `session.add(object)` then `session.commit()`
- Batch creation: `session.add_all([list])` then `session.commit()`
- Query all: `session.execute(select(Model)).scalars().all()` returns a list
- Query with filter: `session.execute(select(Model).where(Model.field == value)).scalars().first()` returns one object or None
- Multiple filters (AND): chain multiple `.where()` clauses
- Ordering: `.order_by(Model.field.desc())`
- Limiting: `.limit(N)`

### Common Mistakes

- Forgetting `session.commit()` -- without it, `session.add()` tracks the object but never saves to the database
- Using `.first()` without checking for None -- if no record matches, accessing attributes crashes
- Assuming the `with` block replaces explicit rollback -- after failed commit, call `session.rollback()` before reusing session logic

### Connections

- **Builds on**: Model definitions from Lesson 2 -- now you populate those empty tables
- **Leads to**: Connecting tables with relationships so you can navigate between related data (Lesson 4)
