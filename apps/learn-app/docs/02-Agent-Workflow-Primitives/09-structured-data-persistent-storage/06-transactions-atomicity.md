---
sidebar_position: 6
title: "Transactions & Atomicity"
chapter: 9
lesson: 5
duration_minutes: 30
description: "Ensure all-or-nothing database operations with transactions and proper error recovery"
keywords: ["SQLAlchemy", "transaction", "atomicity", "commit", "rollback", "try-except", "session management", "error handling"]
---
# Transactions & Atomicity

> **Continuity bridge**
> - From Chapter 7: file operations were reversible through backups.
> - From Chapter 8: script failures mostly meant reruns.
> - Now in Chapter 9: failed writes can corrupt long-lived state unless guarded by transactions.

**Principle anchor:** P6 (Constraints and Safety). Transaction boundaries are your safety boundary for multi-step writes.

In L4, you connected tables. Now the risk shifts: not "can we query data?" but "can we keep data correct when things fail?"

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
from sqlalchemy import select
from sqlalchemy.orm import Session

with Session(engine) as session:
    try:
        # Step 1: First operation
        alice = session.execute(
            select(User).where(User.name == 'Alice')
        ).scalars().first()
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
session.commit()  # Exception here leaves current transaction failed unless rolled back
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
from sqlalchemy import select
from sqlalchemy.orm import Session

def transfer_budget(user_id, from_category_id, to_category_id, amount):
    """
    Transfer budget between categories.
    Creates two expense records atomically - both or none.
    """
    with Session(engine) as session:
        try:
            # Verify both categories exist
            from_cat = session.execute(
                select(Category).where(Category.id == from_category_id)
            ).scalars().first()
            to_cat = session.execute(
                select(Category).where(Category.id == to_category_id)
            ).scalars().first()

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
from sqlalchemy import select
from sqlalchemy.orm import Session

def update_expense_amount(expense_id, new_amount):
    """Update expense amount safely."""
    with Session(engine) as session:
        try:
            expense = session.execute(
                select(Expense).where(Expense.id == expense_id)
            ).scalars().first()

            if not expense:
                raise ValueError(f"Expense {expense_id} not found")

            expense.amount = new_amount
            session.commit()
            return {"success": True}

        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}
```

## Working With AI on Safety Patterns

Use AI to draft the transaction, then force edge-case hardening. Example:

```python
from sqlalchemy import select, update, delete, func
from sqlalchemy.orm import Session

def merge_categories(user_id, from_cat_id, to_cat_id):
    with Session(engine) as session:
        try:
            if from_cat_id == to_cat_id:
                raise ValueError("Source and target categories must differ")

            to_cat = session.execute(
                select(Category).where(Category.id == to_cat_id)
            ).scalars().first()
            if not to_cat:
                raise ValueError(f"Target category {to_cat_id} not found")

            moved_count = session.execute(
                update(Expense).where(
                    (Expense.user_id == user_id) &
                    (Expense.category_id == from_cat_id)
                ).values(category_id=to_cat_id)
            ).rowcount

            remaining = session.execute(
                select(func.count()).select_from(Expense).where(
                    Expense.category_id == from_cat_id
                )
            ).scalar_one()

            if remaining == 0:
                session.execute(delete(Category).where(Category.id == from_cat_id))

            session.commit()
            return {"success": True, "moved_count": moved_count}
        except Exception as e:
            session.rollback()
            return {"success": False, "error": str(e)}
```

The pattern: AI accelerates the first draft; you enforce invariants before commit.

## Optional Extension: Savepoints

For partial-failure batch workflows, `session.begin_nested()` can isolate one item without aborting the full batch.

## What Comes Next

You can now prevent partial writes. Next challenge: durable cloud operation, where connection lifecycle and credential discipline decide whether your reliable code survives production conditions.

Next lesson: a correct transaction strategy still fails in production if connection and secret handling are sloppy.

## Try With AI

### Prompt 1: Classify Atomicity Requirements

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

### Prompt 2: Implement Safe Code

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
- Use SQLAlchemy 2.0 style: session.execute(select(...)), session.execute(update(...)), etc.
- Don't delete the from_cat (other users might use it)

Use the Budget Tracker models (User, Category, Expense).
Import from sqlalchemy: select, update, func as needed.
```

### Prompt 3: Prove Rollback

```
Write a transfer_budget function that deliberately fails halfway through.
Specifically:
1. Create the first expense (debit from Food category) — this should succeed
2. Then raise an exception BEFORE creating the second expense (credit to Entertainment)
3. After the exception, query the database to prove the first expense was NOT saved

Show me the code and the output that proves rollback worked.
Then modify the code to REMOVE the try/except block and show what happens
when the same failure occurs without rollback protection.
```

After each prompt, verify one concrete thing:
- Prompt 1: Did you correctly classify which scenarios require atomicity?
- Prompt 2: Does your function rollback cleanly if `to_cat` does not exist?
- Prompt 3: Can you prove the difference between rollback safety and partial corruption by running both versions?

**Safety reminder:** Transactions prevent data corruption, but they don't prevent logical errors. If your code transfers $100 when it should transfer $10, the transaction will happily commit the wrong amount. Always validate inputs before starting the transaction.

### Checkpoint

Before moving to L6:

- [ ] You understand: Atomicity = all-or-nothing operations
- [ ] You know: Why try/except + rollback are critical for data integrity
- [ ] You can implement: Safe multi-step operations that commit or rollback together
- [ ] You can identify: Which scenarios require atomic transactions (Prompt 1)
- [ ] You've written: Transaction-safe code (Prompt 2)
- [ ] You've proven: Rollback works by deliberately failing a transaction (Prompt 3)
- [ ] You can observe failure paths clearly (exception + rollback + post-check query) instead of guessing

Ready for L6: Neon-specific features and connection reliability.
