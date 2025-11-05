---
sidebar_position: 9
title: "Capstone Exercise: Build with Git & GitHub"
description: "Integrate all Git, GitHub, and AI skills in a realistic calculator project demonstrating complete workflow"
keywords: [capstone, git workflow, github, calculator project, ai-assisted development]

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment, accreditation alignment, and differentiation
skills:
  - name: "Project Setup with Git"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student initializes a Git repository with proper documentation and creates initial commit"

  - name: "AI-Assisted Development"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student uses AI to generate code while reviewing outputs and committing appropriately"

  - name: "Branch-Based Testing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student creates feature branches, tests changes, and merges or discards appropriately"

  - name: "Safety Checkpoints"
    proficiency_level: "A2"
    category: "Soft"
    bloom_level: "Understand"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student commits before major changes and reviews AI-generated code before merging"

  - name: "GitHub Portfolio"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student connects project to GitHub and creates a professional pull request with clear documentation"

learning_objectives:
  - objective: "Initialize a Git project with README and initial commit"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Verify git init, README.md created, and initial commit in git log"

  - objective: "Use AI to generate complete Python code for calculator with add, subtract, multiply, divide functions"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Verify calculator.py exists and is committed with descriptive message"

  - objective: "Create a feature branch and safely test AI-generated enhancements"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Verify feature branch created, changes tested, and merged or discarded with reasoning"

  - objective: "Connect local repository to GitHub and push code"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Verify repository visible on GitHub with complete commit history"

  - objective: "Create and merge a pull request documenting AI assistance"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Verify pull request created with clear description of AI involvement and changes"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (project setup, AI-assisted code generation, feature branches, GitHub integration, PR workflow) within A2 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Extend calculator with additional features (exponentiation, square root, history); push to GitHub with multiple PRs showing git workflow mastery"
  remedial_for_struggling: "Pair with peer or AI assistant for each step; focus on understanding one concept at a time; extend timeline to 45 minutes if needed"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/012-chapter-8-git-github-aidd/plan.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "1.0.0"
---

# Capstone: Build Your First Project

## The Big Picture

You've learned Git piece by piece. Now you'll use EVERYTHING together to build a real project.

**The project**: A Python calculator
**Who writes code**: AI (not you!)
**Your job**: Manage Git, make decisions, review AI's work

**Time**: 30 minutes

---

## What You'll Do

Build a calculator project using:
- ✅ Git (track changes)
- ✅ Branches (test safely)
- ✅ GitHub (backup online)
- ✅ Pull Requests (professional workflow)
- ✅ AI (generates all code)

**Important**: You're not learning Python here. You're learning how to MANAGE a project with Git while AI writes the code.

---

## Simple Analogy

**Building a house**:
- Architect (you) = makes decisions, checks quality
- Construction team (AI) = does the actual building
- Building inspector (Git) = tracks every change
- Photo album (GitHub) = backup of progress

**Same with this project**:
- You = manage Git, make decisions
- AI = writes all the code
- Git = tracks every change
- GitHub = backup and portfolio

---

## The 6 Steps

Follow these in order:

---

## Step 1: Start the Project

**What you're doing**: Create folder, start Git, make first commit

**Just ask your AI**:

```
Create a folder called 'my-calculator'.
Initialize Git.
Create a README saying this is a calculator project.
Commit with message 'Initial project setup'.
```

### Example

**You**: "Create a new project folder called 'my-calculator', set up Git, add a README, and make the first commit."

**AI**: "I'll set everything up..."

[AI creates folder, initializes Git, creates README, commits]

**AI**: "Done! Your project is ready. Git log shows:
- Initial project setup ✓

You have a README.md file and Git is tracking changes."

**You**: "That was fast! What's next?"

**AI**: "Now we'll ask me to generate the calculator code."

---

---

## Step 2: AI Generates Calculator Code

**What you're doing**: Ask AI to write the calculator, review it, commit it

**Just ask your AI**:

```
Create a Python file called calculator.py with these functions:
- add(a, b) - adds two numbers
- subtract(a, b) - subtracts two numbers
- multiply(a, b) - multiplies two numbers
- divide(a, b) - divides with error handling

Save it and commit with message 'Add calculator module'.
```

### Example

**You**: "Generate a calculator.py file with add, subtract, multiply, and divide functions. Save and commit it."

**AI**: "I'll create the calculator for you..."

[AI generates code]

**AI**: "Here's what I created:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Error: Cannot divide by zero'
    return a / b
```

Saved to calculator.py and committed! Git log now shows:
1. Add calculator module ✓
2. Initial project setup"

**You**: "Does the divide function handle errors?"

**AI**: "Yes! If you try to divide by zero, it returns an error message instead of crashing."

---

---

## Step 3: Test Changes on Branch

**What you're doing**: Create branch, improve code, test safely

**Just ask your AI**:

```
Create a branch called 'add-tests'.
Generate unit tests for the calculator.
Save to test_calculator.py and commit.
```

### Example

**You**: "Create a branch called 'add-tests', generate pytest tests for the calculator, and commit them."

**AI**: "I'll create a safe testing branch..."

[AI creates branch, generates tests, commits]

**AI**: "Done! I'm on branch 'add-tests'. Created test_calculator.py with tests for:
- add()
- subtract()
- multiply()
- divide() (including division by zero)

Git log shows:
1. Add unit tests ✓
2. Add calculator module
3. Initial project setup

Main branch is untouched (safe!)."

**You**: "So if the tests are bad, I can just delete this branch?"

**AI**: "Exactly! That's why branches are safe. Test here, merge only if good."

---

---

## Step 4: Test and Merge

**What you're doing**: Run tests, if good → merge, if bad → fix or delete branch

**Just ask your AI**:

```
Run the tests. If they pass, merge to main and delete the branch.
If they fail, tell me what's wrong.
```

### Example

**You**: "Run the tests. If they all pass, merge this branch to main."

**AI**: "Running tests..."

[AI runs pytest]

**AI**: "All tests passed! ✓
- test_add: PASS
- test_subtract: PASS
- test_multiply: PASS
- test_divide: PASS
- test_divide_by_zero: PASS

Ready to merge?"

**You**: "Yes, merge it!"

**AI**: "Merging to main... Done! Deleting 'add-tests' branch... Complete!

Git log now shows all changes merged to main. You're back on main branch."

**You**: "What if tests had failed?"

**AI**: "Then I'd tell you what broke, we'd fix it, test again, and only merge when all tests pass."

---

---

## Step 5: Push to GitHub

**What you're doing**: Backup code to GitHub

**Just ask your AI**:

```
Create a GitHub repository called 'my-calculator'.
Connect my local project to GitHub.
Push all my code.
```

### Example

**You**: "Push my calculator project to GitHub. Repository name: my-calculator."

**AI**: "I'll set up GitHub for you:

1. Go to github.com/new
2. Name: my-calculator
3. Make it Public
4. Create repository

Tell me when done."

**You**: "Created!"

**AI**: "Connecting and pushing..."

[AI connects to GitHub, pushes code]

**AI**: "Done! Your code is now on GitHub at:
github.com/yourusername/my-calculator

Go check it out - all your files and commits are there!"

---

---

## Step 6: Create Pull Request

**What you're doing**: Professional workflow with PR documentation

**Just ask your AI**:

```
Create a branch called 'improve-docs'.
Add better documentation to calculator.py.
Push to GitHub and help me create a Pull Request.
```

### Example

**You**: "Create a branch for improving documentation, make the changes, and help me create a Pull Request on GitHub."

**AI**: "Creating documentation branch..."

[AI creates branch, adds docstrings, pushes]

**AI**: "Done! Branch 'improve-docs' is pushed to GitHub. Now:

1. Go to github.com/yourusername/my-calculator
2. Click 'Pull Requests'
3. Click 'New Pull Request'
4. Select 'improve-docs' → 'main'
5. Title: 'Improve documentation'
6. Description: Say what you changed and that AI helped

Then merge it!"

**You**: "Merged! Now what?"

**AI**: "Pull the changes locally..."

[AI pulls from GitHub]

**AI**: "Perfect! Your project is complete. You have:
- Working calculator code (AI generated)
- Unit tests (AI generated)
- Clean Git history
- Professional Pull Request
- Code on GitHub (portfolio!)

You managed the whole workflow with Git. That's professional development!"

---

---

## Success Checklist

Did you complete everything? Check off:

**Your Project Has:**
- [ ] Git repository with clean history
- [ ] calculator.py with 4 functions
- [ ] test_calculator.py with tests
- [ ] README explaining the project
- [ ] Code on GitHub (public)
- [ ] Pull request created and merged

**You Can Now:**
- [ ] Explain what Git tracks
- [ ] Create branches for safe testing
- [ ] Review AI-generated code before committing
- [ ] Push code to GitHub
- [ ] Create professional pull requests
- [ ] Use Git for any future project

**You Understand:**
- [ ] Why branches keep code safe
- [ ] Why testing before merging matters
- [ ] How GitHub backs up your work
- [ ] That AI writes code, you manage quality

---

## What You Learned

**You can now**:
- Start any project with Git
- Let AI write code while you manage quality
- Test changes safely on branches
- Back up code to GitHub
- Create professional pull requests
- Build a portfolio project

**Key lessons**:
- Git = safety net for your code
- Branches = test without breaking main
- GitHub = cloud backup + portfolio
- AI = your coding partner (you're the manager)
- Testing before merging = professional practice

**This applies to ALL projects** - not just calculators. Every software project uses these same Git workflows.

---

## Optional: Extend Your Project

Want more practice? Try these:

**Add More Features**:
```
Add these functions to calculator:
- power(a, b)
- square_root(a)
- factorial(n)

Use the same workflow: branch → code → test → merge.
```

**Improve It**:
```
Review the calculator. What's missing?
Add better error messages, input validation, or logging.
Create a PR for each improvement.
```

**Share It**:
- Post your GitHub link on social media
- Show it to friends learning to code
- Add it to your resume/portfolio
- Keep building more projects using Git

**Every project you build** reinforces these Git skills. The more you practice, the more natural it becomes.

---

## Try With AI

Follow the 6 steps with your AI. Use one long conversation with these prompts:

**Tool**: Claude Code, Gemini CLI, or ChatGPT

### Complete Workflow (Copy All 6 Prompts)

```
Step 1: Create folder 'my-calculator', initialize Git, add README, commit.

Step 2: Generate calculator.py with add, subtract, multiply, divide functions. Include error handling. Save and commit.

Step 3: Create branch 'add-tests'. Generate pytest tests for all functions. Save to test_calculator.py and commit.

Step 4: Run tests. If they pass, merge to main and delete branch.

Step 5: Create GitHub repository 'my-calculator'. Connect local to GitHub. Push all code.

Step 6: Create branch 'improve-docs'. Add better docstrings. Push to GitHub. Help me create Pull Request, then merge it.

Walk me through each step and confirm completion before moving to the next.
```

### What to Expect

Your AI will:
1. Create project structure
2. Generate all code (calculator + tests)
3. Manage Git operations (branch, commit, merge)
4. Connect to GitHub and push
5. Guide you through Pull Request

You'll end with:
- Working calculator on GitHub
- Clean Git history
- Professional Pull Request
- Portfolio project!

---

## What's Next

**You now have**:
- Complete Git & GitHub skills
- AI collaboration experience
- Portfolio project on GitHub
- Professional workflow knowledge

**Continue learning**:
- Build more projects using this workflow
- Try collaborating with others
- Learn Python to improve the calculator
- Deploy your project online

**Key takeaway**: You managed a complete project like a professional developer. AI wrote the code, you handled Git, testing, and quality control. That's modern software development!


