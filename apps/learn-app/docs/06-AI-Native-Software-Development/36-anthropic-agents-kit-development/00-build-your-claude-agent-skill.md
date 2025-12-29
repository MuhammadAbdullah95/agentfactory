---
sidebar_position: 0
title: "Build Your Claude Agent SDK Skill"
description: "Create your Claude Agent SDK skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 36
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build a Claude Agent SDK skill"

learning_objectives:
  - objective: "Build a Claude Agent SDK skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working claude-agent-sdk skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to Claude Agent SDK domain"

differentiation:
  extension_for_advanced: "Add computer use patterns to initial skill"
  remedial_for_struggling: "Follow exact prompts; customization comes later"
---

# Build Your Claude Agent SDK Skill

You're about to learn Anthropic's Claude Agent SDK—the architecture behind Claude Code itself. But you won't start with SDK concepts.

You'll start by **building a skill that knows Claude Agent SDK**.

In Chapter 5, you learned `skill-creator` and `fetching-library-docs`. Now you'll apply them to create a `claude-agent-sdk` skill. The official Anthropic documentation will teach your skill. Then THIS chapter teaches YOU.

---

## Step 1: Clone the Skills Lab

```bash
git clone https://github.com/panaversity/claude-code-skills-lab.git ch36-claude-agent-skill
cd ch36-claude-agent-skill
claude
```

---

## Step 2: Write Your Learning Specification

Create `LEARNING-SPEC.md`:

```markdown
# Learning Specification: Claude Agent SDK

## What I'm Learning
Anthropic's Claude Agent SDK—the same architecture powering Claude Code.

## Why I'm Learning It
To build agents that:
- Use tools with Claude's schema format
- Leverage extended thinking for complex reasoning
- Support computer use (GUI automation)
- Understand Claude Code's internal architecture

## My Current Level
- I understand agent concepts (Chapter 33)
- I've built with OpenAI (Ch34) and Google (Ch35) SDKs
- I use Claude Code daily—now I'll understand how it works

## What I Want My Skill to Do
Help me create Claude agents with:
- Tool definitions (Anthropic schema format)
- Extended thinking configuration
- Computer use patterns
- Subagent orchestration
- Skills and MCP integration

## Success Criteria
By the end of Chapter 36, my skill can:
1. Generate a working Claude agent with tools
2. Configure extended thinking
3. Set up computer use capabilities
4. Create multi-agent systems with subagents
```

---

## Step 3: Fetch Official Documentation

```
/fetching-library-docs claude-agent-sdk
```

This pulls official Claude Agent SDK documentation via Context7.

---

## Step 4: Build Your Initial Skill

```
/skill-creator

Create a Claude Agent SDK skill based on the documentation I just fetched.

Name: claude-agent-sdk
Purpose: Generate agents using Anthropic's Claude Agent SDK

The skill should help with:
1. Agent configuration and model selection
2. Tool definitions (Anthropic schema format)
3. Extended thinking for complex reasoning
4. Computer use (screen reading, mouse/keyboard)
5. Subagent orchestration
6. Skills and MCP integration patterns

Base everything on the official documentation patterns.
```

---

## Step 5: Verify Your Skill Works

```
Using my claude-agent-sdk skill, generate a simple Claude agent that:
1. Has a system prompt
2. Has one tool with proper Anthropic schema
3. Demonstrates the tool-use conversation loop
```

---

## Step 6: Understand What's Next

Your skill now contains official Claude Agent SDK patterns. Each lesson tests your skill, identifies gaps, and improves it.

This chapter is special—you'll understand how Claude Code itself works. The tool you've been using throughout this book becomes transparent.

---

:::note Your Growing Toolkit
```
.claude/skills/
├── skill-creator/           # From Chapter 5
├── fetching-library-docs/   # From Chapter 5
├── openai-agents/           # From Chapter 34
├── google-adk/              # From Chapter 35
└── claude-agent-sdk/        # NEW - this chapter
```

Each chapter adds to your Digital FTE toolkit.
:::

---

Start **Lesson 1** with your skill ready to test and improve.
