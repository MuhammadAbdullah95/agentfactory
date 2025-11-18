---
title: "Spec-Kit Plus Foundation: What You're About to Build With"
chapter: 31
lesson: 1
duration_minutes: 40

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Understanding SDD-RI Framework Choice"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain why this book teaches Spec-Kit Plus over other SDD frameworks"

  - name: "Recognizing Spec-Kit Plus Architecture"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can describe the three-tier pattern: You → Orchestrator → Specialized Subagents"

  - name: "Distinguishing Horizontal vs Vertical Intelligence"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can differentiate ADRs/PHRs (H-Intelligence) from Orchestrator/Subagents (V-Intelligence)"

  - name: "Connecting SDD-RI Concepts to Framework"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain how Spec-Kit Plus implements SDD-RI concepts from Chapter 30 Lessons 6-7"

learning_objectives:
  - objective: "Explain why this book chose Spec-Kit Plus over Kiro, Spec-Kit, or Tesel"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Verbal explanation with 2-3 specific reasons"

  - objective: "Describe Spec-Kit Plus three-tier architecture (You → Orchestrator → Subagents)"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Diagram annotation or explanation"

  - objective: "Distinguish Horizontal Intelligence (ADRs, PHRs) from Vertical Intelligence (delegation hierarchy)"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Comparison explanation"

  - objective: "Connect Spec-Kit Plus features to SDD-RI concepts learned in Chapter 30"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Mapping exercise (ADRs → reasoning capture, PHRs → AI interaction logging)"

cognitive_load:
  new_concepts: 4
  assessment: "4 new concepts (Framework choice rationale, Spec-Kit Plus architecture, H/V Intelligence distinction, SDD-RI implementation) within A2 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Compare Spec-Kit Plus with other frameworks in depth; design hypothetical Intelligence Template for domain of choice"
  remedial_for_struggling: "Focus on three-tier diagram visualization; use concrete examples of ADRs and PHRs from calculator project"

# Generation metadata
generated_by: "content-implementer v3.0.0"
source_spec: "specs/10-chapter-31-redesign/spec.md"
created: "2025-11-18"
last_modified: "2025-11-18"
git_author: "Claude Code"
workflow: "manual-implementation"
version: "1.0.0"
---

# Spec-Kit Plus Foundation: What You're About to Build With

Before diving into installation and hands-on development, you need to understand WHAT Spec-Kit Plus is and WHY this book uses it. Chapter 30 Lesson 8 introduced you to the SDD framework landscape—four different approaches to specification-driven development. This lesson zooms into Spec-Kit Plus specifically, showing you its architecture and how it implements the SDD-RI concepts you learned.

By the end of this lesson, you'll understand the three-tier Vertical Intelligence pattern (You → Orchestrator → Specialized Subagents), distinguish Horizontal Intelligence (ADRs + PHRs) from Vertical Intelligence, and recognize how Spec-Kit Plus captures the reasoning patterns you learned in Chapter 30 Lessons 6-7. Most importantly, you'll know WHY you're about to install this framework instead of alternatives.

---

## Section 1: Recap - The SDD-RI Journey So Far

You've completed a significant journey through specification-driven development and reusable intelligence:

**Chapter 30 Progression**:
- **Lessons 1-5**: SDD fundamentals (specifications, planning, validation)
- **Lessons 6-7**: RI concepts (skills, subagents, Persona+Questions+Principles pattern)
- **Lesson 8**: Framework landscape (Kiro, Spec-Kit, Spec-Kit Plus, Tesel)

**Key insight from Chapter 30**: Reusable Intelligence (not reusable code) is the new unit of value in AI-native development.

**Transition to Chapter 31**: Now we implement SDD-RI using Spec-Kit Plus framework, the tool specifically designed for this purpose.

---

## Section 2: Why Spec-Kit Plus? (Framework Choice Reasoning)

### The Four SDD Framework Options

When Chapter 30 introduced the framework landscape, four main approaches emerged:

**1. Kiro** — Start Simple
- Philosophy: SDD shouldn't require learning complex processes
- Best for: Solo developers or tiny teams (1-3 people) learning SDD for the first time
- Trade-off: Simplicity and low cognitive load vs governance and consistency enforcement

**2. Spec-Kit** — Strong Governance (GitHub's standard)
- Philosophy: Immutable principles enforce consistency across everything
- Best for: Teams of 5-50+ people where consistency matters, enterprise environments, open-source frameworks
- Strengths: Comprehensive traceability, scales to large teams, strong governance
- Limitations: Doesn't document architectural "why" decisions, no AI interaction tracking, no built-in domain expertise

**3. Spec-Kit Plus** — Spec-Kit + Intelligence (This book)
- Philosophy: Foundation of Spec-Kit + three critical intelligence layers for AI-native teams
- Best for: Teams collaborating with AI agents, building systems that last years, regulated domains, learning from AI interactions
- What it adds: ADRs (reasoning), PHRs (AI interactions), Intelligence Templates (domain expertise)

**4. Tesel** — Specs as Source of Truth
- Philosophy: Take spec-driven development to its logical extreme—specs are the ONLY source of truth
- Best for: Safety-critical systems (aerospace, medical devices)
- Status: Private beta (2025)

### Why This Book Chose Spec-Kit Plus

When you're learning SDD-RI (not just SDD), you need a framework that:

**1. Captures Your Reasoning (ADRs)**
- In Lesson 7, you learned the Persona + Questions + Principles pattern for skill design
- ADRs document that reasoning for your team and AI agents
- Example: "Why git-workflow skill instead of git-commit subagent?" → ADR explains the tradeoff
- This bridges the gap between specification (what to build) and intelligence (how to think about it)

**2. Logs AI Interactions (PHRs)**
- Throughout Chapter 30, you saw: AI suggests → you refine → you converge
- PHRs capture and let you LEARN from those interactions
- Example: "Prompt A generated vulnerable code. Prompt B fixed it. Use B next time."
- This preserves the collaborative knowledge that makes AI partnerships effective

**3. Provides Domain Expertise (Intelligence Templates)**
- You've been using the Education template (Bloom's levels, CEFR proficiency, code requirements)
- Templates prevent rebuilding knowledge every project
- Example: "New healthcare team? Start with healthcare template. Know HIPAA rules before coding."
- This accelerates teams by giving them pre-built domain patterns

**These three additions are not optional overhead.** They implement SDD-RI concepts directly into the framework you'll use every day.

---

## Section 3: Spec-Kit Plus Architecture Deep Dive

Spec-Kit Plus has three independent but integrated components that work together:

### The Three Independent Layers

**1. The Framework** (Spec-Kit Plus toolkit)
- File templates for specifications, plans, tasks, ADRs, PHRs
- Directory structure enforcing Spec → Clarify → Plan → Tasks → Implement progression
- Slash commands (`/sp.specify`, `/sp.plan`, `/sp.tasks`, `/sp.implement`, etc.)
- Prompt templates and evaluation guides
- Storage system for artifacts (ADRs, PHRs)

**2. The AI Orchestrator** (Your chosen tool)
- Claude Code (recommended for this book)
- Gemini CLI (alternative option)
- Or any AI tool that can execute slash commands and specialized roles
- Acts as the "main collaborator" who understands Spec-Kit Plus workflow and routes work appropriately

**3. The Vertical Intelligence Layer** (Delegated AI capabilities)
- Specialized subagents for specification, planning, implementation, validation
- Each subagent has deep expertise in its domain
- Orchestrator knows which expert to consult for each phase

**Critical Insight**: Spec-Kit Plus is NOT an AI service. It's an opinionated methodology framework that works with multiple AI tools. You choose your orchestrator (Claude Code or Gemini CLI), and Spec-Kit Plus provides the workflow and templates.

---

## Section 4: Horizontal vs Vertical Intelligence

To truly understand Spec-Kit Plus, you need to understand both types of intelligence it captures:

### Horizontal Intelligence: Knowledge Across Time

How you preserve decisions and learnings for future reference.

**ADRs (Architectural Decision Records)**
- Document the "WHY" behind significant decisions
- Example: "Why JWT instead of sessions?" → ADR explains security/scalability tradeoff
- Stored in: `history/adr/`
- Created via: `/sp.adr <title>` when architectural choices are made
- Who sees them: Your team, auditors, AI agents reviewing context

**PHRs (Prompt History Records)**
- Capture AI collaboration sessions automatically
- Example: "AI suggested pattern X. We chose it because..." → PHR logs reasoning
- Stored in: `history/prompts/<feature>/`
- Created automatically (system logs them, you don't manually invoke PHR)
- Who sees them: Your team, auditors, AI agents learning from previous interactions

**Connection to SDD-RI**: ADRs capture the reasoning you practiced in Lesson 6-7 (why this skill design? why this subagent persona?). They're not bureaucracy—they're how teams learn together.

### Vertical Intelligence: Knowledge Through Hierarchy

How you work with AI orchestrators and specialized subagents.

**The Three-Tier Pattern**:

```
┌─────────────────────────────────────────────────────────┐
│  👤 YOU (Architect/Validator)                           │
│  Strategic Decisions & Quality Control                  │
│                                                          │
│  "What to build?" ──────────────┐                       │
│                                  ↓                       │
│                   ┌──────────────────────────┐          │
│                   │  🤖 AI ORCHESTRATOR      │          │
│                   │  Main Collaborator       │          │
│                   │  Routes work to experts  │          │
│                   └──────────────────────────┘          │
│                            ↓                             │
│         ┌──────────────────┼──────────────────┐         │
│         ↓                  ↓                  ↓          │
│  ┌────────────┐   ┌────────────┐   ┌────────────┐      │
│  │ 📝 Spec    │   │ 🏗️ Plan    │   │ ⚙️ Impl    │      │
│  │ Subagent   │   │ Subagent   │   │ Subagent   │      │
│  │            │   │            │   │            │      │
│  │ Writes     │   │ Creates    │   │ Generates  │      │
│  │ clear      │   │ plans      │   │ code +     │      │
│  │ specs      │   │            │   │ tests      │      │
│  └────────────┘   └────────────┘   └────────────┘      │
│         │                  │                  │          │
│         └──────────────────┼──────────────────┘         │
│                            ↓                             │
│                   ┌────────────────┐                     │
│                   │ ✅ Validation  │                     │
│                   │ Subagent       │                     │
│                   │ Reviews quality│                     │
│                   └────────────────┘                     │
│                            │                             │
│  ← Review & Approve ───────┘                            │
└─────────────────────────────────────────────────────────┘
```

**How Vertical Intelligence Works**:

1. **You describe intent** - "Build a calculator with 5 operations"
2. **Orchestrator delegates** - Routes to appropriate subagent (e.g., Specification Subagent)
3. **Subagent executes** - Asks clarifying questions, identifies gaps, returns complete spec
4. **You validate** - Review and approve (or iterate)
5. **Orchestrator delegates next phase** - Routes to Planning Subagent
6. **Cycle repeats** - Through Plan → Tasks → Implementation

**Why This Matters**: You don't need to memorize specification templates, planning methodologies, or code patterns. The orchestrator knows which expert to consult for which task. Your job is **thinking clearly about intent and validating results**, not memorizing frameworks.

**Connection to SDD-RI**: Subagents ARE the skills/subagents you designed in Lesson 7 (Persona + Questions + Principles pattern), now operational in a framework you use daily.

---

## Section 5: What You'll Build in Chapter 31

### The Calculator Project (SDD-RI Workflow Demonstration)

You'll build a complete calculator library using Spec-Kit Plus, following the exact workflow structure:

**Phase 1: Constitution** (Lesson 3)
- Create project-wide quality standards
- Document: ADR explaining why these standards matter

**Phase 2: Specification** (Lesson 4)
- Write calculator spec (5 operations: add, subtract, multiply, divide, power)
- Practice: Evals-first thinking from Chapter 30 Lesson 2

**Phase 3: Clarify** (Lesson 5)
- Identify specification gaps with `/sp.clarify`
- Refine until implementation-ready

**Phase 4: Plan** (Lesson 6)
- Generate implementation plan with `/sp.plan`
- Document: ADR for architectural decisions (why this structure?)

**Phase 5: Tasks** (Lesson 7)
- Decompose plan into atomic work units with `/sp.tasks`
- Checkpoint-driven execution planning

**Phase 6: Implement** (Lesson 8)
- AI-driven code generation with `/sp.implement`
- Capture: PHR logging AI interactions and decisions

**Phase 7: Reusable Intelligence** (Lesson 9)
- Extract patterns from Lessons 3-8
- Create: Specification Review Skill + Spec Auditor Subagent using Persona+Questions+Principles

**Outcome**: Complete calculator + reusable intelligence library ready for next projects.

---

## Section 6: Prerequisites Check

Before installation (next lesson), verify you have:

**1. Python 3.12+**
```bash
python --version
# Must show: Python 3.12.0 or higher
```

**2. AI Tool Choice**
- **Claude Code** (recommended for this book)
- **Gemini CLI** (alternative option)
- Or any AI tool capable of executing slash commands

**3. Terminal Comfort**
- **bash** (macOS, Linux, WSL on Windows)
- **powershell** (Windows native)

**4. Git Installed**
```bash
git --version
# Any recent version works
```

If any prerequisite is missing, address it now before Lesson 2 (Installation).

---

## Try With AI

### Setup

**Tool**: Claude Code, Gemini CLI, or your AI companion

**Context**: Chapter 30 complete, ready for Chapter 31 hands-on work

**Goal**: Validate understanding of Spec-Kit Plus architecture before installation

### Prompt Set (Copy-Paste Ready)

**Prompt 1: Framework Choice Reasoning**

```
I just learned about four SDD frameworks in Chapter 30 (Kiro, Spec-Kit,
Spec-Kit Plus, Tesel).

Explain in 2-3 sentences why THIS BOOK chose Spec-Kit Plus instead of
the others. What three features does Spec-Kit Plus add that matter for
AI-native teams learning SDD-RI?
```

**Expected Outcome**: AI should identify ADRs (reasoning capture), PHRs (AI interaction logging), Intelligence Templates (domain expertise) and connect to SDD-RI concepts.

---

**Prompt 2: Architecture Understanding**

```
Explain the three-tier Vertical Intelligence pattern in Spec-Kit Plus:

You → Orchestrator → Specialized Subagents

Use the calculator project as an example. Walk me through how a
specification gets written using this pattern.
```

**Expected Outcome**: AI should explain delegation flow (you describe intent → orchestrator routes to Spec Subagent → subagent asks questions and generates spec → you validate).

---

**Prompt 3: H vs V Intelligence**

```
What's the difference between Horizontal Intelligence (ADRs + PHRs)
and Vertical Intelligence (Orchestrator + Subagents)?

Give me a concrete example of WHEN I would create an ADR vs when
Vertical Intelligence handles something automatically.
```

**Expected Outcome**: AI should distinguish knowledge capture (H-Intelligence, explicit documentation) from delegation hierarchy (V-Intelligence, workflow automation).

---

**Prompt 4: SDD-RI Connection**

```
In Chapter 30 Lesson 7, I learned the Persona + Questions + Principles
pattern for designing skills.

How does Spec-Kit Plus implement this? Where do I see this pattern
in the calculator project I'm about to build?
```

**Expected Outcome**: AI should connect P+Q+P pattern to subagent design (Spec Subagent has persona, asks questions, applies principles) and to Lesson 9 (creating Specification Review Skill using P+Q+P).

---

## What You've Accomplished

You've established the conceptual foundation for Spec-Kit Plus:

✅ **Framework Choice**: Understand why Spec-Kit Plus (not Kiro/Spec-Kit/Tesel) for SDD-RI learning

✅ **Architecture**: Recognize three-tier pattern (You → Orchestrator → Subagents)

✅ **H/V Intelligence**: Distinguish ADRs/PHRs (knowledge capture) from delegation hierarchy

✅ **SDD-RI Connection**: See how Spec-Kit Plus implements Persona+Questions+Principles pattern

✅ **Prerequisites**: Know what's needed before installation (Python 3.12+, AI tool, terminal, git)

**Most importantly**: You understand WHAT you're installing and WHY before you install it (Principle 1: Specification Primacy - intent before implementation).

**Next Lesson**: Installation & Setup (hands-on Spec-Kit Plus installation, project initialization, verification)
