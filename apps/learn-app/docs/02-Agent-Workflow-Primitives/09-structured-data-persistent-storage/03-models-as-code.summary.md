### Core Concept

SQLAlchemy's ORM lets you define database tables as Python classes. You write a class with Column definitions, and SQLAlchemy translates it into actual database tables -- no SQL needed. This is Principle 2 (Code as Universal Interface) applied to data storage.

### Continuity Bridge

- From Chapter 7: files were manipulated, not typed.
- From Chapter 8: values were computed, not schema-enforced.
- Now in Chapter 9: model code defines enforceable structure for every downstream query.

### Key Mental Models

- **Python class = database table**: Each class inheriting from Base becomes a table. `__tablename__` sets the table name, each `Column()` becomes a column with a specific type and constraints.
- **Column types as contracts**: `Integer`, `String(100)`, `Numeric(10, 2)`, `DateTime` tell the database (and every tool reading the schema) exactly what data each field holds. This type awareness is what makes queries reliable.

### Critical Patterns

- Base setup: `Base = declarative_base()` then classes inherit from `Base`
- Column type mapping: `int` to `Integer`, `str` to `String(N)`, `decimal` to `Numeric(precision, scale)`, `bool` to `Boolean`, `datetime` to `DateTime`
- Constraints: `primary_key=True` (auto-increment ID), `nullable=False` (required), `unique=True` (no duplicates), `default=value`
- ForeignKey declaration: `Column(Integer, ForeignKey('users.id'), nullable=False)` -- enforces referential integrity at the database level

### Common Mistakes

- Forgetting `nullable=False` on fields that should be required -- by default columns allow NULL
- Using `String` without a length limit for fields that need one (like email addresses)
- Not understanding that ForeignKey prevents orphaned records -- it is a database-enforced rule, not just documentation

### Connections

- **Builds on**: Why databases beat CSV (Lesson 1) -- now you implement the structure you learned about
- **Leads to**: Creating and reading records using sessions (Lesson 3)
