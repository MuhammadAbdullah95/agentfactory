---
sidebar_position: 6
title: "Principle 6: Constraints and Safety"
chapter: 6
lesson: 6
duration_minutes: 30
description: "Safety measures and constraints that make agentic workflows reliable and trustworthy"
keywords: ["safety", "constraints", "guardrails", "permission", "destructive operations", "sandboxing"]

# HIDDEN SKILLS METADATA
skills:
  - name: "Safety Constraint Design"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Safety and Security"
    measurable_at_this_level: "Student can identify potential safety risks in agentic workflows and design appropriate constraints and guardrails"

  - name: "Permission Model Understanding"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Literacy"
    measurable_at_this_level: "Student can explain different permission models for AI tools and recommend appropriate settings for different scenarios"

  - name: "Risk Assessment for AI Operations"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Critical Thinking"
    measurable_at_this_level: "Student can assess the risk level of AI operations and choose appropriate safety measures"

learning_objectives:
  - objective: "Identify potential safety risks in agentic workflows and design appropriate constraints"
    proficiency_level: "A2"
    bloom_level: "Evaluate"
    assessment_method: "Student can analyze a workflow and identify specific risks (data loss, security issues, cost overruns) and propose mitigation strategies"

  - objective: "Configure appropriate permission models for different AI tool usage scenarios"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student can recommend permission settings (approval modes, sandboxing, resource limits) for different use cases"

  - objective: "Apply safety best practices when working with AI systems that have file and terminal access"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student demonstrates safe AI collaboration practices including pre-approving destructive operations and using sandbox environments"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (destructive vs safe operations, permission models, sandboxing, resource limits, data boundaries, approval workflows, trust gradualism) at upper limit of A2-B1 range ✓"

differentiation:
  extension_for_advanced: "Design a comprehensive safety framework for a team AI workflow including audit logging, rate limiting, and approval hierarchies for different risk levels."
  remedial_for_struggling: "Focus on concrete examples: Show safe vs unsafe configurations, demonstrate what can go wrong with poor safety practices, and provide simple rules to follow."
---

# Principle 6: Constraints and Safety

You give an AI system access to your codebase. It's working well—making helpful changes, running tests, suggesting improvements. Then you notice something odd in git history. The AI deleted a directory you didn't ask it to touch. It ran commands you don't remember approving. It's refactoring code you specifically said not to change.

This isn't science fiction—these are real incidents that have happened. AI systems are powerful, and power without constraints is dangerous.

This principle is about **balancing capability with safety**. You want AI to be effective—but not so effective it causes damage. You want autonomy—but not so much autonomy that you lose control. The solution is thoughtful constraints and safety measures.

## The Risk Spectrum: Understanding What Can Go Wrong

Before designing safety measures, understand what you're protecting against.

### Category 1: Data Loss (Destructive Operations)

AI deletes or overwrites important data:
- `rm -rf` on the wrong directory
- Overwriting files without confirmation
- Git operations that discard work
- Database changes without backups

**Impact**: Hours to weeks of lost work
**Likelihood**: Medium—AI follows instructions literally

### Category 2: Security Vulnerabilities

AI introduces security issues:
- Hardcoded credentials in code
- Insecure authentication implementations
- SQL injection vulnerabilities
- Dependency confusion attacks

**Impact**: System compromise, data breach
**Likelihood**: Medium—AI doesn't automatically think like an attacker

### Category 3: Cost Overruns

AI generates expensive operations:
- Infinite loops in cloud resources
- API calls without rate limiting
- Inefficient algorithms consuming compute
- Unintended large-scale operations

**Impact**: Unexpected cloud bills
**Likelihood**: Low—AI tries to be efficient, but doesn't know costs

### Category 4: Reputation Damage

AI makes changes that affect users:
- Offensive content in user-facing materials
- Bugs that corrupt user data
- Performance issues that cause downtime
- Privacy violations

**Impact**: Lost trust, user churn
**Likelihood**: Low—but high impact

### Category 5: Workflow Disruption

AI interferes with team processes:
- Commits that break CI/CD
- Changes that conflict with others' work
- Alters agreed-upon conventions
- Makes conflicting changes across branches

**Impact**: Team friction, lost productivity
**Likelihood**: Medium—AI doesn't know team context

## The Safety Hierarchy: Defense in Depth

No single safety measure is sufficient. You need layers—each protecting against different failure modes.

### Layer 1: Technical Constraints

**What**: Hard limits on what AI can do

**Examples**:
```bash
# Read-only filesystem access (sandbox)
# Network restrictions (no external API calls)
# Resource limits (CPU, memory, disk)
# Whitelisted commands only
```

**Protects against**: Accidental damage, runaway processes

### Layer 2: Permission Controls

**What**: Require approval for certain actions

**Examples**:
```
# Approve before: deleting files
# Approve before: running git push
# Approve before: installing packages
# Approve before: modifying config files
```

**Protects against**: Unintended destructive operations

### Layer 3: Environment Isolation

**What**: Separate AI work from production

**Examples**:
```
# AI works in staging/sandbox environment
# Production requires manual deployment
# Separate database instances
# Separate API keys/tokens
```

**Protects against**: Production incidents

### Layer 4: Process Controls

**What**: Workflow that incorporates safety

**Examples**:
```
# Always review diffs before applying
# Run tests before committing
# Peer review for AI-generated changes
# Rollback plans prepared in advance
```

**Protects against**: Bad code reaching production

### Layer 5: Human Verification

**What**: Human review before impact

**Examples**:
```
# Review AI suggestions before accepting
# Manual approval for deployments
# Security review for sensitive changes
# Testing in isolated environment first
```

**Protects against**: All categories—final safety net

## Permission Models: Choosing Your Safety Level

Different AI tools offer different permission models. Understanding them helps you choose appropriate settings.

### Model 1: Permissive (Auto-Approve Safe Operations)

**How it works**: AI executes read operations and safe writes automatically; prompts for destructive actions

**Best for**: Experienced users, trusted AI, familiar codebase

**Example configuration**:
```
Auto-approve:
- Read operations (cat, grep, find)
- Test execution (npm test, pytest)
- Git status/diff
- File creation (new files only)

Require approval:
- File deletion (rm)
- Git reset/rebase
- Package installation
- Config file changes
```

### Model 2: Confirming (Approve All Writes)

**How it works**: AI prompts before any write operation

**Best for**: New AI collaboration, unfamiliar codebase, learning phase

**Example configuration**:
```
Auto-approve:
- Read operations only

Require approval:
- All write operations
- All file modifications
- All command execution
```

### Model 3: Restricted (Sandbox Mode)

**How it works**: AI can only read; cannot modify anything

**Best for**: Exploration, code review, understanding unfamiliar codebases

**Example configuration**:
```
Auto-approve:
- Read operations only

Blocked:
- All write operations
- All command execution
- All file modifications
```

### Choosing Your Model

| Situation | Recommended Model | Rationale |
|-----------|------------------|-----------|
| **First time with AI** | Confirming | Build trust before autonomy |
| **Routine work on familiar project** | Permissive | Efficiency for safe operations |
| **Exploring unfamiliar code** | Restricted | Understand before modifying |
| **Production systems** | Confirming + Staging | Extra caution for critical systems |
| **Prototype/experimental work** | Permissive | Speed over caution, rollback available |

## The Destructive Operations List

Know which commands require extra scrutiny. These should always trigger confirmation:

### File Operations
```bash
rm, rm -rf              # Delete files/directories
mv                      # Move (can overwrite)
cp                      # Copy (can overwrite)
> file                  # Redirect and overwrite
dd                      # Low-level disk write
```

### Version Control
```bash
git reset --hard        # Discard all changes
git rebase              # Rewrite history
git push --force        # Overwrite remote
git clean -fd           # Delete untracked files
git checkout -- .       # Discard working directory changes
```

### Package Management
```bash
npm install             # Can change dependencies
pip install             # Can change dependencies
apt install             # System-level changes
brew install            # System-level changes
```

### System Operations
```bash
sudo                    # Elevated privileges
systemctl               # Service management
kill -9                # Force kill processes
reboot, shutdown        # System operations
```

### Data Operations
```bash
DROP DATABASE           # Database destruction
DELETE FROM            # Data deletion (without WHERE)
TRUNCATE TABLE         # Remove all data
UPDATE (no WHERE)      # Modify all rows
```

## Sandboxing: Isolating AI Work

The most effective safety measure: **don't let AI touch production directly**.

### Sandbox Strategies

**1. Docker Container Sandbox**

```bash
# Run AI work in container
docker run -it -v $(pwd):/workspace -w /workspace node:18 bash

# AI works inside container
# Can't affect host system
# Can't access production resources
```

**2. Staging Environment**

```
AI works on: staging.example.com
Manual deploy: production.example.com

AI can make all the changes it wants to staging
You review before promoting to production
```

**3. Feature Branch Workflow**

```bash
# AI works on feature branch
git checkout -b feature/ai-work

# Changes isolated from main
# Merge only after review
```

**4. Separate Credentials**

```bash
# .env.ai - AI's environment
AI_DATABASE_URL=postgresql://localhost:5432/sandbox_db
AI_API_KEY=sandbox_key_limited_permissions

# .env - Production (never shown to AI)
PRODUCTION_DATABASE_URL=postgresql://prod-server:5432/real_db
PRODUCTION_API_KEY=production_key_full_permissions
```

## Trust Gradualism: Easing into Autonomy

Don't go from zero autonomy to full autonomy overnight. Build trust gradually.

### Phase 1: Observation Only (Week 1)

- AI reads files and explains them
- AI suggests changes but doesn't apply them
- You manually apply AI suggestions
- Goal: Understand AI's capabilities and patterns

### Phase 2: Supervised Autonomy (Week 2-4)

- AI makes changes in sandbox/feature branches
- You review all diffs before applying
- Destructive operations always require approval
- Goal: Build confidence with safety net

### Phase 3: Selective Autonomy (Month 2-3)

- AI autonomously handles safe operations (tests, linting)
- AI handles routine refactors within approved patterns
- Destructive operations still require approval
- Goal: Accelerate routine work while maintaining oversight

### Phase 4: Calibrated Autonomy (Month 3+)

- AI autonomously handles most operations
- Pre-approve known-safe command patterns
- Approval only for novel or high-risk operations
- Goal: Maximum efficiency with maintained safety

### Trust Signals to Track

Track these to decide when to increase autonomy:
- **Error rate**: How often does AI make mistakes?
- **Correction ease**: How easy is it to fix AI mistakes?
- **Pattern adherence**: Does AI follow project conventions?
- **Risk awareness**: Does AI avoid known dangerous operations?

## Safety Checklist: Before Each Session

Before starting an AI session, verify:

**Environment**:
- [ ] Working in correct directory (not production)
- [ ] On correct branch (feature branch, not main)
- [ ] Environment variables set correctly (sandbox credentials)
- [ ] Uncommitted work is backed up or committed

**Tool Configuration**:
- [ ] Permission mode appropriate for task
- [ ] Destructive operations require approval
- [ ] Read-only mode if just exploring
- [ ] Logging enabled for audit trail

**Mental Model**:
- [ ] Clear task scope (what AI should and shouldn't do)
- [ ] Identified high-risk operations to watch for
- [ ] Rollback plan if things go wrong
- [ ] Stopping point defined

## Incident Response: What to Do When Something Goes Wrong

Despite all precautions, things will go wrong. Have a plan.

### Immediate Actions

```bash
# 1. Stop the AI
# Ctrl+C or stop button

# 2. Assess damage
git status          # What changed?
git diff            # What's the diff?

# 3. If bad, revert
git checkout -- .   # Revert working directory
git reset --hard    # Reset to last commit

# 4. If already committed
git revert HEAD     # Revert the commit
git reset --hard HEAD~1  # Or remove commit entirely
```

### Post-Incident Review

After an incident, ask:
- What happened?
- Why did safeguards fail?
- What constraint would have prevented this?
- How do I adjust permissions/configuration?

### Example: AI Deleted Wrong Directory

**Incident**: AI ran `rm -rf node_modules/` but executed in wrong directory, deleting source files.

**Immediate**: Ctrl+C immediately. Assess damage with `git status`.

**Recovery**: `git checkout -- .` to restore from git.

**Prevention for next time**:
- Add safeguard: AI must `pwd` before destructive operations
- Change permission mode: require approval for all `rm` commands
- Add alias: `rm` → `rm -i` (interactive mode)

## Why This Principle Matters: Trust Through Safety

Paradoxically, **constraints enable autonomy**. When you have good safety measures:
- You feel comfortable giving AI more autonomy
- You can focus on high-level direction rather than worrying
- AI can be more effective without risking disaster

Without safety measures, you're constantly on edge—afraid to let AI do anything meaningful. With safety measures, you can collaborate confidently.

The goal isn't to prevent AI from doing anything. The goal is to prevent AI from doing **certain things**—while enabling everything else.

## This Principle in Both Interfaces

> "Cowork asks before deleting anything. This isn't just UX—it's architectural."

Constraints manifest differently in each interface, but the underlying safety model is the same.

| Constraint Type | Claude Code | Claude Cowork |
|-----------------|-------------|---------------|
| **Boundary** | Permission flags, CLAUDE.md restrictions | Folder selection, connector permissions |
| **Action** | Configured via settings/hooks | Built-in confirmation dialogs |
| **Resource** | API cost monitoring, token limits | Subscription limits apply |
| **Output** | Specified in prompts/Skills | Skills define output formats |

**In Cowork**: The confirmation dialogs ARE the constraint system. When Cowork asks "Should I delete this file?" or "Should I modify this document?", it's implementing the same safety principle that Claude Code's permission model provides. The difference is that Cowork's constraints are built into the GUI—you don't configure them, you respond to them.

**The paradox applies equally**: In both interfaces, constraints enable capability. When you trust the safety model, you give the agent more autonomy. Without constraints, you'd never let either agent do meaningful work on important files.

## Try With AI

### Prompt 1: Risk Assessment Exercise

```
I want to practice assessing safety risks in AI workflows.

Here's a scenario: I'm planning to have AI help me [describe a task—refactor database schema, update authentication system, optimize performance, etc.]

Help me assess:
1. What could go wrong? Brainstorm specific risks
2. What's the impact if something does go wrong?
3. What safety measures should I put in place?

For each safety measure, categorize it:
- Technical constraint (what to restrict)
- Permission control (what to approve)
- Environment isolation (where to work)
- Process control (how to work)
- Human verification (when to review)

Then, help me create a specific plan: "Before starting, I will X. During work, AI can Y but not Z. After work, I will verify W."
```

**What you're learning**: How to identify risks and design appropriate safety measures. You're developing the skill of anticipating problems before they occur and structuring AI work to be safe by design.

### Prompt 2: Permission Model Design

```
I want to design an appropriate permission model for my situation.

Here's my context:
- [Your experience level with AI]
- [How familiar you are with your codebase]
- [What you're working on—prototype, production, personal project, team project]
- [Your risk tolerance—low, medium, high]

Help me design a permission model:
1. Should I use Permissive, Confirming, or Restricted mode? Why?
2. What operations should be auto-approved?
3. What operations should require approval?
4. What operations should be blocked entirely?

Also, help me understand:
- When should I move to a more permissive model?
- What signals should I track to build trust?
- What would cause me to tighten restrictions?
```

**What you're learning**: How to choose appropriate permission models based on context and experience. You're learning to calibrate autonomy based on trust and risk—balancing safety with effectiveness.

### Prompt 3: Sandbox Setup

```
I want to set up a safe sandbox environment for AI work.

Help me design a sandboxing strategy for my project:
- [Project type—web app, data pipeline, scripts, etc.]
- [Current setup—local development, cloud, etc.]

I want to make sure:
1. AI can't affect production systems
2. AI can experiment freely without risk
3. I can easily promote AI work to production after review

Design a sandbox setup that includes:
- Directory structure (sandbox vs production)
- Git workflow (branches, merge process)
- Environment variables (sandbox credentials)
- Database approach (separate instances)
- Deployment process (manual promotion after review)

After we design it, help me actually set it up step by step.
```

**What you're learning**: How to create isolated environments where AI can work safely. You're learning to structure your workflow so that AI experimentation never puts production at risk—enabling confident collaboration.

### Safety Note

When in doubt, start with more restrictions and ease into autonomy. It's always easier to loosen constraints later than to recover from a preventable incident. The best safety measure is a cautious approach—especially when you're just starting with AI collaboration.
