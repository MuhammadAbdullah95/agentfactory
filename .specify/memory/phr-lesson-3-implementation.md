# Prompt History Record (PHR): Lesson 3 Implementation

**Date**: 2025-01-17
**Task**: Implement Lesson 3 (Testing AI Safely with Branches) — Chapter 8, Stage 2
**Status**: ✅ COMPLETE
**Learning**: Content-implementer reasoning for Stage 2 (AI Collaboration) pedagogical design

---

## Executive Summary

Successfully implemented Lesson 3 for Chapter 8 (Git & GitHub for AI-Driven Development) following Stage 2 (AI Collaboration) framework with mandatory Three Roles demonstrations. The lesson teaches branch-based parallel testing for AI-generated code with explicit bidirectional learning callouts.

**Key Achievement**: All three roles (AI as Teacher, Student as Teacher, Co-Worker Convergence) demonstrated with concrete scenarios and "What X learned" callouts, meeting Stage 2 validation requirements.

---

## Problem Statement

**Task**: Implement Stage 2 lesson on Git branches with Three Roles framework

**Context**:
- Chapter 8 (Git & GitHub for AI-Driven Development) redesign — 7 lessons, A1/A2 cognitive tier
- Lesson 3 is first Stage 2 (AI Collaboration) lesson after Stage 1 (Manual Foundation)
- Must demonstrate Three Roles: AI as Teacher (suggests pattern), Student as Teacher (corrects), Co-Worker (converge)
- Success criteria: SC-004 (75%+ manage branches without confusion), SC-007 (<5 min workflow), SC-013 (80%+ recognize branches vs commits)

**Critical Constraint**: If lesson shows only "human prompts → AI executes → done" without bidirectional learning, it FAILS Stage 2 validation and violates constitutional Principle 2 (Progressive Complexity) teaching framework.

---

## Analysis: Stage 2 Pedagogical Requirements

### What Makes Stage 2 Different from Stage 1

**Stage 1 (Lessons 1-2)**:
- Student learns Git manually (no AI yet)
- Direct command execution: `git init`, `git add`, `git commit`
- Discovery through observation: "What does `git status` show?"
- NO AI collaboration — foundation building only

**Stage 2 (Lessons 3-5)**:
- Concept already understood (from Stage 1)
- NOW introduce AI partnership
- Must demonstrate THREE ROLES simultaneously:
  1. AI teaches student something new (pattern, convention, strategy)
  2. Student teaches AI something new (constraint, context, correction)
  3. Together they iterate toward better solution than either alone

### Why Three Roles Are Mandatory

**Constitutional Principle 2** (Progressive Complexity) requires that Stage 2 teaching avoid "one-way instruction" (human tells AI, AI executes). Instead, knowledge must flow BIDIRECTIONALLY:
- Student learns from AI's suggestions (upskilling on patterns)
- AI learns student's context/constraints (customization)
- Iteration improves both understanding (convergence)

**If Three Roles are missing**:
- ❌ Lesson becomes traditional tutorial (lecture-style: "Here's how branches work, AI does it for you")
- ❌ Violates "AI as partner" principle
- ❌ Students don't practice evaluating AI outputs
- ❌ Fails to teach "AI doesn't know your constraints unless you teach it"

---

## Solution Architecture

### Lesson Structure (6 parts)

**Part 1: Hands-On Discovery** (No AI yet)
- Activities 1-3: Execute `git branch`, `git switch`, create changes
- Students OBSERVE branch isolation before AI enters
- Foundation for Three Roles conversation

**Part 2: Three Roles Demonstration** (Core Stage 2 content)
- Scenario 1 (AI as Teacher): Branch naming conventions
- Scenario 2 (Student as Teacher): Constraint-based corrections
- Scenario 3 (AI as Co-Worker): Convergence through iteration
- EACH scenario has explicit "What X learned" callout

**Part 3: Complete Workflow** (Put it together)
- Activities 4-6: Create second branch, test, merge, delete
- Practical execution of Three Roles decision-making
- Shows "real" workflow applying Three Roles insights

**Part 4: Trade-off Analysis** (Conceptual)
- "Branches are for" vs "Commits are better for"
- Decision framework: When to use which?
- Cognitive scaffolding for Part 6 pattern recognition

**Part 5: Reflection** (Learning synthesis)
- "What you learned from AI as Teacher"
- "What AI learned from you as Student"
- "What neither had individually (convergence)"
- Explicit Three Roles retrospective

**Part 6: Pattern Recognition** (Application)
- Scenarios A-C: Real situations where student applies knowledge
- "Should I branch or commit?" Decision-making
- Preparation for Lesson 6 (reusable patterns)

**Part 7: Try With AI** (Solo practice)
- 3 copyable prompts extending Three Roles learning
- Students practice bidirectional thinking independently

### Why This Structure Works

1. **Cognitive scaffolding**: Observe isolation (Part 1) BEFORE discussing AI collaboration (Part 2)
2. **Explicit learning callouts**: "What X learned" prevents implicit knowledge (student might miss learning otherwise)
3. **Convergence modeling**: Scenario 3 shows iteration isn't "perfect on first try" — improvement is collaborative
4. **Decision framework** (Part 4): Gives student ownership of "when to use branches"
5. **Real scenarios** (Part 6): Concrete patterns for future decision-making

---

## Three Roles Implementation Details

### Scenario 1: AI as Teacher (Branch Naming Conventions)

**Why naming conventions example**:
- Student doesn't ask for this explicitly
- AI volunteers pattern (teacher role)
- Student learns something new they didn't know to ask for

**Implementation**:
```
Student asks: "What are best practices for branch naming?"

AI teaches:
- feature/ prefix for features
- bugfix/ for bugs
- refactor/ for refactoring
- experiment/ for exploratory work

Benefits: team communication, automation, clarity

Callout: "What you learned: AI taught you naming convention system
you didn't explicitly ask for."
```

**Why this works**: Shows AI as **proactive mentor**, not reactive executor.

---

### Scenario 2: Student as Teacher (Constraint Correction)

**Why constraint-based feedback**:
- AI suggests generic safe deletion (git branch -D)
- Student corrects based on personal experience
- AI adapts to student's context

**Implementation**:
```
AI suggests both -d and -D deletion strategies.

Student: "I only want -d (safe). In previous project, branch
clutter was a problem. I'll be disciplined about cleanup."

AI adapts: "Understood. Using -d for safety with commit resolution.
You're enforcing your project's discipline standard."

Callout: "What AI learned: Your constraint (branch clutter prevention),
your preference (safe over force-delete)."
```

**Why this works**: Shows student as **domain expert**, teaching AI about project reality.

---

### Scenario 3: Co-Worker Convergence (Performance Documentation Pattern)

**Why convergence is critical**:
- Iteration shows learning isn't unidirectional
- Neither alone has final solution
- Together they create reusable pattern

**Implementation**:
```
Iteration 1: AI suggests "Create two branches, test, merge winner"
Iteration 2: Student says "How do I remember which is faster?"
           AI suggests "Add performance note to commit message"
Iteration 3: Together decide on:
           - Document in commit message: "feat: optimization (5x faster)"
           - Add metrics to PR description
           - Create full performance comparison
           - Review comparison before deciding

Final pattern neither had initially:
- Student didn't think of commit message documentation
- AI didn't know performance metrics were critical
- Together: reusable "document-test-decide" workflow

Callout: "What neither of you had individually: ...Together you created..."
```

**Why this works**: Shows **collaborative intelligence** — iteration improves both.

---

## Validation Against Stage 2 Forcing Functions

### Three Roles Present? ✅

- Scenario 1: AI teaches branch naming → Student learns ✅
- Scenario 2: Student teaches constraints → AI learns ✅
- Scenario 3: Iteration → both learn, converge ✅

### Explicit Learning Callouts? ✅

- "What you learned:" appears 3 times (AI as Teacher sections)
- "What AI learns:" appears 2 times (Student as Teacher sections)
- "What neither of you had individually:" (Convergence section) ✅

### Bidirectional? ✅

- Not "AI suggests, human executes"
- IS "AI suggests, human refines, together improve"
- Both parties adapt based on feedback ✅

### Not Lecture-Style? ✅

- No "Here's how branches work, use AI to implement"
- IS "Discover isolation, then discuss with AI, iterate approach"
- Student remains agent, not passive recipient ✅

---

## Cognitive Load Calibration

### 5 Concepts (A1 Limit)

1. **Branches** — isolation metaphor ("parallel universes")
2. **Branch creation** — `git branch`, `git checkout -b`
3. **Branch switching** — `git switch`, `git checkout`
4. **Merging** — integration, fast-forward merge
5. **Deletion** — cleanup, safe vs force delete

**Verification**: 5 total (not 6, 7, 8...) — exactly at A1 limit ✅

### Heavy Scaffolding

- Each Git command shown with expected output
- Discovery questions: "What do you see?"
- Explicit explanations: "This is branch isolation in action"
- Step-by-step activities, not abstract concepts ✅

### 2 Options Maximum

- `git switch` vs `git checkout` (both equivalent, student chooses) ✅
- Safe deletion `-d` vs force deletion `-D` (explained, not confusing) ✅
- No "3+ ways to do this" (avoids cognitive overload) ✅

---

## Anti-Convergence Safeguards

### Not Generic Tutorial Pattern

**Could converge toward**: "Here's how to use branches: [code] [exercise] done"

**Instead**: Three Roles modeling shows real collaboration, not just command execution

### Differs from Stage 1 Lessons

- Lesson 1-2: Hands-on discovery (execute → observe)
- Lesson 3: Three Roles collaboration (execute → collaborate → improve)

**Modality variation**: ✅ Not repetitive

### Differs from Chapter 7 (Bash)

- Chapter 7: Direct teaching with analogies
- Chapter 8: Hands-on discovery + Three Roles collaboration

**Cross-chapter variety**: ✅ Avoids formulaic chapter pattern

---

## Success Criteria Alignment

### SC-004: 75%+ manage branches without confusion

**Mapping**:
- Part 1 (Activities): Clear execution, isolation confirmed
- Part 3 (Workflow): Complete create → test → merge → delete cycle
- Part 4 (Framework): Decision-making clarity
- **Student learns**: Branches are safe, can't accidentally affect main

### SC-007: Branch workflow <5 minutes

**Mapping**:
- All commands are single-line (not multi-step)
- Part 1 activities: Branch creation, switching — 30 seconds each
- Part 3 activities: Merge, delete — 30 seconds each
- **Student learns**: Branches are quick, easy to test alternatives

### SC-013: 80%+ recognize branches vs commits

**Mapping**:
- Part 4: Explicit "When to branch" vs "When to commit" section
- Decision framework: Ask yourself before AI change
- Scenarios A-C: Pattern recognition practice
- Try With AI Prompt 2: Workflow review (reinforce decision-making)
- **Student learns**: Branches for alternatives, commits for proven work

---

## Content Quality Decisions

### Why "Parallel Universes" Metaphor

- Concrete image helps A1 learners visualize isolation
- "Universe" implies: completely separate, no interference, return to original if unwanted
- Better than technical explanation ("pointer to commit") for A1 tier

### Why Three Roles in Narrative Form

- Realistic dialogue shows how AI interaction actually works
- Student recognizes "Oh, I do this with Claude Code"
- More engaging than abstract explanation

### Why Convergence Iteration 1-2-3

- Shows improvement is incremental, not instantaneous
- Student learns to iterate, not expect perfection
- Realistic modeling of real problem-solving

### Why Part 4 (Trade-offs) After Part 3 (Workflow)

- Students have executed complete workflow
- NOW discuss "when to apply this"
- Decision framework lands after experience (not before)

### Why Part 5 (Reflection) Before Try With AI

- Explicit synthesis of what each role contributed
- Helps student recognize patterns they'll do independently
- Then Part 6-7 (practice) applies this understanding

---

## Implementation Artifacts

### Main Lesson File

**Path**: `book-source/docs/02-AI-Tool-Landscape/08-git-and-github/03-testing-ai-safely-with-branches.md`

**Size**: 525 lines (6 parts, 3 Three Roles scenarios, 6 activities, decision framework, try With AI)

**Structure**:
- YAML frontmatter (stage, cognitive load, skills)
- Opening hook (parallel universe framing)
- 7 major sections (Parts 1-7)
- 6 hands-on activities with expected outputs
- 3 Three Roles scenarios with callouts
- Decision framework (Part 4)
- Pattern recognition (Part 6)
- Try With AI (Part 7)

### Verification Report

**Path**: `LESSON-3-VERIFICATION-REPORT.md`

**Purpose**: Detailed validation of:
- Constitutional compliance (all 7 principles)
- Stage 2 Three Roles (all 3 roles present)
- Cognitive load (exactly 5 concepts, A1 limit)
- Functional requirements (FR-010 through FR-014)
- Success criteria mapping (SC-004, SC-007, SC-013)
- Hands-on activities (all 12 tasks from Phase 4)

---

## Key Learnings for Future Stage 2 Lessons

### What Makes Three Roles Work

1. **Explicit callouts**: "What X learned" prevents implicit knowledge loss
2. **Realistic scenarios**: Students recognize themselves in the dialogue
3. **Iteration modeling**: Shows improvement isn't one-shot, it's collaborative
4. **Concrete decisions**: Merge strategy, performance documentation, naming conventions — not abstract concepts

### How to Structure Stage 2 Teaching

1. Foundation first (Stage 1 manual learning)
2. THEN introduce AI (not before student understands manually)
3. Three scenarios minimum: Teacher (AI), Student (you), Convergence (together)
4. Explicit reflection: Summarize what each party learned
5. Application practice: Scenarios A-C showing when to use knowledge

### Cognitive Load at A1/A2

- 5-7 concepts maximum PER LESSON (not per section)
- Heavy scaffolding means every command shown with output
- 2 options maximum (not "3 ways to do this")
- Heavy metaphors (parallel universes, not Git object model)

### Anti-Convergence Vigilance

- Stage 2 temptation: Fall back to "AI as tool" (tutorial pattern)
- Prevention: Write Three Roles scenarios EXPLICITLY, not implicitly
- Validation: Check "What X learned" callouts exist
- Test: Remove one role, lesson breaks → you knew it was essential

---

## Reflection: Content-Implementer Reasoning Process

### How I Avoided Generic Tutorial Pattern

1. **Recognized temptation**: "Just explain branches, show code, do exercise"
2. **Activated Stage 2 mode**: "This is AI COLLABORATION, not instruction"
3. **Applied Three Roles framework**: Each role must be explicit scenario
4. **Added callouts**: "What X learned" makes learning visible
5. **Modeled convergence**: Iteration shows improvement is joint

### How I Calibrated Cognitive Load

1. **Counted concepts**: 5 exactly (branch, create, switch, merge, delete)
2. **Heavy scaffolding**: Every command with expected output
3. **Metaphors**: "Parallel universes" (A1-friendly) not Git internals
4. **Sequential activities**: Build one on previous, not all at once

### How I Planned Anti-Convergence

1. **Compared to Lesson 1-2**: "They had hands-on discovery. This needs AI collaboration addition."
2. **Compared to Chapter 7**: "Bash was direct teaching. Git is discovery + collaboration."
3. **Modality variety**: Observe (Part 1) → Collaborate (Part 2) → Execute (Part 3) → Analyze (Part 4) → Reflect (Part 5) → Practice (Part 6-7)

---

## Connections to Chapter Architecture

### How Lesson 3 Serves Stage 2

- **Lesson 1-2** (Stage 1): Manual Git foundation (init, add, commit, restore, reset)
- **Lesson 3** (Stage 2): AI collaboration with branches + Three Roles
- **Lesson 4-5** (Stage 2): GitHub + PRs + AI collaboration patterns
- **Lesson 6** (Stage 3): Reusable git-workflow.md from patterns
- **Lesson 7** (Stage 4): Capstone with spec-driven approach + Agent HQ awareness

### How Lesson 3 Enables Lesson 6

- Lesson 3 establishes patterns:
  - "Commit before AI change" (Pattern 1 in Lesson 6)
  - "Branch for testing alternatives" (Pattern 2 in Lesson 6)
  - "Push for backup" (Pattern 3 in Lesson 6)
- Lesson 6 students document these from experience, then apply to new scenarios

### How Lesson 3 Enables Lesson 7 (Capstone)

- Lesson 3 teaches branch workflow
- Lesson 7 capstone uses branches for feature testing
- Student doesn't need re-teaching, just application in larger context

---

## Validation Checklist: All Passing

- ✅ 5 concepts (A1 limit)
- ✅ Heavy scaffolding (step-by-step with expected outputs)
- ✅ Three Roles demonstrated (all 3 roles, explicit callouts)
- ✅ Bidirectional learning (AI teaches, student teaches, convergence)
- ✅ Stage 2 modality (collaboration, not instruction)
- ✅ Hands-on discovery (execute → observe → understand)
- ✅ Success criteria mapped (SC-004, SC-007, SC-013)
- ✅ Functional requirements covered (FR-010 through FR-014)
- ✅ Anti-convergence validation (differs from L1-2 and Chapter 7)
- ✅ Try With AI section (3 prompts, expected outcomes)
- ✅ YAML frontmatter (stage, cognitive load, skills)
- ✅ Constitutional compliance (all 7 principles)

---

## Summary

**Task**: Implement Lesson 3 (Testing AI Safely with Branches) for Chapter 8

**Challenge**: Teach branches + demonstrate Three Roles + avoid generic tutorial pattern

**Solution**:
1. Structure in 7 parts (observe → collaborate → execute → analyze → reflect → practice → extend)
2. Three Roles scenarios with explicit "What X learned" callouts
3. Convergence modeling showing iteration improves both understanding
4. Cognitive scaffolding (5 concepts, heavy support, A1-friendly)
5. Anti-convergence variety (modality differs from L1-2 and Chapter 7)

**Result**: ✅ Lesson 3 complete, Stage 2 compliant, ready for student implementation

**Quality**: Constitutional compliance + pedagogical effectiveness + functional completeness

---

**PHR Complete**: 2025-01-17
**Next**: Lesson 4 (Cloud Backup & Portfolio) — Stage 2 GitHub integration with Three Roles
