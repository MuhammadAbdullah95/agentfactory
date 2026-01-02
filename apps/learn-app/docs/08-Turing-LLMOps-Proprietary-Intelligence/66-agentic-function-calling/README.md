---
sidebar_position: 66
title: "Chapter 66: Agentic & Function-Calling Fine-Tuning"
description: "Fine-tune for 95%+ JSON accuracy and reliable tool-calling to power agent workflows"
---

# Chapter 66: Agentic & Function-Calling Fine-Tuning

**Your model isn't an agent until it can reliably call tools.**

This chapter teaches structured output fine-tuning—the key to making custom models work as agent backends. You'll learn to design tool-calling datasets, train for 95%+ JSON accuracy, and integrate your model with OpenAI Agents SDK as a drop-in replacement for GPT-4.

## The Agentic Arc

```
L1-L2: Structured Output Fundamentals
  │   └── Why JSON matters, tool-calling patterns
  │
  ├── L3-L7: Hands-on Agentic Training
  │   └── Dataset, training, evaluation, SDK integration, errors
  │
  └── L8: Capstone — Task Agent Backend
      └── Production agent with custom model
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Explain structured output importance**: Why agents need reliable JSON
- **Design tool-calling datasets**: Function schemas, multi-turn conversations
- **Fine-tune for tool-calling**: Special token handling, structured training
- **Evaluate agentic models**: Tool accuracy, argument validation, end-to-end testing
- **Integrate with OpenAI SDK**: Custom model as drop-in replacement
- **Handle tool errors**: Graceful degradation and retry strategies

## Chapter Structure

| # | Lesson | Key Outcome |
|---|--------|-------------|
| 1 | Structured Output Fundamentals | Understand why JSON matters for agents |
| 2 | Tool-Calling Patterns | Design training data for tools |
| 3 | Tool-Calling Dataset Creation | Create synthetic tool-call data |
| 4 | Agentic Fine-Tuning | Train for reliable tool-calling |
| 5 | Agentic Evaluation | Measure 95%+ accuracy |
| 6 | OpenAI Agents SDK Integration | Connect custom model to SDK |
| 7 | Error Handling and Robustness | Graceful degradation patterns |
| **8** | **Capstone — Task Agent Backend** | **Production agent backend** |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lessons 1-2 (Layer 1)**: Build mental models—understand structured outputs
- **Lessons 3-7 (Layer 2)**: Hands-on with AI collaboration
- **Lesson 8 (Layer 4)**: Spec-driven capstone—produce deployable agent backend

## Why Structured Output Matters

```python
# Unstructured (unreliable for agents):
"I'll create a task called 'Review budget' for you."

# Structured (agent can parse):
{
    "action": "create_task",
    "parameters": {
        "title": "Review budget",
        "due_date": "2024-01-15",
        "priority": "high"
    }
}
```

Agents can't work with natural language descriptions—they need parseable tool calls.

## Task API Tools

```python
TASK_TOOLS = [
    {"name": "create_task", "description": "Create a new task", ...},
    {"name": "update_task", "description": "Update an existing task", ...},
    {"name": "complete_task", "description": "Mark task as completed", ...},
    {"name": "list_tasks", "description": "List all tasks", ...}
]
```

## OpenAI SDK Integration

```python
from openai import OpenAI
from agents import Agent, function_tool

# Point to local model via LiteLLM
client = OpenAI(
    base_url="http://localhost:11434/v1",  # Ollama
    api_key="ollama"
)

# Agent with custom model backend
agent = Agent(
    name="TaskAgent",
    model="llama-3-8b-task-api",  # Our fine-tuned model
    tools=[create_task, update_task, complete_task],
)
```

## Success Criteria

```markdown
# Capstone Spec: Task Agent Backend v1.0

## Intent
Fine-tune Llama-3-8B as drop-in replacement for GPT-4 in Task API agent workflows.

## Success Criteria
- Tool-calling accuracy > 95%
- Valid JSON output > 99%
- Latency < 500ms on consumer hardware
- Seamless integration with OpenAI Agents SDK
```

## The Business Case

| Metric | GPT-4 API | Custom Model |
|--------|-----------|--------------|
| Monthly cost | $10K+ (high volume) | $300 (self-hosted) |
| Latency | ~1s | <500ms |
| Control | Black box | Full ownership |
| Customization | Limited | Complete |

## Prerequisites

- **Chapter 65 completion**: You have a persona-tuned model
- **Chapter 63-64**: Training data and fine-tuning experience
- **Part 6**: Familiarity with OpenAI Agents SDK

## Looking Ahead

This chapter produces:
1. A **Task Agent Backend** with 95%+ tool-calling accuracy
2. **SDK integration patterns** for agent framework compatibility
3. **Error handling** for production resilience

Chapter 67 combines your persona and agentic adapters through model merging. Chapters 68-72 complete the LLMOps pipeline with alignment, evaluation, deployment, and capstone.

**Total Duration**: ~6 hours (360 minutes)
