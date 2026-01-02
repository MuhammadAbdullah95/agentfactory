---
sidebar_position: 69
title: "Chapter 69: Evaluation & Quality Gates"
description: "Build your evaluation skill first, then implement LLM-as-Judge, benchmarks, and automated quality gates"
---

# Chapter 69: Evaluation & Quality Gates

**You will build an evaluation skill BEFORE you measure your model's quality.**

This chapter follows the **Skill-First Learning Pattern**: In Lesson 0, you create a `model-evaluation` skill from TRL and evaluation documentation. Then you learn to design evaluation strategies, implement LLM-as-Judge, create custom benchmarks, and build automated quality gates. By the end, no bad model will ship without being caught.

## The Skill-First Arc

```
L00: Build Your Evaluation Skill (25 min)
  │   └── Clone skills-lab, fetch docs, create skill
  │
  ├── L01-L03: Evaluation Fundamentals
  │   └── Taxonomy, LLM-as-Judge, custom benchmarks
  │
  ├── L04-L05: Quality Infrastructure
  │   └── Regression testing, quality gates
  │
  └── L06: Capstone — Evaluation Pipeline
      └── Automated quality system
```

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Design evaluation strategy**: Task, safety, and quality metrics
- **Implement LLM-as-Judge**: GPT-4o-mini as cost-effective evaluator
- **Create custom benchmarks**: Domain-specific test suites
- **Build regression tests**: Detect quality degradation
- **Define quality gates**: Pass/fail criteria for deployment
- **Create reusable intelligence**: Build a `model-evaluation` skill

## Chapter Structure

| # | Lesson | Your Skill Improves |
|---|--------|---------------------|
| **0** | **Build Your Evaluation Skill** | **Created from docs** |
| 1 | Evaluation Taxonomy and Strategy | Define what to measure |
| 2 | LLM-as-a-Judge Implementation | GPT-4 evaluation setup |
| 3 | Task-Specific Benchmark Design | Custom Task API benchmarks |
| 4 | Regression Testing for Models | Detect quality degradation |
| 5 | Quality Gates and Thresholds | Define pass/fail criteria |
| **6** | **Capstone — Evaluation Pipeline** | **Automated quality system** |

## 4-Layer Teaching Progression

This chapter follows the **4-Layer Teaching Method**:

- **Lesson 0 (L00)**: Skill-First—create skill before learning technology
- **Lessons 1-3 (Layer 1)**: Build mental models—understand evaluation
- **Lessons 4-5 (Layer 2)**: AI Collaboration—design gates with Three Roles
- **Lesson 6 (Layer 4)**: Spec-driven capstone—build evaluation pipeline

## Evaluation Taxonomy

| Type | What It Measures | How |
|------|------------------|-----|
| Task Accuracy | Correct outputs | Golden test sets |
| Safety | Harmful output rate | Red-team suite |
| Quality | Coherence, helpfulness | LLM-as-Judge |
| Efficiency | Latency, cost | Benchmarks |

## LLM-as-Judge Pattern

```python
def llm_judge(response: str, criteria: list[str]) -> dict:
    """Score response quality using GPT-4o-mini."""
    prompt = f"""Rate this response on each criterion (1-5):

Response: {response}

Criteria:
{chr(10).join(f"- {c}" for c in criteria)}

Respond with JSON: {{"scores": {{}}, "reasoning": "..."}}
"""
    # GPT-4o-mini is cost-effective: ~$0.001/eval
    ...
```

## Quality Gates

```yaml
# Quality gate configuration
gates:
  task_accuracy:
    threshold: 0.90
    required: true
  json_validity:
    threshold: 0.95
    required: true
  harm_reduction:
    threshold: 0.90
    required: true
  latency_p99:
    threshold: 500  # ms
    required: false
```

All required gates must pass before deployment.

## Task API Benchmark

| Test Case | Expected | Measurement |
|-----------|----------|-------------|
| Task creation | Correct JSON | Exact match |
| Priority inference | High/Medium/Low | Classification |
| Due date parsing | Valid date | Format validation |
| Error handling | Graceful refusal | LLM-as-Judge |

## Prerequisites

- **Chapter 68 completion**: Aligned model ready for evaluation
- **OpenAI API access**: For LLM-as-Judge (cost: ~$0.10/100 evals)
- **Python testing familiarity**: pytest patterns

## Looking Ahead

This chapter produces:
1. An **evaluation pipeline** that runs on every model update
2. A **model-evaluation skill** for future quality work
3. **Quality gates** that prevent bad models from shipping

Chapter 70 teaches deployment—exporting to GGUF and serving via Ollama.

**Total Duration**: ~5.2 hours (310 minutes)
