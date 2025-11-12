---
sidebar_position: 3
title: "Core Commands, Custom Commands & Workflows"
duration: "40 min"
---

# Core Commands, Custom Commands & Workflows

## Specification Verbs: Your Language for Intent

You've learned what Claude Code is (Lesson 1: an agentic AI partner) and how to establish a working partnership (Lesson 2: checkpoints, files, memory). Now comes the crucial step: **learning to articulate what you want with precision**.

Think of commands not as "features to memorize," but as **verbs in a specification language**. Just as a software specification uses clear action verbs ("retrieve user data," "validate email format," "generate report"), Claude Code commands express distinct intents:

- **`claude`** = "I need help with this task"
- **`#`** = "This is a checkpoint—verify progress here"
- **`@filename`** = "Include this file as context"
- **`/init`** = "Remember my project setup"
- **`/clear`** = "Start fresh—forget previous context"

**This is the paradigm shift** (Principle 3 from the Constitution): Your value isn't memorizing command syntax. Your value is **articulating intent clearly** so AI executes it precisely.

In Lesson 1, you learned about agentic execution. In Lesson 2, you discovered checkpoints structure conversations. Now in Lesson 3, you'll learn to **combine commands into workflows**—specifications for how work gets done.

By the end of this lesson, you'll:
- Recognize commands as "specification verbs" (not just features)
- Use checkpoints as "specification milestones" (not just pauses)
- Build decision trees that match task complexity to the right approach
- Create reusable custom commands (encoding your workflows as specifications)
- Understand the progression from simple commands → custom commands → subagents → orchestration (coming in Lessons 4-8)

---

## Command Reference Table: Your Specification Vocabulary

Each command expresses a distinct specification intent. Use this table as a reference—don't memorize. The real skill is knowing **when to use which intent**, not memorizing syntax.

| Command | Purpose | Specification Intent | Example |
|---------|---------|----------------------|---------|
| **`claude`** | Start a session | "I need help with this task" | `claude` or `claude "your prompt"` |
| **`#`** | Save a milestone | "This step is complete; next phase begins here" | `# Fixed the login bug` |
| **`@filename`** | Include context | "Consider this file when you respond" | `@app.py what does this function do?` |
| **`/init`** | Remember project | "Store my project context for future sessions" | `/init` |
| **`/clear`** | Forget context | "End this task; start completely fresh" | `/clear` |
| **`/compact`** | Summarize progress | "Condense our conversation to save tokens" | `/compact` |
| **`ESC`** | Stop (graceful) | "Finish your thought and stop generation" | Press `ESC` once |
| **`ESC ESC`** | Stop (force) | "Stop immediately; no gradual shutdown" | Press `ESC` twice quickly |
| **`/mcp`** | Check tools | "Show which external tools are configured" | `/mcp` |
| **`/usage`** | Check budget | "Show my remaining API usage" | `/usage` |
| **`/permissions`** | Set boundaries | "Define what I allow Claude to do" | `/permissions` |

---

## 💬 AI Colearning Prompt: Map Your Work to Commands

Now that you've seen the specification vocabulary, let's make it personal.

### Your Task
Open Claude Code (or ChatGPT) and run this prompt:

> **"I typically work on [describe your domain: web features, data pipelines, API integrations, mobile apps, system administration, etc.]. Looking at the command reference table above, which 3-4 commands would I use MOST OFTEN in MY workflow? For each one, give me a realistic example from my domain showing WHAT I'd specify (not HOW I'd code it). Then tell me: which commands might I barely use? Why?**

### What This Does
Instead of learning commands abstractly, you'll map them to YOUR work patterns. This is core to specification thinking: you learn the vocabulary in context, not in isolation.

### Expected Output
Claude should return:
- Your top 3-4 commands (specific to your domain)
- Realistic examples from your domain showing WHAT you'd specify
- Clear explanation of why you'd use each command
- Commands you might skip (and why—not all commands fit all workflows)

### What You Learn
**You'll discover that specification thinking is domain-specific.** A data engineer's command workflow differs from a web developer's, which differs from a DevOps engineer's. The VOCABULARY is universal; the USAGE is personal.

---

## When to Use Which Approach: Decision Tree for Command Selection

As you encounter tasks, you'll face a question: "Which approach should I use?" Here's how to decide:

```
Task arrives
    ↓
Single-step task? (e.g., "Read this file" or "Explain this error")
    ├─ YES → Use basic command: claude "..."
    │
    └─ NO
        ↓
Multi-step task with clear phases? (e.g., "Design → Implement → Test")
        ├─ YES → Use checkpoints (#)
        │        Structure: # Phase 1 description # Phase 2 description
        │
        └─ NO
            ↓
Multi-file task needing consistent context? (e.g., "Review auth flow across multiple files")
            ├─ YES → Use @filename references
            │        Example: @login.py @auth.py @db.py compare authentication
            │
            └─ NO
                ↓
Repetitive workflow you'll do many times? (e.g., "Deploy to staging," "Run tests + lint")
                ├─ YES → Create custom command (/slash-command)
                │        Encode workflow once, reuse by name
                │
                └─ NO
                    ↓
Specialized, isolated task needing own context? (e.g., "Code review with specific guidelines")
                    ├─ YES → Use subagent (Lesson 4)
                    │        Separate context, specialized tools
                    │
                    └─ NO
                        ↓
10+ similar items? Complex orchestration? (e.g., "Set up 10 microservices")
                        ├─ YES → Use AI orchestration (Lesson 8)
                        │
                        └─ NO → Start simple; refine approach as pattern emerges
```

**Decision Rule**: Start simple. If you find yourself specifying the same multi-step intent repeatedly, that's a signal to create a custom command.

---

## Core Commands (Explained)

### 1. `claude` - Start a Conversation

**Purpose**: The main command to interact with Claude Code

**Syntax**:
```bash
claude                           # Start interactive conversation
claude "your prompt here"        # One-off request
```

**When to use**:
- Starting a new task
- Asking a question
- Getting help with an error

**Example**:
```bash
claude "Review the authentication logic in auth.py and suggest improvements"
```

**What happens**: Claude reads the file, analyzes the logic, and provides specific suggestions

**Specification Mindset**: When you start a conversation, you're not "using a tool"—you're briefing a co-worker. Think: "What outcome do I want?" not "What commands should I type?" Claude Code's agentic architecture (from Lesson 1) means you specify intent, and AI determines execution.

---

### 2. `#` - Create Checkpoints

**Purpose**: Mark verifiable progress points in multi-step work

**Syntax**:
```bash
# Your checkpoint message here
```

**When to use**:
- After completing a subtask
- Before starting a new feature
- To organize multi-step work

**Example**:
```bash
# Fixed the login bug
# Now working on password reset
```

**Why it matters**: Checkpoints help Claude (and you) track what's done vs. what's next. In long conversations, they prevent Claude from losing context.

---

### 3. `@filename` - Reference Files

**Purpose**: Tell Claude to look at a specific file

**Syntax**:
```bash
@filename.ext your question
```

**When to use**:
- Asking about a specific file
- Comparing multiple files
- Getting file-specific help

**Example**:
```bash
@models.py @views.py how do these two files interact?
```

**What happens**: Claude reads both files and explains their relationship

---

### 4. `/init` - Set Up Project Memory

**Purpose**: Initialize Claude Code for your project (creates CLAUDE.md)

**Syntax**:
```bash
/init
```

**When to use**:
- First time using Claude Code in a project
- When you want Claude to remember project context

**What it does**:
1. Asks about your project (name, language, purpose)
2. Creates CLAUDE.md with your answers
3. Claude reads this file in future sessions

**Time saved**: 2-5 minutes per session (no more repeating project context)

---

### 5. `/clear` - Start Fresh

**Purpose**: End current conversation, clear context

**Syntax**:
```bash
/clear
```

**When to use**:
- Switching to a completely different task
- Current conversation is getting confusing
- Want to start over without previous context

**Example scenario**:
```bash
# Working on feature A
claude "Help me with authentication"
# ... conversation ...

/clear

# Now working on feature B
claude "Help me with database migration"
```

**What gets cleared**: Conversation history, file references
**What stays**: Your project (files), CLAUDE.md

---

### 6. `/compact` - Summarize Conversation

**Purpose**: Condense long conversation to save tokens

**Syntax**:
```bash
/compact
```

**When to use**:
- Long conversation approaching token limit
- Want to keep context but reduce size
- Conversation has lots of back-and-forth

**What it does**:
- Claude summarizes the conversation
- Keeps key decisions and progress
- Removes redundant exchanges

**vs. `/clear`**: `/compact` keeps context (summarized), `/clear` removes all context

---

### 7. `ESC` and `ESC ESC` - Stop Generation

**Purpose**: Interrupt Claude when it's generating

**When to use**:
- Claude is generating too much detail
- Going in wrong direction
- Just want it to stop

**ESC (once)**: Polite stop - Claude finishes current thought and stops
**ESC ESC (twice)**: Force quit - immediate stop

**Example**:
```bash
claude "Explain dependency injection in detail"
# Claude starts generating paragraphs...
# Press ESC - Claude stops gracefully
```

---

### 8. `/mcp` - Check MCP Server Status

**Purpose**: Display configured MCP servers (external tools)

**Syntax**:
```bash
/mcp                              # Show MCP server status
/mcp reconnect <server-name>     # Reconnect to a specific server
```

**When to use**:
- Check which MCP servers are configured
- Verify MCP servers are connected
- Troubleshoot MCP server connections

**Example**:
```bash
/mcp
```

**Example Output (no servers configured)**:
```
No MCP servers configured. Please run /doctor if this is unexpected.
Otherwise, run `claude mcp` or visit https://docs.claude.com/en/docs/claude-code/mcp
to learn more.
```

**Example Output (servers configured)**:
```
MCP Servers:
- web-search: ✓ Connected
- github: ✓ Connected
- docs: ✗ Disconnected
```

**Note**: To configure MCP servers, use `claude mcp` command or edit your configuration files. This is covered in detail in Lesson 6.

---

### 9. `/usage` - Check API Usage (Budget Awareness)

**Purpose**: Show plan usage limits

**Syntax**:
```bash
/usage    # Check current usage
```

**When to use**:
- Before starting large tasks
- When approaching daily/weekly limits
- To understand usage patterns

**Example Output**:
```
Settings:  Status   Config   Usage   (tab to cycle)

 Current session
 ███                                                6% used
 Resets 2pm (Asia/Karachi)

 Current week (all models)
 ███████████                                        22% used
 Resets Nov 12, 10pm (Asia/Karachi)

 Current week (Opus)
                                                    0% used

 Esc to exit
```

**Best practice**: Check `/usage` often to prevent unexpected session limit reached problems.

---

### 10. `/permissions` - Control Access (Security)

**Purpose**: Set what Claude Code can access and do

**Syntax**:
```bash
/permissions                      # Show current permissions
/permissions set <permission>    # Change a permission
```

**When to use**:
- First time setting up (define boundaries)
- Working with sensitive files
- Want to restrict Claude's actions

**Example**:
```bash
/permissions
```

**Example Output**:
```
Current permissions:
- Read files: ✓ Allowed
- Write files: ✓ Allowed (approval required)
- Execute commands: ✓ Allowed (approval required)
- Access network: ✗ Denied
```

**Best practice**: Review permissions when starting work on a new project or when handling sensitive data.

---

## 🎓 Expert Insight: Checkpoints as Specification Markers

In Lesson 1, you learned that Claude Code is agentic—it automatically breaks down your intent. In Lesson 2, you learned to create checkpoints. But there's a strategic insight here worth highlighting:

**Checkpoints aren't just pauses. They're specification boundaries.**

Think about software specifications. A professional spec has:
- **Goals** (what we're building)
- **Constraints** (what we can't do)
- **Acceptance criteria** (how we verify success)
- **Milestones** (verifiable points of completion)

When you write:
```
# Read user data from database
# Validate schema against requirements
# Generate performance report
```

You're not writing prose. You're writing **verifiable milestones**. Each checkpoint is a specification stating: "When we reach this point, this outcome should be verified."

This is Spec-First thinking in action (Constitution Principle 3). You specify outcomes; AI executes. You verify at checkpoints; AI adapts if verification fails.

**Example: Real-world checkpoint verification**

```
# Read user data
→ Check: Is user data successfully read? (JSON valid? Fields present?)

# Validate schema
→ Check: Do all records match the expected schema? (Type correct? Required fields present?)

# Generate report
→ Check: Is report generated? (File created? Content sensible? Format correct?)
```

When you think of checkpoints as specification milestones, you naturally ask: "What needs to be true at this point for us to proceed?" That's professional specification thinking.

---

## 🤝 Practice Exercise: Write Specifications, Not Commands

Here's the core skill we're building: **Writing clear specifications that let AI execute precisely.**

### Your Task

1. **Choose a task you do regularly** (bug fix, code review, feature addition, API integration, database query, etc.)

2. **Write 3 sentences describing WHAT you want** (outcome), not HOW to do it (steps)
   - Bad: "Use grep to find all error logs, then count them, then sort by date"
   - Good: "I need a summary of errors from yesterday—count by type, sorted newest first"

3. **If your task has multiple phases**, use checkpoints to structure it:
   ```
   # Phase 1: Gather data
   # Phase 2: Validate and clean
   # Phase 3: Generate insights
   ```

4. **Give this specification to Claude Code** and observe what it proposes
   - Does Claude's approach match your initial mental "how"?
   - Did Claude suggest something you hadn't thought of?
   - Did Claude ask clarifying questions?

5. **Reflect**:
   - What did you learn from Claude's approach?
   - Did your specification lack detail? (What was unclear?)
   - How would you refine the specification for next time?

### Expected Outcome

You'll practice the PRIMARY skill of AI-native development: articulating intent clearly so AI executes it precisely.

---

## Custom Slash Commands (Team Workflow Automation)

### What Are Custom Slash Commands?

Custom slash commands are **reusable prompt templates** you create for tasks you do repeatedly. They encode your workflows as specifications—once you describe the workflow, you invoke it by name.

**Think of them as**: Shortcuts for common workflows, but more importantly, **specifications made executable and repeatable**

**Stored in**: `.claude/commands/` directory in your project

---

### Why Custom Commands Are Strategic

When you find yourself specifying the same multi-step workflow repeatedly, you've discovered a **specification pattern**. Custom commands let you encode that pattern once.

**Strategic Value**:
- **Efficiency**: `/deploy` vs. typing 12-step specification each time
- **Consistency**: Team uses same specification (no variation in deployment steps)
- **Organizational Knowledge**: YOUR workflows become executable specifications
- **Tier 2 Teaching**: This exemplifies Principle 13 (Graduated Teaching): AI Companion handles complexity after you specify the pattern once

**Remember**: The command name is still a specification—it says WHAT (/deploy), not HOW (build, test, upload, notify, etc.)

---

### How to Create a Custom Command

**Step 1: Create the commands directory**

```bash
mkdir -p .claude/commands
```

**Step 2: Create a markdown file for your command**

Example: `.claude/commands/markdown-review.md`

```markdown
# Markdown Review Command

Review the Markdown in $ARGUMENTS for:
1. Potential bugs or edge cases
2. Style and readability
3. Security vulnerabilities

Provide:
- Summary of findings (critical/major/minor)
- Specific line numbers for issues
- Suggested fixes with examples

Format: Use a clear severity rating for each issue.
```

**Step 3: Use your custom command**

```bash
claude /markdown-review >> We are learning how to Create a custom command
```

**What happens**:
- `$ARGUMENTS` gets replaced with `>> We are learning how to Create a custom command`
- Claude executes the full prompt template
- You get consistent, structured reviews

---

### 🎓 Expert Insight: From Commands to Ecosystem

You're learning the foundation now, but here's the bigger picture:

**Commands are Tier 1 of a composable ecosystem:**

- **Commands** (Lesson 3): Book teaches foundational vocabulary → You combine them into workflows
- **Checkpoints** (Lesson 2): Structure multi-step intent → AI executes with clarity
- **Custom Commands** (this lesson): Encode repetitive workflows → Team reuses by name
- **Subagents** (Lesson 4): Isolated contexts → Specialized tools for complex tasks
- **Skills** (Lesson 5): Discoverable capabilities → AI finds when to help automatically
- **Hooks** (Lesson 7): Event-driven automation → Systems react without human invocation
- **Plugins** (Lesson 8): Full orchestration → Entire workflows automated

You're learning the vocabulary now (Tier 1); upcoming lessons show how to compose it (Tier 2) and orchestrate it (Tier 3). This progression mirrors specification maturity: simple → structured → automated → orchestrated.

---

## 🤝 Practice Exercise: Create Your First Custom Command

Now let's build a reusable workflow specification.

### Your Task

1. **Identify a 3-5 step workflow you repeat often**
   - Examples: git commit flow, test+build, documentation generation, API integration setup, database backup procedure

2. **Write the specification in plain language first**:
   ```markdown
   What: [One-line description of workflow]
   Outcome: [What success looks like]
   Steps:
   # Check [initial state]
   # Review [decision point]
   # Suggest [collaborative point]
   # Execute [final action]
   ```

3. **Convert to custom command** following the lesson walkthrough above
   - Create `.claude/commands/your-command-name.md`
   - Include 3-5 clear instructions
   - Use `$ARGUMENTS` for variable input

4. **Test it**: Does `/your-command` execute your specification correctly?
   - Run the command
   - Verify output matches your intention
   - Note what Claude understood vs. misunderstood

5. **Reflect**:
   - How does having a reusable specification change your workflow?
   - What detail was missing from your initial specification? (Did Claude ask clarifying questions?)
   - Would a teammate understand and use this command correctly?

### Expected Outcome

You'll have a working custom command that encodes YOUR workflow as a reusable specification.

---

## Try With AI

Use Claude Code CLI (or ChatGPT) for this activity. These prompts demonstrate the **Three Roles Framework**: AI as Teacher, Student, and Co-Worker.

### Prompt 1: AI as Teacher (Suggests Patterns)

```
I work on [your domain]. Teach me 3 specification patterns I should master
for common tasks in this domain. For each pattern, show me:
(1) the specification structure using checkpoints,
(2) an example prompt,
(3) why this pattern is reusable and when to use it.
```

**Expected outcome**: Claude suggests domain-specific specification patterns you may not have considered. You learn from Claude's expertise.

---

### Prompt 2: AI as Student (Learns Your Style)

```
Here's how I typically specify work: [paste 2-3 examples of how you
describe tasks to Claude]. Analyze my specification style. What's clear?
What could be more specific? What detail do I always forget? Suggest 2-3
improvements to make MY specifications more effective.
```

**Expected outcome**: Claude learns your communication style and offers personalized improvements. You teach Claude how you think.

---

### Prompt 3: AI as Co-Worker (Collaborative Refinement)

```
# Read the authentication code in /src/auth
# Identify error handling gaps and security issues
# Propose 3 improvements with code examples
# Explain tradeoffs of each approach

Execute this specification step-by-step. Pause at each checkpoint for my
feedback before proceeding to the next step. This helps me verify each
phase.
```

**Expected outcome**: Claude executes from your specification, pausing at each checkpoint. You iterate together—AI executes, you verify, AI adapts. This is true co-learning.

---

### Reflection Prompt (After All Three)

```
Thinking about these three interactions:
- Prompt 1: Where did you learn something from Claude?
- Prompt 2: Where did Claude learn something about you?
- Prompt 3: Where did you and Claude refine each other's thinking?

This is the convergence pattern: bidirectional learning. How did this
experience differ from just asking Claude to "write code"?
```

**Expected outcome**: You recognize that the primary skill isn't coding—it's clear specification and iterative refinement.

---

## Key Takeaway

Commands are your **specification vocabulary**. Checkpoints are your **specification structure**. Custom commands are your **specification library**. Together, they embody the core principle: **Specs Are the New Syntax**.

Your value in AI-native development isn't memorizing command syntax. Your value is articulating intent so clearly that AI executes it precisely, and then knowing how to refine through iteration. Every lesson from here forward teaches you deeper ways to compose specifications—from custom commands, to subagents, to orchestration.

You're building the "new syntax" now.
