---
sidebar_position: 6
title: "Lesson 6: Teaching Your Employee Skills"
description: "Create portable SKILL.md files that extend your AI Employee's capabilities across any platform"
keywords: [skills, SKILL.md, portable, openclaw, subagents, composition]
chapter: 12
lesson: 6
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Skill File Creation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can create a SKILL.md file with proper frontmatter and structured instructions"

  - name: "Skill Architecture Understanding"
    proficiency_level: "B2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Can explain three-tier skill loading and precedence rules"

  - name: "Subagent Delegation"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Can describe when to use subagents vs skills and invoke basic subagent patterns"

learning_objectives:
  - objective: "Create a working SKILL.md file with proper frontmatter and instructions"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student creates research-assistant skill that produces structured output"
  - objective: "Explain skill loading precedence and the three-tier architecture"
    proficiency_level: "B2"
    bloom_level: "Understand"
    assessment_method: "Student correctly predicts which skill version loads in override scenarios"
  - objective: "Distinguish between skills and subagents and choose the right pattern"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Student identifies appropriate pattern for 3 different scenarios"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (SKILL.md format, three-tier loading, skill precedence, subagents, composition) within B1-B2 cognitive limits"

differentiation:
  extension_for_advanced: "Create a multi-reference skill with scripts/ directory for automated research workflows"
  remedial_for_struggling: "Focus on creating a single simple skill with name, description, and basic instructions"
---

# Teaching Your Employee Skills

In Lesson 5, you gave your AI Employee a personality, operating instructions, and memory. Now you will give it expertise.

Your employee is only as useful as what it knows how to do. Right now, it has general capabilities from the underlying language model, but no specialized knowledge about your work. A human employee fresh out of training needs procedures, checklists, and reference materials to perform specific tasks well. Your AI Employee needs the same thing, packaged as skills.

Skills are portable. A skill you create for OpenClaw works in Claude Code, Cursor, and any platform that reads SKILL.md files. You are not building for one tool. You are building expertise that travels with you.

## Activity 1: Create Your First Skill

You will build a research-assistant skill that takes a topic and produces structured research notes. This is useful regardless of your domain, whether you research competitors, technologies, markets, or academic subjects.

### The SKILL.md Format

Every skill lives in its own directory with a `SKILL.md` file at the root:

```
research-assistant/
├── SKILL.md          # Required: instructions with YAML frontmatter
├── references/       # Optional: documentation loaded on demand
└── assets/           # Optional: templates, example files
```

The `SKILL.md` file has two parts: YAML frontmatter (metadata) and markdown body (instructions).

### Step 1: Create the Skill Directory

Navigate to your workspace skills directory:

```bash
mkdir -p ~/.openclaw/skills/research-assistant
cd ~/.openclaw/skills/research-assistant
```

**Output:**
```
(no output — directory created silently)
```

### Step 2: Write the SKILL.md File

Create the file:

```bash
nano SKILL.md
```

Enter the following content:

```markdown
---
name: research-assistant
description: "Produces structured research notes on any topic with sources, key findings, and action items"
emoji: "🔍"
---

# Research Assistant

When asked to research a topic, follow this structured process.

## Process

1. **Clarify scope**: Ask what specific aspect to focus on if the topic is broad
2. **Gather information**: Search for current, authoritative sources
3. **Structure findings**: Organize into the output format below
4. **Cite sources**: Include URLs or references for every claim
5. **Recommend next steps**: Suggest follow-up research or actions

## Output Format

Always deliver research in this structure:

### [Topic Name] — Research Summary

**Date**: [Today's date]
**Scope**: [What was investigated]

#### Key Findings
- Finding 1 (Source: [reference])
- Finding 2 (Source: [reference])
- Finding 3 (Source: [reference])

#### Analysis
[2-3 paragraphs synthesizing the findings]

#### Recommended Actions
1. [Specific action based on findings]
2. [Specific action based on findings]

#### Sources
- [Full source list with URLs]

## Quality Standards

- Prioritize sources from the last 12 months
- Flag when data might be outdated
- Distinguish between facts and opinions
- Note conflicting information across sources
```

Save and exit (Ctrl+X, then Y, then Enter in nano).

### Step 3: Verify the Skill Loads

Check that OpenClaw recognizes your new skill:

```bash
openclaw skills list
```

**Output:**
```
Available skills:
  research-assistant    Produces structured research notes on any topic...
  [other bundled skills]
```

If your skill does not appear, verify:

1. The file is at `~/.openclaw/skills/research-assistant/SKILL.md` (exact path)
2. The YAML frontmatter has both `name` and `description` fields
3. The frontmatter uses single-line values (no multi-line YAML)

For detailed information about any skill:

```bash
openclaw skills info research-assistant
```

**Output:**
```
Name: research-assistant
Description: Produces structured research notes on any topic...
Emoji: 🔍
Location: ~/.openclaw/skills/research-assistant/SKILL.md
User Invocable: true
```

### Step 4: Test the Skill

Send a message through Telegram or your configured channel:

```
Research the current state of AI-powered code review tools.
Focus on which tools are gaining traction in 2026 and why.
```

Your employee should follow the research process you defined: clarifying scope, gathering information, and delivering results in the structured format from your SKILL.md. Compare the output to your specified format. Does it include Key Findings, Analysis, Recommended Actions, and Sources sections?

If the output does not follow the structure, the skill may not have loaded. Restart the gateway and try again.

## How Skills Load: Three Tiers

Your AI Employee does not read every skill file on startup. That would waste context and slow down responses. Instead, skills load progressively through three tiers.

| Tier | What Loads | When | Cost |
|------|-----------|------|------|
| **Tier 1** (Metadata) | Only `name` and `description` from frontmatter | Session start | Near zero |
| **Tier 2** (Full skill) | Entire SKILL.md body | When agent decides skill is relevant | Moderate |
| **Tier 3** (References) | Files in `references/` directory | When specific knowledge is needed | Variable |

This progressive loading matters because context windows have limits. If your employee loaded 50 full skill files at startup, it would consume most of its available context before you said a word. Instead, it reads the one-line descriptions, decides which skills are relevant, and loads only those.

### Skill Precedence: Who Wins?

Skills can exist in three locations, listed from highest to lowest priority:

| Priority | Location | Purpose |
|----------|----------|---------|
| 1 (Highest) | `<workspace>/skills/` | Your workspace customizations |
| 2 | `~/.openclaw/skills/` | Your managed skill library |
| 3 (Lowest) | Bundled with OpenClaw | Default skills that ship with the platform |

If you create a skill named `research-assistant` in your workspace, and a bundled skill with the same name exists, your version wins. This lets you override default behavior without modifying system files.

**Practical example**: OpenClaw ships with a bundled `web-search` skill. If its default search instructions do not match your needs, create `~/.openclaw/skills/web-search/SKILL.md` with your preferred instructions. Your version takes precedence.

## Activity 2: Build a Second Skill and See Composition

Skills become more powerful when they work together. Build a second skill that complements the first.

### Create a Document Summarizer

```bash
mkdir -p ~/.openclaw/skills/document-summarizer
nano ~/.openclaw/skills/document-summarizer/SKILL.md
```

Enter:

```markdown
---
name: document-summarizer
description: "Summarizes documents into structured briefs with key points, decisions, and action items"
emoji: "📋"
---

# Document Summarizer

When asked to summarize a document, produce a structured brief.

## Process

1. Read the full document before summarizing
2. Identify the document type (meeting notes, report, article, email thread)
3. Extract key information based on type
4. Produce output in the format below

## Output Format

### Summary Brief

**Document**: [Title or description]
**Type**: [Meeting notes | Report | Article | Email thread | Other]
**Length**: [Original word count] → [Summary word count]

#### Key Points
- [Most important point]
- [Second most important point]
- [Additional key points]

#### Decisions Made
- [Decision 1 with context]
- [Decision 2 with context]
(If no decisions, state "No decisions recorded")

#### Action Items
- [ ] [Action] — Owner: [person] — Due: [date if mentioned]
(If no action items, state "No action items identified")

#### Questions Raised
- [Unanswered question 1]
- [Unanswered question 2]
(If none, state "No open questions")
```

Save and exit.

### Composition in Action

Now you have two skills. Watch what happens when you give your employee a task that requires both:

```
Research the latest trends in remote team communication tools,
then summarize your findings into a brief I can share with my team.
```

Your employee uses the research-assistant skill to gather information, then applies the document-summarizer pattern to package the findings into a shareable brief. You did not have to tell it which skills to use. It read the skill descriptions at Tier 1, recognized both were relevant, loaded them at Tier 2, and applied them in sequence.

This is composition. Small, focused skills combine to handle complex tasks. Instead of one massive "do everything" instruction set, you build modular capabilities that your employee assembles as needed.

## When Tasks Need Subagents

Skills handle most work, but some tasks are too large or too parallel for a single agent. When your employee needs to investigate three competing products simultaneously, or research a topic from multiple angles at once, it can spawn subagents.

A subagent is a separate, isolated session that runs a specific task in the background. Your main agent delegates work to subagents and continues with other tasks while they run.

### How Subagents Work

Your employee creates subagents through natural language or the `sessions_spawn` tool:

```
I need to research three competing CRM platforms in parallel.
Spawn a sub-agent for each: Salesforce, HubSpot, and Pipedrive.
Each should analyze pricing, features, and recent reviews.
```

What happens:

1. Your employee creates 3 subagent sessions (one per CRM)
2. Each subagent runs independently and concurrently
3. The `sessions_spawn` call returns immediately (non-blocking)
4. Each subagent produces its own research output
5. Your main employee collects and synthesizes the results

### Subagent Rules and Limits

| Rule | Detail |
|------|--------|
| **Concurrency** | Maximum 8 subagents at once |
| **Nesting** | Subagents cannot spawn their own subagents |
| **Tools** | Subagents have access to skills and tools but not system admin capabilities |
| **Lifetime** | Auto-archive after 60 minutes of inactivity |
| **Blocking** | Non-blocking: main agent continues working while subagents run |

### Skills vs Subagents: When to Use Each

| Scenario | Use a Skill | Use Subagents |
|----------|-------------|---------------|
| Summarize a single document | Skill (sequential, single task) | |
| Research one topic in depth | Skill | |
| Research 3 topics simultaneously | | Subagents (parallel execution) |
| Process a batch of files | | Subagents (parallel, independent) |
| Format output in a specific way | Skill (reusable template) | |
| Complex analysis needing multiple perspectives | | Subagents (each takes one angle) |

The decision rule: if the task is sequential and self-contained, use a skill. If the task benefits from parallel execution or requires isolated sessions, use subagents.

## What Professionals Build

The skills you created today are starting points. People building on OpenClaw and similar platforms have created skill libraries that transform their AI Employees into specialized teams.

Matt Wolfe, a tech creator with over a million YouTube subscribers, documented building skills for:

- **CRM management**: Skills that track leads, draft follow-ups, and update pipeline stages
- **Video production pipeline**: Skills that research topics, draft scripts, suggest thumbnails, and schedule uploads
- **Knowledge base maintenance**: Skills that ingest new articles, update summaries, and surface relevant past research
- **Competitive intelligence**: Skills that monitor competitor announcements and produce weekly briefing documents

The pattern is consistent. Each skill is small, focused, and composable. The CRM skill does not know about video production. The video pipeline skill does not handle lead tracking. But when you ask your employee to "research a video topic about our top competitor's new product launch," it composes the competitive intelligence skill with the video production skill to deliver exactly what you need.

You can browse and install community-created skills:

```bash
npx clawhub
```

**Output:**
```
ClaHub — Browse and install skills for OpenClaw

Categories:
  productivity (23 skills)
  research (15 skills)
  development (31 skills)
  content (18 skills)
  ...

Use arrow keys to browse. Press Enter to view details.
```

To install a skill directly:

```bash
npx clawhub install <skill-name>
```

This downloads the skill to your managed skills directory (`~/.openclaw/skills/`), making it available to your employee immediately.

## Try With AI

### Prompt 1: Create a Domain-Specific Skill

```
I work in [your field — e.g., marketing, software development, education, finance].
Help me create a SKILL.md file for a task I do repeatedly. The skill should:
1. Have proper YAML frontmatter with name, description, and emoji
2. Include a clear step-by-step process
3. Define a structured output format
4. Include quality standards

Walk me through each section and explain why it matters.
```

**What you're learning:** You are practicing the full SKILL.md creation workflow with AI guidance. The AI will suggest process steps and output formats tailored to your domain. Pay attention to how the AI structures the skill differently for your field compared to the generic research-assistant you built manually. This reveals how skills should be adapted to specific domains.

### Prompt 2: Debug a Skill That Will Not Load

```
I created a skill but `openclaw skills list` does not show it. Here is my setup:

Directory: ~/.openclaw/skills/my-skill/
File: SKILL.md

Frontmatter:
---
name: my-skill
description: |
  This skill helps with
  multiple things across
  different domains
---

Help me figure out why it is not loading.
```

**What you're learning:** You are practicing diagnostic reasoning about the skill loading system. The answer involves a specific technical constraint: the parser supports single-line frontmatter values only. The multi-line `description` using the YAML `|` operator breaks parsing. This kind of debugging builds real operational understanding that documentation alone does not provide.

### Prompt 3: Design a Subagent Research Team

```
I need to evaluate whether my company should adopt a new technology.
The evaluation requires:
- Technical feasibility analysis
- Cost-benefit comparison with current tools
- Team readiness assessment
- Risk identification

Design a subagent strategy that parallelizes this research.
For each subagent, specify:
- What it investigates
- What skills it should use
- What output format it should produce
- How the main agent synthesizes the results

Remember: subagents cannot spawn their own subagents,
and maximum 8 can run concurrently.
```

**What you're learning:** You are designing a delegation strategy that respects real system constraints. The AI will help you decompose a complex evaluation into parallel, independent investigations. Notice how each subagent needs a clear scope and output format so the main agent can synthesize results without ambiguity. This is the same pattern used in professional AI Employee deployments for market research, due diligence, and technical evaluations.
