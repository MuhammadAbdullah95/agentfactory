---
sidebar_position: 6
title: "Transactions & Atomicity"
chapter: 9
lesson: 5
duration_minutes: 30
description: "Ensure all-or-nothing database operations with transactions and proper error recovery"
keywords: ["SQLAlchemy", "transaction", "atomicity", "commit", "rollback", "try-except", "session management", "error handling"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Atomicity Understanding"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can explain why all-or-nothing operations prevent data corruption"

  - name: "Transaction Implementation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can implement try/except with session.commit() and session.rollback()"

  - name: "Error Recovery Pattern"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can write code that gracefully handles database errors and cleans up"

  - name: "Multi-Step Operation Safety"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Data Management"
    measurable_at_this_level: "Student can identify when transactions are critical (money transfers, linked records)"

  - name: "AI Collaboration for Safety Patterns"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can iterate with AI to identify failure points and implement error handling"

learning_objectives:
  - objective: "Explain atomicity and why all-or-nothing operations matter for data integrity"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student explains what happens to data if a multi-step operation partially fails"

  - objective: "Implement the try/except + rollback pattern for safe database operations"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student writes code that commits on success and rolls back on any error"

  - objective: "Use session.commit() and session.rollback() correctly in transaction workflows"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student demonstrates proper session management in multi-step operations"

  - objective: "Identify when transactions are critical (money transfers, account updates)"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Given scenarios, student correctly identifies which require atomic transactions"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (atomicity definition, session.commit(), session.rollback(), try/except pattern, multi-step transactions, savepoints mention) - appropriate for A2 with prior L4 relationship knowledge"

differentiation:
  extension_for_advanced: "Explore savepoints (nested transactions with begin_nested()), isolation levels, deadlock prevention strategies"
  remedial_for_struggling: "Focus on: What is atomicity? Why try/except matters? Practice single-step transactions before multi-step"
---
# Transactions & Atomicity

In L4, you connected tables with relationships. You can query Alice's expenses, navigate from expenses to categories, and delete records with cascade.

But here's a problem: What if you need to do two things that must succeed together?

Imagine Alice wants to transfer $100 from her Food budget to Entertainment. That's two operations:

1. Debit Food by $100
2. Credit Entertainment by $100

If step 1 succeeds but step 2 fails (server crash, network issue, constraint violation), Alice loses $100. The money left Food but never arrived in Entertainment.

This is the transaction problem. The solution: atomicity.

## What is Atomicity?

**Atomicity** means: Either ALL operations succeed, or NONE of them do.

Think of it like a bank wire transfer. The bank doesn't debit your account and then hope the credit goes through. Both happen as one unit. If anything fails, both are cancelled.

**Without atomicity:**

```
Step 1: Debit Alice's Food: $200 - $100 = $100  [SUCCESS]
Step 2: [Server crashes]
Step 3: Credit Entertainment: Never happens      [FAILED]
Result: Alice lost $100
```

**With atomicity:**

```
Step 1: Start transaction
Step 2: Debit Alice's Food: $200 - $100 = $100
Step 3: Credit Entertainment: $50 + $100 = $150
Step 4: If both succeed: Commit (save both)
Step 5: If ANY fails: Rollback (undo both)
Result: Data always consistent
```

The database guarantees: You'll never see a state where one happened without the other.

## The Basic Transaction Pattern

Here's the pattern you'll use for every multi-step operation:

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    try:
        # Step 1: First operation
        alice = session.query(User).filter(User.name == 'Alice').first()
        alice.food_budget -= 100

        # Step 2: Second operation
        alice.entertainment_budget += 100

        # Step 3: Commit BOTH (only if no exceptions)
        session.commit()
        print("Transfer succeeded")
    except Exception as e:
        # If ANY step fails, undo everything
        session.rollback()
        print(f"Transfer failed: {e}")
```

**Output (success case):**

```
Transfer succeeded
Alice's Food: $100
Alice's Entertainment: $150
```

**Output (failure case):**

```
Transfer failed: insufficient_funds
Alice's Food: $200 (unchanged)
Alice's Entertainment: $50 (unchanged)
```

Let's break down what each part does:

| Part                                 | What It Does                                      |
| ------------------------------------ | ------------------------------------------------- |
| `with Session(engine) as session:` | Opens a session (starts a transaction implicitly) |
| `try:`                             | Groups operations that should succeed together    |
| `session.commit()`                 | Makes all changes permanent (saves to database)   |
| `except Exception as e:`           | Catches any error                                 |
| `session.rollback()`               | Undoes all uncommitted changes                    |

## Why Try/Except is Non-Negotiable

Without try/except, errors leave your session in a broken state:

```python
# BAD: What happens when commit fails?
session.add(expense)
session.commit()  # Exception here = session left open, memory leaks, data inconsistent
```

The commit could fail for many reasons:

- Invalid foreign key (category doesn't exist)
- Constraint violation (duplicate email)
- Connection dropped (network issue)
- Disk full (database can't write)

**Good pattern:**

```python
# GOOD: Always handle errors
try:
    session.add(expense)
    session.commit()
except Exception as e:
    session.rollback()
    raise e  # Re-raise so caller knows it failed
```

**Output (when category doesn't exist):**

```
IntegrityError: FOREIGN KEY constraint failed
Session rolled back - no partial data saved
```

The rollback ensures your database stays consistent even when things go wrong.

## Real Example: Budget Transfer Function

Here's the `transfer_budget` function from the Budget Tracker. This shows atomicity in action:

```python
def transfer_budget(user_id, from_category_id, to_category_id, amount):
    """
    Transfer budget between categories.
    Creates two expense records atomically - both or none.
    """
    with Session(engine) as session:
        try:
            # Verify both categories exist
            from_cat = session.query(Category).filter(
                Category.id == from_category_id
            ).first()
            to_cat = session.query(Category).filter(
                Category.id == to_category_id
            ).first()

            if not from_cat or not to_cat:
                raise ValueError("Category not found")

            # Create BOTH transfer records
            from_expense = Expense(
                user_id=user_id,
                category_id=from_category_id,
                description=f"Transfer to {to_cat.name}",
                amount=-amount  # Negative = debit
            )
            to_expense = Expense(
                user_id=user_id,
                category_id=to_category_id,
                description=f"Transfer from {from_cat.name}",
                amount=amount  # Positive = credit
            )

            session.add(from_expense)
            session.add(to_expense)
            session.commit()  # Both records saved or none

            return {"success": True, "message": f"Transferred ${amount}"}

        except Exception as e:
            session.rollback()  # Both records discarded
            return {"success": False, "error": str(e)}
```

**Output (success):**

```python
result = transfer_budget(user_id=1, from_category_id=1, to_category_id=3, amount=100)
print(result)
# {'success': True, 'message': 'Transferred $100'}

# Database now has:
# - Expense: "Transfer to Entertainment", -$100, category=Food
# - Expense: "Transfer from Food", $100, category=Entertainment
# Both exist. Always.
```

**Output (failure - category not found):**

```python
result = transfer_budget(user_id=1, from_category_id=1, to_category_id=999, amount=100)
print(result)
# {'success': False, 'error': 'Category not found'}

# Database unchanged. Zero expense records created.
# Not one record with no matching pair.
```

This is why atomicity matters: you never have a debit without a matching credit.

## Common Patterns

### Pattern 1: Simple Create (One Operation)

Even single operations benefit from try/except:

```python
def create_expense(user_id, description, amount, category_id):
    """Create one expense with error handling."""
    with Session(engine) as session:
        try:
            expense = Expense(
                user_id=user_id,
                description=description,
                amount=amount,
                category_id=category_id
            )
            session.add(expense)
            session.commit()
            return {"success": True, "id": expense.id}
        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}
```

**Output:**

```python
create_expense(1, "Groceries", 52.50, 1)
# {'success': True, 'id': 5}

create_expense(1, "Test", 10.00, 999)  # Invalid category
# {'success': False, 'error': 'FOREIGN KEY constraint failed'}
```

### Pattern 2: Read-Modify-Write (Update Existing)

When you modify an existing record:

```python
def update_expense_amount(expense_id, new_amount):
    """Update expense amount safely."""
    with Session(engine) as session:
        try:
            expense = session.query(Expense).filter(
                Expense.id == expense_id
            ).first()

            if not expense:
                raise ValueError(f"Expense {expense_id} not found")

            expense.amount = new_amount
            session.commit()
            return {"success": True}

        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}
```

**Output:**

```python
update_expense_amount(1, 75.00)
# {'success': True}
# Expense #1 amount is now $75.00

update_expense_amount(999, 50.00)
# {'success': False, 'error': 'Expense 999 not found'}
# Nothing changed
```

### Pattern 3: Bulk Delete (Multiple Records)

Deleting multiple records should be atomic:

```python
def delete_category_expenses(user_id, category_id):
    """Delete all expenses in a category for a user."""
    with Session(engine) as session:
        try:
            deleted_count = session.query(Expense).filter(
                (Expense.user_id == user_id) &
                (Expense.category_id == category_id)
            ).delete()

            session.commit()
            return {"success": True, "deleted": deleted_count}

        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}
```

**Output:**

```python
delete_category_expenses(1, 1)  # Delete all Food expenses for user 1
# {'success': True, 'deleted': 3}
# All 3 Food expenses deleted in one transaction
```

## Working With AI on Safety Patterns

You understand the business logic. AI helps identify failure points you might miss.

**Your request:**
"I need to merge two categories. Move all expenses from 'Fast Food' to 'Food' and delete the Fast Food category."

**AI suggests:**

```python
def merge_categories(user_id, from_cat_id, to_cat_id):
    with Session(engine) as session:
        try:
            # Update all expenses
            session.query(Expense).filter(
                (Expense.user_id == user_id) &
                (Expense.category_id == from_cat_id)
            ).update({Expense.category_id: to_cat_id})

            # Delete the empty category
            session.query(Category).filter(
                Category.id == from_cat_id
            ).delete()

            session.commit()
            return {"success": True}
        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}
```

**Your refinement:**
"What if the 'to' category doesn't exist? Or someone else has expenses in 'Fast Food'?"

**AI adapts:**

```python
def merge_categories(user_id, from_cat_id, to_cat_id):
    with Session(engine) as session:
        try:
            # Verify target category exists
            to_cat = session.query(Category).filter(
                Category.id == to_cat_id
            ).first()
            if not to_cat:
                raise ValueError(f"Target category {to_cat_id} not found")

            # Only update THIS user's expenses
            updated = session.query(Expense).filter(
                (Expense.user_id == user_id) &
                (Expense.category_id == from_cat_id)
            ).update({Expense.category_id: to_cat_id})

            # Only delete if no other users have expenses there
            remaining = session.query(Expense).filter(
                Expense.category_id == from_cat_id
            ).count()

            if remaining == 0:
                session.query(Category).filter(
                    Category.id == from_cat_id
                ).delete()

            session.commit()
            return {"success": True, "updated": updated}
        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}
```

**What emerged:** A robust solution that handles edge cases neither of you fully anticipated at the start. AI suggested the basic transaction structure; you identified the safety gaps; together you converged on production-quality code.

## Advanced: Savepoints (Brief Mention)

For batch operations where you want to roll back individual items (not the whole batch):

```python
def process_expense_batch(expense_list):
    """Process multiple expenses, rolling back only failed ones."""
    with Session(engine) as session:
        results = []
        for expense_data in expense_list:
            try:
                with session.begin_nested():  # Savepoint
                    expense = Expense(**expense_data)
                    session.add(expense)
                    session.flush()
                    results.append({"id": expense.id, "status": "ok"})
            except Exception as e:
                results.append({"status": "failed", "error": str(e)})

        session.commit()  # Commit all successful ones
        return results
```

**Output:**

```python
batch = [
    {"user_id": 1, "category_id": 1, "description": "A", "amount": 10},
    {"user_id": 1, "category_id": 999, "description": "B", "amount": 20},  # Bad category
    {"user_id": 1, "category_id": 1, "description": "C", "amount": 30},
]
results = process_expense_batch(batch)
# [{'id': 5, 'status': 'ok'},
#  {'status': 'failed', 'error': 'FOREIGN KEY constraint failed'},
#  {'id': 6, 'status': 'ok'}]
# A and C saved. B failed alone. Transaction didn't abort entirely.
```

Savepoints are advanced. For most operations, the basic try/except/rollback pattern is sufficient.

## What Happens Next

You now know how to make database operations safe. Multi-step operations either succeed completely or fail together. No partial data corruption. No dangling references.

But so far, you've been testing locally with SQLite. In-memory databases are great for learning, but they disappear when your script stops. Real applications need persistent databases that run 24/7, handle multiple users, and scale automatically. That's where L6 comes in.

| Lesson | What You Learn                        | What You Add to Your Skill            |
| ------ | ------------------------------------- | ------------------------------------- |
| L5 (now) | Atomic multi-operation safety       | Transaction patterns with error handling |
| L6     | Deploy to Neon serverless database  | Connection pooling and production config |
| L7     | Combine SQL + bash hybrid patterns   | Tool choice framework                    |
| L8     | Integrate all patterns               | Complete, production-ready Budget Tracker |

Transactions ensure correctness locally. Cloud deployment ensures availability globally.

## Try With AI

### Prompt 1: Identify Atomicity Problems

**What you're learning:** Recognizing when operations need atomic transactions.

```
Which of these scenarios NEED atomic transactions?

1. Creating a single expense record
2. Transferring $100 between two budget categories
3. Logging a page view counter
4. Splitting one $150 expense across Food ($100) and Entertainment ($50)
5. Deleting a user and all their expenses
6. Reading a monthly spending summary
7. Moving all "Fast Food" expenses to "Food" category

For each scenario, answer:
- "Needs atomic transaction" or "Doesn't need atomic transaction"
- Why? (What could go wrong without atomicity?)
```

After AI explains, verify: Do you understand why multi-step operations that must succeed together need transactions?

### Prompt 2: Write Safe Code

**What you're learning:** Implementing the transaction pattern yourself.

```
Write a function called merge_categories with these requirements:

def merge_categories(user_id, from_cat_id, to_cat_id):
    """
    Move all expenses from from_cat to to_cat for this user.
    Returns {"success": True/False, "moved_count": N}
    """

Requirements:
- All expense moves must be atomic (all or none)
- Handle case where from_cat doesn't exist
- Handle case where to_cat doesn't exist
- Use try/except + rollback pattern from this lesson
- Don't delete the from_cat (other users might use it)

Use the Budget Tracker models (User, Category, Expense).
```

After AI responds, trace through the error handling. Would this code corrupt data if to_cat doesn't exist?

### Prompt 3: Document in Your Skill

**What you're learning:** Capturing transaction patterns for reuse.

```
Add to my /database-deployment skill:

## Transactions & Atomicity

Include:
1. What atomicity means (all or nothing)
2. When to use transactions (multi-step operations, transfers, cascade deletes)
3. The try/except + rollback pattern (with code template)
4. Real example: transfer_budget function

Format as markdown for SKILL.md. Make it usable for ANY database project, not just Budget Tracker.
```

After AI responds, check: Could you use these patterns in a different project (order processing, inventory management)?

**Safety reminder:** Transactions prevent data corruption, but they don't prevent logical errors. If your code transfers $100 when it should transfer $10, the transaction will happily commit the wrong amount. Always validate inputs before starting the transaction.

### Checkpoint

Before moving to L6:

- [ ] You understand: Atomicity = all-or-nothing operations
- [ ] You know: Why try/except + rollback are critical for data integrity
- [ ] You can implement: Safe multi-step operations that commit or rollback together
- [ ] You can identify: Which scenarios require atomic transactions (Prompt 1)
- [ ] You've written: Transaction-safe code (Prompt 2)
- [ ] You've documented: Transaction patterns in your `/database-deployment` skill

Ready for L6: Neon-specific features and connection reliability.
