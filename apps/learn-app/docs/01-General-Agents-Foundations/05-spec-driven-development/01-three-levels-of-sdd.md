---
sidebar_position: 1
title: "The Three Levels of SDD"
description: "Understanding the spectrum of spec-driven development from throwaway specs to code-generating specifications"
keywords:
  [
    "spec-driven development",
    "SDD",
    "specification levels",
    "spec-first",
    "spec-anchored",
    "spec-as-source",
    "AI development",
    "Digital FTE",
  ]
chapter: 5
lesson: 1
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Classify SDD Implementation Levels"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify which SDD level applies to a given project scenario"

  - name: "Evaluate SDD Level Trade-offs"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can articulate why one level suits a scenario better than others"

  - name: "Select Appropriate SDD Level"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can choose the right SDD level for their project and justify the choice"

learning_objectives:
  - objective: "Distinguish between Spec-First, Spec-Anchored, and Spec-as-Source levels"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can correctly classify project scenarios into the three levels"

  - objective: "Analyze the trade-offs between maintaining specs alongside code versus regenerating code from specs"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can explain why a team might choose one level over another"

  - objective: "Select the appropriate SDD level for a given project context"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student can recommend an SDD level for a described scenario with justification"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (Spec-First, Spec-Anchored, Spec-as-Source, maintenance burden, determinism challenges) within A2-B1 transition range"

differentiation:
  extension_for_advanced: "Explore Model-Driven Development parallels and the determinism challenges that make Spec-as-Source experimental"
  remedial_for_struggling: "Focus on the two most common levels (Spec-First and Spec-Anchored) before introducing Spec-as-Source"
---

# The Three Levels of SDD

In Lesson 00, you experienced why vibe coding fails: context loss, assumption drift, and pattern violations compound until your AI produces unusable output. Specifications solve this by giving Claude the complete picture upfront.

But not all specifications are created equal. Some are planning artifacts you throw away after implementation. Others become living documentation that evolves with your codebase. And at the experimental frontier, some teams treat specifications as the only artifact worth maintaining, regenerating code on demand.

Understanding where you operate on this spectrum helps you calibrate your effort. You don't need enterprise-grade living documentation for a weekend project. But you also shouldn't throwaway specs for a system your team will maintain for years.

## The Three Levels

| Level              | Creation                   | Maintenance                        | Use Case                            |
| ------------------ | -------------------------- | ---------------------------------- | ----------------------------------- |
| **Spec-First**     | Spec guides implementation | Spec discarded after               | Most common; quick tasks            |
| **Spec-Anchored**  | Spec written first         | Both spec + code maintained        | Team projects; living documentation |
| **Spec-as-Source** | Spec is primary artifact   | Only spec edited; code regenerated | Experimental (Tessl approach)       |

Let's examine each level.

## Level 1: Spec-First (Most Common)

**You write the spec. Claude implements it. You move on.**

This is where most practitioners operate, and for good reason. For 80% of tasks, the specification served its purpose the moment Claude finished implementing it. The spec prevented vibe coding, ensured Claude had complete context, and resulted in working code.

After that? The spec becomes historical record at best, garbage at worst.

### When Spec-First Works

- Single-session tasks that won't require revisiting
- Personal projects without team coordination
- Prototypes and experiments
- Bug fixes where the spec is the fix description

### The Trade-off

**Benefit**: Zero maintenance overhead. Write once, implement once, done.

**Cost**: Six months later, when you need to modify the feature, you have no specification. You're reading code to understand intent, which is exactly the problem specifications solve.

### Example: Adding a Notification System

```markdown
# Notification System Specification

## Intent

Add browser notifications for new messages.

## Requirements

- Toast notifications appear in bottom-right
- Notifications auto-dismiss after 5 seconds
- Maximum 3 notifications visible simultaneously
- Queue excess notifications

## Constraints

- No external notification libraries
- Use existing design system colors
- Must work with current message polling interval

## Success Criteria

- Notifications appear within 500ms of new message
- Users can manually dismiss notifications
- Notifications don't stack infinitely
```

Claude implements it. You verify it works. The spec gets filed somewhere you'll never look again. This is perfectly appropriate for a single developer building a personal project.

## Level 2: Spec-Anchored (Team Standard)

**Both specification and code are maintained artifacts.**

When you work with a team, specifications become documentation. A new developer joining in month six shouldn't need to reverse-engineer your notification system from code. They should read the spec and understand the intent.

### When Spec-Anchored Works

- Team projects with multiple contributors
- Systems requiring compliance documentation
- Products with long maintenance horizons
- Features that will undergo multiple iterations

### The Trade-off

**Benefit**: Specifications serve as onboarding documentation, architectural decision records, and implementation guides. When requirements change, you update the spec first, then the code, maintaining alignment.

**Cost**: Double maintenance burden. Every code change potentially requires a spec change. Specs and code can drift out of sync if discipline lapses.

### The Discipline Requirement

Spec-Anchored only works if you enforce the discipline:

1. **Spec changes before code changes.** Always.
2. **Code reviews check spec alignment.** Reviewers verify the spec was updated.
3. **Specs live near code.** Not in a separate wiki no one visits.

When teams adopt Spec-Anchored without this discipline, they get the worst outcome: outdated specs that actively mislead readers, combined with maintenance overhead that provides no value.

### Example: The Same Notification System, Anchored

The spec from Level 1 becomes a living document:

```
docs/
  notification-system/
    spec.md              # Living specification
    changelog.md         # History of changes
    decisions/           # ADRs for architectural choices
src/
  notifications/
    ... implementation ...
```

When you later need to add notification sound support, you:

1. Update `spec.md` with the new requirements
2. Have Claude implement against the updated spec
3. Commit both spec and code changes together

A developer joining the team reads `spec.md` and understands the notification system without reading implementation code.

## Level 3: Spec-as-Source (Experimental)

**The specification is the primary artifact. Code is regenerated on demand.**

This is the frontier. Companies like Tessl are exploring a world where you never edit code directly. You edit specifications, and AI regenerates the implementation. Code becomes a build artifact, like compiled binaries.

### The Appeal

Think about it: if Claude can generate code reliably from specifications, why maintain code at all? Code has bugs, requires refactoring, accumulates technical debt. Specifications express intent directly.

In this model:

- You edit the spec to add a feature
- AI regenerates affected code
- Tests verify the generation
- Code is never manually modified

### The Problem: Determinism

Here's where Spec-as-Source breaks down in practice:

**Identical specifications do not produce identical code.**

Ask Claude to implement the same spec twice. You'll get functionally equivalent but syntactically different implementations. Variable names differ. Control flow varies. Comments appear or disappear.

For production systems, this creates problems:

- Git diffs become meaningless (every regeneration is a massive diff)
- Debugging becomes harder (which generation introduced the bug?)
- Performance characteristics vary unpredictably
- Third-party integrations may break on regeneration

### The MDD Parallel

This isn't a new challenge. Model-Driven Development (MDD) promised the same transformation in the 2000s: write models, generate code, never touch implementation.

MDD failed to achieve mainstream adoption for the same reasons Spec-as-Source struggles:

- Generated code needed manual patches for edge cases
- Models couldn't express all implementation concerns
- The abstraction leaked, requiring developers to understand both layers

AI-powered generation is more flexible than MDD code generators, but the determinism problem remains unsolved.

### When to Consider Spec-as-Source

Despite challenges, Spec-as-Source makes sense for:

- **Highly repetitive code**: CRUD operations, API clients, data transformations
- **Disposable code**: Scripts, one-time migrations, proof-of-concepts
- **Environments with strong test coverage**: When tests validate behavior, implementation variance matters less

For a production web application with years of expected maintenance? Spec-Anchored remains the safer choice.

## Choosing Your Level

Most practitioners should default to **Spec-First** and graduate to **Spec-Anchored** when:

- Working with a team (2+ people)
- Building something with 6+ month maintenance horizon
- Creating systems that require compliance documentation
- Developing features that will undergo multiple iterations

Reserve **Spec-as-Source** experimentation for:

- Personal projects with strong test coverage
- Highly repetitive, well-understood domains
- Situations where you're willing to accept regeneration variance

## The Maturity Spectrum

Think of these levels as a maturity spectrum you can adopt gradually:

**Week 1**: Start with Spec-First. Write specs before asking Claude to implement. Experience the improvement over vibe coding.

**Month 1**: For projects you'll maintain, try Spec-Anchored. Keep specs alongside code. Update specs when requirements change.

**Later**: When you have strong test coverage and understand the trade-offs, experiment with Spec-as-Source for appropriate use cases.

You don't need to commit to one level for all projects. A solo weekend project is Spec-First. Your team's core product is Spec-Anchored. That AI-generated API client you regenerate weekly might be Spec-as-Source.

## Try With AI

**Setup:** Open Claude Code with any project you're currently working on.

**Prompt 1: Level Classification**

```
I'm working on [describe your project briefly].

Help me decide which SDD level is appropriate:
- Spec-First (write once, implement, discard spec)
- Spec-Anchored (maintain both spec and code)
- Spec-as-Source (spec is primary, regenerate code)

Consider: team size, maintenance horizon, documentation needs, and how often requirements change.
```

**What you're learning:** This prompt forces you to articulate the factors that determine SDD level selection. Claude will ask clarifying questions about your project that reveal your implicit assumptions about maintenance and collaboration.

**Prompt 2: Trade-off Analysis**

```
For a team of 5 developers building a customer portal that will be maintained for 3+ years:

Explain the risks of using Spec-First instead of Spec-Anchored. Then explain the costs of Spec-Anchored that might make a team choose Spec-First anyway.
```

**What you're learning:** This prompt explores the tension between documentation value and maintenance burden. There's no universally correct answer, which forces you to reason about trade-offs rather than follow rules.

**Prompt 3: Failure Scenarios**

```
When would Spec-as-Source fail catastrophically in a real project? Give me three specific scenarios with enough detail that I could recognize if I'm heading toward them.
```

**What you're learning:** Understanding failure modes helps you recognize when an approach is inappropriate for your context. Claude's scenarios will likely include determinism issues, debugging challenges, and third-party integration problems that the lesson introduced conceptually.

**Safety note:** These prompts are exploratory, helping you think through SDD level selection. None will modify your codebase or create files.
