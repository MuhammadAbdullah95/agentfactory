---
sidebar_position: 5
title: "Chapter 5: The Seven Principles of General Agent Problem Solving"
slides:
  source: "https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/slides/part-1/chapter-05/agent-engineering-principles.pdf"
  title: "Agent Engineering Principles"
  height: 700
---

# Chapter 5: The Seven Principles of General Agent Problem Solving

You've learned about the Agent Factory paradigm and experienced Claude Code and Cowork firsthand. Now comes the crucial question: **How do you work effectively with agentic AI systems?**

This chapter begins with **Operational Best Practices**—the practical workflows that separate productive Claude Code sessions from frustrating ones. You'll learn to structure your work, course correct when things go wrong, and recognize failure patterns before they waste your time.

Then we introduce **The Seven Principles of General Agent Problem Solving**—the conceptual framework that explains *why* those practices work. These principles emerged from real-world experience with agentic AI systems and represent the core patterns that separate successful AI-augmented workflows from frustrating ones.

The seven principles are:

1. **Bash is the Key** — Terminal access is the foundational capability that distinguishes agentic AI from passive assistants
2. **Code as the Universal Interface** — Code provides the precision that natural language lacks, making it the true shared language of human-AI collaboration
3. **Verification as Core Step** — Continuous testing and validation, not as an afterthought but as the primary workflow
4. **Small, Reversible Decomposition** — Breaking problems into atomic steps that can be independently tested and rolled back
5. **Persisting State in Files** — Using context files (CLAUDE.md, ADRs) to maintain shared understanding across sessions
6. **Constraints and Safety** — Guardrails and permission models that enable confident collaboration
7. **Observability** — Visibility into what the AI is doing, enabling debugging and trust

These principles work together as an integrated system. Terminal access enables agentic capability. Code specification provides precision. Verification ensures reliability. Decomposition manages complexity. State persistence accumulates context. Constraints enable safety. Observability builds trust.

## 📚 Teaching Aid

## What You'll Learn

By the end of this chapter, you'll have:

- **Operational Workflows** — Practical patterns for structuring sessions, course correcting, and avoiding common failure modes
- **Terminal Access Fundamentals** — Understanding why bash/terminal access is the primal agentic capability that enables all other principles
- **Code as Communication Medium** — Learning to use code and examples as the primary interface for precise AI collaboration
- **Verification-First Mindset** — Building workflows where testing happens continuously, not as a final step
- **Decomposition Strategies** — Breaking complex problems into small, reversible steps that can be independently verified
- **Context Management** — Creating and maintaining CLAUDE.md files and Architecture Decision Records that persist knowledge
- **Safety Frameworks** — Designing appropriate permission models and constraints for different risk levels
- **Observability Practices** — Making AI workflows transparent and debuggable through activity logs and progress tracking
- **Integrated Workflows** — Applying all seven principles together in real-world scenarios

## Why This Matters

The seven principles transform AI from a novelty into a reliable tool for production work. Without them:

- You're constantly repeating yourself (no state persistence)
- You're surprised by AI changes (no observability)
- You're afraid to let AI work (no safety constraints)
- You're debugging mysterious failures (no verification)
- You're overwhelmed by large changes (no decomposition)

With them:

- Context accumulates across sessions
- You see what AI is doing
- You can confidently give AI autonomy
- Problems are caught early
- Complex work becomes manageable
