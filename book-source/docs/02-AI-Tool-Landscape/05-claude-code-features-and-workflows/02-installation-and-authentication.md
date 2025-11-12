---
sidebar_position: 2
title: "Installing and Authenticating Claude Code"
duration: "25-30 min"
---

# Installing and Authenticating Claude Code

## Partnership Onboarding: From Installation to Collaboration

In Lesson 1, you learned that Claude Code is an **agentic agent**—not a passive tool, but an active team member that reads your files, understands your context, and collaborates on your code. You learned about the **Three-Role AI Partnership** where Claude acts as both Teacher (suggesting patterns you haven't considered) and Student (learning your project's conventions and preferences).

Now comes the crucial bridge: **making that partnership real on your machine.**

Installation and authentication aren't just technical setup steps. They're how you **establish trust boundaries** and **enable personalization**. When you authenticate Claude Code with your account, you're not just logging in—you're personalizing the AI partnership. Authentication tells Claude:
- "This is YOUR development environment"
- "Remember MY project structure, MY coding style, MY team's preferences"
- "Learn from MY patterns and adapt to MY context"

This is fundamentally different from the web-based Claude, which starts fresh with zero project context in every conversation. Authenticated Claude Code becomes YOUR co-worker—one that remembers your standards, understands your codebase, and adapts its suggestions to YOUR specific needs.

By the end of this lesson, you'll have installed Claude Code, authenticated it with your account, and completed your first collaborative interaction. More importantly, you'll understand **why each step matters for the partnership** you're building.

We've designed this lesson to achieve a **95% first-attempt success rate**. We'll cover Windows, macOS, and Linux with clear authentication paths, practical verification steps, and straightforward troubleshooting. Let's establish your partnership.

---

## Prerequisites: What You Need Before Installing

Before we begin, verify you have the following:

**1. Terminal Access**
- **Windows**: Command Prompt, PowerShell, or Windows Terminal
- **macOS**: Terminal app (Applications → Utilities → Terminal)
- **Linux**: Any terminal emulator (GNOME Terminal, Konsole, etc.)

**Why this matters**: The terminal is where Claude Code lives—where your partnership happens. This is where you describe tasks, Claude reads your files, and you approve changes together.

**2. Claude Account** (one of the following):
- **Option A**: Claude.ai subscription (Pro or free tier)
  - Sign up at: https://claude.ai
  - You'll use this account to authenticate Claude Code
- **Option B**: Claude Console account with API credits
  - Create account at: https://console.anthropic.com
  - Requires payment method for API usage

**Why this matters**: Your Claude account is your partnership's identity. Authentication connects Claude Code on your machine to this account, enabling personalization and usage tracking.

**3. Node.js 18+ (for NPM installation method)**
- Check if installed: `node --version`
- If not installed: https://nodejs.org (download LTS version)

**Why this matters**: Node.js is the engine that powers Claude Code—it lets Claude Code execute tasks and interact with your system. Think of it as the software "hands" that allow AI to act.

**4. Internet Connection**
- Needed for initial download and authentication
- Claude Code requires connection to communicate with Claude AI

**Why this matters**: Your partnership is distributed—Claude Code on your machine talks to Claude AI's servers. This connection is how the collaboration happens.

---

## Installation: Choose Your Method

Claude Code offers **four official installation methods**. Choose the one that best fits your development environment:

### Decision Guide: Which Method?

- **macOS/Linux developers** → Use native installer (curl) or Homebrew
- **Windows developers** → Use native installer (PowerShell)
- **Node.js developers (any platform)** → Use npm (familiar workflow)
- **Package manager users** → Use Homebrew (macOS/Linux)

All methods install the same Claude Code—pick what feels most comfortable for YOUR workflow.

---

### Method 1: Native Installer (macOS/Linux) - Recommended for Most Users

**macOS or Linux terminal**:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**What just happened?** You've downloaded and executed the official Claude Code installer. This native installer:
- Detects your operating system automatically
- Installs Claude Code with appropriate permissions
- Configures your PATH so `claude` command works everywhere
- No Node.js required (Claude Code handles dependencies)

**Why this method?** Native installers are platform-optimized and don't require Node.js. If you're not a JavaScript developer, this is your fastest path to Claude Code.

**Step 2: Verify Installation**

```bash
claude --version
```

**Expected output** (version number may vary):
```
2.0.35 (Claude Code)
```

**What just happened?** You've verified that Claude Code installed correctly and can be found in your system's command path. You can now start conversations with Claude directly from your terminal.

---

### Method 2: Homebrew (macOS/Linux) - For Package Manager Users

If you already use Homebrew for managing software:

```bash
brew install --cask claude-code
```

**What just happened?** Homebrew downloaded, installed, and configured Claude Code as a system application. If you use Homebrew for other tools (git, node, python, etc.), this keeps Claude Code in the same management workflow.

**Why this method?** Familiar workflow if you already use `brew install` for everything. Updates are handled through `brew upgrade` alongside your other tools.

**Verify Installation**:

```bash
claude --version
```

---

### Method 3: Native Installer (Windows) - For Windows Developers

**Windows PowerShell (Run as Administrator)**:

```powershell
irm https://claude.ai/install.ps1 | iex
```

**What just happened?** You've executed the official Windows installer using PowerShell. `irm` (Invoke-RestMethod) downloads the installer, and `iex` (Invoke-Expression) runs it.

**Important**: You may need to enable script execution if you see a security warning:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Why this happens**: Windows restricts script execution by default for security. `RemoteSigned` allows downloaded scripts from trusted sources (like claude.ai) to run.

**Verify Installation**:

```powershell
claude --version
```

---

### Method 4: NPM Installation (All Platforms) - For Node.js Developers

**If you already have Node.js 18+ installed**:

```bash
npm install -g @anthropic-ai/claude-code
```

**What just happened?** You've downloaded Claude Code from npm (Node Package Manager) and installed it globally on your system. The `-g` flag means you can now type `claude` in any directory.

**Why this method?** If you're a JavaScript/TypeScript developer with Node.js already installed, npm is familiar territory. Updates happen through `npm update -g @anthropic-ai/claude-code`.

**Common issue on macOS/Linux**: Permission errors

**If you see `EACCES` permission error**:
```bash
sudo npm install -g @anthropic-ai/claude-code
```

**Why this happens**: Some systems require elevated permissions to install software globally. The `sudo` command runs the install with administrator privileges.

**Verify Installation**:

```bash
claude --version
```

**Expected output** (version number may vary):
```
2.0.35 (Claude Code)
```

---

## 💬 AI Colearning Prompt: Verify Your Installation

Before you authenticate, let's make sure Claude Code is working properly in YOUR environment. Different systems sometimes have different configurations, and this is your chance to troubleshoot with an AI guide.

**Open your terminal and run this command:**

```bash
claude "I just installed Claude Code on my system. Walk me through verifying that the installation is working correctly. Here's what I see when I check: [paste the output from `claude --version` above]"
```

**What to expect**: Claude will walk you through verification step-by-step, help you understand what each component means, and suggest next steps if anything seems off.

**Why this matters**: This is your first collaborative interaction with Claude Code. You're not just installing software—you're learning how to describe problems and work with AI in real-time. This conversation demonstrates AI in the **Teacher role** (explaining your installation) and **Student role** (learning about your specific environment).

If you hit any issues, Claude will help you troubleshoot. If everything works, Claude will explain what successful installation looks like on your system.

---

## Authentication: Establishing Trust and Personalization

Authentication is where your partnership truly begins. When you authenticate Claude Code, you're not just logging in—you're **personalizing the AI partnership**. You're telling Claude Code:

- "This is MY development environment—learn MY patterns"
- "Access MY files and understand MY project structure"
- "Remember MY preferences and conventions"
- "Build context over time as we work together"

This is radically different from web-based Claude, which starts fresh with zero context every conversation. Authenticated Claude Code becomes YOUR co-worker—one that learns your standards, understands your codebase, and adapts to your workflow.

### Which Authentication Method Should I Use?

**Decision Tree**:

```
Do you have a Claude.ai account?
├─ Yes → Use Claude.ai Authentication (Method A)
│        Most common for individual users
│
└─ No, but I have Claude Console API credits
   └─ Use Claude Console Authentication (Method B)
           Common for developers with API access
```

**If you have both**: Use Claude.ai authentication (Method A).

---

### Authentication Method A: Claude.ai Account (Most Common)

**Step 1: Start the Authentication Flow**

In your terminal, run:

```bash
claude
```

**Expected output**:
```
Choose the text style that looks best with your terminal
To change this later, run /theme
❯ 1. Dark mode ✔

 Select login method:

 ❯ 1. Claude account with subscription · Pro, Max, Team, or Enterprise

   2. Anthropic Console account · API usage billing
```

**What just happened?** Claude Code detected that you haven't authenticated yet and is asking for your login preference. Your default browser is about to open.

**Step 2: Log In to Claude.ai**

1. If not already logged in, enter your Claude.ai credentials
2. Review the permissions Claude Code is requesting
3. Click "Allow" or "Authorize"

**What this means**: You're granting Claude Code permission to use YOUR Claude account to make API calls. This is how Claude Code connects to the Claude AI servers and maintains personalization across sessions.

**Step 3: Confirm Authentication**

Return to your terminal. You should see:

```
Logged in as email@gmail.com
Login successful. Press Enter to continue…
```

**What just happened?** Your authentication token has been saved locally. Claude Code can now identify itself as YOU when talking to Claude AI's servers. From now on, all your conversations with Claude Code will build on each other—Claude learns your style, your patterns, your codebase.

**Step 4: Test Your Setup**

Run a simple test command:

```bash
claude "Hello! Can you confirm Claude Code is working?"
```

**Expected output**: Claude responds with a greeting confirming the connection works.

**What this demonstrates**: This is your first authenticated interaction. Claude now has access to the directory you're in and can see your files. Try this follow-up:

```bash
claude "What files and directories do you see in my current directory? Describe what kind of project this looks like."
```

Claude should list your actual files—THIS is the agentic AI at work. Zero copy-paste. Claude reads your context directly.

---

## 🎓 Expert Insight: Why Personalization Matters More Than You Think

Here's something many developers miss: **the difference between generic AI and personalized AI compounds rapidly over time.**

**Generic AI (Web-Based Claude)**:
- Every conversation starts from zero context
- You repeat project setup: "This is a Python Flask project. We use SQLAlchemy. Tests are in /tests. We follow PEP 8..."
- Suggestions are generic best practices (not YOUR project's patterns)
- Feedback loop is slow: Suggest → Copy → Paste → Test → Report back

**Personalized AI (Authenticated Claude Code)**:
- Claude remembers your codebase structure
- Claude learns YOUR naming conventions, architectural patterns, testing approach
- Suggestions get MORE specific and relevant with each interaction
- Feedback loop is instantaneous: Describe → Claude reads files → Suggests specific changes → Approves
- Over time, Claude becomes a team member who knows your standards as well as you do

**The Compounding Effect**:
- Week 1: Claude saves you 10 minutes per session (reducing copy-paste friction)
- Week 4: Claude saves you 45 minutes per session (suggestions match your patterns perfectly)
- Month 3: Claude saves you 2-3 hours per day (acts as your pair programmer, not just advisor)

This is **co-learning in action** from Lesson 1: Each interaction teaches Claude more about YOUR work. Each iteration Claude understands YOUR context better. Your partnership gets stronger.

**Bottom line**: Authentication isn't just a login step. It's the difference between hiring a consultant (generic advice) and onboarding a team member (project-specific partnership).

---

## 🤝 Practice Exercise: Experience Your First Agentic Interaction

Let's make your partnership real. You've authenticated. Now let's see what agentic AI actually does.

**Setup**: Navigate to ANY project directory on your machine (or create a simple one with a few files if you don't have one yet).

```bash
cd /path/to/a/project
```

**Try this conversation**:

```bash
claude "Look at the files in this directory and tell me:
1. What kind of project is this?
2. What technologies does it use?
3. What does the main application do?

Base your answer on what you actually see in the files—not what I tell you."
```

**Observe**:
- Claude lists files WITHOUT you copying them
- Claude reads actual code WITHOUT you pasting snippets
- Claude understands project purpose WITHOUT you explaining it

**Reflection**:
- This is the paradigm shift from Lesson 1 in action
- Compare this to web-based Claude: How would you describe your project there? (You'd need to copy-paste files)
- Notice how Claude became a Teacher (explaining your own project to you) AND a Student (learning your project structure)

**This is agentic AI.** You're experiencing the partnership in real-time.

---

## Pause and Reflect: You've Crossed the Bridge

**If your installation and authentication succeeded**: Celebrate. You've moved from "Claude Code installed on my machine" to "I have an active AI partnership." Claude now understands YOUR development environment.

**Reflection Questions**:
- How was your first agentic interaction different from asking a question on ChatGPT?
- What could Claude do that web-based AI cannot?
- What would happen if you ran that same "describe my project" prompt in web-based Claude?

**If you're still troubleshooting**: Installation hiccups are normal, especially across different platforms. They don't reflect on you or your technical ability. Different systems have different configurations. Work through it systematically—and remember, this is where Claude Code (once working) is YOUR partner in troubleshooting future technical challenges.

## 🤝 Practice Exercise: Building Your Partnership Memory

Your partnership gets stronger when Claude learns YOUR project's conventions. That's where CLAUDE.md comes in.

### What is CLAUDE.md?

CLAUDE.md is your partnership's shared memory file. It teaches Claude Code about:
- Your project's purpose and architecture
- Your coding standards and naming conventions
- Common workflows and how to execute them
- Important context that never changes

**Think of it as**: The onboarding document you'd give to a new team member. Except Claude reads it and remembers everything.

### Why This Matters for Your Partnership

**Without CLAUDE.md**: You repeat yourself constantly
- Every conversation you say: "This is a Python Flask project..."
- You explain: "We follow PEP 8, tests go in /tests, we use pytest..."
- Context switching: Claude forgets from one conversation to the next

**With CLAUDE.md**: Your partnership grows
- Claude remembers your standards automatically
- Suggestions get more specific (Claude knows your conventions)
- Conversations are shorter (Claude already has context)
- The partnership compounds over time

**Real-world example**:
- Without CLAUDE.md: "Add a new test for the user login feature" → Claude asks "Which testing framework? Where do tests go? Follow any conventions?"
- With CLAUDE.md: "Add a new test for the user login feature" → Claude creates the test in your /tests folder, using pytest, following your naming conventions, ready to commit

### Creating Your First CLAUDE.md

You don't need to write CLAUDE.md manually. Let Claude Code help you create it.

**Navigate to your project directory**:

```bash
cd /path/to/your/project
```

**Ask Claude Code to create the onboarding file**:

```bash
claude "Create a CLAUDE.md file that documents this project. Include:
- Project name and purpose
- Main technologies and frameworks
- Where tests go and which framework we use
- Coding standards and naming conventions
- How to run the project
- Any important context I should know

Use what you see in the files to fill in accurate information."
```

**What happens**: Claude examines your project, creates a comprehensive CLAUDE.md, and saves it to your project root.

**Verify it worked**:

```bash
claude "Read CLAUDE.md and summarize what you learned about this project"
```

Claude should reflect back accurate information about YOUR project—proof that the partnership memory is working.

### When to Update CLAUDE.md

Your CLAUDE.md evolves as your project grows:
- ✅ You add a new major framework or dependency
- ✅ Your team adopts new coding standards
- ✅ Project structure changes significantly
- ✅ You notice Claude repeatedly asking for the same information (that's a signal to add it to CLAUDE.md)

**CLAUDE.md is collaborative**: You write it once, Claude learns it permanently. Your partnership gets stronger with every update.

---

## Try With AI

Your partnership is set up. Now let's deepen it with a collaborative task.

**Goal**: Work WITH Claude Code to refine your understanding of its capabilities and limitations.

---

### Prompt Set: Understanding Your Partnership

**Prompt 1 (Opening)**: Ask Claude Code to explain itself
```bash
claude "I just installed and authenticated you. From your perspective, what can you do for a developer like me? What are your strengths and limitations?"
```

**What to expect**: Claude will honestly describe what it can and cannot do. This is the Student role—Claude learns YOUR expectations and adapts.

---

**Prompt 2 (Deepen)**: Follow up with context
```bash
claude "Based on what you said, which of your capabilities would be most valuable for MY workflow? You haven't seen my projects yet, but based on your understanding of development, what's the competitive advantage of having you as a partner?"
```

**What to expect**: Claude will become a Teacher—suggesting patterns and approaches you might not have considered.

---

**Prompt 3 (Converge)**: Make it real
```bash
claude "Now show me. What's one concrete task you could do RIGHT NOW if I asked you to help with my actual project? Describe a specific example of how you'd help."
```

**What to expect**: Claude suggests a concrete, project-specific action. This is Co-Working—Claude proposes implementation details while you evaluate.

---

### Safety Reminder: Responsible Partnership

**Verify before you trust**: If Claude suggests code changes, always review the diffs before approving. If Claude suggests architecture decisions, validate against YOUR project's constraints and goals. Your judgment + Claude's capabilities = better decisions together.

**This is the partnership principle in action**: You're not blindly following AI suggestions. You're collaborating with a tool that has opinions, but YOU make final decisions.

---