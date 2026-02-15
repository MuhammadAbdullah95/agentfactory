### Core Concept

The hybrid pattern queries data with SQL as the primary tool, then independently verifies results from raw source data using a separate path (for example, Python `csv.DictReader`). This is Principle 3 (Verification as Core Step) applied to persistent data and finalizes the Part 2 tool-escalation story.

### Continuity Bridge

- From Chapter 7: bash remained useful for file-level exploration.
- From Chapter 8: verification-before-trust became habitual for computation.
- Now in Chapter 9: verification is selectively escalated for high-stakes structured outputs.

### Key Mental Models

- **Independent verification over repeated execution**: Running the same query twice proves little. Running SQL and an independent raw-data recomputation validates through different failure modes.
- **Tool selection as cost-benefit analysis**: Bash excels at file exploration, Python at computation/parsing, SQL at structured queries, and hybrid at high-stakes reliability. Choose based on failure cost.
- **Schema clarity as the dividing line**: The Braintrust experiment showed bash achieved 52.7% accuracy vs SQL's 100% on structured data. The root cause: bash treats data as plain text and guesses at structure. SQL knows the schema explicitly. Your SQLAlchemy models provide that schema clarity.

### Critical Patterns

- Query-then-verify workflow: SQLAlchemy `select()` query (primary), independent CSV recomputation with robust parser, compare using explicit tolerance (`Decimal("0.01")`)
- Cost-benefit decision: hybrid costs ~2x tokens. Use it for financial reporting, audit trails, and automated agent pipelines. Skip it for development, debugging, and one-off exploration.
- Part 2 tool progression: bash (file ops) to Python (computation) to SQL (structured queries) to hybrid (self-checking pipelines)

### Common Mistakes

- Using hybrid verification for every query -- the extra cost is only justified when wrong answers have real consequences
- Thinking "verification" means running the same query twice -- true verification uses an independent method
- Parsing quoted CSV with `awk -F,` or naive string split -- this can silently corrupt verification
- Converting money to float inside verification code -- use `Decimal` end-to-end
- Dismissing bash entirely after learning SQL -- bash remains the best tool for file exploration and quick text searches

### Connections

- **Builds on**: Chapter 7 (bash file operations), Chapter 8 (verified computation), and lessons 1-6 of Chapter 9
- **Leads to**: The capstone (Lesson 8) where all patterns integrate into one complete Budget Tracker application
