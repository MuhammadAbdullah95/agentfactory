---
sidebar_position: 6
title: "Chapter 6: The Seven Principles of General Agent Problem Solving"
slides:
  source: "https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/slides/part-1/chapter-06/agent-engineering-principles.pdf"
  title: "Agent Engineering Principles"
  height: 700
---

# Chapter 6: The Seven Principles of General Agent Problem Solving

You've learned about the Agent Factory paradigm and experienced Claude Code and Cowork firsthand. Now comes the crucial question: **How do you work effectively with agentic AI systems?**

This chapter begins with **Operational Best Practices**—the practical workflows that separate productive Claude Code sessions from frustrating ones. You'll learn to structure your work, course correct when things go wrong, and recognize failure patterns before they waste your time.

Then we introduce **The Seven Principles of General Agent Problem Solving**—the conceptual framework that explains _why_ those practices work. These principles emerged from real-world experience with agentic AI systems and represent the core patterns that separate successful AI-augmented workflows from frustrating ones.

The seven principles are:

1. **Bash is the Key** — Terminal access is the foundational capability that distinguishes agentic AI from passive assistants
2. **Code as the Universal Interface** — Code provides the precision that natural language lacks, making it the true shared language of human-AI collaboration
3. **Verification as Core Step** — Continuous testing and validation, not as an afterthought but as the primary workflow
4. **Small, Reversible Decomposition** — Breaking problems into atomic steps that can be independently tested and rolled back
5. **Persisting State in Files** — Using context files (CLAUDE.md, ADRs) to maintain shared understanding across sessions
6. **Constraints and Safety** — Guardrails and permission models that enable confident collaboration
7. **Observability** — Visibility into what the AI is doing, enabling debugging and trust

These principles work together as an integrated system. Terminal access enables agentic capability. Code specification provides precision. Verification ensures reliability. Decomposition manages complexity. State persistence accumulates context. Constraints enable safety. Observability builds trust.

## Prerequisites

This chapter builds directly on:

- **Chapter 3: General Agents** — You learned Claude Code's core capabilities: how agentic AI differs from chat-based assistants, tool use patterns, and the autonomous problem-solving loop
- **Chapter 4: Context Engineering** — You learned why context quality determines agent reliability, the context window as working memory, and how to structure information for AI consumption
- **Chapter 5: Spec-Driven Development** — You learned the four-phase SDD workflow, specification design, and task orchestration patterns

The Seven Principles provide the **conceptual framework** that explains _why_ these capabilities work together effectively.

## Lessons in This Chapter

| # | Lesson | Duration | Focus |
|---|--------|----------|-------|
| 0 | Operational Best Practices | 25 min | Session structure, course correction, failure patterns |
| 1 | Bash is the Key | 20 min | Terminal as foundational agentic capability |
| 2 | Code as Universal Interface | 25 min | Precision through code vs. natural language |
| 3 | Verification as Core Step | 25 min | Continuous testing as primary workflow |
| 4 | Small, Reversible Decomposition | 30 min | Atomic steps, independent testing, rollback |
| 5 | Persisting State in Files | 25 min | CLAUDE.md, ADRs, shared context |
| 6 | Constraints and Safety | 30 min | Permission models, guardrails, risk levels |
| 7 | Observability | 25 min | Activity logs, progress tracking, debugging |
| 8 | Putting It All Together | 35 min | Integrated workflows, real-world scenarios |
| 9 | Chapter Quiz | 20 min | Assessment of principle understanding |

**Total Duration:** ~4.5 hours

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

## Key Prompt Patterns

| Principle | Pattern | Example Prompt |
|-----------|---------|----------------|
| **Bash is the Key** | Command verification | "Use `ls` to verify the directory exists before creating files" |
| **Code as Interface** | Specification over description | "Write a TypeScript interface for the expected input/output" |
| **Verification** | Test-first instruction | "Write the test first, then implement the function to pass it" |
| **Decomposition** | Atomic commits | "Break this into steps. Commit after each step works." |
| **State Persistence** | Context file creation | "Add this decision to CLAUDE.md so future sessions remember" |
| **Constraints** | Permission boundaries | "Only modify files in the `src/` directory" |
| **Observability** | Progress reporting | "After each step, report what you did and what's next" |

## References & Further Reading

This chapter synthesizes insights from:

- Anthropic. (2025). "Claude Code: Best practices for agentic coding." anthropic.com/engineering
- Anthropic. (2025). "Building effective agents." anthropic.com/research
- Brooks, F. (1975). _The Mythical Man-Month_. Addison-Wesley — Classic on decomposition and managing complexity
- Hunt, A. & Thomas, D. (2019). _The Pragmatic Programmer_, 2nd ed. — Foundations of verification-first development
- Fowler, M. (2025). "Understanding Spec-Driven Development." martinfowler.com — Context on agentic workflows
