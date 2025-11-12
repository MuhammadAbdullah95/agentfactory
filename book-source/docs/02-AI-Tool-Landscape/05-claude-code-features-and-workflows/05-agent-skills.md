---
sidebar_position: 5
title: "Teaching Claude What You Care About: Skills"
duration: "20-25 min"
---

# Teaching Claude What You Care About: Skills

Imagine you're training a new team member. You spend a week teaching them:
- "Here's how we format our code"
- "This is the security standard we follow"
- "We always document like this"
- "Here's the testing framework we use"

After a week of training, they know what to do. You don't have to tell them anymore—they just *do* it.

**Skills are how you teach Claude Code what matters to you.**

Instead of repeating "follow this coding standard" every time, you teach Claude once. Then Claude remembers and applies it automatically.

---

## What is a Skill? (Start Here If New)

**A skill is something you teach Claude Code so it remembers and applies automatically.**

Think of skills as "permanent knowledge" Claude learns about your work:
- "Our code style is: spaces not tabs, always add docstrings"
- "Security-wise: always hash passwords, never store credentials in code"
- "Testing: write tests before pushing code"
- "Documentation: every function needs a description"

Once you teach Claude these skills, it applies them without you asking.

**Different from subagents**:
- **Subagents** (Lesson 4): Specialists you ask for help (like hiring a code reviewer)
- **Skills** (this lesson): Permanent knowledge Claude learns (like training someone on your team's standards)

---

## How Skills Work: A Real Example

### Without Skills
```bash
claude "Write a function to validate emails"
# Claude writes a function...

claude "Check this for security problems"
# Claude: "The function doesn't hash passwords..."
# (Claude doesn't know your security standards)

claude "Write tests for this email function"
# Claude writes tests, but doesn't follow your testing style
```

You have to keep reminding Claude of your standards.

### With Skills
You teach Claude once:
```bash
# Teaching phase (one time only)
"Claude, here's what I care about:
- Always add type hints to functions
- Always write docstrings
- Always hash passwords, never store plain text
- Always write tests in pytest format"
```

Then everything Claude creates automatically follows these standards:
```bash
claude "Write a function to validate emails"
# Claude writes it with type hints, docstrings, and security properly implemented
# (Claude remembers your standards)

claude "Write tests for this function"
# Tests are in pytest format with full coverage
# (Claude remembered your testing style)
```

---

## Pause and Reflect: Why This Matters

You've learned about subagents (specialists you ask for help) and skills (permanent knowledge Claude learns).

Think about your own work:
1. **What standards do you follow repeatedly?** (coding style, security practices, testing approach)
2. **How often do you explain these standards?** (every time you ask Claude for help?)
3. **What if Claude just... remembered?**

That's what skills do.

---

## Real-World Use Cases for Skills

Here are some skills people teach Claude Code:

### Skill 1: Code Style Standards
```
"When writing Python code, always:
- Use type hints on every function
- Follow PEP 8 naming conventions
- Write Google-style docstrings
- Use f-strings for formatting
"
```

### Skill 2: Security Practices
```
"When writing authentication code:
- Always hash passwords with bcrypt
- Never store plain-text passwords
- Always validate input
- Always use HTTPS for login
"
```

### Skill 3: Testing Standards
```
"When writing tests:
- Use pytest framework
- Aim for 80%+ code coverage
- Test happy path, error cases, and edge cases
- Use descriptive test names like test_function_does_something()
"
```

### Skill 4: Documentation Standards
```
"When documenting:
- Every function needs a description
- Include parameter types
- Include return types
- Include example usage for complex functions
"
```

---

## How to Create Your First Skill

You don't need to be technical to create a skill. You just describe what matters to you.

**Step 1: Pick one standard you follow**
- Example: "I always add type hints to Python functions"

**Step 2: Write it down clearly**
- "When writing Python: Always include type hints. Example: def add(x: int, y: int) -> int:"

**Step 3: Tell Claude this is a skill**
- Simply ask Claude: "I want to teach you a skill. When you write Python code, always add type hints like this..."

**Step 4: Claude remembers**
- From then on, Claude applies it automatically

---

## When to Create a Skill vs. Just Asking

**Create a skill when**:
- You'll repeat the same standard 5+ times
- The standard is important to your work
- You want it applied automatically every time

**Just ask Claude when**:
- It's a one-time request
- The standard might change soon
- You want to override your usual style for one task

**Example**:
```bash
# Probably needs a skill (you'll repeat it often):
"Always write type hints"

# Probably just one request (might change):
"For this task, use simple variable names instead of our usual style"
```

---

## Common Skills for Beginners

Here are simple skills you might want to teach Claude:

### Skill: "Always Add Comments"
```
"When writing code, add a comment above each section explaining what it does.
Example:
# Check if user exists
if user in database:
    ...
"
```

### Skill: "Always Handle Errors"
```
"When writing code, include error handling.
Don't assume things will work—handle the case where they don't."
```

### Skill: "Write Beginner-Friendly Explanations"
```
"When you explain something, assume I'm new to programming.
Define technical terms. Use everyday analogies.
Avoid jargon."
```

---

## How Claude Applies Skills Automatically

Once you teach Claude a skill, it works **automatically**.

**You don't have to ask**. Claude sees "I'm writing Python code" and thinks "The user cares about type hints—I should add them."

This is powerful because:
1. **You don't have to remember** to ask for type hints every time
2. **You don't have to repeat** the standard
3. **Everything stays consistent** across all your work
4. **Claude learns what matters to you** specifically (not generic best practices)

---

## Pause and Reflect: What Would You Teach?

Before moving forward, think: **What's one standard or practice you follow in everything you do?**

Examples:
- "I always organize my folders a certain way"
- "I always add comments to explain my code"
- "I always test my work before I'm done"
- "I always write documentation"
- "I prefer simple explanations over technical jargon"

Write this down. This is a skill candidate.

---

## Common Mistakes

### Mistake 1: Teaching Too Many Skills at Once

Don't overwhelm Claude with 10 new standards. Start with one.

**Wrong**:
```bash
# Teaching too much at once
claude "Here's 15 different coding standards I follow..."
```

**Right**:
```bash
# Start with one
claude "Here's my most important standard: Always add type hints to Python functions"
# (Later, teach another skill)
```

---

### Mistake 2: Being Too Vague

Skills need to be clear and specific.

**Vague**:
"Write good code"

**Clear**:
"When writing Python, include type hints. Example: def greet(name: str) -> str:"

---

## Try With AI: Learn About Skills

Open ChatGPT or another AI tool:

### Prompt 1: Identify Your Standards

```
I do [type of work: coding, writing documentation, creating databases, etc.].
What are 3-5 standards or practices I should teach an AI assistant about my work?
For each one:
1. What is the standard?
2. Why is it important to me?
3. How would I teach it clearly?
```

**Expected outcome**: Understanding what standards matter in your work.

---

### Prompt 2: Teaching a Skill

```
I want to teach an AI assistant about how I work. Here's one standard I follow:
[Your standard here]

Help me write this as a clear "skill" that an AI could remember and apply automatically.
Make sure it includes:
1. Clear description of the standard
2. Why I care about it
3. An example showing the standard in action
```

**Expected outcome**: Knowing how to teach Claude one of your standards.

---

### Prompt 3: Skills for Your Domain

```
I work in [your domain: web development, data science, writing, etc.].
What are professional standards people in my field follow?
For each standard, suggest:
1. What is it?
2. Why do professionals care about it?
3. How would I teach this to an AI assistant?
```

**Expected outcome**: Understanding industry standards you could teach Claude.

---

## Key Terms Review

**Skill**: Something you teach Claude Code to remember and apply automatically.

**Standard**: A practice or rule you follow consistently (like always adding comments to code).

**Teaching Claude**: Explaining to Claude what matters to you so it remembers.

**Applying a skill**: Claude automatically uses what it learned without you asking.

---

## What's Next

In Lesson 6, you'll learn about **MCP servers**—ways Claude can reach outside your computer to access information like websites, databases, and APIs.

But first, think about one skill you'd teach Claude if you could. What standard is most important to your work?

**Before moving to Lesson 6**:
1. Think about one standard you follow repeatedly
2. Write it down clearly
3. Be ready to teach it to Claude

---

## Try With AI: Create Your First Skill Teaching

Open Claude Code (or ChatGPT) and try this:

### Activity 1: Clarify Your Standards

```
I want to teach Claude Code about MY standards and practices.
Here are the things I value in my work:
[List 2-3 things: examples might be: clear code, security, testing, good documentation]

For each one, help me write a clear skill description that Claude could remember and apply.
```

**Expected outcome**: Written skills you can teach Claude.

---

### Activity 2: See a Skill in Action

```
Imagine I teach Claude this skill:
"Always include type hints in Python functions. Example: def add(x: int, y: int) -> int:"

Now, show me:
1. A function Claude writes WITHOUT knowing this skill (no type hints)
2. The same function with the skill applied (with type hints)
3. Why the skill version is better

Make it clear how the skill changes Claude's output.
```

**Expected outcome**: Understanding how skills improve Claude's work.

---

**Ready for Lesson 6?** Let's learn how Claude can reach beyond your computer using MCP servers.
