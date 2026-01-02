---
sidebar_position: 70
title: "Chapter 70: Deployment & Serving"
description: "Build your serving skill first, then export to GGUF and deploy locally via Ollama"
---

# Chapter 70: Deployment & Serving

**You will build a model serving skill BEFORE you deploy your model.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create a `model-serving` skill from Ollama and GGUF documentation. Then you learn export formats, quantization for serving, Ollama setup, and performance optimization. By the end, your Task API model runs locally with <500ms latency.

## The Skill-First Arc

```
L00: Build Your Model Serving Skill (25 min)
  │   └── Clone skills-lab, fetch Ollama docs, create skill
  │
  ├── L01-L05: Deployment Fundamentals
  │   └── Formats, quantization, Ollama, local serving, vLLM theory
  │
  ├── L06: Performance Optimization
  │   └── Tune for latency and throughput
  │
  └── L07: Capstone — Deploy Task API Model
      └── Production-ready local serving
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Compare export formats**: Safetensors, GGUF, GGML
- **Apply serving quantization**: Q4_K_M vs. Q8_0 tradeoffs
- **Set up Ollama**: Installation and custom model loading
- **Serve models locally**: REST API with Python client
- **Understand vLLM**: Production serving architecture (theory)
- **Optimize performance**: Latency tuning for consumer hardware
- **Create reusable intelligence**: Build a `model-serving` skill

## Chapter Structure

| # | Lesson | Your Skill Improves |
|---|--------|---------------------|
| **0** | **Build Your Model Serving Skill** | **Created from Ollama docs** |
| 1 | Model Export Formats | Understand GGUF, safetensors |
| 2 | Quantization for Serving | Choose Q4 vs Q8 tradeoffs |
| 3 | Ollama Installation and Setup | Working local environment |
| 4 | Local Model Serving | REST API integration |
| 5 | vLLM Architecture (Theory) | Understand production serving |
| 6 | Performance Optimization | Tune for <500ms latency |
| **7** | **Capstone — Deploy Task API Model** | **Local production serving** |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lesson 0 (L00)**: Skill-First—create skill before learning technology
- **Lessons 1-5 (Layer 1)**: Build mental models—understand deployment
- **Lesson 6 (Layer 2)**: AI Collaboration—optimize with Three Roles
- **Lesson 7 (Layer 4)**: Spec-driven capstone—deploy production model

## Export Format Comparison

| Format | Size | Speed | Use Case |
|--------|------|-------|----------|
| Safetensors | Large | Fast load | Cloud deployment |
| GGUF Q4_K_M | ~4GB | Optimal | Local Ollama |
| GGUF Q8_0 | ~8GB | Slower | Higher quality |

## Ollama Integration

```python
# Modelfile for custom model
FROM ./task_api_model.gguf

TEMPLATE """{{ .System }}
User: {{ .Prompt }}
Assistant: """

SYSTEM "You are TaskMaster, a helpful task management assistant..."

# Register with Ollama
# $ ollama create task-api-model -f Modelfile
```

## Ollama REST API

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "task-api-model",
        "prompt": "Create a task for reviewing the budget",
        "stream": False
    }
)
print(response.json()["response"])
```

## Performance Targets

| Metric | Target | Consumer Hardware |
|--------|--------|-------------------|
| First token | <200ms | M1 Mac, RTX 3060+ |
| Total latency | <500ms | 8GB+ RAM |
| Throughput | 10+ req/s | Batch enabled |
| Memory | <8GB | Quantized GGUF |

## vLLM (Theory Only)

vLLM provides production-scale serving but requires dedicated GPU:
- PagedAttention for memory efficiency
- Continuous batching for throughput
- Out of scope for Colab Free Tier

We cover theory for awareness; Ollama handles local deployment.

## Prerequisites

- **Chapter 69 completion**: Evaluated model ready for deployment
- **8GB+ RAM**: For running quantized models locally
- **macOS/Linux/Windows**: Ollama supports all platforms

## Looking Ahead

This chapter produces:
1. A **locally deployed Task API model** via Ollama
2. A **model-serving skill** for future deployments
3. **Performance benchmarks** for latency verification

Chapter 71 integrates your deployed model with agent frameworks.

**Total Duration**: ~5.7 hours (340 minutes)
