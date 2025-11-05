---
sidebar_position: 2
title: "Chapter 31: Spec-Kit Plus Hands-On"
---

# Chapter 31: Spec-Kit Plus Hands-On

Welcome to hands-on specification-driven development. This chapter transforms understanding (from Chapter 30) into practice. You won't read about specifications—you'll write them. You won't learn about AI collaboration—you'll build projects with your AI companion from specifications to implementation.

Whether you're eager to start coding or skeptical that specs are worth the time, this chapter proves the value through direct experience: building projects specification-first is faster, more reliable, and more scalable than code-first development.

---

## From Chapter 30 to Chapter 31

**Chapter 30** taught you the foundations:
- Why specification-driven development matters (the vague code problem)
- What SDD is (spec-first, spec-anchored, spec-as-source levels)
- How to write your first spec (calculator exercise)
- Why teams need shared rules (Constitutions, ADRs, PHRs)
- When SDD became essential (AI convergence moment)
- Which tools exist (Kiro, Spec-Kit, **Spec-Kit Plus**, Tessel)

**Chapter 31** teaches you the workflow:
- How to install and configure Spec-Kit Plus
- How to create project Constitutions
- How to collaborate with AI on specifications (evals-first pattern)
- How to refine specs iteratively
- How to generate plans and document decisions (ADRs)
- How to decompose work with checkpoint-driven execution
- How to implement with validation protocols
- How to complete end-to-end workflows independently

**The Bridge**: Chapter 30 gave you the map. Chapter 31 teaches you to drive.

---

## What You'll Learn

By completing this chapter, you'll master:

1. **Spec-Kit Plus Architecture** — Understand Horizontal Intelligence (ADRs + PHRs) and Vertical Intelligence (orchestrator + subagents)
2. **Evals-First Collaboration** — How to explore problem space with AI BEFORE writing formal specifications
3. **Constitution Creation** — Setting project-wide quality standards that cascade to all features
4. **Specification Writing** — Creating clear, testable requirements using SMART criteria
5. **Iterative Refinement** — Using `/sp.clarify` to identify and resolve specification gaps
6. **Architecture Planning** — Generating implementation plans and documenting decisions with ADRs
7. **Task Decomposition** — Breaking plans into atomic work units with checkpoint-driven execution
8. **AI-Driven Implementation** — Orchestrating code generation with systematic validation protocols
9. **Independent Workflow** — Applying all skills end-to-end without guidance

Most importantly, you'll build the muscle memory for specification-first thinking that makes you dramatically faster in Chapters 32 and beyond.

---

## The Learning Journey (8 Lessons)

### **Lesson 1: Installation & Setup** (1.5 hours, A2 proficiency)
Install Spec-Kit Plus framework and configure your AI tool (Claude Code or Gemini CLI). Learn the three-tier architecture: Framework → Orchestrator → Subagents.

### **Lesson 2: Constitution Phase** (1.5 hours, A2 proficiency)
Create your first project Constitution defining global quality standards. Understand the cascade starting point: Constitution → Specs → Plans → Code.

### **Lesson 3: Specify Phase** (2 hours, A2→B1 proficiency)
Write a complete calculator specification using the evals-first pattern: collaborate with AI to explore the problem space, THEN formalize requirements with `/sp.specify`.

**Critical Teaching**: Evals are YOU asking your AI companion questions to clarify requirements before formalizing the spec.

### **Lesson 4: Clarify Phase** (1.5 hours, B1 proficiency)
Refine your specification iteratively using `/sp.clarify`. Learn to identify gaps, resolve ambiguities, and improve spec quality systematically.

### **Lesson 5: Plan Phase + ADRs** (2 hours, B1 proficiency)
Generate implementation plan with `/sp.plan`. Document architectural decisions using ADRs (Architectural Decision Records) for future reference.

### **Lesson 6: Tasks Phase + Checkpoints** (1.5 hours, B1 proficiency)
Decompose plan into atomic tasks with `/sp.tasks`. Master the checkpoint pattern: Agent completes phase → YOU review → YOU commit → Agent continues.

**Critical Teaching**: YOU control the workflow through checkpoints. AI doesn't run autonomously.

### **Lesson 7: Implement + Validate + PHRs** (2.5 hours, B1→B2 proficiency)
Orchestrate AI-driven implementation with `/sp.implement`. Apply systematic validation protocols. Understand PHR auto-creation (Prompt History Records are automatically generated).

**Critical Teaching**: PHRs are created by the system automatically. You learn where to find them for audit/review.

### **Lesson 8: Capstone Integration** (3-4 hours, B2 proficiency)
Complete end-to-end workflow independently: Constitution → Spec → Plan → Tasks → Implement → Validate. Build a converter system (temperature or unit conversion) without step-by-step guidance.

---

## Two Complete Projects

### **1. Calculator (Guided)** — Lessons 2-7
Build a 5-operation calculator (add, subtract, multiply, divide, power) through the complete Spec-Kit Plus workflow with step-by-step guidance.

**What You'll Create**:
- Project Constitution
- Complete specification with edge cases
- Implementation plan with architectural decisions
- Atomic task breakdown
- Working Python code with tests
- Validation report

**Time**: 10-11 hours across 6 lessons

### **2. Converter (Independent)** — Lesson 8
Build a temperature converter (simple) or multi-unit converter (complex) applying the complete workflow independently.

**What You'll Create**:
- All artifacts from Constitution to validated code
- 2-3 ADRs for architectural decisions
- 8-10 auto-created PHRs
- Reflection on cascade effect (spec quality → code quality)

**Time**: 3-4 hours in capstone lesson

---

## Prerequisites

Before starting Chapter 31, you should have:

✅ **Completed Chapter 30** — Specification-Driven Development Fundamentals
✅ **Python 3.13+** installed and working
✅ **Terminal/command-line familiarity** (basic navigation, running commands)
✅ **AI tool access** — Claude Code (via Anthropic) OR Gemini CLI (via Google)
✅ **Text editor or IDE** — VS Code, PyCharm, or similar

---

## Skills You'll Develop

By the end of this chapter, you'll have developed these skills:

**Technical Skills** (A2→B2 proficiency):
- Tool configuration and setup
- Constitution writing for quality standards
- SMART criteria specification writing
- Iterative refinement workflows
- Architecture planning and documentation
- Task decomposition and dependency management
- Checkpoint-driven execution control
- Validation protocol application

**Conceptual Skills** (A2→B2 proficiency):
- Evals-first thinking (explore before formalizing)
- Cascade principle (quality flows from specs)
- Horizontal Intelligence (organizational knowledge capture)
- Vertical Intelligence (orchestrator + specialist pattern)
- Human-in-control AI collaboration
- Specification as source-of-truth

**Soft Skills** (B1→B2 proficiency):
- Requirement clarification through AI dialogue
- Architectural decision-making
- Quality validation and critical thinking
- Independent problem-solving
- Reflective practice

---

## How to Use This Chapter

### **Linear Progression** (Recommended)
Complete lessons 1→8 in order. Each lesson builds on previous lessons. The calculator project spans lessons 2-7, and the capstone (lesson 8) applies everything independently.

### **Time Commitment**
- **Total**: 13-15 hours
- **Per lesson**: 1.5-4 hours
- **Per week**: 3-5 hours = 3-4 weeks at comfortable pace

### **Learning Style**
- **Hands-on**: Every lesson includes "Try With AI" activities
- **Concrete**: Real projects (calculator, converter) not abstract examples
- **Guided → Independent**: Scaffolding decreases as proficiency increases
- **Validated**: Checklists and rubrics help you self-assess

### **AI Tool Choice**
You'll choose between:
- **Claude Code** (recommended for this book)
- **Gemini CLI** (alternative, equally capable)

Lesson 1 includes decision guide. Both work identically with Spec-Kit Plus.

---

## What Makes This Chapter Different

Unlike traditional programming tutorials, this chapter teaches you to:

1. **Think specifications-first** — Requirements before code
2. **Collaborate with AI** — Co-reasoning, not just code generation
3. **Validate everything** — Never trust without verification
4. **Control the workflow** — Human architect, AI implementer
5. **Build for scale** — Single developer practices that work for teams

**The Result**: You'll complete projects faster, with fewer bugs, and clearer documentation than code-first development.

---

## After Chapter 31

You'll be ready for:

**Chapter 32: Real-World Spec-Kit Workflows** — Team parallelization, multi-component systems, and professional SDD at scale

**Part 6+: Advanced Topics** — Agents, APIs, databases, deployment (all using spec-first methodology)

**Real Projects** — You'll have the workflow muscle memory to build production systems specification-first

---

## Ready to Begin?

Start with **[Lesson 1: Installation & Setup](./01-installation-and-setup.md)** to configure your AI-native development toolkit.

Remember: Specifications are the primary artifact. Code is generated. Validation is non-negotiable. You are in control.

Let's build something real.
