---
title: "Compiling MCP to Skills"
sidebar_position: 9
chapter: 5
lesson: 9
duration_minutes: 25

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration) - applying skills + MCP knowledge from previous lessons"
layer_1_foundation: "Completed in Lessons 04-06 (Skills) and 08 (MCP)"
layer_2_collaboration: "Introspecting MCP servers with Claude, compiling to skills, validating token reduction"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "MCP-to-Skill Compilation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can identify MCP token bloat, introspect server definitions, and compile to skill + script format"

learning_objectives:
  - objective: "Identify when MCP servers cause token bloat"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Recognize high-token MCP patterns and articulate the problem"
  - objective: "Introspect an MCP server's tool definitions using Claude"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successfully extract tool definitions from a running MCP server"
  - objective: "Compile MCP definitions into skill + script format"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Create a working skill that replaces direct MCP tool calls"
  - objective: "Validate token reduction through before/after comparison"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Measure and report token savings"

# Cognitive load tracking
cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (MCP token bloat, introspection, code execution pattern, skill compilation, progressive disclosure optimization) - within B1-B2 limit"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Compile multiple MCP servers into a unified skill library; implement caching strategies"
  remedial_for_struggling: "Focus on single MCP server; use provided templates"

# Generation metadata
generated_by: "manual placeholder"
source_spec: "TBD - specs/XXX-lesson-09-compiling-mcp-to-skills/spec.md"
created: "2025-12-19"
last_modified: "2025-12-19"
git_author: "Claude Code"
workflow: "manual"
version: "0.1.0"

# Legacy compatibility
prerequisites:
  - "Lesson 05: The Concept Behind Skills"
  - "Lesson 06: Agent Skills (SKILL.md format)"
  - "Lesson 08: MCP Integration"
---

# Compiling MCP to Skills

:::caution PLACEHOLDER LESSON
This lesson is under development. The structure and learning objectives are defined, but content implementation is pending via `/sp.specify` workflow.
:::

## The Problem: MCP Token Bloat

> "The description is both too long to eagerly load it, and too short to really tell the agent how to use it."
> — Armin Ronacher, [Skills vs Dynamic MCP Loadouts](https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/)

MCP servers load ALL tool definitions at startup. A single server like Sentry can consume **8,000+ tokens** immediately—before you've even asked a question.

When you chain MCP operations, intermediate data flows through the context repeatedly. A 2-hour meeting transcript might consume **50,000 additional tokens** with each tool operation.

**The waste**: 80-98% of tokens consumed by MCP could be eliminated.

---

## The Solution: Code Execution + Skills

Instead of calling MCP tools directly, Claude can:

1. **Introspect** the MCP server to understand its tools
2. **Compile** tool definitions into a lean SKILL.md (~100 tokens)
3. **Generate** TypeScript/Python scripts that execute locally (0 tokens)
4. **Apply** progressive disclosure—load only what's needed, when needed

**The result**: From 150,000 tokens to 2,000 tokens—a **98.7% reduction**.

---

## Hands-On: Compile Your First MCP Server

*Content pending—will walk through:*

1. Identifying a high-token MCP server
2. Asking Claude to introspect its tool definitions
3. Generating SKILL.md + scripts
4. Testing the compiled skill
5. Measuring token savings

---

## When to Compile vs. Use Direct MCP

| Scenario | Recommendation |
|----------|----------------|
| One-off query to external service | Direct MCP |
| Repeated workflow with same tools | Compile to skill |
| High-token tool definitions | Compile to skill |
| Rapidly changing API | Direct MCP |
| Privacy-sensitive data processing | Compile (local execution) |

---

## Sources

- [Anthropic: Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- [Armin Ronacher: Skills vs Dynamic MCP Loadouts](https://lucumr.pocoo.org/2025/12/13/skills-vs-mcp/)
- [SmartScope: MCP Code Execution Deep Dive](https://smartscope.blog/en/blog/mcp-code-execution-agent-design/)

---

## Next Steps

After this lesson, you'll understand how Skills and MCP complement each other at a deeper level—Skills as the "expertise layer" that makes MCP's "connectivity layer" token-efficient.

Lesson 10 explores **Subagents and Orchestration**—how to compose multiple skills and tools into autonomous workflows.
