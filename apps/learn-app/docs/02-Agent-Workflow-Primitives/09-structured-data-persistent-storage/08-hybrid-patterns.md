---
sidebar_position: 8
title: "Hybrid Patterns — When Tools Work Together"
chapter: 9
lesson: 7
duration_minutes: 30
description: "Discover how combining SQL queries with bash verification creates self-checking data pipelines, and synthesize the Part 2 tool choice story"
keywords: ["hybrid patterns", "SQL verification", "bash", "tool selection", "self-checking", "data pipelines", "Budget Tracker", "Braintrust"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Hybrid Query Pattern"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can implement a query-then-verify workflow combining SQL and bash for structured data tasks"

  - name: "Tool Selection Reasoning"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can analyze a data task and select the appropriate tool (bash, Python, SQL, or hybrid) with justification"

  - name: "Verification Strategy Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can design a verification step that cross-checks query results using an independent method"

learning_objectives:
  - objective: "Implement a hybrid query-then-verify pattern using SQLAlchemy and bash"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student writes a SQLAlchemy query and a bash command that independently confirm the same result"

  - objective: "Analyze a data task and justify which tool or combination of tools to use"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student evaluates three scenarios and selects tool with written reasoning"

  - objective: "Evaluate the cost-benefit tradeoff of hybrid verification versus single-tool approaches"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student explains when hybrid verification is worth the extra tokens and when it is not"

cognitive_load:
  new_concepts: 3
  assessment: "3 new concepts (hybrid verification pattern, tool selection framework, cost-benefit reasoning for verification). All build on previously mastered SQL, Python, and bash skills from the File Processing, Computation, and earlier lessons in this chapter."

differentiation:
  extension_for_advanced: "Design a three-tool verification chain (SQL query, Python analysis, bash file check) for a production audit trail"
  remedial_for_struggling: "Focus on the tool selection table only; skip the code implementation and use the Try With AI prompts for guided practice"
---
# Hybrid Patterns — When Tools Work Together

Through L0-L6, you've learned every piece of the database puzzle: models, CRUD operations, relationships, transactions, and cloud deployment with Neon. In the Braintrust benchmark introduced earlier, SQL was the strongest single-tool approach for structured queries.

The follow-up result is the key tension in this lesson: a hybrid approach (SQL primary query + bash independent verification) matched top accuracy while adding a self-checking path.

This lesson shows when that extra verification cost is worth paying.

## The Experiment Recap

Here is the initial benchmark snapshot Braintrust reported:

| Approach | Accuracy | Tokens Used | Time | Cost |
|----------|----------|-------------|------|------|
| SQL queries | 100% | 155K | 45s | $0.51 |
| Bash (grep/awk) | 52.7% | 1.06M | 401s | $3.34 |
| Hybrid (SQL + bash) | 100% | 310K | ~150s | Higher than pure SQL |

The hybrid agent used SQL as the primary query engine and bash to spot-check results. It spent roughly twice the tokens of pure SQL, trading cost for an independent verification path.

Why did the bash agent fail half the time? The researchers identified the root cause: "it didn't know the structure of the JSON files." Your SQLAlchemy models solve this — the `Expense` model with its `user_id`, `category_id`, `amount`, and `date` columns gives any query engine structural certainty that `grep` never has.

## Why Hybrid Matters for Agents

A single query path creates a single point of failure. If the query has a subtle bug (wrong filter, missing join, timezone mismatch), the answer can look correct but be wrong.

Hybrid adds independent verification: compute one way, verify another way. This is Principle 3 applied to structured data.

## The Hybrid Pattern in Practice

Here is how you apply the hybrid pattern to your Budget Tracker. Suppose you need to answer: "How much did Alice spend on Food in January 2024?"

### Step 1: SQL Query (Primary)

Use SQLAlchemy to get the structured answer:

```python
from sqlalchemy.orm import Session
from sqlalchemy import func, select
from datetime import date

def get_food_spending_sql(engine, user_id, year, month):
    """Primary query: SQLAlchemy with joins and aggregation."""
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    current_month = date(year, month, 1)

    with Session(engine) as session:
        result = session.execute(
            select(func.sum(Expense.amount))
            .join(Category)
            .where(
                Expense.user_id == user_id,
                Category.name == "Food",
                Expense.date >= current_month,
                Expense.date < next_month
            )
        ).scalar()

        return float(result or 0)

sql_total = get_food_spending_sql(engine, user_id=1, year=2024, month=1)
print(f"SQL result: ${sql_total:.2f}")
```

**Output:**

```
SQL result: $117.00
```

### Step 2: Bash Verification (Independent Check)

Export the raw data and use bash to compute the same answer independently:

```python
import subprocess
import csv

def verify_with_bash(engine, user_id, category_name, year, month):
    """Independent verification: export to CSV, grep, sum with awk."""
    # Export expenses to CSV
    with Session(engine) as session:
        expenses = session.execute(
            select(Expense.amount, Category.name.label("category"), Expense.date)
            .join(Category)
            .where(Expense.user_id == user_id)
        ).all()

    csv_path = "/tmp/expenses_verify.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["amount", "category", "date"])
        for amount, cat, d in expenses:
            writer.writerow([amount, cat, d.isoformat()])

    # Use bash to filter and sum independently
    # Note: In production, never interpolate user input into shell commands.
    # Use shlex.quote() or argument lists to prevent command injection.
    import shlex
    cmd = (
        f"grep {shlex.quote(category_name)} {shlex.quote(csv_path)} | "
        f"grep {shlex.quote(f'{year}-{month:02d}')} | "
        f"awk -F',' '{{sum += $1}} END {{printf \"%.2f\", sum}}'"
    )
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return float(result.stdout or 0)

bash_total = verify_with_bash(engine, 1, "Food", 2024, 1)
print(f"Bash result: ${bash_total:.2f}")
```

**Output:**

```
Bash result: $117.00
```

### Step 3: Compare Results

```python
def hybrid_query(engine, user_id, category_name, year, month):
    """Hybrid: query with SQL, verify with bash."""
    sql_result = get_food_spending_sql(engine, user_id, year, month)
    bash_result = verify_with_bash(engine, user_id, category_name, year, month)

    if abs(sql_result - bash_result) < 0.01:
        print(f"VERIFIED: ${sql_result:.2f} (both methods agree)")
        return sql_result
    else:
        print(f"MISMATCH: SQL=${sql_result:.2f}, Bash=${bash_result:.2f}")
        print("Investigate before trusting either result.")
        return None

hybrid_query(engine, 1, "Food", 2024, 1)
```

**Output:**

```
VERIFIED: $117.00 (both methods agree)
```

### When to Use This Pattern

The hybrid pattern costs roughly 2x the tokens. Use it when:

| Scenario | Use Hybrid? | Why |
|----------|-------------|-----|
| Financial reporting | Yes | Errors have real monetary consequences |
| Audit trails | Yes | Regulators require independent verification |
| Agent pipelines | Yes | Agents cannot ask humans to double-check |
| Quick data exploration | No | Speed matters more than certainty |
| Development/debugging | No | You are already inspecting results manually |
| One-off queries | No | The cost of verification exceeds the cost of error |

Decision rule: if a wrong answer is costly (money, compliance, or downstream automation), pay for verification.

## The Tool Choice Framework

Looking back across Part 2, each tool excels at specific tasks:

| Tool | Best For | Accuracy | Cost | Learned In |
|------|----------|----------|------|------------|
| **Bash** | File exploration, text search, quick verification | Moderate (52.7% for structured queries) | High for structured-query workloads (1.06M tokens in benchmark) | File Processing |
| **Python** | Computation, data transformation, decimal arithmetic | High (deterministic) | Low (local) | Computation & Data Extraction |
| **SQL (SQLAlchemy)** | Structured queries, persistent storage, relationships | High (100% with schema) | Low (155K tokens) | This chapter |
| **Hybrid** | Production reliability, self-verification, audit trails | Highest (100% + cross-check) | Medium (310K tokens) | This lesson |

The goal is not one tool. It's correct tool choice, and sometimes two tools for one answer.

## What Comes Next

The capstone removes scaffolding. You will need this exact judgment under pressure: which tool to run first, and when to verify with a second path before trusting output.

## Try With AI

### Prompt 1: Implement a Hybrid Verification

```
I have a Budget Tracker with SQLAlchemy models (User, Category, Expense)
connected to Neon PostgreSQL.

Write a hybrid verification function that:
1. Uses SQLAlchemy to query all Food expenses over $20 for user_id=1
2. Exports those same expenses to a CSV file
3. Uses a bash command (via subprocess) to grep the CSV and count matching rows
4. Compares the SQLAlchemy count with the bash count
5. Prints VERIFIED if they match, MISMATCH if they differ

Use the Budget Tracker models from this chapter (Expense has user_id,
category_id, amount, date; Category has name).
```

**What you're learning:** Design two independent paths to the same result.

### Prompt 2: Tool Selection Reasoning

```
For each scenario below, tell me which tool (bash, Python, SQL, or hybrid)
you would use and why. Consider accuracy, cost, and speed.

1. Counting how many .py files exist in a project directory
2. Calculating compound interest over 30 years with monthly payments
3. Finding all users who spent more than $500 last month across categories
4. Generating a financial report for an auditor that must be provably correct
5. Searching a log file for error messages from the last hour

For each answer, explain what would go WRONG if you picked a different tool.
```

**What you're learning:** Match tool strengths to task requirements by reasoning about failure modes.

### Prompt 3: Explain the Bash Agent's Failure

```
The Braintrust experiment tested bash/grep against SQL for querying 68,000
GitHub issues. The bash agent generated sophisticated shell commands — find,
grep, jq, awk chains — but only achieved 52.7% accuracy compared to SQL's
100%.

Explain to me:
1. Why did sophisticated bash commands still fail half the time?
2. What does "schema clarity" mean and why does it matter?
3. How do SQLAlchemy models provide schema clarity that grep cannot?
4. Give me a concrete example where grep would return wrong results
   because it doesn't understand data structure.
```

**What you're learning:** Root-cause reasoning about tool limits (schema awareness vs text matching).

## Checkpoint

Before moving to the capstone, verify:

- [ ] I can explain what the hybrid pattern is and when to use it
- [ ] I can describe why the bash agent scored 52.7% (schema awareness)
- [ ] I can select the right tool for a given data task with justification
- [ ] I understand the cost-benefit tradeoff of hybrid verification
- [ ] I can trace the Part 2 tool choice story: bash (File Processing) to Python (Computation) to SQL (this chapter) to hybrid (this lesson)

Ready for L8: the capstone where you put everything together into a complete Budget Tracker application.
