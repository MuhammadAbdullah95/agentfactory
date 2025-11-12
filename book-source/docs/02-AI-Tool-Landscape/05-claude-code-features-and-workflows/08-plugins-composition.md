---
sidebar_position: 8
title: "Putting It All Together: Plugins"
duration: "20-25 min"
---

# Putting It All Together: Plugins

You've learned five different ways to extend Claude Code:

1. **Commands** (Lesson 3): Ways to ask Claude for help
2. **Subagents** (Lesson 4): Specialists you explicitly ask for help
3. **Skills** (Lesson 5): Permanent knowledge Claude learns and applies
4. **Hooks** (Lesson 7): Automatic reminders at key moments
5. **MCP servers** (Lesson 6): Tools that connect Claude to information outside your computer

**But what if you wanted all five working together as one package?**

That's what **plugins** do. A plugin bundles commands, subagents, skills, and hooks together into one cohesive tool that works as a team.

---

## What is a Plugin? (Start Here If New)

**A plugin is a complete package that combines all the Claude Code extensions you've learned.**

Think of plugins like pre-made kits:
- A **code-review kit** includes: commands to start reviews, a code-review subagent, security skills Claude applies, and hooks that remind you to review before committing
- A **testing kit** includes: commands to run tests, a test-generator subagent, testing standards skills, and hooks that remind you to test before pushing

Instead of managing five separate things, you activate one plugin and everything works together.

---

## How Plugins Are Different from Individual Extensions

You've been learning individual extensions separately. Here's how plugins change that:

### Individual Extensions (What You've Learned)
```bash
# You have to manage each part separately:
claude "Use the code-reviewer subagent"  # Run a specialist
# Claude applies your code style skills automatically  # And skills
# Before committing, hook reminds you to review  # And hooks
# You manually remember to run the command  # And commands
```

### With a Plugin
```bash
# One command runs the entire code-review workflow:
/code-review

# Behind the scenes:
# - Activates the code-review subagent
# - Applies code style skills
# - Reminds you of your standards (hooks)
# - Everything works together automatically
```

When you activate the plugin, **all the parts work together automatically**.

---

## Real-World Example: The Code Review Plugin

Let's imagine a plugin called **code-review**:

### What's Inside the Plugin
- **Commands**: `/review` (start a review), `/approve` (mark as approved)
- **Subagent**: Code-review specialist trained on your standards
- **Skills**: Type hints, docstrings, security checks
- **Hooks**: Reminds you to review before committing
- **MCP Integration**: Can access GitHub to review pull requests

### How You Use It
```bash
# Activate the plugin
/code-review

Claude: "Code review plugin activated. Here's what I can help with:
- Review your code for style, security, and errors
- Auto-check before commits
- Create review reports

What would you like?"
```

All five extensions work together automatically.

---

## When to Use Plugins vs. Individual Extensions

**Use a plugin when**:
- You have a complete workflow you do regularly
- Multiple extensions (subagents, skills, hooks) work together
- You want to package expertise for sharing with team members
- You want everything organized and coordinated

**Use individual extensions when**:
- You need just one specialist (subagent)
- You want to teach Claude one standard (skill)
- You need one specific reminder (hook)
- You want flexibility and control

**Example**:
```bash
# Simple task - use individual extension:
claude "Use the code-reviewer subagent to check my function"

# Complete workflow - use plugin:
/code-review
# (entire workflow activates: reviews, checks standards, reminds you)
```

---

## Common Plugins You Might Use

Here are examples of plugins teams create:

### Plugin 1: Code Review Workflow
```
Includes: Commands (/review), Subagent (code-reviewer),
Skills (your code standards), Hooks (remind before commit)
```

### Plugin 2: Testing Workflow
```
Includes: Commands (/test), Subagent (test-generator),
Skills (your testing standards), Hooks (remind before pushing)
```

### Plugin 3: Documentation Workflow
```
Includes: Commands (/document), Subagent (doc-writer),
Skills (your doc standards), Hooks (remind to document)
```

### Plugin 4: Project Setup Workflow
```
Includes: Commands (/init-project), Subagent (setup helper),
Skills (your project structure), Hooks (verify setup on start)
```

---

## How Plugins Connect Everything

The power of plugins is **orchestration**—making parts work together seamlessly.

### Before Plugins (Fragmented)
```bash
claude "Set up my project structure"  # Command 1
claude "Use test-generator: Create tests"  # Subagent
claude "Here's my code style"  # Teaching a skill
# ... later, remember to commit ...
# ... later, remember to document ...
```

You're managing five things manually.

### With Plugins (Orchestrated)
```bash
/new-project

# Everything happens automatically:
# - Project structure created
# - Documentation skill applied
# - Test standards configured
# - Hooks set up to remind you
# - All working together
```

One command, everything orchestrated.

---

## Pause and Reflect: What Workflow Would You Bundle?

Think about your work:

1. **What's your most common workflow?** (code review, testing, deployment, documentation)
2. **Which extensions would help?** (commands, subagents, skills, hooks)
3. **Would packaging them together save you time?**

This is a plugin candidate.

---

## Creating Your First Plugin

You don't have to create plugins yet—that's more advanced. For now, just understand that plugins **bundle extensions together**.

When you're ready to create one, you'll:
1. Identify a complete workflow you do regularly
2. Create or find the subagents needed
3. Define the skills that apply
4. Set up the hooks for reminders
5. Create commands to start it all
6. Package it as one plugin

But that's a future lesson.

---

## Real Workflow: Using a Plugin

Let's see how plugins fit into your day:

### Monday Morning: Starting New Feature
```bash
/new-feature

Claude: "Feature development plugin activated.
I've set up:
- Code quality hooks (remind before committing)
- Test generation subagent (ready to write tests)
- Your code style standards (will apply automatically)
- Documentation hooks (remind to document)

Ready to start?"
```

### During Development
```bash
(You write code)

Claude (from hooks): "Your code is ready to review. Want me to check it?"

(Code review happens automatically using plugin components)
```

### Before Committing
```bash
(You're ready to commit)

Claude (from hooks): "Before you commit, your tests should pass. Run tests?"

(Tests run, pass, standards verified, all through plugin)
```

The entire workflow flows naturally because the plugin orchestrates everything.

---

## Common Mistakes

### Mistake 1: Creating Plugins Too Early

Don't create plugins before you understand individual extensions.

**Wrong**:
Learn about plugins first, then try to create one

**Right**:
Learn commands, subagents, skills, hooks separately. Then bundle them into a plugin when you have a complete workflow.

---

### Mistake 2: Over-Engineering Plugins

Don't create a 100-part plugin. Keep them simple and focused.

**Wrong**:
"One mega-plugin that does everything about coding"

**Right**:
"One plugin for code review" (focused on one workflow)

---

## Try With AI: Learn About Plugins

Open ChatGPT or another AI tool:

### Prompt 1: Identify a Bundleable Workflow

```
I work on [your type of work: coding, writing, data analysis, etc.].
What's my most common, repetitive workflow?
For that workflow, which extensions would help?
- Commands (to start it)
- Subagents (specialists)
- Skills (standards)
- Hooks (reminders)
- MCP servers (external tools)

Help me design this as a plugin.
```

**Expected outcome**: Understanding which workflow would make a good plugin.

---

### Prompt 2: See a Plugin in Action

```
Design a realistic plugin for my work in [your domain].
Show me:
1. What's the workflow? (what task does it automate)
2. What commands activate it?
3. Which specialists (subagents) help?
4. What standards (skills) apply?
5. What reminders (hooks) matter?
6. How would I use it in my day?

Make it feel realistic and helpful.
```

**Expected outcome**: Understanding how plugins orchestrate extensions.

---

### Prompt 3: Simple vs. Complex Plugins

```
Should plugins be simple (5 parts) or complex (20+ parts)?
Give pros and cons of each approach.
What makes a "good" plugin design?
How do I avoid over-engineering?
```

**Expected outcome**: Understanding plugin design principles.

---

## Key Terms Review

**Plugin**: A package that bundles commands, subagents, skills, hooks, and MCPs together.

**Orchestration**: Making parts work together as a coordinated whole.

**Workflow**: A sequence of steps you do regularly.

**Bundling**: Grouping related extensions into one package.

**Activation**: Turning on a plugin (usually with a command like `/code-review`).

---

## What's Next

In Lesson 9, you'll learn about the **Marketplace**—a place where people share plugins and extensions they've created, so you can use them without building everything from scratch.

But first, think about one workflow you could bundle into a plugin. What would make your work easier?

**Before moving to Lesson 9**:
1. Identify one workflow you do repeatedly
2. List which extensions (commands, subagents, skills, hooks) it needs
3. Imagine how it would feel if they all worked together automatically

---

## Try With AI: Design a Plugin for Your Work

Open Claude Code (or ChatGPT) and try this:

### Activity 1: Map Your Workflow

```
Here's a workflow I do regularly:
[Describe your workflow: step 1, step 2, step 3...]

For each step, which extension would help?
- Commands (to trigger it)
- Subagents (specialists)
- Skills (standards to apply)
- Hooks (reminders)
- MCPs (external tools)

Design how they'd work together as a plugin.
```

**Expected outcome**: Understanding how to bundle extensions.

---

### Activity 2: Feel the Difference

```
Show me the difference between:
1. Doing my workflow with individual extensions (fragmented)
2. Doing it with a plugin (orchestrated)

Make it obvious why the plugin is better.
```

**Expected outcome**: Understanding the value of orchestration.

---

**Ready for Lesson 9?** Let's learn about the Marketplace where communities share plugins and extensions.
