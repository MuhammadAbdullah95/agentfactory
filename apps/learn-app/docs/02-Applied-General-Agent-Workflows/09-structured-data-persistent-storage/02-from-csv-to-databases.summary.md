### Core Concept

CSV files break down when data has relationships, needs querying, or requires concurrent access. Relational databases solve this by organizing data into connected tables with enforced integrity -- every new question becomes a query, not a new script.

### Key Mental Models

- **Schema clarity**: Databases define structure explicitly (column types, constraints, relationships). Tools that know the schema achieve 100% query accuracy; tools guessing at structure (like bash/grep) achieve ~53%. This is why SQL wins.
- **Foreign keys as enforced connections**: A foreign key is a column that must point to a valid row in another table. The database rejects invalid references automatically -- no orphaned data, no manual checking.

### Critical Patterns

- CSV-to-database mapping: files become tables, headers become typed columns, rows become records with auto-generated IDs
- Foreign key pattern: `expenses.user_id` points to `users.id`, enforcing that every expense belongs to a real user
- Transactions guarantee all-or-nothing: crash between step 1 and step 2 of a money transfer and the database rolls back both

### Common Mistakes

- Thinking databases are "just bigger CSV files" -- the key difference is enforced relationships and queryability, not size
- Confusing foreign keys with just storing a name string (like "Alice") -- IDs are stable references that survive updates
- Assuming you need to write Python loops to answer questions about database data

### Connections

- **Builds on**: File processing (bash for CSV manipulation), computation chapter (Python for data transformation)
- **Leads to**: Defining database tables as Python classes with SQLAlchemy (Lesson 2)
