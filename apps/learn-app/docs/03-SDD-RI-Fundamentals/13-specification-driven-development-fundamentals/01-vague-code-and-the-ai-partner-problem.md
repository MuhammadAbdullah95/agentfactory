---
title: "Vague Code and the AI Partner Problem"
chapter: 30
lesson: 1
duration_minutes: 65

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Problem Identification"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify vagueness in requirements and explain its impact on AI-generated code quality and iteration costs"

  - name: "AI Communication Clarity"
    proficiency_level: "B1"
    category: "Soft"
    bloom_level: "Analyze"
    digcomp_area: "Communication & Collaboration"
    measurable_at_this_level: "Student can recognize the gap between conversational intent and machine-executable instructions; understand AI literal-mindedness"

  - name: "Specification Understanding"
    proficiency_level: "A1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain the core problem that Specification-Driven Development solves and why clarity matters for AI collaboration"

learning_objectives:
  - objective: "Identify vagueness in requirements and quantify its impact on AI-generated code (time, rework, debugging cycles)"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Analyze vague vs. clear prompts and predict iteration costs"

  - objective: "Recognize the gap between conversational intent and machine-executable instructions through hands-on experience"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Compare vague prompt output vs. collaborative spec output"

  - objective: "Understand the core problem that Specification-Driven Development solves and why it emerged in 2025"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Explain SDD value proposition in student's own words"

cognitive_load:
  new_concepts: 4
  assessment: "4 new concepts (foundation vs interior metaphor, vibe coding, specification clarity, collaborative spec writing) within A2-B1 limit of 7-10 ✓"

differentiation:
  extension_for_advanced: "Analyze cost-benefit tradeoffs of spec-first vs. code-first across different project types (prototype vs. production); design decision framework"
  remedial_for_struggling: "Focus on Sandra vs Alex contrast; use house-building analogy (foundation vs interior) as visual anchor for the concept"

# Generation metadata
generated_by: "content-implementer v3.0.0"
source_spec: "specs/book/chapter-32-sdd-fundamentals/spec.md"
created: "2025-01-15"
last_modified: "2026-01-07"
git_author: "Claude Code"
workflow: "format-standardization"
version: "2.0.0"
---

# Vague Code and the AI Partner Problem

Imagine you're building a house. You hire a contractor and say, "Build me something modern with lots of natural light." The contractor delivers exactly that—an open floor plan with floor-to-ceiling windows. Beautiful.

But when you move in, problems emerge. The foundation wasn't designed for the soil type. The plumbing can't handle more than two showers running simultaneously. The electrical panel is undersized for modern appliances. The house *looks* perfect, but it wasn't *engineered* for real life.

This is the difference between **interior design** and **architecture**. One focuses on what you see; the other focuses on what holds everything together.

**The same distinction exists in AI-assisted software development.**

## Sandra's Volunteer App: A Cautionary Tale

Sandra, a non-technical founder, used AI to build a volunteer coordination app for her nonprofit. The AI delivered quickly—a polished interface where volunteers could sign up for shifts. Sandra was thrilled. The demo looked professional.

Then launch day arrived. Fifty volunteers tried to sign up for the same shift simultaneously. The app:
- Assigned the same slot to multiple people
- Lost some registrations entirely
- Froze when volunteers tried to swap shifts
- Crashed when the database couldn't handle concurrent writes

Sandra's AI companion had built beautiful *interior design*—the UI, the forms, the basic flow. But there was no *foundation*—no database transactions, no concurrency handling, no error recovery.

The AI wasn't incompetent. Sandra never *asked* for concurrent user handling. She said "build a volunteer sign-up app," and the AI built exactly that—for a single user at a time.

**This gap between what you describe and what production systems require is the root of every failed AI coding session.**

This lesson explains why this happens and introduces Specification-Driven Development—the practice of building foundations before interiors.

---

## The Problem with Vibe Coding

The emergence of powerful AI coding agents has highlighted a critical problem in how we communicate intent to machines.

**Vibe coding** is developing software by intuition or conversational suggestion. You describe your goal loosely, get code back, and hope it matches what you envisioned. It's called "vibe" coding because you're coding by feel, not by precision.

Here's the pattern:

1. **You describe a feature** (loosely, conversationally)
   - "Build me a login system"
   - "Add a search feature to my blog"
   - "Create a payment processor"

2. **Your AI companion generates code** (following the pattern it recognizes)
   - The code is syntactically correct
   - The code implements what you said literally
   - The code *looks* complete
   - Made 50+ implicit decisions without your input.

3. **You run it and discover** the code doesn't do what you *meant*
   - Missing error handling
   - No password reset
   - No input validation
   - No rate limiting on login attempts
   - No encryption for sensitive data

4. **You iterate** (in frustration)
   - "Add password reset"
   - "Handle invalid input"
   - "Add rate limiting"
   - Each iteration: one more fix, one more conversation cycle

Vibe coding can be great for rapid prototypes—throw something together quickly, see if the concept works. But it's **fragile** when building production systems, integrating with existing code, or handling sensitive data.

### Why This Happens

The problem isn't that AI coding agents are poor programmers. They're actually remarkably good.

The problem is how we're using them.

We treat AI agents like search engines:
- Search engines: "Find me pictures of cats" → Get pictures of cats (good enough)
- Coding: "Build me a login system" → Get login code (but missing 30% of real requirements)

But AI coding agents aren't search engines. **They're more like literal-minded pair programmers.**

Pair programmers need clarity. They thrive on:
- **Explicit requirements** (not implied assumptions)
- **Structured context** (not loose descriptions)
- **Clear constraints** (not open-ended possibilities)

Without these, even brilliant pair programmers can only infer intent from patterns they've seen before. And when your system is unique—when it has special requirements, edge cases, or domain-specific rules—patterns from general code examples won't suffice.

---

## The Cost of Skipping Foundations

Sandra's situation isn't unusual. Studies show that **85% of AI projects fail due to data and requirement issues**—not because AI can't code, but because humans don't specify what they actually need.

The pattern repeats across industries:

| What You Say | What AI Builds | What You Actually Needed |
|--------------|----------------|--------------------------|
| "Build a sign-up app" | Single-user form flow | Multi-user with concurrency handling |
| "Add a payment feature" | Basic Stripe integration | PCI compliance, refunds, webhooks, audit logs |
| "Create a chat system" | Real-time messages | Message history, read receipts, offline sync, moderation |

Each missing requirement becomes a production incident, a debugging session, or (worse) a security vulnerability. Research indicates that **45% of AI-generated code contains OWASP Top 10 vulnerabilities** when built from vague prompts without security specifications.

**The time you "save" by skipping specification work gets multiplied 5-10x in iteration cycles.**

#### 💬 AI Colearning Prompt
> "Why can't AI coding agents infer what I mean when I say 'build a volunteer sign-up app'? What's the difference between what AI hears literally versus what I assume is obvious?"

---

## The Solution: Build the Foundation First

Now imagine Sandra had taken a different approach—one where she worked with her AI companion to build a clear specification BEFORE generating any code.

This isn't just "AI answers your questions." This is **bidirectional learning**—both you and AI improve through collaboration.

### Step 1: Discover Missing Requirements

Instead of writing specs alone, you start with intent and let AI help you think through the details.

Tell your companion:

```
Help me write a specification for a login system. I want users to create accounts
and authenticate securely, with account recovery support.

What should I specify to make this complete? What questions should I answer upfront
to avoid implementation surprises?
```

**Your companion responds**:

> "To make this specification complete, you should answer:
>
> 1. **Email verification**: Should users verify email before login is enabled?
> 2. **Rate limiting**: How many failed login attempts before blocking?
> 3. **Session management**: How long should sessions last? Refresh tokens?
> 4. **Password hashing**: Which algorithm? (bcrypt, argon2, scrypt?)
> 5. **Password reset**: Email or SMS? Token expiration time?
> 6. **Edge cases**: What if user tries to reset password for non-existent email?"

**Reflect**: Which of these questions surprised you? Which requirements did you initially overlook?

### Step 1.5: Provide Your Constraints

Now you refine AI's generic suggestions with YOUR specific constraints.

You respond:

```
Good questions. Here are my constraints:

1. Email verification: YES, required before login
2. Rate limiting: 5 attempts per IP per minute (we're a healthcare app, security is critical)
3. Session management: 24-hour sessions, no refresh (users log in daily anyway)
4. Password hashing: bcrypt cost 12 (our security policy mandates this)
5. Password reset: EMAIL only (no SMS, we don't collect phone numbers)
6. Password reset for non-existent email: Return "success" anyway (don't leak which emails exist)
```

**Your companion responds**:

> "Got it. A few clarifications based on your healthcare context:
>
> - Should failed login attempts be logged for audit? (HIPAA compliance)
> - Do passwords need minimum complexity rules? (12 chars minimum, special chars?)
> - Should we implement 2FA given the security requirements?
> - What about session timeout after inactivity?"

**Notice**: Your companion picked up on your healthcare context and raised compliance questions. Your constraints shaped its follow-up questions.

### Step 2: Converge Together (Iterative Refinement)

Now watch the convergence loop—both you and AI refine the spec through dialogue.

**You respond to AI's HIPAA question:**

```
Yes, log all failed attempts with timestamp, IP, and attempted email (for audit trail).
Password complexity: minimum 12 chars, at least one uppercase, one number, one special char.
2FA: Not in v1 (out of scope), but design API to support it later.
Session timeout: 15 minutes of inactivity.
```

**Your companion responds**:

> "Perfect. I've incorporated those constraints. One edge case I noticed: what happens if someone requests password reset multiple times before the first token expires? Should we:
>
> A. Invalidate previous tokens (only latest works)
> B. Allow multiple valid tokens simultaneously
> C. Rate limit reset requests (e.g., max 3 per hour)"

**You respond:**

```
Option A—invalidate previous tokens. We don't want multiple valid reset links floating around.
Also add rate limiting: max 3 reset requests per email per hour.
```

**Your companion:** will generate the final spec.

Through 3 rounds of conversation:
1. Your companion suggested questions you hadn't considered
2. You provided domain-specific constraints and context
3. Together, you discovered edge cases and refined requirements

This is **collaborative specification**—neither you nor your companion could have written this spec alone. You brought domain knowledge (healthcare context, security requirements). Your companion brought systematic thinking (edge cases, best practices). Together, you created a production-ready specification.

#### 💬 AI Colearning Prompt
> "Explain why the specification we just built collaboratively is better than what either a human or AI could write alone. What did each partner contribute that the other couldn't?"

---

## Generate Code From the Collaborative Spec

Now that you and your companion have built a clear specification together, ask for implementation:

```
Based on the login system specification we just created, generate the Python code
with all the requirements we discussed.
```

**Watch what happens:**

Your companion:
- ✅ Understands email requirement (not username)
- ✅ Implements bcrypt hashing (not just SHA-256)
- ✅ Adds rate limiting logic
- ✅ Adds email verification workflow
- ✅ Implements reset tokens with expiration
- ✅ Generates code that's production-ready, not toy code

### Compare the Results

The first code (from vague prompt): needs 10+ iterations
The second code (from clear spec): works correctly on first try

---

## The Aha Moment: Alex's Approach

Remember Sandra's volunteer app that crumbled under real users? Now consider Alex, another non-technical founder building something similar.

Alex started the same way—describing the app to an AI companion. But before accepting any code, Alex asked: "What questions should I answer to make this specification complete? What could go wrong when 50 people use this simultaneously?"

The AI responded with questions about concurrency, database transactions, error handling, and edge cases. Alex spent 45 minutes in dialogue, answering questions and making decisions. Then the AI generated code.

**Alex's launch day**: The same 50 volunteers signed up. The app handled concurrent requests gracefully. When two people tried to claim the same slot, one got a clear "slot just taken" message instead of silent data corruption. The foundation held.

**The difference wasn't AI capability—both used the same tools.** The difference was whether they built the foundation first.

### The Pattern

| Sandra's Approach (Interior First) | Alex's Approach (Foundation First) |
|------------------------------------|-------------------------------------|
| "Build me a volunteer app" | "Help me specify a volunteer app" |
| AI makes 50+ hidden assumptions | AI surfaces 50+ questions to answer |
| Demo looks great | Spec looks thorough |
| Production fails | Production succeeds |

**Key insight**: AI helps you write BETTER specifications by:
- Asking clarifying questions you didn't consider
- Identifying edge cases and concurrency issues
- Suggesting standard patterns and best practices
- Catching ambiguities before they become bugs

**Specifications become clear through collaborative dialogue, not solo effort.**

#### 🤝 Practice Exercise

> **Ask your AI**: "Help me write a specification for a user registration system with email verification. What questions should I answer upfront to avoid implementation surprises? What edge cases should I consider?"

**Expected Outcome**: Your AI will ask clarifying questions (password requirements? rate limiting? email service? token expiration?) that reveal gaps in your initial thinking. This dialogue produces a complete specification collaboratively.

---

## Why This Matters: Foundation Before Interior

The house-building metaphor isn't just an analogy—it's a mindset shift.

> **Specification quality determines implementation quality.**

Sandra focused on what users would *see* (the interior). Alex focused on what would *hold everything together* (the foundation). Both used AI. Only one succeeded in production.

This pattern applies whether your implementation partner is an AI agent or a human colleague. But when you're working with AI agents—which can't read minds, can't infer context, can't guess at unstated requirements—**specification becomes even more critical.**

The future of AI-assisted development isn't about prompting better. It's about **specifying better**. The developers who thrive will be those who know how to collaborate with AI on foundations before asking for interiors.

**This is Specification-Driven Development. And in the age of AI agents, it's the way serious work gets done.**

---

## Try With AI

Ready to experience the difference between vague and clear specifications? Here are four prompts to explore:

**🔍 Explore the Problem:**
> "Show me two versions of a 'build a search feature' prompt: one vague (like I'd naturally write) and one clear (with all details specified). Then explain what gaps the vague version has."

**🎯 Practice Collaborative Specification:**
> "I want to build a password reset feature. Ask me clarifying questions to help write a complete specification. Don't let me skip important details like security, rate limiting, or error handling."

**🧪 Test Your Understanding:**
> "Generate code from this vague prompt: 'Build a file upload system.' Then show me what's missing or assumed. What should the spec have included?"

**🚀 Apply to Your Work:**
> "I'm building [describe your actual project feature]. Help me identify what's vague in my description and what details I need to specify before asking you to generate code."

---