---
sidebar_position: 0
title: "Build Your Google ADK Skill"
description: "Create your Google Agent Development Kit skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 35
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build a Google ADK skill"

learning_objectives:
  - objective: "Build a Google ADK skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working google-adk skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to Google ADK domain"

differentiation:
  extension_for_advanced: "Add workflow agent patterns to initial skill"
  remedial_for_struggling: "Follow exact prompts; customization comes later"
---

# Build Your Google ADK Skill

You're about to learn Google's Agent Development Kit—building reliable agents with Gemini. But you won't start with ADK concepts.

You'll start by **building a skill that knows Google ADK**.

In Chapter 5, you learned `skill-creator` and `fetching-library-docs`. Now you'll apply them to create a `google-adk` skill. The official Google documentation will teach your skill. Then THIS chapter teaches YOU.

---

## Step 1: Clone the Skills Lab

```bash
git clone https://github.com/panaversity/claude-code-skills-lab.git ch35-google-adk-skill
cd ch35-google-adk-skill
claude
```

---

## Step 2: Write Your Learning Specification

Create `LEARNING-SPEC.md`:

```markdown
# Learning Specification: Google Agent Development Kit

## What I'm Learning
Google's ADK—building reliable agents powered by Gemini.

## Why I'm Learning It
To build agents that:
- Use Google's workflow patterns (Sequential, Parallel, Loop)
- Integrate with Vertex AI for production deployment
- Support multi-agent orchestration
- Connect to MCP servers

## My Current Level
- I understand agent concepts (Chapter 33)
- I've built with OpenAI Agents SDK (Chapter 34)
- I want to compare frameworks

## What I Want My Skill to Do
Help me create Google ADK agents with:
- Agent configuration with Gemini models
- Tool definitions
- Workflow agents (SequentialAgent, ParallelAgent, LoopAgent)
- Multi-agent patterns
- MCP integration

## Success Criteria
By the end of Chapter 35, my skill can:
1. Generate a working ADK agent with tools
2. Create workflow agents for complex tasks
3. Set up multi-agent orchestration
4. Connect agents to MCP servers
```

---

## Step 3: Fetch Official Documentation

```
/fetching-library-docs google-adk
```

This pulls official Google ADK documentation via Context7.

---

## Step 4: Build Your Initial Skill

```
/skill-creator

Create a Google ADK skill based on the documentation I just fetched.

Name: google-adk
Purpose: Generate reliable agents using Google's Agent Development Kit

The skill should help with:
1. Agent configuration (LlmAgent, model selection)
2. Tool definitions
3. Workflow agents (Sequential, Parallel, Loop)
4. Multi-agent orchestration
5. MCP server integration
6. Vertex AI deployment patterns

Base everything on the official documentation patterns.
```

---

## Step 5: Verify Your Skill Works

```
Using my google-adk skill, generate a simple LlmAgent that:
1. Uses Gemini as the model
2. Has one tool
3. Can be run with the ADK runner
```

---

## Step 6: Understand What's Next

Your skill now contains official Google ADK patterns. Each lesson tests your skill, identifies gaps, and improves it.

---

:::note Your Growing Toolkit
```
.claude/skills/
├── skill-creator/           # From Chapter 5
├── fetching-library-docs/   # From Chapter 5
├── openai-agents/           # From Chapter 34
└── google-adk/              # NEW - this chapter
```

Each chapter adds to your Digital FTE toolkit.
:::

---

Start **Lesson 1** with your skill ready to test and improve.
