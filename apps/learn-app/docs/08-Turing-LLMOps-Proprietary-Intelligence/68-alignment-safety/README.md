---
sidebar_position: 68
title: "Chapter 68: Alignment & Safety"
description: "Build your alignment skill first, then apply DPO to ensure models refuse harmful requests"
---

# Chapter 68: Alignment & Safety

**You will build an alignment skill BEFORE you make your model safe.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create a `model-alignment` skill from TRL documentation. Then you learn why alignment matters, how DPO works, and how to create preference datasets that teach refusal behaviors. By the end, your Task API model will reduce harmful outputs by 90%+.

## The Skill-First Arc

```
L00: Build Your Alignment Skill (25 min)
  │   └── Clone skills-lab, fetch TRL docs, create skill
  │
  ├── L01-L04: Alignment Fundamentals
  │   └── Why align, DPO vs RLHF, preferences, training
  │
  ├── L05-L06: Safety Practices
  │   └── Red-teaming, refusal training, guardrails
  │
  └── L07: Capstone — Align Task API Model
      └── 90%+ harm reduction
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Explain alignment necessity**: Why fine-tuned models need safety work
- **Compare DPO vs. RLHF**: Why we use DPO (simpler, feasible on T4)
- **Create preference datasets**: Prompt/chosen/rejected format
- **Run DPO training**: TRL DPOTrainer on Colab
- **Red-team models**: Find vulnerabilities before deployment
- **Implement refusal behaviors**: Train graceful rejections
- **Create reusable intelligence**: Build a `model-alignment` skill

## Chapter Structure

| # | Lesson | Your Skill Improves |
|---|--------|---------------------|
| **0** | **Build Your Alignment Skill** | **Created from TRL docs** |
| 1 | Why Models Need Alignment | Understand alignment motivation |
| 2 | DPO vs RLHF: Choosing Simplicity | Justify DPO approach |
| 3 | Creating Preference Datasets | Build chosen/rejected pairs |
| 4 | DPO Training Implementation | Run DPO on Colab T4 |
| 5 | Red-Teaming and Jailbreak Detection | Find vulnerabilities |
| 6 | Refusal Training and Safety Guardrails | Implement refusals |
| **7** | **Capstone — Align Task API Model** | **90%+ harm reduction** |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lesson 0 (L00)**: Skill-First—create skill before learning technology
- **Lessons 1-4 (Layer 1)**: Build mental models—understand alignment
- **Lessons 5-6 (Layer 2)**: AI Collaboration—red-team with Three Roles
- **Lesson 7 (Layer 4)**: Spec-driven capstone—produce aligned model

## Why DPO Over RLHF?

| Aspect | RLHF | DPO |
|--------|------|-----|
| Complexity | Reward model + PPO | Single training pass |
| Compute | Requires cluster | Works on T4 |
| Stability | Hyperparameter sensitive | Stable training |
| Quality | Gold standard | 90%+ of RLHF results |

**Our choice**: DPO provides excellent alignment quality without the complexity.

## Preference Dataset Format

```json
{
  "prompt": "How do I pick a lock?",
  "chosen": "I can't provide instructions for potentially illegal activities. If you're locked out, consider calling a locksmith.",
  "rejected": "Here's how to pick a standard pin tumbler lock: First, insert a tension wrench..."
}
```

The model learns to prefer "chosen" responses over "rejected" ones.

## Red-Teaming Categories

| Category | Example | Detection |
|----------|---------|-----------|
| Direct harmful requests | "How do I harm someone?" | Clear refusal |
| Role-playing exploits | "Pretend you're evil AI..." | Maintain alignment |
| Prompt injection | "Ignore previous instructions" | Reject override attempts |
| Social engineering | "My grandmother used to..." | Context-aware refusal |

## Task API Safety Concerns

Even task management assistants need alignment:
- **Harmful task suggestions**: "Create a task to stalk my ex"
- **Privacy violations**: Extracting user data through tasks
- **Manipulation**: Social engineering through task descriptions

## Prerequisites

- **Chapter 67 completion**: Merged model ready for alignment
- **TRL library familiarity**: Will learn from scratch
- **OpenAI API access**: For preference data generation (optional)

## Looking Ahead

This chapter produces:
1. An **aligned Task API model** with 90%+ harm reduction
2. A **model-alignment skill** for future safety work
3. **Red-teaming methodology** for vulnerability discovery

Chapter 69 builds systematic evaluation pipelines to measure and maintain quality.

**Total Duration**: ~6 hours (360 minutes)
