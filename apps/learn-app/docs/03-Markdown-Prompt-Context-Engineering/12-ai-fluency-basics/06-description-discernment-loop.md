---
sidebar_position: 6
title: "The Description-Discernment Loop"
description: "Master the iterative workflow of describing intent to AI, evaluating outputs, and refining toward convergence"
keywords: [description, discernment, iteration, refinement, AI collaboration, prompt engineering, feedback loop]
chapter: 12
lesson: 6
duration_minutes: 35

# HIDDEN SKILLS METADATA
skills:
  - name: "Executing the Description-Discernment Loop"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can execute a complete 5-iteration loop starting from vague description through convergence on production-quality output"

  - name: "Identifying Loop Phases"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can identify whether current interaction is Description phase (communicating intent) or Discernment phase (evaluating output)"

  - name: "Recognizing Loop Termination Criteria"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can determine when to continue iterating versus when diminishing returns indicate loop completion"

  - name: "Designing Refinement Prompts"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can write prompts that incorporate specific feedback from Discernment phase into improved Description"

  - name: "Tracking Quality Improvement"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can document and compare output quality across iterations to demonstrate measurable improvement"

learning_objectives:
  - objective: "Apply the Description-Discernment iterative loop to real tasks"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Complete 5-iteration loop producing measurable quality improvement"

  - objective: "Identify when to apply Description versus Discernment"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Label phases correctly in interaction transcript"

  - objective: "Recognize loop patterns in real workflows"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Analyze workflow trace to identify transition points between phases"

  - objective: "Design prompts that enable effective loops"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Write refinement prompts that address specific gaps identified in Discernment"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (loop structure, phase identification, transition triggers, termination criteria, quality tracking) within B1 limit (7-10 concepts)"

differentiation:
  extension_for_advanced: "Apply loop to multi-file refactoring project; track convergence metrics quantitatively across 10+ iterations"
  remedial_for_struggling: "Focus on single-file loop with explicit phase labels; provide sentence starters for refinement prompts"
---

# The Description-Discernment Loop

You write a prompt. AI generates output. You look at it, think "not quite right," and try again.

You just executed the most fundamental pattern in AI collaboration: the **Description-Discernment Loop**. Every productive interaction with AI follows this rhythm. Understanding it transforms you from someone who gets lucky sometimes into someone who converges reliably on quality outputs.

The loop isn't complicated. But naming it and understanding its phases changes how you approach AI work. Instead of hoping for perfect outputs on the first try, you design for iteration. Instead of vaguely feeling that something is wrong, you develop specific feedback that guides the next attempt.

This lesson teaches you to see the loop, execute it deliberately, and know when you've arrived.

## The Core Loop: A Mental Model

The Description-Discernment Loop has five phases that repeat until convergence:

```
       ┌─────────────────────────────────────────────┐
       │                                             │
       ▼                                             │
┌─────────────┐     ┌─────────────┐     ┌───────────┴───┐
│  DESCRIBE   │────▶│  GENERATE   │────▶│   EVALUATE    │
│   Intent    │     │   Output    │     │   Quality     │
└─────────────┘     └─────────────┘     └───────────────┘
       ▲                                       │
       │                                       ▼
       │                               ┌─────────────┐
       │                               │   REFINE    │
       │                               │   Prompt    │
       │                               └──────┬──────┘
       │                                      │
       │         ┌─────────────┐              │
       └─────────┤   REPEAT    │◀─────────────┘
                 │  Or Finish  │
                 └─────────────┘
```

**Description Phase (Lessons 3 and 5)**: You communicate intent to AI. This includes your prompts, context files, examples, and constraints.

**Generation Phase**: AI produces output based on your description. This is the part you don't control directly.

**Discernment Phase (Preview of Lesson 7)**: You evaluate the output. Is it correct? Does it match your intent? What's missing?

**Refinement Phase**: Based on your evaluation, you modify your description. Add constraints. Provide examples. Clarify ambiguities.

**Repeat or Finish**: Continue until success criteria met, or stop when returns diminish.

The key insight: **Description and Discernment are complementary skills.** Strong description reduces the number of iterations needed. Strong discernment identifies exactly what to fix. Master both, and you converge faster.

## When to Apply Each Phase

Recognizing which phase you're in helps you apply the right skill at the right time.

### The Description Phase

You're in Description when you're **communicating intent to AI**. Signs include:

- Writing or modifying a prompt
- Adding context files or examples
- Specifying constraints or requirements
- Structuring your input for clarity

**Description skills to apply**:

| Technique | When to Use | Example |
|-----------|-------------|---------|
| Add constraints | Output too broad | "Maximum 200 words, focused on security implications" |
| Provide examples | AI misunderstands format | "Format like this: [example]" |
| Specify non-goals | AI includes unwanted content | "Do NOT cover deployment; focus only on local development" |
| Add context | AI lacks domain knowledge | Include relevant documentation or specifications |
| Break into steps | Task too complex | "First, analyze the problem. Then, propose three solutions." |

### The Discernment Phase

You're in Discernment when you're **evaluating AI output**. Signs include:

- Reading through generated content
- Comparing output against requirements
- Identifying gaps, errors, or mismatches
- Deciding what needs to change

**Discernment skills to apply**:

| Evaluation Focus | Questions to Ask | What to Look For |
|-----------------|------------------|------------------|
| Correctness | "Is this accurate?" | Factual errors, logical flaws, bugs in code |
| Completeness | "Does this cover everything?" | Missing sections, overlooked requirements |
| Relevance | "Does this stay on topic?" | Tangents, unnecessary content, scope creep |
| Quality | "Is this production-ready?" | Polish, clarity, professional standards |
| Intent Match | "Is this what I actually wanted?" | Misinterpretation, wrong assumptions |

### Transition Triggers

Knowing when to switch phases prevents common mistakes:

**Switch from Description to Discernment when**:
- AI has generated output
- You're reading rather than writing
- You're forming opinions about quality

**Switch from Discernment to Description when**:
- You've identified specific gaps
- You know what to change
- You're ready to communicate new requirements

**Common Mistake**: Staying too long in one phase. Endless refinement of prompts without testing them (Description paralysis). Or repeatedly reading output without making concrete changes (Discernment paralysis).

## A Complete Loop: Five Iterations in Practice

Let's walk through a real example: creating a specification for a user authentication feature. Watch how each iteration improves quality through deliberate Description-Discernment cycles.

### Iteration 1: Vague Description

**Description** (your prompt):

```
Write a spec for user authentication.
```

**Generation** (AI output):

```markdown
# User Authentication Specification

## Overview
This document specifies user authentication for the application.

## Requirements
- Users should be able to log in
- Users should be able to log out
- Passwords should be secure

## Implementation
Use a standard authentication library.
```

**Discernment** (your evaluation):

| Criterion | Score | Gap Identified |
|-----------|-------|----------------|
| Completeness | 2/10 | Missing: password requirements, session handling, error cases |
| Specificity | 1/10 | Vague phrases: "should be secure," "standard library" |
| Actionable | 1/10 | Developer couldn't implement from this |

**Refinement insight**: Specification lacks concrete requirements. Need to add specific criteria.

---

### Iteration 2: Adding Specificity

**Description** (refined prompt):

```
Write a detailed specification for user authentication.

Include:
- Password requirements (length, complexity)
- Session management (duration, invalidation)
- Error handling (invalid credentials, locked accounts)
- Security considerations (rate limiting, encryption)
```

**Generation** (AI output):

```markdown
# User Authentication Specification

## Password Requirements
- Minimum 8 characters
- Must contain: uppercase, lowercase, number
- Optional: special character

## Session Management
- Sessions last 24 hours
- Invalidate on logout
- Invalidate on password change

## Error Handling
- Invalid credentials: "Invalid email or password"
- Locked account: Account locks after 5 failed attempts

## Security
- Passwords hashed with bcrypt
- Rate limit: 5 attempts per minute
- HTTPS required for all auth endpoints
```

**Discernment** (your evaluation):

| Criterion | Score | Gap Identified |
|-----------|-------|----------------|
| Completeness | 5/10 | Missing: registration flow, forgot password, multi-device |
| Specificity | 6/10 | Better, but some numbers seem arbitrary |
| Actionable | 5/10 | Closer, but lacking acceptance criteria |

**Refinement insight**: Covered what I asked for, but I forgot key flows. Need to think about complete user journey.

---

### Iteration 3: Expanding Scope

**Description** (refined prompt):

```
Write a detailed specification for user authentication.

Cover the complete user journey:
1. Registration (new user signup)
2. Login (existing user access)
3. Password reset (forgot password flow)
4. Session management
5. Logout

For each flow, include:
- User actions
- System responses
- Error cases
- Acceptance criteria

Security requirements:
- Password: 12+ chars, complexity requirements
- bcrypt with cost factor 12
- Rate limiting: 5/min per IP
- Session: JWT with 1-hour access, 7-day refresh
```

**Generation** (AI output):

```markdown
# User Authentication Specification

## 1. Registration Flow

### User Actions
1. User navigates to /register
2. User enters: email, password, confirm password
3. User clicks "Create Account"

### System Responses
- **Success**: Create account, send verification email, redirect to /verify
- **Email exists**: Display "Email already registered"
- **Password mismatch**: Display "Passwords do not match"

### Acceptance Criteria
- [ ] New user can create account with valid email
- [ ] Duplicate emails are rejected
- [ ] Verification email sent within 30 seconds
- [ ] Account cannot login until email verified

## 2. Login Flow

### User Actions
1. User navigates to /login
2. User enters email and password
3. User clicks "Sign In"

### System Responses
- **Success**: Issue JWT, redirect to /dashboard
- **Invalid credentials**: Display generic error
- **Unverified email**: Prompt to verify

### Acceptance Criteria
- [ ] Valid credentials grant access
- [ ] Invalid credentials show generic error (no hints)
- [ ] Account locks after 5 failed attempts

[... continues with Password Reset, Session Management, Logout ...]

## Security Requirements

### Password Policy
- Minimum 12 characters
- Must contain: 2+ of (uppercase, lowercase, number, special)
- Cannot contain email or common words

### Hashing
- Algorithm: bcrypt
- Cost factor: 12
- Salt: auto-generated per password

### Rate Limiting
- 5 attempts per minute per IP
- Progressive backoff: 1min, 5min, 15min, 1hour
- Lockout notification sent to user email

### Session Tokens
- Access token: JWT, 1-hour expiry, contains user_id only
- Refresh token: opaque, 7-day expiry, stored in httpOnly cookie
- Revocation: stored in Redis blocklist until expiry
```

**Discernment** (your evaluation):

| Criterion | Score | Gap Identified |
|-----------|-------|----------------|
| Completeness | 8/10 | Missing: OAuth, remember me, multi-device sessions |
| Specificity | 8/10 | Good concrete numbers, but some edge cases unclear |
| Actionable | 8/10 | Developer could implement most of this |

**Refinement insight**: Much better. Quality improvement is slowing. But OAuth is important for our use case. Need to add it.

---

### Iteration 4: Final Additions

**Description** (refined prompt):

```
This specification is good. Please add:

1. OAuth integration section (Google, GitHub)
2. "Remember me" functionality
3. Multi-device session management (view/revoke sessions)
4. Edge case: what happens if user changes email?

Keep all existing content. Add these sections using the same format.
```

**Generation** (AI output adds the requested sections with same quality level)

**Discernment** (your evaluation):

| Criterion | Score | Gap Identified |
|-----------|-------|----------------|
| Completeness | 9/10 | Core flows covered; edge cases addressed |
| Specificity | 9/10 | Clear, testable requirements |
| Actionable | 9/10 | Developer can implement from this |

**Refinement insight**: Quality improvement from iteration 3 to 4 was smaller (8 to 9) than from 2 to 3 (5 to 8). Diminishing returns.

---

### Iteration 5: Polish and Confirmation

**Description** (final prompt):

```
Review this specification for:
1. Any inconsistencies between sections
2. Missing error codes
3. Ambiguous language that could be interpreted multiple ways

Make corrections inline. Highlight any architectural decisions
that should be reviewed by a senior engineer.
```

**Generation** (AI output adds error codes, flags decisions for review)

**Discernment** (your evaluation):

| Criterion | Score | Improvement |
|-----------|-------|-------------|
| Completeness | 9.5/10 | +0.5 from previous |
| Specificity | 9.5/10 | +0.5 from previous |
| Actionable | 10/10 | +1 from previous |

**Decision**: Quality improvement less than 5% per iteration. **Loop complete.**

### Quality Progression Summary

| Iteration | Completeness | Specificity | Actionable | Total |
|-----------|--------------|-------------|------------|-------|
| 1 | 2 | 1 | 1 | 4/30 |
| 2 | 5 | 6 | 5 | 16/30 |
| 3 | 8 | 8 | 8 | 24/30 |
| 4 | 9 | 9 | 9 | 27/30 |
| 5 | 9.5 | 9.5 | 10 | 29/30 |

**Pattern to notice**: The biggest improvements happened between iterations 2-3 (from 16 to 24 points). Later iterations showed diminishing returns. This is typical: early iterations fix major gaps; later iterations polish.

## Loop Termination: When to Stop

Knowing when to stop iterating is as important as knowing how to iterate.

### Success Criteria Met

**Primary termination condition**: Output meets all requirements.

Before starting a loop, define success criteria:

```markdown
## Success Criteria for This Specification
- [ ] All 5 user flows covered with error cases
- [ ] Security requirements match OWASP guidelines
- [ ] Acceptance criteria are testable
- [ ] Senior engineer approves architecture decisions
```

When all boxes are checked, you're done.

### Diminishing Returns

**Secondary termination condition**: Improvements per iteration drop below threshold.

| Improvement Rate | Action |
|------------------|--------|
| >20% per iteration | Continue iterating |
| 10-20% per iteration | Consider stopping, check if major gaps remain |
| 5-10% per iteration | Likely diminishing returns; stop unless critical gap |
| Under 5% per iteration | Stop; polish isn't worth more iterations |

**How to measure**: Use your evaluation scores. If iteration N scores 27/30 and iteration N+1 scores 28/30, that's a 3.7% improvement. Likely time to stop.

### Time Budget Exceeded

**Practical termination condition**: You've spent allocated time.

Before starting, set a time budget:

```
Task: Write auth specification
Time budget: 45 minutes
```

If you hit 45 minutes and have an 8/10 specification, that's often better than spending 90 minutes for a 9/10. Perfect is the enemy of done.

### Escape Conditions

Sometimes you need to exit the loop early:

| Condition | Signal | Action |
|-----------|--------|--------|
| Wrong approach | Iterations aren't improving | Step back, reconsider strategy |
| Missing capability | AI can't do what you need | Switch tools or do manually |
| Scope creep | Requirements growing each iteration | Freeze scope, finish current |
| Context degradation | AI repeating errors from early iterations | New conversation, fresh context |

## Designing Prompts for Effective Loops

Some prompts are designed for single-shot use. Others are designed for iteration. The difference matters.

### Single-Shot Prompt Pattern

```
Generate a complete, final user authentication specification
covering all aspects of registration, login, and security.
```

**Problem**: If output isn't perfect, you have to regenerate everything.

### Loop-Friendly Prompt Pattern

```
Generate a user authentication specification.

Focus on: [current focus area]

This is iteration [N] of [M]. Previous feedback:
- [Gap 1 from discernment]
- [Gap 2 from discernment]

Success criteria remaining:
- [ ] Unchecked criterion 1
- [ ] Unchecked criterion 2
```

**Advantage**: Each iteration builds on previous. Feedback is explicit. Progress is tracked.

### Prompt Templates for Each Loop Phase

**Initial Description Template**:

```
Create a [deliverable] for [purpose].

Focus on these aspects first:
1. [Most important element]
2. [Second priority]
3. [Third priority]

Format: [How you want output structured]

This is iteration 1. We'll refine together.
```

**Refinement Prompt Template**:

```
Good progress. The [aspect that worked] is solid.

Please improve:
1. [Specific gap]: [How to fix]
2. [Specific gap]: [How to fix]

Keep: [What to preserve from current version]

Add: [New element to include]
```

**Finalization Prompt Template**:

```
This is nearly complete. Final review:

1. Check for inconsistencies between [section A] and [section B]
2. Verify all [specific elements] are present
3. Flag any [type of decision] for human review

Make only necessary corrections. Explain any changes made.
```

## Common Loop Patterns in Practice

Different tasks follow different loop patterns:

### The Expanding Loop

```
Iteration 1: Core concept only
Iteration 2: Add first layer of detail
Iteration 3: Add second layer of detail
Iteration 4: Fill edge cases
Iteration 5: Polish
```

**Best for**: Documentation, specifications, designs

### The Narrowing Loop

```
Iteration 1: Generate multiple options
Iteration 2: Evaluate and eliminate options
Iteration 3: Deepen best option
Iteration 4: Finalize chosen approach
```

**Best for**: Creative tasks, problem-solving, architecture decisions

### The Fix-and-Extend Loop

```
Iteration 1: Initial generation
Iteration 2: Fix critical errors
Iteration 3: Extend to cover more cases
Iteration 4: Fix new errors from extension
Iteration 5: Final fixes
```

**Best for**: Code generation, complex implementations

### The Parallel Loop

```
Branch A, Iteration 1-3: Approach A
Branch B, Iteration 1-3: Approach B
Merge: Compare branches, combine best elements
Final: Polish merged result
```

**Best for**: When optimal approach is unclear; want to explore alternatives

## Try With AI

Use your AI companion to practice the Description-Discernment Loop.

### Prompt 1: Execute a 5-Iteration Loop

```
I want to practice the Description-Discernment Loop. Let's create
a README for a personal project.

Start with this vague description:
"Write a README for my project."

After your response, I'll evaluate it using Completeness,
Specificity, and Actionability (each 1-10). Then I'll give you
refined requirements. We'll iterate 5 times.

Track our progress with a quality table after each iteration.
Ready? Generate iteration 1.
```

**What you're learning**: Deliberate practice of the full loop. By tracking quality scores, you'll see where the biggest improvements happen and when diminishing returns set in.

### Prompt 2: Identify Loop Phases

```
Here's a transcript of an AI interaction. Help me identify which
phase each part belongs to:

PHASE 1: [I wrote a prompt asking for help with error handling]
PHASE 2: [AI generated code with try/except blocks]
PHASE 3: [I read the code and noticed it didn't handle network errors]
PHASE 4: [I asked AI to add network error handling specifically]
PHASE 5: [AI updated the code]
PHASE 6: [I tested it and found it worked]

Label each phase as: Description, Generation, Discernment, or Refinement.
Explain your reasoning for each label.
```

**What you're learning**: Phase recognition. Being able to name what you're doing helps you apply the right skills at the right time.

### Prompt 3: Track Quality Improvement

```
Let's measure quality improvement across a real task.

Task: Create a study schedule for learning [topic you're learning].

We'll do 4 iterations. After each, rate the output on:
- Completeness (1-10): Does it cover all study areas?
- Specificity (1-10): Are times and activities concrete?
- Practicality (1-10): Could I actually follow this?

Calculate percentage improvement between iterations.
Identify which iteration gave the biggest improvement and why.

Start with: "Create a study schedule for [your topic]."
```

**What you're learning**: Quantitative tracking of loop effectiveness. You'll develop intuition for when to iterate versus when to stop.

### Safety Note

As you practice the loop, remember: the goal is convergence on quality, not perfection. If you find yourself on iteration 10+ with marginal improvements, step back. Your time might be better spent on the next task than polishing this one further.
