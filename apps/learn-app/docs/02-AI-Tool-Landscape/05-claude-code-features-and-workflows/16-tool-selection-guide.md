---
title: "Strategic Tool Selection: Build Your Digital FTE Architecture"
sidebar_position: 16
chapter: 5
lesson: 16
duration_minutes: 10
chapter_type: Concept
running_example_id: tool-selection-framework

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 (Strategic Synthesis)"
layer_1_foundation: "N/A"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "Synthesizing all tool concepts into a strategic decision framework"

# HIDDEN SKILLS METADATA
skills:
  - name: "Strategic Tool Selection"
    proficiency_level: "C1"
    category: "Strategic"
    bloom_level: "Evaluate"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can analyze a workflow problem and select the optimal Claude Code extension mechanism (Skill vs Subagent vs MCP vs Hook) based on technical and operational constraints"

learning_objectives:
  - objective: "Select the correct extension mechanism for a given problem"
    proficiency_level: "C1"
    bloom_level: "Evaluate"
    assessment_method: "Scenario-based matching exercise"
  - objective: "Understand the 'Digital FTE' department analogy for extensions"
    proficiency_level: "B2"
    bloom_level: "Understand"
    assessment_method: "Mapping technical tools to organizational roles"
    
# Cognitive load tracking
cognitive_load:
  new_concepts: 1
  assessment: "1 concept (The Hierarchy of Automation) - Low load synthesis lesson"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Design a complex system using all 5 tools"
  remedial_for_struggling: "Focus solely on the '5-Second Guide' table"

# Generation metadata
generated_by: "antigravity-editor"
source_spec: "specs/029-chapter-5-refinement/spec.md"
created: "2026-01-15"
version: "1.0.0"

# Legacy compatibility
prerequisites:
  - "Lessons 01-16: Familiarity with all tool types"
---

# The Tool Selection Guide: The Hierarchy of Automation

You’ve learned the parts. You know how to build a Skill, configure a Subagent, and connect an MCP server.

But the most common question from founders and developers isn’t *"How do I build X?"*—it’s *"WHAT should I build?"*

> *"I want to automate my code reviews. Is that a Skill? Or a Subagent?"*
> *"I need to search my database. Do I need an MCP server, or can a Skill do that?"*

This guide is your compass. We’ll cut through the complexity with a simple decision framework.

---

## The 5-Second Decision Guide

If you stop reading here, memorize this table. It solves 90% of architectural debates.

| If you need... | Then use... | The "Digital FTE" Analogy |
| :--- | :--- | :--- |
| **Persistent Context** | **CLAUDE.md** | The Employee Handbook |
| **Repeated Procedures** | **Skill** | A Standard Operating Procedure (SOP) |
| **Delegation & Focus** | **Subagent** | A Specialized Department / Team |
| **External Systems/Data** | **MCP** | IT Access / Permitted Software |
| **Quality Gates/Safety** | **Hooks** | Compliance & Security Officers |

---

## The Decision Flow

When you face a new automation challenge, ask these questions in order:

**Question 1: Does it need external data or external systems?**
- **Yes** (Jira, database, API, website) → **Use MCP**
- **No** (local files, local context) → Continue to Q2

**Question 2: Is it a complex, multi-step workflow requiring autonomy?**
- **Yes** (research, analysis, report generation) → **Use Subagent**
- **No** (specific, bounded task) → Continue to Q3

**Question 3: Is it about enforcing rules or preventing bad actions?**
- **Yes** (validation, security, compliance) → **Use Hook**
- **No** (helpful procedure) → Continue to Q4

**Question 4: Do you explain this task the same way every time?**
- **Yes** (repetitive, consistent procedure) → **Use Skill**
- **No** (context-dependent, general knowledge) → **Use CLAUDE.md**

---

## The "Digital FTE" Mental Model

To truly design "Digital Employees," stop thinking like a developer (functions, scripts) and start thinking like a Manager (roles, responsibilities).

#### 1. CLAUDE.md: The Employee Handbook

Every new hire gets a handbook. It tells them: *"Here is our mission. Here is how we prefer things formatted. Here is who to ask for help."*

**Use when:**
- You want to set the baseline culture and context for every interaction

**Don't use for:**
- Specific, granular tasks (too much noise)

#### 2. Skills: Standard Operating Procedures

When you hire an accountant, you give them a checklist: *"Project Setup Checklist."* *"End-of-Month Protocol."*

**Use when:**
- You have a repeatable task (writing a test, formatting a blog post) that you want done *your way*

**Don't use for:**
- Massive, ambiguous projects requiring 2 hours of autonomy

#### 3. Subagents: Specialized Departments

You don't ask the "General Receptionist" to audit your taxes. You send that to the "Accounting Department."

**Use when:**
- The task requires a different *mindset* or set of tools
- Example: A "Testing Subagent" needs different prompts than a "Creative Writing Subagent"

**Don't use for:**
- Simple tasks (creating a whole department to "fix a typo" is bureaucracy)

#### 4. MCP: IT Access & Software

An employee can't check Salesforce if you don't give them a login. MCP is that login.

**Use when:**
- The intelligence is locked away in a database, API, or website

**Don't use for:**
- Things the model already knows (e.g., Python syntax)

#### 5. Hooks: Compliance & Security

The Compliance Officer doesn't do the work; they typically *stop* work that is dangerous. *"Stop! You can't merge to main without approval."*

**Use when:**
- You need to enforce hard constraints or automate invisible logging

**Don't use for:**
- Helpful suggestions (that's a Skill)

---

## Common Scenarios: What Would You Pick?

- **Scenario A:** "I want Claude to check our Jira board for new tickets."

**Analysis:** Does it need external data? Yes (Jira is a project management tool outside your computer).

**Selection:** **MCP**. You need a Jira MCP server.

- Scenario B: "Every time Claude writes code, I want it to follow our naming conventions consistently."

**Analysis:** Is it a repeated preference? Yes.

**Selection:** **CLAUDE.md** (if it's a global project rule) or **Skill** (if specific to one task type). Likely **CLAUDE.md**.

- Scenario C: "I want to give Claude a 'Research Mode' where it browses the web, summarizes 50 pages, and writes a report without distracting me."

**Analysis:** Is it complex? Yes. Does it need focused autonomy? Yes.

**Selection:** **Subagent**. Create a "Researcher" subagent equipped with Browser MCP.

- Scenario D: "Stop Claude from committing secrets/API keys to git."

**Analysis:** Is it safety/validation? Yes (preventing accidental leaks of passwords).

**Selection:** **Hook**. A `pre-git-commit` hook (a script that runs before saving changes).

---

## The Strategic Takeaway

**Amateurs build prompts to conplete current work - vibe code the current task.**

**Professionals build Systems.**

A "System" is simply the smart combination of these five elements. Your goal as an Agent Architect is to place the complexity in the right bucket.

---

## See It in Action

This framework is the decision-making engine. But what does it look like when applied?

Lesson 17 shows how Boris Cherny—the creator of Claude Code—actually uses these tools together in his daily workflow. 15-20 parallel sessions, Plan Mode discipline, specialized subagents for different tasks, Hooks automating the edge cases.

Study his patterns. They're blueprints for your own systems.