---
sidebar_position: 3
title: "Core Commands & Slash Commands"
duration: "40 min"
---

# Core Commands & Slash Commands

## From Setup to Daily Use: Mastering Gemini CLI Commands

In Lesson 2, you installed Gemini CLI and saw it work for the first time. Now comes the crucial step: **learning to write specifications that direct your AI development partner**.

This isn't about memorizing command syntax. It's about understanding the three **specification patterns** Gemini CLI recognizes, when to use each pattern, why it matters, and how to collaborate with your AI partner like a professional.

---

## Understanding Gemini CLI's Three Specification Patterns

Gemini CLI recognizes three ways to **specify** what you want your AI to do:

**1. Session Specifications (/)** — How you want your AI session to behave
- Specification type: Session state management
- Examples: `/memory add <context>`, `/chat save <tag>`, `/compress`
- Mental model: "I need my AI session to behave THIS way"
- **What you're learning**: How to specify session architecture for your work

**2. Context Specifications (@)** — What information your AI needs
- Specification type: Context architecture definition
- Examples: `@./src/auth.ts`, `@./docs/`
- Mental model: "Here's the context scope for this conversation"
- **What you're learning**: How to specify context boundaries

**3. Execution Specifications (!)** — What system operations to perform
- Specification type: System command delegation to AI
- Examples: `!git status`, `!npm test`
- Mental model: "Execute this operation and help me interpret results"
- **What you're learning**: How to specify system operations for AI guidance

Let's dive into each pattern and see how to use them in real work.

---

## Slash Commands: The Complete Reference

Gemini CLI provides 29+ slash commands. Here are the essential ones you'll use daily:

### Conversation Management

| Command | Purpose | Example |
|---------|---------|---------|
| **`/chat save <tag>`** | Save current conversation | `/chat save auth-implementation` |
| **`/chat resume <tag>`** | Restore saved conversation | `/chat resume auth-implementation` |
| **`/chat list`** | List saved conversations | `/chat list` |
| **`/chat delete <tag>`** | Remove saved conversation | `/chat delete auth-implementation` |
| **`/chat share file.md`** | Export conversation to file | `/chat share output.md` |
| **`/clear`** | Clear terminal display | `/clear` |

### Context & Memory Management

| Command | Purpose | Example |
|---------|---------|---------|
| **`/memory add <text>`** | Add to AI's context | `/memory add we use TypeScript strict mode` |
| **`/memory show`** | Display loaded context | `/memory show` |
| **`/memory refresh`** | Reload GEMINI.md files | `/memory refresh` |
| **`/memory list`** | Show active GEMINI.md paths | `/memory list` |
| **`/directory add <path>`** | Add workspace directory | `/directory add ./shared-libs` |
| **`/directory show`** | Show workspace directories | `/directory show` |

### System & Configuration

| Command | Purpose | Example |
|---------|---------|---------|
| **`/settings`** | Open settings editor | `/settings` |
| **`/theme`** | Change terminal theme | `/theme` |
| **`/vim`** | Toggle vim-mode editing | `/vim` |
| **`/editor`** | Select default editor | `/editor` |
| **`/auth`** | Change authentication | `/auth` |
| **`/help` or `/?`** | Show help | `/help` |
| **`/about`** | Show version info | `/about` |

### Tools & Integrations

| Command | Purpose | Example |
|---------|---------|---------|
| **`/tools [desc]`** | List available tools | `/tools` or `/tools read file` |
| **`/mcp`** | Show MCP servers & tools | `/mcp` |
| **`/extensions`** | List active extensions | `/extensions` |

### Optimization & Restoration

| Command | Purpose | Example |
|---------|---------|---------|
| **`/stats`** | Show token usage | `/stats` |
| **`/compress`** | Reduce context size | `/compress` |
| **`/copy`** | Copy last response | `/copy` |
| **`/restore [id]`** | Undo file modifications | `/restore` |

### Utility

| Command | Purpose | Example |
|---------|---------|---------|
| **`/bug`** | Report issue | `/bug command X doesn't work` |
| **`/privacy`** | View privacy notice | `/privacy` |
| **`/quit` or `/exit`** | Exit Gemini CLI | `/quit` |
| **`/init`** | Create GEMINI.md | `/init` |

---

## Deep Dive: Commands You'll Use Most

### 1. `/chat save` & `/chat resume` — Conversation Checkpointing

**Purpose**: Specify when to save conversation checkpoints and resume work without re-explaining context

**Syntax**:
```bash
/chat save my-project-v1
(Later, in new session...)
/chat resume my-project-v1
```

**When to use**:
- After completing a meaningful chunk of work
- Before starting something unrelated
- End of day (save progress)
- Beginning of day (resume work)

**Example Workflow**:
```
You: [Work on authentication for 2 hours]

You: /chat save auth-endpoints-complete
Gemini: ✓ Saved conversation as "auth-endpoints-complete"

(Later, next day...)

You: /chat resume auth-endpoints-complete
Gemini: ✓ Resumed conversation "auth-endpoints-complete"
        [Shows your conversation history]

You: Now let's add password reset functionality
(Continues seamlessly from yesterday)
```

**Working WITH Your AI on Session Management**

🎓 **AI as Teacher**: Learning when to checkpoint
```
You: I've been working for 2 hours on authentication. Should I save now or wait?

Gemini: "You've completed the login endpoint with tests. This is a natural checkpoint
before starting password reset functionality. I recommend:
  /chat save auth-login-complete

This helps you resume at a logical breakpoint tomorrow."
```

💙 **AI as Student**: Learning your workflow patterns
```
You: I prefer saving every hour with tags like YYYY-MM-DD-HHMM.
Adapt to this pattern and remind me when it's been an hour.

Gemini: "I'll track time and suggest hourly saves with timestamp tags.
When it's been 60 minutes, I'll remind you: 'Ready to checkpoint?'"
```

🤝 **AI as Co-Worker**: Collaborative session management
```
You: Help me organize my saved conversations. List them, suggest which ones
to delete (old or completed), and help me create a naming convention.

Gemini: [Lists 12 saved conversations, suggests cleanup, proposes naming system]
```

**Why it matters**: Without saved conversations, you'd need to re-explain your project every session. With `/chat save/resume`, context persists. More importantly, you learn to think about work in **checkpoints and phases**—a specification-first mindset.

---

### 2. `/memory add`, `/memory show`, `/memory refresh` — Context Management

**Purpose**: Manage AI's long-term knowledge about your project

These commands work with **GEMINI.md files** (covered in Lesson 4).

**Syntax**:
```bash
/memory add we use strict TypeScript and functional patterns
/memory show          # Shows all loaded context
/memory refresh       # Reloads GEMINI.md files
/memory list          # Shows which GEMINI.md files are loaded
```

**How it works**:
1. Gemini CLI looks for GEMINI.md files (global, project, subdirectory)
2. `/memory show` displays what's currently loaded
3. `/memory refresh` reloads if you update GEMINI.md
4. `/memory add` adds temporary facts to the session

**Example**:
```
You: /memory show
Gemini CLI:
  Loaded from: ~/.gemini/GEMINI.md
  - My preferences (Python + TypeScript)
  - My coding style

  Loaded from: ./GEMINI.md
  - Project architecture
  - Team standards

You: /memory add API returns ISO 8601 dates
Gemini: ✓ Added to context
```

---

### 3. `/stats` — Token Budget Awareness

**Purpose**: Monitor how many tokens you've used

**Syntax**:
```bash
/stats
```

**Output**:
```
Session Statistics:
- Tokens used: 125,000 / 1,000,000
- Remaining: 875,000
- Session duration: 2h 45m
- Messages: 42
```

**Why it matters**: Gemini CLI has a 1 million token context window. Long sessions can approach the limit. `/stats` tells you when to start a new conversation or use `/compress`.

---

### 4. `/compress` — Reduce Context Size

**Purpose**: Specify that you want to compress context while preserving critical project decisions

**Syntax**:
```bash
/compress
```

**What happens**:
- Gemini replaces your conversation with a summary
- Frees up 40-60% of tokens
- Keeps key decisions and code context

**Example**:
```
You: [After 3 hours of work, 250K tokens used]
You: /stats
Gemini: Used 250,000 / 1,000,000 tokens

You: /compress
Gemini: ✓ Compressed conversation. Now using 90,000 tokens
        (Freed 160,000 tokens for continued work)
```

**Validating Compression Results**

After compression, **always validate** that important context was preserved:

```bash
You: /stats
Gemini: Used 90,000 / 1,000,000 tokens (tokens freed: 160K ✓)

You: What key decisions and constraints did you preserve from our
     compressed conversation? List the major architecture choices
     and requirements you remember.

Gemini: [Lists preserved decisions]
```

**Red Flags to Watch** 🚩:
- ❌ Can't recall specific code decisions made earlier
- ❌ Forgets project constraints you specified
- ❌ Loses track of completed work items
- ✅ Remembers architecture choices, requirements, and design patterns

**Recovery**: If validation fails, use `/chat resume` to restore the pre-compression state and save before trying `/compress` again.

---

### 5. `/clear` — Start Fresh

**Purpose**: End current conversation and start new one

**Syntax**:
```bash
/clear
```

**Important**: Use `/chat save` before `/clear` if you want to preserve work.

```bash
You: /chat save current-work
Gemini: ✓ Saved

You: /clear
Gemini: ✓ Conversation cleared

You: [Starting completely new task with fresh context]
```

---

### 6. `/tools` — Discover Available Tools

**Purpose**: See what tools Gemini can use

**Syntax**:
```bash
/tools                # List all tools
/tools search         # Filter tools by keyword
```

**Output**:
```
Available Tools:
- GoogleSearch — Search the web
- WriteFile — Create/modify files
- ReadFile — Read file contents
- WebFetch — Fetch URL content
- RunShell — Execute shell commands
```

---

### 7. `/mcp` — Manage External Integrations

**Purpose**: List configured MCP servers and their tools

**Syntax**:
```bash
/mcp
```

**Output**:
```
Configured MCP Servers:
- playwright (✓ connected) — Web browsing
- context7 (✓ connected) — Documentation lookup
- github (✓ connected) — Repository access
```

---

### 8. `/directory add` & `/directory show` — Workspace Management

**Purpose**: Include additional directories in Gemini's context discovery

**Syntax**:
```bash
/directory add ../shared-libs        # Add a directory
/directory show                      # See all included directories
```

**Why useful**: If you work with monorepos or shared libraries, tell Gemini where to find them.

---

## At Commands: Including Files & Directories

### `@` Syntax for File References

**Purpose**: Include file or directory content in your prompt

**Syntax**:
```bash
@path/to/file.js                # Single file
@./src/                         # Entire directory
@./docs/                        # Read all files in directory
@image.png                      # Image file
@document.pdf                   # PDF file
```

**Examples**:
```bash
You: @./src/auth.ts explain this authentication flow

You: @./docs/ summarize the project documentation

You: Compare @./old-design.ts and @./new-design.ts

You: Read @./config.json and tell me the API endpoint
```

**Smart Filtering**: Gemini CLI automatically excludes:
- `node_modules/`
- `.env` files
- `.git/` directories
- Other common non-code files

---

## Shell Commands: System Access

### `!` Syntax for Shell Execution

**Purpose**: Run system commands with AI guidance

**Syntax**:
```bash
!<command>              # Run single command
!                       # Toggle shell mode
```

**Examples**:
```bash
You: !git status
Gemini: [Executes command, shows output, can discuss results]

You: !
Gemini: [Enters shell mode - all commands execute without !]
$ npm test
$ git log --oneline
$ exit                  # Exit shell mode back to chat
```

**Safety**: Gemini can warn you about dangerous commands before executing.

---

## Keyboard Shortcuts

Quick actions while typing:

| Shortcut | Action |
|----------|--------|
| `Ctrl+L` | Clear terminal (same as `/clear`) |
| `Ctrl+Z` | Undo last input |
| `Ctrl+Shift+Z` | Redo undone input |

---

## Practical Daily Workflow

Here's how these commands flow in real work:

### Morning: Resume Previous Work

```bash
$ gemini
Gemini: Loading context from ~/.gemini/GEMINI.md and ./GEMINI.md

You: /chat resume api-endpoints-in-progress
Gemini: ✓ Resuming conversation
        (Shows your conversation history from yesterday)

You: Let's continue with the user endpoints
(Continues exactly where you left off)
```

### Mid-Day: Monitor Budget

```bash
You: [After 2 hours of work]

You: /stats
Gemini: Used 200,000 / 1,000,000 tokens remaining

You: We're in good shape, let's keep going
```

### Switch Projects

```bash
You: /chat save api-endpoints-complete
Gemini: ✓ Saved

You: /clear
Gemini: ✓ Fresh conversation started

You: /chat resume frontend-redesign
Gemini: ✓ Resuming previous project
```

### End of Day: Save Progress

```bash
You: /chat save current-work-session
Gemini: ✓ Saved

You: Good progress today. See you tomorrow!
(Exit Gemini CLI)
```

### Next Day: Resume Seamlessly

```bash
$ gemini

You: /chat resume current-work-session
Gemini: ✓ Loaded. Where were we...
```

---

## Common Questions

**Q: What's the difference between `/chat save` and GEMINI.md?**

A:
- `/chat save` = Saves your CONVERSATION (what you discussed)
- `GEMINI.md` = Persistent PROJECT CONTEXT (what Gemini should know about your project)

Use both together:
- GEMINI.md tells Gemini about your architecture
- `/chat save` remembers what you've discussed this session

**Q: Can I use `/chat resume` to work with someone else's saved conversation?**

A: Not directly. Saved conversations are personal. But you can use `/chat share file.md` to export, then share the file.

**Q: If I use `/compress`, will I lose my conversation?**

A: No. It summarizes your conversation but keeps important decisions and context. You can still reference previous work.

**Q: What happens if I close Gemini without using `/chat save`?**

A: Your conversation is lost. Always save important work with `/chat save`.

**Q: Can I use shell commands safely?**

A: Yes. Gemini will warn you about dangerous commands (rm, sudo, etc.) before executing. Always read the warning before confirming.

---

## Specification-Driven Exercises

These exercises teach you to **think in specifications**, not just execute commands. You'll work WITH your AI partner to solve real problems.

### Exercise 1: Specify Your Session Management Strategy

**Specification Challenge**:

> You're starting a multi-day project with three distinct phases:
> - **Phase 1 (Research)**: Understanding the problem (2 hours)
> - **Phase 2 (Implementation)**: Building the solution (4 hours)
> - **Phase 3 (Testing)**: Validating the work (2 hours)
>
> Design a conversation management strategy. What should you specify about when to save, what to name conversations, and how to resume work?

**With Your AI Partner**:

1. **Collaborate**: Open Gemini CLI and ask your AI:
   ```
   I'm starting a project with research → implementation → testing phases.
   How should I design a conversation checkpointing strategy?
   What naming convention would help me find conversations weeks from now?
   ```

2. **Execute**: Implement your strategy using `/chat save` and `/chat resume` throughout your work

3. **Validate**: Test resuming conversations—verify that AI remembers context

**Success Criteria**:
- [ ] Can resume any conversation and AI remembers context
- [ ] Naming convention makes conversations discoverable
- [ ] Strategy scales to 5+ saved conversations
- [ ] You understand WHY you checkpoint at each phase

---

### Exercise 2: Design Your Context Architecture

**Specification Challenge**:

> You're working on a project with these directories:
> - `frontend/` — React components
> - `backend/` — Python API
> - `shared/` — Shared utilities
>
> Design a memory management specification. Which context belongs in global GEMINI.md vs. project GEMINI.md? How do you optimize for a 8-hour work session?

**With Your AI Partner**:

1. **Explore**: Open Gemini CLI and run:
   ```bash
   /memory show      # See what's currently loaded
   /memory list      # See which GEMINI.md files exist
   /stats            # Check current token usage
   ```

2. **Collaborate**: Ask your AI:
   ```
   My project has frontend/backend/shared. How should I organize
   GEMINI.md files to optimize context loading without redundancy?
   ```

3. **Validate**: Verify your context architecture:
   ```bash
   /memory refresh   # Reload after changes
   /stats            # Confirm token usage is optimized
   ```

**Success Criteria**:
- [ ] Context architecture prevents redundancy
- [ ] AI has access to all necessary project knowledge
- [ ] Token usage optimized for 8-hour work session
- [ ] You understand trade-offs between global vs. local GEMINI.md

---

### Exercise 3: Practice Validation: Token Budget Awareness

**Specification Challenge**:

> Monitor your token usage across a full work session. When should you use `/compress`? How do you validate that compression preserved important context?

**With Your AI Partner**:

1. **Start Monitoring**:
   ```bash
   You: /stats
   Gemini: Shows current token usage
   ```

2. **Work for 1 hour**, then check again:
   ```bash
   You: /stats
   Gemini: Shows new usage total
   ```

3. **When approaching 70% usage, compress**:
   ```bash
   You: /compress
   You: /stats     # Verify tokens freed
   ```

4. **Validate preservation**:
   ```bash
   You: List the 3 most important architectural decisions we discussed.
   Gemini: [Should list them accurately]
   ```

**Success Criteria**:
- [ ] You understand when to compress (around 70% of token budget)
- [ ] Compression successfully frees tokens
- [ ] Validation confirms important context preserved
- [ ] You can recover with `/chat resume` if validation fails

---

### Exercise 4: File Reference Practice

**Specification Challenge**:

> You have a JavaScript file. Specify that you want Gemini to analyze it, explain it, and identify potential improvements.

**Steps**:

1. Create a simple file in your project:
   ```bash
   cat > example.js << 'EOF'
   function greet(name) {
     if (name == "World") {
       console.log("Hello World!");
     } else {
       console.log("Hello " + name);
     }
   }
   greet("Alice");
   EOF
   ```

2. In Gemini CLI, specify what you want analyzed:
   ```
   @./example.js Can you:
   1. Explain what this code does
   2. Identify modernizations (ES6+)
   3. Suggest improvements
   ```

3. Compare with AI's improvements:
   ```
   @./example.js vs. @./example-modern.js
   What improvements did you suggest?
   ```

**Success Criteria**:
- [ ] You understand @ syntax for file reference
- [ ] AI reads and analyzes file content
- [ ] You can specify multiple analysis dimensions
- [ ] You see how @ syntax reduces copy-pasting

---

### Exercise 5: Shell Command Guidance Practice

**Specification Challenge**:

> You want to run a complex shell command, but you want your AI partner to explain the results and help you interpret what happened.

**Steps**:

1. In Gemini CLI, use ! to execute with explanation:
   ```bash
   You: !git log --oneline | head -5
   Gemini: [Shows output and explains what it means]
   ```

2. Ask for interpretation:
   ```bash
   You: Based on that output, when was the last breaking change?
   Gemini: [Analyzes commits to answer]
   ```

3. Ask for next steps:
   ```bash
   You: Should I create a release now? What would you recommend?
   Gemini: [Suggests based on commit history]
   ```

**Success Criteria**:
- [ ] You understand ! syntax for system commands
- [ ] You can interpret shell output with AI's help
- [ ] AI guides your decisions based on command results
- [ ] You work WITH AI on system operations, not just execute blindly

---

## Key Takeaways

- **Three specification patterns** (session, context, execution) are how you direct your AI partner
- **Spec-first thinking**: You're not memorizing command syntax—you're learning to specify what you want your session to be
- **Three-Role Partnership**: AI teaches you when to checkpoint, learns your workflow patterns, and collaborates on session design
- **Session Specifications (/)**: `/chat save/resume` for checkpointing, `/memory` for context management, `/stats`/`/compress` for budget awareness
- **Context Specifications (@)**: `@./file.js` and `@./directory/` to specify context scope without copy-pasting
- **Execution Specifications (!)**: `!git status` and shell mode to have AI guide system operations
- **Validation matters**: Always verify compression preserved important context, always validate that AI understood your specification
- **Commands are discoverable**—use `/help` when needed, but focus on the PATTERN, not memorizing 29 commands

**Most Important Learning**: When using these commands, you're not executing syntax—you're **specifying how your AI session should behave**. This is THE core skill of AI-native development.

Next lesson: You'll learn **GEMINI.md context files**, so you can specify your entire project architecture once and Gemini automatically understands it across all conversations.

