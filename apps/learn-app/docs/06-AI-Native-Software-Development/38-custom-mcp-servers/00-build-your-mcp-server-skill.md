---
sidebar_position: 0
title: "Build Your MCP Server Skill"
description: "Create your MCP server building skill FIRST, then learn to understand and improve it throughout the chapter"
chapter: 38
lesson: 0
duration_minutes: 25

skills:
  - name: "Skill-First Learning Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student applies skill-creator and fetching-library-docs to build an MCP server skill"

learning_objectives:
  - objective: "Build an MCP server skill using Chapter 5 tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student has a working mcp-server-builder skill in .claude/skills/"

cognitive_load:
  new_concepts: 2
  assessment: "Applies existing Ch5 knowledge to MCP server development"

differentiation:
  extension_for_advanced: "Add sampling and progress notification patterns to initial skill"
  remedial_for_struggling: "Follow exact prompts; customization comes later"
---

# Build Your MCP Server Skill

You learned MCP fundamentals in Chapter 37—architecture, primitives, and using existing servers. Now you'll BUILD servers. But you won't start with "how to write a server."

You'll start by **building a skill that knows MCP server development**.

In Chapter 5, you learned `skill-creator` and `fetching-library-docs`. Now you'll apply them to create an `mcp-server-builder` skill. The official MCP documentation will teach your skill. Then THIS chapter teaches YOU.

---

## Step 1: Clone the Skills Lab

```bash
git clone https://github.com/panaversity/claude-code-skills-lab.git ch38-mcp-server-skill
cd ch38-mcp-server-skill
claude
```

---

## Step 2: Write Your Learning Specification

Create `LEARNING-SPEC.md`:

```markdown
# Learning Specification: MCP Server Development

## What I'm Learning
Building custom MCP servers with advanced features.

## Why I'm Learning It
To create servers that:
- Expose my domain expertise as MCP tools
- Call LLMs through sampling
- Provide real-time progress notifications
- Deploy to production with StreamableHTTP

## My Current Level
- I understand MCP architecture (Chapter 37)
- I've used existing MCP servers
- I want to build my own

## What I Want My Skill to Do
Help me create MCP servers with:
- @mcp.tool, @mcp.resource, @mcp.prompt decorators
- Context object for logging and progress
- Sampling (server calling LLM through client)
- Progress and logging notifications
- Roots for file system permissions
- StreamableHTTP for production

## Success Criteria
By the end of Chapter 38, my skill can:
1. Generate a working MCP server with tools
2. Add sampling capabilities
3. Implement progress notifications
4. Configure for production deployment
```

---

## Step 3: Fetch Official Documentation

```
/fetching-library-docs mcp-python-sdk
```

This pulls official MCP Python SDK documentation via Context7.

---

## Step 4: Build Your Initial Skill

```
/skill-creator

Create an MCP server building skill based on the documentation I just fetched.

Name: mcp-server-builder
Purpose: Generate production MCP servers with advanced features

The skill should help with:
1. Server setup with FastMCP
2. Tool definitions (@mcp.tool decorator)
3. Resource definitions (@mcp.resource decorator)
4. Prompt templates (@mcp.prompt decorator)
5. Context object usage (logging, progress)
6. Sampling (server calling LLM)
7. StreamableHTTP configuration
8. Error handling patterns

Base everything on the official documentation patterns.
```

---

## Step 5: Verify Your Skill Works

```
Using my mcp-server-builder skill, generate a simple MCP server that:
1. Has one tool that processes text
2. Uses Context for logging
3. Can be tested with MCP Inspector
```

---

## Step 6: Understand What's Next

Your skill now contains official MCP server patterns. Each lesson tests your skill, identifies gaps, and improves it.

---

:::note Your Growing Toolkit
```
.claude/skills/
├── skill-creator/           # From Chapter 5
├── fetching-library-docs/   # From Chapter 5
├── openai-agents/           # From Chapter 34
├── google-adk/              # From Chapter 35
├── claude-agent-sdk/        # From Chapter 36
└── mcp-server-builder/      # NEW - this chapter
```

Each chapter adds to your Digital FTE toolkit.
:::

---

Start **Lesson 1** with your skill ready to test and improve.
