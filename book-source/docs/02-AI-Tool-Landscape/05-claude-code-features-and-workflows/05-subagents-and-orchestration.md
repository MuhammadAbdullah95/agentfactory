---
sidebar_position: 5
title: "Subagents and Orchestration"
duration: "6-8 min"
---

# Subagents and Orchestration

You've installed Claude Code and tried basic commands. Now let's understand **subagents**—specialized AI assistants that help Claude Code handle complex tasks more effectively.

---

## The Problem: Context Clutter

Imagine you're working on a Python project. You ask Claude Code to:
1. Explain how authentication works
2. Debug a payment function
3. Find all API endpoints
4. Refactor the database layer

By request #4, Claude Code's conversation context is cluttered with explanations, debugging details, and endpoint lists. The context is messy.

**Solution**: Instead of one AI trying to do everything, **specialized assistants (subagents)** handle focused tasks with clean, isolated context.

---

## What Are Subagents?

**Definition**: A subagent is a specialized AI assistant with its own instructions and isolated context window. Each subagent is an expert at one type of task.

Think of Claude Code as a project manager with a team of specialists:
- **Claude Code (main)**: Coordinates overall work
- **Plan subagent**: Researches your codebase and creates multi-step plans
- **Custom subagents**: You can create specialists for your team's specific needs (code review, security checks, documentation, etc.)

**Key benefit**: Each subagent has **clean context** (no clutter from other conversations) and **focused expertise** (specialized instructions for its task).

---

## The Plan Subagent (Built-In)

Claude Code includes a **Plan subagent** that automatically activates for complex, multi-step tasks.

### When Plan Activates

When you ask for complex work, Claude Code delegates to the Plan subagent:

**You ask**: "Add user authentication to this project"

**Plan subagent does**:
1. **Researches your codebase** to understand current structure
2. **Creates a multi-phase plan**:
   - Phase 1: Database schema (users table, sessions)
   - Phase 2: Auth logic (password hashing, login/logout)
   - Phase 3: Integration (middleware, protect routes)
   - Phase 4: Testing (unit tests, flow validation)
3. **Presents plan for your approval** before any changes

### Why This Matters

**Without Plan subagent**: Claude might jump straight to code without understanding your project structure, missing dependencies or creating conflicts.

**With Plan subagent**: Research happens first, then a strategic plan, then execution—step by step.

---

## How Subagents Work

### The Execution Model: One Task, One Completion

**Critical concept**: A subagent is invoked **once** for a specific goal, completes its work, and **returns results to main Claude Code**.

**The flow**:
1. Main Claude Code recognizes a task that needs a specialist
2. Launches the subagent with a specific goal
3. Subagent works independently in isolated context
4. Subagent completes its task and returns results
5. **Control returns to main Claude Code**
6. You interact with main Claude Code to proceed

**Think of it like this**: You send a specialist to research something. They go off, do their work, come back with a report, and then you continue the conversation with your main assistant.

### Automatic Delegation

You don't command "use the Plan subagent." Claude Code decides when to delegate based on:
- Task complexity (multi-step tasks trigger Plan)
- Your request type (code review request might trigger a review subagent if you have one)
- Subagent descriptions (Claude matches task to specialist)

**Example**:
```
You: "Refactor this Flask app to use async/await"
Claude Code: *recognizes complexity, delegates to Plan subagent*
Plan subagent: *researches your code, creates phase breakdown, returns plan*
Claude Code: *receives plan, presents it to you*
You: *approve or modify the plan*
Claude Code: *proceeds with execution*
```

### Explicit Invocation

You can also request a specific subagent directly:

```
You: "Use the code-reviewer subagent to check my changes"
Claude Code: *invokes code-reviewer, waits for results, presents findings*
```

---

## Custom Subagents (Preview)

You can create your own subagents for team-specific workflows. Examples:

**Code Review Subagent**:
- Checks for your team's style guide
- Verifies type hints
- Ensures security best practices
- Runs on every pull request

**Documentation Subagent**:
- Generates docstrings
- Creates README sections
- Updates API docs
- Follows your team's doc standards

**Important**: Creating custom subagents is **Part 5 content** (intermediate/advanced). For now, you're learning the concept and using the built-in Plan subagent.

---

## Understanding Orchestration

**Orchestration** = AI coordinating multiple specialists toward a goal

When you ask for a complex task:
1. **Claude Code (orchestrator)** analyzes your request
2. **Launches a specialist subagent** (e.g., Plan subagent) for a specific goal
3. **Subagent completes its task** (researches, creates plan) and **returns results**
4. **Control returns to main Claude Code**, which presents the results to you
5. **You approve/modify** the plan
6. **Main Claude Code executes** step-by-step with your oversight

**Key insight**: Subagents don't stick around. They're invoked for one task, complete it, return results, and hand control back to main Claude Code.

**This is orchestration in action**: One AI managing a team of specialist AIs to accomplish complex work—each specialist does their job and returns the baton.

---

## Practical Example: Add User Login

Let's see the complete subagent lifecycle:

**You**: "Add user login with email/password to this project"

**What happens**:

1. **Claude Code recognizes complexity** → launches Plan subagent with goal: "research project and create auth plan"
2. **Plan subagent works independently**:
   - Reads your project structure
   - Identifies: Flask app, SQLAlchemy ORM, no auth yet
   - Notes: Has pytest for testing
   - Creates multi-phase plan
3. **Plan subagent completes task and returns plan**:
   - Subagent's job is done
   - Control returns to main Claude Code
4. **Main Claude Code presents the plan to you**:
   ```
   Phase 1: Database Setup
   - Create User model with hashed password field
   - Add sessions table for token storage
   - Create database migration

   Phase 2: Authentication Logic
   - Implement password hashing (bcrypt)
   - Create login/logout endpoints
   - Build session management

   Phase 3: Protection Layer
   - Add authentication middleware
   - Protect existing endpoints that need auth
   - Create login UI form

   Phase 4: Testing
   - Unit tests for password hashing
   - Integration tests for login flow
   - Security test for password requirements
   ```
5. **You approve** (or modify the plan)
6. **Main Claude Code executes** the plan phase by phase
   - Plan subagent is not involved in execution
   - Main Claude Code handles all the coding work
   - You oversee and approve changes at each step

**Key insight**: The Plan subagent's job ended at step 3 when it returned the plan. Everything after that is main Claude Code executing the plan you approved.

**Total time**: 10-15 minutes for complete authentication system (vs hours manually)

---

## Where Subagents Live

Subagents are stored as Markdown files with YAML frontmatter:

**Project-level**: `.claude/agents/` (specific to this project)
**User-level**: `~/.claude/agents/` (available across all your projects)

**Example subagent file structure**:
```markdown
---
name: code-reviewer
description: Reviews Python code for quality and security
tools: [Read, Grep]
---

# Code Review Instructions

When reviewing code:
1. Check for type hints
2. Verify error handling
3. Look for security issues
4. Ensure docstrings exist
...
```

---

## What You Can Do Now vs Later

**NOW (Part 2 - Beginner)**:
- ✅ Understand what subagents are
- ✅ Use the built-in Plan subagent (automatic)
- ✅ Recognize when delegation happens
- ✅ Understand orchestration concept

**LATER (Part 5 - Intermediate)**:
- ⏰ Create custom subagents for your team
- ⏰ Configure subagent tools and permissions
- ⏰ Build sophisticated orchestration workflows

---

## Try With AI

Open Claude Code in a project directory and try these prompts:

### Prompt 1: Trigger the Plan Subagent

```
I want to add a REST API with CRUD endpoints for "Product" resource.
Create a plan showing the phases and what each phase does.
```

**Expected outcome**: Plan subagent researches your project, then presents a multi-phase breakdown (setup → endpoints → validation → testing).

### Prompt 2: Understand the Delegation

```
Explain what just happened when I asked for that plan.
Did you delegate to a subagent? How did you decide to use Plan mode?
```

**Expected outcome**: Claude explains that complex multi-step tasks trigger the Plan subagent automatically for better research and strategic planning.

### Prompt 3: Compare Approaches

```
What's the difference between:
1. Me asking you to "add authentication" (and you doing it immediately)
2. Me asking you to "plan how to add authentication" (Plan subagent)

Which approach is better for complex features? Why?
```

**Expected outcome**: Explanation that planning first (via Plan subagent) prevents mistakes by researching the codebase before making changes.

---

## What You Learned

- ✅ **Subagents** are specialized AI assistants with isolated context
- ✅ **Plan subagent** (built-in) researches your code and creates multi-phase plans
- ✅ **Automatic delegation** happens when Claude Code recognizes task complexity
- ✅ **Orchestration** means AI coordinating specialists toward a goal
- ✅ Creating custom subagents is advanced (Part 5), but you understand the concept now

**Next lesson**: You'll learn about Skills—another way to extend Claude Code's capabilities automatically.
