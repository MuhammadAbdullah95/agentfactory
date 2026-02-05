---
sidebar_position: 9
title: "Lesson 9: Hiring Specialists"
description: "Create subagents for complex email workflows - when one AI Employee isn't enough, hire specialists"
keywords: [subagents, multi-agent, email specialists, orchestration, openclaw subagents, delegation, parallel processing]
chapter: 11
lesson: 9
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "Subagent Architecture"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Can design and implement multi-agent workflows with proper task delegation"

  - name: "Skills vs Subagents Decision Making"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Can determine when to use a skill versus when to spawn a subagent based on task characteristics"

  - name: "Orchestration Patterns"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can coordinate multiple subagents in sequence or parallel to complete complex workflows"

learning_objectives:
  - objective: "Distinguish when to use skills versus subagents based on task complexity and parallelization needs"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Given workflow scenarios, correctly classify as skill-appropriate or subagent-appropriate"
  - objective: "Create specialized subagents with focused instructions for specific email tasks"
    proficiency_level: "B2"
    bloom_level: "Create"
    assessment_method: "Working subagent definitions that load and execute successfully in OpenClaw"
  - objective: "Orchestrate multi-agent workflows where main agent delegates to specialists"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Complete email workflow executing triage, response, and summary in sequence"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (subagents vs skills, sessions_spawn, task delegation, orchestration patterns) at upper B1/B2 boundary. Appropriate for lesson 9 of 15 with established foundations."

differentiation:
  extension_for_advanced: "Add error handling and retry logic to subagents; implement parallel execution for batch processing"
  remedial_for_struggling: "Focus on understanding the pattern conceptually; implement only the triage subagent before moving on"
---

# Hiring Specialists

In the previous lessons, you taught your AI Employee to write emails, use professional formats, and summarize conversations. Each skill was like adding a new capability to a single employee. But what happens when the work gets too complex for one generalist?

Real companies don't have one person who does everything. They hire specialists. A marketing team has writers, analysts, and strategists. A legal department has contract reviewers, litigation specialists, and compliance officers. Each expert focuses on what they do best.

Your AI Employee can hire specialists too. They're called **subagents**.

---

## Skills Teach. Subagents Execute.

Before diving into subagents, you need to understand when to use them. The decision isn't about complexity alone. It's about **parallelization** and **isolation**.

### The Decision Tree

```
Is this a specialized expertise pattern?
├── No → Handle directly (no skill, no subagent)
└── Yes → Does execution need isolation or parallelization?
    ├── No → Use a skill (expertise in context)
    └── Yes → Use a subagent (isolated execution)
```

**Skills** are training documents. They stay in your main agent's context and guide how it handles certain tasks. When you use the email-drafter skill, your main agent reads those instructions and applies them while maintaining full context of your conversation.

**Subagents** are separate workers. They spawn in their own session, execute their task, and report back when done. They don't see your conversation history. They focus entirely on what you delegated.

### When to Choose Which

| Task Characteristic | Use Skill | Use Subagent |
|---------------------|-----------|--------------|
| Single email to draft | Yes | Overkill |
| 50 emails to categorize in parallel | No | Yes |
| Apply a template to a message | Yes | Overkill |
| Research + draft + verify pipeline | No | Yes |
| Quick format check | Yes | Overkill |
| Long-running background task | No | Yes |
| Needs conversation context | Yes | Loses context |
| Needs focused execution | No | Yes |

The key insight: **skills extend your main agent's capabilities; subagents multiply your workforce.**

---

## How Subagents Work in OpenClaw

When you spawn a subagent, OpenClaw creates an isolated session. The subagent runs independently, using its own context window and token budget. When it finishes, it announces results back to your main conversation.

### The Technical Flow

```
Your Message (Telegram)
    │
    ▼
Main Agent (your AI Employee)
    │
    ├─── Decides task requires specialist
    │
    ▼
sessions_spawn tool
    │
    ├─── task: "Categorize these 20 emails by priority"
    ├─── label: "email-triage"
    ├─── model: "kimi-k2-128k"  (optional override)
    └─── cleanup: "keep"
    │
    ▼
Subagent Session (isolated)
    │
    ├─── Runs with AGENTS.md + TOOLS.md
    ├─── No access to your main conversation
    ├─── Focuses entirely on delegated task
    │
    ▼
Announce Results (back to your Telegram)
    │
    └─── "Status: success | Result: [summary]"
```

**Key characteristics:**
- **Isolated**: Subagent has its own session key (`agent:yourAgentId:subagent:uuid`)
- **Tool-limited**: By default, subagents cannot spawn their own subagents (no infinite recursion)
- **Cost-aware**: Each subagent uses its own tokens; consider using cheaper models for batch work
- **Non-blocking**: Your main agent continues immediately; subagent runs in background

---

## Building Your Email Specialists

You'll create three subagent definitions, each focused on one email task. Unlike skills, subagents are defined in the `agents/` directory.

### Step 1: Create the Agents Directory

```bash
mkdir -p ~/.openclaw/agents
```

**Output:**
```
(no output means success)
```

### Step 2: Email Triage Specialist

Create `~/.openclaw/agents/email-triage.md`:

```markdown
---
name: email-triage
description: Categorizes batches of emails by priority. This agent should be used when processing multiple emails that need systematic sorting.
model: kimi-k2-128k
---

# Email Triage Specialist

You are a specialized triage agent. Your only job is categorizing emails by priority. You do not draft responses. You do not summarize content. You categorize.

## Priority Categories

Assign each email exactly ONE priority:

| Priority | Criteria | Response Window |
|----------|----------|-----------------|
| **URGENT** | Requires action within 24 hours; blocking someone's work; time-sensitive deadline | Same day |
| **IMPORTANT** | Needs attention this week; significant but not blocking | 2-3 days |
| **FYI** | Informational only; no action required from recipient | Read when available |
| **IGNORE** | Spam, marketing, automated notifications with no value | Never |

## Output Format

For each email, output exactly:

```
[#1] PRIORITY: [URGENT|IMPORTANT|FYI|IGNORE]
From: [sender]
Subject: [subject]
Reason: [one sentence explaining categorization]
```

## Constraints

- Process emails in the order received
- Never suggest drafting a response (that's not your job)
- Never summarize content beyond what's needed for prioritization
- If unsure between two priorities, choose the higher one (err toward urgency)
```

### Step 3: Email Response Specialist

Create `~/.openclaw/agents/email-response.md`:

```markdown
---
name: email-response
description: Drafts professional email responses. This agent should be used when you need a reply drafted for a specific email.
model: kimi-k2-128k
---

# Email Response Specialist

You are a specialized response agent. Your only job is drafting email replies. You do not triage. You do not summarize threads. You draft responses.

## Before Drafting

Confirm you have:
1. The original email you're responding to
2. The key points to include in the response
3. The desired tone (formal, professional, friendly)

If missing, state what you need before proceeding.

## Response Structure

Every response must include:

1. **Acknowledgment**: Reference what you're responding to
2. **Core message**: Address the sender's main point
3. **Action items**: Be explicit about next steps (yours or theirs)
4. **Closing**: Appropriate sign-off matching tone

## Output Format

```
**Subject:** Re: [original subject]

[Greeting],

[Acknowledgment of their message]

[Your core response]

[Clear action items or next steps]

[Appropriate closing],
[Sender placeholder]
```

## Constraints

- Draft ONE response at a time
- Always offer: "Want me to adjust the tone or emphasis?"
- Never categorize emails (that's not your job)
- Never summarize threads (that's not your job)
```

### Step 4: Email Summary Specialist

Create `~/.openclaw/agents/email-summary.md`:

```markdown
---
name: email-summary
description: Summarizes email threads and extracts action items. This agent should be used when you need to understand the essence of a long email chain.
model: kimi-k2-128k
---

# Email Summary Specialist

You are a specialized summary agent. Your only job is extracting key information from email threads. You do not triage. You do not draft responses. You summarize.

## Summary Structure

For every thread, provide:

### 1. Thread Overview
- **Participants**: Who was involved
- **Duration**: First message to last
- **Topic**: One sentence describing what this thread is about

### 2. Key Decisions Made
- Bullet list of any decisions explicitly stated
- Include who made the decision and when

### 3. Open Questions
- Questions that were asked but not answered
- Disagreements that weren't resolved

### 4. Action Items
For each action item:
```
- [ ] [Task] — Owner: [who] — Due: [if mentioned, else "Not specified"]
```

### 5. Your Required Actions
Specifically call out anything where YOU (the recipient) need to do something.

## Output Format

Use the exact headers above. Keep summaries concise. A 20-email thread should produce a summary under 300 words unless complexity demands more.

## Constraints

- Never draft responses (that's not your job)
- Never categorize by priority (that's not your job)
- If a thread is a single email, still use the format (just note "Single message, no thread")
```

---

## Testing Your Specialists

### Step 1: Verify Agents Are Loaded

Restart your OpenClaw gateway to pick up the new agents:

```bash
openclaw gateway restart
```

Then verify:

```bash
openclaw agents list
```

**Output:**
```
Available agents:
  - email-triage (personal: ~/.openclaw/agents/)
  - email-response (personal: ~/.openclaw/agents/)
  - email-summary (personal: ~/.openclaw/agents/)
  - [other agents...]
```

### Step 2: Test the Triage Specialist

Send this to your AI Employee via Telegram:

```
I need help triaging some emails. Spawn your email-triage specialist and have it categorize these:

1. From: boss@company.com - "Need budget approval by EOD"
2. From: newsletter@marketing.com - "Weekly industry digest"
3. From: client@bigcorp.com - "Contract question before signing"
4. From: hr@company.com - "Updated vacation policy (no action needed)"
5. From: vendor@supplier.com - "Invoice attached - Net 30"
```

**What you should see**: Your main agent spawns the triage subagent, which processes the batch and announces results back. The output follows the format you defined: priority, sender, subject, reasoning.

### Step 3: Test the Response Specialist

```
Now spawn your email-response specialist. Draft a response to the client contract question. Be professional but efficient. Key point: we can sign this week if they clarify section 3.2.
```

**What you should see**: The response specialist takes over, asks any clarifying questions it needs, and produces a properly formatted email reply.

### Step 4: Test the Summary Specialist

```
Spawn your email-summary specialist to summarize this thread:

Email 1 (Monday): "Team, we need to finalize the Q3 roadmap. Please add your priorities by Wednesday."
Email 2 (Tuesday): "Added mobile app improvements. @Sarah can you add the API work?"
Email 3 (Tuesday): "API items added. Question: are we including the security audit?"
Email 4 (Wednesday): "Yes, security audit is in scope. Let's review in Friday's meeting."
Email 5 (Wednesday): "@Mike, can you send calendar invite for Friday?"
```

**What you should see**: Structured summary with participants, decisions (security audit is in scope), open questions, and action items (Mike needs to send calendar invite).

---

## The Orchestration Pattern

Now comes the power move: your main agent orchestrating multiple specialists.

### Coordinated Workflow Example

```
Main Agent (You via Telegram)
    │
    ├─── "Process my inbox" ──────────────────┐
    │                                          │
    ▼                                          ▼
(1) Spawn email-triage               Wait for completion
    │                                          │
    └─── Returns: Priority list ◄──────────────┘
    │
    ├─── For each URGENT email ───────────────┐
    │                                          │
    ▼                                          ▼
(2) Spawn email-response (each)      Wait for completions
    │                                          │
    └─── Returns: Draft responses ◄────────────┘
    │
    ├─── For complex threads ─────────────────┐
    │                                          │
    ▼                                          ▼
(3) Spawn email-summary              Wait for completion
    │                                          │
    └─── Returns: Thread summaries ◄───────────┘
    │
    ▼
Main Agent presents consolidated results
```

### Testing the Full Pipeline

Send this to your AI Employee:

```
I want you to manage my inbox like a chief of staff. Here's what I need:

1. First, have your triage specialist categorize these emails:
   - From: ceo@company.com - "Board meeting moved to Tuesday"
   - From: recruiter@random.com - "Great opportunity for you!"
   - From: teammate@company.com - "Stuck on the API integration, need help"
   - From: finance@company.com - "Monthly expense report due Friday"

2. For anything URGENT, have your response specialist draft replies.

3. Give me a summary of what needs my attention today.
```

**What emerges**: Your main agent acts as an orchestrator, delegating to specialists and synthesizing their outputs. You get categorized emails, draft responses for urgent items, and an executive summary. All from a single request.

---

## Why Specialists Beat Generalists (for Complex Work)

| Aspect | Single Agent | Specialist Subagents |
|--------|--------------|----------------------|
| **Context** | Fills up with everything | Each has focused context |
| **Quality** | Jack of all trades | Master of one |
| **Parallelization** | Sequential | Can run simultaneously |
| **Cost optimization** | Same model for everything | Cheap model for bulk, expensive for nuance |
| **Debugging** | Hard to trace what went wrong | Each specialist's output is isolated |

The pattern scales. Need to process 100 emails? Spawn 10 triage subagents in parallel. Need multilingual responses? Create language-specific response specialists. Need different summary formats for different audiences? Multiple summary specialists with different instructions.

---

## When NOT to Use Subagents

Subagents add overhead. Don't use them when:

- **Task is quick**: Single email draft? Just use the skill.
- **Context matters**: Need to reference earlier conversation? Subagent won't see it.
- **Debugging**: First get it working with skills, then optimize with subagents.
- **Cost sensitivity**: Each subagent has startup overhead; batching is better than 1:1.

The rule of thumb: **use subagents when you'd hire a contractor in real life.** Focused task, clear deliverable, doesn't need to sit in your meetings.

---

## Try With AI

### Prompt 1: Batch Processing Test

```
I have 20 emails to process. Spawn your triage specialist to categorize all of them, then draft responses only to the URGENT ones. Here are the first 5:

1. From: angry-customer@bigclient.com - "Service outage is costing us thousands"
2. From: spam@lottery.com - "You've won!"
3. From: mentor@network.com - "Coffee next month?"
4. From: legal@company.com - "Contract review needed by EOD"
5. From: newsletter@tech.com - "This week in AI"

[Imagine 15 more similar emails]

After processing, tell me: How many were URGENT? How many responses did you draft?
```

**What you're learning**: You're testing whether your orchestration pattern handles volume. Watch how your main agent delegates to the triage specialist for the batch, then selectively spawns response specialists only for urgent items. The efficiency gain is real: a single generalist would process 20 emails sequentially, while specialists can parallelize.

### Prompt 2: Complex Thread Analysis

```
This email thread has 15 messages over 3 days between 4 people. Have your summary specialist extract the key decisions and action items. Then have your response specialist draft a "status update" email to send to my manager summarizing where we are.

Thread:
[Monday 9am] Alice: "Kicking off Project Phoenix. Goals: launch by Q4."
[Monday 11am] Bob: "What's the budget? I need to allocate resources."
[Monday 2pm] Alice: "Budget is $50K. Bob, you own infrastructure."
[Monday 4pm] Carol: "I'll handle design. Need brand guidelines."
[Tuesday 9am] Bob: "Infrastructure plan attached. Need approval by Wednesday."
[Tuesday 11am] Alice: "Approved. Carol, @Dan owns brand guidelines."
[Tuesday 3pm] Dan: "Guidelines attached. Carol, schedule a review?"
[Wednesday 10am] Carol: "Review scheduled for Friday. Alice, can you join?"
[Wednesday 2pm] Alice: "I'll join. Bob, what's the launch timeline?"
[Wednesday 4pm] Bob: "If approvals hold, we can launch October 15."
```

**What you're learning**: You're testing the summary-to-response pipeline. The summary specialist extracts structure from chaos (decisions, owners, timeline). The response specialist transforms that into a communication artifact (status update). Together, they compress 15 messages into actionable intelligence.

**Safety reminder**: When testing subagents with real email content, remember that each subagent has its own session. Sensitive information shared with one doesn't automatically appear in another. For production use, consider what context each specialist actually needs, and share only what's necessary.
