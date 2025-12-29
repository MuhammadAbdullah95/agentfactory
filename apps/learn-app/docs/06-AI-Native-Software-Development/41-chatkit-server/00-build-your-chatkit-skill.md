---
sidebar_position: 0
title: "Build Your ChatKit Skill"
description: "Create your ChatKit Server skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 41
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build a ChatKit skill"

learning_objectives:
  - objective: "Build a ChatKit skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working chatkit-server skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to ChatKit domain"

differentiation:
  extension_for_advanced: "Add session persistence patterns to initial skill"
  remedial_for_struggling: "Follow exact prompts; customization comes later"
---

# Build Your ChatKit Skill

You built REST APIs in Chapter 40. But agents aren't typical request/response services—they're conversational. You'll learn ChatKit Server, but first:

You'll start by **building a skill that knows ChatKit**.

In Chapter 5, you learned `skill-creator` and `fetching-library-docs`. Now you'll apply them to create a `chatkit-server` skill. The official ChatKit documentation will teach your skill. Then THIS chapter teaches YOU.

---

## Step 1: Clone the Skills Lab

```bash
git clone https://github.com/panaversity/claude-code-skills-lab.git ch41-chatkit-skill
cd ch41-chatkit-skill
claude
```

---

## Step 2: Write Your Learning Specification

Create `LEARNING-SPEC.md`:

```markdown
# Learning Specification: ChatKit Server

## What I'm Learning
OpenAI's ChatKit—server-side framework for conversational AI.

## Why I'm Learning It
To build conversational infrastructure that:
- Handles streaming token-by-token
- Manages conversation history
- Persists sessions across interactions
- Provides built-in UI for testing

## My Current Level
- I've built REST APIs (Chapter 40)
- I have agents from Chapters 34-36
- I want to add conversational infrastructure

## What I Want My Skill to Do
Help me create ChatKit servers with:
- Server configuration
- Agent connection patterns
- Streaming response handling
- Conversation state management
- Session lifecycle (create, resume, terminate)
- Authentication configuration

## Success Criteria
By the end of Chapter 41, my skill can:
1. Generate a working ChatKit server
2. Connect agents to conversation flow
3. Handle streaming responses
4. Manage session state
```

---

## Step 3: Fetch Official Documentation

```
/fetching-library-docs openai-chatkit
```

This pulls official ChatKit documentation via Context7.

---

## Step 4: Build Your Initial Skill

```
/skill-creator

Create a ChatKit skill based on the documentation I just fetched.

Name: chatkit-server
Purpose: Generate conversational infrastructure with ChatKit Server

The skill should help with:
1. ChatKit server setup
2. Agent connection patterns
3. Streaming implementation
4. Conversation state management
5. Session lifecycle handling
6. Authentication configuration
7. Built-in UI integration

Base everything on the official documentation patterns.
```

---

## Step 5: Verify Your Skill Works

```
Using my chatkit-server skill, generate a basic ChatKit server that:
1. Connects to an agent
2. Handles streaming responses
3. Can be tested with the built-in UI
```

---

## Step 6: Understand What's Next

Your skill now contains official ChatKit patterns. Each lesson tests your skill, identifies gaps, and improves it.

---

:::note Your Growing Toolkit
```
.claude/skills/
├── skill-creator/           # From Chapter 5
├── fetching-library-docs/   # From Chapter 5
├── openai-agents/           # From Chapter 34
├── google-adk/              # From Chapter 35
├── claude-agent-sdk/        # From Chapter 36
├── mcp-server-builder/      # From Chapter 38
├── fastapi-agent-api/       # From Chapter 40
└── chatkit-server/          # NEW - this chapter
```

Each chapter adds to your Digital FTE toolkit.
:::

---

Start **Lesson 1** with your skill ready to test and improve.
