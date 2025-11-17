# My Git Workflow for AI-Assisted Development

*Personal reference guide for safe, professional development*

**Created**: [Your Date]
**Last Updated**: [Today's Date]

---

## Pattern 1: Commit Before Experiment

### When to Use This
- Before asking AI to make any changes to code
- Before pulling from GitHub (to have a restore point)
- Anytime you think "this might go wrong"
- After completing a working feature before starting next task

### The Workflow

```bash
# Step 1: Check what you're about to commit
git status
# Should show what's modified or new

# Step 2: Understand the changes
git diff
# Review specific changes you're about to save

# Step 3: Stage relevant files (be selective!)
git add [specific files or .]
# Examples:
# git add calculator.py          # Single file
# git add .                      # All files

# Step 4: Commit with clear message about what you're preserving
git commit -m "Before [task]: [brief context]"
```

### Example Commit Messages
- ✓ "Before refactor: working calculator"
- ✓ "Before AI feature: existing authentication system"
- ✓ "Before performance optimization: baseline version"
- ✗ "stuff" (too vague)
- ✗ "update" (doesn't explain what's being preserved)

### Questions to Ask Myself
- [ ] Do I understand what I'm committing?
- [ ] If this experiment fails, will I want to return to this exact state?
- [ ] Is my commit message clear enough for future me to understand?

### Principles
- **Commit Intentionally**: Every commit is a conscious decision, not automatic
- **Message Clarity**: "Before X" messages explicitly signal a restore point
- **Selective Staging**: Don't commit unrelated work—stay focused

---

## Pattern 2: Branch-Test-Merge for Alternatives

### When to Use This
- Testing two or more AI implementations of the same feature
- When main branch is working and you want to keep it that way
- Experimenting with significant changes
- When uncertain about outcome before merging

### The Workflow

#### Step 1: Create Branch for Experiment
```bash
# Create and switch to new branch with descriptive name
git checkout -b feature/[clear-name]

# Examples:
# git checkout -b feature/add-validation
# git checkout -b feature/optimize-performance
# git checkout -b feature/refactor-auth
```

#### Step 2: Let AI Implement on Branch
```bash
# Ask AI to implement the feature on this branch
# Tell AI: "Implement [feature description]"
# AI makes changes, you commit them

# Check what was generated
git log --oneline -5

# View differences from main
git diff main
```

#### Step 3: Test the Implementation
```bash
# Execute your test suite / manual testing
# Run: python main.py, npm test, etc.
# Note: DO NOT merge yet—only test locally

# Questions to answer:
# - Does it work correctly?
# - Is it better than alternatives (if multiple branches)?
# - Would you want this code in main?
# - Are there bugs or issues?
```

#### Step 4: Keep or Discard (The Decision)

**Option A: Keep Changes → Merge to Main**
```bash
# If tests pass and you like the implementation:
git checkout main          # Switch back to main
git merge feature/[name]   # Merge the branch
git branch -d feature/[name]  # Delete completed branch
git push                   # Backup to GitHub
```

**Option B: Discard Changes → Delete Branch**
```bash
# If tests fail or you don't like the approach:
git checkout main          # Switch back to main
git branch -D feature/[name]  # Force delete without merging
# The feature code is gone—main is unchanged
git push                   # Backup to GitHub
```

### Questions to Ask Myself
- [ ] Have I tested thoroughly before merging?
- [ ] Can I explain why this branch is better than alternatives?
- [ ] Is my branch name descriptive enough to remember later?
- [ ] Would I want to look at this code in 6 months?

### Principles
- **Parallel Safety**: Never modify main directly when uncertain
- **Test Before Commit**: Merge only after validation
- **Easy Discard**: If branch fails, delete it—no harm done, main is protected

---

## Pattern 3: Push for Backup and Recovery

### When to Use This
- Daily (or after meaningful commits)
- Before risky operations
- After merging important features
- At end of work day

### The Workflow

#### Step 1: Verify Local State is Clean
```bash
# Check that everything is committed
git status
# Should show: "On branch main, nothing to commit, working tree clean"

# See recent commits
git log --oneline -5
```

#### Step 2: Push to GitHub

**First-time setup (one per repository):**
```bash
git remote add origin https://github.com/[your-username]/[repo-name].git
git push -u origin main
# This creates the connection and pushes code
```

**Subsequent pushes (after first setup):**
```bash
# All commits from main branch go to GitHub
git push
```

#### Step 3: Verify Backup Worked
```bash
# (Not a Git command, but important validation step)
# 1. Open your browser
# 2. Go to https://github.com/[your-username]/[repo-name]
# 3. Verify you see your commits there
# 4. Verify you see your branch names there
# This confirms backup is successful
```

### Questions to Ask Myself
- [ ] Is everything committed locally before I push?
- [ ] Can I access my code from GitHub right now?
- [ ] Would I recover my work if my computer broke today?
- [ ] When did I last push? (Should be today)

### Principles
- **Backup Discipline**: Remote is not optional; it's your safety net
- **Verify Backup**: Don't assume push worked—check GitHub
- **Frequency**: Push at least daily; push immediately after major features

---

## My Decision Framework

### Facing a Git Decision?

**Q: "Should I commit directly to main?"**
- Only if: It's a tiny fix and you're 100% confident
- Otherwise: Use Pattern 1 (save current state first) or Pattern 2 (test on branch)

**Q: "Should I test this on a branch or commit first?"**
- If uncertain about outcome: Pattern 2 (Branch-Test-Merge)
- If just saving known-good state: Pattern 1 (Commit Before Experiment)

**Q: "How often should I push to GitHub?"**
- At least once daily
- Immediately after completing major features
- Never go more than 1 hour of work without pushing

**Q: "What if I make a mistake?"**
- Refer to "Error Recovery" section below

---

## Error Recovery

### Scenario: Committed to main instead of branch

```bash
# You committed directly to main but wanted a branch
# Solution:

# Create new branch from current main
git checkout -b feature/[name]

# Go back to previous commit on main
git checkout main
git reset --hard HEAD~1

# Now you have:
# - main: back to before your change
# - feature/[name]: has your change
# Go back to feature branch and test it
git checkout feature/[name]
```

### Scenario: Merged wrong branch

```bash
# You merged the wrong branch to main
# Solution:

# Undo the merge
git reset --hard HEAD~1

# main is now back to before merge
# Nothing is lost—the branch still exists
git branch  # List all branches to find the one you actually wanted
```

### Scenario: Pushed something you didn't want

```bash
# You pushed to GitHub but realize you don't want those commits
# Solution (for most cases):

# Create new commit that undoes the bad one
git revert [commit-hash]
# Shows the commit hash in: git log

# This is safer than force-push for learning
git push

# Everyone can see the undo happened (transparency)
```

---

## My Workflow at a Glance

```
Morning:
1. Start day: git status (Am I clean?)
2. git pull (Get latest from GitHub)

During Work:
3. Before AI changes: Commit current state (Pattern 1)
4. AI generates code: Create branch if uncertain (Pattern 2)
5. Test locally
6. Decision: Keep (merge) or discard (delete branch)

End of Work:
7. Final push to GitHub (Pattern 3)
8. Verify on GitHub (backup confirmed)
9. End of day: Everything backed up
```

---

## Commands Reference

| Task | Command |
|------|---------|
| Check repository status | `git status` |
| View recent commits | `git log --oneline -5` |
| See what changed | `git diff` |
| Stage all changes | `git add .` |
| Stage specific file | `git add filename.py` |
| Commit with message | `git commit -m "message"` |
| Create branch | `git checkout -b feature/name` |
| Switch branch | `git checkout branch-name` |
| List branches | `git branch` |
| Merge branch | `git merge feature/name` |
| Delete branch | `git branch -d feature/name` |
| Force delete branch | `git branch -D feature/name` |
| Push to GitHub | `git push` |
| Pull from GitHub | `git pull` |
| View diff from main | `git diff main` |

---

## Notes & Customizations

Use this space to add patterns specific to your workflow:

### Pattern 4: [Your Pattern Name]
- When to use:
- The workflow:
- Questions to ask:
- Principles:

### Pattern 5: [Your Pattern Name]
- When to use:
- The workflow:
- Questions to ask:
- Principles:

---

## Last Revision Notes

- **Revision Date**: ___________
- **What Changed**: ___________
- **Why**: ___________

---

*Keep this file in your project root: `/your-project/git-workflow.md`*

*Copy and customize for each new project. Update as you discover new patterns.*
