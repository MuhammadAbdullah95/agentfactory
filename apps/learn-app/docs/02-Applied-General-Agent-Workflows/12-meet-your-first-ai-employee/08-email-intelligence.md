---
sidebar_position: 8
title: "Lesson 8: Teaching Email Intelligence"
description: "Create email-summarizer skill for analysis and triage"
keywords: [email analysis, email triage, summarizer skill, email intelligence]
chapter: 12
lesson: 8
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Analysis Skill Patterns"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Can create analysis skills with structured output formats that transform unstructured input into actionable intelligence"

  - name: "Skill Type Distinction"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Can distinguish between generation skills (create new content) and analysis skills (understand existing content), selecting the appropriate type for a given task"

  - name: "Workflow Composition"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Collaboration"
    measurable_at_this_level: "Can combine multiple skills into coherent workflows that address complete business processes"

learning_objectives:
  - objective: "Distinguish analysis from generation skills"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Comparison explanation identifying whether given skill descriptions are analysis or generation type"
  - objective: "Create structured analysis output formats"
    proficiency_level: "B2"
    bloom_level: "Create"
    assessment_method: "Working email-summarizer skill that produces consistent, structured output"
  - objective: "Combine multiple skills into workflows"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Demonstration of email workflow using summarizer, drafter, and templates together"

cognitive_load:
  new_concepts: 3
  assessment: "Moderate - new analysis pattern builds on generation pattern from L06-L07. Single email analysis is simple; batch triage and workflow composition add complexity. Within B1-B2 range (7-10 concepts when combined with prior knowledge)."

differentiation:
  extension_for_advanced: "Add sentiment analysis to summaries (detecting tone: urgent, frustrated, positive) and thread context awareness"
  remedial_for_struggling: "Focus on single email analysis first. Master the basic output format before attempting batch triage."
---

# Teaching Email Intelligence

Writing is one thing. Understanding is another.

In the previous lessons, you taught your AI Employee to write emails and use professional templates. Those are **generation skills**. Your employee creates something that did not exist before. But generation only solves half the problem. Before you can respond appropriately to an email, you need to understand it. Before you can decide which emails matter, you need to analyze them all. Before your AI Employee can help you communicate effectively, it must first help you comprehend effectively.

This lesson introduces a different category of skill: **analysis skills**. Where generation skills create output from nothing, analysis skills transform input into understanding. Your email-drafter produces emails from intentions. Your email-summarizer will produce intelligence from emails. Together, they complete a workflow: understand what came in, decide what matters, craft appropriate responses.

The distinction matters because analysis and generation require different design patterns. Generation skills focus on tone, format, and creative flexibility. Analysis skills focus on consistency, structured output, and actionable categorization. Your AI Employee needs both capabilities to be genuinely useful.

## Analysis vs Generation Skills

Every skill you build falls into one of two categories. Understanding the difference helps you design better skills from the start.

| Dimension | Generation Skills | Analysis Skills |
|-----------|------------------|-----------------|
| **Purpose** | Create new content | Understand existing content |
| **Input** | Intent, context, constraints | Raw information, documents |
| **Output** | Text, documents, artifacts | Structured insights, categories |
| **Success Metric** | Quality, appropriateness, tone | Accuracy, consistency, actionability |
| **Examples** | email-drafter, templates | summarizer, categorizer, prioritizer |

**Generation skills** excel when you need to produce something. "Write a follow-up email." "Create a meeting agenda." "Draft a proposal outline." The skill takes your intention and creates appropriate content.

**Analysis skills** excel when you need to understand something. "What does this email want?" "Which of these 50 messages need my attention today?" "What is the status of this thread?" The skill takes raw input and produces structured intelligence.

Most real workflows require both. You cannot write an effective response without first understanding what you are responding to. You cannot prioritize your inbox without first analyzing what is in it. The skills complement each other.

### Why Structured Output Matters

Analysis skills produce value through consistency. When your email-summarizer produces the same output format every time, you can:

- Scan quickly because you know where to look
- Compare across emails because structure is uniform
- Make decisions faster because priorities are explicit
- Compose workflows because output is predictable

Unstructured analysis ("This email is about the Johnson project and seems urgent") is harder to act on than structured analysis:

```
**Priority:** High
**Category:** Action Required
**Summary:** Johnson project deadline moved to Friday
**Action Required:** Yes - Confirm new timeline with team by end of day
```

The structure makes the intelligence actionable.

## The email-summarizer Skill

Your email-summarizer skill will handle two modes: single email analysis and batch email triage. Single analysis gives you deep understanding of one email. Batch triage gives you rapid prioritization of many.

Create this skill in your OpenClaw workspace:

**Location**: `~/.openclaw/workspace/skills/email-summarizer/SKILL.md`

```markdown
---
name: email-summarizer
description: Analyze and summarize emails with actionable insights. Use when you need to understand what an email is asking, prioritize multiple emails, or triage an inbox.
metadata: { "openclaw": { "always": true } }
---

# Email Summarizer

You analyze emails and provide structured summaries that make action decisions easy.

## Single Email Analysis

When given a single email, provide this structured analysis:

```
**From:** [Sender name and role if discernible]
**Subject:** [Subject line]
**Priority:** [High/Medium/Low]
**Category:** [Action Required | FYI | Question | Follow-up | Scheduling]

**Summary:** [2-3 sentence summary focusing on what is being asked or communicated]

**Key Points:**
- [Most important point]
- [Second important point]
- [Additional points as needed]

**Action Required:** [Yes/No - What specific action is needed]
**Deadline:** [If mentioned or implied, otherwise "Not specified"]
**Stakeholders:** [Anyone CC'd or mentioned who should be involved]
```

## Batch Email Triage

When given multiple emails, create a triage report organized by urgency:

```
# Email Triage Report

## Urgent (Respond Today)
1. **[Subject]** from [Sender] - [Why urgent: deadline, executive, customer issue]
2. ...

## Important (This Week)
1. **[Subject]** from [Sender] - [Brief summary of request]
2. ...

## FYI (When Available)
1. **[Subject]** - [One-line summary]
2. ...

## Can Ignore
1. **[Subject]** - [Reason: spam, outdated, duplicate, promotional]

---
**Total:** X emails | **Urgent:** X | **Important:** X | **FYI:** X | **Ignore:** X
```

## Priority Criteria

Use these criteria to assess priority:

**Urgent (Respond Today):**
- Deadline within 24 hours
- Sender is executive or key customer
- Active customer issue or complaint
- Time-sensitive opportunity
- Blocking someone else's work

**Important (This Week):**
- Deadline within the week
- Project-related requiring your input
- Direct request from colleague
- Meeting prep or follow-up needed

**FYI (When Available):**
- Newsletter or announcement
- CC'd for awareness only
- General updates
- No action needed from you

**Can Ignore:**
- Spam or promotional
- Already addressed in another email
- Outdated (event passed, deadline missed)
- Duplicate of another email

## Thread Analysis

When analyzing an email thread (multiple replies in one conversation):

```
# Thread Summary: [Subject]

**Participants:** [List who is involved]
**Started:** [Original date]
**Current Status:** [What is the thread's current state]

**Timeline:**
1. [Date] [Sender]: [What they said/asked]
2. [Date] [Sender]: [Response/update]
3. ...

**Current Question/Blocker:** [What is being waited on]
**Next Action:** [Who should do what next]
**Your Role:** [What is expected of you in this thread]
```
```

### Understanding the Skill Structure

This skill handles three scenarios:

1. **Single email analysis**: Deep dive on one email. Useful when you receive something complex and need to understand exactly what is being asked.

2. **Batch email triage**: Rapid prioritization. Useful when you have many emails and need to know which ones matter now.

3. **Thread analysis**: Conversation context. Useful when you are joining a thread mid-conversation or need to understand the history.

Each scenario has explicit output format. This consistency is the key to making analysis actionable.

## Testing the Skill

Create your skill file, then test it with real email content.

### Test 1: Single Email Analysis

Paste an email into your AI Employee conversation and ask for analysis:

```
Analyze this email:

---
From: Sarah Chen <sarah.chen@acme.com>
Subject: Q3 Budget Review - Need your input by Wednesday

Hi,

Hope you had a good weekend. I'm pulling together the Q3 budget review deck
for the executive team and need your department's actuals vs forecast numbers.

Could you send me:
1. Actual spend through August
2. Revised forecast for September
3. Any variance explanations over 10%

The board meeting is Friday so I need this by end of day Wednesday to have
time for revisions.

Also, Tom mentioned you might have some efficiency wins to highlight. If you
have anything worth calling out, I can include it in the wins section.

Thanks,
Sarah
---
```

**Expected output format:**

```
**From:** Sarah Chen (appears to be Finance/Accounting based on context)
**Subject:** Q3 Budget Review - Need your input by Wednesday
**Priority:** High
**Category:** Action Required

**Summary:** Sarah is compiling the Q3 budget review deck for an executive
board meeting on Friday. She needs department financial data by Wednesday
EOD, with three specific deliverables requested.

**Key Points:**
- Three specific items needed: actuals, revised forecast, variance explanations
- Firm deadline: Wednesday EOD (board meeting Friday)
- Optional: efficiency wins for inclusion in presentation

**Action Required:** Yes - Compile and send budget data (actuals, forecast, variances)
**Deadline:** Wednesday end of day
**Stakeholders:** Tom (mentioned as source of efficiency wins info)
```

If your skill produces output matching this structure, it is working correctly.

### Test 2: Batch Triage

Test with multiple emails at once:

```
Triage these 5 emails and tell me what needs my attention today:

Email 1:
From: Newsletter <updates@techdigest.com>
Subject: This Week in AI: January 2026 Roundup
[Newsletter content about industry news]

Email 2:
From: David Park <david.p@client.com>
Subject: RE: Contract Amendment - URGENT
Need your sign-off on the revised terms today. Legal is waiting.

Email 3:
From: Team Calendar <calendar@company.com>
Subject: Meeting Reminder: Weekly Standup Tomorrow
Your weekly standup is scheduled for tomorrow at 10am.

Email 4:
From: James Wilson <j.wilson@vendor.com>
Subject: Invoice #4521 - Past Due Notice
Your invoice from December is 15 days past due. Please advise.

Email 5:
From: Maria Santos <m.santos@company.com>
Subject: Quick question about the Henderson proposal
Hey, when you get a chance, can you clarify the timeline section?
No rush, just want to make sure I'm reading it right before the client call next week.
```

**Expected output structure:**

```
# Email Triage Report

## Urgent (Respond Today)
1. **RE: Contract Amendment - URGENT** from David Park - Legal waiting for sign-off on contract terms

## Important (This Week)
1. **Invoice #4521 - Past Due Notice** from James Wilson - Past due vendor invoice needs resolution
2. **Quick question about the Henderson proposal** from Maria Santos - Clarification needed before client call next week

## FYI (When Available)
1. **Meeting Reminder: Weekly Standup Tomorrow** - Standard calendar reminder

## Can Ignore
1. **This Week in AI: January 2026 Roundup** - Newsletter/promotional

---
**Total:** 5 emails | **Urgent:** 1 | **Important:** 2 | **FYI:** 1 | **Ignore:** 1
```

The triage report tells you exactly where to focus your limited time.

## Batch Processing Pattern

When Gmail MCP is not yet configured, you can still benefit from email analysis by pasting content directly. This batch processing pattern works with any email source:

1. **Copy emails** from your email client (select multiple, copy)
2. **Paste into conversation** with your AI Employee
3. **Request triage** using the skill

```
I have these 10 emails from this morning. Create a triage report showing:
- What needs my attention today
- What can wait
- What I can ignore

[Paste email content here]
```

This approach works immediately, before any MCP integration. You can start getting value from your analysis skill today.

## Combining All Three Skills

Your AI Employee now has three email skills:

| Skill | Type | Purpose |
|-------|------|---------|
| email-drafter | Generation | Create email drafts from intentions |
| email-templates | Generation | Apply professional formats to content |
| email-summarizer | Analysis | Understand and prioritize incoming email |

Together, they form a complete email workflow:

```
Incoming Email
      │
      ▼
┌─────────────────┐
│ email-summarizer │  ← Understand what was received
└─────────────────┘
      │
      ▼
   Decision: Does this need a response?
      │
      ├── No → Archive or reference
      │
      └── Yes → What kind of response?
                    │
                    ▼
            ┌─────────────────┐
            │  email-drafter  │  ← Generate appropriate response
            └─────────────────┘
                    │
                    ▼
            ┌─────────────────┐
            │ email-templates │  ← Apply professional format
            └─────────────────┘
                    │
                    ▼
               Ready to Send
```

### Workflow Example

Here is how the skills compose in practice:

**Step 1: Analyze incoming email**
```
Summarize this email from my client:

[Client email about project delay concerns]
```

AI Employee produces structured analysis showing priority, action required, and key points.

**Step 2: Decide and draft response**
```
Draft a response that:
- Acknowledges their concern
- Explains our mitigation plan
- Proposes a check-in call this week
```

AI Employee produces draft using email-drafter skill.

**Step 3: Apply professional format**
```
Make this a formal client communication with appropriate sign-off
```

AI Employee applies email-templates skill.

The three skills work together, each handling its part of the workflow. You make the strategic decisions (what kind of response, what tone). Your AI Employee handles the execution (analysis, drafting, formatting).

## Skill Composition Insight

Notice what just happened. You did not build one massive "email handling" skill. You built three focused skills, each doing one thing well:

- **email-summarizer**: Turns chaos into clarity
- **email-drafter**: Turns intention into words
- **email-templates**: Turns words into professional formats

This composition approach has advantages:

**Reusability**: Each skill can be used independently. Email-summarizer works for emails you will not reply to. Email-templates works for documents beyond email.

**Maintainability**: When you want to improve summarization, you update one skill without touching the others.

**Flexibility**: You can skip steps when they are not needed. Quick internal email? Draft directly, skip templates. Complex thread? Analyze thoroughly, skip drafting if you need to think first.

**Portability**: Each skill transfers to any MCP-compatible platform. Your investment is protected.

This is the pattern you will use throughout this book: small, focused skills that compose into larger workflows. The power comes from composition, not from monolithic complexity.

## Try With AI

### Prompt 1: Analysis Skill Design

```
I want to create an analysis skill for [your domain: sales calls, support tickets,
meeting notes, research papers, etc.].

Help me design the structured output format. For my [domain items], I need to
quickly understand:
- [What key information matters most]
- [How to categorize/prioritize]
- [What actions might be required]

Create a template similar to the email-summarizer that would work for my use case.
Show me the SKILL.md content I would create.
```

**What you're learning**: How to transfer the analysis skill pattern to your own domain. You're learning that structured output formats can be designed for any information type, not just email. The key is identifying what decisions you need to make and what information enables those decisions.

### Prompt 2: Workflow Composition

```
I have these three activities in my work:
1. [Receiving something: emails, tickets, requests, documents]
2. [Processing/deciding: prioritizing, routing, responding]
3. [Creating output: responses, reports, summaries, decisions]

Help me design a three-skill workflow similar to the email workflow in this lesson.
What would each skill do? How would they connect? What decisions stay with me
versus what can the AI Employee handle?
```

**What you're learning**: How to identify skill boundaries in your own workflows. You're learning to separate analysis (understanding input) from decision (choosing action) from generation (creating output), keeping human judgment where it matters most.

**Safety note**: Analysis skills read your content but should not take action on it. When testing, use emails or documents you are comfortable sharing with your AI Employee. Start with low-sensitivity content until you trust the skill's behavior.
