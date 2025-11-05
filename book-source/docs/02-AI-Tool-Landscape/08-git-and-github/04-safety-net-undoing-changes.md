---
sidebar_position: 4
title: "Safety Net: Undoing Changes"
description: "Learn how to undo mistakes safely with Git and AI"

# HIDDEN SKILLS METADATA
skills:
  - name: "View File Changes"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can ask AI to show what changed"

  - name: "Undo Uncommitted Work"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information & Data Literacy"
    measurable_at_this_level: "Student can discard changes with AI help"

  - name: "Undo Committed Work Safely"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information & Data Literacy"
    measurable_at_this_level: "Student can undo commits safely with AI guidance"

  - name: "Recognize Danger Zones"
    proficiency_level: "A1"
    category: "Soft"
    bloom_level: "Understand"
    digcomp_area: "Safety & Security"
    measurable_at_this_level: "Student knows when undoing is dangerous"

learning_objectives:
  - objective: "View changes before deciding to keep or undo"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Student asks AI to show changes"

  - objective: "Safely discard unwanted changes"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Student undoes changes with AI help"

  - objective: "Identify safe vs dangerous undo methods"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Student can explain which methods are safe"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (view, discard, undo commit, revert, danger zones) within A2 limit ✓"

# Generation metadata
generated_by: "lesson-writer"
source_spec: "specs/012-chapter-8-git-github-aidd/plan.md"
created: "2025-11-05"
last_modified: "2025-11-05"
version: "2.0.0"
---

# Safety Net: Undoing Changes

## The Problem

Your AI assistant refactored your code. You tested it. Something broke. Now what?

**Good news**: Git lets you undo mistakes. Always.

This lesson teaches you how to go back when things go wrong.

**Time**: 20 minutes

---

## Why This Matters with AI

AI makes changes fast. Sometimes:
- AI's code looks good but breaks things
- You commit something and realize it's wrong
- You want to try AI's idea but keep your old version safe

Git has your back. You can always undo.

---

## Three Types of Undo

### 1. "Show me what changed"
Before deciding to keep or undo, look at the changes first.

### 2. "I don't like this, throw it away"
Undo changes you haven't saved yet (not committed).

### 3. "I saved this but it was wrong, undo it"
Undo changes you already committed.

Let's learn each one.

---

## Type 1: Show Me What Changed

**What you want**: See exactly what's different before deciding

**Instead of**: `git diff`

**Just ask your AI**:
- "Show me what changed"
- "What files did I modify?"
- "Display the differences"
- "What's different from my last save?"

### Simple Example

**You**: "Show me what changed"

**AI**: "Let me check your changes..."

[AI looks at differences]

**AI**: "You modified calculator.py:
- Added a new multiply() function
- Changed how add() works

Want me to show you the exact lines that changed?"

**You**: "Yes, show me"

**AI**: "In calculator.py:
- Line 8: You added 'def multiply(a, b):'
- Line 15: You changed 'return a + b' to 'return sum([a, b])'

The multiply function is new. The add function now works differently."

**You**: "I don't like the change to add(). Can I undo just that?"

**AI**: "Yes! I can undo just the add() change and keep the multiply() function. Should I?"

**Key point**: You see what changed before deciding what to keep or undo.

---

## Type 2: Throw Away Changes (Not Saved Yet)

**What you want**: Discard changes you haven't committed

**Instead of**: `git checkout` or `git restore`

**Just ask your AI**:
- "Throw away my changes"
- "Undo everything since last save"
- "Go back to last commit"
- "Discard all changes"

### Simple Example

**You**: "I changed calculator.py but I don't like it. Throw it away."

**AI**: "I'll discard all changes to calculator.py. This will:
- Delete any new code you added
- Restore the file to your last commit

Are you sure? This can't be undone."

**You**: "Yes, do it"

**AI**: "Done! calculator.py is back to your last save point. All changes removed."

**You**: "What if I only want to undo changes to one file?"

**AI**: "Just say 'undo changes to calculator.py' and I'll restore only that file. Other files stay as they are."

### Safety Note

⚠️ **This deletes your work!** Make sure you really want to discard the changes.

✅ **Safe because**: You hadn't committed yet, so you can ask AI to recreate the code if you change your mind.

---

## Type 3: Undo a Commit (Already Saved)

Sometimes you commit code and then realize it was wrong.

### Option A: Safe Undo (Recommended)

**What you want**: Undo the commit but keep the changes so you can fix them

**Instead of**: `git reset --soft`

**Just ask your AI**:
- "Undo my last commit but keep the changes"
- "Uncommit but don't delete my work"
- "I want to fix my last commit"

### Simple Example

**You**: "I committed too fast. Undo the last commit but keep my changes."

**AI**: "I'll undo your last commit. Your changes will stay, but they won't be saved yet. You can fix them and commit again."

[AI undoes the commit]

**AI**: "Done! Your last commit is undone. Your changes are still there, ready for you to fix and commit again."

**You**: "So nothing is deleted?"

**AI**: "Correct! Your code is still there, just not committed. It's like you pressed 'undo' on the save, but your work is safe."

✅ **Very safe**: Nothing is deleted. You can fix and recommit.

---

### Option B: Create an Undo Commit (Super Safe)

**What you want**: Keep the bad commit in history, but add a new commit that undoes it

**Instead of**: `git revert`

**Just ask your AI**:
- "Create a commit that undoes my last commit"
- "Reverse my last change but keep history"
- "Undo publicly with a new commit"

### Simple Example

**You**: "I pushed bad code to GitHub. How do I undo it safely?"

**AI**: "Since you already pushed, I'll create a new commit that reverses your changes. This way:
- The bad commit stays in history (so people can see it)
- A new commit undoes it
- Everything is transparent

Should I proceed?"

**You**: "Yes"

**AI**: "Creating undo commit..."

[AI creates the revert commit]

**AI**: "Done! I created a new commit called 'Revert: Add broken feature'. Your code is back to how it was before, and both commits are in the history."

**You**: "Why not just delete the bad commit?"

**AI**: "If you already pushed to GitHub, others might have downloaded your code. Deleting the commit would confuse them. Reverting is the professional way to undo public mistakes."

✅ **Safest option**: Nothing is deleted. Everything is transparent.

---

### Option C: Permanent Delete (DANGER!)

**What you want**: Completely delete a commit and all its changes

**Instead of**: `git reset --hard`

**Ask your AI**: "Permanently delete my last commit"

### Warning Example

**You**: "Delete my last commit completely"

**AI**: "⚠️ WARNING: This will **permanently delete**:
- Your last commit
- All changes in that commit
- You CANNOT get them back

This is dangerous! Are you absolutely sure?

Safer alternatives:
1. Undo the commit but keep changes (safe)
2. Create a reverse commit (safest)

Which do you want?"

**You**: "I'm sure, it was an accident"

**AI**: "Okay, deleting permanently..."

[AI deletes the commit]

**AI**: "Deleted. The commit is gone forever."

⚠️ **Use with extreme caution**: Only when you're 100% certain.

❌ **Dangerous because**: You can't get it back.

---

## When to Use Each Method

**Situation**: AI changed my code, I haven't committed yet, I don't like it
→ **Ask AI**: "Throw away these changes"

**Situation**: I committed code but forgot to add a comment
→ **Ask AI**: "Undo my last commit but keep the changes"

**Situation**: I pushed bad code to GitHub that broke things
→ **Ask AI**: "Create a commit that undoes my last commit"

**Situation**: I accidentally committed my password (very rare!)
→ **Ask AI**: "I need to permanently delete my last commit"
→ Then immediately change your password!

---

## A Complete Example

**You**: "I asked AI to optimize my code. Let me see what it changed."

**AI**: "It modified 3 files: calculator.py, utils.py, test.py. Want details?"

**You**: "Yes, show calculator.py"

**AI**: "AI changed the add() function to use NumPy. Looks 20% faster."

**You**: "Hmm, let me test it first. Stage and commit these changes."

**AI**: "Committed! Message: 'Optimize calculator with NumPy'"

**You**: "Now let me test it..."

[You test, it crashes with empty lists]

**You**: "It crashes! Undo that commit but keep the code so I can fix it."

**AI**: "Undoing commit... Done! Your changes are back but not committed. Fix the bug and I'll help you commit again."

**You**: "AI, fix the empty list crash"

**AI**: "Fixed! Added a check for empty lists. Want to commit this?"

**You**: "Yes, commit with message 'Optimize calculator and fix empty list bug'"

**AI**: "Committed! This version is tested and safe."

---

## Remember

Git + AI = Fear-free coding

**Key points**:
- Always see what changed before deciding
- Undo uncommitted work easily (just ask AI)
- Undo commits safely (AI keeps your work)
- Only use permanent delete when absolutely necessary

**The pattern**:
1. Try something
2. Test it
3. If bad, ask AI to undo
4. Try differently
5. Repeat until it works

---

## Try With AI

Practice undoing changes safely.

**Tool**: Claude Code, Gemini CLI, or ChatGPT

### Exercise 1: View Changes

```
I modified a file but haven't committed yet.
Show me what changed in simple terms.
```

What to expect: AI shows your changes clearly.

### Exercise 2: Discard Changes

```
I don't like my changes. Throw them away
and go back to my last commit.
```

What to expect: AI discards changes and confirms.

### Exercise 3: Undo a Commit Safely

```
I just committed something but made a mistake.
Undo my last commit but keep the changes so I can fix them.
```

What to expect: AI undoes commit, your work stays safe.

### Exercise 4: Understanding Danger

```
Explain the difference between:
1. Undoing a commit but keeping changes
2. Permanently deleting a commit

Which is safer and why?
```

What to expect: AI explains safety levels clearly.

---

## What's Next

In Lesson 5, you'll learn **branches** - the ultimate safe way to experiment. You'll create a copy of your code, test AI's changes there, and only merge if they work.

**Key takeaway**: With Git + AI, you never lose work. You can always undo, try again, and experiment freely.
