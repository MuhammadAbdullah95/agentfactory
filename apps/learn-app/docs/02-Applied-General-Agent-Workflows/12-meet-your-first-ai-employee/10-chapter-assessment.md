---
sidebar_position: 10
title: "Lesson 10: Chapter Assessment"
description: "Quiz and portfolio submission for Chapter 12 certification"
keywords: [assessment, quiz, portfolio, certification, chapter 12, ai employee]
chapter: 12
lesson: 10
duration_minutes: 60

skills:
  - name: "Self-Assessment"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Can evaluate own work against criteria and identify areas for improvement"

  - name: "Portfolio Documentation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can create portfolio-ready documentation that demonstrates competency"

learning_objectives:
  - objective: "Demonstrate understanding of AI Employee concepts through quiz completion"
    proficiency_level: "B2"
    bloom_level: "Remember"
    assessment_method: "Quiz score of 70% or higher"
  - objective: "Create portfolio-ready documentation of your AI Employee project"
    proficiency_level: "B2"
    bloom_level: "Create"
    assessment_method: "Portfolio review against checklist"
  - objective: "Self-assess work quality against defined criteria"
    proficiency_level: "B2"
    bloom_level: "Evaluate"
    assessment_method: "Checklist completion with self-reflection"

cognitive_load:
  new_concepts: 0
  assessment: "Low - review and synthesis of previously learned concepts"

differentiation:
  extension_for_advanced: "Submit Gold tier portfolio with 24/7 deployment"
  remedial_for_struggling: "Focus on Bronze tier completion before attempting quiz"
---

# Chapter Assessment

You have built an AI Employee. You taught it skills, connected it to real services, configured trust boundaries, and deployed it to run around the clock. Now it is time to verify your understanding and document what you have created.

This assessment has two parts: a knowledge check that tests your understanding of the concepts, and a portfolio submission that demonstrates your practical skills. Both parts matter. Understanding without building is theory. Building without understanding is fragile. Together, they prove you can create and maintain AI Employees.

## Part 1: Knowledge Check Quiz

This quiz covers concepts from lessons 1 through 9. Each question has one correct answer. Aim for 70% or higher to demonstrate solid understanding.

### Section A: Concepts (Questions 1-5)

**Question 1**: What distinguished OpenClaw from previous AI chatbots in the eyes of the market?

- a) Better language understanding
- b) Acting autonomously on the user's behalf
- c) Faster response times
- d) Lower cost per interaction

**Question 2**: Which file defines your AI Employee's personality and boundaries?

- a) AGENTS.md
- b) SOUL.md
- c) USER.md
- d) TOOLS.md

**Question 3**: What is the correct precedence order for skills when multiple locations have the same skill?

- a) Bundled > Managed > Workspace
- b) Workspace > Managed > Bundled
- c) Managed > Workspace > Bundled
- d) All skills have equal priority

**Question 4**: What does MCP stand for?

- a) Model Configuration Protocol
- b) Model Context Protocol
- c) Machine Communication Protocol
- d) Multi-Channel Protocol

**Question 5**: When should you use a subagent instead of a skill?

- a) For any complex task
- b) When you need a different persona or specialized focus
- c) Always prefer subagents over skills
- d) Only for simple, single-step tasks

### Section B: Technical (Questions 6-11)

**Question 6**: Which command starts the OpenClaw gateway on port 18789?

- a) `openclaw start --port 18789`
- b) `openclaw gateway run --port 18789`
- c) `openclaw serve 18789`
- d) `openclaw init --gateway 18789`

**Question 7**: Where is the default workspace directory for OpenClaw?

- a) `/opt/openclaw/workspace/`
- b) `~/Documents/openclaw/`
- c) `~/.openclaw/workspace/`
- d) `/var/lib/openclaw/workspace/`

**Question 8**: Which two frontmatter fields are required in every SKILL.md file?

- a) `triggers` and `dependencies`
- b) `name` and `description`
- c) `activation` and `persona`
- d) `title` and `category`

**Question 9**: What is the purpose of the `memory/` directory in the workspace?

- a) Cache LLM responses for faster retrieval
- b) Store daily memory logs that persist across sessions
- c) Keep backup copies of configuration files
- d) Store temporary conversation fragments

**Question 10**: How does OpenClaw integrate with Gmail?

- a) Through a dedicated Gmail MCP server
- b) Through `gog` (gogcli) and webhooks via Google Pub/Sub
- c) Through direct IMAP/SMTP connections
- d) Through the Google Workspace API only

**Question 11**: What happens when you create a watcher for Gmail?

- a) Your AI Employee checks email only when you ask
- b) Your AI Employee monitors Gmail continuously and acts on new messages
- c) Gmail sends push notifications to your terminal
- d) Email attachments are automatically downloaded

### Section C: Application (Questions 12-15)

**Question 12**: Which process manager is recommended for keeping your AI Employee running 24/7?

- a) systemd only
- b) PM2
- c) Docker Compose only
- d) cron

**Question 13**: In OpenClaw's three-tier skill loading, what does it mean for a skill to be at Level 1?

- a) The full SKILL.md content is loaded into memory
- b) Only the skill's name and description metadata are loaded
- c) The skill's supporting files and scripts are loaded
- d) The skill is disabled until manually activated

**Question 14**: How does `sessions_spawn` behave when launching a subagent?

- a) It blocks until the subagent completes its task
- b) It is non-blocking, returns immediately, with a maximum of 8 concurrent sessions
- c) It replaces the current agent session with the subagent
- d) It queues the subagent to run after the current task finishes

**Question 15**: Your AI Employee sent a message without asking for approval first. What should you check?

- a) Whether HITL approval workflow is configured in exec-approvals.json
- b) Whether your internet connection is stable
- c) Whether the LLM provider is overloaded
- d) Whether the message was saved to drafts

---

### Answer Key

| Question | Answer | Explanation |
| -------- | ------ | ----------- |
| 1 | b | OpenClaw's breakthrough was autonomous action, not just conversation |
| 2 | b | SOUL.md defines persona, tone, and boundaries |
| 3 | b | Workspace > Managed > Bundled (local overrides remote) |
| 4 | b | Model Context Protocol |
| 5 | b | Subagents provide different personas or specialized focus via sessions_spawn |
| 6 | b | `openclaw gateway run --port 18789` |
| 7 | c | `~/.openclaw/workspace/` |
| 8 | b | `name` and `description` are the two required SKILL.md frontmatter fields |
| 9 | b | Daily memory logs that persist across sessions |
| 10 | b | Gmail integrates through `gog` (gogcli) and webhooks via Google Pub/Sub, not MCP |
| 11 | b | Continuous monitoring and autonomous action on new messages |
| 12 | b | PM2 is recommended for Node.js process management |
| 13 | b | Level 1 loads only metadata (name, description); full content loads on-demand at Level 2 |
| 14 | b | sessions_spawn is non-blocking, returns immediately, max 8 concurrent sessions |
| 15 | a | exec-approvals.json controls which actions require human approval |

**Scoring:**

- 13-15 correct: Excellent understanding
- 10-12 correct: Good understanding, review missed areas
- 7-9 correct: Adequate, focus on weak sections before continuing
- Below 7: Review lessons 1-9 before proceeding

---

## Part 2: Portfolio Requirements

Your portfolio demonstrates that you can build working AI Employees. Choose the tier that matches your goals and available time.

### Bronze Tier (Minimum Certification)

Complete these requirements to demonstrate foundational competency:

**Required Components:**

- [ ] Working skill (any domain) with proper SKILL.md format
- [ ] README.md documenting your AI Employee's capabilities
- [ ] Screenshot showing your AI Employee completing a real task

**Verification:**

- Screenshot showing a successful skill invocation through Telegram or CLI
- Skill present in workspace `skills/` directory with valid SKILL.md frontmatter

### Silver Tier (Intermediate)

All Bronze requirements, plus:

- [ ] At least one watcher configured (Gmail, File, or other)
- [ ] HITL approval workflow set up with exec-approvals.json
- [ ] USER.md customized with your actual preferences
- [ ] Memory system actively used (daily logs present in `memory/`)

**Verification:**

- Screenshot of watcher detecting a new event
- Screenshot of approval prompt awaiting your response

### Gold Tier (Advanced)

All Silver requirements, plus:

- [ ] 24/7 deployment running (PM2 or Oracle Cloud Free Tier)
- [ ] At least one custom domain-specific skill beyond the basics
- [ ] Monitoring configured (health checks, restart on failure)
- [ ] One week of operation logs demonstrating stability

**Verification:**

- `pm2 status` output or Oracle Cloud dashboard screenshot
- Log files showing multi-day operation

---

## Part 3: Submission Guidelines

### GitHub Repository Structure

Organize your portfolio repository as follows:

```
my-ai-employee/
├── README.md
├── skills/
│   ├── research-assistant/
│   │   └── SKILL.md
│   └── your-custom-skill/
│       └── SKILL.md
├── config/
│   └── openclaw.json.example
├── docs/
│   ├── setup-guide.md
│   └── architecture.md
└── screenshots/
    └── skill-in-action.png
```

### Submission Checklist

Before submitting, verify:

- [ ] Public GitHub repository created
- [ ] All skills included with proper SKILL.md format (name and description in frontmatter)
- [ ] README explains what your AI Employee can do
- [ ] No secrets committed (API keys, tokens, passwords)
- [ ] Config example file has placeholder values, not real credentials
- [ ] At least one screenshot showing your AI Employee in action
- [ ] Setup guide allows someone else to run your AI Employee

### What NOT to Include

- `.env` files or any file with real credentials
- Session transcripts containing personal information
- Memory files with private content
- OAuth tokens or refresh tokens

---

## Part 4: Self-Assessment Reflection

Before submitting, answer these questions honestly:

**Understanding:**

- Can I explain the difference between a skill and a subagent?
- Can I describe how MCP connects my AI Employee to external services?
- Do I understand why HITL approval matters for autonomous actions?
- Can I explain the three tiers of skill loading and when each tier activates?

**Capability:**

- Can I create a new skill from scratch for a different domain?
- Can I debug why a skill is not being invoked?
- Can I configure a watcher for a new event source?
- Can I set up exec-approvals.json to control what needs human approval?

**Portability:**

- Would my skills work with Claude Code if I switched platforms?
- Did I design for portability or did I hard-code platform-specific assumptions?

If you answered "no" to any question, review the relevant lesson before submitting.

---

## What Comes Next

Completing this assessment marks the end of Chapter 12, but it is just the beginning of your AI Employee journey.

**Immediate next steps:**

- Share your repository with peers for feedback
- Try your skills on a different platform (Claude Code) to verify portability
- Identify one new workflow you want to automate next

**Advanced paths:**

- Chapter 13+: More workflow types (coding, research, writing)
- Custom domains: Adapt the patterns you learned to your specific industry
- Monetization: Package your skills for others to use

## Try With AI

### Prompt 1: Quiz Review

```
I just completed a 15-question quiz about AI Employees. Here are the questions I got wrong:
[List your incorrect answers]

For each one:
1. Explain why the correct answer is right
2. Point me to the specific lesson where this was covered
3. Give me one practical example that demonstrates the concept
```

**What you're learning:** Targeted review of concepts you did not fully grasp. The AI helps you understand not just the correct answer but why it matters in practice. This transforms quiz mistakes into learning opportunities.

### Prompt 2: Portfolio Enhancement

```
Review my AI Employee portfolio structure:
[Paste your directory tree or README]

Help me improve it by:
1. Identifying any missing documentation
2. Suggesting ways to make my skills more reusable
3. Recommending one advanced feature I could add for the next tier
4. Checking if my setup guide would work for someone new to OpenClaw
```

**What you're learning:** How to evaluate and improve your own work. You are practicing the skill of getting constructive feedback and translating it into specific improvements. This mirrors professional code review processes where external perspectives reveal blind spots.

**Safety note:** When sharing your portfolio for review, ensure you have removed all real credentials and personal information. Even in a learning context, credential hygiene matters.
