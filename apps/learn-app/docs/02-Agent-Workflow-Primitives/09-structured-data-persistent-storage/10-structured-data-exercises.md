---
title: "Structured Data Practice Exercises"
sidebar_position: 10
chapter: 9
lesson: 9
duration_minutes: 120

primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Apply Chapter 9 patterns through build/debug modules"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Model-Build-Debug Discipline"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student can build and debug relational apps under realistic constraints"

  - name: "Operational Verification"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Quality Assurance"
    measurable_at_this_level: "Student can prove correctness using evidence paths, not assumptions"

learning_objectives:
  - objective: "Build chapter-consistent solutions from requirements"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Build exercises produce working artifacts with verifiable outputs"

  - objective: "Debug production-like failures across schema, CRUD, relationships, transactions, and ops"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Debug exercises identify root cause and implement robust fix"

---

# Structured Data Practice Exercises

These exercises are intentionally harder than lessons.

Every exercise follows one rule:

- **Claim nothing. Prove everything.**

## How to Use

1. Open exercise folder.
2. Read `INSTRUCTIONS.md`.
3. Implement or debug.
4. Collect evidence from tests, schema, and outputs.
5. Write a short postmortem before moving on.

## Database Development Framework (Use Every Time)

1. **Model**: types, constraints, relationships.
2. **Connect**: SQLite first, Neon when required.
3. **Operate**: CRUD with context-managed sessions.
4. **Protect**: atomic writes and rollback paths.
5. **Verify**: queries/tests/trace evidence.
6. **Deploy**: secrets, pooling, connection checks.

## Assessment Rubric (Quick)

| Criterion | 1 (Weak) | 2 (Developing) | 3 (Strong) | 4 (Excellent) |
|---|---|---|---|---|
| Modeling | wrong types/constraints | mostly correct | correct + relationally sound | includes performance/safety refinements |
| Write safety | no rollback discipline | partial | robust transaction handling | robust + failure-path tests |
| Debug quality | symptom-only | fixes issue | fixes root cause | adds prevention + regression check |
| Evidence | no proof | partial proof | clear proof trail | reproducible proof bundle |

---

## Module 1: Data Modeling

### Exercise 1.1 — Library Catalog (Build)

- **Objective:** Translate ambiguous requirements into robust schema.
- **Failure mode to avoid:** encoding relationships as free text and losing queryability.
- **Evidence path:** `expected-queries.txt` + schema inspection + sample inserts.

Deliver:
- models for Book/Member/Loan
- constraints (required fields, uniqueness)
- relationship design justified in `DECISIONS.md`

### Exercise 1.2 — Broken Pet Store (Debug)

- **Objective:** Repair six schema defects without introducing regressions.
- **Failure mode to avoid:** fixing crash bugs while leaving silent data corruption bugs.
- **Evidence path:** `test_models.py` failures -> fixed tests -> before/after schema diff.

Deliver:
- corrected `models.py`
- bug-by-bug root cause notes in `FIXLOG.md`

---

## Module 2: CRUD Operations

### Exercise 2.1 — Recipe Book (Build)

- **Objective:** Implement reliable CRUD against imported CSV data.
- **Failure mode to avoid:** writes that "succeed" but persist incorrect values.
- **Evidence path:** `verify-operations.py` + manual spot checks.

Deliver:
- import + 6 CRUD functions
- read/update/delete verification outputs

### Exercise 2.2 — Broken Task Manager (Debug)

- **Objective:** Diagnose 5 behavioral CRUD bugs.
- **Failure mode to avoid:** patching symptoms instead of operation ordering errors.
- **Evidence path:** failing test -> code trace -> corrected output.

Deliver:
- fixed `task_manager.py`
- short causal analysis per bug

---

## Module 3: Relationships & Navigation

### Exercise 3.1 — Music Library (Build)

- **Objective:** Define bidirectional relationships and query across hops.
- **Failure mode to avoid:** one-sided relationships causing inconsistent navigation.
- **Evidence path:** 8 query outputs vs `expected-results.txt`.

Deliver:
- relationship-complete models
- multi-hop query implementations

### Exercise 3.2 — Broken Blog (Debug)

- **Objective:** Fix relationship config failures (naming, FK types, cascade).
- **Failure mode to avoid:** "empty result" bugs caused by subtle schema mismatch.
- **Evidence path:** `test_blog.py` + relationship introspection + fixed outputs.

Deliver:
- corrected relationships and FK types
- added regression tests for broken cases

---

## Module 4: Transaction Safety

### Exercise 4.1 — Game Inventory Trading (Build)

- **Objective:** Build atomic multi-step trading workflow.
- **Failure mode to avoid:** partial transfer that creates/losses assets.
- **Evidence path:** success/failure scenario replay with before/after state snapshots.

Deliver:
- `trade()` with rollback-safe logic
- scenario proofs in `TRADE-EVIDENCE.md`

### Exercise 4.2 — Broken Bank (Debug)

- **Objective:** Eliminate transaction boundary defects.
- **Failure mode to avoid:** using separate sessions for one logical transfer.
- **Evidence path:** failure simulation + balance invariants hold after fix.

Deliver:
- fixed `bank.py`
- invariant checklist and proof traces

---

## Module 5: Cloud Deployment & Security

### Exercise 5.1 — Contact Book Deploy (Build)

- **Objective:** Deploy existing app to Neon with secure config.
- **Failure mode to avoid:** credentials exposure or stale connection behavior.
- **Evidence path:** `SELECT 1`, CRUD through deployed app, restart persistence check.

Deliver:
- Neon-ready config
- `.env` + `.gitignore` proof
- persistence proof after restart

### Exercise 5.2 — Connection Doctor (Debug)

- **Objective:** Diagnose 5 connection failures quickly and correctly.
- **Failure mode to avoid:** random trial-and-error without ordered diagnostics.
- **Evidence path:** per scenario: error text -> root cause -> fixed run.

Deliver:
- `DIAGNOSIS.md` (error, cause, fix, verification)

---

## Module 6: Hybrid Verification & Tool Selection

### Exercise 6.1 — Expense Audit (Build)

- **Objective:** Build SQL-primary + independent-check audit flow.
- **Failure mode to avoid:** fake hybrid checks that reuse same logic path.
- **Evidence path:** aggregate mismatch detection + record-level discrepancy report.

Deliver:
- audit pipeline
- `AUDIT-REPORT.md` with discrepancy classification

### Exercise 6.2 — Wrong Tool, Wrong Answer (Debug/Analysis)

- **Objective:** Identify wrong-tool choices and implement correct alternatives.
- **Failure mode to avoid:** plausible but wrong outputs accepted without verification.
- **Evidence path:** wrong result vs corrected result side-by-side.

Deliver:
- `TOOL-ANALYSIS.md` with corrected solutions and rationale

---

## Module 7: Capstone Options (Choose 1+)

### Capstone A — Student Grade Portal

- **Objective:** Full-stack relational design + analytics + deployment.
- **Failure mode to avoid:** weak grade logic and unverifiable GPA outputs.
- **Evidence path:** test suite + GPA manual cross-check sample.

### Capstone B — CSV Migration

- **Objective:** Normalize messy legacy dataset with lossless migration.
- **Failure mode to avoid:** silent data loss during cleaning/dedup.
- **Evidence path:** row-count reconciliation + key-field parity checks.

### Capstone C — Disaster Recovery

- **Objective:** Triage and recover broken budget tracker under pressure.
- **Failure mode to avoid:** fixing low-severity issues before integrity/security blockers.
- **Evidence path:** failing tests -> prioritized fix log -> passing regression set.

---

## Outcome Mapping (Exercise -> Chapter Mastery)

| Chapter outcome | Evidence-producing modules |
|---|---|
| Correct models/constraints | 1, 3 |
| Safe CRUD/session handling | 2, 4 |
| Relationship-correct analytics | 3, 7 |
| Transaction integrity | 4, 7 |
| Neon deployment reliability | 5, 7 |
| Hybrid judgment and verification | 6, 7 |

If you can complete one capstone with clear evidence artifacts, you are beyond tutorial competence.
