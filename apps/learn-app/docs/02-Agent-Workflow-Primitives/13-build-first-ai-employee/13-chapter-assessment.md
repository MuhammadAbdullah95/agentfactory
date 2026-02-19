---
sidebar_position: 13
title: "Chapter Assessment"
sidebar_label: "L13: Assessment"
description: "Validate your Personal AI Employee knowledge with a 20-question tiered quiz covering vault setup, skills, subagents, MCP, watchers, HITL, scheduling, error recovery, and audit logging."
keywords:
  - chapter quiz
  - assessment
  - Personal AI Employee
  - Digital FTE
  - skills
  - subagents
  - MCP
  - watchers
  - HITL
  - error recovery
  - audit logging
chapter: 13
lesson: 13
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Vault Architecture Recall"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Remember"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can identify the roles of AGENTS.md and CLAUDE.md in the vault"
  - name: "Skill and Subagent Decision-Making"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can determine when to use a skill vs a subagent for a given task"
  - name: "MCP Integration Understanding"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can explain what MCP provides over direct API calls"
  - name: "Watcher Pattern Comprehension"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can describe the three watcher methods and the check-process-deposit pattern"
  - name: "HITL Governance Evaluation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can evaluate which actions require human approval and design permission boundaries"
  - name: "Error Recovery Design"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can distinguish transient from authentication errors and select recovery strategies"
  - name: "System Architecture Synthesis"
    proficiency_level: "B2"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can describe the complete pipeline from trigger to log entry across all layers"

learning_objectives:
  - objective: "Recall vault structure components and their governance roles"
    proficiency_level: "A2"
    bloom_level: "Remember"
    assessment_method: "Multiple-choice questions on AGENTS.md, CLAUDE.md, and folder purposes"
  - objective: "Distinguish between skills, subagents, and MCP servers based on task characteristics"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Scenario-based multiple-choice selecting the correct component type"
  - objective: "Evaluate permission boundaries and identify actions requiring human approval"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Multiple-choice on HITL patterns and sensitive action categories"
  - objective: "Analyze error categories and select appropriate recovery strategies"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Multiple-choice mapping error types to recovery approaches"

cognitive_load:
  new_concepts: 0
  assessment: "Assessment lesson — no new concepts introduced. Tests recall and application of concepts from L01-L12."

differentiation:
  extension_for_advanced: "After completing the quiz, design a permission boundary table for a domain not covered in the chapter (e.g., healthcare scheduling, inventory management)"
  remedial_for_struggling: "Review L00 spec sections referenced in each answer explanation before retaking the quiz"

teaching_guide:
  lesson_type: "supplementary"
  session_group: 5
  session_title: "Chapter Assessment"
  key_points:
    - "The assessment validates understanding across all three tiers — Bronze (skills, subagents, MCP), Silver (watchers, HITL, scheduling), Gold (error recovery, audit logging)"
    - "Questions test both conceptual understanding (when to use skills vs subagents) and practical application (which recovery strategy for a given error)"
    - "Students should target 80% on their tier's questions — Bronze questions are foundational for everyone"
  misconceptions:
    - "Students think they must complete Gold Tier to pass the assessment — Bronze questions (1-10) are the foundation; Silver and Gold are extensions"
    - "Students confuse the assessment with the hackathon submission — the quiz tests knowledge, the submission demonstrates working implementation"
    - "Students assume getting a wrong answer means they failed the lesson — use the answer key explanations to identify which lesson to revisit"
  discussion_prompts:
    - "Which tier did you target and why? What would change your decision if you could start over?"
    - "Which question surprised you most? What concept do you want to revisit?"
  teaching_tips:
    - "Use the Bronze questions (1-10) as a review session before the quiz — they cover the most testable concepts from L01-L07"
    - "Have students grade themselves and identify their weakest area before reviewing the answer key"
    - "The answer key references specific lessons — encourage students to revisit those lessons for any incorrect answers"
  assessment_quick_check:
    - "What are the three architecture layers from L00?"
    - "Which tier concepts does each question block cover? (1-10 Bronze, 11-16 Silver, 17-20 Gold)"

generated_by: "content-implementer"
created: "2026-02-19"
version: "1.0.0"
---

# Chapter Assessment

In Lessons 1 through 12, you built a Personal AI Employee from an empty Obsidian vault to a production-ready autonomous system. This assessment checks how well you absorbed the key concepts across all three tiers.

**Format**: 20 multiple-choice questions arranged by tier. Answer on paper or in a text file, then check yourself against the answer key at the bottom.

| Tier   | Questions | Passing | Covers                                                            |
| ------ | --------- | ------- | ----------------------------------------------------------------- |
| Bronze | 1-10      | 8/10    | Vault, skills, subagents, MCP, orchestration                      |
| Silver | 11-16     | 5/6     | Watchers, HITL, scheduling, CEO Briefing                          |
| Gold   | 17-20     | 3/4     | Error recovery, audit logging, graceful degradation, architecture |

Score yourself on the tier you completed. Bronze is the baseline everyone should pass.

---

## Bronze Tier (Questions 1-10)

### Question 1: Vault Governance

**What is the relationship between AGENTS.md and CLAUDE.md in the vault?**

A) AGENTS.md is the file Claude reads first; CLAUDE.md stores governance rules

B) CLAUDE.md is the entry point Claude reads first; AGENTS.md defines governance rules like skill and agent formats

C) Both files serve the same purpose and are interchangeable

D) AGENTS.md lists installed MCP servers; CLAUDE.md stores email templates

---

### Question 2: File-Based Memory

**Why does the Personal AI Employee use Obsidian vault files instead of a database for memory?**

A) Databases are too expensive for personal projects

B) Obsidian has a built-in AI engine that processes files automatically

C) Files are human-readable, version-controllable with git, and editable in any text editor — no special tools required

D) Claude Code can only read markdown files and has no database drivers

---

### Question 3: Skill Creation

**What are the required components of a valid SKILL.md file?**

A) A Python script with a main() function and requirements.txt

B) YAML frontmatter with `name` and `description` fields, plus a markdown body explaining when and how to use the skill

C) A JSON configuration file with `type`, `version`, and `endpoints` fields

D) An HTML template with embedded JavaScript for the skill interface

---

### Question 4: Skill Activation

**How does Claude Code know when to activate a specific skill?**

A) The user must type the exact skill filename as a command

B) Claude reads the skill's `description` field in the YAML frontmatter and matches it against the current task context

C) Skills run on a fixed schedule defined in a cron configuration

D) Claude Code loads all skills into memory at startup and runs them in sequence

---

### Question 5: Subagent vs Skill

**When should you create a subagent instead of a skill?**

A) When the task requires a different programming language

B) When the task needs autonomous reasoning, makes its own decisions, and may produce varied outputs depending on the input

C) When the task takes longer than 30 seconds to complete

D) When you want to reuse the same logic across multiple projects

---

### Question 6: Subagent YAML

**Why must subagent definition files use a single-line description?**

A) Multi-line descriptions exceed the YAML file size limit

B) The description is displayed in Claude Code's agent selector dropdown, which only renders one line

C) Multi-line descriptions can break the tool parsing that Claude Code uses to discover and invoke agents

D) Single-line descriptions load faster and reduce memory consumption

---

### Question 7: Gmail MCP Authentication

**What is the key difference between SMTP App Password and OAuth for Gmail MCP?**

A) App Password is free; OAuth requires a paid Google Workspace subscription

B) App Password gives send-only access via SMTP and takes 2 minutes to set up; OAuth gives full Gmail API access (read, search, labels, draft, send) and takes about 10 minutes

C) App Password works on Windows only; OAuth works on all platforms

D) App Password is more secure because it uses two-factor authentication

---

### Question 8: Draft-First Safety

**According to the chapter's safety protocols, which email types should ALWAYS go through draft review before sending?**

A) Only emails containing attachments larger than 5 MB

B) Emails to new contacts and bulk sends — these should never auto-send without human review

C) All emails regardless of recipient, with no exceptions

D) Only emails written in a language other than English

---

### Question 9: Master Skill Orchestration

**How does the Bronze Capstone master skill (email-assistant) delegate work to its components?**

A) It copies the full email content into each component's directory and waits for file changes

B) It analyzes the user's intent, selects the appropriate workflow mode (triage, suggest, draft, send), and invokes the right combination of skills, subagents, and MCP tools for that mode

C) It sends HTTP requests to each component's REST API endpoint

D) It runs all components in parallel and merges their outputs into a single response

---

### Question 10: MCP Architecture

**What does MCP (Model Context Protocol) provide that direct API calls do not?**

A) Faster network speeds through protocol-level compression

B) A standardized interface so Claude Code can discover and use tools from any MCP server without custom integration code for each service

C) Automatic encryption of all data transmitted between Claude and external services

D) Built-in rate limiting that prevents API quota exhaustion

---

## Silver Tier (Questions 11-16)

### Question 11: Watcher Pattern

**What are the three methods every watcher implements according to the spec?**

A) `start()`, `stop()`, and `restart()`

B) `connect()`, `listen()`, and `disconnect()`

C) `check_for_updates()`, `create_action_file(item)`, and `run()`

D) `init()`, `process()`, and `cleanup()`

---

### Question 12: Poll-Based Watching

**Why does the Gmail watcher use poll-based checking (check every N seconds) instead of event-based push notifications?**

A) Gmail does not support any form of push notifications

B) Poll-based watching is simpler to implement, works without webhook infrastructure, and runs locally without exposing a public endpoint — important for a personal tool on your laptop

C) Event-based systems are slower than polling for email workloads

D) Poll-based checking uses less bandwidth than maintaining a persistent WebSocket connection

---

### Question 13: HITL Rejection

**What happens when a human moves an approval request file to the /Rejected/ folder?**

A) Claude Code automatically deletes the rejected file and all related data

B) The AI employee retries the action with modified parameters

C) The action is cancelled — Claude Code reads the rejection, logs it, and does not execute the requested action

D) The file is forwarded to a backup approver for a second opinion

---

### Question 14: Permission Boundaries

**According to the spec's permission boundaries table, name two action categories that should ALWAYS require human approval.**

A) Reading files and searching emails

B) Creating plans and updating the dashboard

C) Payments to new payees (or over $100) and social media replies or DMs

D) Scheduling cron jobs and restarting watcher processes

---

### Question 15: PM2 Persistence

**What two PM2 commands make your watcher processes survive a system reboot?**

A) `pm2 start` and `pm2 restart`

B) `pm2 save` and `pm2 startup`

C) `pm2 enable` and `pm2 persist`

D) `pm2 daemon` and `pm2 autostart`

---

### Question 16: CEO Briefing Data Sources

**What three data sources does the CEO Briefing skill read to generate the Monday morning report?**

A) Gmail inbox, calendar events, and browser history

B) Business_Goals.md, the /Done/ folder, and the /Accounting/ folder

C) CLAUDE.md, AGENTS.md, and Dashboard.md

D) GitHub commits, Slack messages, and Jira tickets

---

## Gold Tier (Questions 17-20)

### Question 17: Error Recovery Categories

**What is the difference between transient errors and authentication errors in the spec's error handling table?**

A) Transient errors are bugs in your code; authentication errors are bugs in the API

B) Transient errors (network timeout, rate limit) recover automatically with exponential backoff retry; authentication errors (expired token, revoked access) require alerting the human and pausing operations

C) Transient errors affect only email operations; authentication errors affect all domains

D) Transient errors happen during development; authentication errors happen only in production

---

### Question 18: Audit Logging

**According to the spec, what fields must every audit log entry contain?**

A) `filename`, `size`, `encoding`, and `checksum`

B) `timestamp`, `action_type`, `actor`, `target`, `parameters`, `approval_status`, and `result`

C) `user_id`, `session_id`, `ip_address`, and `browser`

D) `date`, `description`, and `category`

---

### Question 19: Graceful Degradation

**If the Gmail API goes down, what should the AI employee do according to the spec?**

A) Switch to a backup email provider and continue sending

B) Alert the human immediately and shut down all operations

C) Queue outgoing emails locally and process them when the service is restored

D) Retry the Gmail connection every 5 seconds until it recovers

---

### Question 20: Full Pipeline Architecture

**Describe the correct sequence when a watcher detects a new urgent email and the employee needs to send a payment in response.**

A) Watcher sends payment directly via banking API, then logs the result

B) Watcher creates an action file in /Needs_Action/ with email details; Claude Code reads it, reasons about the required payment, and creates an approval request in /Pending_Approval/; human reviews and moves it to /Approved/; Claude Code reads the approval and executes the payment via MCP; the action is logged in /Logs/

C) Claude Code monitors Gmail directly, detects the email, processes the payment, and writes a summary to /Done/

D) Watcher sends the email to Claude Code via API call; Claude Code responds with a payment command; the watcher executes the payment

---

## Answer Key

**Bronze Tier**

**1. B** — CLAUDE.md is the entry point that Claude Code reads first when it opens your vault. It typically references AGENTS.md with `@AGENTS.md`. AGENTS.md defines governance: skill format, agent format, and behavioral rules. (L01)

**2. C** — Files are human-readable (open in any editor), version-controllable (commit to git for history), and tool-agnostic (no database driver needed). This makes the entire system inspectable and portable. (L01)

**3. B** — A valid SKILL.md requires YAML frontmatter with at least `name` and `description` fields. The `description` tells Claude when to activate the skill. The markdown body contains instructions, examples, and usage guidance. (L02)

**4. B** — Claude Code reads the `description` field from each skill's YAML frontmatter. When your request matches a description's activation criteria (e.g., "Use when drafting emails"), Claude selects that skill. (L02)

**5. B** — Use a subagent when the task requires autonomous reasoning with varied outputs. Skills are for deterministic, reusable patterns (format an email). Subagents are for tasks needing judgment (triage an inbox and classify priority). (L05)

**6. C** — Multi-line YAML descriptions can break the tool parsing that Claude Code uses to discover and invoke agents. A single-line description ensures reliable agent discovery. (L05)

**7. B** — App Password provides SMTP send-only access in about 2 minutes of setup. OAuth provides full Gmail API access (read, search, labels, draft, send) in about 10 minutes, requiring a Google Cloud project. (L06)

**8. B** — Emails to new contacts (people not in your known contacts list) and bulk sends should always go through draft review. Known contacts with 3+ email exchanges in 90 days can auto-approve. (L06, L00 Permission Boundaries)

**9. B** — The master skill interprets the user's intent, selects the appropriate workflow mode (triage, suggest, draft, or send), then invokes the right combination of component skills, subagents, and Gmail MCP tools. It coordinates rather than does work itself. (L07)

**10. B** — MCP provides a standardized protocol for tool discovery and invocation. Any MCP-compatible server exposes its tools in a uniform way, so Claude Code can use Gmail MCP, filesystem MCP, or any future server without custom integration code per service. (L06)

**Silver Tier**

**11. C** — Every watcher implements `check_for_updates()` to poll the external source, `create_action_file(item)` to write a markdown file in /Needs_Action/, and `run()` for the infinite check-sleep loop. (L00 Watcher Pattern, L08)

**12. B** — Poll-based watching is simpler (no webhook server), works locally (no public endpoint), and runs on your laptop without infrastructure. Event-based push requires exposing a public URL, which is impractical for a personal tool. (L08)

**13. C** — Moving a file to /Rejected/ cancels the action. Claude Code reads the rejection, logs it as denied, and does not execute the requested action. The file stays in /Rejected/ as an audit record. (L09)

**14. C** — The permission boundaries table specifies that payments to new payees or over $100 always require approval, as do social media replies and DMs. Email to known contacts and file creation can auto-approve. (L00, L09)

**15. B** — `pm2 save` saves the current process list so PM2 knows what to restart. `pm2 startup` generates a system startup script so PM2 launches automatically after reboot. Together they make processes persistent. (L10)

**16. B** — The CEO Briefing reads Business_Goals.md (your objectives and KPI thresholds), the /Done/ folder (completed tasks this week), and /Accounting/ (bank transactions and revenue) to generate the Monday morning report. (L00, L11)

**Gold Tier**

**17. B** — Transient errors (network timeout, API rate limit) are temporary and recover with exponential backoff retry. Authentication errors (expired token, revoked access) require human intervention: alert the human and pause operations until credentials are refreshed. (L00 Error Categories, L12)

**18. B** — Every audit log entry must contain `timestamp`, `action_type`, `actor`, `target`, `parameters`, `approval_status`, and `result`. Logs are stored as JSON in /Vault/Logs/YYYY-MM-DD.json with 90-day minimum retention. (L00 Audit Logging, L12)

**19. C** — Queue outgoing emails locally and process them when the service is restored. The spec explicitly states: never retry payments automatically, but email queuing is safe. Watchers continue collecting items for later processing even when Claude Code or APIs are unavailable. (L00 Graceful Degradation)

**20. B** — The full pipeline: Watcher detects urgent email and deposits an action file in /Needs_Action/. Claude Code reads it, reasons about the payment need, and writes an approval request to /Pending_Approval/. The human reviews and moves it to /Approved/. Claude Code reads the approval and executes payment via MCP. The action is logged in /Logs/. Every sensitive action flows through this Perception-Reasoning-Approval-Action-Logging sequence. (L00 Architecture, L08, L09, L12)

---

## Self-Evaluation

Record your score for the tier you completed:

| Tier   | Questions | Your Score | Passing |
| ------ | --------- | ---------- | ------- |
| Bronze | 1-10      | \_\_/10    | 8/10    |
| Silver | 11-16     | \_\_/6     | 5/6     |
| Gold   | 17-20     | \_\_/4     | 3/4     |

If you scored below passing on any tier, revisit the lessons referenced in the answer explanations. Each answer points to the specific lesson where that concept was taught.

## Try With AI

**Prompt 1: Generate your own review questions**

```
I just completed Chapter 13 (Build Your First AI Employee).
Read my vault's AGENTS.md and CLAUDE.md, then generate 5 new
quiz questions about MY specific implementation — not generic
questions, but ones that test whether I truly understand how
my own employee is configured.
```

**What you are practicing**: Turning AI into a personalized assessor. Generic quizzes test textbook knowledge; AI-generated questions based on your actual vault test applied understanding.

**Prompt 2: Identify your weakest concept**

```
Here are the Chapter 13 topics I got wrong on the assessment:
[paste your wrong answers]. For each one, explain the concept
in a different way than the textbook did, and give me a
concrete scenario where getting it wrong would cause a real
problem in my AI employee.
```

**What you are practicing**: Using AI as a targeted tutor. Instead of re-reading entire lessons, you direct AI to the exact gaps in your understanding and ask for alternative explanations with real-world consequences.
