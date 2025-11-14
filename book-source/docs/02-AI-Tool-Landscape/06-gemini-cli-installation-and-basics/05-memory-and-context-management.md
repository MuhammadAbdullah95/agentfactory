---
sidebar_position: 5
title: Memory & Context Management
---

# Memory & Context Management

**Duration**: 18-20 minutes

## The Context Problem

Imagine you're working on an e-commerce API project. You open a fresh Gemini CLI session and ask:

> **You**: "What coding standards should I follow for this project?"

**Without context**, Gemini responds:
> *"I don't have any information about your specific project. Could you tell me: What programming language? What type of project? What frameworks?"*

You have to explain: TypeScript, Express.js, your team's conventions, architecture decisions, database setup...

**Every. Single. Session.**

---

## The Solution: Memory & Context Management

Now imagine the same scenario, but you've created a `GEMINI.md` file in your project:

```markdown
# Project Context: E-commerce API

## Team Conventions
- TypeScript with strict mode
- Use async/await for all async operations
- Maximum function length: 50 lines
- Run `npm test` before every commit

## Architecture
- REST API: Express.js + TypeScript
- Database: PostgreSQL (Prisma ORM)
- Auth: JWT tokens (24-hour expiry)
```

You open Gemini CLI. Same question:

> **You**: "What coding standards should I follow for this project?"

**With context loaded from GEMINI.md**, Gemini responds:
> *"Based on your E-commerce API project, here are your team's coding standards:*
> - *TypeScript strict mode is required*
> - *Use async/await (not .then() chains)*
> - *Keep functions under 50 lines*
> - *Always run `npm test` before committing*
>
> *Since you're using Prisma ORM, database queries should go through your schema definitions. Want me to review your code against these standards?"*

**Zero setup required.** Gemini CLI loaded `GEMINI.md` automatically.

### What Just Happened? The Loading Process

When you start Gemini CLI in your project directory, here's what happens behind the scenes:

**1. Discovery Phase** (Gemini CLI scans for GEMINI.md files):
```
✓ Found: ~/.gemini/GEMINI.md (User level)
✓ Found: /tmp/ecommerce-api/GEMINI.md (Project level)
```

**2. Loading Phase** (in hierarchy order):
```
[Loading User-Level Context - ~/.gemini/GEMINI.md]
• Your personal coding preferences
• Your default tools and styles

[Loading Project-Level Context - ./GEMINI.md]
• E-commerce API architecture
• Team conventions (TypeScript strict, async/await)
• Monorepo structure decision
```

**3. Context Window Status**:
```
User GEMINI.md: ~150 tokens
Project GEMINI.md: ~300 tokens
Total loaded: 450 tokens / 1,000,000 available
✅ Session ready!
```

**4. Merged Context in Action**:

Now when you ask: *"Write a function to validate user email"*

AI responds using **BOTH** your personal preferences AND project requirements:

```typescript
/**
 * Validates user email format for authentication
 * @param email - Email address to validate
 * @returns true if valid, false otherwise
 */
export const validateEmail = async (email: string): Promise<boolean> => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

// Follows your team's conventions:
// ✓ TypeScript strict mode (project)
// ✓ async/await pattern (project)
// ✓ JSDoc comments (your preference)
// ✓ Under 50 lines (project)
```

AI merged context from **multiple levels**—your personal style + project requirements.

This is the power of **persistent memory hierarchy**—and in this lesson, you'll master it alongside Gemini CLI's massive **1 million token context window**.

---

## Part 1: Understanding Context

### What Is Context?

Your context window is like **the amount of information Gemini can "see" at once**. Gemini CLI gives you 1 million tokens—approximately:
- 750,000 words (average 1.33 tokens per word)
- 100,000 lines of code (average 10 tokens per line)
- 20-30 large software projects worth of code

:::note Verified in Gemini CLI 0.15.0
The 1M token context window is confirmed as of January 2025 using the Gemini 2.0 Flash model.
:::

But here's the catch: **every message, file, and command output consumes tokens from your context window**.

### How Context Gets Constructed

When you start a Gemini CLI session, here's what happens:

1. **Startup Phase** (consumes tokens):
   - Load all `GEMINI.md` files in hierarchy (system → user → workspace → project → extension)
   - Load configuration from `settings.json`
   - Initialize system instructions

2. **Conversation Phase** (ongoing token consumption):
   - Each message you type consumes tokens
   - Each AI response consumes tokens
   - File contents you read consume tokens
   - Command outputs consume tokens
   - MCP server responses consume tokens

### Red Flags: Context Running Low

After long conversations, you might notice:
- **Slow responses** (AI is processing near the limit)
- **Forgotten context** (AI repeats questions answered earlier)
- **Errors about token limits** (explicit message)

When this happens, you have tools to manage it: **GEMINI.md for persistent memory**, and **context commands for session cleanup**.

#### 💬 AI Colearning Prompt

> "Explain why Gemini CLI gives you 1 million tokens instead of unlimited context. What are the tradeoffs of having a context limit vs unlimited history?"

---

## Part 2: Long-Term Memory with GEMINI.md

### The Problem with Context Alone

Context is **session-specific**. When you close Gemini CLI and reopen it tomorrow, all that conversation history is gone (unless you saved it).

For information that needs to persist across sessions, you need **memory**.

### Enter GEMINI.md

`GEMINI.md` files are persistent memory files that load **at every session start**. Gemini CLI checks multiple locations and loads them **hierarchically**:

1. **System level**: `/etc/gemini/GEMINI.md` (machine-wide context)
2. **User level**: `~/.gemini/GEMINI.md` (your personal defaults)
3. **Workspace level**: `<workspace-root>/.gemini/GEMINI.md` (shared across projects)
4. **Project root**: `<project-root>/GEMINI.md` (project-wide conventions)
5. **Directory level**: `<any-subdirectory>/GEMINI.md` (directory-specific context)
6. **Extension level**: `<extension-path>/GEMINI.md` (if extension is active)

:::tip Verified File Locations
User, project-root, and directory-level GEMINI.md files have been tested and confirmed working in v0.15.0. Gemini CLI automatically loads these hierarchically based on your current working directory.
:::

### Why Multiple Levels? Problem Each Level Solves

Imagine a large e-commerce monorepo:

```
ecommerce-monorepo/
├── GEMINI.md              ← Root level (project-wide)
├── backend/
│   ├── GEMINI.md          ← Directory level (backend-specific)
│   └── controllers/
├── frontend/
│   ├── GEMINI.md          ← Directory level (frontend-specific)
│   └── components/
└── shared/
```

**Root Level Problem**: *"Where do I add a new API endpoint?"*
- Without root GEMINI.md: AI asks about project structure
- With root GEMINI.md: AI knows monorepo layout, points to `backend/` directory

**Directory Level Problem**: *"Create a user authentication endpoint"*
- With only root: AI knows structure, but not backend-specific patterns
- With root + backend/GEMINI.md: AI knows Express.js, Prisma ORM, JWT auth, repository pattern

### Hierarchical Loading in Action

**Scenario**: You're working in `backend/` directory

```bash
cd ecommerce-monorepo/backend
gemini
```

**What loads**:
1. `~/.gemini/GEMINI.md` (your personal preferences)
2. `ecommerce-monorepo/GEMINI.md` (project-wide conventions)
3. `ecommerce-monorepo/backend/GEMINI.md` (backend-specific)

**Merged context**:
- Personal: JSDoc comments, functional style (user level)
- Project-wide: TypeScript strict, Jest, Conventional Commits (root level)
- Backend-specific: Express.js, Prisma, JWT, repository pattern (directory level)

**Result**: AI understands all three layers when generating code in `backend/`

If you move to `frontend/`:
```bash
cd ../frontend
gemini
```

**What loads**:
1. `~/.gemini/GEMINI.md` (your personal preferences)
2. `ecommerce-monorepo/GEMINI.md` (project-wide conventions)
3. `ecommerce-monorepo/frontend/GEMINI.md` (frontend-specific)

**Now AI knows**: React, Zustand, Tailwind (frontend-specific) instead of backend patterns.

### What Goes in GEMINI.md?

**Good candidates for GEMINI.md** (persistent across sessions):
- Team conventions and coding standards
- Architecture documentation
- Project structure and conventions
- Common setup commands
- Key design decisions
- Links to important docs

**Not for GEMINI.md** (session-specific):
- Today's debugging notes (use `/chat save` instead)
- Temporary task status
- One-off questions

### Example GEMINI.md

```markdown
# Project Context: My Web App

## Team Conventions
- Use TypeScript for all new code
- Prefer async/await over promises
- Run `npm test` before committing
- Keep components under 200 lines

## Architecture
- **Frontend**: React + TypeScript on port 3000
- **Backend**: Express.js + Node.js on port 5000
- **Database**: PostgreSQL (localhost:5432 for dev)
- **Auth**: JWT tokens, 24-hour expiry

## Key Decision: Monorepo Structure
We chose a monorepo (not separate repos) because:
- Shared types between frontend/backend
- Atomic commits for related changes
- Easier dependency management

## Setup Checklist
1. `npm install` in root
2. `npm run build:frontend`
3. `npm run dev:backend`
4. Postgres running locally
```

Every time you start a session in this project, Gemini reads this file and understands your architecture.

### Token Impact

⚠️ **Important**: GEMINI.md files **consume tokens from your 1M context window**.

If your GEMINI.md is 10,000 tokens and you have a 50,000-token conversation, you've used 60,000 of your 1M available. Keep GEMINI.md focused and lean.

#### 🎓 Expert Insight

> GEMINI.md is Gemini CLI's equivalent to CLAUDE.md in Claude Code or .cursorrules in Cursor. This "persistent context file" pattern is becoming universal across AI coding tools. Learn the concept once—file names change, but the pattern stays the same.

#### 🤝 Practice Exercise

> **Ask your AI**: "I'm working on a web app with React frontend and Node.js backend. Create a project-level GEMINI.md that includes: 1) Team conventions (coding style, commit rules), 2) Architecture overview (tech stack, ports, auth method), 3) Setup commands (install, build, run), and 4) One key design decision we made. Keep it under 2000 tokens."
>
> **Expected Outcome**: Copy-paste-ready GEMINI.md file you can add to your project root.

---

## Part 3: Context Management Commands

Now that you have GEMINI.md for **long-term persistent memory**, let's explore commands for managing **short-term session context**.

:::note Slash Commands Are Interactive
All commands starting with `/` work only in **interactive mode** (`gemini` command). They cannot be used with CLI flags (e.g., `gemini --clear` doesn't exist). Start an interactive session to use these commands.
:::

### Hard Reset: `/clear`

The `/clear` command **wipes everything**:
- Deletes entire conversation history
- Deletes all saved context
- **Keeps** persistent `GEMINI.md` files
- Returns to a fresh session

```
/clear
```

**Use Cases**:
- Starting completely new topic (e.g., "I was debugging authentication. Now I want to plan a database schema")
- Context pollution (too much irrelevant conversation)
- Fresh perspective on a problem

**Tradeoff**: You lose all conversation history. Start from scratch.

### Smart Summary: `/compress`

The `/compress` command is more intelligent:
- Summarizes entire conversation into compact form
- Replaces history with AI-generated summary
- Preserves key facts, decisions, and context
- Frees up tokens while maintaining continuity

```
/compress
```

**Use Cases**:
- Long conversation approaching 1M token limit
- Need to continue current task but want more tokens
- Want to keep context but compress it

**Tradeoff**: Summary is lossy (you lose exact wording, some details). But you keep the gist.

### Comparison: `/clear` vs `/compress`

| Command | History | GEMINI.md | Best For |
|---------|---------|-----------|----------|
| `/clear` | Deleted | Preserved | Fresh start, context switch |
| `/compress` | Summarized | Preserved | Freeing tokens, same task |

---

## Part 4: Conversational Branching

### The Problem: Multi-Task Workflows

You're debugging an authentication bug. You've been working for 2 hours. Suddenly, an urgent question arrives: "Can you review these API docs?"

If you just start a new conversation, you lose all your debugging context. If you ask AI to explain the API docs in the same conversation, you pollute your debugging context.

**Solution**: Save and resume conversations.

### Save Conversation: `/chat save`

```
/chat save debugging-auth
```

This saves your **entire conversation state** (all messages, context, variables) with the tag `debugging-auth`.

### Resume Conversation: `/chat resume`

```
/chat resume debugging-auth
```

This **restores** the exact conversation you saved. The 2 hours of debugging context comes back, exactly as you left it.

### List Saved Conversations: `/chat list`

```
/chat list
```

**Output**:
```
Saved conversations:
- debugging-auth (saved 2025-01-14 10:30)
- refactoring-api (saved 2025-01-14 09:15)
- planning-feature-x (saved 2025-01-13 16:45)
```

### Delete Conversation: `/chat delete`

```
/chat delete debugging-auth
```

Removes the saved conversation permanently.

### Practical Workflow

1. **Start Task A** (debugging authentication)
   ```
   /chat save debugging-auth
   ```

2. **Urgent Task B arrives** (API docs review)
   - Save Task A
   - Start fresh conversation for Task B

3. **Review API docs** (without pollution from Task A)

4. **Finish Task B**

5. **Back to Task A** with full context restored
   ```
   /chat resume debugging-auth
   ```

6. **Continue debugging** as if you never left

This workflow lets you handle interruptions without losing complex context.

---

## Part 5: Memory Management Commands

Now that you understand GEMINI.md files, here are commands to manage them:

### Show Current Memory: `/memory show`

```
/memory show
```

Displays all loaded `GEMINI.md` content (in hierarchy order).

### Refresh Memory: `/memory refresh`

```
/memory refresh
```

Reloads all `GEMINI.md` files from disk. **Use this** if you edited GEMINI.md outside Gemini CLI and want the changes reflected.

### Add to Memory: `/memory add`

```
/memory add "Team convention: Always use snake_case for database column names"
```

Appends text to the **project-level GEMINI.md** (if you're in a project) or **user-level GEMINI.md** (if global).

### SaveMemory Tool (Automatic)

Gemini CLI can automatically save important facts to memory. When AI detects key information worth persisting, it shows:

```
Saved to memory: "Database schema uses UUID primary keys"
```

This is **automatic** (AI-triggered), unlike `/memory add` which is **manual** (you triggered).

### Memory vs Context

| Type | Lifetime | Storage | Purpose |
|------|----------|---------|---------|
| **Context** | Single session | RAM | Short-term conversation |
| **Memory** | Persistent | GEMINI.md files | Long-term facts |

---

## Red Flags to Watch

### "Context window exceeded"
- You've hit the 1M token limit
- Use `/compress` to summarize conversation
- Or use `/clear` for fresh start
- Save important notes before clearing

### Slow responses after long conversation
- Context is getting full
- Use `/compress` to free tokens
- Or save with `/chat save` and start fresh

### GEMINI.md changes not appearing
- Run `/memory refresh` to reload from disk
- Check file path is correct
- Verify GEMINI.md format is valid Markdown

### Lost conversation after closing terminal
- Always use `/chat save tag-name` before closing
- Without saving, conversation is lost when you quit
- `.env` files and GEMINI.md persist; conversation history doesn't

---

## Try With AI

### Prompt 1: Context Management Strategy
```
I'm working on a large project in Gemini CLI. My conversations are getting long,
and I'm worried about hitting the token limit.

Should I use /clear, /compress, or /chat save? Show me:
1. When to use each command
2. What you preserve vs lose with each
3. A daily workflow strategy for keeping context under control
```

**Expected outcome**: Clear decision framework for context management.

### Prompt 2: GEMINI.md Setup for Your Project
```
Help me create a project-level GEMINI.md for a [describe your project type].
Include:
- Team conventions
- Architecture overview
- Common setup/commands
- Key design decisions
- Anything else AI should know on session start

Keep it concise (target: 2000 tokens max).
```

**Expected outcome**: Ready-to-use GEMINI.md you can create in your project.

### Prompt 3: Multi-Task Workflow
```
I work on multiple projects in Gemini CLI, and I get interrupted a lot.
Design a workflow using /chat save and /chat resume that lets me:
1. Save work on Project A
2. Switch to Project B for urgent task
3. Return to Project A with full context
4. Not lose important decisions

Show me the exact commands and naming strategy.
```

**Expected outcome**: Practical multi-task workflow you can implement.

### Prompt 4: When to Use GEMINI.md vs /chat save
```
For each scenario, tell me whether to use GEMINI.md, /chat save, or neither:
1. Team coding standards that don't change
2. Today's debugging progress
3. Architecture decisions made months ago
4. Temporary notes for this session

Explain the reasoning for each.
```

**Expected outcome**: Decision framework for choosing persistence method.

