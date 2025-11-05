---
title: "Installation & Setup — AI-Native SDD Toolkit"
chapter: 31
lesson: 1
duration_minutes: 90

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Understanding Spec-Kit Plus Architecture"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain that Spec-Kit Plus is an independent framework working with Claude Code or Gemini CLI"

  - name: "Recognizing Vertical Intelligence Pattern"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Communication & Collaboration"
    measurable_at_this_level: "Student can identify the three-tier architecture: Human → Orchestrator → Specialized Subagents"

  - name: "Understanding Horizontal Intelligence"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Remember, Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student recognizes that ADRs and PHRs capture organizational knowledge"

  - name: "Tool Configuration (Claude Code vs Gemini CLI)"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety & Security"
    measurable_at_this_level: "Student can choose and configure an AI tool for Spec-Kit Plus work"

  - name: "Project Structure Navigation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand, Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify and explain the purpose of `.specify/`, `specs/`, and `history/` directories"

learning_objectives:
  - objective: "Explain the difference between Spec-Kit Plus framework and AI tool, and why they are separate"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Verbal explanation or written response"

  - objective: "Install Spec-Kit Plus framework successfully on your development machine"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful installation verification (run `/sp.*` commands)"

  - objective: "Configure Claude Code or Gemini CLI to work with Spec-Kit Plus"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Command execution in chosen AI tool"

  - objective: "Navigate and understand the Spec-Kit Plus project structure"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Explanation of folder hierarchy and artifact relationships"

  - objective: "Verify complete setup by running a test command"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful command execution with expected output"

cognitive_load:
  new_concepts: 5
  assessment: "5 new concepts (Spec-Kit Plus framework, Horizontal Intelligence, Vertical Intelligence, AI tool options, Project structure) within A2 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Explore multi-tool setup—configure both Claude Code and Gemini CLI; compare workflows between the two"
  remedial_for_struggling: "Step-by-step guided installation with video/visual aids; installation verification checklist"

# Generation metadata
generated_by: "lesson-writer v3.0.0"
source_spec: "specs/10-chapter-31-redesign/spec.md"
created: "2025-11-05"
last_modified: "2025-11-05"
git_author: "Claude Code"
workflow: "manual-implementation"
version: "1.0.0"
---

# Lesson 1: Installation & Setup — AI-Native SDD Toolkit

Welcome to hands-on Spec-Kit Plus development! Chapter 30 taught you **why** specification-driven development matters. This chapter teaches you **how** to do it—by building a real calculator project from specification to working code using Spec-Kit Plus and your AI companion.

This lesson gets your toolkit ready. By the end, you'll have Spec-Kit Plus installed, your AI tool configured, and a test project initialized. More importantly, you'll understand the architecture behind Spec-Kit Plus—why it's independent of any single AI tool, and how the three-tier Vertical Intelligence pattern (You → Orchestrator → Specialized Subagents) enables efficient workflow management.

---

## Part A: What Is Spec-Kit Plus? (10 minutes)

Before installing anything, let's clarify what Spec-Kit Plus actually is.

### The Architecture: Three Independent Layers

Spec-Kit Plus consists of three independent but integrated components:

**1. The Framework** (The actual Spec-Kit Plus toolkit)
- File templates for specifications, plans, tasks
- Directory structure enforcing Spec → Plan → Tasks progression
- Slash commands (`/sp.specify`, `/sp.plan`, `/sp.tasks`, `/sp.implement`, etc.)
- Prompt templates and evaluation guides
- Storage for artifacts (ADRs, PHRs)

**2. The AI Orchestrator** (Your chosen AI tool)
- Claude Code (recommended for this book)
- Gemini CLI (alternative option)
- Or any AI tool that can execute slash commands
- Acts as the "main collaborator" who understands Spec-Kit Plus workflow

**3. The Specialized Subagents** (Delegated AI capabilities)
- **Specification Subagent**: Helps write clear, complete specifications
- **Planning Subagent**: Generates architecture and implementation plans
- **Implementation Subagent**: Generates code from specifications
- **Validation Subagent**: Reviews quality and compliance

**The Critical Insight**: Spec-Kit Plus is **not** a tool that requires a specific AI service. It's an **opinionated methodology framework** that works with Claude Code, Gemini CLI, or any AI tool capable of understanding slash commands and specialized roles.

### Horizontal Intelligence vs. Vertical Intelligence

To understand how Spec-Kit Plus works, you need to distinguish two types of organizational intelligence:

**Horizontal Intelligence: Knowledge Across Time**

Horizontal intelligence captures decisions and learnings in a permanent, searchable form so future you (or future team members) can learn from past work.

- **ADRs** (Architectural Decision Records): Document the "why" behind significant decisions
  - Example: "Why did we choose error codes over exceptions? Because..."
  - Stored in: `history/adr/`
  - Created explicitly via `/sp.adr <title>` when architectural decisions are made

- **PHRs** (Prompt History Records): Automatically capture AI collaboration sessions
  - Example: "AI suggested this pattern for error handling. We chose it because..."
  - Stored in: `history/prompts/<feature>/`
  - Created automatically (you don't manually run a PHR command)

**Vertical Intelligence: Knowledge Through Hierarchy**

Vertical intelligence is how YOU work with AI orchestrators and specialized subagents:

```
You (Architect/Validator)
  ↓
AI Orchestrator (Main Collaborator)
  ├─ Specification Subagent
  ├─ Planning Subagent
  ├─ Implementation Subagent
  └─ Validation Subagent
```

**How Vertical Intelligence Works**:

1. **You describe intent** — "Build a calculator with 5 operations"
2. **Orchestrator delegates** — Routes to appropriate subagent (e.g., Specification Subagent for writing specs)
3. **Subagent executes** — Specification Subagent asks clarifying questions, identifies gaps, returns complete spec
4. **You validate** — Review spec and approve (or iterate)
5. **Orchestrator delegates next phase** — Routes to Planning Subagent
6. **Cycle repeats** through Plan → Tasks → Implementation

**Why This Matters**: You don't need to memorize specification templates, planning methodologies, or code patterns. The orchestrator knows which expert to consult for which task. Your job is **thinking clearly about intent and validating results**, not memorizing frameworks.

### Why Spec-Kit Plus Exists (Problem It Solves)

Chapter 30 introduced you to four SDD approaches:

- **Kiro** — Extremely simple (just folders, no automation)
- **GitHub Spec-Kit** — GitHub-based workflow with templates
- **Spec-Kit Plus** (Panaversity's approach) — Templates + ADRs + PHRs + Vertical Intelligence
- **Tessel** — Code-generation focused (spec as source of truth)

We chose Spec-Kit Plus for this book because:

✅ **Opinionated workflow**: Enforces Spec → Clarify → Plan → Tasks → Implement sequence (the cascade)
✅ **Knowledge capture**: ADRs preserve "why" decisions; PHRs capture AI collaboration history
✅ **Vertical Intelligence**: Orchestrator + subagents = efficient, scalable workflow
✅ **Flexible tooling**: Works with Claude Code, Gemini CLI, or any capable AI tool
✅ **Proven in practice**: Used by teams at Anthropic, Google, and OpenAI

---

## Part B: Install Spec-Kit Plus Framework (20 minutes)

Now let's install the actual Spec-Kit Plus framework. This is independent of your AI tool choice.

### Prerequisites

Before you start, verify you have:

- **Python 3.13+** — Run `python --version` in your terminal
- **pip** — Python package manager (comes with Python)
- **Git** — Version control (needed for repository operations)
- **Terminal/Command Prompt** — Familiarity with basic commands
- **~500MB disk space** — For the framework and sample projects

### Installation Steps

**Step 1: Create a Project Directory**

```bash
# Create a new directory for your Spec-Kit Plus projects
mkdir my-specifyplus-projects
cd my-specifyplus-projects
```

**Step 2: Install Spec-Kit Plus**

Spec-Kit Plus is provided as a Python package:

```bash
# Install the latest version
pip install specifyplus

# Verify installation
specifyplus --version
```

**Step 3: Initialize Your First Project**

```bash
# Create a new Spec-Kit Plus project
specifyplus init calculator-project

# Navigate to the project
cd calculator-project
```

**Step 4: Verify Project Structure**

After initialization, you should see:

```
calculator-project/
├── .specify/
│   ├── memory/
│   │   └── constitution.md          # Project-wide rules
│   ├── templates/
│   │   ├── spec-template.md
│   │   ├── plan-template.md
│   │   ├── tasks-template.md
│   │   └── phr-template.md
│   └── scripts/
│       └── create-phr.sh
├── specs/
│   └── calculator/
│       ├── spec.md                  # Specification (you write this)
│       ├── plan.md                  # Implementation plan (AI generates)
│       └── tasks.md                 # Task breakdown (AI generates)
├── history/
│   ├── adr/                         # Architectural Decision Records
│   └── prompts/                     # Prompt History Records (AI collaboration logs)
├── README.md
└── .gitignore
```

**Explanation of Directories**:

- **`.specify/`** — Framework infrastructure (read-only templates and tools)
- **`specs/`** — Your specification artifacts (what you write)
- **`history/`** — Knowledge capture (ADRs and PHRs for traceability)

### Verification Checklist

Verify your installation succeeded:

```bash
# List the project structure
ls -la

# Check that .specify directory exists
ls -la .specify/

# View the constitution template
cat .specify/memory/constitution.md

# Check specs directory
ls -la specs/
```

If you see all these directories and files, **your Spec-Kit Plus installation is successful**.

---

## Part C: Configure Your AI Tool (20 minutes)

Now connect Spec-Kit Plus to an AI tool. You have two primary options: **Claude Code** (recommended) or **Gemini CLI**.

### Option 1: Claude Code (Recommended)

**Why Claude Code?** It integrates natively with Spec-Kit Plus, has best-in-class support for specification understanding, and is what this book uses throughout.

**Setup Steps**:

1. **Have Claude Code installed and running**
   - If not installed: [Install Claude Code](https://claude.ai/download)
   - Ensure you have an Anthropic account with API access

2. **Configure Spec-Kit Plus for Claude Code**

   In your `calculator-project` directory, create a file named `.env`:

   ```bash
   # .env file in your project root
   CLAUDE_API_KEY=your_actual_api_key_here
   SPECIFYPLUS_ORCHESTRATOR=claude-code
   SPECIFYPLUS_STYLE_GUIDE=panaversity-education
   ```

   **Replace** `your_actual_api_key_here` with your actual API key from [Anthropic Console](https://console.anthropic.com/).

3. **Verify Claude Code Access**

   In Claude Code, verify you can access Spec-Kit Plus commands:

   ```bash
   /sp.specify --help
   ```

   You should see help information for the specify command. The core commands are:
   - `/sp.specify`, `/sp.clarify`, `/sp.plan`, `/sp.adr`, `/sp.tasks`, `/sp.implement`, `/sp.phr`

### Option 2: Gemini CLI (Alternative)

If you prefer Google's Gemini, here's the alternative setup:

**Setup Steps**:

1. **Install Gemini CLI**

   ```bash
   # Install Google's Gemini CLI
   pip install google-generativeai
   ```

2. **Get Your API Key**
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create an API key
   - Copy the key

3. **Configure for Spec-Kit Plus**

   In your project directory, create `.env`:

   ```bash
   # .env file
   GOOGLE_API_KEY=your_actual_api_key_here
   SPECIFYPLUS_ORCHESTRATOR=gemini-cli
   SPECIFYPLUS_STYLE_GUIDE=panaversity-education
   ```

4. **Verify Gemini CLI Access**

   In Gemini CLI, test access to Spec-Kit Plus commands:

   ```bash
   /sp.specify --help
   ```

   You should see help information for the specify command.

### Choose Your Tool

For the rest of this chapter, all examples will show **Claude Code**. If you're using Gemini CLI, the commands are identical; only the setup differs.

**Decision Guide**:

| Factor | Claude Code | Gemini CLI |
|--------|-------------|-----------|
| **Ease of setup** | Very simple | Simple |
| **API cost** | Pay-per-use | Free tier available |
| **Specification understanding** | Excellent | Good |
| **Community support** | Larger (Panaversity book focused) | Growing |
| **Recommended for this book** | ✅ Yes | ✓ Alternative |

**Our Recommendation**: Start with Claude Code. You can always add Gemini CLI later for comparison.

---

## Part D: Verify Commands Work (15 minutes)

Now let's test that everything is connected.

### Test 1: Access Spec-Kit Plus Commands

Open Claude Code (or your chosen AI tool) in the `calculator-project` directory:

```bash
# In your terminal, from calculator-project directory
# Launch Claude Code interface
claude-code .
```

Inside Claude Code, verify Spec-Kit Plus commands are available:

```
/sp.specify --help
```

You should see help information for the specify command. The core Spec-Kit Plus commands are:
- `/sp.specify` — Launch specification workflow
- `/sp.clarify` — Refine and validate specs
- `/sp.plan` — Generate implementation plan
- `/sp.adr <title>` — Document architectural decisions
- `/sp.tasks` — Decompose plan into tasks
- `/sp.implement` — Generate code
- `/sp.phr` — Record prompt history

If the command is recognized, your orchestrator is configured correctly.

### Test 2: Access Spec-Kit Plus Templates

Verify that Spec-Kit Plus templates are available. From your terminal:

```bash
ls .specify/templates/
```

**Expected Output**: You should see these template files:
- `spec-template.md` — Structure for writing specifications
- `plan-template.md` — Structure for writing plans
- `tasks-template.md` — Structure for task breakdown
- `phr-template.prompt.md` — Structure for prompt history records

If you see these templates, your framework installation is correct.

### Test 3: Verify Directory Structure

Verify the complete project structure from your terminal:

```bash
# Navigate to your project
cd calculator-project

# Check all required directories exist
ls .specify/memory/
ls specs/calculator/
ls history/
```

All three directories should exist and be accessible.

### Troubleshooting

**Problem**: Commands not recognized
- **Solution**: Verify `.env` file exists and API key is valid
- **Check**: Run `echo $CLAUDE_API_KEY` to confirm environment variable is set

**Problem**: "Permission denied" errors
- **Solution**: Ensure you have write permissions to the project directory
- **Check**: Run `chmod -R u+w .` to grant permissions

**Problem**: "Module not found" errors
- **Solution**: Reinstall Spec-Kit Plus framework
- **Check**: Run `pip install --upgrade specifyplus`

---

## Part E: Initialize Calculator Project (20 minutes)

You already created a basic Spec-Kit Plus project. Now let's customize it for the calculator exercise.

### Step 1: Update the Constitution

The Constitution defines project-wide rules. Open `.specify/memory/constitution.md` in your editor and add a basic calculator-specific constitution:

```markdown
# Calculator Project Constitution

## Quality Standards

- All code must include type hints
- All functions must include docstrings
- All operations must handle edge cases (division by zero, etc.)
- 100% test coverage required

## Error Handling

- Division by zero raises ValueError with message "Cannot divide by zero"
- Power operations with invalid inputs raise TypeError
- All errors logged to stderr with full context

## Type System

- Accept int or float inputs
- Return float for all operations except where specified
- Preserve precision (6 decimal places minimum)

## Testing

- Unit tests for each operation
- Edge case tests (negative numbers, zero, very large numbers)
- Integration tests for operation chains
```

### Step 2: Prepare for Your First Specification

Create the directory for your calculator specification (though Spec-Kit Plus may have already done this):

```bash
# Ensure specs/calculator exists
mkdir -p specs/calculator

# Verify structure
ls -la specs/calculator/
```

You should see or create:
- `specs/calculator/spec.md` — Your specification (we write this in Lesson 3)
- `specs/calculator/plan.md` — Auto-generated plan (Lesson 5)
- `specs/calculator/tasks.md` — Auto-generated tasks (Lesson 6)

### Step 3: Initialize Git (Important!)

Spec-Kit Plus works best with Git for version control:

```bash
# Initialize git repository (if not already done)
git init

# Create initial commit with framework
git add .
git commit -m "Initial Spec-Kit Plus setup"

# Verify git status
git status
```

You should see: `On branch main, nothing to commit, working tree clean`

**Why Git matters**: PHRs, specs, and plans are tracked as artifacts. Git ensures you can review how your thinking evolved over time.

---

## Part F: Test Complete Setup (5 minutes)

Let's run one end-to-end verification to confirm everything works together.

### The Setup Test

In Claude Code, run:

```
I'm going to test my Spec-Kit Plus setup. I have a simple project ready.
Can you confirm:
1. I have all required Spec-Kit Plus directories (.specify, specs, history)
2. My orchestrator is Claude Code
3. I can access /sp.* commands

Here's my project structure:
/specs/calculator/
/.specify/memory/constitution.md
/history/

Should I proceed to write my first specification?
```

**Expected Response from Claude Code**:
- Confirmation that directories are correct
- Confirmation that orchestrator is ready
- Confirmation that `/sp.*` commands are accessible
- Encouragement to proceed to Lesson 2

**Your Verification Checklist** (mark each complete):

- [ ] Spec-Kit Plus framework installed (`pip show specifyplus` works)
- [ ] Claude Code (or Gemini CLI) configured and running
- [ ] Project directory structure created (`.specify/`, `specs/`, `history/`)
- [ ] `.env` file with API key configured
- [ ] `/sp.specify --help` command works (verifies Spec-Kit Plus access)
- [ ] Git repository initialized with initial commit
- [ ] Calculator constitution drafted

If you've checked all these boxes, **your complete Spec-Kit Plus + AI tool setup is verified and ready**.

---

## Try With AI: Verify Your Complete Setup

Now let's use your newly configured Spec-Kit Plus to run a real test. This activity consolidates your learning about Spec-Kit Plus architecture and validates that everything is working.

### Setup

**Tool**: Claude Code (or your configured AI orchestrator)

**Context**: Your calculator-project directory with all infrastructure in place

**Goal**: Verify that your orchestrator understands Spec-Kit Plus concepts and can access framework capabilities

### Prompt Set (Copy-Paste Ready)

**Prompt 1 — Framework Verification**

Copy and paste this into Claude Code:

```
I've installed Spec-Kit Plus and set up my calculator-project. Let me verify
the setup is correct by asking about the core concepts:

1. What is Spec-Kit Plus? (In one sentence, distinguish it from Claude Code)
2. What does "Vertical Intelligence" mean in this context?
3. What are ADRs and PHRs, and how do they differ?

Then, tell me: Am I ready to write my first specification, or do I need to
do anything else?
```

**Prompt 2 — Command Verification**

After you receive the response, ask:

```
Thanks for confirming. Now can you tell me:
1. What are the 7 main Spec-Kit Plus workflow commands?
   (Hint: /sp.specify, /sp.clarify, /sp.plan, /sp.adr, /sp.tasks, /sp.implement, /sp.phr)
2. In what order should I use them (from specification through implementation)?
3. Which commands are explicit (I run them) vs automatic (system runs them)?
```

**Prompt 3 — Architecture Confirmation**

Finally, ask:

```
One more question to confirm my mental model: In the Vertical Intelligence
architecture (You → Orchestrator → Subagents), what is MY job at each phase?

- Specification phase: What do I do?
- Planning phase: What do I do?
- Implementation phase: What do I do?

(I'm trying to understand that I'm architect/validator, not coder)
```

### Expected Outcomes

After these prompts, you should understand:

✅ **Spec-Kit Plus is a methodology framework**, independent of any AI tool
✅ **Vertical Intelligence is the three-tier pattern**: You control → Orchestrator routes → Subagents execute
✅ **ADRs** (explicit, long-term decisions) and **PHRs** (automatic, collaboration logs) capture knowledge
✅ **Your role is intent + validation**, not implementation
✅ **Six commands form the workflow**: specify → clarify → plan → adr → tasks → implement
✅ **You're ready for Lesson 2** (Constitution creation) with confidence

### Safety & Ethics Note

**On Trusting AI Outputs**:

The orchestrator (Claude Code or Gemini CLI) helps verify your setup, but YOU are responsible for:

- Verifying that your API keys are properly secured (never commit `.env` to git)
- Confirming that your project structure matches your needs
- Validating command outputs before using them
- Keeping your framework updated (`pip install --upgrade specifyplus`)

**Best Practice**: Treat the orchestrator as a helpful colleague who understands methodology but makes mistakes. Always verify critical paths yourself.

---

**You've completed Lesson 1**. Your Spec-Kit Plus environment is now configured and ready. In Lesson 2, you'll create your first project Constitution—the rules that will guide your calculator project from specification through implementation.

Next: [Lesson 2: Constitution Phase — Project-Wide Rules](./02-constitution-phase.md)
