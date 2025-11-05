---
title: "GitHub Integration"
chapter: 8
lesson: 6
sidebar_position: 6
duration_minutes: 20
description: Connect your local Git repository to GitHub, authenticate securely, and keep your code backed up online.

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Add Remote Repository"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can connect a local Git repository to a GitHub repository using git remote commands"

  - name: "Authenticate Securely"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student understands the difference between SSH and Personal Access Token authentication and can choose appropriate method"

  - name: "Push and Pull"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can upload commits to GitHub (push) and download updates (pull) to keep local and remote in sync"

learning_objectives:
  - objective: "Connect a local Git repository to a GitHub repository"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Exercise demonstrating successful remote connection"

  - objective: "Authenticate to GitHub using a secure method (Personal Access Token recommended)"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Explanation of authentication choice and successful authentication"

  - objective: "Push commits to GitHub and verify they appear online"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Exercise showing code on GitHub after push"

cognitive_load:
  new_concepts: 5
  assessment: "5 new concepts (remote, origin, SSH, Personal Access Token, push/pull) at A1-A2 limit ✓"

differentiation:
  extension_for_advanced: "Explore SSH key setup and compare security models between PAT and SSH; research GitHub security best practices"
  remedial_for_struggling: "Use AI assistant to guide each step of remote setup and authentication; practice with simple test files before pushing real projects"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/012-chapter-8-git-github-aidd/plan.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "1.0.0"
---

# GitHub Integration

## The Problem

Your code is only on your computer. What if:
- Your computer breaks? (code is lost)
- You want to work from a different computer? (code is trapped)
- You want to show your work to someone? (can't share easily)

**Solution**: GitHub - cloud backup for your code.

**Time**: 20 minutes

---

## What Is GitHub?

**GitHub** is like Google Drive, but for code.

**Simple explanation**:
- Your code sits on your computer (local)
- You upload it to GitHub (cloud)
- Now it's backed up and you can access it anywhere

**Why this matters**:
- Safe backup (if computer dies, code survives)
- Work from anywhere (laptop, desktop, anywhere)
- Professional portfolio (employers look at your GitHub)
- Collaboration (work with others)

---

## Simple Analogy

**Saving photos**:
- Photos on phone = local
- Upload to Google Photos = cloud backup
- Access from any device = anywhere, anytime

**Same with code**:
- Code on computer = local Git
- Upload to GitHub = cloud backup
- Access from any device = work anywhere

---

## Step 1: Create Repository on GitHub Website

**What you need**: A GitHub account (free at github.com)

**Steps** (do this on GitHub website):

1. Go to **github.com**
2. Click **"New repository"** button (green button or "+" in top right)
3. Fill in:
   - **Name**: `my-project` (or whatever you want)
   - **Description**: "My first project" (optional)
   - **Public** (so others can see your work)
4. Click **"Create repository"**

**After creating**: GitHub shows you a page with commands. Don't worry about them yet - your AI will handle it.

---

## Step 2: Connect to GitHub

**What you want**: Link your local code to GitHub

**Instead of**: Typing Git commands

**Just ask your AI**:
- "Connect my code to GitHub"
- "Link this project to my GitHub repository"
- "Set up GitHub for this project"

### Example

**You**: "I created a repository on GitHub called 'my-calculator'. Connect my local code to it."

**AI**: "I'll connect your local repository to GitHub. What's your GitHub username?"

**You**: "myusername"

**AI**: "Setting up the connection..."

[AI runs the connection command]

**AI**: "Done! Your local code is now linked to GitHub. Ready to push your code?"

**You**: "How do I know it worked?"

**AI**: "I'll show you the connected repositories..."

[AI checks the connection]

**AI**: "Connection confirmed! Your repository is linked to: github.com/myusername/my-calculator"

---

## Step 3: Set Up Authentication

**The problem**: GitHub needs to know it's really you uploading code.

**Solution**: Create a special password (called a "token").

**Just ask your AI**:
- "Help me set up GitHub authentication"
- "I need a token to push to GitHub"
- "Walk me through GitHub authentication"

### Example

**You**: "I need to push my code but GitHub needs authentication. Help me."

**AI**: "I'll help you create a Personal Access Token. Here's what to do:

1. Go to github.com → Your profile picture → Settings
2. Scroll down → Developer settings
3. Personal access tokens → Tokens (classic)
4. Generate new token
5. Give it a name: 'My computer'
6. Check the 'repo' box
7. Generate token
8. Copy it immediately (you'll only see it once!)

Tell me when you have the token."

**You**: "I got it! It starts with ghp_..."

**AI**: "Perfect! Keep that token safe. When you push for the first time, GitHub will ask for:
- Username: your GitHub username
- Password: paste your token (not your regular password!)

The token is like a special key just for Git. Ready to push?"

### Important Safety Notes

⚠️ **Never share your token** - it's like a password
⚠️ **Save it somewhere safe** - you can't see it again
⚠️ **If exposed, delete it immediately** on GitHub

✅ **It's normal to feel confused** - authentication is the hardest part
✅ **Your AI will guide you** through each step

---

## Step 4: Push Your Code to GitHub

**What you want**: Upload your code to GitHub

**Instead of**: Typing push commands

**Just ask your AI**:
- "Push my code to GitHub"
- "Upload my commits to GitHub"
- "Backup my code to GitHub"

### Example

**You**: "Push my code to GitHub now"

**AI**: "I'll push your code to GitHub. This is the first push, so GitHub will ask for your username and token."

[AI starts the push]

**AI**: "GitHub is asking for authentication:
- Username: your GitHub username
- Password: paste your token (the one starting with ghp_)

Enter those now."

**You**: [enters username and token]

**AI**: "Uploading..."

[Push completes]

**AI**: "Success! Your code is now on GitHub. Go to github.com/yourusername/my-calculator to see it."

**You**: "It worked! I can see my files on GitHub!"

---

### Verify It Worked

1. Open your browser
2. Go to github.com/yourusername/your-repo-name
3. See your files? ✅ Success!
4. See your commits? ✅ Everything uploaded!

---

## Push and Pull: Staying In Sync

Two simple operations:

### Push = Upload to GitHub

**When to push**:
- After you commit changes
- End of work session
- Before switching computers

**Just say**: "Push my changes to GitHub"

### Pull = Download from GitHub

**When to pull**:
- Start of work session
- Before making new changes
- When working from different computer

**Just say**: "Pull the latest code from GitHub"

---

## Working Across Computers

**The workflow**:

```
Laptop (morning):
  → Make changes
  → Commit
  → "Push to GitHub"

Desktop (evening):
  → "Pull from GitHub"
  → Continue where you left off
  → Commit
  → "Push to GitHub"

Laptop (next day):
  → "Pull from GitHub"
  → All your work from desktop is here!
```

**Why this is amazing**: Your code follows you everywhere. No USB drives, no email, no confusion.

---

## Key Points

**GitHub lets you**:
- Back up code safely in the cloud
- Work from any computer
- Share your work with others
- Build a professional portfolio

**The workflow**:
1. Create repository on GitHub
2. Connect local code to GitHub
3. Set up authentication (token)
4. Push code to GitHub
5. Pull code when working from different computer

**Remember**: You don't memorize commands. You tell your AI what you want:
- "Push my code to GitHub"
- "Pull the latest from GitHub"
- "Connect this project to GitHub"

Your AI handles the technical details. You understand what's happening.

---

## Try With AI

Practice connecting to GitHub.

**Tool**: Claude Code, Gemini CLI, or ChatGPT

### Exercise 1: Connect to GitHub

```
I created a repository on GitHub called "test-project".
My username is "myusername".
Connect my local code to this GitHub repository.
```

What to expect: AI sets up the connection and confirms it worked.

### Exercise 2: Get Authentication Help

```
I need to push code to GitHub but need authentication.
Walk me through creating a Personal Access Token step by step.
```

What to expect: AI explains exactly where to click on GitHub, what to check, and how to save the token.

### Exercise 3: First Push

```
I have my token. Push my code to GitHub.
My repo is: github.com/myusername/test-project
```

What to expect: AI pushes, asks for username and token when GitHub prompts, confirms success.

### Exercise 4: Verify Upload

```
Did my code upload? Check if my files are visible on GitHub.
```

What to expect: AI tells you to visit your GitHub page, or checks for you if it has web access.

### Exercise 5: Practice Pull

```
Pretend I'm on a different computer now.
How do I get my code from GitHub?
```

What to expect: AI explains pull command, walks you through downloading your code.

---

## What's Next

In Lesson 7, you'll learn Pull Requests - the professional way to merge branches. In Lesson 8, you'll set up your code editor with Git integration. In Lesson 9, you'll build a complete project using everything you've learned.

**Key takeaway**: GitHub = Your code's backup home. Push often, pull before working, never lose your work again.
