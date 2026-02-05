---
sidebar_position: 15
title: "Lesson 15: Chapter Assessment"
description: "Quiz and portfolio submission for Chapter 11 certification"
keywords: [assessment, quiz, portfolio, certification, chapter 11, ai employee]
chapter: 11
lesson: 15
duration_minutes: 60

# HIDDEN SKILLS METADATA
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

You have built an AI Employee. You taught it to draft emails, use professional templates, summarize threads, and access Gmail through MCP. Now it is time to verify your understanding and document what you have created.

This assessment has two parts: a knowledge check that tests your understanding of the concepts, and a portfolio submission that demonstrates your practical skills. Both parts matter. Understanding without building is theory. Building without understanding is fragile. Together, they prove you can create and maintain AI Employees.

## Part 1: Knowledge Check Quiz

This quiz covers concepts from all 14 lessons. Each question has one correct answer. Aim for 70% or higher to demonstrate solid understanding.

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

### Section B: Technical (Questions 6-15)

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

**Question 8**: In a SKILL.md file, which frontmatter field indicates when the skill should be activated?

- a) `triggers`
- b) `activation`
- c) `description`
- d) `dependencies`

**Question 9**: What is the purpose of the `memory/` directory in the workspace?

- a) Cache LLM responses for faster retrieval
- b) Store daily memory logs that persist across sessions
- c) Keep backup copies of configuration files
- d) Store temporary conversation fragments

**Question 10**: Which MCP server enables your AI Employee to read and send Gmail?

- a) `mcp-server-email`
- b) `google-mail-mcp`
- c) `gmail-mcp-server`
- d) `mcp-gmail`

**Question 11**: What happens when you create a watcher for Gmail?

- a) Your AI Employee checks email only when you ask
- b) Your AI Employee monitors Gmail continuously and acts on new messages
- c) Gmail sends push notifications to your terminal
- d) Email attachments are automatically downloaded

**Question 12**: In HITL (Human-in-the-Loop) approval workflows, what does the approval file contain?

- a) The complete conversation history
- b) A pending action description awaiting your yes/no
- c) Encrypted credentials for the action
- d) Performance metrics for the AI Employee

**Question 13**: Which process manager is recommended for keeping your AI Employee running 24/7?

- a) systemd only
- b) PM2
- c) Docker Compose only
- d) cron

**Question 14**: What is the purpose of the `@invoke` directive in a skill file?

- a) Call a function in your code
- b) Invoke a subagent with specific instructions
- c) Start the OpenClaw gateway
- d) Trigger a watcher manually

**Question 15**: How do you verify that a new persona took effect after editing SOUL.md?

- a) The changes are immediate, no action needed
- b) Restart the gateway and ask "Who are you?"
- c) Run `openclaw validate --persona`
- d) Wait 24 hours for the cache to refresh

### Section C: Application (Questions 16-20)

**Question 16**: Your AI Employee drafts an email but the tone is too casual. Which file should you modify?

- a) USER.md
- b) AGENTS.md
- c) SOUL.md or the email-drafter skill
- d) TOOLS.md

**Question 17**: You want your AI Employee to handle calendar scheduling in addition to email. What is the first step?

- a) Edit SOUL.md to add "calendar expert"
- b) Find or create an MCP server for calendar access
- c) Ask your AI Employee to learn scheduling
- d) Upgrade to a paid LLM tier

**Question 18**: A skill you created works on OpenClaw but you want it to also work with Claude Code. What makes this possible?

- a) Skills are proprietary to OpenClaw
- b) Skills use a portable format based on markdown
- c) You must rewrite the skill for each platform
- d) Only MCP servers are portable, not skills

**Question 19**: Your AI Employee sent an email without asking for approval first. What should you check?

- a) Whether HITL approval workflow is configured
- b) Whether your internet connection is stable
- c) Whether the LLM provider is overloaded
- d) Whether the email was in your drafts folder

**Question 20**: You want to deploy your AI Employee on Oracle Cloud free tier. What is the primary constraint?

- a) Oracle Cloud does not support Node.js
- b) ARM architecture may require different build configurations
- c) OpenClaw requires Windows Server
- d) MCP servers cannot run on cloud infrastructure

---

### Answer Key

| Question | Answer | Explanation |
|----------|--------|-------------|
| 1 | b | OpenClaw's breakthrough was autonomous action, not just conversation |
| 2 | b | SOUL.md defines persona, tone, and boundaries |
| 3 | b | Workspace > Managed > Bundled (local overrides remote) |
| 4 | b | Model Context Protocol |
| 5 | b | Subagents provide different personas or specialized focus |
| 6 | b | `openclaw gateway run --port 18789` |
| 7 | c | `~/.openclaw/workspace/` |
| 8 | c | `description` field explains when to use the skill |
| 9 | b | Daily memory logs that persist across sessions |
| 10 | c | `gmail-mcp-server` (verify your actual server name) |
| 11 | b | Continuous monitoring and autonomous action on new messages |
| 12 | b | Pending action description awaiting approval |
| 13 | b | PM2 is recommended for Node.js process management |
| 14 | b | Invoke a subagent with specific instructions |
| 15 | b | Restart gateway and verify with identity question |
| 16 | c | SOUL.md for general tone, or the specific skill for task-specific tone |
| 17 | b | MCP server provides the capability; persona changes come after |
| 18 | b | Skills are portable markdown format |
| 19 | a | HITL approval workflow controls when approval is required |
| 20 | b | Oracle Free uses ARM (Ampere) processors, which may need different builds |

**Scoring:**
- 18-20 correct: Excellent understanding
- 14-17 correct: Good understanding, review missed areas
- 10-13 correct: Adequate, focus on weak sections before continuing
- Below 10: Review lessons 1-14 before proceeding

---

## Part 2: Portfolio Requirements

Your portfolio demonstrates that you can build working AI Employees. Choose the tier that matches your goals and available time.

### Bronze Tier (Minimum Certification)

Complete these requirements to demonstrate foundational competency:

**Required Components:**

- [ ] Working email-assistant skill that invokes specialized subagents
- [ ] Three supporting skills (email-drafter, email-templates, email-summarizer)
- [ ] Gmail MCP server configured and tested
- [ ] README.md documenting your assistant's capabilities

**Verification:**
- Screenshot showing a successful email draft created through Telegram
- All skills present in `.claude/skills/` directory

### Silver Tier (Intermediate)

All Bronze requirements, plus:

- [ ] At least one watcher configured (Gmail or File)
- [ ] HITL approval workflow set up for sending emails
- [ ] USER.md customized with your actual preferences
- [ ] Memory system actively used (daily logs present in `memory/`)

**Verification:**
- Screenshot of watcher detecting a new email
- Screenshot of approval file awaiting your response

### Gold Tier (Advanced)

All Silver requirements, plus:

- [ ] 24/7 deployment running (PM2 or Oracle Cloud)
- [ ] At least one custom domain-specific skill (beyond email)
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
my-email-assistant/
├── README.md                     # Project overview and capabilities
├── skills/
│   ├── email-drafter/
│   │   └── SKILL.md
│   ├── email-templates/
│   │   └── SKILL.md
│   ├── email-summarizer/
│   │   └── SKILL.md
│   └── email-assistant/
│       └── SKILL.md
├── config/
│   └── openclaw.json.example    # Sanitized config (no secrets)
├── docs/
│   ├── setup-guide.md           # How to install and configure
│   └── architecture.md          # How the components work together
└── screenshots/
    ├── telegram-conversation.png
    └── skill-in-action.png
```

### Submission Checklist

Before submitting, verify:

- [ ] Public GitHub repository created
- [ ] All skills included with proper SKILL.md format
- [ ] README explains what your assistant can do
- [ ] No secrets committed (API keys, tokens, passwords)
- [ ] Config example file has placeholder values, not real credentials
- [ ] At least one screenshot showing your assistant in action
- [ ] Setup guide allows someone else to run your assistant

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

**Capability:**
- Can I create a new skill from scratch for a different task?
- Can I debug why a skill is not being invoked?
- Can I configure a new MCP server?

**Portability:**
- Would my skills work with Claude Code if I switched platforms?
- Did I design for portability or did I hard-code platform-specific assumptions?

If you answered "no" to any question, review the relevant lesson before submitting.

---

## What Comes Next

Completing this assessment marks the end of Chapter 11, but it is just the beginning of your AI Employee journey.

**Immediate next steps:**
- Share your repository with peers for feedback
- Try your skills on a different platform (Claude Code) to verify portability
- Identify one new workflow you want to automate next

**Advanced paths:**
- Chapter 12+: More workflow types (coding, research, writing)
- Custom domains: Adapt the email patterns to your specific industry
- Monetization: Package your skills for others to use

## Try With AI

### Prompt 1: Quiz Review

```
I just completed a 20-question quiz about AI Employees. Here are the questions I got wrong:
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
