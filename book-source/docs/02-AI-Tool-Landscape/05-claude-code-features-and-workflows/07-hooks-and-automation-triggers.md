---
sidebar_position: 7
title: "Hooks: Automating Before & After Actions"
duration: "25 min"
learning_objectives:
  - "Identify repetitive tasks in your workflow that hooks could automate"
  - "Apply the Automation Thinking Pattern to choose appropriate hook types"
  - "Write hook specifications following Specification-First principles"
  - "Implement simple hooks using SessionStart, PreToolUse, and PostToolUse events"
  - "Explain how hooks represent Tier 2 delegation to your AI Co-Worker"
estimated_time: "25 minutes"
skills_taught:
  - "Hooks as Executable Specifications (CEFR: A2)"
  - "Automation Pattern Recognition (CEFR: A2)"
  - "Strategic Delegation Thinking (CEFR: B1)"
generation_metadata:
  generated_by: "claude-lesson-writer"
  source_spec: "021-audit-chapter5-claude-code/specs/lesson7-spec.md"
  created: "2025-01-12"
  last_modified: "2025-01-12"
  git_author: "Claude Code Agent"
  workflow: "enhanced-regeneration"
  version: "2.0.0-enhanced"
---

# Hooks: Automating Before & After Actions

## Your Tedious Tasks: The Automation Starting Point

Think about your typical development workflow. What do you check manually **every single time**?

- Before you commit code: *"Did I run the linter? Did I run tests? Are there console warnings?"*
- After you edit a file: *"This needs formatting. I need to check types."*
- When you start a project session: *"Let me check the git branch, verify dependencies are installed."*
- Before Claude makes changes: *"I should verify this is safe—no deleting important files."*

**These repetitive checks are tedious.** You know what to check. You know the order. You do it dozens of times a day. But every time, you do it manually.

**What if Claude Code proactively handled these checks?**

That's exactly what **hooks** do. In this lesson, you'll learn to specify automation rules once, and Claude Code enforces them automatically—forever. This is **Specification-Driven Automation** (Constitution Principle 3): You articulate the automation pattern (the "what" and "when"), Claude handles execution (the "how").

**Strategic value:** Hooks transform your AI Co-Worker from passive executor to proactive partner. You delegate routine validation to AI, freeing your attention for high-value decisions. This is Principle 13 (Graduated Teaching Pattern), Tier 2: You specify the quality gates once, Claude enforces them forever.

---

## Automation Thinking Pattern: Tedious → Hook Type → Matcher → Action

Before diving into hook types, let's learn to think in **automation patterns**. This four-step framework transforms any tedious task into a hook specification.

### Step 1: Identify Tedious

What do you check manually EVERY TIME? Examples:
- Git status before committing (verbose but important)
- Linting after editing Python files
- Type checking before pushing
- Verifying test suite passes before production deploy
- Checking for hardcoded secrets before commits
- Formatting code after edits
- Running dependency security scans
- Checking environment variables before session starts

**Key insight:** Anything you do repeatedly without thinking = candidate for automation.

### Step 2: Choose Hook Type (WHEN)

Different hooks fire at different moments. Match the moment to your task:

| Hook Type | Fires When | Best For |
|-----------|-----------|----------|
| **SessionStart** | Claude Code starts | Environment checks, setup validation |
| **PreToolUse** | BEFORE Claude uses a tool | Safety checks, prevention ("don't do X") |
| **PostToolUse** | AFTER Claude completes | Validation, follow-up checks ("did it work?") |
| **UserPromptSubmit** | You submit a prompt | Context enrichment, logging, rate limiting |

**Examples matching task to hook type:**
- **SessionStart**: "Check git branch is correct" (setup validation)
- **PreToolUse** (targeting Bash): "Warn before running delete commands" (safety prevention)
- **PostToolUse** (targeting Edit): "Run linter after file edits" (quality validation)
- **UserPromptSubmit**: "Log each prompt + attach git diff for context" (enrichment)

### Step 3: Define Matcher (WHAT triggers specifically)

Matchers narrow the scope. Without matchers, hooks run everywhere (expensive, noisy). With matchers, hooks run only where needed:

**Options:**
- **Single tool:** `"Edit"` = fires for Edit tool only
- **Multiple tools:** `"Edit|Write"` = fires for Edit OR Write
- **All tools:** `"*"` = fires for any tool
- **Bash subcommands:** `"Bash(npm:*)"` = fires for npm commands only

**Examples:**
- PostToolUse + `"Edit"` matcher = "Run linter ONLY after edits" (not after reads)
- PreToolUse + `"Bash(rm:*)"` matcher = "Warn ONLY before delete commands" (not before other bash)
- SessionStart (no matcher) = "Always run on session start"

### Step 4: Specify Action (DO WHAT)

What should happen? Options:

- **command**: Run a shell command (`npm run lint`, `git status`, `python -m pytest`)
- **block**: Prevent action (useful for safety: "don't run rm in production")
- **warn**: Alert before proceeding
- **enrich**: Add context (e.g., "attach git diff to every prompt")

**Examples:**
- Action: `npm run lint` = run linter
- Action: `python -m pytest` = run test suite
- Action: `git status` = show branch status
- Action: `echo "Running bash command..."` = provide user feedback

---

## 💬 AI Colearning Prompt: Identify YOUR Automation Opportunities

You've learned the pattern. Now let AI help YOU identify opportunities in YOUR workflow.

> **Explore with your AI:**
> "I work on [your domain: web apps, data pipelines, DevOps, mobile, etc.]. Analyze my typical development workflow and suggest 3 automation opportunities where hooks would save me time or catch errors. For each suggestion: (1) What tedious task it automates, (2) Which hook type to use (SessionStart/PreToolUse/PostToolUse/UserPromptSubmit), (3) What command/action the hook would execute, (4) Estimated time saved or errors prevented per day."

**What you'll learn:** AI will likely identify automation opportunities YOU hadn't considered. This is Principle 18 (Three Roles), AI as Teacher: AI suggests patterns (type checking validation, security scanning) based on domain expertise.

---

## Hook Types: When To Automate

### SessionStart — Environment Health Checks

**Fires:** When Claude Code starts

**Strategic Use Case:** Use SessionStart for environment validation. Examples:
- Verify you're on the correct git branch (prevents working in wrong context)
- Check that required tools are installed
- Confirm environment variables are set
- Test database connections
- Show project status summary

**Why this matters:** A 3-second environment check at session start prevents 30 minutes of wasted work later.

### PreToolUse — Safety & Prevention

**Fires:** BEFORE Claude Code executes any tool (Bash, Edit, Write, etc.)

**Matcher Options:**
- Single tool: `"Bash"` = before any bash command
- Specific bash commands: `"Bash(rm:*)"` = before delete commands only
- Multiple tools: `"Edit|Write"` = before file modifications

**Strategic Use Case:** Use PreToolUse to prevent mistakes. Examples:
- Warn before destructive commands (`rm`, `git push`, database deletes)
- Block dangerous operations in production environment
- Check permissions before file writes
- Validate specifications before large operations
- Prevent actions during protected hours (e.g., "no deployments between 5pm-8am")

**Why this matters:** A 2-second PreToolUse warning prevents catastrophic mistakes. This is damage prevention—worth its weight in gold.

### PostToolUse — Validation & Follow-Up

**Fires:** AFTER Claude completes a tool

**Matcher Options:**
- After edits: `"Edit"` = after file modifications
- After bash: `"Bash"` = after commands complete
- After writes: `"Write"` = after file creation
- Multiple: `"Edit|Write|Bash"`

**Strategic Use Case:** Use PostToolUse to validate and enforce quality gates. Examples:
- Run linter after file edits
- Run type checker after code changes
- Run test suite after significant edits
- Format code automatically
- Generate documentation
- Check for security vulnerabilities

**Why this matters:** Automated quality gates mean consistent standards. Every edit is automatically validated.

### UserPromptSubmit — Context Enrichment & Logging

**Fires:** When you submit a prompt to Claude

**Strategic Use Case:** Use UserPromptSubmit to enrich context. Examples:
- Automatically attach git diff to every prompt (helps AI understand context)
- Log prompts for audit trails
- Enforce rate limits (prevent prompt spam)
- Add project metadata (branch, environment)
- Check token usage before accepting

**Why this matters:** Enriching Claude's context improves response quality. Adding git diff means AI sees what you changed, enabling better suggestions.

### Notification, Stop, SubagentStop, PreCompact, SessionEnd — Advanced Events

**In this lesson:** We focus on the four core hooks above. Advanced hooks (Notification, Stop, etc.) are available for complex automation patterns (Tier 3) but are optional for beginners.

---

## 🎓 Expert Insight: Strategic Delegation to Your AI Co-Worker

Hooks demonstrate the **Three-Role AI Partnership** in action:

**AI as Co-Worker (Proactive Partner):**
- You specify a quality gate once (hook configuration)
- Claude enforces it automatically, forever
- No manual reminders needed—automation is "ambient"
- AI learns your standards and applies them consistently

**Example:** You create a PostToolUse hook that runs linter after edits. From that moment on, EVERY edit is linted automatically. Claude doesn't wait for you to ask—it proactively checks quality. That's co-working.

**Tier 2 Strategic Delegation (Constitution Principle 13):**
- **Tier 1 (Book teaches):** Understanding hook types and when to use them ← You learned this above
- **Tier 2 (AI Companion):** Creating hooks is easy; you specify intent, Claude handles configuration ← This lesson focuses here
- **Tier 3 (AI Orchestration):** Complex multi-hook workflows managing your entire quality pipeline ← Advanced, optional

**Compounding Effect:**
- 1-2 hooks = single quality gate (useful)
- 5-10 hooks = comprehensive quality layer (powerful)
- 20+ hooks = entire team's standards encoded as automation (competitive advantage)

**Organizational Value:**
Well-designed hooks capture YOUR team's quality standards and workflow policies as executable code. This is "Specs as Strategic Assets"—specifications that create business value:
- New team members inherit standards automatically
- Consistency enforced without policing
- Quality gates are transparent (anyone can read the hook config)
- Hooks are versionable (like code, you track changes)

---

## 🤝 Practice Exercise 1: Design Your First Hook (Specification-First)

Before building, specify. This is the Graduated Teaching Pattern: you'll plan your automation before writing code.

**Choose ONE tedious task** from your workflow:

Examples:
- Running linter after every Python file edit
- Checking git status at session start
- Verifying no hardcoded secrets before commits
- Formatting code after edits
- Running tests before important operations

**Apply the Automation Thinking Pattern:**

1. **Tedious Task**: Describe what you check manually and how often (e.g., "I run eslint manually after editing JavaScript files, about 20 times per day")

2. **Hook Type**: Which fits best? (SessionStart/PreToolUse/PostToolUse/UserPromptSubmit)
   - Reasoning: Why this type? (e.g., "PostToolUse because I want validation AFTER edits, not before")

3. **Matcher**: What triggers specifically?
   - Example: `"Edit"` for file edits, `"Bash(npm:*)"` for npm commands, `"*"` for all tools

4. **Action**: What command runs?
   - Example: `npm run lint`, `python -m pytest`, `git status`, `echo "Linting complete..."`

5. **Write 3-5 sentences** describing your hook specification (not code yet—just intent)

6. **ROI Check**: Is this worth >5 minutes saved per day?
   - If no: Choose higher-value task
   - If yes: You're ready to create the hook

**Example Specification:**
```
I manually run 'npm run lint' after almost every JavaScript edit to catch style errors.
This is tedious and I often forget. I'll create a PostToolUse hook targeting Edit that
automatically runs npm run lint. This saves me 2-3 minutes per day and catches errors
I'd otherwise miss. Estimated value: 1 hour/week saved + 5 errors/week prevented.
```

---

## Step 1: Write Your First Hook (Foundation)

You'll write JSON directly so you understand exactly how hooks work.

### Create `.claude/settings.json`

In your project root, create a file named `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "echo '🚀 Claude Code session started for this project'"
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo '⚡ Running bash command...'"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo '✅ File edited successfully'"
          }
        ]
      }
    ]
  },
  "permissions": {
    "allow": [
      "Bash(*)",
      "Write",
      "Edit",
      "Read"
    ],
    "deny": [],
    "ask": []
  }
}
```

**Understanding the structure**:

**Hooks section**:
- **`SessionStart`**: Runs when Claude Code starts
- **`PreToolUse`**: Runs BEFORE a tool executes (with `matcher: "Bash"` = only bash)
- **`PostToolUse`**: Runs AFTER a tool completes (with `matcher: "Edit"` = only edits)
- **`type: "command"`**: Execute a shell command
- **`command`**: The actual shell command to run (`echo` in this case)

**Permissions section** (CRITICAL):
- **`allow`**: Tools that Claude Code is permitted to use
  - `"Bash(*)"` → Allow any bash command
  - `"Write"` → Allow creating files
  - `"Edit"` → Allow editing files
  - `"Read"` → Allow reading files
- **`deny`**: Tools to explicitly block (empty = no blocks)
- **`ask`**: Tools that require user confirmation each time (empty = none)

**Why permissions?** Hooks run shell commands, which are powerful. Permissions tell Claude Code which tools are safe in this project and which need user approval.

### Test Your Hook

1. Save the file
2. Exit Claude Code: `exit`
3. Restart: `claude`
4. You should see: `🚀 Claude Code session started for this project`
5. Ask Claude: "List Python files in this project"
6. You should see: `⚡ Running bash command...` before the command runs
7. Ask Claude: "Add a comment to test.md"
8. You should see: `✅ File edited successfully` after the edit

**Why write it manually?** You now understand exactly what each hook does, how the JSON is structured, AND why permissions matter.

**What you learned:** Hooks are specifications you write once. They execute automatically forever. This is Specification-Driven Automation.

---

## Step 2: The Interactive Way (Easier)

Now that you understand hooks, Claude Code has a faster way to add them:

### Use the `/hooks` Command

Instead of writing JSON, type:

```
/hooks
```

You'll see an interactive menu:
- PreToolUse — Before tool execution
- PostToolUse — After tool execution
- Notification — When notifications are sent
- UserPromptSubmit — When the user submits a prompt
- SessionStart — When a new session is started

Select an event, enter your command, done. No JSON to write.

**When to use**: When you want to quickly add a simple hook without editing config files.

---

## Step 3: The AI-Native Way (Automation)

For more complex hooks or when you want AI to help, use Claude Code's AI-native approach:

### Tell Claude to Configure Your Hooks

Instead of writing JSON or using `/hooks`, just ask Claude:

**Example prompt**:
```
I want to add a hook that runs npm run lint after every file edit.
Use the official Claude Code hooks documentation to create the right
configuration. Here's the link: https://docs.claude.com/en/docs/claude-code/hooks
```

Claude will:
1. Fetch the official hooks documentation
2. Generate the correct JSON
3. Create or update `.claude/settings.json`
4. Test the hook with you

**Why this works**: Claude reads the official docs in real-time, ensuring your hooks match the latest Claude Code API. This is how AI serves Tier 2 (AI Companion): you specify the goal, AI handles the implementation complexity.

---

:::note
Windows users: run hooks in WSL or Git Bash for best compatibility. If using PowerShell, replace `jq` with `ConvertFrom-Json`, skip `chmod`, and invoke scripts with `python path/to/script.py` instead of relying on POSIX executability.
:::

## Understanding Permissions (Critical for Hooks)

Hooks execute shell commands, which are powerful. The `permissions` section controls what Claude Code is allowed to do in your project.

### Permission Types

**`allow`** — Tools Claude Code can use automatically:
```json
"allow": [
  "Bash(*)",          // Allow any bash command
  "Write",            // Allow creating files
  "Edit",             // Allow editing files
  "Read"              // Allow reading files
]
```

**`deny`** — Tools to explicitly block:
```json
"deny": [
  "Bash(rm:*)"        // Block delete commands
]
```

**`ask`** — Tools that require user confirmation:
```json
"ask": [
  "Bash(git push:*)"  // Always ask before pushing
]
```

### Why This Matters for Hooks

Hooks are shell commands that run **automatically** (without user input). Permissions ensure:

1. **Security**: Only safe commands can run automatically
2. **Control**: You decide which tools need approval
3. **Predictability**: No surprises from automated actions

**Example**: A hook that runs `npm run lint` needs:
```json
"allow": ["Bash(npm:*)"]
```

Without this permission, the command will be denied by the permissions system and won't execute.

---

## Understanding Hook Events

Each hook fires at a specific lifecycle moment:

| Hook Event | Fires When | Use For |
|-----------|-----------|---------|
| **SessionStart** | Claude Code starts | Greeting, environment setup |
| **PreToolUse** | Before a tool executes | Validation, warnings |
| **PostToolUse** | After a tool completes | Confirmation, running tests |
| **UserPromptSubmit** | User submits a prompt | Logging, preprocessing |
| **Notification** | Claude sends a notification | Logging events |
| **Stop** | Claude finishes responding | Cleanup |
| **SubagentStop** | Subagent task completes | Collecting results |
| **PreCompact** | Before history compaction | Snapshots |
| **SessionEnd** | Session ends | Cleanup, saving state |

---

## How Matchers Work

Hooks can target specific tools with `matcher`. You have three options:

### Option 1: Target a Single Tool

**Available tool matchers**:
- `"Bash"` — Bash/shell commands
- `"Edit"` — File edits
- `"Read"` — File reads
- `"Write"` — File writes
- `"Glob"` — File pattern searches
- `"Grep"` — File content searches

**Example - Single tool**:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo '⚡ Running bash command...'"
          }
        ]
      }
    ]
  }
}
```

### Option 2: Target Multiple Tools (Pipe Notation)

Use the pipe character `|` to match multiple tools:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo '✅ File operation complete'"
          }
        ]
      }
    ]
  }
}
```

Now the hook fires after EITHER Edit OR Write operations.

### Option 3: Target All Tools (Wildcard)

Use `"*"` to match all tools:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '🔄 About to execute any tool...'"
          }
        ]
      }
    ]
  }
}
```

Now the hook fires before ANY tool is executed.

### Example - Different Messages for Different Tool Groups

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo '🔧 Running command...'"
          }
        ]
      },
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "echo '✏️  Modifying file...'"
          }
        ]
      },
      {
        "matcher": "Read|Glob|Grep",
        "hooks": [
          {
            "type": "command",
            "command": "echo '📖 Searching for files...'"
          }
        ]
      }
    ]
  }
}
```

Now:
- Before bash: `🔧 Running command...`
- Before Edit/Write: `✏️  Modifying file...`
- Before Read/Glob/Grep: `📖 Searching for files...`

---

## Scope: Project vs. Global

### Project Hooks (What We Created)

**Location**: `.claude/settings.json` in your project

**Applies to**: Only this project

**When to use**: Project-specific automation

### Global Hooks (Optional)

**Location**: `~/.claude/settings.json` in your home folder

**Applies to**: ALL projects on your machine

**When to use**: Rules you want everywhere (e.g., block dangerous commands)

**Pro tip**: Start with project hooks. Add global hooks only when you want the rule in all projects.

---

## Strategic Hook Management (Best Practices)

Hooks are organizational assets—treat them like code (version control, documentation, team review). Here's how to maximize value:

### Start With Simple Hooks

Create basic hooks first (single matcher, single action). Examples:
- SessionStart hook checking git branch
- PostToolUse + Edit hook running linter
- PreToolUse + Bash hook warning before deletes

**Why this matters**: Simple hooks have high ROI (easy to debug, obvious value). Build confidence before complexity.

### Document Why Each Hook Exists

Add comments to `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "git branch",
        // WHY: Remind me which branch I'm on. Prevents commits to wrong branch.
        // VALUE: Prevents 30-minute merge nightmares.
      }
    ]
  }
}
```

**Why this matters**: Future you (and your team) will understand intent, not just mechanics.

### Test Hooks Individually

When creating a hook:
1. Create it
2. Trigger the event (restart for SessionStart, run a tool for PreToolUse, etc.)
3. Verify the hook executed
4. Check the output

**Why this matters**: Caught-early bugs are cheap. Late-stage hook bugs are expensive (they run automatically in production).

### Version Control Your Hooks

`.claude/settings.json` belongs in git:
```bash
git add .claude/settings.json
git commit -m "Add pre-commit linting hook"
```

**Why this matters**: Hooks are team standards. Version control makes changes transparent and reversible.

### Gradual Rollout for Team Hooks

Don't add 10 hooks at once. Instead:
1. Add 1-2 hooks per week
2. Gather feedback (does this hook help or annoy?)
3. Refine based on usage
4. Only then add more

**Why this matters**: Hooks change behavior. Gradual adoption allows teams to adapt.

---

## Common Hook Patterns

### Pattern 1: Friendly Greeting

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "echo '👋 Welcome to [Project Name]!'"
      }
    ]
  }
}
```

### Pattern 2: Action Confirmations

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo '💾 File saved'"
          }
        ]
      },
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo '✨ Command executed'"
          }
        ]
      }
    ]
  }
}
```

### Pattern 3: Pre-Action Warnings

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo '⚠️  Command about to run...'"
          }
        ]
      }
    ]
  }
}
```

---

## Troubleshooting

### Hook Not Executing?

**Check 1: Permissions**
- Does `.claude/settings.json` include the tool in `"allow"`?
- Example: If your hook runs `npm run lint`, does permissions include `"Bash(npm:*)"`?
- Fix: Add missing tool to `allow` section

**Check 2: Syntax**
- Is your JSON valid? (Test at jsonlint.com)
- Are hook matchers spelled correctly? (`"Edit"`, not `"edit"`)
- Fix: Validate JSON syntax

**Check 3: Restart Claude Code**
- Changes to `.claude/settings.json` require restart
- Exit: `exit`
- Restart: `claude`
- Fix: Restart and test again

**Check 4: Matcher Mismatch**
- Is your matcher targeting the right tool?
- Example: PostToolUse with `"Bash"` matcher won't fire on file edits
- Fix: Check matcher is correct for your trigger

### Hook Causing Issues?

**Disable Temporarily**
- Comment out the hook in `.claude/settings.json`
- Restart Claude Code
- Does the issue disappear?
- If yes: Hook is the problem. Refine or remove it.

**Debug Output**
- Add echo statements to see what's executing:
  ```json
  "command": "echo 'HOOK FIRED' && npm run lint"
  ```
- Check output to verify hook runs

### Permission Denied Errors?

**Symptom**: Hook runs but says "permission denied"

**Causes**:
1. Tool not in `allow` list
2. Command requires special permissions (e.g., `sudo`)

**Solutions**:
- Add tool to `allow`: `"Bash(npm:*)"`
- For privileged commands, use full path or sudo in hook

### Platform-Specific Issues

**Windows (PowerShell)**:
- Replace `jq` commands with PowerShell equivalents
- Use `ConvertFrom-Json` instead of `jq`
- Skip `chmod` (not applicable to Windows)
- Paths: Use backslashes or forward slashes (both work)

**macOS/Linux**:
- Use standard bash commands
- Ensure scripts are executable: `chmod +x script.sh`
- Use shebang: `#!/bin/bash` at top of scripts

---

## 🤝 Practice Exercise 2: Create and Test Your First Hook

Now implement the hook you designed in Practice Exercise 1.

**Steps:**

1. **Open/Create `.claude/settings.json`** in your project root (see "Step 1" section for template)

2. **Add your hook** to the appropriate section:
   - SessionStart hook? Add to `"SessionStart": [...]`
   - PreToolUse hook? Add to `"PreToolUse": [...]`
   - PostToolUse hook? Add to `"PostToolUse": [...]`
   - UserPromptSubmit hook? Add to `"UserPromptSubmit": [...]`

3. **Ensure your hook's tool is in `permissions.allow`**:
   - If hook runs bash? Make sure `"Bash(*)"` is in allow
   - If hook edits files? Make sure `"Edit"` is in allow

4. **Save the file**

5. **Test the trigger**:
   - **SessionStart hook**: Exit Claude Code (`exit`) and restart (`claude`)
   - **PreToolUse/PostToolUse hook**: Trigger the tool (e.g., ask Claude to edit a file)
   - **UserPromptSubmit hook**: Submit a prompt

6. **Observe the output**:
   - Did your hook run?
   - Did your command execute?
   - Did you see the expected output?

7. **Iterate if needed**:
   - Syntax error? Check JSON validity
   - Matcher not working? Verify matcher is correct
   - Permissions issue? Check `allow` list

8. **Reflect**:
   - What did you learn by creating this hook?
   - What's your next automation opportunity?
   - How would you describe what hooks do to someone else?

**Expected Outcome**: One working hook that automatically handles your tedious task. This is your automation foundation.

---

## 💬 AI Colearning Prompt: Strategic Hook Library Design

Now think beyond individual hooks. AI can help you design a complete hook library for your team.

> **Plan with your AI:**
> "My team's common pain points are [list 3-5 tedious or error-prone tasks, like 'forgetting to run tests before pushing', 'inconsistent code formatting', 'accidental commits to main branch', etc.]. Design a hook library (5-7 hooks) that would address these pain points. For each hook in the library: (1) Hook name and type, (2) What manual task it replaces, (3) Matcher criteria (which tool), (4) Exact action/command, (5) Estimated time/frustration saved per week. Also suggest rollout order (which hooks first, which later)."

**What you'll learn:**
- AI will help you see patterns (most teams have similar pain points)
- You'll discover hooks you hadn't thought of (security scanning, dependency checking, etc.)
- You'll learn prioritization (implement high-ROI hooks first)
- This is Principle 18 (Three Roles): AI as Teacher suggesting best practices, AI as Co-Worker helping you design systems

---

## Try With AI

### Exercise 1: Claude as Teacher — Hook Opportunities (AI Suggests)

**Prompt to Claude:**
```
Analyze my development workflow. I primarily work on [Python/JavaScript/other],
my projects are [type: web apps/data pipelines/CLI tools/etc], and I'm concerned about
[performance/security/reliability/consistency/testing]. Using that context, identify
3-4 automation opportunities where hooks would improve my workflow. For each:
(1) What problem it solves, (2) Recommended hook type and matcher,
(3) Exact command/action to implement, (4) How to test it works.
```

**What Claude generates:**
- Domain-specific hook recommendations (AI knows your tech stack)
- Practical matchers and commands (tested patterns)
- Testing strategies (how to verify hooks work)

**Your role:** Evaluate suggestions. Which hooks matter most to you? Which do you want to implement first?

---

### Exercise 2: Claude as Student — Learning YOUR Workflow (AI Adapts)

**Prompt to Claude:**
```
Interview me about my development workflow so you can recommend custom hooks.
Ask me: (1) What do I check manually most often before/after actions?
(2) What errors have I made repeatedly that automation could prevent?
(3) What frustrates me most about my current process?
(4) What tools/languages do I use most?

Based on my answers, design 2-3 custom hooks specifically for my workflow.
```

**What Claude does:**
- Asks clarifying questions (Claude as Student, learning your context)
- Listens to your answers (adapts understanding)
- Designs custom hooks based on YOUR specific needs (not generic patterns)

**Your role:** Answer questions authentically. Claude learns your workflow and tailors recommendations. This is Principle 18: AI as Student, learning from your domain expertise.

---

### Exercise 3: Claude as Co-Worker — Build and Deploy Your Hook

**Prompt to Claude:**
```
I want to create a hook that [describe your automation goal: runs tests before commits,
checks for hardcoded secrets, formats code after edits, validates branch before pushes,
verifies deployment readiness, etc.]. Help me:
(1) Choose the right hook type and matcher for this goal
(2) Write the exact hook JSON configuration
(3) Specify the correct permissions needed in .claude/settings.json
(4) Create a testing plan to verify it works
(5) Troubleshoot if something doesn't work as expected
```

**What Claude does:**
- Collaborates on implementation (not just tells you what to do)
- Generates correct JSON configuration
- Handles complexity (you focus on intent, Claude handles syntax)

**Your role:** Specify intent, validate Claude's implementation, run tests, adjust if needed. This is Principle 18: AI as Co-Worker, handling tactical execution while you manage strategy.

---

## Closing: Automation as Strategic Asset

You've learned hooks—specifications that trigger automation.

**Key takeaways:**
- **Hooks = Specifications**: You specify (once) when/what/how to automate. Claude enforces (forever).
- **Automation Thinking Pattern**: Tedious → Hook Type → Matcher → Action. Apply this to any repetitive task.
- **Tier 2 Delegation**: Hooks represent Graduated Teaching Pattern (Tier 2): you specify quality gates, AI enforces them.
- **Strategic Value**: Each hook saves time. 5-10 hooks = quality layer your team uses unconsciously.
- **Compounding Effect**: Individual hooks seem small, but together they encode organizational standards.

**What hooks represent in Constitution Principle 13 (Graduated Teaching):**
- **Tier 1** (Book teaches): Understanding hook types, automation patterns
- **Tier 2** (AI Companion): Creating and configuring hooks ← **You did this**
- **Tier 3** (AI Orchestration): Complex multi-hook systems managing entire workflows (optional, advanced)

You've mastered Tier 2. Tier 3 (orchestrating 20+ hooks across team) is optional—available when you need it.

---

## Try With AI

Pick one exercise and start now:

**Option 1: Discovery** (Easy start)
- Run Exercise 1: Ask Claude to identify 3 automation opportunities in YOUR workflow

**Option 2: Custom Design** (Deeper learning)
- Run Exercise 2: Have Claude interview you, then design custom hooks

**Option 3: Implementation** (Hands-on)
- Run Exercise 3: Build your first hook with Claude's help, then test it

**Expected outcomes:**
- Exercise 1: 3 concrete hook ideas you can implement (or not—it's your choice)
- Exercise 2: Deep understanding of YOUR automation opportunities
- Exercise 3: One working hook + confidence to build more

Pick whichever sounds most valuable to you right now. Start with what interests you most.
