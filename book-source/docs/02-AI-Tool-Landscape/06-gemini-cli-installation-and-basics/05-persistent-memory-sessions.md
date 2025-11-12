---
sidebar_position: 5
title: "Memory & Session Management"
duration: "30 min"
skills:
  - Session Architecture Specification (A2-B1)
  - Context Persistence Design (A2-B1)
  - Multi-Day Workflow Orchestration (B1)
generated_by: lesson-writer (claude-haiku-4-5)
source_spec: 022-audit-chapter6-gemini-cli/plan.md#lesson-5
created: 2025-01-12
last_modified: 2025-01-12
git_author: claude-code
workflow: "SDD: Evals-First → Spec-First → Implement → Validate (Constitutional Alignment)"
version: "2.0.0-constitutional-alignment"
---

# Memory & Session Management: Specifying Session Persistence

## Learning Objectives

By the end of this lesson, you'll be able to:
- **Write specifications** for multi-day workflows that persist conversation state across sessions
- **Architect checkpoint strategies** that preserve context and decisions without repetition
- **Validate session recovery** to ensure conversations resume with complete context
- **Collaborate with AI** on session organization and workflow optimization

---

## Understanding Session Architecture

Gemini CLI gives you two complementary systems for preserving your work:

| System | Purpose | Scope |
|--------|---------|-------|
| **GEMINI.md** (Lesson 4) | Static project knowledge (tech stack, conventions, architecture) | Automatically loaded every session |
| **Saved checkpoints** (this lesson) | Dynamic work progress (conversations, decisions, code reviews) | Per-task persistence across sessions |

**Mental Model**: You're specifying HOW your work persists across time, not just SAVING outputs.

---

## Checkpoint Mechanics: What Persists

### Specification: Session Persistence Requirements

When you save a checkpoint with `/chat save <tag>`, you're implementing a specification:

**Specification**:
> Preserve conversation history and decisions so I can resume tomorrow without re-explaining the project

**What Gets Saved**:
- ✅ Full conversation history (everything you discussed)
- ✅ Context knowledge you shared (project details, code patterns)
- ✅ Decisions made together (architectural choices, approaches tested)
- ✅ Code you reviewed (files examined, feedback provided)
- ✅ Current work state (what you decided to do next)

**What Does NOT Get Saved**:
- ❌ Your actual source code files (those live in Git; GEMINI.md describes them)
- ❌ Terminal output or shell history
- ❌ External API responses (though you can re-request them)

**Why This Matters**: You can reconstruct your work context without memorizing details. Gemini remembers, you orchestrate.

---

## The Checkpoint Command Family

### Commands as Session Specifications

Each command implements a specific session architecture decision:

| Command | Specification | When to Use |
|---------|--------------|-----------|
| `/chat save <tag>` | "Checkpoint this conversation for later resumption" | After completing a meaningful work chunk |
| `/chat resume <tag>` | "Restore previous conversation with full context" | Starting work on something you paused |
| `/chat list` | "Show all saved checkpoints" | When organizing your work or switching projects |
| `/chat delete <tag>` | "Remove completed checkpoint" | After archiving finished work |
| `/chat share file.md` | "Export conversation for collaboration" | Sharing design decisions with teammates |

---

## Naming Checkpoints: Specification Clarity

Good checkpoint names make your sessions **discoverable**:

### Specification Pattern: `[feature/task]-[status]` or `[date]-[phase]`

**Examples of Clear Specifications**:
- `auth-jwt-endpoints-designed` — Specifies what's done and what's next
- `database-migration-v2-approved` — Version clarity for parallel work
- `2025-01-12-morning-research` — Time-based specification for time-series work
- `payments-integration-testing` — Task-phase clarity

**Avoid (Vague Specifications)**:
- ❌ `save1`, `checkpoint`, `temp` — No semantic meaning
- ❌ `test` — Ambiguous (test what?)
- ❌ `work` — No specificity about state

**Validation**: Can a teammate understand what you did just from the name? If not, your checkpoint name isn't specific enough.

---

## Multi-Day Workflow: Specification-Driven Checkpointing

### Day 1: Research & Design Phase

**Specification**:
> Research authentication patterns and design JWT approach for our API. Save state for implementation review tomorrow.

```bash
$ gemini
You: Let's design JWT authentication. Requirements:
     - User registration endpoint
     - Login with JWT tokens
     - Refresh token rotation
     - Protected routes

Gemini: I'll help design this security-conscious approach...
(Spend 2 hours discussing architecture and design patterns)

You: /chat save auth-jwt-designed
Gemini: ✓ Saved conversation as "auth-jwt-designed"

You: /quit
```

**Validation Checklist**:
- [ ] Checkpoint saved with clear name
- [ ] All architecture decisions documented in conversation
- [ ] Known gotchas (rate limits, token expiry) discussed

---

### Day 2: Implementation Phase

**Specification**:
> Resume yesterday's design context and implement the register endpoint with proper error handling and validation.

```bash
$ gemini
You: /chat resume auth-jwt-designed
Gemini: ✓ Resumed "auth-jwt-designed"
        (Full conversation history restored)

You: Perfect, I have all the context. Now let's implement the register endpoint
     with the design we discussed.

(Implement register endpoint)

You: /chat save register-endpoint-complete
Gemini: ✓ Saved
```

**Validation Checklist**:
- [ ] Resumed conversation and verified Gemini remembers yesterday's design
- [ ] Can ask follow-up questions referencing previous decisions
- [ ] No need to re-explain requirements or architecture

---

### Day 3: Testing & Refinement Phase

**Specification**:
> Resume implementation context and add comprehensive testing. Mark as complete when tests pass.

```bash
$ gemini
You: /chat resume register-endpoint-complete
Gemini: ✓ Resumed

You: Now let's write tests covering success and error cases

(Develop test suite)

You: /chat save register-endpoint-tested
Gemini: ✓ Saved
```

**Validation Checklist**:
- [ ] Tests pass against specification from Day 1
- [ ] Code review completed and documented
- [ ] Ready for next phase (login endpoint)

---

## Context Overflow Management

### Specification Challenge: Deep Projects

**Scenario**: After 5 days of implementation, your conversation is 50,000 tokens. Gemini's context is getting full.

**Three Strategies**:

#### Strategy 1: Checkpointing at Phase Boundaries

**Specification**: Break long projects into phases, checkpoint at boundaries

```bash
Day 1-2:  /chat save phase-1-auth-endpoints-complete
Day 3-4:  /chat save phase-2-database-schema-complete
Day 5-6:  /chat save phase-3-integration-testing-complete
```

**Why This Works**: Each phase checkpoint has ~10-15 hours of context (manageable), and you can reference previous checkpoints if needed.

#### Strategy 2: Compression Checkpoints

**Specification**: When context fills, save current checkpoint, then use `/compress` and continue

```bash
(Work for 5 hours, context is 80% full)
You: /chat save current-state-backup
Gemini: ✓ Saved

You: /compress
Gemini: Intelligently summarized conversation (40% size reduction)

(Continue working with freed capacity)
```

#### Strategy 3: Reference Checkpoints

**Specification**: Save frequently, only keep recent checkpoints active

```bash
(Every 2 hours)
You: /chat save [phase]-[timestamp]
You: /chat list
You: /chat delete [phase]-old-checkpoint
```

---

## Multi-Project Context Switching

### Specification: Project Isolation

When switching between projects, checkpoints keep contexts separate:

```bash
# Project A
$ cd auth-service && gemini
You: /chat resume auth-jwt-system-complete
Gemini: ✓ Resumed Project A context

You: [Work for 2 hours]
You: /chat save auth-api-endpoint-testing
You: /quit

# Switch to Project B
$ cd frontend && gemini
You: /chat save frontend-current-progress
You: /clear

You: /chat resume frontend-components-v2
Gemini: ✓ Resumed Project B context (completely separate from Project A)
```

**Validation**: Verify Gemini doesn't confuse contexts between projects by asking about Project A details while on Project B. It should respond "I'm not sure about that—let me review your GEMINI.md if available."

---

## Pair Programming: Checkpoint Handoff

### Specification: Multi-Developer Workflows

**Scenario**: Developer A works 9 AM–1 PM, Developer B works 1 PM–5 PM

**Developer A (Morning)**:
```bash
You: [Work on authentication feature for 3 hours]
You: /chat save feature-auth-progress-for-bob
You: /quit
```

**Developer B (Afternoon)**:
```bash
You: /chat resume feature-auth-progress-for-bob
Gemini: ✓ Resumed Bob's conversation

You: I can see Bob designed the auth flow. Let me review and add refresh tokens...
```

**Validation Checklist**:
- [ ] Context handoff is clean (no missing context)
- [ ] Gemini remembers morning's decisions and code reviews
- [ ] New developer can continue seamlessly

---

## Advanced Pattern: Experimentation With Safety

### Specification: Reversible Exploration

Try risky approaches without losing stable work:

```bash
You: /chat save stable-version  # Create safety checkpoint
Gemini: ✓ Saved

# Try experimental refactoring
You: Let me try a completely different architecture approach...
(Experiment for 1 hour)

You: Hmm, this isn't better. Going back.
You: /clear
You: /chat resume stable-version
Gemini: ✓ Resumed

You: I'm back to the working version.
```

**Why This Works**: You have multiple checkpoints at different points in time, so you can branch explorations and merge or discard them.

---

## GEMINI.md + Checkpoints Together

### Complete Specification: Unified Persistence

These two systems combine for complete context management:

```bash
Day 1:
  $ cd auth-service && gemini
  # GEMINI.md loads automatically: "Python 3.13, FastAPI, PostgreSQL, JWT tokens"

  You: [Discuss architecture for 2 hours]
  You: /chat save arch-design-approved
  You: /quit

Day 2:
  $ cd auth-service && gemini
  # GEMINI.md loads automatically (same project context as before)

  You: /chat resume arch-design-approved
  # Now you have TWO contexts:
  # 1. GEMINI.md: What the project uses (tech stack, conventions)
  # 2. Checkpoint: What you discussed yesterday (design decisions, code reviews)

  You: Let's implement the endpoints now...

Day 3 (Switch Projects):
  $ cd frontend && gemini
  # Different GEMINI.md loads (frontend-specific context)

  You: /clear
  You: /chat resume frontend-components-v2
  # Now working on frontend with its own GEMINI.md + frontend's saved checkpoint
```

**Result**: Perfect context switching. Gemini always knows which project, what conventions apply, and what work was done.

---

## Red Flags to Watch

### Checkpoint Corruption Detection

**Red Flag 1**: Conversation won't resume
```
❌ You: /chat resume old-session
❌ Gemini: "That conversation doesn't exist" or "File corrupted"
✅ SOLUTION: If backup exists, try `/chat resume backup-name`
           Otherwise, rebuild context with GEMINI.md + fresh conversation
```

**Red Flag 2**: Resumed conversation loses context
```
❌ You: /chat resume session-name
❌ Gemini: Resumes but forgets previous decisions/code
✅ SOLUTION: Check `/stats` (context may have been trimmed)
           Ask Gemini: "What was the main decision we made yesterday?"
           If blank, context was lost; save fresh checkpoint
```

**Red Flag 3**: Context accumulates; compression fails
```
❌ You: /compress
❌ Gemini: "Context is at maximum, can't summarize further"
✅ SOLUTION: Create checkpoint at phase boundary
           Clear conversation and start fresh with new checkpoint
           Reference old checkpoint if needed ("Remember we decided X...")
```

**Red Flag 4**: Switching projects, wrong context loads
```
❌ You: [Switch projects, resume checkpoint]
❌ Gemini: References old project's details
✅ SOLUTION: Always run `/clear` before switching projects
           Verify GEMINI.md for new project loaded correctly
           Ask: "What project are you working on?" to confirm
```

---

## Validation in Practice

### Specification: Verify Session Recovery

Before relying on a checkpoint, validate it works:

```bash
You: /chat resume important-session
Gemini: ✓ Resumed

# VALIDATION TEST:
You: What project were we working on?
Gemini: [Should answer accurately from checkpoint]

You: What was the main architectural decision?
Gemini: [Should recall from saved conversation]

You: Show me the key code we reviewed
Gemini: [Should reference files/patterns from conversation]

# All tests pass? Checkpoint is reliable.
```

---

## Common Checkpoint Questions

**Q: Do checkpoints sync across my devices (laptop + desktop)?**

A: No—checkpoints are stored locally on each machine. Save explicitly on each device:
```bash
Laptop: /chat save feature-design
Desktop: That checkpoint doesn't exist here yet
```
Solution: Use `/chat share` to export and transfer, or keep device-specific checkpoint names.

**Q: Can I edit a saved checkpoint?**

A: Not directly, but you can:
1. Resume the checkpoint
2. Continue the conversation (adds to it)
3. Save with a new name
```bash
You: /chat resume old-design
(Conversation history loads)
You: [Continue discussing, modifying approach]
You: /chat save new-design-v2
```

**Q: If I don't save, am I losing work?**

A: Conversation history is lost when you close Gemini CLI. **Always save before quitting**:
```bash
❌ You: /quit  # Lost all conversation!
✅ You: /chat save my-session
   You: /quit  # Safe—checkpoint exists
```

**Q: How much storage does a checkpoint use?**

A: Conversations are text-based, very lightweight. A 2-hour conversation (~8,000 tokens) is typically 100–500 KB.

---

## Exercises

### Exercise 1: Create Your First Checkpoint

**Specification**: Save a real conversation checkpoint that you can resume later.

```bash
$ gemini
You: [Have a meaningful conversation for 15+ minutes on a real task]
You: /chat save first-checkpoint
Gemini: ✓ Saved
```

**Validation**:
- [ ] Checkpoint saved successfully
- [ ] List shows checkpoint: `/chat list`
- [ ] Can resume it: `/chat resume first-checkpoint`

---

### Exercise 2: Multi-Session Resumption

**Specification**: Close Gemini, reopen it, and verify context is fully restored.

```bash
# Session 1
$ gemini
You: [Work for 10 minutes on a specific topic]
You: /chat save session-one
You: /quit

# Session 2 (immediately after)
$ gemini
You: /chat resume session-one
Gemini: ✓ Resumed

# VALIDATION:
You: What was I working on? (Should recall from saved conversation)
Gemini: [Answers accurately—context preserved ✓]
```

---

### Exercise 3: Checkpoint Organization

**Specification**: Manage multiple checkpoints and understand what each represents.

```bash
You: /chat list
# Shows: checkpoint-1, checkpoint-2, checkpoint-3...

# Rename by archiving old, saving new:
You: /chat save checkpoint-1-archived
You: /chat delete checkpoint-1

# Now list is clean and organized
You: /chat list
# Shows only relevant checkpoints
```

---

### Exercise 4: Project Switching

**Specification**: Work on Project A, checkpoint, switch to Project B, verify isolation.

```bash
# Project A
$ cd project-a && gemini
You: /chat save project-a-checkpoint
You: /quit

# Project B (different directory)
$ cd project-b && gemini
You: /clear
You: [Work on project-b for 10 minutes]
You: /chat save project-b-checkpoint

# Back to Project A
You: /quit
$ cd project-a && gemini
You: /chat resume project-a-checkpoint
Gemini: ✓ Resumed (completely separate from Project B)
```

**Validation**: Confirm Project A context is restored independently.

---

## Try With AI

### Co-Learning Exercise: Session Architecture Design

Let's practice specifying session management strategies with your AI partner.

**Tool Selection**: Use Gemini CLI itself (the tool you're learning) for authentic practice.

---

### Prompt 1: AI as Teacher — Understanding Strategies

Copy and paste into Gemini CLI:

```
I'm working on a multi-week project with 3 distinct phases (research → design → implementation).
Teach me: what's the difference between:
1. Saving one big checkpoint at the very end
2. Saving checkpoints at each phase boundary
3. Saving hourly checkpoints throughout

When should I use each approach, and what are the trade-offs?
```

**Expected Outcome**: Gemini explains checkpoint strategies you might not have considered (frequency, granularity, recovery vs. organization tradeoffs).

**What You Learn**: AI teaches you orchestration patterns—when checkpointing matters most.

---

### Prompt 2: AI as Student — Adapting to Your Workflow

After Gemini responds above, follow with:

```
I work in 2-hour blocks, 3 times a week, on the same project. Given my specific schedule,
what checkpoint strategy would you recommend? Suggest a naming convention too.
```

**Expected Outcome**: Gemini adapts its recommendation to YOUR pattern (not generic advice). It suggests practical naming that fits your workflow.

**What You Learn**: AI learns YOUR constraints and personalizes advice. This is the partnership in action.

---

### Prompt 3: AI as Co-Worker — Design Together

Continue:

```
Let's design a session management specification for my project together.
Here's my constraint: I want to be able to recover from any failed experiment without losing stable work.

Help me design a checkpoint strategy that protects against that. What commands would I run?
```

**Expected Outcome**: Gemini collaborates to design a strategy with you—combining your requirement (safety) with its technical knowledge (checkpoint mechanics).

**What You Learn**: Session management is specification (describing what you want), not just commands (typing what exists).

---

### Safety & Verification Note

- **Before relying on checkpoints**: Always test resumption on real work. Verify Gemini remembers context.
- **Checkpoint naming**: Use descriptive names so you know exactly what each checkpoint represents.
- **Device isolation**: Remember—checkpoints are device-local. Don't expect them to sync automatically.

---

