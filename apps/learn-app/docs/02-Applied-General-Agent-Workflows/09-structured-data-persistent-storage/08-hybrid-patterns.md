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

Through L0-L6, you've learned every piece of the database puzzle: models, CRUD operations, relationships, transactions, and cloud deployment with Neon. SQLAlchemy handles your structured data with 100% accuracy — as the Braintrust experiment showed in L1.

But the Braintrust researchers found something worth examining more closely. Pure SQL hit 100% accuracy, yes. A hybrid approach that uses SQL for queries AND bash for verification also hit 100% — and it caught edge cases that SQL alone might miss. The hybrid agent naturally developed a self-checking behavior: query the database, then verify the result through an independent path.

This lesson explores that pattern and synthesizes the Part 2 tool choice story.

## The Experiment Recap

Here are the three approaches Braintrust tested:

| Approach | Accuracy | Tokens Used | Time | Cost |
|----------|----------|-------------|------|------|
| SQL queries | 100% | 155K | 45s | $0.51 |
| Bash (grep/awk) | 52.7% | 1.06M | 401s | $3.34 |
| Hybrid (SQL + bash) | 100% | 310K | ~150s | — |

The hybrid agent used SQL as the primary query engine and bash to spot-check results. It spent roughly twice the tokens of pure SQL, but independently verified every answer.

Why did the bash agent fail half the time? The researchers identified the root cause: "it didn't know the structure of the JSON files." Your SQLAlchemy models solve this — the `Expense` model with its `user_id`, `category_id`, `amount`, and `date` columns gives any query engine structural certainty that `grep` never has.

## Why Hybrid Matters for Agents

A single query path creates a single point of failure. If the query logic has a subtle bug — a wrong filter, a missing join, a timezone mismatch — the result looks correct but is not.

The hybrid pattern introduces independent verification: query your data one way, confirm the result a different way. This is Principle 3 (Verification as Core Step) applied to data — the same principle you used in the File Processing chapter (bash output checks), the Computation chapter (Python assertions), and now this chapter (cross-tool verification).

## The Hybrid Pattern in Practice

Here is how you apply the hybrid pattern to your Budget Tracker. Suppose you need to answer: "How much did Alice spend on Food in January 2024?"

### Step 1: SQL Query (Primary)

Use SQLAlchemy to get the structured answer:

```python
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

def get_food_spending_sql(engine, user_id, year, month):
    """Primary query: SQLAlchemy with joins and aggregation."""
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    current_month = date(year, month, 1)

    with Session(engine) as session:
        result = session.query(
            func.sum(Expense.amount)
        ).join(Category).filter(
            Expense.user_id == user_id,
            Category.name == "Food",
            Expense.date >= current_month,
            Expense.date < next_month
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
        expenses = session.query(
            Expense.amount,
            Category.name.label("category"),
            Expense.date
        ).join(Category).filter(
            Expense.user_id == user_id
        ).all()

    csv_path = "/tmp/expenses_verify.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["amount", "category", "date"])
        for amount, cat, d in expenses:
            writer.writerow([amount, cat, d.isoformat()])

    # Use bash to filter and sum independently
    cmd = (
        f"grep '{category_name}' {csv_path} | "
        f"grep '{year}-{month:02d}' | "
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

The decision: what is the cost of a wrong answer? If it causes financial loss or cascading errors in an automated pipeline, the extra tokens are cheap insurance.

## The Tool Choice Framework

Looking back across Part 2, each tool excels at specific tasks:

| Tool | Best For | Accuracy | Cost | Learned In |
|------|----------|----------|------|------------|
| **Bash** | File exploration, text search, quick verification | Moderate (52.7% for structured queries) | Low (tokens) | File Processing |
| **Python** | Computation, data transformation, decimal arithmetic | High (deterministic) | Low (local) | Computation & Data Extraction |
| **SQL (SQLAlchemy)** | Structured queries, persistent storage, relationships | High (100% with schema) | Low (155K tokens) | This chapter |
| **Hybrid** | Production reliability, self-verification, audit trails | Highest (100% + cross-check) | Medium (310K tokens) | This lesson |

The best tool is not one tool. It is knowing which tool for which job — and when the job requires two. In the next chapter, you will add version control (Git) to track changes across all these tools. After that, you will combine everything into your first AI employee.

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

**What you're learning:** Implementing the hybrid verification pattern yourself. The key skill is designing two independent paths to the same answer — if you can only think of one way to verify, you have not verified at all.

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

**What you're learning:** Tool selection is not about preference — it is about matching tool strengths to task requirements. The "what would go wrong" question forces you to think about failure modes, which is how experienced engineers make tool choices.

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

**What you're learning:** The root cause behind tool limitations. Understanding WHY bash fails at structured queries — not just that it does — is what separates someone who follows rules ("always use SQL for databases") from someone who makes informed decisions ("this task needs schema awareness, so I need a schema-aware tool").

## Checkpoint

Before moving to the capstone, verify:

- [ ] I can explain what the hybrid pattern is and when to use it
- [ ] I can describe why the bash agent scored 52.7% (schema awareness)
- [ ] I can select the right tool for a given data task with justification
- [ ] I understand the cost-benefit tradeoff of hybrid verification
- [ ] I can trace the Part 2 tool choice story: bash (File Processing) to Python (Computation) to SQL (this chapter) to hybrid (this lesson)

Ready for L8: the capstone where you put everything together into a complete Budget Tracker application.
