---
sidebar_position: 7
title: "Automatic Helpers: Hooks"
duration: "20-25 min"
---

# Automatic Helpers: Hooks

Have you ever had a friend who reminds you to do things?

"Hey, you're about to commit code—did you check for errors first?"
"Wait, you're editing that file—did you save before?"
"Starting a new project—let me help you set things up."

**Hooks are Claude's way of being that helpful friend.**

Hooks watch what you do and offer help automatically—before or after you act. You tell Claude once, "Hey, when I do THIS, remind me about THAT." Then Claude remembers and helps every time.

---

## What is a Hook? (Start Here If New)

**A hook is an automatic helper that offers Claude's assistance at key moments in your work.**

Think of hooks as reminders that activate automatically:
- **Before you act**: "Wait, before you delete that, make sure it's safe"
- **After you act**: "You just edited a file. Want me to check for errors?"
- **When you start**: "Starting a new session? Let me help set things up"

You define the moment and what Claude should do. Then Claude watches and helps automatically.

**Different from skills and subagents**:
- **Subagents** (Lesson 4): You explicitly ask for help
- **Skills** (Lesson 5): Claude applies knowledge automatically as it works
- **Hooks** (this lesson): Claude offers help at specific moments you define

---

## Real-World Example: How Hooks Help

### Without Hooks (Manual Checking)
```bash
# Every time, you have to remember to check things manually
claude "I'm about to commit my code. Please check for errors first"
# ... Claude checks ...

# Later, commit again
claude "I'm about to commit. Please check for errors again"
# You had to ask again

# Three commits later, you forget to ask...
# And commit code with an error
```

### With Hooks (Automatic Reminding)
You define once:
```
"Hook: Before I commit code, remind me to check for errors"
```

Then Claude helps automatically:
```bash
# First commit
(You're about to commit)
Claude: "Wait! I can check for errors before you commit. Want me to look?"
(You accept)
# Errors found and fixed

# Second commit
(You're about to commit)
Claude: "I can check for errors before you commit. Want me to look?"
# Claude remembers and reminds you every time
```

Claude doesn't forget. Every time you commit, Claude reminds you.

---

## When Hooks Are Useful

Hooks help with repetitive checks:

### Example 1: Before Making Changes
```
Hook: "Before I edit a file, remind me to back it up"
(Every time you edit, Claude offers to back up first)
```

### Example 2: After Making Changes
```
Hook: "After I write code, offer to check for errors"
(Every time you finish coding, Claude suggests a review)
```

### Example 3: When Starting Work
```
Hook: "When I start a session, remind me what I was working on"
(Claude helps you remember where you left off)
```

### Example 4: For Safety
```
Hook: "If I'm about to delete files, double-check that I really want to"
(Claude prevents accidental deletions)
```

---

## Common Hooks for Beginners

Here are simple hooks you might want to set up:

### Hook 1: "Check Before Committing"
```
"Before I commit code to git, remind me to:
1. Check for errors
2. Add a clear commit message
3. Verify the file contents"
```

### Hook 2: "Save Progress"
```
"After I finish a major change, remind me to save and back up my work"
```

### Hook 3: "Review Before Submitting"
```
"Before I submit any code or document, offer to review it one more time"
```

### Hook 4: "Safety Check Before Deleting"
```
"If I'm about to delete files, make me confirm it's safe"
```

---

## How to Create a Hook

Creating a hook is simple: you describe the moment and what Claude should do.

**Step 1: Pick the moment**
- "Before I commit code" → Before moment
- "After I edit a file" → After moment
- "When I start working" → Start moment

**Step 2: Describe what Claude should do**
- "Remind me to check for errors"
- "Offer to review the code"
- "Help me write a commit message"

**Step 3: Tell Claude it's a hook**
```bash
claude "Create a hook: Before I commit code, remind me to check for errors"
```

That's it. Claude will remember and activate the hook.

---

## Pause and Reflect: What Would Help You?

Think about your own workflow:

1. **What do you forget to check?** (errors, saving, backing up)
2. **What repetitive reminders do you need?** (before committing, before submitting, after editing)
3. **What safety checks matter to you?** (don't delete accidentally, verify before sending)

These are hook candidates.

---

## How Hooks Work: The Technical Basics (Don't Worry Too Much)

Hooks "listen" for specific moments in your work. When that moment happens, Claude jumps in.

**Three common hook types**:

1. **SessionStart Hook**
   - Fires when you start working
   - Example: "Remind me what I was working on"

2. **Before Tool Use Hook**
   - Fires before you do something
   - Example: "Before I delete, make sure it's safe"

3. **After Tool Use Hook**
   - Fires after you do something
   - Example: "After I code, offer to review"

**You don't need to know the technical details.** Just know that Claude watches for the moment you specify and offers help automatically.

---

## Real Workflow: Using Hooks in Your Day

Let's see how hooks fit into actual work:

### Morning: Starting Work
```bash
claude # Starting session

Claude (from SessionStart hook): "Welcome back! You were working on the
login feature. Want me to remind you where you left off?"

You: "Yes, tell me what I was doing"
```

### During Work: Writing Code
```bash
(You write a new function)

Claude (from After Code hook): "You just wrote some code. Want me to
check it for errors before you move on?"

You: "Sure, check it"
```

### Before Committing: Safety Check
```bash
(You're about to commit)

Claude (from Before Commit hook): "Before you commit, want me to make sure
there are no errors?"

You: "Yes, please"
```

Hooks keep Claude helping throughout your workflow, without you having to ask.

---

## Common Mistakes

### Mistake 1: Creating Too Many Hooks

Don't set up 10 hooks at once. Start with one.

**Wrong**:
```bash
# Too many
claude "Create hooks for: before commit, after edit, before delete, on start,
after error, before submit, after finish, ..."
```

**Right**:
```bash
# Start with one
claude "Create a hook: Before I commit code, remind me to check for errors"
# (Add more hooks later if needed)
```

---

### Mistake 2: Creating Hooks You Don't Actually Need

Don't create hooks for rare events.

**Unnecessary**:
```bash
"Hook: If I accidentally delete all my files, notify me"
(This almost never happens, so the hook adds noise)
```

**Good**:
```bash
"Hook: Before I delete files, confirm it's intentional"
(This is something you do regularly, so the reminder helps)
```

---

## Try With AI: Learn About Hooks

Open ChatGPT or another AI tool:

### Prompt 1: Identify Repetitive Checks

```
I work on [your type of work: coding, writing, data analysis, etc.].
What repetitive checks do I do (or forget to do) regularly?
For each check, suggest:
1. When should it happen? (before/after/during what action)
2. What would Claude remind me to check?
3. Would setting up a hook for this save me time?
```

**Expected outcome**: Understanding which hooks would help your work.

---

### Prompt 2: Design Your First Hook

```
I want to create my FIRST hook. Here's my situation:
[Describe something you do repeatedly or often forget]

Help me design a hook for this:
1. WHEN should it activate? (describe the moment)
2. WHAT should Claude remind me to do?
3. How would I ask Claude to create this hook?
```

**Expected outcome**: Clear design for your first hook.

---

### Prompt 3: Safety Hooks

```
For my work in [your domain], what are potentially risky actions I take?
For each risky action, suggest a hook that would make it safer.
Examples might be: before deleting, before submitting, before sending, etc.
```

**Expected outcome**: Understanding how hooks can keep you safe.

---

## Key Terms Review

**Hook**: An automatic reminder Claude gives you at specific moments in your work.

**SessionStart**: A hook that activates when you start working.

**Before Hook**: A reminder Claude gives before you do something (like before committing).

**After Hook**: A reminder Claude gives after you do something (like after editing).

**Automation**: Setting something up once so it helps automatically going forward.

---

## What's Next

In Lesson 8, you'll learn about **plugins**—ways to bundle commands, subagents, skills, and hooks together into organized packages that work as a team.

But first, think about one repetitive check you do (or forget to do). This could be your first hook.

**Before moving to Lesson 8**:
1. Identify one repetitive task where Claude could help
2. Think about when Claude should offer help (before, after, or during)
3. Be ready to ask Claude to create that hook

---

## Try With AI: Start Your First Hook

Open Claude Code (or ChatGPT) and try this:

### Activity 1: What Would Help?

```
I do [type of work]. Here's one thing I do repeatedly and would like help with:
[Describe the repetitive task]

Should Claude remind me BEFORE, AFTER, or AT THE START of this task?
What exactly should Claude help me remember or check?
```

**Expected outcome**: Clear understanding of how a hook would help.

---

### Activity 2: Seeing Hooks in Action

```
Show me a realistic workflow where a hook saves me from making a mistake.
Example:
1. I'm about to do something risky
2. The hook reminds me to check first
3. I discover a problem before it's too late
4. The hook protected me

Make it realistic for my work in [your domain].
```

**Expected outcome**: Understanding the real value of hooks.

---

**Ready for Lesson 8?** Let's learn about plugins—putting everything together.
