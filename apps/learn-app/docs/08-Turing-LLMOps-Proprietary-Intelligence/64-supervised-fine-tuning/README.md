---
sidebar_position: 64
title: "Chapter 64: Supervised Fine-Tuning (SFT)"
description: "Build your fine-tuning skill first, then master LoRA/QLoRA training with Unsloth on Colab T4"
---

# Chapter 64: Supervised Fine-Tuning (SFT)

**You will build a fine-tuning skill BEFORE you train your first model.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create an `llmops-fine-tuner` skill from Unsloth documentation. Then you spend the chapter understanding LoRA theory, hyperparameters, and training workflows—testing and improving your skill at each step. By the end, you'll have a fine-tuned Task API Assistant running locally.

## The Skill-First Arc

```
L00: Build Your Fine-Tuning Skill (30 min)
  │   └── Clone skills-lab, fetch Unsloth docs, create skill
  │
  ├── L01-02: LoRA Theory & Hyperparameters
  │   └── Understand why LoRA works, configure training
  │
  ├── L03-07: Training Workflow
  │   └── Setup, training loop, monitoring, tuning, export
  │
  └── L08: Capstone — Task API Assistant
      └── Fine-tune complete Digital FTE
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Explain LoRA theory**: Low-rank adaptation and why it reduces 99% of trainable parameters
- **Configure hyperparameters**: Learning rate, epochs, batch size, rank, alpha
- **Set up Unsloth**: Fast installation and model loading on Colab T4
- **Run training loops**: SFTTrainer with proper monitoring
- **Debug training issues**: Interpret loss curves, detect overfitting
- **Export models**: Adapter-only, merged, and GGUF for Ollama
- **Create reusable intelligence**: Build an `llmops-fine-tuner` skill

## Chapter Structure

| # | Lesson | Your Skill Improves |
|---|--------|---------------------|
| **0** | **Build Your Fine-Tuning Skill** | **Created from Unsloth docs** |
| 1 | LoRA Theory | Test: explains low-rank decomposition |
| 2 | Hyperparameters Explained | Add: parameter selection framework |
| 3 | Unsloth Setup | Refine: correct installation pattern |
| 4 | Training Loop | Add: SFTTrainer workflow |
| 5 | Monitoring and Debugging | Add: loss curve interpretation |
| 6 | Hyperparameter Tuning | Add: systematic tuning approach |
| 7 | Checkpointing and Resume | Add: Colab-safe patterns |
| 8 | Model Export | Add: GGUF export for Ollama |
| **9** | **Capstone — Task API Assistant** | **Production Digital FTE** |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lesson 0 (L00)**: Skill-First—create your skill before learning the technology
- **Lessons 1-2 (Layer 1)**: Build mental models—understand LoRA and hyperparameters
- **Lessons 3-8 (Layer 2)**: Hands-on training with AI collaboration
- **Lesson 9 (Layer 4)**: Spec-driven capstone—produce deployable Digital FTE

## The LoRA Insight

```
Original weight matrix W: (4096 × 4096) = 16M parameters
LoRA adapters: A (4096 × 16) + B (16 × 4096) = 131K parameters

We train the small adapters, keep base weights frozen.
Result: 99.2% parameter reduction, ~95% quality retention
```

This is why we can fine-tune 8B models on free GPUs.

## Training Configuration

```python
# Optimal starting point for Task API
training_args = TrainingArguments(
    learning_rate=2e-4,              # Higher for LoRA
    num_train_epochs=3,              # Start small
    per_device_train_batch_size=4,   # Limited by VRAM
    gradient_accumulation_steps=4,   # Effective batch = 16
    warmup_ratio=0.03,               # 3% warmup
    weight_decay=0.01,               # Light regularization
    fp16=True,                       # Mixed precision
)
```

## Running Example: Task API Assistant

Using the dataset from Chapter 63, you'll fine-tune a model that:

- Understands task management domain
- Follows consistent response format
- Handles create/update/complete/delete operations

```markdown
# Capstone Spec: Task API Assistant v1.0

## Success Criteria
- Val loss < 1.0
- Task creation accuracy > 90% on test set
- Response latency < 500ms on Ollama
```

## Model Export Options

| Method | Size | Use Case |
|--------|------|----------|
| Adapter only | ~30MB | When base model available |
| Merged | ~16GB (FP16) | Cloud deployment |
| GGUF q4 | ~4GB | Local Ollama |

## Prerequisites

- **Chapter 63 completion**: You have a 500-row training dataset
- **Google Colab account**: Free tier T4 GPU access
- **No ML experience required**: We explain everything

## Looking Ahead

This chapter produces:
1. A **fine-tuned Task API Assistant** exported to GGUF
2. An **llmops-fine-tuner skill** encoding training patterns
3. **Hands-on training experience** with Unsloth and LoRA

Chapter 65 adds persona characteristics to make your model distinctive. Chapter 66 adds tool-calling for agentic integration.

**Total Duration**: ~7 hours (420 minutes)
