---
sidebar_position: 71
title: "Chapter 71: Agent Framework Integration"
description: "Build your integration skill first, then connect custom models to OpenAI SDK, LiteLLM, and MCP"
---

# Chapter 71: Agent Framework Integration

**You will build an agent integration skill BEFORE you connect your model to frameworks.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create an `agent-integration` skill from OpenAI SDK and LiteLLM documentation. Then you learn to use your custom model as an agent backend—a drop-in replacement for GPT-4 in agentic workflows. By the end, your Task API model powers a fully functional agent.

## The Skill-First Arc

```
L00: Build Your Agent Integration Skill (25 min)
  │   └── Clone skills-lab, fetch SDK docs, create skill
  │
  ├── L01-L03: Integration Fundamentals
  │   └── Custom backends, LiteLLM proxy, SDK integration
  │
  ├── L04-L06: Production Patterns
  │   └── Tool-calling, MCP servers, error handling
  │
  └── L07: Capstone — Task API Agent
      └── Complete agent with custom backend
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Explain agent backend patterns**: How custom models fit agent architectures
- **Deploy LiteLLM proxy**: Unified OpenAI-compatible API
- **Integrate with OpenAI SDK**: Custom base_url configuration
- **Achieve 95%+ tool accuracy**: Reliable structured outputs
- **Build MCP servers**: Custom model as reasoning engine
- **Handle errors gracefully**: Fallback to foundation models
- **Create reusable intelligence**: Build an `agent-integration` skill

## Chapter Structure

| # | Lesson | Your Skill Improves |
|---|--------|---------------------|
| **0** | **Build Your Agent Integration Skill** | **Created from SDK docs** |
| 1 | Custom Models as Agent Backends | Understand integration patterns |
| 2 | LiteLLM Proxy for SDK Compatibility | Unified API interface |
| 3 | OpenAI SDK with Custom Backend | Working SDK integration |
| 4 | Tool-Calling with Custom Models | Achieve 95%+ JSON accuracy |
| 5 | MCP Server with Custom Backend | MCP-compatible endpoint |
| 6 | Error Handling and Fallbacks | Production resilience |
| **7** | **Capstone — Task API Agent** | **Complete agent integration** |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lesson 0 (L00)**: Skill-First—create skill before learning technology
- **Lessons 1-3 (Layer 1)**: Build mental models—understand integration
- **Lessons 4-6 (Layer 2)**: AI Collaboration—optimize with Three Roles
- **Lesson 7 (Layer 4)**: Spec-driven capstone—deploy complete agent

## LiteLLM Proxy

LiteLLM provides OpenAI-compatible API for any model backend:

```python
# config.yaml
model_list:
  - model_name: task-api-model
    litellm_params:
      model: ollama/task-api-model
      api_base: http://localhost:11434

# Run proxy
# $ litellm --config config.yaml
```

## OpenAI SDK Integration

```python
from openai import OpenAI
from agents import Agent, function_tool

# Point SDK to LiteLLM proxy
client = OpenAI(
    base_url="http://localhost:4000/v1",  # LiteLLM
    api_key="sk-local"
)

@function_tool
def create_task(title: str, priority: str = "medium"):
    """Create a new task."""
    return {"task_id": 123, "status": "created"}

# Agent with custom model backend
agent = Agent(
    name="TaskAgent",
    model="task-api-model",
    tools=[create_task, update_task, complete_task],
)
```

## Error Handling Pattern

```python
def call_with_fallback(prompt: str, tools: list):
    """Try custom model, fallback to GPT-4 on failure."""
    try:
        response = custom_client.chat.completions.create(
            model="task-api-model",
            messages=[{"role": "user", "content": prompt}],
            tools=tools,
            timeout=5.0
        )
        if validate_tool_call(response):
            return response
    except (Timeout, JSONDecodeError):
        pass

    # Fallback to foundation model
    return openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        tools=tools
    )
```

## MCP Server with Custom Backend

```python
from fastmcp import FastMCP

mcp = FastMCP("Task API Agent")

@mcp.tool
def create_task(title: str, priority: str = "medium"):
    """Create a new task using Task API model."""
    # Use custom model for reasoning
    response = generate_with_custom_model(
        f"Create task: {title}, priority: {priority}"
    )
    return parse_task_response(response)
```

## Prerequisites

- **Chapter 70 completion**: Model deployed via Ollama
- **Part 6 completion**: Familiarity with agent frameworks
- **OpenAI SDK**: For fallback integration

## Looking Ahead

This chapter produces:
1. A **fully integrated Task API Agent** with custom backend
2. An **agent-integration skill** for future framework connections
3. **Production patterns** for error handling and fallbacks

Chapter 72 is the capstone: build a complete LLMOps pipeline from data to deployment, producing a Digital FTE ready for monetization.

**Total Duration**: ~6 hours (365 minutes)
