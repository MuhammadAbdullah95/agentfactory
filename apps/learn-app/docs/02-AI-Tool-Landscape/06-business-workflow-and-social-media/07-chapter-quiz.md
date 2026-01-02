---
sidebar_position: 7
title: "Chapter Quiz"
sidebar_label: "Chapter Quiz"
description: "Test your understanding of building a complete Email Assistant system with skills, subagents, and MCP integration."
keywords: [quiz, assessment, email assistant, skills, subagents, MCP, orchestration]
chapter: 6
quiz: true
questions: 15
pass_threshold: 60
---

# Chapter 6 Quiz: Building a Complete Email Assistant

This quiz tests your understanding of building a complete Email Assistant system using Claude Code skills, subagents, and MCP integration. You learned how to create interconnected components that work together as a Digital FTE.

**Quiz Details:**
- **Questions:** 15
- **Passing Score:** 60% (9/15 correct)
- **Topics Covered:** Skills (4), Subagents (4), MCP (3), Orchestration (4)

---

## Skills

### Question 1

**Difficulty**: Easy

What file contains the main instructions for a Claude Code skill?

- A) skill.yaml
- B) SKILL.md
- C) agent.md
- D) config.json

<details>
<summary>Answer</summary>

**Correct Answer**: B

**Explanation**: SKILL.md is the core instruction file for Claude Code skills. It contains the YAML frontmatter with name and description fields, plus the markdown body with instructions. Option A (skill.yaml) is incorrect because skills use markdown files, not YAML files. Option C (agent.md) is incorrect because that format is used for subagents in the .claude/agents/ directory. Option D (config.json) is incorrect because JSON configuration files are used for MCP settings, not skill definitions.
</details>

---

### Question 2

**Difficulty**: Easy

In the email-drafter skill, what is the purpose of the references/ folder?

- A) To store backup copies of SKILL.md
- B) To contain supporting files loaded when needed
- C) To hold compiled skill executables
- D) To archive old versions of the skill

<details>
<summary>Answer</summary>

**Correct Answer**: B

**Explanation**: The references/ folder contains supporting files like tone-guidelines.md that are loaded only when the skill needs them (Level 3 loading). This three-level architecture protects Claude's working memory by not loading everything at once. Option A is incorrect because backups are not stored there. Option C is incorrect because skills are not compiled into executables. Option D is incorrect because version control is handled by git, not reference folders.
</details>

---

### Question 3

**Difficulty**: Medium

Which field in a SKILL.md YAML frontmatter helps Claude Code understand when to activate the skill?

- A) name
- B) model
- C) description
- D) tools

<details>
<summary>Answer</summary>

**Correct Answer**: C

**Explanation**: The description field tells Claude Code when to activate the skill. It should start with "This skill should be used when..." to clearly define activation triggers. The name field (A) identifies the skill but doesn't explain activation context. The model field (B) specifies which model to use for the skill. The tools field (D) specifies which tools the skill can access, but doesn't define activation conditions.
</details>

---

### Question 4

**Difficulty**: Medium

What is the correct syntax for variable placeholders in email templates?

- A) [variable_name]
- B) {variable_name}
- C) `{{variable_name}}`
- D) $variable_name

<details>
<summary>Answer</summary>

**Correct Answer**: C

**Explanation**: The double-brace syntax `{{variable_name}}` is the standard for email templates because it's unambiguous and Claude recognizes it immediately. Single brackets (A) could be confused with markdown links. Single braces (B) might conflict with other formatting. Dollar sign syntax (D) is associated with shell variables and could cause parsing issues in markdown contexts.
</details>

---

## Subagents

### Question 5

**Difficulty**: Easy

What is the CRITICAL format requirement for subagent descriptions in the YAML frontmatter?

- A) Must be at least 100 characters long
- B) Must be single-line (no multi-line with |)
- C) Must include a version number
- D) Must be written in all caps

<details>
<summary>Answer</summary>

**Correct Answer**: B

**Explanation**: The description must be a single line because multi-line descriptions using the YAML pipe character (|) break Claude Code's parser. While descriptions can be long (up to 1024 characters), they must remain on one line. Option A is incorrect because there's no minimum length requirement. Option C is incorrect because version numbers are not required in descriptions. Option D is incorrect because all caps would make descriptions harder to read and isn't required.
</details>

---

### Question 6

**Difficulty**: Medium

When should you use a subagent instead of a skill?

- A) When generating predictable content
- B) When applying templates consistently
- C) When classification or reasoning is required
- D) When sending emails directly

<details>
<summary>Answer</summary>

**Correct Answer**: C

**Explanation**: Subagents are designed for autonomous reasoning and classification tasks with 5+ decision points, where output depends on context analysis. Skills (A, B) handle predictable content generation with 2-4 decision points. MCP tools (D) handle external operations like sending emails. The inbox-triager subagent, for example, analyzes sender, subject, deadline, recipient field, and action indicators to classify email priority.
</details>

---

### Question 7

**Difficulty**: Hard

The inbox-triager subagent uses a five-step classification sequence. Which is the correct order?

- A) Check deadline, scan subject, analyze body, check sender, look for actions
- B) Check sender, scan subject, analyze body, check recipient, look for actions
- C) Scan subject, check sender, analyze body, check recipient, look for actions
- D) Look for actions, check sender, scan subject, analyze body, check deadline

<details>
<summary>Answer</summary>

**Correct Answer**: B

**Explanation**: The inbox-triager follows this sequence: (1) Check sender against priority contacts, (2) Scan subject for urgency signals, (3) Analyze body for deadlines, (4) Check recipient field (TO: vs CC:), (5) Look for action indicators. This sequence is logical because sender identity often establishes baseline priority before examining content. Starting with deadlines (A) or subjects (C) misses the sender context. Starting with actions (D) would lack the context needed to evaluate action importance.
</details>

---

### Question 8

**Difficulty**: Medium

How does the response-suggester subagent structure its output?

- A) Single response with multiple paragraphs
- B) List of five response options ranked by quality
- C) Three options: Brief, Detailed, and Alternative
- D) Two options: Formal and Casual versions

<details>
<summary>Answer</summary>

**Correct Answer**: C

**Explanation**: The response-suggester provides exactly three options: Option 1 (Brief) for quick responses, Option 2 (Detailed) for full context, and Option 3 (Alternative) for different approaches like deferral or clarification. This structure gives meaningful choice without overwhelming. Single response (A) doesn't offer options. Five options (B) would be too many. Two options (D) only addresses tone, not approach variety.
</details>

---

## MCP Integration

### Question 9

**Difficulty**: Easy

What are the two authentication methods supported by Gmail MCP?

- A) API Key and OAuth
- B) SMTP with App Password and OAuth
- C) Username/Password and API Key
- D) OAuth only with no alternatives

<details>
<summary>Answer</summary>

**Correct Answer**: B

**Explanation**: Gmail MCP supports two authentication paths: SMTP with App Password (quick 2-minute setup) and OAuth (comprehensive 10-minute setup with full API access). SMTP uses Google's App Passwords for limited access, while OAuth provides full access to all 19 Gmail tools. API Keys (A, C) are not used for Gmail authentication. Username/Password (C) would be insecure. OAuth-only (D) is incorrect because SMTP is also supported.
</details>

---

### Question 10

**Difficulty**: Medium

Which Gmail MCP authentication method is required for label management and filter operations?

- A) SMTP only provides access to these features
- B) OAuth provides access to these features
- C) Both SMTP and OAuth provide equal access
- D) Neither method supports label management

<details>
<summary>Answer</summary>

**Correct Answer**: B

**Explanation**: OAuth authentication provides full API access including label management (create_gmail_label, update_gmail_label, delete_gmail_label) and filter operations. SMTP with App Password provides basic send/receive capabilities but not the complete 19-tool suite. The lesson recommends starting with SMTP for testing, then moving to OAuth for production use requiring advanced features.
</details>

---

### Question 11

**Difficulty**: Medium

What is the recommended safety protocol for sending important emails through Gmail MCP?

- A) Send immediately to save time
- B) Use draft_email first, review, then send manually
- C) Disable MCP authentication before sending
- D) Only send emails during business hours

<details>
<summary>Answer</summary>

**Correct Answer**: B

**Explanation**: The draft-first rule recommends using draft_email before send_email for important messages. This creates the draft in Gmail where you can review it before manual sending. This protects against AI-generated errors, incorrect recipients, or inappropriate tone. Immediate sending (A) risks errors. Disabling authentication (C) would prevent any email operations. Business hours (D) is unrelated to safety protocols.
</details>

---

## Orchestration

### Question 12

**Difficulty**: Easy

What is the primary purpose of the email-assistant master skill?

- A) To replace all other skills with one skill
- B) To coordinate skills, subagents, and MCP together
- C) To directly compose emails without templates
- D) To manage Gmail authentication settings

<details>
<summary>Answer</summary>

**Correct Answer**: B

**Explanation**: The email-assistant master skill is an orchestrator that coordinates all components: skills (email-drafter, email-templates, email-summarizer), subagents (inbox-triager, response-suggester, follow-up-tracker), and Gmail MCP. It doesn't replace components (A) but coordinates them. It delegates composition to component skills (C). Authentication is handled by MCP configuration, not the skill (D).
</details>

---

### Question 13

**Difficulty**: Hard

In graceful degradation mode, what happens when Gmail MCP is unavailable?

- A) All email functions stop working completely
- B) Skills and subagents still work, drafts go to clipboard
- C) Only template-based emails can be created
- D) The orchestrator crashes with an error

<details>
<summary>Answer</summary>

**Correct Answer**: B

**Explanation**: When Gmail MCP is unavailable, the system degrades gracefully: skills work fully for content generation, subagents work with user-provided data, and instead of creating Gmail drafts, email content is copied to clipboard with clear notification. This maintains functionality rather than failing completely (A) or crashing (D). All skills work, not just templates (C). The lesson emphasizes this resilience pattern as critical for Digital FTE design.
</details>

---

### Question 14

**Difficulty**: Hard

According to the delegation logic decision tree, which component handles a request to "prioritize 50 inbox emails"?

- A) email-drafter skill because it creates content
- B) email-templates skill because it uses patterns
- C) inbox-triager subagent because it requires classification
- D) Gmail MCP because it accesses external data

<details>
<summary>Answer</summary>

**Correct Answer**: C

**Explanation**: The decision tree shows: Is task about classification/analysis? Yes, for priority classification, use inbox-triager subagent. Prioritizing emails requires analyzing sender importance, deadline signals, recipient fields, and action indicators (5+ decision points), which is autonomous reasoning work. Skills (A, B) handle content generation. Gmail MCP (D) would fetch the emails, but classification reasoning is the subagent's job. MCP provides data; the subagent provides analysis.
</details>

---

### Question 15

**Difficulty**: Medium

What is the correct workflow sequence in Mode 1 (Inbox Management)?

- A) Send emails, then triage, then summarize
- B) Summarize threads, then triage, then suggest responses
- C) Triage emails, then summarize important ones, then suggest responses
- D) Draft responses, then triage, then send

<details>
<summary>Answer</summary>

**Correct Answer**: C

**Explanation**: Mode 1 follows the sequence: (1) Fetch unread emails, (2) Classify by priority with inbox-triager, (3) Summarize important threads with email-summarizer, (4) Suggest responses for urgent items, (5) Draft replies, (6) Create Gmail drafts. Triage must come before summarization because you need to know which threads are important enough to summarize. Responses come after understanding priority and content. Options A, B, and D have the sequence out of order.
</details>

---

## Quiz Complete

Review any questions you found challenging by revisiting the relevant lessons:

- **Skills questions**: Review Lessons 1-3
- **Subagents questions**: Review Lesson 4
- **MCP questions**: Review Lesson 5
- **Orchestration questions**: Review Lesson 6

Remember: The Email Assistant pattern you learned applies to any domain where skills, subagents, and external integrations need coordination. Master this pattern, and you can build Digital FTEs for customer support, document processing, data analysis, and beyond.
