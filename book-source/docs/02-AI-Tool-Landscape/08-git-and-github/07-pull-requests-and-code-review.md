---
sidebar_position: 7
title: "Pull Requests and Code Review"
description: "Create pull requests documenting AI assistance, review changes, address feedback, and merge professionally"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Create Pull Request"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student can create a pull request with clear title, description, testing instructions, and documentation of AI assistance"

  - name: "Review Code Changes"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can examine code diffs in a PR, understand what changed, and provide feedback on specific lines"

  - name: "Address Feedback"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student can update code based on review feedback, commit changes, and have PR automatically reflect updates"

  - name: "Merge Safely"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Remember"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can merge PR after approval and delete the feature branch from GitHub"

learning_objectives:
  - objective: "Create pull requests documenting changes and AI assistance"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student writes clear PR description with title, what changed, why, testing instructions, and AI assistance documentation"

  - objective: "Review code changes in a pull request by examining diffs"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student examines PR diff, identifies specific changes, and provides actionable feedback"

  - objective: "Handle code review feedback and update pull requests"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student makes requested changes, commits, and pushes (PR auto-updates)"

  - objective: "Merge pull requests and clean up branches"
    proficiency_level: "A1"
    bloom_level: "Remember"
    assessment_method: "Student merges PR and deletes feature branch after approval"

cognitive_load:
  new_concepts: 5
  assessment: "5 new concepts (Pull Request, Diff, Code Review, Discussion, Merge) within A2 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Explore advanced PR practices: code review standards, addressing specific comment threads, using PR templates for documentation consistency"
  remedial_for_struggling: "Focus on the pull request as a 'conversation with your code' using the given template; practice reviewing a simple PR diff before creating one"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/012-chapter-8-git-github-aidd/plan.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "1.0.0"
---

# Pull Requests and Code Review

## The Problem

You tested changes on your branch. Everything works great! Now what?

**Old way**: Just merge to main and hope nothing breaks.

**Smart way**: Create a Pull Request (PR) - a safety check before merging.

**Think of it like this**: You finished a draft. You want someone (or future-you) to review it before publishing. That's a PR.

**Time**: 20 minutes

---

## What Is a Pull Request?

A **Pull Request** is like saying: "I'm done with these changes. Please check them before we add them to main."

Simple flow:

```
Branch (your changes) → Pull Request → Review → Merge to Main
```

**Why this matters**:
- Last chance to review before merging
- Shows what changed (side-by-side comparison)
- Documents why you made changes
- Looks professional on GitHub

---

## Simple Analogy

**Submitting homework**:
- Branch = Your completed assignment
- Pull Request = Handing it in for grading
- Review = Teacher checks your work
- Merge = Assignment accepted, grade recorded

**Same with code**:
- Branch = Your finished code
- Pull Request = Asking to merge it
- Review = Check for problems
- Merge = Changes go to main

---

## Why Pull Requests Matter

**For you learning**:
- Review AI-generated code one more time
- Document what AI helped with
- Keep a record of changes
- Practice professional workflow

**For teams**:
- Everyone sees changes before they go live
- Catch mistakes early
- Share knowledge
- Maintain quality

---

## The Simple Workflow

### Task 1: Push Your Branch to GitHub

**What you want**: Get your branch from your computer to GitHub

**Instead of**: Typing Git commands

**Just ask your AI**:
- "Push this branch to GitHub"
- "Upload my branch"
- "Send my changes to GitHub"

### Example

**You**: "I finished working on my 'add-calculator' branch. Push it to GitHub."

**AI**: "I'll push your branch to GitHub..."

[AI pushes the branch]

**AI**: "Done! Your 'add-calculator' branch is now on GitHub. Ready to create a Pull Request?"

**You**: "Yes! How do I do that?"

**AI**: "Go to your GitHub repository. You'll see a yellow banner that says 'add-calculator had recent pushes' with a green button 'Compare & pull request'. Click it."

---

### Task 2: Create the Pull Request

**What you want**: Tell GitHub you want to merge your branch

**Where to do it**: GitHub website (not AI)

**Steps**:

1. Go to your repository on GitHub
2. Look for the yellow banner at the top
3. Click "Compare & pull request" (green button)
4. Fill in title and description
5. Click "Create Pull Request"

---

### Task 3: Write the Description

**What you want**: Explain what you changed and why

**Just ask your AI**:
- "Help me write a PR description"
- "What should I say in my Pull Request?"
- "Explain my changes for GitHub"

### Simple Example

**You**: "Help me write a PR description. I added a calculator with add, subtract, multiply, divide. AI generated most of the code. All tests pass."

**AI**: "Here's a clear description:

**Title**: Add calculator module

**Description**:
Added a calculator with 4 functions:
- add()
- subtract()
- multiply()
- divide() (handles division by zero)

**What AI helped with**:
- Generated all calculator functions
- Created unit tests
- Added error handling

**How to test**:
Run: python test_calculator.py
All tests should pass (8 tests)

Want me to copy this for you?"

**You**: "Yes!"

**AI**: "Copied! Now paste it into GitHub's description box."

---

### What to Include

**Title**: Short summary (5-10 words)
- Example: "Add calculator module"

**Description**: Answer 3 questions:

1. **What changed?** (list main changes)
2. **What did AI do?** (be transparent)
3. **How to test?** (give simple steps)

---

### Task 4: Review Your Changes

**What you want**: Check what will be merged

**Where to look**: GitHub shows a "diff" (side-by-side comparison)

**You can**:
- See what changed (green = added, red = removed)
- Leave comments on specific lines
- Approve or request changes

### If Someone Leaves Feedback

**You**: "Someone said to add better error messages. How do I fix this?"

**AI**: "I'll help you:

1. I'll update the code with better error messages
2. Commit the changes
3. Push to your branch

GitHub will automatically update your PR with the new changes. Ready?"

**You**: "Yes, do it"

**AI**: "Updated! The PR now shows your new changes. The reviewer can check again."

---

### Task 5: Merge the Pull Request

**What you want**: Add your changes to main

**When to do it**: After reviewing (or when others approve)

**Instead of**: Git commands

**Just click on GitHub**:

1. Go to your PR page
2. Click green "Merge Pull Request" button
3. Click "Confirm Merge"
4. Done! Changes are now in main

### After Merging

**What happens**:
- PR marked as "merged" (purple badge)
- Your branch can be deleted (GitHub offers a button)
- Changes are now in main code

**You**: "Should I delete my branch now?"

**AI**: "Yes! Once merged, you don't need the branch. Click 'Delete branch' on GitHub. I'll also delete it locally for you."

[AI cleans up local branch]

**AI**: "All clean! Your main branch now has all the changes."

---

## A Complete Example

**You**: "I finished my calculator. AI wrote all the code. How do I create a good PR?"

**AI**: "I'll help you write a professional PR description. Tell me what the calculator does."

**You**: "It has add, subtract, multiply, and divide. Handles division by zero."

**AI**: "Great! Here's your PR description:

---

**Title**: Add calculator module

**What I built**:
A calculator with 4 functions:
- add() - adds two numbers
- subtract() - subtracts two numbers
- multiply() - multiplies two numbers
- divide() - divides with error handling for zero

**What AI did**:
- Generated all 4 functions
- Created unit tests (8 tests, all pass)
- Added error handling for division by zero
- Fixed bugs during testing

**How to test**:
Run: python test_calculator.py
All 8 tests should pass

---

Want me to copy this?"

**You**: "Yes! Does this look professional?"

**AI**: "Absolutely! This PR shows:
- What you built
- What AI helped with (transparent)
- How to test it (anyone can verify)
- All information clear and organized

Perfect for your GitHub portfolio!"

---

## Common Mistakes

### Mistake 1: Vague Description

**Bad**: "Added stuff"

**Good**: "Added calculator with 4 functions. AI generated code, all tests pass."

**Why**: People need to know what changed.

---

### Mistake 2: Not Mentioning AI Help

**Bad**: "Added calculator" (no mention of AI)

**Good**: "Added calculator. AI generated all functions. I tested everything."

**Why**: Be honest about AI's role.

---

### Mistake 3: Merging Broken Code

**Bad**: Create PR, tests fail, merge anyway

**Good**: Test first, fix problems, then create PR

**Why**: Don't merge broken code to main.

---

## Key Points

**Pull Requests let you**:
- Review changes one more time
- Document what AI did
- Look professional on GitHub
- Keep main code safe

**The workflow**:
1. Push branch to GitHub
2. Create Pull Request
3. Write clear description
4. Review changes
5. Merge when ready

**Remember**: A good PR description shows what you built, what AI helped with, and how to test it.

---

## Try With AI

Practice the Pull Request workflow.

**Tool**: Claude Code, Gemini CLI, or ChatGPT

### Exercise 1: Create Your First PR

```
I have a branch called "add-calculator" that's pushed to GitHub.
Walk me through creating a Pull Request step by step.
What do I click? What do I write?
```

What to expect: AI guides you through GitHub, explains each field, helps write description.

### Exercise 2: Write a PR Description

```
Help me write a PR description for my calculator:
- It has add, subtract, multiply, divide
- AI generated all the code
- All tests pass

Make it professional but simple.
```

What to expect: AI gives you a clear, copy-paste ready description.

### Exercise 3: Handle Feedback

```
Someone left a comment on my PR saying "add more tests".
How do I:
1. Add the tests
2. Update my PR with the changes
```

What to expect: AI explains: make changes locally → commit → push → PR auto-updates.

### Exercise 4: Merge and Clean Up

```
My PR is approved! Help me:
1. Merge it to main
2. Delete the branch
3. Clean up locally
```

What to expect: AI walks you through merge button, branch deletion, local cleanup.

### Exercise 5: Understanding PRs

```
Explain why Pull Requests are important.
What happens if I just merge without a PR?
```

What to expect: AI explains safety, documentation, and professional workflow benefits.

---

## What's Next

In Lesson 8, you'll set up your IDE (VS Code, Cursor, or Zed) with Git integration so you can manage branches and commits from your editor. In Lesson 9, you'll build a complete project where AI generates all the code while you handle all the Git operations.

**Key takeaway**: Pull Requests = Your final safety check. Review, document AI's help, then merge with confidence.
