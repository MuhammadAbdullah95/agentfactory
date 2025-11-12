---
sidebar_position: 4
title: "Understanding and Using Subagents"
---

# Understanding and Using Subagents

## The Problem: Context Pollution and Specialization

You've installed Claude Code and run your first commands. But as you use it more, you'll encounter a common challenge: **context pollution**.

Imagine this scenario: You're working on a Python project. You ask Claude Code to help debug a function, then to review your code for style issues, then to generate documentation, then to suggest performance optimizations. By the time you're on your fifth request, Claude Code's context includes all your previous conversations—debugging details, style discussions, documentation drafts. The conversation has become cluttered.

**What if you could press "reset" without losing your work?**

**What if you could have specialized AI assistants for different tasks—a code reviewer, a documentation writer, a debugging expert—each with clear focus and isolated context?**

That's what **subagents** enable. They're one of Claude Code's most powerful features, yet often overlooked by beginners who stick to the main conversation for everything.

In this lesson, you'll learn what subagents are, when to use them, and how to create your first custom subagent—a code reviewer that applies your team's specific standards.

---

## Three-Role AI Partnership in Subagent Design

Remember from Lesson 1 the Three-Role AI Partnership? Subagents are where that partnership becomes concrete. When you create a specialized subagent, you're not just organizing tasks—you're **clarifying roles**. A code-reviewer subagent acts as your **Teacher** (suggesting standards you might not consider), your **Student** (learning your team's specific preferences), and your **Co-Worker** (executing reviews alongside you with focus and consistency). This is role clarity in action: instead of one Claude Code agent wearing many hats in a cluttered conversation, subagents allow your AI partner to specialize—deepening expertise in focused domains while you orchestrate the larger workflow. When you delegate a code review explicitly to a specialized subagent, you're practicing the co-learning partnership at its best: you set the intention, AI brings focused expertise, and together you achieve better results than either could alone.

---

## What Are Subagents?

**Definition**: A subagent is a specialized task-specific agent for improved context management. They are configured with custom instructions (called a "system prompt") and isolated context separate from the main conversation.

Think of subagents as specialized team members:

- **Main Claude Code**: Your general assistant—handles one-off questions, exploratory tasks, varied workflows. It will manage the subagents as well.
- **Subagent 1 (Code Reviewer)**: Focused solely on reviewing code for bugs, style, and best practices
- **Subagent 2 (Test Writer)**: Specialized in generating unit tests for functions
- **Subagent 3 (Documentation Generator)**: Expert at writing clear, comprehensive documentation

Each subagent has:
1. **Custom system prompt**: Instructions that define its role, constraints, and expertise
2. **Isolated context**: Conversations in this subagent don't affect the main conversation or other subagents
3. **Tool access configuration**: You can limit which tools (file read/write, command execution) the subagent can use

### Subagents vs. Main Conversation: When to Use Each

| Aspect | Main Conversation | Subagent |
|--------|-------------------|----------|
| **Use Case** | Exploratory work, varied tasks, one-off questions | Repetitive specialized tasks with clear scope |
| **Context** | Accumulates all conversation history | Isolated—only sees subagent's own history |
| **Customization** | General-purpose Claude behavior | Custom system prompt defines specific role |
| **When to Use** | "Help me understand this error" | "Review this code using our team's style guide" |
| **Examples** | Debugging, learning concepts, exploring codebases | Code reviews, test generation, refactoring, documentation |

**Key Insight**: Use subagents when you have **repeatable tasks with clear instructions**. Use the main conversation when you need flexibility and exploration.

---

#### 💬 AI Colearning Prompt: Identify Context Pollution in Your Workflow

Before diving into subagent creation, let's make the problem real in **your** context:

> **Explore with your AI companion**: "I work on [describe your typical project: web app, data pipeline, DevOps infrastructure, mobile app, etc.]. When I'm working with Claude Code in my terminal, what kinds of tasks might cause 'context pollution'? Give me 2–3 examples from MY domain where mixing main conversation with specialized tasks could create confusion or lead to mistakes. For each example, explain what clean separation with subagents would improve."

This prompt helps you recognize context pollution in your own workflow—not as an abstract concept, but as a real problem you've likely already experienced. Pay attention to what your AI companion suggests; those insights may reveal tasks you didn't realize would benefit from specialization.

---

## Why Subagents Matter: Three Key Benefits

### Benefit 1: Context Preservation

**Problem Without Subagents**: After 10 interactions in the main conversation, Claude Code's context is filled with unrelated discussions. Asking for a code review now means Claude considers all previous context—even if irrelevant.

**Solution With Subagents**: Launch a fresh subagent for each focused task. The code review happens in a clean context, without clutter from previous debugging or documentation work.

### Benefit 2: Specialization and Consistency

**Problem Without Subagents**: You must repeatedly tell Claude Code your code review standards, testing framework preferences, or documentation style with every new session.

**Solution With Subagents**: Encode these instructions once in a subagent's system prompt. Every time you invoke the "code-reviewer" subagent, it already knows your standards.

**Example System Prompt for Code Reviewer**:
```
You are a code reviewer specializing in Python.
Apply these standards:
- PEP 8 style compliance
- Type hints required for all functions
- Docstrings required (Google style)
- Prefer list comprehensions over loops where readable
- Flag any security concerns (SQL injection, hardcoded secrets)
- Suggest performance improvements for O(n²) or worse complexity
```

Every code review from this subagent applies these standards consistently.

### Benefit 3: Reusability Across Projects

**Problem Without Subagents**: You manually recreate your preferred workflows for each new project.

**Solution With Subagents**: Subagents are stored as files in `.claude/agents/`. You can:
- Share subagents with your team via version control
- Reuse the same subagent across multiple projects
- Build a library of specialized assistants

A well-designed subagent becomes **organizational knowledge**—capturing expertise that benefits your entire team.

---

## Subagent Architecture: How They Work

Let's peek under the hood to understand how subagents function.

### File Structure

When you create a subagent named `code-reviewer`, Claude stores a single file under `.claude/agents/` with:
- A name and short description of its purpose
- Optional model selection and color
- A clear checklist of standards it applies
- The expected form of its output (e.g., prioritized issues and actionable suggestions)

### Subagent Lifecycle (Zero Overhead View)

1. Create once via `/agents` and describe the role.
2. Use naturally ("Use the code-reviewer subagent...")—Claude may also auto‑delegate when the match is obvious.
3. Work happens in a clean, isolated context; results return to the main thread.
4. Iterate the description over time as your team practices evolve.

---

#### 🤝 Practice Exercise: Design Your Subagent Before Building

Before jumping to creation, let's practice **specification thinking**—planning your subagent's purpose before you build it. This is the essence of subagent design: clarity first, implementation second.

**Your task:**
1. **Think of a repetitive task in YOUR workflow** — Something you do multiple times per week. Examples: code testing, style linting, documentation generation, security auditing, dependency updates, API documentation, database migrations, etc.
2. **Answer these planning questions:**
   - **What context does this task need?** (e.g., "code files and test framework info", "configuration files and lint rules", "API schemas and team style guide")
   - **What tools would it use?** (e.g., Read files, Execute bash commands, Web Search for library docs, etc.)
   - **When should it run?** (e.g., "explicit command when I ask for reviews" vs "automatic when I push code with linting issues")
3. **Write your subagent spec** — 2–3 sentences describing its purpose, the problem it solves, and its role.

**Example specification** (for a linting subagent):
> "Purpose: Automatically identify Python style violations using flake8 and provide fixes. Problem solved: Context pollution from switching between main conversation (debugging) and linting (style cleanup). Role: Automatic delegation when code has style issues; explicit invocation when I want proactive cleanup."

This exercise teaches you to think like a subagent designer: What's the clear, repeatable task? What context does it need? When does it activate? By the end, you'll have a written specification for your first subagent.

---

## Creating a "Latest News" Subagent

Let's create a **"latest-news" subagent**—a focused researcher that surfaces current headlines, trends, and concise summaries with citations.

### Step 1: Create the Subagent

- Start claude session, from slash commands run `/agents` interface and select "Create new agent"
- Choose Project location so your team can reuse it
- Describe the role succinctly, for example:
  - Purpose: daily news researcher for a chosen domain (e.g., AI, security)
  - Output: 5–7 bulleted headlines with one‑sentence summaries and links; a short trend synopsis; 2 follow‑up questions
  - Constraints: prioritize reputable sources; avoid duplicates; keep total read under 2 minutes

Claude will create the subagent file under `.claude/agents/latest-news.md` (or similar) with your description and settings.

**Expected result**: The agent appears in your list and retains its focused role.

### Step 2: Try the "Latest News" Subagent (Daily Workflow)

- Try now: Ask Claude to use the latest-news subagent for your topic today (for example, AI policy). You should receive headlines with links, a short trend synopsis, and two follow‑up questions.

**If you see targeted, phase‑specific feedback**: ✅ It works. You get clean execution and clear results with minimal prompting.

---

#### 🤝 Practice Exercise: Test Explicit vs. Automatic Delegation

Now that you've created a subagent (or used the example), let's compare the two delegation modes in practice:

**Your task:**
1. **Test explicit delegation**: Ask Claude Code explicitly: "Use the latest-news subagent to find [topic]." Notice the control you have—you're directing the role shift.
2. **Test automatic delegation** (if enabled): Make a request that would naturally match the subagent (e.g., "Find the latest news on [topic]" without mentioning the subagent name). Does Claude Code automatically use the subagent, or does it stay in main conversation?
3. **Compare your experience**:
   - When did explicit invocation feel better (more control)?
   - When did automatic delegation feel more convenient (less overhead)?
   - Which approach matches YOUR working style better?

**Reflection**: There's no universally "better" delegation mode. Explicit is predictable; automatic is convenient. Some teams prefer explicit control (especially for production-critical tasks like code review). Others prefer automatic for convenience (especially for exploratory tasks like research). Your job is to recognize the tradeoff and make intentional choices about which mode fits which task.

---

## Delegation Modes

Subagents can be used in two ways:

- Explicit invocation: You request a specific subagent (e.g., "Use the code-reviewer subagent to check my recent changes").
- Automatic delegation: Claude can delegate to a subagent when your task clearly matches that subagent’s description and allowed tools.

Use explicit invocation for predictability. Rely on automatic delegation as a convenience when descriptions are specific.

---

#### 🎓 Expert Insight: Delegation Modes Reveal Role Clarity

The distinction between explicit and automatic delegation isn't just organizational—it's about **role clarity in the Three-Role AI Partnership**. When you **explicitly invoke** a code-reviewer subagent, you're actively directing your AI partner's role: "Now I need you as a specialized Teacher/Co-Worker focused on code review." The AI knows exactly which specialized role to adopt. When you **enable automatic delegation**, you're trusting your AI partner's judgment to recognize when a task matches a subagent's expertise and shift roles autonomously. This is role flexibility—the same AI partner adapts between general multi-role assistant (main conversation) and specialized expert (subagent) based on task recognition. Neither approach is "passive"—both require your AI partner to understand the role and execute with specialized focus. The key difference is who decides when the role shift happens: you (explicit) or the AI recognizing the pattern (automatic).

---

## ✓ Your Subagent Is Working When:

**Quick verification**:

1. **Subagent is created** - You can list it
2. **Subagent can be invoked** - You can ask it to explain code
3. **It returns helpful explanations** - The response makes sense and helps clarify the code
4. **It stays in character** - Multiple invocations maintain the "collaborative explainer" role

**If this works**: 🎉 **Your collaborative helper is ready! You now have a dedicated partner to help you understand code.**

---

## Subagent Best Practices

**1. Keep System Prompts Focused**
- One clear responsibility per subagent
- Avoid combining unrelated tasks (e.g., "review code AND generate docs")

**2. Use Descriptive Names**
- ✅ `python-code-reviewer`, `pytest-test-generator`
- ❌ `helper`, `tool1`, `bob`

**3. Limit Tool Access Appropriately**
- Read-only subagents for analysis tasks
- Full access only when necessary (e.g., refactoring subagents)

**4. Iterate and Improve**
- After using a subagent, refine its system prompt
- Add examples of good/bad outputs to guide behavior
- Collect feedback from team members

---

#### 🎓 Expert Insight: Organizational Knowledge as Competitive Advantage

Here's a strategic insight that elevates subagents beyond "better organization": Your subagents become **captured organizational knowledge**. When your team creates a `python-code-reviewer` subagent with your specific standards (PEP 8 + type hints + Google-style docstrings + security checks + performance analysis), you're encoding team expertise into a reusable artifact. That subagent now runs automatically across all projects—your team's collective knowledge operating without you needing to remind anyone of the standards every review. Scale this across your team: `pytest-test-generator` (your testing philosophy), `documentation-writer` (your docs style), `security-auditor` (your threat model), `performance-optimizer` (your optimization priorities). Suddenly, you have 10+ custom subagents representing "the way we do things here." This is **ambient autonomous expertise**—knowledge that runs without human intervention. Competitors using generic AI chat have no such advantage. But your team with 10+ specialized subagents has a library of organizational best practices baked into your AI partnership. That's a competitive moat: not just speed, but amplified consistency and quality that gets better with every project.

---

## Pause and Reflect: Specialization vs. Flexibility

You've learned how to create specialized AI assistants with subagents. But there's a tradeoff to consider:

**Specialization** provides consistency and focus, but reduces flexibility. A code-reviewer subagent won't help you debug runtime errors or generate documentation—that's by design.

**The main conversation** is flexible and exploratory, but lacks the focused instructions and clean context that subagents provide.

**Reflection Questions**:
- Think about your own daily workflow. What repetitive tasks could benefit from a specialized subagent?
- When would you prefer the flexibility of the main conversation over a focused subagent?
- If you work on a team, what subagents could capture and share your team's unique expertise?

---

## Try With AI

Use Claude Code for this activity. If you already have another AI companion tool set up (e.g., ChatGPT web, Gemini CLI), you may use that instead—the prompts are the same.

### Prompt 1: Decision Tree for Tool Selection

```
I'm confused about when to use subagents vs. the main conversation. Give me a simple decision tree: For each scenario below, should I use a subagent or main conversation? (a) Quick question about Python syntax, (b) Code review following team standards, (c) Debugging a weird error I've never seen, (d) Generating tests for 10 similar functions, (e) Exploring a new codebase I just downloaded.
```

**Expected outcome:** Clear decision framework for when to use subagents

### Prompt 2: First Subagent Design

```
I want to create my FIRST subagent. My most repetitive task is [describe your task: code reviews / writing tests / generating docs / etc.]. Help me design it: (a) What should I name it? (b) What 3-5 instructions should go in the system prompt? (c) What tool access should it have? (d) Give me the exact command to create it.
```

**Expected outcome:** Complete design for your first custom subagent

### Prompt 3: Custom Code Reviewer

```
The lesson shows a code-reviewer subagent with specific standards (PEP 8, type hints, docstrings). I work with [your language/framework]. Create a custom system prompt for a code-reviewer subagent tailored to MY stack. Include 5-7 specific standards I should enforce. Make it copy-paste ready.
```

**Expected outcome:** Copy-paste-ready system prompt for your specific needs
