---
sidebar_position: 5
title: "Branches for Experimentation"
description: "Test AI changes safely without risking your main code"
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Create Feature Branch"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can create a branch and test changes safely"

  - name: "Test Before Merging"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can decide to merge or discard based on tests"

  - name: "Understand Branching Metaphor"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain why branches are essential for AI work"

learning_objectives:
  - objective: "Create a safe testing space with branches"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates and uses branches"

  - objective: "Test AI changes without affecting main code"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student tests on branch, then merges or discards"

  - objective: "Explain why branches make AI work safer"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student explains safety benefits"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (branch, test, merge, discard) within A2 limit ✓"

# Generation metadata
generated_by: "lesson-writer"
source_spec: "specs/012-chapter-8-git-github-aidd/plan.md"
created: "2025-11-05"
last_modified: "2025-11-05"
version: "2.0.0"
---

# Branches for Experimentation

## The Problem

Your AI wants to refactor your entire codebase. It's 50+ changes across 10 files. You think: "I want this, but what if it breaks everything?"

**Old way**: Make changes on your main code. Test. Hope. If it breaks, panic and undo.

**Smart way**: Create a copy. Test AI's changes there. If good, merge. If bad, delete the copy. Your main code stays safe.

**That's what branches do.**

**Time**: 20 minutes

---

## What Are Branches?

A **branch** is a copy of your code where you test things.

Think of it like this:

```
Main Code (safe version)
  ↓
Make a copy → Test Branch
  ↓
AI makes changes here
  ↓
Test it
  ↓
Works? → Copy back to main
Broken? → Delete the copy
```

Your main code **never** gets touched until you're sure it works.

---

## Simple Analogy

**Writing an essay**:
- Main document = Your finished, safe version
- New copy = Draft where you try new paragraphs
- Test = Read it, see if it's better
- Keep or delete = Save the new version or throw it away

**Same with code**:
- Main = Your working code
- Branch = Copy where AI changes things
- Test = Run it, see if it works
- Merge or delete = Copy it back or throw it away

---

## Why This Matters with AI

AI makes big changes fast. Without branches:
- AI changes your main code
- Something breaks
- You panic
- Hard to undo everything

With branches:
- AI changes the copy (branch)
- Test the copy
- If broken, delete the copy
- Main code never got touched
- Try again differently

**Branches = Fearless experimentation**

---

## The Simple Workflow

### Step 1: Create a Test Space

**What you want**: A safe copy to test changes

**Instead of**: Working directly on main

**Just ask your AI**:
- "Create a branch to test this change"
- "Make a copy for testing"
- "Set up a test branch called 'try-new-feature'"

### Example

**You**: "Create a branch called 'test-refactor' so I can try changes safely"

**AI**: "Creating test branch 'test-refactor'..."

[AI creates the branch]

**AI**: "Done! You're now working on the test branch. Any changes you make here won't affect your main code until you decide to merge."

**You**: "So if I break something, my main code is safe?"

**AI**: "Exactly! Your main code is untouched. You can experiment freely here."

---

### Step 2: Make Changes on the Branch

**What you want**: AI changes code on the test copy

**Just ask your AI**:
- "Add error handling to calculator.py"
- "Refactor this function for performance"
- "Optimize database queries"

### Example

**You**: "Refactor calculator.py to be faster"

**AI**: "I'll optimize your calculator functions. Making changes on the 'test-refactor' branch..."

[AI modifies code]

**AI**: "Done! I made the add() and subtract() functions 3x faster using better algorithms. Ready to test?"

**You**: "Show me what changed"

**AI**: "Main changes:
- add() now uses sum() instead of loop (faster)
- subtract() optimized for large numbers
- Both functions now have error checking

Want to see the exact code differences?"

---

### Step 3: Test Everything

**What you want**: Make sure it works before keeping it

**Just ask your AI**:
- "Test the changes"
- "Run my code and check for errors"
- "Does everything still work?"

### Example

**You**: "Test calculator.py to make sure nothing broke"

**AI**: "Running tests..."

[AI runs the code]

**AI**: "All tests passed!
- Addition works correctly
- Subtraction works correctly
- Error handling works
- No crashes

The refactored code is working perfectly."

**You**: "Great! How do I keep these changes?"

**AI**: "You have two options:
1. Merge - Copy the changes to your main code
2. Discard - Delete this test branch and keep main unchanged

Which do you want?"

---

### Step 4: Decide What to Do

You have two choices:

**Choice A: Keep the Changes (Merge)**

**You**: "The changes work great. Merge them to main."

**AI**: "Merging 'test-refactor' into main..."

[AI merges the branch]

**AI**: "Done! Your main code now has the faster calculator functions. Should I delete the test branch to clean up?"

**You**: "Yes"

**AI**: "Test branch deleted. Your main code is updated and ready to use."

**Choice B: Throw Away the Changes**

**You**: "Actually, the changes broke something. Delete this branch."

**AI**: "Deleting 'test-refactor' branch..."

[AI deletes the branch]

**AI**: "Branch deleted. Your main code is unchanged - exactly as it was before. Want to try a different approach?"

---

## A Complete Example

**You**: "I want to try adding NumPy to my calculator, but I'm not sure if it's worth it."

**AI**: "I'll create a test branch called 'try-numpy' so we can experiment safely."

[AI creates branch]

**AI**: "Branch created! Now on 'try-numpy'. What should I do?"

**You**: "Rewrite add() to use NumPy"

**AI**: "Converting add() to use NumPy..."

[AI makes changes]

**AI**: "Done! The function now uses NumPy for faster math. Test it?"

**You**: "Yes, test it"

**AI**: "Testing..."

[AI runs tests]

**AI**: "⚠️ Found a problem! The NumPy version crashes with empty lists. Should I:
1. Fix the bug and try again
2. Delete this branch and try a different approach
3. Keep investigating"

**You**: "Fix it"

**AI**: "Adding empty list check..."

[AI fixes bug]

**AI**: "Fixed! Now testing again..."

[AI tests]

**AI**: "All tests pass! The NumPy version is 5x faster and handles edge cases. Merge to main?"

**You**: "Yes!"

**AI**: "Merged and cleaned up. Your main code now uses NumPy safely."

---

## Key Points

**Branches let you**:
- Test big AI changes safely
- Keep your main code protected
- Try multiple approaches
- Delete experiments that don't work

**The pattern**:
1. Create branch (safe copy)
2. AI changes code there
3. Test thoroughly
4. Keep (merge) or delete (discard)
5. Main code only changes if you approve

**Remember**: Experiments are free when your main code is safe!

---

## When to Use Branches

**Use a branch when**:
- AI wants to make big changes
- You're trying something experimental
- You're not sure if changes will work
- You want to test before committing

**Don't need a branch when**:
- Making tiny changes (like fixing a typo)
- Changes are super simple
- You're already testing on a branch

**Rule of thumb**: If you're nervous about changes, use a branch.

---

## Try With AI

Practice the branch workflow.

**Tool**: Claude Code, Gemini CLI, or ChatGPT

### Exercise 1: Create and Use a Branch

```
Help me practice branches:
1. Create a branch called "test-feature"
2. Make a small change to any file
3. Show me what changed
4. Merge it back to main
5. Delete the branch

Walk me through each step.
```

What to expect: AI creates branch, makes changes, merges, and cleans up.

### Exercise 2: Test and Discard

```
Create a branch to test something.
Make a change that we'll discard.
Then delete the branch without merging.

Confirm main is unchanged afterward.
```

What to expect: AI creates branch, makes changes, deletes branch, proves main is safe.

### Exercise 3: Understanding Safety

```
Explain why branches make AI work safer.
Give me a specific example of when a branch
would save me from a big mistake.
```

What to expect: AI explains with concrete example.

---

## What's Next

In Lesson 6, you'll learn how to push branches to GitHub so your experiments are backed up in the cloud. In Lesson 7, you'll learn **Pull Requests** - how to ask others to review your branches before merging.

**Key takeaway**: Branches = Experiment fearlessly. Your main code stays safe until you're ready to merge.
