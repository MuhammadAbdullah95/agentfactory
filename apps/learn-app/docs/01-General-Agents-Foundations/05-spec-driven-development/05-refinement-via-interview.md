---
sidebar_position: 5
title: "Phase 3: Refinement via Interview"
description: "Surface design decisions and ambiguities before implementation through structured AI interviews using the ask_user_question tool"
keywords:
  [
    "spec-driven development",
    "refinement phase",
    "ask_user_question",
    "design decisions",
    "ambiguity resolution",
    "interview pattern",
    "implementation planning",
  ]
chapter: 5
lesson: 5
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Apply Interview Pattern for Spec Refinement"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can trigger the interview pattern and respond to AI questions to refine their specification"

  - name: "Identify Common Ambiguity Categories"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can list the five categories where ambiguities commonly hide in specifications"

  - name: "Evaluate Specification Completeness"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can use the interview checklist to assess whether their specification is implementation-ready"

learning_objectives:
  - objective: "Apply the ask_user_question prompt pattern to surface specification ambiguities"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student successfully triggers an AI interview and responds to clarifying questions"

  - objective: "Explain why each ambiguity found before coding saves 10x time during implementation"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can articulate the cost multiplier of mid-implementation pivots"

  - objective: "Use the interview checklist to validate specification completeness"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student can apply the checklist categories to their own specifications"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (interview pattern, ask_user_question tool, ambiguity categories, 10x cost multiplier, interview checklist) within B1 range"

differentiation:
  extension_for_advanced: "Design custom interview questions for domain-specific specifications beyond the standard checklist"
  remedial_for_struggling: "Focus on the five ambiguity categories first, then practice the prompt pattern"
---

# Phase 3: Refinement via Interview

Every ambiguity you find before coding saves 10x the time it would cost to fix mid-implementation.

In Lesson 4, you learned to write effective specifications. But even well-structured specs contain hidden assumptions. You know what "conflict resolution" means in your head. Does Claude? You imagine the error handling approach. Did you write it down?

This lesson teaches the refinement phase: a structured interview where Claude surfaces every design decision that would otherwise become a mid-implementation pivot. The result is a specification precise enough that implementation becomes execution of a well-understood plan.

## The Interview Pattern

The refinement phase uses a specific prompt pattern that triggers Claude's ask_user_question tool:

```
Here's my spec. Use the ask_user_question tool to surface any ambiguities
before we implement.
```

When you give this instruction, Claude shifts from implementation mode to investigation mode. Instead of generating code, Claude reads your specification critically and asks questions about anything unclear, unstated, or potentially problematic.

**What makes this different from conversation:**

In normal prompting, you ask questions and Claude answers. In the interview pattern, the roles reverse. Claude asks questions and you answer. This shift matters because Claude can identify gaps you didn't know existed—assumptions so natural to you that you didn't think to document them.

## Why Ambiguities Are Expensive

Consider what happens when an ambiguity survives to implementation:

| When Discovered        | What Happens                                     | Time Cost  |
| ---------------------- | ------------------------------------------------ | ---------- |
| **During spec**        | Add clarification, continue                      | 5 minutes  |
| **During interview**   | Answer question, update spec                     | 10 minutes |
| **During coding**      | Stop, discuss, decide, restart                   | 30 minutes |
| **After first commit** | Code review reveals issue, refactor needed       | 2-4 hours  |
| **In production**      | Bug report, investigation, emergency fix, review | 8-16 hours |

The 10x multiplier is conservative. A decision that takes 10 minutes to clarify in an interview can cost days when discovered after deployment.

**Real example:** A developer's specification said "handle conflicts optimistically." The developer meant "last write wins." Claude interpreted this as "prompt user to resolve." Implementation proceeded with user prompts. The developer discovered this three days later during testing. Refactoring took an entire afternoon—time that a single interview question would have prevented.

## The Five Ambiguity Categories

Claude's interview questions cluster around five categories. Understanding these helps you anticipate questions and write better specs proactively.

### 1. Data Decisions

How existing information transitions to the new system:

- Should we migrate existing data or start fresh?
- What happens to records that don't match the new schema?
- How do we handle data from the old system during the transition period?

**Why this matters:** Data decisions are often unstated because developers assume "obviously we keep our data." But the HOW requires explicit decisions.

### 2. Conflict Resolution

What happens when systems disagree:

- What's the conflict resolution strategy? (Last write wins? User resolves? Merge automatically?)
- If two users edit simultaneously, who wins?
- What happens when local and server state diverge?

**Why this matters:** Every multi-user or distributed system faces conflicts. The absence of a stated strategy means Claude chooses one—possibly not the one you wanted.

### 3. Pattern Selection

Which approach among valid alternatives:

- The research found two patterns for this. Which matches your constraints?
- Should we use the approach from [reference A] or [reference B]?
- Given your performance requirements, which architecture fits?

**Why this matters:** Research often surfaces multiple valid approaches. Without explicit selection, Claude picks based on its training distribution—not your project's needs.

### 4. Failure Recovery

What happens when things go wrong:

- What's the failure recovery approach?
- If the external API times out, do we retry, queue, or fail?
- What state should the system preserve after a crash?

**Why this matters:** Happy path specifications are common. Error path specifications are rare. But production systems spend significant time in error states.

### 5. Boundary Conditions

Where the system's scope ends:

- What happens at the rate limit boundary?
- How do we handle users who exceed storage quotas?
- What's the maximum scale this needs to support?

**Why this matters:** Specifications often describe the normal case. Edge cases at boundaries are where implementations diverge from intent.

## The Interview in Action

Here's what a refinement interview looks like with a notification system specification:

**Your specification includes:**

```markdown
## Notification Preferences

Users can configure notification preferences per channel (email, SMS, push).
Default to email enabled, others disabled.
```

**Claude's interview questions:**

> Question 1: For notification preferences—if a user updates their preferences on mobile while the web app has unsaved changes, how should we handle that conflict?

Your answer: "Mobile wins. Mobile changes should apply immediately. Web should sync on next page load."

> Question 2: The spec mentions "per channel" preferences. Should users be able to configure different preferences per notification type within a channel? (e.g., "email me about security alerts but not marketing")

Your answer: "Yes, good catch. We need per-type settings within each channel, not just channel-level toggles."

> Question 3: What happens to queued notifications if a user disables a channel? Should pending notifications for that channel be deleted, held until re-enabled, or delivered via fallback channel?

Your answer: "Delete them. If they disabled email, they don't want emails—even ones that were about to send."

**Specification updates based on answers:**

```markdown
## Notification Preferences

Users can configure notification preferences per channel (email, SMS, push)
AND per notification type within each channel.

Default: email enabled for all types, others disabled.

### Conflict Resolution

Mobile preference changes take precedence. Web syncs on page load.

### Channel Disable Behavior

When user disables a channel, delete all pending notifications for that
channel. Do not deliver via fallback.
```

Three questions. Three decisions documented. Three mid-implementation pivots prevented.

## The Interview Checklist

Use this checklist to ensure your specification addresses common ambiguity areas before implementation:

```markdown
## Pre-Implementation Interview Checklist

### Data Decisions

[ ] Migration strategy defined (migrate existing / start fresh / hybrid)
[ ] Schema transition plan documented
[ ] Data validation rules specified

### Conflict Resolution

[ ] Multi-user edit strategy defined
[ ] Local/server sync behavior documented
[ ] Tie-breaking rules specified

### Pattern Selection

[ ] Architectural approach chosen from research options
[ ] Performance tradeoffs acknowledged
[ ] Scalability approach defined

### Failure Recovery

[ ] Timeout handling specified
[ ] Retry strategy documented
[ ] Crash recovery behavior defined
[ ] Error state persistence rules specified

### Boundary Conditions

[ ] Rate limits defined
[ ] Resource quotas documented
[ ] Scale limits acknowledged
[ ] Edge case behaviors specified
```

You don't need to fill every checkbox for every specification. A small utility script doesn't need crash recovery documentation. But running through the checklist surfaces which categories apply to your project.

## When to Stop Interviewing

The interview phase ends when:

1. **Questions become repetitive** — Claude asks variations of questions you've already answered
2. **New questions are trivial** — Questions about details that don't affect architecture
3. **Specification feels complete** — You can read through it and imagine implementation without guessing

If Claude's questions feel like implementation details rather than design decisions, you're ready for Phase 4.

**Warning sign:** If you're annoyed by the questions, that's often a signal that you haven't thought through those decisions. The annoyance comes from realizing you need to think harder, not from Claude being pedantic.

## Lab: Interview Your Specification

**Objective:** Practice the interview pattern on a real specification.

### Task

Take a specification you've written (or use the one from Lesson 4's lab). Run it through the interview pattern:

1. **Trigger the interview:**

   ```
   Here's my spec. Use the ask_user_question tool to surface any ambiguities
   before we implement.

   [paste your spec]
   ```

2. **Answer the questions thoughtfully.** Don't rush. Each question represents a potential mid-implementation pivot.

3. **Update your specification** with decisions from your answers.

4. **Check the checklist.** Which categories did Claude's questions address? Which categories weren't relevant to your spec?

The goal isn't to fill checkboxes—it's to surface decisions you hadn't consciously made.

## Try With AI

**Prompt 1: Initial Interview**

```
Here's my spec. Use the ask_user_question tool to surface any ambiguities
before we implement.

[paste your specification]
```

**What you're learning:** The interview pattern shifts Claude from implementation mode to investigation mode. You're practicing how to trigger this shift and respond to Claude's questions effectively.

**Prompt 2: Specification Update**

```
Based on my answers to your questions, update the spec with the clarified
requirements. Preserve the original structure but add the new decisions
we've made.
```

**What you're learning:** Decisions made during the interview need to persist in the specification. This prompt ensures your answers become documented constraints, not conversation history that disappears on session end.

**Prompt 3: Decision Summary**

```
What are the three most important decisions we made during this interview
that will affect implementation? For each one, explain what would have
happened if we hadn't clarified it.
```

**What you're learning:** Not all decisions are equal. Some affect architecture fundamentally; others are details. This prompt develops your judgment about which interview outcomes matter most—helping you prioritize future refinement efforts.

**Safety note:** Interview prompts examine your specification—they don't modify code or make irreversible changes. You're developing the habit of refinement before implementation, not during it.
