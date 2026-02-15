### Core Concept

SQLAlchemy relationships let you navigate between connected tables using Python attributes instead of writing JOIN queries. Define `relationship()` on both sides with `back_populates`, and accessing `user.expenses` or `expense.user` works automatically -- SQLAlchemy generates the SQL behind the scenes.

### Continuity Bridge

- From Chapter 7: categories could be inferred from text patterns.
- From Chapter 8: categories could be computed per run.
- Now in Chapter 9: relationships enforce durable links across users, categories, and expenses.

### Key Mental Models

- **Bidirectional navigation**: Relationships work both ways. From a User you can access `user.expenses` (list of Expense objects). From an Expense you can access `expense.user` (the User object). Both sides must declare `relationship()` with matching `back_populates` for this to work.
- **Cascade as cleanup policy**: `cascade="all, delete-orphan"` means deleting a parent (User) automatically deletes all children (their Expenses). Without cascade, deletion is blocked or leaves orphaned records.

### Critical Patterns

- Relationship declaration (parent side): `expenses = relationship("Expense", back_populates="user", cascade="all, delete-orphan")`
- Relationship declaration (child side): `user = relationship("User", back_populates="expenses")`
- Navigation without queries: `user.expenses` returns all expenses for that user
- Explicit join for filtering on related table: `session.execute(select(Expense).join(Category).where(Category.name == 'Food')).scalars().all()`
- Computing with relationships: `sum(expense.amount for expense in user.expenses)`

### Common Mistakes

- Defining relationship on only one side -- both models need `relationship()` with matching `back_populates` for bidirectional access
- Using plural names on the "belongs to" side (`users` instead of `user` on Expense) -- singular for one-to-one direction, plural for one-to-many
- Not understanding cascade implications -- `delete-orphan` deletes ALL children when a parent is removed, which can be dangerous in production

### Connections

- **Builds on**: Foreign keys from Lesson 2 (database-level enforcement) and CRUD from Lesson 3 (now enhanced with relationship navigation)
- **Leads to**: Transactions and atomicity (Lesson 5) -- ensuring multi-step operations across related tables succeed or fail together
