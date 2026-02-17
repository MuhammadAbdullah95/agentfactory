---
sidebar_position: 6
title: "Your Employee Orchestrating Agents"
description: "Watch your AI Employee delegate complex tasks to General Agents, understand the two-tier delegation pattern, and see the Agent Factory thesis running live"
keywords:
  [
    ai employee delegation,
    general agents,
    custom agents,
    agent orchestration,
    two-tier delegation,
    claude code delegation,
    agent factory thesis,
  ]
chapter: 7
lesson: 6
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Delegation Understanding"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can explain the two-tier delegation pattern (Custom Agent manages context, General Agent executes tasks) and identify when delegation adds value"

  - name: "Delegation Workflow Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can design a multi-step workflow that leverages delegation between Custom and General Agents for non-coding tasks"

learning_objectives:
  - objective: "Observe and explain the two-tier delegation pattern (Custom Agent to General Agent) through hands-on tasks"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student sends complex tasks to their AI Employee, observes the delegation behavior, and describes the Custom Agent/General Agent relationship in their own words"

  - objective: "Distinguish between tasks the employee handles directly versus delegates to General Agents"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Given a list of tasks, student correctly classifies which require delegation and explains the decision criteria"

  - objective: "Design a multi-step workflow that leverages agent delegation for research, analysis, and document creation"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates a workflow description that identifies which steps the employee handles directly and which it delegates, with reasoning for each decision"

cognitive_load:
  new_concepts: 5
  concepts_list:
    - "Two-tier delegation (Custom Agent manages, General Agent executes)"
    - "Invisible orchestration (employee decides when and how to delegate)"
    - "Context vs capability (employee has context, specialist has skills)"
    - "Parallel delegation (multiple agents working simultaneously)"
    - "Delegation judgment (when to delegate vs handle directly)"
  assessment: "5 concepts within B1 range (7-10). Each concept builds on the Custom Agent vs General Agent distinction from Chapter 1. Exercises ground every concept in hands-on experience."

differentiation:
  extension_for_advanced: "Design a 5-step daily workflow where your employee delegates different steps to different General Agents. Document the handoff points and what context each agent needs."
  remedial_for_struggling: "Focus on Exercise 1 only. Observe whether your employee delegates or handles directly. Describe the result in your own words."
---

# Your Employee Orchestrating Agents

In Lesson 5, you taught your AI Employee new skills and learned why security matters when running agents on your machine. Those skills handle text-based work -- meeting prep, research summaries, skill creation. But some tasks need more than your employee can do alone: deep analysis across dozens of files, complex research requiring multiple sources, or creating entire project structures from scratch.

In Chapter 3, you used Claude Code directly -- typing commands, reviewing output, iterating on results. Now watch what happens when your AI Employee uses Claude Code for you. You do not manage the process. You do not choose which agent handles what. You ask for a result, and your employee figures out the orchestration.

This is the Agent Factory thesis from Chapter 1, running live. Your employee is a Custom Agent -- it knows your context, your projects, your preferences. Claude Code is a General Agent -- a specialist that can research, analyze, and create with capabilities your employee does not have. Together, they form something neither could be alone.

## Delegation in Action

The best way to understand delegation is to trigger it. Send your AI Employee tasks complex enough that it needs help -- then watch what happens.

### Exercise 1: Research Delegation

Send this to your employee on Telegram (adapt the topic to your interests):

```
Research the top 5 AI agent frameworks released in 2025-2026.
For each, create a comparison table with: name, primary language,
key features, GitHub stars, and best use case. Save as
frameworks-comparison.md in my workspace.
```

Watch the response. Your employee may handle parts of this itself (it already knows some framework names from its training data) and delegate other parts to a General Agent (web research for current star counts, file creation). The result arrives as a file you can open and verify.

**What to observe:** Did your employee mention delegating? Did it take longer than a simple question would? The exact behavior depends on how your instance is configured -- the point is that you asked for a result and received a result, without managing the process in between.

### Exercise 2: Document Creation

```
Create a project proposal for building a personal finance tracker.
Include an executive summary, problem statement, proposed solution,
timeline with milestones, and budget estimate. Save as proposal.md.
```

This task requires your employee to combine what it knows about you (your workspace, your preferences from MEMORY.md) with substantial writing and structuring work. For a task this large, delegation to a General Agent becomes valuable -- the specialist handles the heavy research and document creation while your employee provides the personal context.

### Exercise 3: Multi-Step Analysis

```
Read all the markdown files in my workspace. Create a summary
of what I have been working on this week, identify the 3 most
important tasks I should focus on tomorrow, and save the analysis
as weekly-review.md.
```

This forces multi-step work: file reading, synthesis, analysis, prioritization, and writing. Your employee decides what to handle itself and what to delegate. The result is a personalized weekly review that neither agent could produce alone -- Claude Code does not know your priorities, and your employee may not have the deep file analysis capabilities.

### The Takeaway

You did not manage the delegation. You did not choose which agent handles what. You did not supervise the process. You asked for a result, and your employee figured out the orchestration. That is the difference between using a tool and having an employee.

---

## The Delegation Pattern

Now that you have seen delegation in action, here is what happened under the hood -- at a conceptual level, not a technical one.

```
You (Telegram) --> Employee (Custom Agent) --> General Agent --> Result
                                            <-- Files/Reports <--
```

Two roles, two types of knowledge:

| Role              | Type          | What It Knows                                    |
| ----------------- | ------------- | ------------------------------------------------ |
| **Your Employee** | Custom Agent  | Your projects, preferences, schedule, domain     |
| **Claude Code**   | General Agent | How to research, analyze, create files, organize |

Neither is sufficient alone. Claude Code can do excellent research and create well-structured documents, but it does not know which project you are focused on, what your priorities are, or what format you prefer. Your employee knows all of that context but may need a specialist for complex, multi-step tasks.

Together: the manager who understands your needs plus the specialist who has the execution capability. This is the same pattern behind every effective team -- human or AI.

Your employee handles delegation internally. It decides when to delegate, which agent to use, and how to pass context. You never need to manage this process -- just like a good human manager delegates without making you supervise the delegation.

---

## What General Agents Can Do

Your employee can delegate to different General Agents depending on what is available on your machine:

| Agent           | What It Excels At                                           |
| --------------- | ----------------------------------------------------------- |
| **Claude Code** | Deep research, file operations, analysis, document creation |
| **Codex CLI**   | Multi-file operations, structured output                    |
| **OpenCode**    | Model-agnostic -- works with any LLM provider               |

The delegation pattern stays the same regardless of which specialist is behind it. Your employee sends the brief, provides your context, and reports the result. The specialist changes; the pattern does not.

When you learn programming in later chapters, these same General Agents handle coding tasks too -- writing scripts, debugging, refactoring, testing. The delegation pattern does not change. Only the tasks get more technical.

---

## The Scaling Insight

One employee. Multiple specialists. Parallel when needed.

Your employee can delegate multiple tasks simultaneously. While one General Agent researches competitors, another organizes your files, and a third drafts a report. You asked once. Three specialists worked. One employee managed them all.

This is why Chapter 1 called it a "factory." You are not building one agent that does everything. You are assembling specialists managed by an agent that knows you. The employee becomes more capable not by learning every skill, but by knowing which specialist to call for each task.

Consider the difference:

| Approach                         | Limitation                                      |
| -------------------------------- | ----------------------------------------------- |
| **One agent does everything**    | Limited by that agent's capabilities            |
| **You manage multiple agents**   | Limited by your time and attention              |
| **Employee manages specialists** | Scales with the number of available specialists |

The third approach is the Agent Factory model. Your employee is the factory floor manager. General Agents are the specialists on the line.

---

## What Transfers

The delegation pattern you just experienced is not specific to OpenClaw. It is the architectural foundation of every multi-agent system:

| Concept                     | In OpenClaw                                 | In Any Framework                         |
| --------------------------- | ------------------------------------------- | ---------------------------------------- |
| **Custom Agent manages**    | Your employee knows your context            | Orchestrator holds user preferences      |
| **General Agent executes**  | Claude Code performs tasks                  | Specialist agent performs task           |
| **Delegation is invisible** | Employee decides when and how to delegate   | Orchestrator routes to best agent        |
| **Parallel execution**      | Multiple agents work simultaneously         | Async task execution                     |
| **Context + Capability**    | Employee has context, specialist has skills | Orchestrator has state, worker has tools |

When you build your own AI Employee in Chapter 13, you implement this exact pattern: a Custom Agent that knows your domain, delegating to General Agents that have technical skills. The employee you used in this chapter is your prototype. The one you build will be yours from the ground up.

---

## Try With AI

### Prompt 1: Delegation Boundaries

```
For these 6 tasks, which should my AI Employee handle directly
versus delegate to a General Agent? Explain the decision criteria.

1. Summarize a meeting transcript
2. Research and compare 10 cloud hosting providers
3. Draft a project status email
4. Analyze all files in a project folder and create a dependency map
5. Remind me about a deadline tomorrow
6. Create a 20-page market analysis with charts and recommendations
```

**What you're learning:** Judgment about when delegation adds value. Not every task needs a specialist -- the overhead of delegation only pays off for complex, multi-step work. Simple tasks (reminders, short emails) are faster handled directly. Complex tasks (deep research, multi-file analysis) benefit from a specialist. Developing this judgment is the core skill of an effective agent manager.

### Prompt 2: Multi-Agent Workflow

```
Design a weekly review workflow for a small business owner:
gather workspace activity, summarize accomplishments, identify
blockers, and suggest priorities for next week. Which parts
should the employee handle directly versus delegate to a
General Agent? Explain the handoff points.
```

**What you're learning:** Workflow design -- breaking a complex goal into steps and deciding which agent handles each step. Real productivity comes from orchestrated workflows where different agents handle different parts of a pipeline. This is the same design thinking you will use when building your own AI Employee in Chapter 13.
