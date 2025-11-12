---
sidebar_position: 4
title: "GEMINI.md Context Files: Specifying Project Context"
duration: "35 min"
skills_taught:
  - skill: "Context Design"
    cefr_level: "A2-B1"
    category: "Technical"
    focus: "Writing context specifications that AI agents understand"
  - skill: "Hierarchy Thinking"
    cefr_level: "B1"
    category: "Technical"
    focus: "Designing multi-level configurations with proper inheritance"
  - skill: "Specification-First Context"
    cefr_level: "B1"
    category: "Technical"
    focus: "Articulating project requirements in context files"
generation_metadata:
  generated_by: "Claude Code"
  source_spec: "022-audit-chapter6-gemini-cli/plan.md - Lesson 4"
  created: "2025-01-12"
  last_modified: "2025-01-12"
  git_author: "Claude Code (lesson-writer agent)"
  workflow: "spec-driven-development"
  version: "1.0.0"
---

# GEMINI.md Context Files: Specifying Project Context

## The Problem: Context as Architecture

Imagine this: You spend 2 hours teaching your AI partner about your project. You explain the architecture, show examples, define your conventions. Then you close Gemini CLI.

Next day, you reopen it and... you start from scratch. You're re-explaining the same things. The AI partner doesn't remember what you taught it yesterday.

**This is not collaboration. It's repetition.**

The real problem isn't memory loss—it's architectural. You haven't specified your project context in a way that persists across sessions. GEMINI.md solves this by **positioning context files as architectural specifications**, not just "helpful files."

When you write a GEMINI.md file, you're doing something important: **you're specifying how you want your AI partner to understand your project.**

---

## Learning Objectives

By the end of this lesson, you'll be able to:

- **Write specifications** for project context architecture using GEMINI.md
- **Design three-level hierarchies** (global/project/subdirectory) that auto-inject context
- **Apply inheritance rules** so context layers combine appropriately
- **Validate** that context injection enables AI to work without re-explanation
- **Collaborate with AI** to architect context specifications for complex projects

---

## Understanding GEMINI.md: A Context Specification Layer

**GEMINI.md** is more than a markdown file. It's your **project context specification**—a formal way of telling Gemini how to understand your work.

**Structure**:
1. **Lives in your project** (at multiple levels: global `~/.gemini/GEMINI.md`, project `./GEMINI.md`, subdirectory `./src/GEMINI.md`)
2. **Gets auto-loaded** when you work in that directory
3. **Specifies context architecture** — what your AI partner needs to know to work effectively
4. **Persists across sessions** — specify once, benefit permanently

Think of GEMINI.md files as **blueprints for how AI understands your project**, not just "context injection" mechanics.

### The Three-Level Hierarchy (Specification Architecture)

GEMINI.md uses a **three-level inheritance model** where context flows from general (global) to specific (subdirectory):

#### Level 1: Global Context (`~/.gemini/GEMINI.md`)

**Specification Purpose**: Define your personal AI interaction standards

**Scope**: Applies to ALL projects

**Content**:
- Your coding language preferences
- Your testing frameworks
- Your personal conventions and style
- Security rules you follow everywhere
- Team/company standards (if applicable)

**Example Specification**:

```markdown
# Global Development Context

## Language & Framework Standards
- Primary: Python 3.13 with type hints (strict)
- Secondary: TypeScript 5.3 with strict mode
- Testing: pytest (Python), Jest (TypeScript)

## Code Style Rules
- Type hints required on all functions
- Docstrings for public APIs (PEP 257)
- Line length: 100 characters (soft), 120 (hard)
- Imports: alphabetical, standard → third-party → local

## Security Standards
- Secrets: Environment variables only, never committed
- API keys: Rotated every 90 days minimum
- Logs: Never include PII or credentials
- Dependencies: Regular security audits

## Testing Standards
- Minimum coverage: 80%
- All public APIs have tests
- Integration tests for critical paths
```

#### Level 2: Project Context (`./GEMINI.md`)

**Specification Purpose**: Define this specific project's architecture and decisions

**Scope**: Applies only to THIS project (when you're in its directory)

**Content**:
- What this project does (product, not code)
- Architecture overview and decisions
- Technology choices and constraints
- Current status (what's done, in progress, planned)
- Project-specific conventions
- Important warnings or gotchas

**Example Specification**:

```markdown
# E-Commerce Backend - Context Specification

## Project Purpose
FastAPI REST API for fashion e-commerce platform. Handles product catalog, orders, payments, inventory management.

## Architecture Decisions

### Monolith Not Microservices (for now)
- Decision: Single FastAPI application
- Rationale: Team is 3 people; simplicity > scalability at this stage
- Trade-off: Deployment is coupled; harder to scale independently later

### PostgreSQL for Persistence
- Decision: Relational database, not NoSQL
- Rationale: Orders have ACID requirements; data consistency critical
- Trade-off: Schema changes require migrations; less flexible

### Stripe for Payments
- Decision: Never handle raw payment data; delegate to Stripe
- Rationale: PCI compliance, security, fraud detection
- Trade-off: Additional vendor dependency; Stripe fees

## Technology Stack
- Framework: FastAPI 0.104+
- Language: Python 3.13
- Database: PostgreSQL 15
- Cache: Redis (session store, rate limiting)
- Testing: pytest + pytest-asyncio
- Deployment: Docker → AWS ECS

## Directory Structure (Important for AI Understanding)
- `src/routes/` — API endpoints (products, orders, payments)
- `src/models/` — Pydantic schemas and ORM (sqlalchemy)
- `src/services/` — Business logic (no HTTP knowledge)
- `src/db/` — Database layer (migrations, queries)
- `src/integrations/` — External APIs (Stripe, email)
- `tests/` — Unit, integration, E2E tests

## Current Status
### ✅ Complete
- Product CRUD, search, filtering
- User authentication (JWT)
- Order creation and history
- Stripe webhook handlers

### 🔄 In Progress
- Email order confirmations
- Inventory tracking

### ⏳ Planned
- Admin dashboard API
- Recommendation engine
- Analytics

## Code Conventions for This Project
- Functions: snake_case, database tables: snake_case
- Classes: PascalCase (Pydantic models, services)
- Constants: UPPER_SNAKE_CASE
- Always validate at route handler BEFORE calling service
- Services should not know about HTTP (no FastAPI imports)

## Critical Constraints
- Free tier Stripe: 10 req/sec limit
- PostgreSQL connection pool: max 10 (shared with batch jobs)
- Redis: 5GB memory limit
- No external HTTP calls during request handlers (use async tasks)
```

#### Level 3: Subdirectory Context (`./src/api/GEMINI.md`)

**Specification Purpose**: Define context for a specific module or subdirectory

**Scope**: Applies only when working in this directory or its files

**Content**:
- Module-specific architecture
- API versioning strategy (if applicable)
- Specific coding patterns used here
- Module-specific constraints
- Interaction with other modules

**Example Specification**:

```markdown
# Payment Routes Module - Context Specification

## Module Purpose
Handle all payment-related HTTP routes. Expose Stripe webhook handlers, payment status checks, refund requests.

## Architecture
- Routes: `/api/v1/payments/*`
- Depends on: `services.payment_service`, `integrations.stripe_client`
- Exposes: Order payment endpoints (POST), webhook receiver (POST), status checks (GET)

## Key Pattern: Stripe Webhooks
All webhook events (payment.success, charge.disputed, etc.) are:
1. Validated with Stripe signature
2. Parsed into domain events
3. Passed to service layer for processing
4. Stored in audit log

## Important: Never Block on Stripe
- All Stripe API calls are async
- Long-running operations use background tasks
- Webhooks respond immediately (200 OK) to Stripe, process async

## Current State
Working on proper idempotency for webhook handlers (same webhook called twice = same result)
```

---

## How Context Layers Combine: Inheritance Rules

**Critical to Understand**: How does Gemini decide which context to use when you have GEMINI.md files at multiple levels?

### The Inheritance Pattern

When you open Gemini CLI in a directory:

```
1. Load Global Context (~/.gemini/GEMINI.md)
   ↓ (base foundation)
2. Layer Project Context (./GEMINI.md)
   ↓ (overrides where different)
3. Layer Subdirectory Context (./src/api/GEMINI.md)
   ↓ (most specific)
Final: Merged context (Global + Project + Subdirectory)
```

**Key Rules**:

- **Specificity Wins**: Subdirectory context overrides project context overrides global
- **Additive Not Exclusive**: Subdirectory context ADDS TO project context (both apply)
- **Last Write Wins**: If global says "use Python 3.12" and project says "use Python 3.13", the project context wins

### Example: How Context Merges

**Scenario**: You're working on `./src/payments/` in the e-commerce project.

**What Gets Loaded**:

```
Global Context (~/.gemini/GEMINI.md):
  - Python 3.13 required
  - Type hints mandatory
  - 80% test coverage minimum
  - Security: No secrets in code

Project Context (./GEMINI.md):
  - FastAPI backend
  - PostgreSQL database
  - Stripe integration
  - Free tier limits apply

Subdirectory Context (./src/payments/GEMINI.md):
  - Stripe webhook handlers
  - Async-only operations
  - Idempotency required
  - Never block on external APIs
```

**Result**: Gemini understands ALL of this context together. When you ask for help with a payment handler:
- Uses Python 3.13 with type hints (global)
- Within FastAPI/PostgreSQL architecture (project)
- Following async patterns and idempotency rules (subdirectory)

### How to Update Context: The Refresh Pattern

If you modify a GEMINI.md file, Gemini doesn't automatically reload it.

**Specification**: "I updated my context; let me tell Gemini"

**Execution**: Use `/memory refresh`

```bash
# You edit ./GEMINI.md to add a new architecture decision
$ nano ./GEMINI.md

# Tell Gemini to reload
gemini /memory refresh

# Gemini responds
Gemini: ✓ Reloaded context from all GEMINI.md files
```

**Validation**: Confirm the change took effect

```bash
gemini /memory show
# Should display your updated context
```

---

## Specification-First GEMINI.md Design

### Step 1: Specify What AI Needs to Know

Before writing GEMINI.md, clarify **what your AI partner needs to understand** about this project.

**Bad specification**: "Create a context file"
**Good specification**: "Create a context file so Gemini understands my API's authentication pattern without me re-explaining it every session"

### Step 2: Design the Three-Level Hierarchy

Decide what goes at each level:

```
Global (~/.gemini/GEMINI.md):
  [Your personal standards]

Project (./GEMINI.md):
  [This project's architecture]

Subdirectory (./src/api/GEMINI.md):
  [API-specific patterns]
```

### Step 3: Write Context with AI Collaboration

**Prompt Your AI Partner**:

```
I'm building a FastAPI e-commerce backend. Help me design a GEMINI.md
context specification for this project. Here's what I need Gemini to understand:

1. We use PostgreSQL for data (ACID requirements)
2. We use Stripe for payments (webhook handlers needed)
3. We enforce async-only pattern (no blocking operations)
4. We require 80%+ test coverage

Structure this as a GEMINI.md file that helps Gemini understand
all these constraints automatically.
```

**AI Suggests**:
- Sections to include in GEMINI.md
- Specific constraints to highlight
- Architecture explanations needed
- Critical gotchas to document

**You Refine**:
- Adjust based on your reality
- Add project-specific decisions
- Remove sections that don't apply

### Step 4: Validate Context Injection

**Specification**: "Verify that Gemini actually understands my project without re-explanation"

**Execution**:

```bash
# Terminal Session 1: Set up project context
$ cd ~/my-project && gemini

gemini> Here's my architecture:
[Explain your project]

gemini> /memory save session-1-context

# Exit and wait 30 minutes (simulate next day)

# Terminal Session 2: Resume without explanation
$ cd ~/my-project && gemini

gemini> /memory restore session-1-context

# Now ask Gemini something that requires understanding
gemini> What's the best approach for adding a new API endpoint
        to my payment service? Keep in mind my constraints.
```

**Validation Checklist**:
- [ ] Gemini references your architecture (shows it was loaded)
- [ ] Gemini suggests patterns consistent with your constraints
- [ ] Gemini doesn't ask you to re-explain the project
- [ ] Response quality is high (AI understands context)

---

## Creating GEMINI.md Files: Two Approaches

### Approach 1: Specification-First Collaboration (Recommended)

**You write the specification**. AI helps you turn it into a structured context file.

```markdown
## SPECIFICATION: Design Project Context File

**Problem**: I have a complex microservices architecture. Gemini needs to
understand service boundaries without me explaining every time.

**Requirements**:
1. List which service owns which endpoints
2. Explain inter-service communication patterns
3. Document shared data/contracts
4. Flag critical deployment constraints

**Success**: Gemini can suggest a new endpoint and recommend which
microservice should handle it, based on the GEMINI.md.

**Constraints**:
- Max 2000 words (keep it focused)
- Use clear section headers (AI parses these)
- Include decision rationale, not just decisions
```

**Prompt AI**:

```
Here's my specification for a GEMINI.md file:
[Paste specification above]

Generate the GEMINI.md content that meets this specification.
```

**AI Generates**: Complete, well-structured GEMINI.md

**You Validate**: Does it capture what you need? Edit as needed.

### Approach 2: Template-Based (Faster)

Use this template structure:

```markdown
# [Project Name] - Context Specification

## Summary
[One paragraph: What are we building? Core purpose.]

## Technology Stack
- Language & frameworks
- Database, cache, queues
- External services (Stripe, SendGrid, etc.)

## Architecture Overview
[2-3 key decisions and why you made them]

## Project Structure
[Key directories and what's in them]

## Current Status
- ✅ Complete
- 🔄 In Progress
- ⏳ Planned

## Code Conventions
[Your style rules, naming patterns, testing approach]

## Critical Constraints
[Rate limits, resource limits, deployment constraints]

## Important Notes
[Gotchas, common mistakes, things to watch for]
```

---

## Real-World Example: Three-Level Context Architecture

Here's how a real project uses all three levels:

### Level 1: Global (`~/.gemini/GEMINI.md`)

```markdown
# Global Development Context

## Languages
- Python 3.13 (backend)
- TypeScript 5.3 (frontend)

## Type Checking
- Python: mypy --strict
- TypeScript: strict mode enabled

## Testing
- pytest with >80% coverage (Python)
- Jest with snapshots (TypeScript)

## Security
- No secrets in code ever
- Use environment variables
- Rotate tokens every 90 days
```

### Level 2: Project (`./GEMINI.md`)

```markdown
# SaaS Billing Platform

## Purpose
Handle billing, invoicing, and payment reconciliation for our SaaS.

## Tech Stack
- FastAPI backend
- PostgreSQL database
- Stripe for payment processing
- Celery for async tasks

## Architecture
- REST API (/api/v1/)
- Background workers (payment reconciliation)
- Webhook handlers (Stripe events)

## Key Decision: Stripe as Source of Truth
Don't re-implement payment logic. Trust Stripe's payment state.
Reconcile daily: our DB vs Stripe API.

## Current
- ✅ Invoice generation
- 🔄 Payment reconciliation
- ⏳ Customer portal
```

### Level 3: Subdirectory (`./src/workers/GEMINI.md`)

```markdown
# Async Workers Module

## Purpose
Background jobs: reconciliation, email sending, report generation.

## Architecture
- Celery tasks (run via Redis queue)
- Scheduled: Celery Beat
- Monitoring: Sentry for error tracking

## Key Pattern: Idempotency
Every worker task must be idempotent.
If Celery retries, same result. No duplicates.

## Current
- Payment reconciliation (daily)
- Invoice email sending (async)
```

**How They Merge**: When you're in `./src/workers/` asking for help on a reconciliation task:
- Gemini knows Python 3.13, type hints, testing (global)
- Knows Stripe is source of truth, REST API structure (project)
- Knows idempotency is critical, Celery retry pattern (subdirectory)

---

## Best Practices for GEMINI.md Files

### ✅ DO

- **DO update regularly**: As your project evolves, update GEMINI.md
- **DO include rationale**: Document WHY you made decisions, not just WHAT
- **DO be specific with examples**: Show patterns, not just rules
- **DO include warnings**: What should AI never do? Put it here
- **DO keep it focused**: ~500-1000 words per level; prioritize what matters

### ❌ DON'T

- **DON'T include secrets**: Never put API keys, passwords, or credentials
- **DON'T copy README verbatim**: README is for humans; GEMINI.md is for AI
- **DON'T write it once and forget**: Context becomes outdated quickly
- **DON'T overwhelm with detail**: If AI doesn't need to know, leave it out
- **DON'T use unexplained jargon**: Define domain-specific terms

---

## Practical Exercises

### Exercise 1: Write a Global GEMINI.md

**Specification**: Create a global context that captures YOUR coding standards.

**Steps**:
1. Identify your 3 most important coding rules
2. Write them as a specification
3. Create `~/.gemini/GEMINI.md` with these rules
4. Launch Gemini and run `/memory show` to verify it loaded

**Validation**: Can you see your rules in the loaded context?

### Exercise 2: Create Project Context

**Specification**: Document ONE project you're working on using the GEMINI.md structure.

**Steps**:
1. Pick a current project
2. Write its purpose (1 paragraph)
3. List its technology stack
4. Document 2 key architecture decisions and why
5. Create `./GEMINI.md` in project root
6. Load project in Gemini: `cd ~/project && gemini /memory show`

**Validation**: Can Gemini describe your project back to you?

### Exercise 3: Test Context Layers

**Specification**: Verify that project context overrides global context.

**Steps**:
1. Create/edit your `~/.gemini/GEMINI.md` with: "Primary language: Python"
2. Create/edit `./GEMINI.md` in a project with: "Primary language: TypeScript (this project only)"
3. Launch Gemini in that project: `gemini /memory show`
4. Ask Gemini: "What's my primary language for this project?"

**Validation**: Does Gemini correctly say TypeScript (not Python)?

### Exercise 4: Design a Three-Level Hierarchy

**Specification**: Create context for a complex project at all three levels.

**Scenario**: You have a microservices project with API, worker, and database services.

**Steps**:
1. Create `~/.gemini/GEMINI.md` (personal standards)
2. Create `./GEMINI.md` (microservices architecture)
3. Create `./src/api/GEMINI.md` (API service specifics)
4. Create `./src/workers/GEMINI.md` (worker service specifics)
5. Test each level: `cd ./src/api && gemini /memory show`

**Validation**:
- [ ] Each level loads correctly
- [ ] Levels combine (don't replace each other)
- [ ] Most specific level wins in case of conflicts

---

## Try With AI

**Setup**: You have Gemini CLI installed and a project to work with.

**Prompt 1: Context Specification**

```
I want to create a GEMINI.md file for my project. Help me design it.
Here's what my project does: [briefly describe your project]

What should I include in GEMINI.md so you can understand this project
without me re-explaining it every session?
```

**Expected Outcome**: AI suggests sections and content for your GEMINI.md. Note that AI teaches you about context architecture—a concept you may not have considered before.

**Prompt 2: Validation Through Understanding**

After you create a GEMINI.md file:

```
I just created a GEMINI.md file for my project. Without me explaining
anything else, tell me: What is this project? What are its main
constraints? What should I never do here?
```

**Expected Outcome**: AI reads your GEMINI.md and summarizes the project. This validates that context injection works—AI understands without re-explanation.

**Prompt 3: Collaborative Hierarchy Design**

```
My project has both a public API and internal admin tools.
Should these be at the same level in GEMINI.md, or use different
directories? Help me design a three-level hierarchy that makes
sense for this structure.
```

**Expected Outcome**: AI teaches you about context architecture. You learn hierarchy thinking by collaborating on design decisions.

**Safety Note**: GEMINI.md is non-executable—it's just text Gemini reads. However, ensure you never include credentials, API keys, or sensitive configuration in GEMINI.md files. If you commit GEMINI.md to Git, anyone with repo access can read it.

---

## Summary

GEMINI.md files are **context specifications**—how you architect your AI partner's understanding of your project:

- **Three-level hierarchy**: Global (personal standards) + Project (architecture) + Subdirectory (module specifics)
- **Inheritance rules**: Specific overrides general; all levels combine together
- **Write once, benefit forever**: GEMINI.md persists across sessions
- **Update as you evolve**: GEMINI.md is a living document alongside your code
- **Specification-first approach**: Clarify WHAT Gemini needs to know BEFORE writing context
- **Validate context works**: Test that AI understands without re-explanation

Next lesson: You'll learn **memory checkpoints**—how to save and resume conversations across days without losing context.
