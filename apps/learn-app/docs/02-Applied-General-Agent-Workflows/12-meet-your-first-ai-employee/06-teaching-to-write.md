---
sidebar_position: 6
title: "Lesson 6: Teaching Your Employee to Write"
description: "Create your first portable skill - email-drafter - that works across OpenClaw, Claude Code, and any AgentSkills-compatible platform"
keywords: [openclaw skills, skill.md, email drafter, portable skills, agentskills, ai employee skills, skill creation]
chapter: 12
lesson: 6
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Skill Creation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can create a working SKILL.md file with proper YAML frontmatter and instructions"

  - name: "Skill Portability Understanding"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Can explain how skills work across different AI platforms"

  - name: "Skill Testing"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Can verify skill loading and functionality in OpenClaw"

learning_objectives:
  - objective: "Understand the SKILL.md format including YAML frontmatter and instruction structure"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Format explanation and identification of required components"
  - objective: "Create a working email-drafter skill with proper formatting and instructions"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Working skill file that OpenClaw loads successfully"
  - objective: "Verify skill portability by testing across platforms"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Cross-platform test demonstrating identical behavior"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (skill format, YAML frontmatter, skill precedence) within B1 limit of 3-5"

differentiation:
  extension_for_advanced: "Add conditional metadata gating; create a second skill with references/ directory for complex domain knowledge"
  remedial_for_struggling: "Use the exact template provided verbatim; focus on getting one skill working before customizing"
---

# Teaching Your Employee to Write

In the previous lessons, you connected to your AI Employee through Telegram and gave it tasks. The AI responded based on its general training. Now you're going to teach it something specific to YOU. Something it will remember every session. Something you can take with you to any platform.

This is the moment your AI Employee stops being a generic assistant and becomes YOUR specialized worker.

When you hire a human employee, you don't just assign tasks. You train them. You teach them how YOUR company writes emails, how YOUR team formats reports, what tone to use with YOUR clients. That training is what makes them valuable. The same principle applies to AI Employees, but with one crucial difference: the training you create is **portable**. Build it once for OpenClaw, and it works in Claude Code, Goose, or any AgentSkills-compatible platform.

---

## What Are Skills?

Skills are expertise packages. They're markdown files with a specific format that tell your AI Employee how to handle particular types of work. When you create a skill for "writing professional emails," you're encoding exactly how you want emails written: the tone, the structure, the questions to ask before drafting.

Think of skills like training manuals for a new hire:
- **Without training**: Employee uses generic approaches, requires constant correction
- **With training**: Employee follows your standards, produces consistent quality

The technical format is simple: a directory containing a `SKILL.md` file with YAML frontmatter at the top (metadata) and instructions below (the actual training).

---

## Where Skills Live (Precedence)

OpenClaw loads skills from three locations, and if names conflict, it uses the first one found:

| Priority | Location | Use Case |
|----------|----------|----------|
| **Highest** | `<workspace>/skills/` | Your current project's specific skills |
| **Middle** | `~/.openclaw/skills/` | Your personal skills (available to all agents) |
| **Lowest** | Bundled | Built-in skills shipped with OpenClaw |

This precedence system means:
- **Workspace skills** override everything (project-specific customizations)
- **Personal skills** apply everywhere you work (your standard toolkit)
- **Bundled skills** provide defaults you can override

For your first skill, we'll use the personal location (`~/.openclaw/skills/`) so it's available in every session.

---

## Hands-On: Create Your Email-Drafter Skill

Time to build something real. You'll create a skill that makes your AI Employee an expert at drafting professional emails.

### Step 1: Create the Skill Directory

Open your terminal and run:

```bash
mkdir -p ~/.openclaw/skills/email-drafter
```

**Output:**
```
(no output means success)
```

This creates the directory structure OpenClaw expects. The directory name (`email-drafter`) will be how you reference this skill.

### Step 2: Create the SKILL.md File

Create the file `~/.openclaw/skills/email-drafter/SKILL.md` with this content:

```markdown
---
name: email-drafter
description: Draft professional emails with appropriate tone and formatting. This skill should be used when users need to write emails, compose messages, or communicate professionally via email.
metadata: { "openclaw": { "always": true } }
---

# Email Drafter

You are an expert email writer. When asked to draft an email, follow this process:

## Information Gathering

Before drafting, confirm you have:

1. **Recipient**: Who is this email to? (colleague, client, manager, external)
2. **Purpose**: What's the goal? (request, follow-up, introduction, thanks, apology)
3. **Key Points**: What must be included?
4. **Tone**: Formal, professional, friendly, or urgent?

If any information is missing, ask for it before proceeding.

## Email Structure

Always include these elements:

- **Subject line**: Action-oriented, clear, under 60 characters
- **Greeting**: Appropriate to relationship and culture
- **Opening**: State purpose in first sentence
- **Body**: Supporting details, context, specifics
- **Call to action**: What do you want the recipient to do?
- **Closing**: Professional sign-off appropriate to tone

## Tone Guidelines

| Tone | Greeting | Language | Closing |
|------|----------|----------|---------|
| **Formal** | "Dear Mr./Ms. [Name]" | "I am writing to..." | "Best regards" |
| **Professional** | "Hi [First Name]" | Direct, clear | "Thanks" or "Best" |
| **Friendly** | "Hey [First Name]" | Conversational | "Cheers" or "Talk soon" |
| **Urgent** | "Hi [Name]" | "Time-sensitive:" prefix | "Please respond by [date]" |

## Output Format

Present every drafted email in this format:

```
**Subject:** [Clear, action-oriented subject]

[Greeting],

[Opening - state purpose immediately]

[Body - supporting details]

[Call to action - be specific about what you need]

[Closing],
[Sender name placeholder]
```

After the first draft, always offer: "Want me to adjust the tone, length, or emphasis?"
```

### Step 3: Verify the Skill Format

Let's confirm the structure is correct:

```bash
cat ~/.openclaw/skills/email-drafter/SKILL.md | head -20
```

**Output:**
```
---
name: email-drafter
description: Draft professional emails with appropriate tone and formatting. This skill should be used when users need to write emails, compose messages, or communicate professionally via email.
metadata: { "openclaw": { "always": true } }
---

# Email Drafter

You are an expert email writer. When asked to draft an email, follow this process:

## Information Gathering

Before drafting, confirm you have:

1. **Recipient**: Who is this email to? (colleague, client, manager, external)
2. **Purpose**: What's the goal? (request, follow-up, introduction, thanks, apology)
3. **Key Points**: What must be included?
```

---

## Testing Your Skill

### Restart to Load the Skill

Skills are loaded when a session starts. To pick up your new skill, you need to start a fresh session.

If using the OpenClaw gateway:
```bash
# Restart the gateway to reload skills
openclaw gateway restart
```

Or simply start a new conversation with your AI Employee via Telegram.

### Test the Skill

Send this message to your AI Employee:

```
Draft an email to my manager requesting a meeting to discuss my career development goals.
```

**What you should see**: Your AI Employee now asks clarifying questions based on your skill's "Information Gathering" section before drafting. It follows the structure you defined. It offers to adjust after the first draft.

Compare this to how it would have responded before: a generic email with no systematic approach.

### Verify Skill Loading

You can check which skills are loaded:

```bash
openclaw skills list
```

**Output:**
```
Loaded skills:
  - email-drafter (personal: ~/.openclaw/skills/)
  - [other skills...]
```

If `email-drafter` doesn't appear, check:
1. Directory name matches `name:` in frontmatter
2. File is named exactly `SKILL.md` (case-sensitive)
3. YAML frontmatter is valid (no syntax errors)

---

## Understanding the Skill Format

Let's break down what makes a skill work:

### YAML Frontmatter (Required)

```yaml
---
name: email-drafter
description: Draft professional emails with appropriate tone...
metadata: { "openclaw": { "always": true } }
---
```

| Field | Purpose | Notes |
|-------|---------|-------|
| `name` | Unique identifier | Lowercase, hyphens only, must match directory name |
| `description` | When to use this skill | Helps AI decide if skill applies; include trigger phrases |
| `metadata` | Platform-specific settings | `"always": true` means skill loads every session |

### Instruction Body

Everything after the frontmatter is the actual training. Write it like you're explaining to a capable new employee:
- What to do first (information gathering)
- How to structure the output
- Guidelines for variations (tone, format)
- What to offer after completion

---

## The Portability Promise

Here's where skills become powerful: they're not locked to OpenClaw.

### The AgentSkills Standard

OpenClaw uses the AgentSkills format, which is an open standard. Any platform that supports AgentSkills can use the same skill files. This includes:

- **OpenClaw** (what you're using now)
- **Claude Code** (Anthropic's CLI)
- **Other AgentSkills-compatible tools**

### Test Portability: Claude Code

If you have Claude Code installed, test the same skill there:

```bash
# Copy to Claude Code's skill location
mkdir -p ~/.claude/skills/email-drafter
cp ~/.openclaw/skills/email-drafter/SKILL.md ~/.claude/skills/email-drafter/
```

Now in Claude Code, the same skill works identically. One skill, multiple platforms.

### Why Portability Matters

| Without Portability | With Portability |
|---------------------|------------------|
| Train AI in each platform separately | Build once, use everywhere |
| Different behavior across tools | Consistent quality everywhere |
| Lost work when switching platforms | Your skills are YOUR assets |
| Vendor lock-in | Platform independence |

The skills you build are intellectual property. They encode your expertise, your standards, your way of working. They're portable because they should belong to YOU, not to any platform.

---

## What You Built

In this lesson, you:

1. **Created your first skill** - A working email-drafter that follows YOUR standards
2. **Understood skill structure** - YAML frontmatter + instruction body
3. **Learned skill precedence** - Workspace > Personal > Bundled
4. **Verified portability** - Same skill works across platforms

This is the foundation of the Digital FTE paradigm. You're not just using AI. You're training AI with reusable, portable expertise that compounds over time.

---

## Try With AI

### Prompt 1: Test Your Email Skill

```
Draft a professional email to a potential client introducing our consulting services. The client is a mid-size tech company. Keep it under 150 words.
```

**What you're learning**: You're testing whether your skill's structure (information gathering, format, tone guidelines) actually influences the output. Compare the response to what you'd get from a generic AI without the skill.

### Prompt 2: Test Edge Cases

```
I need to follow up on an unanswered email from last week. The person is a senior executive. Draft something polite but firm that creates urgency without being pushy.
```

**What you're learning**: Edge cases reveal whether your skill handles nuance. The tension between "firm" and "not pushy" requires the AI to apply your tone guidelines thoughtfully. If the result isn't right, you've found an area to improve in your skill.

### Prompt 3: Test Adaptation

```
Draft an email declining a meeting invitation politely while suggesting an alternative time next week.
```

**What you're learning**: Declining requires a different structure than requesting. You're testing whether your skill is flexible enough to handle the full range of email types, or whether you need to expand its guidelines.

**Safety reminder**: When testing email skills with real scenarios, avoid including actual confidential information. Use realistic but fictional details, or anonymize sensitive content before sharing with your AI Employee.
