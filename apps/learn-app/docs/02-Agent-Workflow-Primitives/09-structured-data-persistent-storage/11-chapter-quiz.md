---
sidebar_position: 11
title: "Chapter 09: Structured Data & Persistent Storage Quiz"
proficiency_level: A2
layer: 2
estimated_time: "45 mins"
chapter_type: Technical
running_example_id: structured-data-persistent-storage-quiz-v2
---

# Chapter 09: Structured Data & Persistent Storage Quiz

This assessment checks engineering judgment, not trivia. Choose the option you would trust in production.

## How to Use This Quiz

1. Treat each item as a real implementation decision.
2. Prefer answers that protect integrity, safety, and debuggability.
3. When two options seem possible, choose the one with lower failure cost.

## What This Quiz Measures

- Data modeling quality and constraints
- Session/CRUD correctness
- Relationship and query reasoning
- Transaction safety under failure
- Neon deployment reliability and security
- Tool selection and hybrid verification judgment

## Question-to-Outcome Map

Outcome IDs:
- `O1` Modeling and constraints
- `O2` CRUD and session correctness
- `O3` Relationships and query reasoning
- `O4` Transaction safety
- `O5` Neon operations and security
- `O6` Tool choice, hybrid verification, and release judgment

| Question | Primary outcome |
|---|---|
| Q1 | O6 |
| Q2 | O1 |
| Q3 | O1 |
| Q4 | O2 |
| Q5 | O2 |
| Q6 | O2 |
| Q7 | O3 |
| Q8 | O3 |
| Q9 | O3 |
| Q10 | O4 |
| Q11 | O4 |
| Q12 | O4 |
| Q13 | O5 |
| Q14 | O5 |
| Q15 | O5 |
| Q16 | O5 |
| Q17 | O6 |
| Q18 | O6 |
| Q19 | O6 |
| Q20 | O3 |
| Q21 | O6 |
| Q22 | O6 |
| Q23 | O6 |
| Q24 | O1 |
| Q25 | O6 |
| Q26 | O6 |
| Q27 | O5 |
| Q28 | O4 |
| Q29 | O6 |
| Q30 | O3 |
| Q31 | O6 |

<Quiz
title="Chapter 09: Structured Data & Persistent Storage Assessment (v2)"
questionsPerBatch={10}
questions={[
{
question: "Your app stores expenses in CSV and now needs user-level monthly reporting across 3 years. What is the strongest reason to move to a relational database?",
options: [
"SQL is always faster than Python in every case",
"Relational schema enforces relationships and enables ad-hoc structured queries without rewriting loops",
"CSV cannot store dates or decimals",
"Databases automatically fix bad business logic"
],
correctOption: 1,
explanation: "The key shift is schema + query power + integrity guarantees. You stop re-authoring custom loops for each question.",
source: "Lesson 0"
},
{
question: "Which model choice is safest for money in Expense.amount?",
options: [
"Float, because most tutorials use it",
"String, to avoid numeric conversion errors",
"Numeric(10, 2), because exact decimal semantics are required",
"Integer, then divide by 100 in UI"
],
correctOption: 2,
explanation: "Numeric/Decimal avoids floating-point drift in financial values.",
source: "Lesson 2"
},
{
question: "A teammate removed nullable=False from User.email. What is the most likely production risk?",
options: [
"Database refuses all inserts",
"Users with NULL email can be created, breaking identity assumptions",
"Primary key autoincrement stops working",
"The app cannot connect to Neon"
],
correctOption: 1,
explanation: "Required identity fields should be enforced at schema level, not only app level.",
source: "Lesson 2"
},
{
question: "You call session.add(row) but forget session.commit(). What is the expected outcome?",
options: [
"Row persists because session context auto-commits",
"Row usually does not persist; transaction is not committed",
"SQLAlchemy retries commit automatically",
"Row persists only on Neon"
],
correctOption: 1,
explanation: "Session context closes resources; it does not guarantee persistence without commit for write flow.",
source: "Lesson 3"
},
{
question: "After a failed commit, why is explicit session.rollback() important before reusing that session?",
options: [
"It improves query speed",
"It resets failed transaction state so the session can continue safely",
"It encrypts pending data",
"It is only needed for PostgreSQL, not SQLite"
],
correctOption: 1,
explanation: "Failed transactions leave the session in error state until rollback.",
source: "Lesson 3/5"
},
{
question: "Which query approach is best for 'expenses over $100' from 1M rows?",
options: [
"Load all rows into Python and filter in a for-loop",
"Filter in SQL with where() and fetch only matches",
"Export all rows to CSV then grep",
"Run same query twice and average"
],
correctOption: 1,
explanation: "Push filtering to database execution engine.",
source: "Lesson 3"
},
{
question: "You need User -> Expenses navigation and Expense -> User navigation. What is the correct relationship pattern?",
options: [
"Define relationship() only on User",
"Define relationship() only on Expense",
"Define relationship() on both sides with matching back_populates",
"Use foreign keys only; relationships are unnecessary"
],
correctOption: 2,
explanation: "Bidirectional access requires both relationship endpoints.",
source: "Lesson 4"
},
{
question: "Deleting a parent without cascade and with FK enforcement usually does what?",
options: [
"Silently creates orphans",
"Fails with foreign key constraint error",
"Deletes children anyway",
"Drops both tables"
],
correctOption: 1,
explanation: "With enforced FKs, invalid delete is blocked unless cascade/SET NULL policy allows otherwise.",
source: "Lesson 4"
},
{
question: "Which is the best use of explicit join()?",
options: [
"When you need filtering conditions on related-table fields",
"Only when relationships are broken",
"Never; relationship attributes replace all joins",
"Only for SQLite"
],
correctOption: 0,
explanation: "Join is ideal when query predicate depends on related-table columns.",
source: "Lesson 4"
},
{
question: "A transfer operation debits one category and credits another. What is the must-have property?",
options: [
"Cascade delete",
"Atomicity (all-or-nothing)",
"Read replica",
"Auto-pause"
],
correctOption: 1,
explanation: "Multi-step financial writes must not commit partially.",
source: "Lesson 5"
},
{
question: "Which implementation is safer for multi-step writes?",
options: [
"Two separate sessions, one per step",
"Single session + try/except + commit/rollback",
"Commit after each line to reduce risk",
"No exception handling so failures surface quickly"
],
correctOption: 1,
explanation: "Atomic boundaries require one logical transaction with explicit rollback path.",
source: "Lesson 5"
},
{
question: "A function catches exception but does not rollback, then continues reusing session. Biggest risk?",
options: [
"Minor performance drop only",
"Session remains in failed state and subsequent operations misbehave/fail",
"Only logging is affected",
"It works fine if using context manager"
],
correctOption: 1,
explanation: "Failed transaction state must be reset with rollback.",
source: "Lesson 5"
},
{
question: "Which credential handling is correct for Neon?",
options: [
"Hardcode DATABASE_URL in Python for simplicity",
"Store DATABASE_URL in .env and add .env to .gitignore",
"Commit .env but rotate later",
"Put credentials in README so team can copy"
],
correctOption: 1,
explanation: "Secret management baseline: env vars + ignore files.",
source: "Lesson 6"
},
{
question: "What does pool_pre_ping=True protect against most directly on Neon?",
options: [
"Wrong passwords",
"Stale pooled connections after idle auto-pause/wakeup",
"SQL injection",
"Missing tables"
],
correctOption: 1,
explanation: "Pre-ping detects dead connections before use.",
source: "Lesson 6"
},
{
question: "Error: 'password authentication failed'. First best action?",
options: [
"Reinstall sqlalchemy",
"Reset/verify DB user password and update DATABASE_URL",
"Disable SSL",
"Increase pool_size"
],
correctOption: 1,
explanation: "Credential mismatch is the direct failure mode.",
source: "Lesson 6"
},
{
question: "You hit 'remaining connection slots are reserved'. Best immediate response?",
options: [
"Increase pool_size and max_overflow to absorb spikes quickly",
"Reduce pool footprint and audit session leaks",
"Temporarily reduce app concurrency and add pool diagnostics",
"Upgrade plan tier first, then debug later"
],
correctOption: 1,
explanation: "Fix connection pressure first: right-size pool and close sessions reliably.",
source: "Lesson 6"
},
{
question: "Which statement best describes hybrid verification in this chapter?",
options: [
"Run the same SQL twice and compare",
"Use SQL primary result plus an independent second path when stakes justify it",
"Replace SQL with bash entirely",
"Use hybrid for every query by default"
],
correctOption: 1,
explanation: "Hybrid is selective, risk-based reliability engineering.",
source: "Lesson 7"
},
{
question: "Which check is NOT truly independent?",
options: [
"SQL total + raw ledger recomputation",
"SQL query rerun with same predicates",
"SQL result + separately parsed CSV totals",
"SQL result + independently maintained audit export"
],
correctOption: 1,
explanation: "Same logic path has same failure modes.",
source: "Lesson 7"
},
{
question: "When should mismatch in high-stakes report verification block release?",
options: [
"Only when mismatch exceeds 5% of monthly spend",
"Whenever mismatch exceeds defined tolerance and root cause is unknown",
"Only after two consecutive mismatches",
"Only if both SQL and verification paths fail tests"
],
correctOption: 1,
explanation: "Unknown discrepancy in high-stakes output is a release blocker.",
source: "Lesson 7/8"
},
{
question: "Capstone query quality: which is better for monthly category totals?",
options: [
"Loop categories, run one query per category",
"Single grouped join query with date bounds",
"Export then pivot manually",
"Read all rows then group in frontend"
],
correctOption: 1,
explanation: "Grouped join reduces round-trips and keeps computation near data.",
source: "Lesson 8"
},
{
question: "A teammate says 'production-ready' after successful local run. What is the strongest rebuttal?",
options: [
"Need explicit migration and rollback plan only",
"Need evidence for rollback paths, connection reliability, and report verification policy",
"Need naming and style consistency before release",
"Need benchmark screenshots from local machine"
],
correctOption: 1,
explanation: "Operational readiness requires safety and verification evidence.",
source: "Lesson 8"
},
{
question: "Which sequence best matches Part 2 tool escalation?",
options: [
"SQL -> Bash -> Python",
"Bash -> Python -> SQL -> selective hybrid",
"Python -> SQL -> Bash",
"Hybrid only from the beginning"
],
correctOption: 1,
explanation: "Each tool is added when previous tool hits its boundary.",
source: "README + Lesson 7"
},
{
question: "For one-off local analysis with low consequence, default choice is:",
options: [
"Hybrid verification",
"SQL-only (or Python script depending task shape)",
"Always bash",
"No verification ever"
],
correctOption: 1,
explanation: "Hybrid is not free; use risk-based escalation.",
source: "Lesson 7"
},
{
question: "Which modeling move most reduces downstream query ambiguity?",
options: [
"Store user name directly on every expense",
"Use FK user_id and FK category_id with constraints",
"Keep all data in one text column",
"Use optional IDs and infer later"
],
correctOption: 1,
explanation: "Explicit relational keys enforce unambiguous joins.",
source: "Lesson 2/4"
},
{
question: "What is the safest first step when a report total looks suspicious?",
options: [
"Cross-check against prior month trend first and ship if trend looks normal",
"Enable query observability/logging and inspect generated SQL + predicates",
"Rebuild indexes before checking query semantics",
"Patch schema constraints before isolating query behavior"
],
correctOption: 1,
explanation: "Debug the executed query path before structural rewrites.",
source: "Lesson 4/8"
},
{
question: "Why can Chapter 8-style loops become a liability in Chapter 9 scenarios?",
options: [
"Python cannot handle dates",
"Each new question becomes new code path, increasing bug surface and maintenance cost",
"Loops are disallowed in SQLAlchemy",
"Neon blocks Python loops"
],
correctOption: 1,
explanation: "Ad-hoc loops do not scale as query surface and relationship complexity grow.",
source: "Lesson 0"
},
{
question: "Which fallback is best if foreign-key behavior differs between local SQLite and production Postgres?",
options: [
"Trust Postgres behavior and skip local parity tests",
"Enable SQLite FK checks explicitly and add cross-environment tests",
"Wrap writes in try/except only, without changing local DB config",
"Downgrade FK rules to app-level validation"
],
correctOption: 1,
explanation: "Parity checks prevent false confidence from local-only behavior.",
source: "Lesson 3/6"
},
{
question: "You must choose between shipping today with no transaction tests vs delaying one day to add failure-path tests. Best decision?",
options: [
"Ship now; tests later",
"Delay and add failure-path tests for multi-step writes",
"Skip tests if demo passes",
"Only test reads"
],
correctOption: 1,
explanation: "Data corruption cost usually exceeds short delivery delay.",
source: "Lesson 5"
},
{
question: "Which statement best reflects 'skill ownership' outcome of this chapter?",
options: [
"You memorized SQLAlchemy syntax",
"You can apply a reusable decision framework for persistent relational applications",
"You can only build budget apps",
"You no longer need debugging"
],
correctOption: 1,
explanation: "The durable output is transferable engineering judgment + patterns.",
source: "Lesson 1 + Capstone"
},
{
question: "A monthly summary query is correct but too slow. Best first optimization direction?",
options: [
"Run it more times to warm cache",
"Inspect query shape (joins/grouping/date filters) and add targeted indexes if needed",
"Convert everything to bash",
"Remove constraints"
],
correctOption: 1,
explanation: "Optimize query design first, then indexing strategy.",
source: "Lesson 8"
},
{
question: "Which evidence bundle most credibly supports a 'release-ready' chapter capstone?",
options: [
"One screenshot of successful run",
"Passing happy-path run + deliberate failure rollback proof + Neon connection resilience check + verification policy output",
"Only lint output",
"Only README narrative"
],
correctOption: 1,
explanation: "Release readiness needs multi-angle evidence, especially failure-path evidence.",
source: "Lesson 8"
}
]}
/>

## After You Finish

Use misses as a directed repair list:

- Modeling/relationship misses -> revisit Lessons 2 and 4.
- Session/transaction misses -> revisit Lessons 3 and 5.
- Neon operational misses -> revisit Lesson 6.
- Hybrid/tool-choice misses -> revisit Lesson 7.

A strong score means you can defend your design decisions, not just execute examples.
