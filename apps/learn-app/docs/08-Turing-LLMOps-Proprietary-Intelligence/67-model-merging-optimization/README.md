---
sidebar_position: 67
title: "Chapter 67: Model Merging & Optimization"
description: "Build your merging skill first, then combine multiple LoRA adapters with MergeKit techniques"
---

# Chapter 67: Model Merging & Optimization

**You will build a model merging skill BEFORE you combine your adapters.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create a `model-merging` skill from MergeKit documentation. Then you learn to combine your persona adapter (Chapter 65) with your function-calling adapter (Chapter 66) into a single, unified model. By the end, you'll have a merged model that's both distinctive AND agentic.

## The Skill-First Arc

```
L00: Build Your Model Merging Skill (25 min)
  │   └── Clone skills-lab, fetch MergeKit docs, create skill
  │
  ├── L01-L04: Merging Fundamentals
  │   └── Theory, setup, strategies, RAM constraints
  │
  ├── L05: Reasoning Distillation (Theory)
  │   └── Understand when distillation adds value
  │
  └── L06: Capstone — Merge Task API Adapters
      └── Production merged model
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Explain adapter merging**: When to merge vs. retrain combined
- **Set up MergeKit**: Installation and YAML configuration
- **Apply merge strategies**: TIES, SLERP, DARE and when to use each
- **Handle RAM constraints**: Sharded merging on 12GB RAM
- **Evaluate merge quality**: Compare to individual adapters
- **Create reusable intelligence**: Build a `model-merging` skill

## Chapter Structure

| # | Lesson | Your Skill Improves |
|---|--------|---------------------|
| **0** | **Build Your Model Merging Skill** | **Created from MergeKit docs** |
| 1 | Adapter Merging Fundamentals | Test: explains merge vs retrain |
| 2 | MergeKit Setup and Configuration | Refine: correct YAML patterns |
| 3 | TIES, SLERP, and DARE Strategies | Add: strategy selection |
| 4 | Sharded Merging for RAM Constraints | Add: 12GB RAM patterns |
| 5 | Introduction to Reasoning Distillation | Understand when to distill |
| **6** | **Capstone — Merge Task API Adapters** | **Unified model** |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lesson 0 (L00)**: Skill-First—create skill before learning technology
- **Lessons 1-4 (Layer 1)**: Build mental models—understand merging
- **Lesson 5 (Layer 2)**: AI Collaboration—evaluate distillation need
- **Lesson 6 (Layer 4)**: Spec-driven capstone—produce merged model

## Merge Strategies

| Strategy | Best For | How It Works |
|----------|----------|--------------|
| TIES | Distinct capabilities | Trim, elect, sign & merge |
| SLERP | Similar adapters | Spherical linear interpolation |
| DARE | Complementary skills | Drop and rescale parameters |

## The RAM Challenge

Merging 7B models typically requires 32GB+ RAM. We solve this with **sharded merging**:

```yaml
# MergeKit config with sharded loading
merge_method: ties
slices:
  - sources:
      - model: ./task_api_persona_adapter
        layer_range: [0, 16]
      - model: ./task_api_agentic_adapter
        layer_range: [0, 16]
    ...
# Process 16 layers at a time instead of all 32
```

Result: Works on Colab's 12GB RAM.

## Running Example: Merge Task API Adapters

You'll combine:
1. **Persona adapter** (Chapter 65): TaskMaster encouraging personality
2. **Agentic adapter** (Chapter 66): Reliable tool-calling

Into a **unified model** that:
- Maintains TaskMaster voice
- Achieves 95%+ tool-calling accuracy
- Runs on consumer hardware

## Prerequisites

- **Chapter 65 completion**: TaskMaster persona adapter
- **Chapter 66 completion**: Agentic tool-calling adapter
- **MergeKit familiarity**: Will learn from scratch

## Looking Ahead

This chapter produces:
1. A **merged model** combining persona and agentic capabilities
2. A **model-merging skill** for future adapter combinations
3. **RAM-efficient patterns** for local development

Chapter 68 applies DPO alignment to ensure your merged model is safe and refuses harmful requests.

**Total Duration**: ~5.25 hours (315 minutes)
