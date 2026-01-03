---
sidebar_position: 0
title: "Setting Up Your AI Vault"
sidebar_label: "Setting Up Your AI Vault"
description: "Set up your General Agent for professional work. Obsidian vault with AGENTS.md governance, CLAUDE.md context, and Claude Code as your operator."
keywords:
  - Obsidian vault
  - Claude Code
  - General Agent
  - AGENTS.md
  - CLAUDE.md
  - professional workspace
chapter: 6
lesson: 0
duration_minutes: 25

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation) - Setting up General Agent workspace"
layer_1_foundation: "Installing Obsidian, creating AGENTS.md, CLAUDE.md, testing with Claude Code"
layer_2_collaboration: "N/A (foundation setup)"
layer_3_intelligence: "N/A (foundation setup)"
layer_4_capstone: "N/A (foundation setup)"

# HIDDEN SKILLS METADATA
skills:
  - name: "Obsidian Vault Setup"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create Obsidian vault with governance files"
  - name: "AGENTS.md Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can create AGENTS.md with skill and agent formats"
  - name: "Claude Code Context Verification"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can verify Claude Code reads vault context"

learning_objectives:
  - objective: "Create Obsidian vault as professional workspace"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successfully create new Obsidian vault"
  - objective: "Write AGENTS.md with governance rules and formats"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "AGENTS.md contains skill and agent format specifications"
  - objective: "Create CLAUDE.md that references AGENTS.md"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "CLAUDE.md exists and references @AGENTS.md"
  - objective: "Verify Claude Code picks up vault context"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Claude Code responds with vault-specific knowledge"
  - objective: "Enable hidden files visibility in Obsidian"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Can see .claude folder in Obsidian"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (Obsidian vault, AGENTS.md, CLAUDE.md, hidden files plugin) - within A2 limit"

differentiation:
  extension_for_advanced: "Add git version control; configure additional governance rules"
  remedial_for_struggling: "Use folder-only approach without Obsidian"

# Generation metadata
generated_by: "manual creation"
created: "2026-01-03"
version: "3.0.0"
---

# Setting Up Your AI Vault

You're setting up Claude Code as your **General Agent** for professional work.

---

## The Problem

Most AI usage today is:

- **Chat-based** — conversations that disappear
- **Ephemeral** — no memory between sessions
- **Prompt-heavy** — re-explaining context every time
- **Inconsistent** — different results for same requests
- **Ungoverned** — no rules, no accountability

Even advanced users copy-paste context, re-explain their rules, and lose knowledge over time.

**The question**: How do we make AI work like a **trained professional**, not a clever chatbot?

---

## The Core Insight

**Separate memory, reasoning, and execution.**

| Role | Tool | What It Does |
|------|------|--------------|
| **Memory** | Obsidian Vault | Source of truth you curate (notes, rules, SOPs) |
| **Reasoning + Execution** | Claude Code | Reads memory, follows rules, produces work |
| **Training** | Skills | Explicit teaching — repeatable, reviewable, auditable |

**Mental model**: Claude Code is a junior professional with access to your shared drive. Not autonomous. Not magical. Just capable and fast — and it follows your written instructions.

**Key shift**: Skills are *teaching*, not prompting. You write what the skill does, when to use it, how to do it, what not to do. This makes behavior predictable.

---

## Why This Matters

| Aspect | Without Vault | With Vault |
|--------|---------------|------------|
| Context per session | Zero | Full |
| Re-explaining needed | Every time | Never |
| Memory | None | Persistent |
| Aligned advice | Generic | Your goals |
| Pattern detection | Impossible | Automatic |
| Institutional knowledge | Lost | Accumulated |

**Claude Code without vault** = Smart agent with amnesia

**Claude Code with vault** = Your personal operator who knows your goals, remembers your history, follows your rules, and builds on previous work.

**One sentence**: The vault turns Claude Code into a stateful partner that accumulates context, enforces your rules, and compounds knowledge over time.

---

## Step 1: Install Obsidian

Download from [obsidian.md](https://obsidian.md)

| Platform | Installation |
|----------|--------------|
| **macOS** | Download .dmg, drag to Applications |
| **Windows** | Download .exe, run installer |
| **Linux** | Download .AppImage or use package manager |

---

## Step 2: Create Your Vault

1. Open Obsidian
2. Select **"Create new vault"**
3. Name your vault: `skills-lab`
4. Choose location: `~/projects/skills-lab`
5. Click **Create**

Obsidian opens with an empty vault.

---

## Step 3: Create AGENTS.md

This file contains all the governance rules for how Claude Code should operate in your vault.

In Obsidian, create a new note called `AGENTS.md` and paste:

```markdown
# AGENTS.md - General Agent Governance

## Purpose

This vault is where I (human) and Claude Code (General Agent) work together on business workflows.

## Workspace Structure

skills-lab/
├── .claude/
│   ├── skills/        # Reusable expertise (SKILL.md format)
│   └── agents/        # Autonomous workers
├── references/        # Supporting documents
├── CLAUDE.md          # Project context (references this file)
└── AGENTS.md          # This file (governance)

## Governance Rules

1. **Skills go in `.claude/skills/{name}/SKILL.md`**
2. **Agents go in `.claude/agents/{name}.md`**
3. **Skills for guidance (2-4 decisions), agents for reasoning (5+)**
4. **Always read this file before operating**

## Skill Format

```yaml
---
name: skill-name
description: Single line describing when to use this skill.
---

# Skill Name

## When to Use
Triggers for this skill.

## Instructions
Step-by-step guidance.
```

## Agent Format

```yaml
---
name: agent-name
description: Single line describing when to use this agent.
model: sonnet
tools: Read, Grep, Glob
---

# Agent Name

Classification logic and decision trees.
```

## Active Projects

| Project | Series | Status |
|---------|--------|--------|
| Email Assistant | Email-1 to Email-7 | Starting |
```

Save the file.

---

## Step 4: Create CLAUDE.md

This is the entry point Claude Code reads first. Create `CLAUDE.md` in the vault root:

```markdown
# Skills Lab

This is my professional Claude Code workspace.

Read @AGENTS.md for governance rules, formats, and structure.

## Current Focus

- **Email-N series**: Building an Email Assistant
```

Save the file.

---

## Step 5: Open in Claude Code

Now test that Claude Code picks up your context.

```bash
cd ~/projects/skills-lab
claude
```

**Test prompt 1:**

```
What is this workspace and what governance rules should you follow?
```

**Expected**: Claude Code reads `CLAUDE.md`, follows the `@AGENTS.md` reference, and explains your workspace structure and governance rules.

**Test prompt 2:**

```
Show me the exact format I should use to create a new skill.
```

**Expected**: Claude Code references the skill format from `AGENTS.md` and shows you the YAML frontmatter + markdown structure.

If Claude Code responds with your vault-specific information, **your General Agent is configured**.

---

## Step 6: Create the Folder Structure

Now that Claude Code understands your workspace, create the folders:

```bash
mkdir -p .claude/skills
mkdir -p .claude/agents
mkdir -p references
```

**But wait** — you can't see `.claude` in Obsidian. Folders starting with `.` are hidden by default.

---

## Step 7: Enable Hidden Files in Obsidian

To see and edit `.claude/skills/` directly in Obsidian, install the Show Hidden Files plugin.

### Part A: Enable Hidden Folders

1. In Obsidian, click **Settings** (gear icon, bottom-left)
2. Click **"Files and links"**
3. Enable **"Show hidden folders"**

### Part B: Install the Plugin

1. Go to [github.com/polyipseity/obsidian-show-hidden-files/releases/tag/2.5.0](https://github.com/polyipseity/obsidian-show-hidden-files/releases/tag/2.5.0)
2. Download: `main.js`, `manifest.json`, `styles.css`
3. Open your vault folder in Finder/Explorer
4. Create: `.obsidian/plugins/show-hidden-files/`
5. Copy the 3 downloaded files into that folder
6. Create `data.json` in the same folder:

```json
{
  "errorNoticeTimeout": 0,
  "language": "",
  "noticeTimeout": 5,
  "openChangelogOnUpdate": true,
  "showConfigurationFolder": true,
  "showHiddenFiles": true,
  "showingRules": [
    "+/",
    "-/\\.git(?:\\/|$)/u",
    "-/\\.venv(?:\\/|$)/u"
  ]
}
```

### Part C: Enable the Plugin

1. Go to **Settings** → **Community plugins**
2. Click **"Turn on community plugins"**
3. Toggle **"Show Hidden Files"** ON
4. Restart Obsidian

**Result**: You can now see `.claude/skills/` and `.claude/agents/` in Obsidian's file explorer.

---

## Why No MCP for Obsidian?

You might wonder: "Why not use an Obsidian MCP server to connect Claude Code to my vault?"

**Answer**: We're proving value with the simplest approach first.

| Approach | Complexity | Value |
|----------|------------|-------|
| **Direct filesystem (what we did)** | Zero setup | Claude Code already reads files |
| MCP server | Extra dependency | Same result, more moving parts |

Claude Code can already:
- Read your `CLAUDE.md` and `AGENTS.md`
- Create files in `.claude/skills/`
- Execute skills you define

MCP adds value when you need **actions Claude Code can't do natively** (like sending emails via Gmail MCP in Email-5). For reading/writing files in your vault, the filesystem is the simplest interface.

**Principle**: Prove value first, add complexity only when needed.

---

## (Optional) Git Version Control

If you want institutional memory — tracking every change to your skills and agents:

```bash
cd ~/projects/skills-lab
git init
git add .
git commit -m "Initialize skills-lab vault"
```

This is good practice but not required for the Email series.

---

## Your Setup Complete

```
skills-lab/
├── .claude/
│   ├── skills/         ← Visible in Obsidian, ready for Email-1
│   └── agents/         ← Visible in Obsidian, ready for Email-4
├── .obsidian/
│   └── plugins/
│       └── show-hidden-files/
├── references/
├── AGENTS.md           ← Governance rules
└── CLAUDE.md           ← Entry point for Claude Code
```

**What you have:**

- **Obsidian** = Human interface for reading/writing markdown
- **Claude Code** = General Agent that operates in the same files
- **AGENTS.md** = Single source of truth for governance
- **CLAUDE.md** = Entry point that references AGENTS.md

Same files. Different interfaces. No translation layer.

---

## Try With AI

**Prompt 1: Verify Governance**

```
Read my AGENTS.md and tell me: What are my governance rules? What format should skills use?
```

**What you're practicing**: Confirming Claude Code reads and follows your governance file.

**Prompt 2: Create First Structure**

```
Based on my AGENTS.md, create the folder structure I need for skills and agents if it doesn't exist.
```

**What you're practicing**: Having Claude Code execute based on your governance rules.

**Prompt 3: Skill Preview**

```
I'm about to create an email-drafter skill. Based on my AGENTS.md skill format, show me exactly what the file should look like and where it should go.
```

**What you're practicing**: Verifying Claude Code understands your skill conventions before you start Email-1.
