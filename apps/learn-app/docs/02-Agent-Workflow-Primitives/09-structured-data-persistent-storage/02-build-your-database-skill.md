---
sidebar_position: 2
title: "Build Your Database Skill"
chapter: 9
lesson: 1
duration_minutes: 20
description: "Create a reusable `/database-deployment` skill, but start by proving persistence in under 5 minutes"
keywords: ["skill ownership", "SQLAlchemy patterns", "Neon", "persistence proof", "reusable workflow"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Skill Ownership"
    proficiency_level: "A1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Learning Strategy"
    measurable_at_this_level: "Student can explain why reusable patterns beat one-off memory"

  - name: "Pattern Capture"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can capture model/CRUD/transaction/deployment patterns in SKILL.md"

learning_objectives:
  - objective: "Prove data persistence across script restarts"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Student runs write/read split scripts and confirms data survives process boundary"

  - objective: "Create `/database-deployment` skill scaffold"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates structured skill file with focused sections and initial decision logic"

  - objective: "Understand how this skill compounds across lessons"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Student can state what each next lesson adds to the skill"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (persistence proof, skill scaffold, pattern accumulation), intentionally lightweight for fast momentum"

---

# Build Your Database Skill

> **Chapter 8 callback:** You already know how to compute correctly. This lesson proves the new promise: your data can survive restarts and become queryable infrastructure.

## Failure Hook

A Chapter 8 script that computes correctly but forgets everything after exit is still fragile for real applications.

Before building any skill structure, we prove one thing fast: **data survives process boundaries**.

## Minimal Working Win (Do This First)

Create two scripts.

### `write_once.py`

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

engine = create_engine("sqlite:///quick_persist.db")
Base = declarative_base()

class Marker(Base):
    __tablename__ = "markers"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

Base.metadata.create_all(engine)

with Session(engine) as session:
    session.add(Marker(name="persistent-check"))
    session.commit()

print("Wrote marker")
```

### `read_later.py`

```python
from sqlalchemy import create_engine, select, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session

engine = create_engine("sqlite:///quick_persist.db")
Base = declarative_base()

class Marker(Base):
    __tablename__ = "markers"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

with Session(engine) as session:
    rows = session.execute(select(Marker)).scalars().all()
    print([r.name for r in rows])
```

Run:

```bash
python write_once.py
python read_later.py
```

If second script prints `['persistent-check']`, you just crossed from "compute and forget" to "persist and query." That is the point of Chapter 9.

## Why Skill-First Still Matters

Now that value is proven, we capture patterns so you do not relearn them next month.

A skill is not notes. It is an execution interface for future projects.

- Notes describe what you learned.
- Skill tells you what to do, in what order, with what guardrails.

## Skill Scaffold (Lean Version)

Create:

```bash
mkdir -p database-deployment/references
mkdir -p database-deployment/examples
```

Create `database-deployment/SKILL.md`:

```markdown
---
name: database-deployment
description: Build persistent data layers with SQLAlchemy + PostgreSQL (Neon).
---

# Database Deployment

## Persona
I build systems where data must remain correct across restarts, users, and failures.

## When to Use
- Structured data with relationships
- Multi-user persistence
- Query-heavy workflows
- Integrity-sensitive writes

## Core Patterns
1. Models as code
2. Session-based CRUD
3. Relationships + joins
4. Transactions + rollback
5. Neon deployment + pooling
6. Optional hybrid verification for high-stakes outputs

## Decision Logic
- One-off local script -> stay Chapter 8 style
- Persistent multi-user app -> Chapter 9 style
- High-stakes report -> Chapter 9 + hybrid verification

## Guardrails
- Never hardcode DB credentials
- Never skip rollback path on write failures
- Never claim "production-ready" without verification checks
```

This is intentionally short. You will enrich it each lesson.

## Pull Patterns From Reference Skill

Use the existing reference skill as source material, not as a copy-paste substitute:

```bash
cat .claude/skills/building-with-sqlalchemy-orm/SKILL.md
```

Focus on:

- model definitions
- session patterns
- transaction safety
- connection reliability

## What Breaks Next

You now have a scaffold and a persistence proof.

Next lesson is the first real schema decision point: if your model design is sloppy, every later query and transaction inherits that weakness.

## Try With AI

### Prompt 1 — Prove

**Goal:** Force a persistence proof, not just belief.

```text
I want a minimal two-script proof that data persists across process restarts.
Script A writes one row. Script B reads it in a separate run.
Use SQLAlchemy with sqlite:/// file storage, not in-memory mode.
Explain why this test proves persistence.
```

### Prompt 2 — Design

**Goal:** Create a lean, reusable skill skeleton.

```text
Draft a concise SKILL.md for /database-deployment with exactly these sections:
Persona, When to Use, Core Patterns, Decision Logic, Guardrails.
Keep each section short and operational.
```

### Prompt 3 — Debug

**Goal:** Anticipate first-class failure modes.

```text
I have a database skill scaffold but no details yet.
List the top 5 mistakes beginners make in early SQLAlchemy + Neon projects,
and for each give one preventive rule I should add to Guardrails.
```

### Before You Continue

- [ ] I ran a write/read split test and verified persistence.
- [ ] I created `/database-deployment/SKILL.md`.
- [ ] My skill has decision logic, not only concepts.
- [ ] My guardrails include secrets + rollback discipline.
