---
sidebar_position: 0
title: "Why Specs Beat Vibe Coding"
description: "Understand the failure modes of conversational AI coding and why specifications solve them"
keywords:
  [
    "spec-driven development",
    "vibe coding",
    "context loss",
    "assumption drift",
    "pattern violations",
    "specifications",
    "AI coding",
    "Claude Code",
  ]
chapter: 5
lesson: 0
duration_minutes: 15

# HIDDEN SKILLS METADATA
skills:
  - name: "Identify Vibe Coding Failure Modes"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can diagnose which failure mode is causing a broken AI interaction"

  - name: "Explain Context Loss"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can describe how iterative discovery loses accumulated knowledge"

  - name: "Explain Assumption Drift"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain why reasonable AI assumptions often diverge from developer intent"

  - name: "Explain Pattern Violations"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify when generated code conflicts with project architecture"

learning_objectives:
  - objective: "Identify the three failure modes of vibe coding in an AI conversation"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Given a failed conversation transcript, student identifies which failure mode(s) occurred"

  - objective: "Explain why iterative discovery through conversation leads to context loss"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student describes the mechanism of context loss in their own words"

  - objective: "Articulate what information AI needs upfront to avoid the three failure modes"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student lists the categories of information that prevent each failure mode"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (vibe coding, context loss, assumption drift, pattern violations, specification upfront) within A2 range of 5-7"

differentiation:
  extension_for_advanced: "Analyze how context window limits compound the three failure modes over long conversations"
  remedial_for_struggling: "Focus on recognizing the three failure modes before exploring solutions"
---

# Why Specs Beat Vibe Coding

You ask Claude to add a notification system. It generates code. You realize you needed email support too, so you ask for that. Claude adds it, but now the original notification types are gone. You clarify, and Claude apologizes and fixes it—but the styling breaks. Twenty minutes later, you have code that technically works but matches nothing in your existing architecture.

Sound familiar?

This is **vibe coding**—the natural way developers first approach AI coding assistants. You have a vague idea, you describe it, and AI generates something. You refine through conversation. Sometimes it works brilliantly. Other times, you spend more time correcting than you would have spent writing the code yourself.

The problem is not the AI. The problem is the workflow. Vibe coding fails systematically for production work, and understanding why reveals the solution.

## The Vibe Coding Pattern

Vibe coding follows a predictable cycle:

```
Prompt → Code → "No, I meant..." → Code → "Actually..." → Code → Repeat
```

Each iteration seems like progress. You're getting closer to what you want. But something corrosive happens beneath the surface.

Consider this real conversation (simplified for clarity):

**Turn 1:**
"Add a notification system to my app."

Claude generates a notification system with in-app popups.

**Turn 5:**
"Also support email notifications."

Claude adds email support but refactors the popup code, changing how notifications are triggered.

**Turn 9:**
"The popups stopped working. Fix them."

Claude fixes popups but now sends duplicate emails.

**Turn 14:**
"Why is this using a different database table than our user_preferences table?"

Claude apologizes and attempts migration logic, but introduces a foreign key that conflicts with existing schema.

**Turn 20:**
Developer gives up and starts over.

What went wrong? Not any single turn—each response was reasonable given the question asked. The failure is structural.

## Three Failure Modes

Vibe coding fails in three predictable ways. Once you recognize these patterns, you'll see them everywhere.

### 1. Context Loss: Each Iteration Loses Discoveries

When you ask Claude to add email support in Turn 5, it focuses on that request. The nuances you established in earlier turns—the specific event types, the popup positioning, the animation decisions—fade from attention. Not because Claude forgot (they're technically still in context), but because newer information receives more weight.

**The mechanism**: Each new request shifts focus. Previous decisions become background noise. With enough turns, early requirements are effectively invisible.

**What it looks like**:

- Features that worked stop working after unrelated changes
- Decisions you made early get silently reversed later
- You find yourself re-explaining the same constraints

### 2. Assumption Drift: Reasonable Guesses Diverge from Intent

You said "notification system." Claude reasonably assumed:

- Notifications are stored in their own table
- Email notifications are separate from in-app notifications
- The system should support future notification types

Each assumption is defensible. An experienced developer might make the same choices. But you already have a `user_preferences` table with notification settings. Your existing architecture uses a unified event system. You only need two notification types, ever.

**The mechanism**: Without explicit constraints, AI fills gaps with reasonable defaults. Those defaults compound, and by Turn 10, you're debugging code designed for requirements you never had.

**What it looks like**:

- Generated code works but feels foreign to your codebase
- You discover structural decisions you didn't ask for
- Fixes require understanding an architecture you didn't design

### 3. Pattern Violations: Generated Code Ignores Project Architecture

Turn 14 reveals the deepest problem. Claude created a new database table because that's a reasonable pattern for notification systems. But your project has specific patterns: all user-related data lives in `user_preferences`, all events flow through a central event bus, all database migrations follow a specific naming convention.

**The mechanism**: Without knowledge of your project's patterns, AI generates code that follows general best practices. Those practices may directly contradict your specific architecture.

**What it looks like**:

- Code works but doesn't fit the existing codebase
- Other developers question why new code follows different patterns
- Integration requires significant refactoring

## The Compounding Problem

These three modes don't just occur—they amplify each other.

Context loss means you stop re-explaining constraints. Assumption drift means Claude fills those gaps with defaults. Pattern violations mean the defaults conflict with your architecture. By Turn 15, you're not iterating toward your goal. You're managing an increasingly divergent codebase.

| Turn  | Context Loss | Assumption Drift | Pattern Violations |
| ----- | ------------ | ---------------- | ------------------ |
| 1-5   | Minimal      | Beginning        | Undetected         |
| 6-10  | Noticeable   | Compounding      | Emerging           |
| 11-15 | Significant  | Structural       | Blocking           |
| 16+   | Critical     | Architectural    | Requires rewrite   |

The further you go, the harder correction becomes. This is why vibe coding works for simple tasks but fails for complex ones.

## The Insight: Claude Needs the Complete Picture Upfront

The solution is surprisingly simple once you see the problem clearly.

Claude can implement a notification system correctly on the first try—if it knows:

- **What exists**: Your current tables, patterns, and architecture
- **What to build**: Specific requirements, not vague features
- **What NOT to build**: Explicit constraints and boundaries
- **How to validate**: Success criteria that can be verified

The pattern for all three failure modes is the same: information Claude needed but didn't have. Context loss happens because requirements weren't written down. Assumption drift happens because constraints weren't explicit. Pattern violations happen because existing architecture wasn't communicated.

**The specification captures this information once, upfront.**

| Failure Mode       | Prevented By                                     |
| ------------------ | ------------------------------------------------ |
| Context loss       | Written requirements that persist across turns   |
| Assumption drift   | Explicit constraints that eliminate guessing     |
| Pattern violations | Architecture documentation that defines patterns |

This is the foundation of Spec-Driven Development: front-loading the information Claude needs rather than discovering it through iteration.

## What Comes Next

The rest of this chapter builds on this insight:

- **Lesson 01** introduces three levels of SDD—from lightweight specs to full workflow orchestration
- **Lesson 02** presents the four-phase workflow that structures spec creation and implementation
- **Lessons 03-06** dive deep into each phase with practical techniques
- **Lesson 07** helps you decide when SDD adds value versus when simpler approaches work better

You don't need complex tools or frameworks. Everything in this chapter uses native Claude Code capabilities you already have access to.

## Try With AI

These prompts help you experience the concepts from this lesson firsthand.

**Prompt 1: Experience the Problem**

```
Add a notification system to my app.
```

After Claude generates code, follow up with variations: "Also support email," "Add scheduling," "Integrate with existing user preferences." Notice what happens to earlier decisions as you iterate.

**What you're learning:** The vibe coding failure pattern happens quickly, even with simple features. By experiencing it directly, you develop intuition for recognizing when iteration is degrading rather than improving.

**Prompt 2: Surface the Assumptions**

```
Look at the notification code you just generated.
List every assumption you made that I didn't explicitly specify.
For each assumption, explain what question you would have asked
if you knew to ask it.
```

**What you're learning:** AI makes dozens of implicit decisions. This prompt makes them visible. The list of "questions Claude would have asked" is essentially the outline of a specification.

**Prompt 3: Identify What Was Missing**

```
Given our conversation about the notification system:
- What information would you have needed upfront to build this correctly the first time?
- Organize that information into categories (requirements, constraints, existing architecture, success criteria).
```

**What you're learning:** Claude can articulate what it needed but didn't have. This reflection transforms frustrating iteration into actionable specification structure. The categories Claude identifies map directly to specification sections in later lessons.
