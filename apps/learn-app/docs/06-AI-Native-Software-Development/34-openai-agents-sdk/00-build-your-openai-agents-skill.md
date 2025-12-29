---
sidebar_position: 0
title: "Build Your OpenAI Agents Skill"
description: "Create your OpenAI Agents SDK skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 34
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build an OpenAI Agents skill"

learning_objectives:
  - objective: "Build an OpenAI Agents skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working openai-agents skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to OpenAI Agents domain"

differentiation:
  extension_for_advanced: "Add multi-agent handoff patterns to initial skill"
  remedial_for_struggling: "Follow exact prompts; customization comes later"
---

# Build Your OpenAI Agents Skill

You're about to learn OpenAI's Agents SDK—building production agents with tools, handoffs, and guardrails. But you won't start with "what is an agent?"

You'll start by **building a skill that knows OpenAI Agents**.

In Chapter 5, you learned `skill-creator` and `fetching-library-docs`. Now you'll apply them to create an `openai-agents` skill. The official OpenAI documentation will teach your skill. Then THIS chapter teaches YOU.

---

## Step 1: Clone the Skills Lab

```bash
git clone https://github.com/panaversity/claude-code-skills-lab.git ch34-openai-agents-skill
cd ch34-openai-agents-skill
claude
```

---

## Step 2: Write Your Learning Specification

Create `LEARNING-SPEC.md`:

```markdown
# Learning Specification: OpenAI Agents SDK

## What I'm Learning
OpenAI's Agents SDK—the framework powering ChatGPT's agentic capabilities.

## Why I'm Learning It
To build production agents that:
- Use tools to interact with external systems
- Hand off between specialized agents
- Include guardrails for safety
- Stream responses in real-time

## My Current Level
- I understand agent concepts (Chapter 33)
- I know Python (Part 5)
- I haven't built agents with SDKs before

## What I Want My Skill to Do
Help me create OpenAI agents with:
- Agent configuration (instructions, model, tools)
- Tool definitions using function_tool
- Multi-agent handoffs
- Guardrails and input validation
- Async execution with Runner

## Success Criteria
By the end of Chapter 34, my skill can:
1. Generate a working single-agent with tools
2. Set up multi-agent handoffs
3. Add input/output guardrails
4. Handle streaming responses
```

---

## Step 3: Fetch Official Documentation

```
/fetching-library-docs openai-agents-sdk
```

This pulls official OpenAI Agents SDK documentation via Context7.

---

## Step 4: Build Your Initial Skill

```
/skill-creator

Create an OpenAI Agents skill based on the documentation I just fetched.

Name: openai-agents
Purpose: Generate production agents using OpenAI's Agents SDK

The skill should help with:
1. Agent configuration (Agent class, instructions, model)
2. Tool definitions using @function_tool decorator
3. Multi-agent handoffs (handoff_to_agent)
4. Guardrails (input_guardrail, output_guardrail)
5. Runner patterns (Runner.run, streaming)
6. Tracing and debugging

Base everything on the official documentation patterns.
```

---

## Step 5: Verify Your Skill Works

```
Using my openai-agents skill, generate a simple agent that:
1. Has a system instruction
2. Has one tool that returns the current time
3. Can be run with Runner.run()
```

---

## Step 6: Understand What's Next

Your skill now contains official OpenAI Agents patterns. Each lesson tests your skill, identifies gaps, and improves it.

| Lesson | Your Skill Learns |
|--------|-------------------|
| 1 | SDK setup validated |
| 2 | Tool patterns refined |
| 3-4 | Multi-agent handoffs |
| 5 | Guardrails and safety |
| 6 | Streaming patterns |
| 7 | Tracing and debugging |
| 8 | Full agent capstone |

---

:::note Your Growing Toolkit
```
.claude/skills/
├── skill-creator/           # From Chapter 5
├── fetching-library-docs/   # From Chapter 5
└── openai-agents/           # NEW - this chapter
```

Each chapter adds to your Digital FTE toolkit.
:::

---

Start **Lesson 1** with your skill ready to test and improve.
