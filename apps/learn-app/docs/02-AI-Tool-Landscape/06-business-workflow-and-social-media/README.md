---
slides:
  source: "https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/slides/chapter-06-slides.pdf"
  title: "Chapter 6: Claude Code for Business Workflows"
  height: 700
---

# Chapter 6: Claude Code for Business Workflows

You've learned Claude Code's features and understood MCP integration. Now it's time to set up Claude Code as a **General Agent** you'll use professionally — with an organized workspace, version-controlled skills, and real business automations.

This chapter establishes your professional Claude Code setup using Obsidian as a knowledge vault and Git for version control. You'll then build a complete Email Assistant that triages your inbox, drafts professional responses, and sends them on your behalf.

The patterns you learn here — organizing skills, building subagents, integrating MCP servers — apply to any business workflow. Email is just the first.

## Your Professional Setup

```
┌─────────────────────────────────────────────────────────────────┐
│  YOUR VAULT (Professional Claude Code Workspace)                │
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │ CLAUDE   │  │ Skills   │  │ Subagents│  │ Git      │        │
│  │ .md      │  │          │  │          │  │ History  │        │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
│                                                                  │
│  Organized workspace for building business automations          │
│                                                                  │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐    │
│  │ Email          │  │ Social Media   │  │ Document       │    │
│  │ Assistant      │  │ Manager        │  │ Processor      │    │
│  │ (This Chapter) │  │ (Future)       │  │ (Future)       │    │
│  └────────────────┘  └────────────────┘  └────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

## Before You Begin

### Prerequisites Checklist

- [ ] **Chapter 5: Claude Code Features and Workflows** (REQUIRED) — You must understand skills, subagents, MCP integration, and orchestration concepts
- [ ] **Obsidian installed** (RECOMMENDED) — Or use any folder-based approach
- [ ] **Git installed** — For version control
- [ ] **Gmail account** (optional for Email-5) — Required only if you want to connect to actual email
- [ ] **Claude Code installed and working** — From Chapter 5

### Proficiency Level

**A2 (Elementary)** — This chapter guides you through building interconnected skills with clear specifications and step-by-step collaboration patterns. Each lesson builds on the previous one.

### Estimated Time

**Total Chapter Duration**: ~4 hours

## What You'll Build

### Professional Workspace (Foundation)

- **Obsidian vault** as organized workspace
- **Git repository** for version control
- **CLAUDE.md** for project context
- **Structured folders** for skills and subagents

### Email Assistant (Email Series)

| Component | Type | Purpose |
|-----------|------|---------|
| `email-drafter` | Skill | Compose with tone control |
| `email-templates` | Skill | Variable substitution, 3 templates |
| `email-summarizer` | Skill | Thread parsing, action extraction |
| `email-assistant` | Skill | Master orchestrator |
| `inbox-triager` | Subagent | Priority classification |
| `response-suggester` | Subagent | Quick reply options |
| `follow-up-tracker` | Subagent | Deadline monitoring |
| Gmail MCP | Integration | 19 tools for real email operations |

## Lesson Navigation

### Foundation

| Lesson | Title | Duration | What You'll Build |
|--------|-------|----------|-------------------|
| [Foundation](./00-setting-up-your-ai-vault.md) | Setting Up Your AI Vault | 30 min | Professional workspace with Obsidian and Git |

### Email Workflow Series

| Lesson | Title | Duration | What You'll Build |
|--------|-------|----------|-------------------|
| [Email-1](./01-project-setup-email-drafter.md) | Project Setup & Email Drafter | 30 min | First skill with tone specification |
| [Email-2](./02-email-templates-skill.md) | Email Templates Skill | 25 min | Template system with variable substitution |
| [Email-3](./03-email-summarizer-skill.md) | Email Summarizer Skill | 25 min | Thread parsing and action extraction |
| [Email-4](./04-creating-custom-subagents.md) | Creating Custom Subagents | 35 min | 3 email processing subagents |
| [Email-5](./05-gmail-mcp-integration.md) | Gmail MCP Integration | 30 min | OAuth setup and 19 Gmail tools |
| [Email-6](./06-orchestrating-complete-system.md) | Orchestrating Complete System | 40 min | Capstone: combine everything |
| [Email-7](./07-chapter-quiz.md) | Chapter Quiz | 15 min | 15 questions on skills, subagents, MCP |

### Future Workflow Series (Planned)

| Series | Domain | What You'll Build |
|--------|--------|-------------------|
| `SMC-N` | Social Media Content | Content scheduling and management |
| `CRM-N` | Customer Relationship | Client communication automation |
| `Doc-N` | Document Processing | Document analysis and generation |

## The Bigger Picture

This chapter teaches how to organize Claude Code for **real business work**.

### The Problem

Most people use AI tools chaotically:
- Skills scattered across random folders
- No version history of what worked
- Starting fresh each conversation
- Losing accumulated knowledge

### The Solution

A professional workspace:
- **Vault as workspace** — All skills in one organized place
- **Git as history** — Every change tracked, nothing lost
- **CLAUDE.md as context** — Claude Code understands your project
- **Structured folders** — Skills and subagents where they belong

### Skills vs Subagents Decision Framework

You'll learn when to use each:

| Component | Use When | Decision Points | Example |
|-----------|----------|-----------------|---------|
| **Skill** | Guidance needed for consistent execution | 2-4 | Email tone guidelines |
| **Subagent** | Autonomous reasoning required | 5+ | Inbox triage prioritization |
| **MCP Tool** | External system integration | N/A | Gmail read/send |

### Why Email First?

Email is the ideal first project because:

1. **Universal relevance** — Everyone manages email
2. **Clear inputs and outputs** — Threads in, professional responses out
3. **Measurable improvement** — Time saved per email is quantifiable
4. **Composition opportunity** — Multiple skills naturally combine
5. **Real integration** — Gmail MCP provides actual send/receive

**By the end of this chapter**, you'll have a complete Email Assistant and, more importantly, the professional workspace pattern you'll use for all future business automations.

Let's build.
