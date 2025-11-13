---
sidebar_position: 6
title: "Skills, Plugins, and MCP Integration: The Unified Architecture"
chapter: 5
lesson: 6
duration_minutes: 12

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Understanding Progressive Disclosure in Agent Architecture"
    proficiency_level: "A2"
    category: "Technical/Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information & Digital Literacy"
    measurable_at_this_level: "Student can explain 3-level progressive disclosure and identify examples at each level"

  - name: "Recognizing Plugin Architecture and Component Hierarchy"
    proficiency_level: "A2"
    category: "Technical/Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving & Digital Systems"
    measurable_at_this_level: "Student can identify what goes inside plugins and how components relate"

  - name: "Installing and Verifying Community Plugins"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Tools & Systems"
    measurable_at_this_level: "Student can successfully install a real plugin from marketplace and verify activation"

  - name: "Configuring MCP Servers within Plugin Context"
    proficiency_level: "A2"
    category: "Technical/Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Systems & Protocols"
    measurable_at_this_level: "Student can explain MCP configuration structure and how it integrates with plugins"

  - name: "Designing Plugin-Based Workflows"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving & Digital Systems"
    measurable_at_this_level: "Student can design appropriate plugin components for a workflow scenario"

  - name: "Evaluating When to Use Skills vs. Commands vs. Plugins"
    proficiency_level: "B1"
    category: "Technical/Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can justify architectural choices for extending Claude Code"

  - name: "Understanding Community Plugin Ecosystems"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information & Digital Collaboration"
    measurable_at_this_level: "Student can describe community ecosystem (Anthropic, Dan Ávila, Seth Hobson plugins)"

learning_objectives:
  - objective: "Explain how agent skills use progressive disclosure (3 levels: YAML in system prompt → SKILL.md when relevant → files on demand)"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student explains 3 levels with PDF skill example"

  - objective: "Identify what components belong inside plugins (skills, commands, agents, hooks, MCP configuration)"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student correctly identifies 5 plugin components from diagram/description"

  - objective: "Install a real community plugin and verify activation"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student successfully runs /plugin command and shows plugin is active"

  - objective: "Configure MCP server integration and understand relationship to plugins"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student explains MCP configuration with 2 examples (GitHub, Filesystem)"

  - objective: "Design plugin components appropriate to a team workflow scenario"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student proposes skill + command + hook combination for real scenario"

cognitive_load:
  new_concepts: 7
  assessment: "7 new concepts (Skills, Progressive Disclosure, Plugins, MCP, Hierarchy, Community, Personalization) exactly at A2 limit of 7 concepts ✓"

differentiation:
  extension_for_advanced: "Design a custom plugin combining 3+ components (skill + command + hook) for your team's workflow; analyze competitive advantage vs. manual processes"
  remedial_for_struggling: "Focus on Skills and Plugins as primary containers; defer MCP configuration to Part 3 or Part 5 when deeper study of protocols occurs"

# Generation metadata
generated_by: "lesson-writer v3.2.0"
source_spec: "Vertical Intelligence context: Layer 1-4"
created: "2025-11-13"
last_modified: "2025-11-13"
git_author: "Claude Code"
workflow: "Manual specification implementation"
version: "1.0.0"
---

# Skills, Plugins, and MCP Integration: The Unified Architecture

## Why You Need This Lesson

You've learned about **agent skills** (Lesson 4) and **MCP servers** (Lesson 5), but they exist separately in your mind. This lesson unifies them: showing how they're actually **components inside a larger architectural whole** called **plugins**.

Understanding this relationship transforms you from someone who knows features to someone who can **design extensible systems**. You'll see how Anthropic, community developers, and your team can bundle reusable capabilities into shareable plugins that persist across projects.

This is where Claude Code stops being a tool and becomes **your team's collaborative platform**.

---

## The Progressive Disclosure Pattern: Elegant Simplicity at Three Levels

Before diving into architecture, you need to understand how Claude Code achieves a seemingly magical feat: **discovering the right skill at the right time without overwhelming the system prompt**.

The answer is **progressive disclosure**—information revealed in layers based on relevance.

### Level 1: Metadata in System Prompt (Always Present)

When Claude Code starts, it loads a summary of every skill as a concise line in its system prompt:

```
Available Skills:
- pdf-skill: Extract and analyze tables, forms, and fields from PDF files
- code-review-skill: Autonomous code quality auditing with architectural insight
- compliance-checker: Validate financial calculations against regulatory requirements
```

This is **tiny**—3-4 lines per skill. Claude reads these summaries and thinks: *"If the user shows me a PDF, I should probably use the pdf-skill."*

**Why this works**: Claude learns WHEN to invoke skills without needing the full SKILL.md file loaded yet.

#### 💬 AI Colearning Prompt
> "How does Claude Code decide when to invoke a skill if it only reads a summary? Isn't that risky—what if it makes mistakes?"

### Level 2: Full SKILL.md When Relevant (On-Demand)

When Claude decides a skill is relevant, it fetches the complete **SKILL.md file**—the full instructions:

```yaml
---
name: "pdf-skill"
description: "Extract tables, forms, and field values from PDF files using deterministic Python scripts"
---

# PDF Skill: Deterministic Table and Form Extraction

## When to Use This Skill
- User uploads a PDF and asks to extract a table
- User wants form fields extracted and validated
- User asks about PDF content structure

## How to Use This Skill
1. Run the bundled Python script: `scripts/pdf_extractor.py --input [path] --output [format]`
2. Validate extracted data matches expected structure
3. Return structured JSON with confidence scores
```

Now Claude has the **full context** needed to execute properly. But it only loads this when relevant.

**Why this works**: Full instructions don't clutter the system prompt; they're loaded on-demand when needed.

### Level 3: Bundled Reference Files and Scripts (Even More Detail)

If the SKILL.md needs supporting files, Claude accesses them:

```
.claude/skills/pdf-skill/
├── SKILL.md                 # Main instructions
├── scripts/
│   └── pdf_extractor.py     # Python script for deterministic field extraction
└── reference/
    └── pdf-standards.md     # Technical reference: PDF field specifications
```

When Claude executes the skill, it can reference the Python script directly or dive into technical specs if needed.

**Real Example: PDF Form Filling Skill**

```
Skill invocation flow:
1. User: "Extract all form fields from this W-2 PDF"
2. Claude reads system prompt summary: "pdf-skill: Extract forms and fields"
3. Claude fetches SKILL.md: "Use pdf_extractor.py for deterministic extraction"
4. Claude runs: pdf_extractor.py --input w2.pdf --output json
5. Claude references pdf-standards.md to validate field names
6. Claude returns: {"ssn": "XXX-XX-XXXX", "income": 125000, ...}
```

**Why this matters**: Skills are discoverable (small summaries), executable (full instructions), and reliable (bundled scripts + reference docs).

#### 🎓 Expert Insight
> In AI-native development, progressive disclosure isn't a feature—it's the difference between cluttered systems and elegant ones. Claude Code loads only what it needs when it needs it. This pattern (metadata → full definition → supporting files) scales to thousands of skills without system prompt bloat.

---

## Plugins: Containers for All Extensions

Now you can understand **plugins**—the broadest architectural container.

### What Is a Plugin?

A **plugin** is a directory (`.claude-plugin/` in your project) that bundles:
- **Skills** (autonomous capabilities discovered by Claude)
- **Commands** (slash commands like `/code-review`)
- **Agents** (specialized subagents with focused context)
- **Hooks** (automation triggered by events like file saves)
- **MCP Configuration** (external integrations)

**A plugin is NOT a single feature—it's an integrated collection of extensions.**

### Plugin Architecture: The Manifest

Every plugin starts with a manifest file: `.claude-plugin/plugin.json`

```json
{
  "name": "feature-dev",
  "version": "1.0.0",
  "description": "Feature development plugin with code review, testing, and deployment hooks",

  "components": {
    "skills": [
      { "path": "skills/code-quality-checker" },
      { "path": "skills/test-coverage-analyzer" }
    ],
    "commands": [
      { "name": "feature-dev", "path": "commands/feature-dev.md" },
      { "name": "code-review", "path": "commands/code-review.md" }
    ],
    "agents": [
      { "name": "test-orchestrator", "path": "agents/test-orchestrator.md" }
    ],
    "hooks": [
      { "trigger": "PreToolUse", "path": "hooks/pre-tool-validation.md" }
    ],
    "mcp_config": "mcp-servers.json"
  }
}
```

**What this says**: *"This plugin includes 2 skills, 2 commands, 1 agent, 1 hook, and MCP configuration."*

### Inside a Plugin Directory Structure

```
.claude-plugin/
├── plugin.json                    # Manifest
├── commands/
│   ├── feature-dev.md             # Slash command: /feature-dev
│   └── code-review.md             # Slash command: /code-review
├── agents/
│   └── test-orchestrator.md       # Specialized subagent for testing
├── skills/
│   ├── code-quality-checker/
│   │   ├── SKILL.md               # Skill definition
│   │   └── scripts/
│   │       └── analyzer.py        # Implementation script
│   └── test-coverage-analyzer/
│       ├── SKILL.md
│       └── scripts/
│           └── coverage.py
├── hooks/
│   └── pre-tool-validation.md     # Runs before tool execution
└── mcp-servers.json               # External integrations (GitHub, Filesystem, etc.)
```

**Key insight**: A **single plugin** can deliver capabilities at multiple levels. The `feature-dev` plugin gives you:
- ✅ Autonomous skills (code quality checking, coverage analysis)
- ✅ Explicit commands (`/code-review`, `/feature-dev`)
- ✅ Specialized agents (test orchestration)
- ✅ Automation hooks (pre-execution validation)
- ✅ External integrations (GitHub MCP for issue tracking)

---

## The Relationship Hierarchy: Plugins Contain Everything

Let me show you how all the pieces fit:

```
┌─────────────────────────────────────────────────────┐
│                    PLUGIN (Container)               │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │         SKILLS (Autonomous Discovery)        │  │
│  │  • Code quality checker (autonomous)         │  │
│  │  • Test coverage analyzer (autonomous)       │  │
│  │  • Compliance checker (autonomous)           │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │        COMMANDS (Explicit Slash Cmds)        │  │
│  │  • /code-review                              │  │
│  │  • /feature-dev                              │  │
│  │  • /deploy                                   │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │      AGENTS (Specialized Subagents)          │  │
│  │  • test-orchestrator (runs tests)            │  │
│  │  • security-auditor (checks vulnerabilities)│  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │     HOOKS (Event-Triggered Automation)       │  │
│  │  • PreToolUse: Validate before execution    │  │
│  │  • PostToolUse: Log execution results        │  │
│  │  • SessionStart: Initialize context          │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │  MCP CONFIGURATION (External Integrations)  │  │
│  │  • GitHub MCP (@github activation)          │  │
│  │  • Filesystem MCP (@filesystem activation)  │  │
│  │  • Jira MCP (@jira for issue tracking)      │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Interpretation**:
- **Skills** = Claude discovers and uses autonomously based on context
- **Commands** = You explicitly invoke with `/command-name`
- **Agents** = Specialized AI assistants you delegate to for focused tasks
- **Hooks** = Automation triggered by events (before/after operations)
- **MCP** = External tools and data (web, GitHub, databases, APIs)

**All of these live INSIDE the plugin**—bundled as a cohesive unit.

---

## Installation and Activation: The Plugin Workflow

The real power of plugins is **sharing and discovering them from a marketplace**.

**Important:** Plugin management uses CLI commands (from your terminal), not session slash commands. Use `claude plugin [subcommand]` outside of a Claude Code session.

### Installing a Community Plugin: Three Steps

**Step 1: Browse the Marketplace**

**From your terminal** (outside any Claude Code session):

```bash
# First, check what marketplaces you have configured
claude plugin marketplace list

# Add the official Anthropic marketplace if not already added
claude plugin marketplace add anthropics/claude-code
```

This gives you access to plugins from three main sources:

**Anthropic Official Plugins** (anthropics/claude-code):
- `feature-dev` — Feature development with testing
- `code-review` — Autonomous code auditing
- `security-guidance` — Security vulnerability detection

**Community Plugins by Dan Ávila**:
- `devops-automation` — Docker, K8s, deployment workflows
- `documentation-generator` — Auto-generate docs
- `testing-frameworks` — Test setup and execution

**Community Plugins by Seth Hobson & Others** (specialized domain-specific agents):
- Framework-specific plugins (React, FastAPI, Django)
- Team standard enforcement (code style, documentation patterns)
- Industry-specific (healthcare HIPAA compliance, fintech validation)

#### 🤝 Practice Exercise

> **Ask your AI**: "What plugins might help my team with [your domain: Python development / JavaScript frameworks / DevOps]? Describe what a 'feature-dev' plugin includes and explain why bundling skills, commands, and hooks together is better than having them separate."

**Expected Outcome**: You'll understand marketplace discovery and the advantages of bundled plugins.

### Step 2: Install a Plugin

**From your terminal:**

```bash
# Install a plugin from the configured marketplace
claude plugin install feature-dev

# Verify it's installed
claude plugin list
# Should show "feature-dev" with enabled status
```

### Step 3: Activate and Verify

**If you have an active Claude Code session, restart it** to load the new plugin:

```bash
# Press Ctrl+C to exit your current session (if running)
# Then start a new session
claude
```

**Inside your Claude Code session**, check what the plugin added:

```
> /help
# Look for new commands added by the plugin
# Different plugins add different capabilities:
# - Slash commands (like /code-review)
# - Autonomous skills (discovered automatically)
# - Specialized agents
```

**Verify from terminal:**

```bash
claude plugin list
# Should show "feature-dev" as enabled
```

**Why restart?** Plugins are loaded when Claude Code starts. A restart loads the new components into memory.

#### 💬 AI Colearning Prompt
> "After installing a plugin, why does Claude Code need to restart? What happens during restart that wouldn't happen if I kept Claude Code running?"

---

## MCP Configuration: Connecting External Systems

MCP (Model Context Protocol) is the standard for Claude Code to integrate external tools. Within a plugin, MCP is configured in **mcp-servers.json**:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "${env:GITHUB_TOKEN}"
      },
      "disabled": false
    },
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"],
      "disabled": false
    }
  }
}
```

### Example 1: GitHub MCP

```json
"github": {
  "command": "npx",
  "args": ["@anthropic-ai/mcp-server-github"],
  "env": {
    "GITHUB_TOKEN": "${env:GITHUB_TOKEN}",
    "GITHUB_SCOPES": ["repo", "gist", "user"]
  }
}
```

**What this enables**:
- `@github search issues` — Find issues matching criteria
- `@github create-pull-request` — Create PRs programmatically
- `@github commit` — Make commits with file changes

### Example 2: Filesystem MCP with Restrictions

```json
"filesystem": {
  "command": "npx",
  "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"],
  "disabled": false
}
```

**What this enables**:
- Restricted file access (only `/home/user/projects` directory)
- `@filesystem read [file]` — Read files safely
- `@filesystem write [file]` — Write with path validation

#### 🎓 Expert Insight
> MCP configuration inside plugins is the bridge between autonomous Claude (skills) and external systems (GitHub, databases, file servers). A well-designed plugin includes MCP servers that give skills the data they need to operate.

---

## Community Plugin Ecosystem: Your Options

You now have choices in how to extend Claude Code:

### Option 1: Official Anthropic Plugins (Most Stable)

**Use when**: You want battle-tested, production-ready capabilities.

**Examples**:
- `feature-dev` (feature development with testing integration)
- `code-review` (autonomous code quality auditing)
- `security-guidance` (vulnerability detection)

**Advantage**: Maintained by Anthropic, automatic updates, high reliability.

### Option 2: Community Plugins by Specialized Developers

**Dan Ávila** (DevOps, Documentation, Testing Focus):
- `devops-automation` — Orchestrate Docker, Kubernetes, CI/CD
- `documentation-generator` — Auto-generate README, API docs
- `testing-frameworks` — Set up tests for your stack

**Seth Hobson & Community** (domain-specific plugins):
- Framework-specific: React, FastAPI, Django, Next.js plugins
- Team standards: Code style enforcement, documentation patterns
- Industry-specific: Healthcare (HIPAA), fintech (compliance), e-commerce

**Advantage**: Specialized expertise, evolving with community needs, often free.

### Option 3: Team Plugins (Your Organization)

Store plugins in your team's `.claude-plugin/` directory and commit to version control.

```bash
# Team plugin in your repo
.claude-plugin/
├── plugin.json              # Team-specific configuration
├── skills/
│   └── compliance-checker/  # Your company's rules
├── commands/
│   └── deploy.md            # Your deployment process
└── mcp-servers.json         # Your internal systems
```

**Advantage**: Encodes your team's expertise, persists across projects, shared standards.

---

## Designing Your First Plugin: Strategic Questions

Before building, ask yourself:

1. **What problem are we solving?**
   - Example: "Our developers forget to add type hints and docstrings"

2. **Which component solves it?**
   - **Skill** (autonomous): Claude auto-detects Python functions without docstrings and suggests additions
   - **Command** (explicit): `/add-docstrings` to run on demand
   - **Hook** (automated): PreToolUse validates code before execution
   - **Agent** (focused): code-quality-checker subagent with specialized context

3. **Do we need external data (MCP)?**
   - **GitHub MCP**: For issue tracking, PR validation
   - **Filesystem MCP**: For safe file access restrictions
   - **Jira MCP**: For project management integration

4. **Should this be team-wide or project-specific?**
   - **Team plugin** (`.claude-plugin/`): Shared across all projects
   - **Project plugin**: Committed with your repo
   - **Community plugin**: Share with broader ecosystem

#### 🎓 Expert Insight
> Plugin design is architectural decision-making. You're not choosing "use a skill" or "use a command." You're asking: "How does my team's constraint (time, expertise, standards) best map to available extension mechanisms?" The plugin ecosystem lets you encode answers to that question once and reuse them forever.

---

## Try With AI

Use Claude Code for this activity (preferred, since you installed it earlier). If you already have another AI companion tool set up (ChatGPT web, Gemini CLI), you may use that instead.

### Prompt 1: Progressive Disclosure Explained (Conceptual Understanding)

```
Explain how Claude Code's "progressive disclosure" pattern works with agent skills.
Use this structure:
(a) Level 1 — what's in the system prompt,
(b) Level 2 — when is SKILL.md fetched and why,
(c) Level 3 — what bundled files look like,
(d) Why this is better than loading everything at startup.
Use the PDF skill form-extraction example from the lesson.
```

**Expected outcome:** Clear explanation of 3-level architecture with PDF example; understanding of why disclosure is "progressive"

### Prompt 2: Install Real Plugin and Verify (Hands-On Validation)

```
Help me install a plugin from the anthropics/claude-code marketplace
and verify it's working. Walk me through:
(a) The CLI command to add the anthropics/claude-code marketplace source,
(b) The CLI command to list available plugins,
(c) The CLI command to install a plugin,
(d) How to verify the plugin is enabled after installation,
(e) How to check what capabilities the plugin adds (commands, skills, agents).

Then explain what types of components plugins typically contain
(skills? commands? agents? hooks? MCP configuration?).
```

**Expected outcome:** Student successfully installs real plugin using correct CLI commands (`claude plugin [subcommand]`), verifies with `claude plugin list`, and describes plugin component types

### Prompt 3: MCP Configuration for GitHub and Filesystem (Technical Detail)

```
Show me the MCP configuration (mcp-servers.json format) for:
(a) GitHub MCP with proper OAuth scopes for issue management,
(b) Filesystem MCP with restricted path /home/user/projects,
(c) Explain what each line does and why those restrictions matter.

Then explain: if a skill needed to read files and create GitHub issues,
how would it reference both MCP servers?
```

**Expected outcome:** Correct JSON configuration with explanations; understanding of MCP as external bridge for skills

### Prompt 4: Design Plugin for Your Domain (Strategic Planning)

```
Design a plugin for my team's biggest pain point: [describe: inconsistent code style / missing tests / security vulnerabilities / slow deployments].

Include:
(a) Plugin name and description,
(b) Which SKILLS you'd include (and what they discover autonomously),
(c) Which COMMANDS you'd add (explicit /command-name actions),
(d) Any HOOKS needed for automation (PreToolUse? PostToolUse? SessionStart?),
(e) Which MCP servers would help (GitHub? Filesystem? Other?),
(f) How would this plugin solve the pain point better than doing it manually?

Make it realistic and implementable in 2 weeks of effort.
```

**Expected outcome:** Complete plugin design combining 3+ components; strategic justification for architectural choices; understanding of unified architecture

---

## Safety & Responsible Use

**Plugin Security Checklist**:
- ✅ Only install plugins from trusted sources (Anthropic, well-known community developers)
- ✅ Review MCP permissions before activating external integrations
- ✅ Store secrets in environment variables, never in configuration files
- ✅ Audit what MCP servers can access (GitHub token scopes, filesystem paths)
- ✅ Ask Claude: "What can this MCP server do?" if you're uncertain

**When to ask for help**:
- "I don't recognize this plugin's source"
- "This MCP asks for permissions I don't understand"
- "This looks like it could expose our codebase externally"

Trust your instincts—security is non-negotiable.

**Key takeaway**: You've learned skills, commands, agents, hooks, and MCP—five ways to extend Claude Code. The real skill is **knowing when to use each one**. Use **skills** for autonomous expertise, **commands** for explicit workflows, **agents** for complex isolated tasks, **hooks** for event automation, **MCP** for external tools, and **plugins** to bundle these into cohesive units. Master this architecture, and you can scale expert knowledge across teams.
