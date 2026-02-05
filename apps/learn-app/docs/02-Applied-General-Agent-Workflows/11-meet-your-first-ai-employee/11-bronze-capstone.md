---
sidebar_position: 11
title: "Lesson 11: Bronze Capstone - Email Assistant"
description: "Orchestrate all skills into a complete, portable email assistant that demonstrates the full Digital FTE pattern"
keywords: [email assistant, capstone, orchestration, portfolio, portable skills, digital fte, openclaw]
chapter: 11
lesson: 11
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Orchestration"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Can create orchestrator skills that coordinate multiple capabilities into unified workflows"

  - name: "Cross-Platform Portability"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Evaluate"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can verify skill functionality across multiple AI platforms"

  - name: "Portfolio Documentation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Communication"
    measurable_at_this_level: "Can document work products for professional portfolio presentation"

learning_objectives:
  - objective: "Create an orchestrator skill that coordinates multiple email capabilities"
    proficiency_level: "B2"
    bloom_level: "Create"
    assessment_method: "Working orchestrator that handles multiple command types"
  - objective: "Verify cross-platform portability by testing skills in multiple environments"
    proficiency_level: "B2"
    bloom_level: "Evaluate"
    assessment_method: "Demonstration of identical behavior across OpenClaw and Claude Code"
  - objective: "Document work for professional portfolio presentation"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Complete README documenting capabilities and platforms tested"

cognitive_load:
  new_concepts: 2
  assessment: "2 concepts (orchestration patterns, portfolio documentation) - low load since this integrates existing knowledge"

differentiation:
  extension_for_advanced: "Add calendar integration for meeting scheduling; create approval workflows for sensitive emails"
  remedial_for_struggling: "Focus on inbox briefing command only; test one platform before attempting cross-platform"
---

# Bronze Capstone: Your Complete Email Assistant

You have skills. You have MCP access. Now you orchestrate.

Over the past lessons, you built individual capabilities: email-drafter for composing messages, email-templates for professional formats, email-summarizer for analyzing content. You created subagents that specialize in different aspects of email work. You connected to real Gmail through MCP.

Each piece works on its own. But an AI Employee does not hand you puzzle pieces and expect you to assemble them. It takes a simple command, coordinates the right capabilities, and delivers complete results. That is what you will build now.

This lesson brings everything together into a single orchestrator skill that transforms your collection of tools into a unified email assistant. More importantly, you will verify that everything you built is truly portable: one skill file, working identically across OpenClaw, Claude Code, and any AgentSkills-compatible platform.

By the end, you will have portfolio-ready work: a documented AI Employee that demonstrates the complete Digital FTE pattern.

---

## What Makes a Capstone

A capstone is not just "the last lesson." It proves integration:

| Building Blocks | Capstone Integration |
|-----------------|---------------------|
| Individual skills | Orchestrated workflow |
| Separate commands | Unified interface |
| Platform-specific setup | Portable documentation |
| Working code | Portfolio-ready presentation |

You have built the blocks. Now you prove they compose into something greater.

---

## Inventory: What You Built

Before creating the orchestrator, confirm your components are in place:

| Component | Lesson | Location | Purpose |
|-----------|--------|----------|---------|
| email-drafter | L06 | `~/.openclaw/skills/email-drafter/` | Compose emails with proper structure |
| email-templates | L07 | `~/.openclaw/skills/email-templates/` | Apply professional formats |
| email-summarizer | L08 | `~/.openclaw/skills/email-summarizer/` | Analyze and extract insights |
| Subagents | L09 | `~/.openclaw/workspace/agents/` | Specialist delegation |
| Gmail MCP | L10 | `~/.openclaw/config.yaml` | Real email access |

Verify each component exists:

```bash
ls ~/.openclaw/skills/
```

**Output:**
```
email-drafter/
email-templates/
email-summarizer/
```

If any skills are missing, return to the relevant lesson to create them before proceeding.

---

## Create the Email Assistant Orchestrator

The orchestrator is a skill that knows about all your other skills and coordinates them based on high-level commands.

### Step 1: Create the Skill Directory

```bash
mkdir -p ~/.openclaw/skills/email-assistant
```

### Step 2: Create the SKILL.md File

Create `~/.openclaw/skills/email-assistant/SKILL.md` with this content:

```markdown
---
name: email-assistant
description: Complete email management assistant orchestrating all email skills. This skill should be used when users want to manage their inbox, triage emails, draft responses, or get briefings on their email status.
metadata: { "openclaw": { "always": true } }
---

# Email Assistant

You are a complete email management assistant. You orchestrate multiple capabilities to handle any email-related task.

## Available Capabilities

Your toolkit includes:

- **email-drafter**: Compose new emails with proper structure
- **email-templates**: Apply professional formats (status update, client follow-up, project kickoff)
- **email-summarizer**: Analyze emails to extract key information
- **Gmail MCP**: Access real email data (read, search, send)

## Command Reference

### "Inbox briefing" or "Check my email"

Full inbox analysis:

1. Fetch unread emails via Gmail MCP
2. Categorize by priority:
   - **Urgent**: Requires response within hours
   - **Important**: Requires response within 24-48 hours
   - **FYI**: No response needed, awareness only
3. Summarize each urgent item (using email-summarizer)
4. Identify action items with deadlines
5. Present organized summary

### "Process email from [sender]"

Handle a specific email:

1. Find the latest email from that sender
2. Summarize content and extract:
   - Main request or information
   - Any deadlines mentioned
   - Required action from you
3. Recommend action: respond, forward, archive, or ignore
4. If respond: draft response using appropriate template

### "Email [recipient] about [topic]"

Compose new email:

1. Check for existing thread with recipient
2. If thread exists: draft reply maintaining context
3. If new conversation: draft fresh email
4. Apply email-drafter structure
5. Apply appropriate template (email-templates)
6. Present draft for review before sending

### "Weekly email report"

Summary and analysis:

1. Count emails sent and received this week
2. Identify threads needing follow-up
3. Highlight important communications
4. Note any overdue responses
5. Present actionable summary

## Safety Rules

These boundaries protect both you and me:

- **Never send without confirmation**: Always show draft and ask "Send this?" before transmitting
- **Flag sensitive content**: Pause for approval on financial discussions, HR matters, legal topics, or confidential projects
- **Acknowledge limitations**: If you cannot access something or are unsure, say so
- **Preserve context**: When drafting replies, maintain the thread's tone and history
```

### Step 3: Verify the Orchestrator

Check the file was created correctly:

```bash
cat ~/.openclaw/skills/email-assistant/SKILL.md | head -30
```

**Output:**
```
---
name: email-assistant
description: Complete email management assistant orchestrating all email skills. This skill should be used when users want to manage their inbox, triage emails, draft responses, or get briefings on their email status.
metadata: { "openclaw": { "always": true } }
---

# Email Assistant

You are a complete email management assistant. You orchestrate multiple capabilities to handle any email-related task.

## Available Capabilities
...
```

---

## Test the Complete System

### Restart to Load the Skill

```bash
openclaw gateway restart
```

Or start a new Telegram conversation.

### Test 1: Morning Briefing

Send this to your AI Employee:

```
Give me my inbox briefing
```

**Expected behavior:**

1. Fetches unread emails from Gmail
2. Categorizes each by priority
3. Summarizes urgent items
4. Presents organized list with recommended actions

If this works, your orchestrator successfully coordinates Gmail MCP with email-summarizer.

### Test 2: Full Email Workflow

Test the complete process:

```
Process the most urgent email and draft a response
```

**Expected behavior:**

1. Identifies the most urgent unread email
2. Summarizes its content
3. Recommends a response approach
4. Drafts a reply using appropriate template
5. Presents draft for your approval

This tests all skills working together: Gmail MCP, email-summarizer, email-drafter, and email-templates.

### Test 3: Proactive Draft

Test new email composition:

```
Email my team about the project deadline moving to Friday. Use the status update template.
```

**Expected behavior:**

1. Applies email-drafter structure
2. Uses status update template from email-templates
3. Shows draft before sending
4. Waits for your confirmation

---

## Verify Portability

The real test of portable skills: do they work elsewhere?

### Copy to Claude Code

If you have Claude Code installed:

```bash
# Create Claude Code skills directory if it doesn't exist
mkdir -p ~/.claude/skills/email-assistant

# Copy the orchestrator
cp ~/.openclaw/skills/email-assistant/SKILL.md ~/.claude/skills/email-assistant/

# Copy the component skills
cp -r ~/.openclaw/skills/email-drafter ~/.claude/skills/
cp -r ~/.openclaw/skills/email-templates ~/.claude/skills/
cp -r ~/.openclaw/skills/email-summarizer ~/.claude/skills/
```

### Test in Claude Code

Start Claude Code and test the same commands:

```bash
claude
```

Then in Claude Code:

```
Give me my inbox briefing
```

**What you're verifying:** The skill file format works identically. The same YAML frontmatter, the same markdown instructions, the same behavior.

Note: Gmail MCP access depends on MCP configuration in each platform. The skills themselves are portable; the external connections require setup per platform.

### Portability Results

Record what works across platforms:

| Feature | OpenClaw | Claude Code |
|---------|----------|-------------|
| Skill loading | Yes/No | Yes/No |
| Command recognition | Yes/No | Yes/No |
| Template application | Yes/No | Yes/No |
| MCP integration | Yes/No | Requires config |

If skills load and commands work identically, you have achieved true portability.

---

## Document for Portfolio

Your email assistant is portfolio-ready work. Document it properly.

### Create a README

Create `~/.openclaw/skills/email-assistant/README.md`:

```markdown
# Email Assistant

A portable AI Employee for comprehensive email management.

## Overview

This project demonstrates the Digital FTE pattern: a specialized AI assistant that handles complete workflows, not just individual tasks.

## Capabilities

| Capability | Command | Skill Used |
|------------|---------|------------|
| Inbox analysis | "Inbox briefing" | email-summarizer |
| Email processing | "Process email from [sender]" | email-summarizer, email-drafter |
| Composition | "Email [recipient] about [topic]" | email-drafter, email-templates |
| Reporting | "Weekly email report" | email-summarizer |

## Skills Included

- **email-assistant** (orchestrator): Coordinates all capabilities
- **email-drafter**: Professional email composition
- **email-templates**: Format library (status update, client follow-up, etc.)
- **email-summarizer**: Content analysis and extraction

## Platform Compatibility

| Platform | Status | Notes |
|----------|--------|-------|
| OpenClaw | Tested | Full functionality |
| Claude Code | Tested | Skills work; MCP requires config |
| Claude Cowork | Untested | Expected compatible |

## Installation

1. Copy skills to platform skill directory:
   ```bash
   cp -r skills/* ~/.openclaw/skills/  # For OpenClaw
   cp -r skills/* ~/.claude/skills/    # For Claude Code
   ```

2. Configure MCP for email access (platform-specific)

3. Restart platform to load skills

## Usage Examples

### Morning routine
```
Give me my inbox briefing
```

### Handle specific email
```
Process the email from [client name] and draft a response
```

### New email
```
Email [recipient] about [topic] using the [template] template
```

## Safety Features

- Drafts shown before sending
- Sensitive content flagged
- No automatic sends without confirmation

## Author

[Your name]
Built as part of The AI Agent Factory curriculum
```

---

## What You Accomplished

This capstone demonstrates:

**Integration**: Four separate skills coordinate through one orchestrator
**Portability**: Same files work across platforms
**Safety**: Clear boundaries and confirmation workflows
**Documentation**: Portfolio-ready presentation

You did not just learn about AI Employees. You built one. You tested it with real email. You verified it works anywhere.

This is the Bronze level: a functional, portable AI Employee handling a complete domain. The patterns you learned here scale to any expertise you want to encode.

---

## Try With AI

### Prompt 1: Full Workflow Test

```
Good morning! Give me my inbox briefing, identify what needs my attention today, and draft responses for anything urgent.
```

**What you're learning:** This tests the complete orchestration loop. Your AI Employee must coordinate Gmail access, prioritization logic, summarization, and drafting, then present it all coherently. Watch how it sequences the operations and maintains context across steps.

### Prompt 2: Edge Case Handling

```
I need to send a sensitive email to HR about a personnel issue. Help me draft it appropriately.
```

**What you're learning:** This tests your safety rules. The orchestrator should recognize "HR" and "personnel issue" as sensitive content and flag it for special handling. It should not proceed with a standard template but instead acknowledge the sensitivity and ask for guidance on tone and content.

### Prompt 3: Adaptation Request

```
I want to add a new command to my email assistant: "Email cleanup" that archives anything older than 30 days that I haven't responded to. How would I modify the skill to add this?
```

**What you're learning:** This tests whether you understand the skill architecture well enough to extend it. Your AI Employee should explain how to add a new command section to the SKILL.md file, what Gmail MCP operations it would need, and any safety considerations for bulk archiving.

**Safety reminder:** When testing with real email data, ensure you have drafts-only mode or use a test account. The orchestrator's safety rules prevent accidental sends, but practicing caution with production email is always wise.
