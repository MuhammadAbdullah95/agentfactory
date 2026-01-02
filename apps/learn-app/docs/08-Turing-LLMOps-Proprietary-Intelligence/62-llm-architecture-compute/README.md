---
sidebar_position: 62
title: "Chapter 62: LLM Architecture & Compute Reality"
description: "Master transformer internals, VRAM budgeting, and quantization techniques for fine-tuning on consumer hardware"
---

# Chapter 62: LLM Architecture & Compute Reality

**You can't fine-tune what you don't understand—and you can't run what doesn't fit in memory.**

This chapter bridges the gap between LLMOps strategy (Chapter 61) and hands-on training (Chapters 63+). You'll learn enough transformer architecture to make informed decisions, master VRAM budgeting to avoid out-of-memory crashes, and understand quantization as the key to running 8B models on free GPUs.

## The Technical Foundation Arc

```
L1-L3: Architecture Mental Models
  │   └── Transformers, tokenization, parameter counting
  │
  ├── L4-L6: Memory Mastery
  │   └── VRAM budgeting, quantization, optimization
  │
  ├── L7: Hands-on Lab
  │   └── Run inference on Colab T4
  │
  └── L8: Intelligence Design
      └── Create your llmops-compute-planner skill
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Explain transformer architecture**: Attention, layers, and parameters relevant to fine-tuning
- **Calculate VRAM requirements**: Know if your model will fit before you try to load it
- **Apply quantization**: Reduce 16GB models to 5GB using BitsAndBytes NF4
- **Optimize memory**: Gradient checkpointing, batch size tuning, mixed precision
- **Run inference on T4**: Practical lab with Colab Free Tier GPU
- **Create reusable intelligence**: Build an `llmops-compute-planner` skill

## Chapter Structure

| # | Lesson | Key Outcome |
|---|--------|-------------|
| 1 | Transformer Architecture Essentials | Understand attention, FFN, and what we modify |
| 2 | Tokenization and Context | How tokenization affects training data |
| 3 | Parameter Counting and Model Sizes | Calculate parameters, compare model tiers |
| 4 | VRAM Budget Planning | Calculate memory requirements before training |
| 5 | Quantization Deep Dive | Apply 4-bit quantization with BitsAndBytes |
| 6 | Memory Optimization Techniques | Gradient checkpointing, batch tuning |
| 7 | Lab — Inference on T4 | Run quantized Llama-3-8B on Colab |
| **8** | **Build Your Compute Planning Skill** | **Create reusable compute planner** |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lessons 1-3 (Layer 1)**: Build mental models manually—understand architecture before calculating
- **Lessons 4-6 (Layer 2)**: Hands-on with AI collaboration—VRAM planning with Three Roles
- **Lesson 7 (Layer 2)**: Practical lab—run inference on real hardware
- **Lesson 8 (Layer 3)**: Create reusable intelligence for future compute decisions

## The Colab Free Tier Constraint

**All Part 8 content works on Google Colab Free Tier:**

| Resource | Limit | Our Solution |
|----------|-------|--------------|
| GPU | NVIDIA T4 (15GB VRAM) | 4-bit quantization |
| RAM | 12GB | Sharded loading |
| Session | ~90 min timeout | Checkpointing |

This chapter teaches you to work within these constraints—the same techniques used in production to minimize costs.

## Running Example: Task API Inference

You'll load and run inference with Llama-3-8B-Instruct using Task API prompts:

```python
prompt = """You are a helpful task assistant.

User: Create a task for reviewing the Q4 budget spreadsheet by Friday.
Assistant:"""
```

This sets up the model you'll fine-tune in Chapter 64.

## Key Technical Concepts

### Model Size Reference

| Model | Parameters | VRAM (FP16) | VRAM (4-bit) | Fits T4? |
|-------|-----------|-------------|--------------|----------|
| Llama-3-8B | 8B | 16GB | 5GB | ✅ Training |
| Mistral-7B | 7B | 14GB | 4.5GB | ✅ Training |
| Llama-3-70B | 70B | 140GB | 40GB | ❌ |

### VRAM Formula (QLoRA)

```
Training VRAM ≈ Base Model (quantized) + LoRA Adapters + Gradients + Activations
             ≈ 5GB + 0.1GB + 0.3GB + 4GB = ~9.4GB (fits T4!)
```

## Prerequisites

- **Chapter 61 completion**: You understand when to fine-tune
- **Basic Python**: Comfortable with code examples
- **No ML/GPU experience required**: We explain everything

## Looking Ahead

This chapter produces:
1. **Practical understanding** of why fine-tuning works on consumer hardware
2. A **working Colab notebook** with quantized inference
3. An **llmops-compute-planner skill** for sizing future training jobs

Chapter 63 applies this knowledge to create training datasets—the fuel for fine-tuning.

**Total Duration**: ~6 hours (360 minutes)
