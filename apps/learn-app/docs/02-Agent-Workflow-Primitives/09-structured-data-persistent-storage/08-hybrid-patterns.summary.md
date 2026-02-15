### Core Concept

The hybrid pattern queries data with SQL as the primary tool, then independently verifies the result with bash -- two different tools arriving at the same answer provides confidence that neither introduced a bug. This is Principle 3 (Verification as Core Step) applied to data, and it synthesizes the Part 2 tool choice story.

### Key Mental Models

- **Independent verification over repeated execution**: Running the same query twice proves nothing. Running SQL to query and bash to cross-check proves correctness through independence -- if two unrelated methods agree, the answer is almost certainly right.
- **Tool selection as cost-benefit analysis**: Each tool has specific strengths. Bash excels at file exploration. Python excels at computation. SQL excels at structured queries. Hybrid excels at production reliability. The right choice depends on what happens when you get a wrong answer -- financial loss demands verification; quick exploration does not.
- **Schema clarity as the dividing line**: The Braintrust experiment showed bash achieved 52.7% accuracy vs SQL's 100% on structured data. The root cause: bash treats data as plain text and guesses at structure. SQL knows the schema explicitly. Your SQLAlchemy models provide that schema clarity.

### Critical Patterns

- Query-then-verify workflow: SQLAlchemy `select()` query (primary), export to CSV, bash grep/awk on the CSV (verification), compare results
- Cost-benefit decision: hybrid costs ~2x tokens. Use it for financial reporting, audit trails, and automated agent pipelines. Skip it for development, debugging, and one-off exploration.
- Part 2 tool progression: bash (file ops) to Python (computation) to SQL (structured queries) to hybrid (self-checking pipelines)

### Common Mistakes

- Using hybrid verification for every query -- the extra cost is only justified when wrong answers have real consequences
- Thinking "verification" means running the same query twice -- true verification uses an independent method
- Dismissing bash entirely after learning SQL -- bash remains the best tool for file exploration and quick text searches

### Connections

- **Builds on**: All previous lessons (models, CRUD, relationships, transactions, Neon) plus the File Processing chapter (bash) and Computation chapter (Python)
- **Leads to**: The capstone (Lesson 8) where all patterns integrate into one complete Budget Tracker application
