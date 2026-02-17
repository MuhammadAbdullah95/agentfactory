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

In Lesson 5, you taught your employee skills and learned why security matters. Those skills handled focused tasks -- meeting prep, research summaries, progress reports. Now give it something harder. Complex enough that one agent cannot handle it alone. Watch what happens.

## Push Your Employee

Each exercise produces a real file you keep. Adapt every prompt to YOUR actual field, role, and industry.

### Exercise 1: Competitive Intelligence

Send this to your AI Employee (adapt to your industry):

```
Research the top 5 competitors in [YOUR INDUSTRY]. For each,
find their pricing, target market, key differentiator, and
one weakness. Save as competitors.md in my workspace.
```

This requires web research, synthesis, structured output, and file creation. Your employee may research some competitors directly and delegate deeper research to Claude Code for current pricing and market data.

Open the file when it is done. Check the competitors. Is the pricing current? Did it miss anyone obvious? Edit the file with your own knowledge -- add the competitor only you know about, correct the pricing your experience tells you is wrong. This artifact is yours now.

### Exercise 2: Weekly Planning System

```
Look at my recent files and conversations. Based on what I have
been working on, create a weekly plan for next week with:
- 3 priority tasks ranked by impact
- 2 tasks I should delegate or automate
- 1 thing I should stop doing
Save as weekly-plan.md.
```

This requires reading your workspace, understanding your context from MEMORY.md, analyzing patterns, and making judgment calls. It is the kind of task you would ask a sharp coworker to help with.

Does the plan make sense? Challenge it:

```
I disagree with priority #1. I think [YOUR REASON]. Also,
what would you automate from the "delegate" list and how?
```

Your employee explains its reasoning and adapts to your pushback. The plan improves because you brought domain knowledge it did not have.

### Exercise 3: Business Idea Analysis

```
I'm considering [YOUR IDEA OR SIDE PROJECT]. Research whether
this is viable: who are the existing players, what's the market
size, what are the 3 biggest risks, and what would a minimum
viable version look like? Save as idea-analysis.md.
```

This is a task that would normally take you hours of research. Your employee orchestrates research, analysis, and structured writing -- delegating to Claude Code for deep web research while it handles the synthesis using what it knows about your goals and constraints.

Review the analysis. Is the market size reasonable? Did it identify real competitors? Add your own insights and save the updated version.

### Exercise 4: Design a Daily Routine

```
Design a complete daily AI Employee routine for my role as
[YOUR ROLE]. What should you do every morning before I check in?
What should you monitor during the day? What should you prepare
for me at end of day? Be specific to my actual work, not generic.
```

This produces a draft routine you will refine over the coming days. The employee uses everything it knows about you to personalize it.

Review the routine. Is the morning check useful? Would you actually read it at 8 AM? Iterate until it would change how you start your day:

```
The morning section is too long. Cut it to 3 bullet points max.
Add monitoring for [SOMETHING SPECIFIC TO YOUR WORK]. Remove the
end-of-day summary -- I never read those.
```

---

## What Just Happened

Each task was too complex for a single prompt-and-response. Your employee broke them into steps, decided what it could handle directly, and delegated what it could not. Research went to web tools. File analysis went to Claude Code. Synthesis stayed with your employee because it knows your context.

This is the **two-tier delegation pattern** from Chapter 1:

| Role                             | What It Contributes                               |
| -------------------------------- | ------------------------------------------------- |
| **Your Employee** (Custom Agent) | Context -- your projects, preferences, priorities |
| **Claude Code** (General Agent)  | Capability -- research, analysis, file operations |

You managed none of the delegation. You asked for results. That is the difference between orchestrating agents yourself (what you did in Chapter 3) and having an employee orchestrate them for you.

When you learn programming in later chapters, these same General Agents handle coding tasks too. The pattern does not change -- only the tasks get more technical.

---

## What Transfers

| Concept                      | What You Experienced                                              |
| ---------------------------- | ----------------------------------------------------------------- |
| Custom Agent manages context | Employee used your MEMORY.md and workspace to personalize results |
| General Agent executes       | Claude Code handled research and file operations                  |
| Delegation is invisible      | You never chose which agent handles what                          |
| Parallel execution           | Multiple steps can run simultaneously                             |
| The factory model            | One manager, multiple specialists, scales with available agents   |

When you build your own AI Employee in Chapter 13, you implement this exact pattern.

---

## Try With AI

### Prompt 1: Stress Test

```
Give me a task so complex it would take me an entire afternoon.
Something relevant to [YOUR ROLE]. Then do it.
```

**What you're learning:** Discovering the boundaries of what your employee can handle. The result will not be perfect -- but the first draft saves you hours. Your job is to edit, not to start from scratch.

### Prompt 2: Routine Refinement

```
Review the daily routine you designed in Exercise 4. What's missing?
Add monitoring for [SOMETHING SPECIFIC TO YOUR WORK] and remove
anything I wouldn't actually read.
```

**What you're learning:** Iteration. The first version of any routine needs refinement. This is the same delegation-then-review pattern from every lesson -- but now applied to a system you will use daily.
