---
sidebar_position: 5
title: "Lesson 5: Your Employee's Memory"
description: "Customize your AI Employee with SOUL.md, AGENTS.md, and workspace configuration to create a personalized, persistent assistant"
keywords: [openclaw workspace, soul.md, agents.md, bootstrap files, ai persona, workspace configuration, memory]
chapter: 11
lesson: 5
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Memory Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can customize bootstrap files and verify changes take effect in conversation"

  - name: "Workspace Structure Understanding"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Can identify which files serve which purpose in the workspace directory"

  - name: "Persona Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can design and implement a custom persona through SOUL.md configuration"

learning_objectives:
  - objective: "Identify the purpose of each bootstrap file in the workspace"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Match each file to its purpose from memory"

  - objective: "Create custom SOUL.md and AGENTS.md files for a specific use case"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Produce working configuration files that change agent behavior"

  - objective: "Verify that persona changes take effect in conversation"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Test conversation confirms new persona is active"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (workspace structure, bootstrap files, persona configuration, memory system) within B1 range (3-5)"

differentiation:
  extension_for_advanced: "Create a complex multi-domain persona with conditional behaviors based on context"
  remedial_for_struggling: "Start with just SOUL.md, verify it works, then add AGENTS.md incrementally"
---

# Your Employee's Memory

In Lesson 4, you saw how the gateway processes your messages and maintains sessions. But your AI Employee arrived as a blank slate, with no idea who you are, what you do, or how you prefer to work. That changes now.

Every human employee has a personality, preferences, and institutional knowledge that shapes how they work. Your AI Employee is no different. The difference is that you get to design these characteristics explicitly rather than discovering them over months of working together.

This lesson shows you how to give your AI Employee its identity. You will create configuration files that define its persona, operating instructions, and daily routines. By the end, you will have transformed a generic assistant into a customized employee that knows your name, understands your work, and operates according to your rules.

## The Workspace: Your Employee's Home

Your AI Employee has a dedicated workspace on your machine. This is its home directory, where it stores everything it needs to know about itself and you.

**Default location**: `~/.openclaw/workspace/`

This workspace is separate from the configuration directory (`~/.openclaw/`) that stores credentials, session transcripts, and system settings. Think of it this way:

| Directory | What It Contains | Who Manages It |
|-----------|-----------------|----------------|
| `~/.openclaw/` | System config, credentials, session logs | OpenClaw automatically |
| `~/.openclaw/workspace/` | Persona, instructions, memory | You explicitly |

The workspace is where you define who your AI Employee is and how it should behave. Everything you put here becomes part of its context every time you start a conversation.

## Bootstrap Files: Loaded Every Session

When you start a conversation with your AI Employee, OpenClaw loads several files from the workspace into the session. These files are called bootstrap files because they establish the foundation for every interaction.

| File | Purpose | When Loaded |
|------|---------|-------------|
| `SOUL.md` | Persona, tone, boundaries | Every session |
| `AGENTS.md` | Operating instructions, routines | Every session |
| `USER.md` | Who you are, how to address you | Every session |
| `IDENTITY.md` | Agent's name, emoji, vibe | Every session |
| `TOOLS.md` | Notes about available tools | Every session |
| `BOOTSTRAP.md` | One-time first-run setup | First session only |
| `memory/YYYY-MM-DD.md` | Daily memory logs | Read on session start |

Each file serves a distinct purpose. Let's examine the three most important ones you will customize.

### SOUL.md: The Personality Definition

`SOUL.md` defines who your AI Employee is at its core. This file establishes:

- **Persona**: What role does it play? What is it good at?
- **Tone**: How does it communicate? Formal or casual?
- **Boundaries**: What will it refuse to do?

When you ask your AI Employee "Who are you?", it draws its answer from this file.

### AGENTS.md: The Operating Manual

`AGENTS.md` contains the operating instructions. Think of it as the employee handbook your AI reads on day one:

- **Daily routines**: What should it check or do regularly?
- **Tools and methods**: How should it use its capabilities?
- **Memory protocol**: How should it record and use information?

This file tells your AI Employee how to do its job, not just what its job is.

### USER.md: The Employee Dossier on You

`USER.md` describes you, the employer. Your AI Employee reads this to understand:

- Your name and how you prefer to be addressed
- Your role and what you do
- Your communication preferences
- Any context that helps it serve you better

## Hands-On: Create Your Branding Expert

Let's transform your AI Employee into a branding expert. You will create configuration files that give it a specific identity and purpose.

### Step 1: Navigate to the Workspace

Open your terminal and navigate to the workspace:

```bash
cd ~/.openclaw/workspace
```

List the current contents:

```bash
ls -la
```

**Output:**
```
total 24
drwxr-xr-x  5 user  staff   160 Jan 15 10:30 .
drwxr-xr-x  8 user  staff   256 Jan 15 09:15 ..
-rw-r--r--  1 user  staff   142 Jan 15 09:15 IDENTITY.md
-rw-r--r--  1 user  staff    89 Jan 15 09:15 TOOLS.md
drwxr-xr-x  2 user  staff    64 Jan 15 09:15 memory
```

You may see default files created during setup, or the directory may be sparse. Either is fine.

### Step 2: Create SOUL.md

Create the persona definition file:

```bash
nano SOUL.md
```

Enter the following content:

```markdown
# Soul

You are a Branding Expert AI Employee named "BrandBot".

## Persona

- Creative, strategic thinker who sees the big picture
- Specializes in YouTube content strategy, trend analysis, and video themes
- Direct and actionable communication style
- Brings industry insights without being asked

## Tone

- Professional but approachable
- Uses industry terminology naturally when helpful
- Proactive: suggests improvements and opportunities
- Concise: respects that time is valuable

## Boundaries

- Never make financial decisions without explicit approval
- Never publish or post content without confirmation
- Always cite sources when referencing trend data or statistics
- Acknowledge uncertainty rather than guessing at data
```

Save and exit (Ctrl+X, then Y, then Enter in nano).

**What each section does:**

| Section | Purpose |
|---------|---------|
| Persona | Defines expertise and working style |
| Tone | Sets communication expectations |
| Boundaries | Establishes hard limits on behavior |

### Step 3: Create AGENTS.md

Create the operating instructions file:

```bash
nano AGENTS.md
```

Enter the following content:

```markdown
# Operating Instructions

## Daily Routine

When starting a session or asked to "catch up":

1. Check YouTube trends in your assigned niche
2. Review competitor activity if specified
3. Draft 3-5 content ideas based on findings
4. Summarize insights in daily memory

## Research Protocol

When researching trends or topics:

1. Use web search to find current data
2. Cross-reference multiple sources
3. Note publication dates (prioritize recent content)
4. Flag when data might be outdated

## Content Development

When helping with content:

1. Start with strategic objectives (why this content?)
2. Research what's working in the space
3. Propose specific angles with rationale
4. Suggest titles, thumbnails concepts, and hooks

## Memory Protocol

- Write daily summaries to `memory/YYYY-MM-DD.md`
- Tag important insights with #important
- Reference previous memory when relevant
- Keep summaries actionable, not just informational
```

Save and exit.

### Step 4: Create USER.md

Create your personal profile:

```bash
nano USER.md
```

Enter content customized to you:

```markdown
# User Profile

- **Name**: [Your name]
- **Preferred address**: [How you want to be called]
- **Role**: Content creator and entrepreneur
- **Focus area**: [Your niche or industry]

## Communication Preferences

- Prefer bullet points over long paragraphs
- Value direct recommendations over options lists
- Like to understand the "why" behind suggestions

## Current Projects

- [List any ongoing projects relevant to the AI's work]

## Goals

- [What you're trying to achieve in the next 3-6 months]
```

Save and exit.

### Step 5: Verify the Configuration

List your workspace files to confirm everything is in place:

```bash
ls -la ~/.openclaw/workspace/
```

**Output:**
```
total 40
drwxr-xr-x  7 user  staff   224 Jan 15 11:00 .
drwxr-xr-x  8 user  staff   256 Jan 15 09:15 ..
-rw-r--r--  1 user  staff   612 Jan 15 11:00 AGENTS.md
-rw-r--r--  1 user  staff   142 Jan 15 09:15 IDENTITY.md
-rw-r--r--  1 user  staff   756 Jan 15 10:45 SOUL.md
-rw-r--r--  1 user  staff    89 Jan 15 09:15 TOOLS.md
-rw-r--r--  1 user  staff   423 Jan 15 11:00 USER.md
drwxr-xr-x  2 user  staff    64 Jan 15 09:15 memory
```

## Testing Your Customization

Now verify that your AI Employee has adopted its new persona.

### Restart the Gateway

For changes to take effect, restart the gateway:

```bash
# If running as a service
systemctl --user restart openclaw-gateway

# Or if running manually, stop and restart it
# (Ctrl+C the running gateway, then)
openclaw gateway run --port 18789
```

### Test the Persona

Send a message through Telegram (or your configured channel):

```
Who are you and what do you do?
```

Your AI Employee should respond with information from `SOUL.md`, mentioning its role as a branding expert, its name "BrandBot," and its focus on YouTube content strategy.

**Expected response pattern:**

> I'm BrandBot, your Branding Expert AI Employee. I specialize in YouTube content strategy, trend analysis, and helping you develop video themes that resonate with your audience. I take a strategic approach, looking at the big picture while providing direct, actionable recommendations...

If the response still sounds generic, verify:

1. The files are saved in the correct location (`~/.openclaw/workspace/`)
2. The gateway was restarted after changes
3. The file names are exactly as shown (case-sensitive)

### Test the Memory Protocol

Ask your AI Employee to check trends and save findings:

```
Check current YouTube trends in tech reviews and save a summary to memory.
```

After it completes, verify the memory file was created:

```bash
ls ~/.openclaw/workspace/memory/
```

**Output:**
```
2026-02-05.md
```

Read the memory file:

```bash
cat ~/.openclaw/workspace/memory/2026-02-05.md
```

You should see a summary of the research with the format specified in your `AGENTS.md`.

## How Memory Persists

Your AI Employee maintains memory through the daily log files in the `memory/` directory. Here is how the system works:

**Session Start:**
1. Gateway loads all bootstrap files (SOUL, AGENTS, USER, etc.)
2. Gateway reads today's memory file if it exists
3. Gateway may read yesterday's memory for continuity
4. All this context enters the conversation

**During Session:**
- Your AI Employee can write to the daily memory file
- Memory entries accumulate throughout the day
- Important insights can be tagged for easy reference

**Across Sessions:**
- Each new session reads the same memory files
- Your AI Employee remembers what it learned yesterday
- Context persists even after the gateway restarts

This creates continuity that basic chat interfaces lack. Your AI Employee builds institutional knowledge over time.

## Session Storage (Separate from Memory)

Sessions themselves are stored separately from workspace memory:

| Storage | Location | Purpose |
|---------|----------|---------|
| Memory | `~/.openclaw/workspace/memory/` | Curated knowledge you control |
| Sessions | `~/.openclaw/agents/<id>/sessions/` | Raw conversation transcripts |

Sessions are stored as JSONL files containing the full conversation history. You generally do not need to edit these directly, but they are available for debugging or analysis.

## Try With AI

### Prompt 1: Persona Verification

```
Tell me about yourself. What's your personality? What are you particularly good at?
How do you prefer to work with me?
```

**What you're learning:** This prompt tests whether your SOUL.md configuration loaded correctly. You are evaluating if the persona you designed actually manifests in conversation. Pay attention to whether it mentions specific traits you defined versus generic assistant responses.

### Prompt 2: Memory Exploration

```
What do you remember about our previous conversations? Check your memory files
and tell me what you know about the work we've done together.
```

**What you're learning:** This prompt tests the memory system. You are discovering how your AI Employee accesses and uses stored context. It reveals whether daily memory files are being created and read. If it says it has no memory, troubleshoot the memory directory permissions.

### Prompt 3: Persona Modification Discussion

```
I want to adjust your personality. Right now you're a branding expert, but I also
need you to help with email management. How would I modify your configuration files
to add this capability while keeping your branding expertise?
```

**What you're learning:** This prompt tests understanding of the configuration system. Your AI Employee should explain that you would edit SOUL.md to add email expertise to the persona, and update AGENTS.md with email-specific operating instructions. This confirms it understands its own architecture.

**Important:** When testing, verify changes by restarting the gateway after each configuration edit. Bootstrap files are loaded at session start, so changes during a session will not take effect until the next session.
