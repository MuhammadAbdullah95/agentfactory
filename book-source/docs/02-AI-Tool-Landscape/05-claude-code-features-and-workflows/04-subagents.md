---
sidebar_position: 4
title: "Specialized Helpers: Subagents"
duration: "20-25 min"
---

# Specialized Helpers: Subagents

Have you ever wished you had a specialist on your team? Someone whose only job is code review. Another person who only writes tests. A third who's an expert at documentation.

With Claude Code, you can have this.

**Subagents are specialized helpers** that Claude creates for specific jobs. Instead of asking one Claude to do everything (debugging, testing, reviewing, documenting), you can have separate specialists—each focused on one task.

---

## What is a Subagent? (Start Here If New)

**A subagent is a specialized version of Claude trained for a specific job.**

Think of it like having different team members, each an expert in their field:
- **Code Reviewer**: Looks at your code and finds problems
- **Test Writer**: Creates tests for your functions
- **Documentation Expert**: Writes clear explanations of your code

In real life, you'd hire these people. With Claude Code, they're already available.

**Why this matters**: Instead of asking one Claude for everything, you ask the right specialist for each job. Each specialist knows exactly what to look for.

---

## Real-World Example: What Problems Do Subagents Solve?

Imagine you're working on a Python project. Here's what happens **without subagents**:

```bash
claude "Review my login code for security issues"
# Claude reviews the code...

claude "Write tests for the login function"
# Claude looks back at the security review...
# Remembers all those details...
# Now tries to write tests...
# Gets confused because it's juggling two completely different tasks
```

**With subagents**, you use specialists:

```bash
# First: Use the code-review specialist
claude "Use the code-reviewer subagent: Review my login code for security issues"
# Code reviewer focuses ONLY on security

# Second: Use the test-writer specialist
claude "Use the test-writer subagent: Write tests for the login function"
# Test writer focuses ONLY on testing
```

Each specialist has a clear job. No confusion. Better results.

---

## Two Kinds of Subagents

### 1. Using Existing Subagents

When you first start with Claude Code, there are already some helpful subagents available:
- **Code Reviewer**: Finds bugs and style problems
- **Test Generator**: Writes tests for your code
- **Documentation Writer**: Explains your code clearly

**How to use them**:
```bash
claude "Use the code-reviewer subagent to review my login.py file"
```

Claude will use that specialist to review your code.

### 2. Creating Custom Subagents

As you get more experience, you can create your own specialists trained exactly the way you want.

**For now**: Focus on using existing subagents. Creating custom ones comes later.

---

## When to Use a Subagent

Here's a simple guide:

**Use a subagent when**:
- The task is the same every time (code review, writing tests, documentation)
- You want consistent, focused results
- You're switching between different types of work

**Use the regular `claude` command when**:
- You're asking a quick question
- You're exploring ideas
- You're debugging something unexpected

**Example**:
```bash
# Quick question - use regular claude
claude "What does this error message mean?"

# Repetitive task - use subagent
claude "Use the code-reviewer subagent: Check my authentication code for security issues"
```

---

## How Subagents Work: The Key Difference

When you use a subagent, **Claude remembers what that specialist is trained to do.**

**Without subagent** (Claude gets confused):
```bash
claude "Review my code for style issues"
# Claude: "Looking at the style..."

claude "Write tests for this function"
# Claude is thinking: "Wait, we were just doing style review...
# Now tests? I need to remember the style review too..."
```

**With subagent** (Specialist focus):
```bash
claude "Use the code-reviewer: Check my style"
# Code reviewer: "My job is style checking. Here's what I found..."

claude "Use the test-writer: Write tests for this function"
# Test writer: "My job is writing tests. Here are your tests..."
# (Doesn't think about the previous style review)
```

Each subagent has **one clear job** and isn't distracted by previous tasks.

---

## Real-World Scenario: Using Subagents in Your Workflow

Let's walk through a realistic example:

### Step 1: Ask for Code Review
```bash
claude "Use the code-reviewer subagent: Review my user registration function for bugs and security problems"
```

The code-reviewer specialist looks at your code and suggests improvements.

### Step 2: Ask for Test Writing
```bash
claude "Use the test-writer subagent: Write tests for my user registration function"
```

The test-writer specialist creates tests. It doesn't get distracted by what the code-reviewer said.

### Step 3: Ask for Documentation
```bash
claude "Use the documentation-writer subagent: Write clear documentation for my user registration function"
```

The documentation-writer specialist explains your code. Again, focused on its job.

---

## Pause and Reflect

You've learned what subagents are and when to use them. Ask yourself:

**Do you understand**:
1. What a subagent is? (A specialist Claude trained for one job)
2. When you'd use one? (Repetitive tasks like code review, testing, documentation)
3. Why they're useful? (Each specialist focuses on their job instead of juggling tasks)

If you answered yes to all three, you're ready to move forward.

---

## Understanding Subagent Names

When you use a subagent, you use its name in your request:

```bash
claude "Use the CODE-REVIEWER subagent: ..."
claude "Use the TEST-GENERATOR subagent: ..."
claude "Use the DOCUMENTATION-WRITER subagent: ..."
```

**Common subagent names you might use**:
- `code-reviewer` - Reviews code for problems
- `test-generator` - Writes tests
- `documentation-writer` - Creates documentation
- `security-auditor` - Checks for security issues
- `performance-analyzer` - Finds optimization opportunities

Don't worry about memorizing these. When you need a specialist, Claude can tell you which ones are available.

---

## Common Mistakes

### Mistake 1: Using a Subagent for Quick Questions

You don't need a subagent for simple questions.

**Wrong**:
```bash
claude "Use the code-reviewer: What does this error mean?"
```

**Right**:
```bash
claude "What does this error mean?"
```

Subagents are for tasks they specialize in, not for quick questions.

---

### Mistake 2: Asking a Subagent to do Something Outside Its Job

Each subagent has one specialty. Don't ask them to do something different.

**Wrong**:
```bash
claude "Use the test-generator: Review my code for security problems"
```

(Test generator specializes in tests, not security review)

**Right**:
```bash
claude "Use the code-reviewer: Check my code for security issues"
```

---

## Try With AI: Learn About Subagents

Open ChatGPT or another AI tool and ask:

### Prompt 1: Understanding Specialists

```
Imagine you manage a software team with three people:
- Alice (code reviewer)
- Bob (test writer)
- Carol (documentation expert)

If I ask Alice to do testing, or Bob to do documentation,
that's not their specialty. Explain why using the wrong specialist
is less effective than using the right one.
```

**What you're learning**: Why specialization matters.

---

### Prompt 2: Real-World Workflow

```
I'm learning about "subagents" - specialized AI helpers in Claude Code.
Give me a realistic example of a workflow where I'd use THREE different subagents.
For each one, explain:
1. What task would I ask it to do?
2. Why would I use a specialist instead of asking regular Claude?
3. How would I phrase my request to the subagent?
```

**Expected outcome**: Concrete examples of when and how to use subagents.

---

### Prompt 3: Choosing the Right Specialist

```
I work on [your type of project: Python web apps, data analysis, JavaScript, etc.].
What are the 3-5 different types of work I do repeatedly?
For each one, suggest what type of specialist/subagent would help.
```

**Expected outcome**: Understanding which specialists exist for your work.

---

## Key Terms Review

**Subagent**: A specialized version of Claude trained for one specific job (like code review or testing).

**Specialist**: Another word for subagent—a helper focused on one type of work.

**Code-Reviewer**: A subagent that looks for bugs and style problems in code.

**Test-Generator**: A subagent that writes tests for functions.

**Documentation-Writer**: A subagent that explains code clearly.

---

## What's Next

In Lesson 5, you'll learn about **skills**—a different way to extend Claude's abilities. Instead of using specialists for specific tasks (like subagents), skills teach Claude permanent expertise that it applies automatically across your work.

But first, get comfortable with subagents. Try using them in your next coding session.

**Before moving to Lesson 5**, try:
1. Identify one task you do repeatedly (code review, testing, documentation)
2. Ask Claude which subagent could help with that task
3. Try using that subagent once

You don't need to be perfect. Just get familiar with how they work.

---

## Try With AI: Start Using Subagents

Open Claude Code (or ChatGPT) and practice:

### Activity 1: Identify Your Subagent Need

```
I'm learning Claude Code subagents. I do [type of work: Python coding, web development, data analysis, etc.].

What's the ONE repetitive task I do most often that could benefit from a specialist subagent?
Describe:
1. What task is it?
2. Which subagent would help? (code reviewer, test generator, etc.)
3. How would I request that subagent's help?
```

**Expected outcome**: Understanding which subagent fits your work.

---

### Activity 2: See a Subagent in Action

```
Show me a realistic example where a code-reviewer subagent catches something that regular Claude might miss.
Give me:
1. Some code with a subtle bug or style problem
2. What regular Claude might say (generic response)
3. What the specialist code-reviewer would say (detailed, focused)
4. Why the specialist is better
```

**Expected outcome**: Understanding the value of specialization.

---

**Ready for Lesson 5?** Let's learn about skills—another way Claude learns and helps you.
