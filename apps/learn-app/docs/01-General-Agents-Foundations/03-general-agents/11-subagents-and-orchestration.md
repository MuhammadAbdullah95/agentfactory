---
title: "Subagents and Orchestration"
sidebar_position: 11
chapter: 3
lesson: 11
duration_minutes: 12

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "N/A"
layer_2_collaboration: "Co-learning subagent design, Three Roles Framework applied to subagent creation, testing custom subagents with AI partnership"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Using and Creating Subagents for Task Specialization"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can use built-in subagents (Explore, Plan), invoke multiple subagents in parallel, and create custom subagents using /agents workflow"

learning_objectives:
  - objective: "Use built-in subagents (Explore, Plan) for immediate task delegation"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful invocation of Explore and Plan subagents with real tasks"
  - objective: "Invoke multiple subagents in parallel for complex workflows"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Demonstration of parallel subagent invocation in a single prompt"
  - objective: "Understand subagents as specialized AI assistants with isolated context"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of subagent execution model and context isolation benefits"
  - objective: "Create custom subagents using the /agents workflow"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Creation of functional custom subagent with appropriate instructions"

# Cognitive load tracking
cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (built-in agents, Explore/Plan usage, parallel invocation, context isolation, custom agents) - within B1 limit of 10 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Design multi-subagent workflows with orchestration patterns; create domain-specific subagent suites"
  remedial_for_struggling: "Focus on using Explore and Plan before creating custom subagents"

# Generation metadata
generated_by: "content-implementer v1.0.0 (029-chapter-5-refinement)"
source_spec: "specs/029-chapter-5-refinement/spec.md"
created: "2025-01-17"
last_modified: "2026-01-19"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "3.0.0"

# Legacy compatibility
prerequisites:
  - "Lessons 01-09: Claude Code installation, skills, architecture, CLAUDE.md"
  - "Experience with single-agent limitations (context loss, distraction)"
---

# Subagents and Orchestration

A subagent is a specialized AI Agent with its own instructions and isolated context window. Each subagent is an expert at one type of task.

Think of Claude Code as a project manager with a team of specialists:

- **Claude Code (main)**: Coordinates overall work
- **Plan subagent**: Researches your codebase and creates multi-step plans
- **Custom subagents**: You can create specialists for your team's specific needs (content planning, research synthesis, document structuring, etc.)

![Three-tier hierarchy tree showing Claude Code (orchestrator) at top, Subagents (specialized agents) in middle tier, and Skills (reusable capabilities) at bottom, with delegation arrows and example instances](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-2/chapter-05/skills-subagents-hierarchy-tree.png)

You already have a team of AI specialists. Let's meet them.

---

## You Already Have a Team

Run this command in Claude Code right now:

```
/agents
```

**What you'll see**:

```
│ Agents                                                                               │
│ ❯ Create new agent                                                                   │
│                                                                                      │
│   Built-in agents (always available)                                                 │
│   Bash · inherit                                                                     │
│   general-purpose · sonnet                                                           │
│   statusline-setup · sonnet                                                          │
│   Explore · haiku                                                                    │
│   Plan · inherit                                                                     │
│   claude-code-guide · haiku                                                          │
```

These are **subagents**—specialized AI assistants that Claude Code can delegate work to. Each has its own expertise and isolated context window.

**You don't need to create anything yet.** You already have a team ready to work.

---

## Try It Now: Your First Subagent

Let's use the **Explore** subagent to see what's in your current folder.

**Type this in Claude Code**:

```
Use the Explore subagent to tell me what's in this folder and summarize the project structure.
```

**What happens**:

1. Claude Code delegates to the Explore subagent
2. Explore scans your directory with its own clean context
3. Explore returns a summary to main Claude Code
4. You see the results

**Try it!** This is hands-on learning—run it now and see what Explore finds.

---

## Meet the Built-In Agents

| Agent                 | Best For                                                        | Model            |
| --------------------- | --------------------------------------------------------------- | ---------------- |
| **Explore**           | Finding files, searching code, understanding codebase structure | Haiku (fast)     |
| **Plan**              | Complex multi-step tasks, creating implementation strategies    | Sonnet (smart)   |
| **general-purpose**   | Multi-step tasks requiring various tools                        | Sonnet           |
| **Bash**              | Command execution tasks                                         | Inherits current |
| **claude-code-guide** | Questions about Claude Code itself                              | Haiku            |

**Key insight**: Claude Code automatically picks the right specialist based on your request. But you can also explicitly invoke any agent.

---

## How Subagents Work?

**Critical concept**: A subagent is invoked **once** for a specific goal, completes its work, and **returns results to main Claude Code**.

**The flow**:

1. Main Claude Code recognizes a task that needs a specialist
2. Launches the subagent with a specific goal
3. Subagent works independently in isolated context
4. Subagent completes its task and returns results
5. **Control returns to main Claude Code**
6. You interact with main Claude Code to proceed

**Think of it like this**: You send a specialist to research something. They go off, do their work, come back with a report, and then you continue the conversation with your main assistant.

### Automatic Delegation

You don't command "use the Plan subagent." Claude Code decides when to delegate based on:

- Task complexity (multi-step tasks trigger Plan)
- Your request type (code review request might trigger a review subagent if you have one)
- Subagent descriptions (Claude matches task to specialist)

---

## Parallel Power: Multiple Agents at Once

Here's where it gets powerful. You can invoke **multiple subagents in a single prompt**.

**Try this**:

```
Use Explore to show me what files are in this project, AND use Plan to outline how I could add a README if one doesn't exist.
```

**What happens**:

- Claude Code launches **both** subagents
- They work in parallel with isolated contexts
- Results combine into a single response

**Real-world example**:

```
Use Explore to find all test files in this project, AND use Plan to suggest a testing strategy for the gaps you find.
```

This is **orchestration**—coordinating multiple specialists toward a goal.

---

## Why Subagents Work: Clean Context

Each subagent has its own **isolated context window**. Why does this matter?

**Without subagents** (one AI doing everything):

1. You ask Claude to research competitors
2. Context fills with research notes
3. You ask Claude to draft a pitch
4. Context is cluttered—Claude might confuse research notes with your pitch

**With subagents**:

1. Research subagent does research, returns clean summary
2. Main Claude receives summary, context stays clean
3. Planning subagent drafts pitch with fresh context
4. Each specialist focuses on one job

**Think of it like a team meeting**: The researcher presents findings, then leaves. The strategist creates a plan with fresh focus. Nobody is juggling everything at once.

#### 💬 AI Colearning Prompt

> "Explain why subagents use isolated context windows instead of sharing the main conversation. What problems does context isolation solve?"

---

## The Execution Model

**How subagents work**:

```
You → Main Claude Code → Launches Subagent → Subagent works → Returns results → Main Claude Code → You
```

**Key concepts**:

1. **One task, one completion**: Subagent is invoked for a specific goal, completes it, returns
2. **Control returns**: After the subagent finishes, you interact with main Claude Code again
3. **Automatic or explicit**: Claude Code can auto-delegate, or you can request a specific agent

**Automatic triggers**:

- Ask "What files handle authentication?" → Explore auto-activates
- Ask "Help me add user login to this app" → Plan auto-activates (complex task)

**Explicit invocation**:

```
Use the Plan subagent to analyze this feature request.
```

---

## Hands-On: Create Your First Custom Subagent

Now that you've used built-in agents, let's create your own specialist.

### Step 1: Open the Agent Menu

```
/agents
```

Select **"Create new agent"**

### Step 2: Choose Location

```
│ Choose location                                                               │
│ ❯ 1. Project (.claude/agents/)                                                │
│   2. Personal (~/.claude/agents/)                                             │
```

**Choose 1** (Project)—makes the agent available in this project only.

### Step 3: Choose Creation Method

```
│ Creation method                                                               │
│ ❯ 1. Generate with Claude (recommended)                                       │
│   2. Manual configuration                                                     │
```

**Choose 1**—let Claude generate the agent from your description.

### Step 4: Describe Your Agent

**Type something like**:

```
Help me review code for bugs and suggest improvements.
Use when I say "review this code" or "check for bugs."
```

Claude Code creates:

- Agent name (e.g., `code-reviewer`)
- Instructions based on your description
- Tool permissions
- Saves to `.claude/agents/code-reviewer.md`

### Step 5: Test It

```
Use the code-reviewer subagent to review this function: [paste your code]
```

**You just created a reusable specialist.**

---

## Where Subagents Live

**Project-level**: `.claude/agents/` (this project only)
**User-level**: `~/.claude/agents/` (all your projects)

**Example file** (`.claude/agents/code-reviewer.md`):

```markdown
---
name: code-reviewer
description: Reviews code for bugs and suggests improvements
model: sonnet
---

# Code Review Instructions

When reviewing code:

1. Check for bugs and edge cases
2. Suggest performance improvements
3. Note any security concerns
4. Recommend cleaner patterns
```

---

## More Subagent Ideas

Once you understand the pattern, create specialists for any repeated task:

- **Research subagent**: Deep-dive into documentation, gather requirements
- **Testing subagent**: Generate test cases, identify edge cases
- **Documentation subagent**: Write README files, API docs, architecture notes
- **Refactor subagent**: Suggest cleaner code patterns, reduce complexity

**The pattern**:

1. What expertise does this specialist have?
2. What should it do autonomously?
3. What format should results be in?

---

### What's Next

Subagents are one-shot workers that report back to the caller. But what happens when workers need to talk to _each other_? In Chapter 4, Lesson 9, you'll learn about **Agent Teams**—multiple Claude Code instances that communicate directly, share a task list, and self-coordinate. Same context isolation principles, but with inter-agent collaboration.

Lesson 12 introduces **MCP Integration**—connecting Claude to external systems like web browsers, databases, and documentation servers. Where subagents give you coordination between AI specialists, MCP gives you access to the outside world.

---

:::tip Ready to Practice?
Head to **Lesson 10: Agent Skills Exercises** for 27 hands-on exercises covering skill composition, real-world skill building, and capstone projects — with one-click exercise downloads and step-by-step guidance.
:::

---

## Try With AI

**🔍 Explore Your Codebase:**

> "Use the Explore subagent to find all configuration files in this project. Then explain what each one does."

**What you're learning:** How the Explore subagent does research autonomously—it reads files, follows imports, and reports findings without manual guidance.

**📋 Plan a Feature:**

> "Use the Plan subagent to create an implementation plan for adding dark mode to a React application. Include phases, dependencies, and testing strategy."

**What you're learning:** How Plan Mode creates comprehensive strategies before execution. This pattern—plan first, execute second—produces better outcomes than iterative guessing.

**⚡ Parallel Agents:**

> "Use Explore to find all API routes in this project, AND use Plan to suggest how to add authentication to routes that don't have it."

**What you're learning:** Parallel agent execution—running multiple specialists simultaneously. This pattern appears in production workflows where throughput matters.

**🛠️ Create a Custom Agent:**

> "Walk me through creating a custom subagent for [your repeated task: code reviews, blog planning, meeting notes, test design]. Help me think through: What should it do? What questions should it ask? What format should output be?"

**What you're learning:** The subagent design process—from identifying a need to defining behavior. Custom subagents are your first step toward building specialized AI teams.

**🎯 Orchestrate Multiple Agents:**

> "I need to understand this unfamiliar codebase. Use Explore to map the project structure, AND use Plan to create a learning path for understanding the architecture. Show me how the results combine."
