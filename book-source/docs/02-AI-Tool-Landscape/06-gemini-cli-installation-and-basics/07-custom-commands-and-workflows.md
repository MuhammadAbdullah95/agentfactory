---
sidebar_position: 7
title: "Custom Commands & Professional Workflows"
duration: "40 min"
learning_objectives:
  - "Design custom commands that specify repeated workflows as reusable automation"
  - "Write TOML specifications for Gemini CLI that others (and future-you) can execute"
  - "Validate custom commands before deployment and test edge cases"
  - "Synthesize all Chapter 6 skills into professional-grade automation workflows"
  - "Compare and position Gemini CLI and Claude Code as complementary automation tools"
estimated_time: "40 minutes"
skills_taught:
  - skill: "Automation Specification Design"
    proficiency_level: "B1"
    domain: "Technical"
  - skill: "TOML Configuration Architecture"
    proficiency_level: "B1"
    domain: "Technical"
  - skill: "Specification-First Synthesis"
    proficiency_level: "B2"
    domain: "Meta-skill"
  - skill: "Tool Positioning & Decision-Making"
    proficiency_level: "B1"
    domain: "Conceptual"
generation_metadata:
  generated_by: "claude-code (lesson-writer agent)"
  source_spec: "specs/022-audit-chapter6-gemini-cli/spec.md"
  created: "2025-01-12"
  last_modified: "2025-01-12"
  git_author: "Claude Code"
  workflow: "constitutional-revision: 022-audit-chapter6-gemini-cli"
  version: "2.0.0 (constitutional alignment)"
---

# Custom Commands & Professional Workflows: Automation as Specification Architecture

## Introduction: Encoding Workflows Into Specifications

By now, you've mastered the foundations of Gemini CLI:

- **Lesson 1**: Why open source matters (and why Gemini CLI competes with Claude Code)
- **Lesson 2**: Installation and first conversations
- **Lesson 3**: Slash commands that orchestrate Gemini's behavior
- **Lesson 4**: GEMINI.md context files (specifications for project knowledge)
- **Lesson 5**: Memory checkpoints (specifications for conversation persistence)
- **Lesson 6**: MCP servers and Marketplace Extensions (specifications for capability integration)

This final lesson synthesizes everything into **professional-grade automation architecture**. You'll learn to encode repeated workflows as custom commands—specifications that others (including future-you) can understand and execute without explanation.

**The Mental Model Shift**: Custom commands aren't just shortcuts. They're *specifications for automation* that capture team knowledge and encode best practices into reusable patterns.

---

## The Core Problem: Repeated Workflows as Specification Debt

Imagine you perform this workflow twice a week:

```
Manual workflow (5-10 minutes, multiple steps):
1. Ask Gemini: "Research competitors for [market]"
2. Ask Gemini: "Summarize findings in a 1-page brief"
3. Save the brief to your notes
4. Ask Gemini: "Generate 3 social media posts based on findings"
5. Copy posts to your content calendar
```

**The Problem**: Each time, you:
- Re-explain the task to Gemini
- Repeat the same constraints and format preferences
- Copy-paste outputs manually
- Risk inconsistent results (Gemini may respond differently each time)

**The Specification Solution**: Encode this workflow as a custom command `/research-and-share` that:
- Defines inputs once (market, tone, format)
- Orchestrates all steps automatically
- Applies consistent constraints every execution
- Returns outputs in predictable format

**Result**: Weeks of knowledge captured in a reusable, shareable specification.

---

## Specification First: Why This Matters

Before diving into TOML syntax, understand the shift in thinking:

**Old mental model** (command-driven):
> "How do I create a Gemini custom command?"

**New mental model** (specification-driven):
> "What workflow should I automate? What should it accept as input? What output format do I need? How should it validate results?"

**Practice this principle now**: Every custom command you design should follow this pattern:

```markdown
## 1. Specification (WHAT & WHY)

**Goal**: Automate [task] to save [time/effort/consistency]

**Inputs** (what does the user provide):
- [parameter 1]: [description]
- [parameter 2]: [description]

**Expected Output** (what should the command return):
[describe format, structure, validation criteria]

**Success Criteria** (how do we validate it worked):
- [criterion 1]
- [criterion 2]

## 2. Prompt to AI (HOW)

Collaborate with AI: "Help me design a TOML configuration for this specification"
[Paste specification above]

## 3. Implementation (TOML)

[Generated TOML configuration]

## 4. Validation (DID IT WORK)

- [ ] Command executes without errors
- [ ] Output matches specification
- [ ] Edge cases handled correctly
- [ ] Works for team members, not just me
```

This pattern—Specification→Prompt→Code→Validation—is the same pattern you use for AI-native development. Custom commands are just another application.

---

## TOML: The Configuration Language for Custom Commands

Gemini CLI uses **TOML** (a simple, human-readable configuration format) to define custom commands.

### Basic Anatomy

Every custom command has three essential parts:

```toml
# File location determines command name:
# ~/.gemini/commands/research.toml  →  /research command

# Part 1: Metadata (what is this command?)
description = "Research a topic using multiple MCP servers and summarize findings"

# Part 2: Parameters (what inputs does user provide?)
# {{parameter_name}} is replaced with user input at execution time

# Part 3: Prompt template (what does Gemini do?)
prompt = """
Using available MCP servers, research {{topic}} and provide:
- Current state of the field
- Recent developments (last 6 months)
- Key trends
- 3 resources for learning more

Format as a structured markdown report.
"""
```

### Real-World Example: Specification → TOML

**Specification** (what we want):

> Build a command that analyzes our TypeScript codebase for security issues. It should:
> - Accept a file path as input
> - Check for common security patterns (hardcoded secrets, unsafe dependencies, XSS vulnerabilities)
> - Format findings as a structured report
> - Return actionable remediation steps
> - Succeed even if no vulnerabilities found (don't error)

**Prompt to AI**:

> Help me design a TOML configuration for this Gemini CLI custom command:
> [paste specification above]

**AI-Generated TOML** (example output):

```toml
# ~/.gemini/commands/security-audit.toml  →  /security-audit
description = "Security audit of TypeScript files for vulnerabilities"

prompt = """
Review the TypeScript file(s) at {{filepath}} for security issues.

Specifically check for:
1. Hardcoded secrets (API keys, tokens, credentials)
2. Unsafe dependencies (known vulnerabilities in package.json)
3. XSS vulnerabilities (unsanitized DOM operations)
4. Authentication/Authorization gaps
5. SQL Injection patterns (if applicable)

For each issue found, provide:
- Issue description
- Risk severity (Critical/High/Medium/Low)
- Location in code
- Remediation step-by-step

If NO issues found, respond: "✓ Security review complete—no vulnerabilities detected in {{filepath}}"
"""
```

**Validation** (did it work?):

```bash
# Test 1: File with a vulnerability
/security-audit filepath=src/auth.ts
# Expected: Returns issues with remediation steps

# Test 2: Secure file
/security-audit filepath=src/utils.ts
# Expected: Returns "✓ Security review complete..." message

# Test 3: Non-existent file (edge case)
/security-audit filepath=src/missing.ts
# Expected: Graceful error message (doesn't crash)
```

---

## Two Levels of Custom Commands

### Level 1: User Commands (`~/.gemini/commands/`)

**Purpose**: Workflows you use across multiple projects

**Examples**:
- `/research` — General research tool (works for any topic)
- `/brainstorm` — Idea generation (works for any domain)
- `/explain` — Teach you an unfamiliar concept
- `/architecture-review` — Suggest architecture improvements

**Execution**:
```bash
mkdir -p ~/.gemini/commands/
# Create TOML files here; they're available in ALL projects
```

**Sharing**: Copy your `~/.gemini/commands/` directory to teammates

### Level 2: Project Commands (`./gemini/commands/`)

**Purpose**: Workflows specific to this codebase

**Examples**:
- `/spec` — Generate API specification from project code
- `/migration-plan` — Plan database migrations for THIS project
- `/test-strategy` — Suggest testing approach for project's tech stack
- `/compliance-check` — Verify compliance with project's standards

**Execution**:
```bash
mkdir -p ./gemini/commands/
# Create TOML files here; committed to Git, shared with team
```

**Sharing**: These commands are in your Git repo—teammates clone and use automatically

---

## The Three-Role AI Partnership: Designing Commands Together

Custom commands are perfect for demonstrating the Three-Role AI Partnership. Let's walk through a real example:

### Role 1: AI as Teacher

**You say**: "I want to build a custom command for code review. Teach me: what makes a good code review specification? What should I include?"

**AI teaches**: "A good code review specification should include:
- What you're checking FOR (security, performance, style, maintainability)
- WHO should perform the review (AI vs human developers)
- FORMAT for output (structured findings, not narrative)
- CONSTRAINTS on review scope (just this function vs entire module)
- SEVERITY LEVELS for different issue types

Here's a template specification to start with: [AI provides structured template]"

**What you learned**: A code review command needs 5 distinct parts, and AI suggested a template you wouldn't have created solo.

### Role 2: AI as Student

**You provide context**: "Our team does code reviews on pull requests. We specifically care about:
- Readability (new devs need to understand our code)
- Test coverage (we require 80%+ coverage)
- Security (compliance requirement for fintech)
- Performance (we have performance SLAs)"

**AI adapts**: "Given your context, I'd prioritize the review in this order:
1. Security (compliance, not optional)
2. Performance (SLAs matter)
3. Test coverage (team policy)
4. Readability (developer experience)

I'm adjusting the command to check security FIRST, then fail fast if critical issues found. This saves your team time on non-critical issues."

**What AI learned**: Your specific constraints (compliance, SLAs) changed the command architecture. AI incorporated your domain knowledge into the design.

### Role 3: AI as Co-Worker

**Collaborative design**:
- **You provide**: Business constraints (compliance, performance SLAs, team policies)
- **AI provides**: Technical architecture (command structure, error handling, output formatting)
- **Together**: You converge on a command that balances business needs with technical elegance

**Result**: Better command than either of you could design alone. You focused on business logic; AI handled technical execution.

---

## Building Your First Custom Command: A Walkthrough

### Step 1: Identify a Repeated Workflow

Look at your work week. What do you ask Gemini repeatedly?

Examples:
- "Analyze this data file and suggest visualizations"
- "Review this code for bugs"
- "Generate documentation for this API"
- "Suggest test cases for this function"
- "Explain this error message"

**Your task**: Write down one workflow you repeat 2+ times per week.

### Step 2: Write the Specification

Before touching TOML, specify what the command should do:

```markdown
## Command Specification

**Name**: [short, verb-based name]

**Purpose**: Automate [your repeated workflow]

**Inputs** (what does the user provide?):
- Input 1: [description and constraints]
- Input 2: [description and constraints]

**Processing** (what steps should happen?):
1. [step 1]
2. [step 2]
3. [step 3]

**Output** (what format should results be?):
[describe structure, sections, formatting]

**Success Criteria** (how do we know it worked?):
- [criterion 1]
- [criterion 2]
- [criterion 3]

**Edge Cases** (what could go wrong?):
- If [edge case], then [expected behavior]
```

### Step 3: Design with Your AI Partner

**Prompt to Gemini**:
```
I want to create a Gemini CLI custom command. Here's the specification:

[paste your specification above]

Help me:
1. Identify gaps in my specification
2. Suggest the TOML structure
3. Write the prompt template that should go in the command
```

**What happens**: AI teaches you what you missed, suggests improvements, and provides the TOML template.

### Step 4: Create the TOML File

```bash
# Create the command file
mkdir -p ~/.gemini/commands/    # User command
# OR
mkdir -p ./gemini/commands/     # Project command

# Use your chosen name
touch ~/.gemini/commands/yourcommand.toml
```

Paste the TOML from AI, then test.

### Step 5: Test With Sample Inputs

**Test happy path** (expected input):
```bash
/yourcommand input1="sample" input2="another"
# Expected: Command succeeds, output matches specification
```

**Test edge cases** (unusual inputs):
```bash
/yourcommand input1="very long text with special chars !@#$%"
# Expected: Command handles gracefully

/yourcommand input1=""
# Expected: Command errors with helpful message (or succeeds with default)
```

**Refine based on results**: If output doesn't match specification, ask Gemini:
```
My custom command isn't producing the expected output. Here's what I got:
[paste actual output]

Here's what I expected:
[paste expected output from spec]

How should I adjust the TOML to fix this?
```

### Step 6: Document for Your Team

Create a README explaining the command:

```markdown
## /yourcommand

**Purpose**: [one-line description]

**Usage**:
/yourcommand input1="value" input2="value"

**Parameters**:
- input1: [description]
- input2: [description]

**Example**:
/yourcommand input1="security" input2="src/auth.ts"

**Output**: [describe what user gets back]

**Common Use Cases**:
1. [Use case 1]
2. [Use case 2]
```

---

## Validation: Testing Commands Before Deployment

Never deploy a custom command to your team without validation.

### Validation Checklist

#### Technical Validation

- [ ] **Command syntax is valid** — No TOML parsing errors
- [ ] **Parameters work correctly** — `{{param}}` placeholders are replaced with actual inputs
- [ ] **No hardcoded secrets** — No API keys, passwords, or credentials in the TOML
- [ ] **Error handling** — Command fails gracefully (doesn't crash) when given invalid input
- [ ] **Output is deterministic** — Same input always produces same format output (content may vary)

#### Specification Validation

- [ ] **Matches specification** — Output format matches what specification promised
- [ ] **Inputs are sufficient** — User provides everything needed; no missing context
- [ ] **Success criteria are clear** — You can verify command succeeded without ambiguity
- [ ] **Edge cases handled** — Empty input, very long input, special characters all work or error gracefully

#### Team Validation

- [ ] **Works on other machines** — Test on Windows, macOS, and Linux (or your team's platforms)
- [ ] **Works for teammates** — Someone else (not you) runs the command successfully
- [ ] **Documentation is clear** — README explains everything a new team member needs
- [ ] **No proprietary assumptions** — Doesn't assume team member has specific tools, credentials, or setup

### Example: Validation in Action

**Before deployment**, test edge cases:

```bash
# Happy path (expected use)
/security-audit filepath=src/auth.ts
# ✓ Should return security findings

# Empty parameter
/security-audit filepath=
# ✓ Should error: "filepath cannot be empty"

# Non-existent file
/security-audit filepath=src/missing-file.ts
# ✓ Should error gracefully: "File not found: src/missing-file.ts"

# Very long filepath
/security-audit filepath=src/very/deeply/nested/path/with/many/segments/file.ts
# ✓ Should work (handle long paths)

# Special characters in filepath
/security-audit filepath="src/files with spaces.ts"
# ✓ Should work (handle quoted paths)
```

If any test fails, ask your AI partner:
```
My /security-audit command failed this test case:
[describe test case and error]

How should I adjust the TOML to handle this correctly?
```

---

## Complementary Workflows: Gemini CLI + Claude Code Together

This is Lesson 7's key insight: **Both Gemini CLI and Claude Code support custom automation**. They're not competitors; they're complementary.

### Gemini CLI Custom Commands: Best For

- **Large codebase analysis** — 1M token context window handles massive projects
- **Open source workflows** — Free tier ($0) makes it ideal for learning and open source
- **Extensibility** — MCP servers and Marketplace Extensions add capabilities
- **Team sharing** — Commands in Git repos spread knowledge across team
- **Cross-platform** — Terminal-based works everywhere

**Example**: Your team uses Gemini CLI `/code-review` command to analyze pull requests. It's free, works on all platforms, and leverages open source MCP integrations.

### Claude Code Skills: Best For

- **Iterative, web-based exploration** — Chat interface perfect for back-and-forth
- **Complex reasoning** — Anthropic's training excels at nuanced decisions
- **Enterprise workflows** — Superior context understanding for large codebases
- **Proprietary integrations** — Native integrations with existing tools (GitHub, Slack, etc.)
- **Visual feedback** — Web interface shows code side-by-side with analysis

**Example**: Your enterprise uses Claude Code Skills for API design and architectural reviews. The web interface supports iterative discussion, and Claude's stronger reasoning catches subtle design issues.

### Decision Framework: Which Tool for Your Workflow?

Use this matrix to decide:

| Workflow Need | Gemini CLI | Claude Code | Both Together |
|---------------|-----------|------------|---------------|
| **Quick analysis, free tier** | ✓ Best | Paid | Gemini CLI |
| **Iterative exploration** | ✓ OK | ✓✓ Better | Claude Code |
| **Team sharing, Git-based** | ✓✓ Better | ✓ OK | Gemini CLI |
| **Enterprise reasoning** | ✓ OK | ✓✓ Better | Claude Code |
| **Large codebase (1M tokens)** | ✓✓ Better | ✓ OK | Gemini CLI |
| **Visual chat interface** | ✓ CLI | ✓✓ Better | Claude Code |
| **MCP Marketplace Extensions** | ✓✓ Better | ✓ OK | Gemini CLI |
| **Skills/plugins system** | ✓ Commands | ✓✓ Better | Claude Code |

**Neither is "better"—they're optimized for different contexts.**

### Example: Using Both in One Project

**Scenario**: Your team maintains a 500K-line Python codebase.

**Gemini CLI custom command** (`/code-review`):
- Analyzes pull requests for security/style
- Free tier saves cost at scale
- Runs in CI/CD pipeline (terminal-based)
- Result: Consistent, automated gate on code quality

**Claude Code Skills**:
- Architects major refactorings
- Reasons about complex performance issues
- Explores design alternatives interactively
- Result: Deep thinking on hard decisions

**Together**: Gemini CLI handles routine checks (fast, cheap); Claude Code handles complex analysis (careful reasoning).

---

## Red Flags to Watch: Common Command Mistakes

### Red Flag 1: Hardcoded Secrets

```toml
# ❌ BAD: API key in command
prompt = """
Using Context7 API key "sk-abc123...xyz", research {{topic}}
"""

# ✓ GOOD: Use environment variables or configuration
prompt = """
Using configured research APIs, research {{topic}}
"""
```

**Why**: If you share this command, you leak credentials.

### Red Flag 2: Unclear Parameters

```toml
# ❌ BAD: Vague parameter name
{{input}}

# ✓ GOOD: Descriptive parameter name
{{topic_to_research}}
```

**Why**: Future-you won't remember what `{{input}}` means.

### Red Flag 3: No Output Format Specification

```toml
# ❌ BAD: Vague expected output
prompt = "Research {{topic}} and tell me about it"

# ✓ GOOD: Specify exact format
prompt = """
Research {{topic}} and provide:
1. Definition (2-3 sentences)
2. Current trends (bulleted list)
3. Key players (table format)
4. Resources (3 links with descriptions)
"""
```

**Why**: Without format specification, output varies wildly between executions.

### Red Flag 4: Commands That Require Explanation

```toml
# ❌ BAD: Requires explanation to use
/command-x

# ✓ GOOD: Clear, obvious purpose
/security-audit filepath=src/auth.ts
```

**Why**: If teammates need to ask "what does this command do?", your specification failed.

### Red Flag 5: No Error Handling

```toml
# ❌ BAD: Will crash if input is invalid
prompt = """
Analyze {{filepath}}
"""

# ✓ GOOD: Handles edge cases
prompt = """
If {{filepath}} is provided:
  - Analyze {{filepath}}
Else:
  - Return error: "filepath parameter required"
"""
```

**Why**: Robust commands are usable; fragile ones are frustrating.

---

## Capstone Synthesis: Putting It All Together

Lesson 7 is the final lesson in Chapter 6. Let's synthesize everything:

### What You've Learned (Lessons 1-7)

**Lesson 1**: Why open source matters → Gemini CLI's value proposition
**Lesson 2**: Installation and authentication → Tools you use daily
**Lesson 3**: Slash commands (`/memory`, `/mcp`, `/stats`) → Gemini's built-in orchestration
**Lesson 4**: GEMINI.md context files → Specification architecture for project knowledge
**Lesson 5**: Memory checkpoints → Specification persistence across sessions
**Lesson 6**: MCP servers and Marketplace Extensions → Extensible capability ecosystem
**Lesson 7**: Custom commands → Specification-based automation (this lesson)

### Professional-Grade Workflow

Putting these pieces together, here's what professional Gemini CLI workflow looks like:

```markdown
## Complete Workflow: Building a Team Automation Suite

### Step 1: Project Context (Lesson 4)
Create ./GEMINI.md specifying your project (tech stack, conventions, architecture)

### Step 2: Shared Memory (Lesson 5)
Save checkpoints after important context: /memory save checkpoint=project-state-v2

### Step 3: MCP Integration (Lesson 6)
Install Marketplace Extensions your team needs: gemini extensions install [source]

### Step 4: Custom Commands (Lesson 7)
Design commands that encode team workflows:
/spec — Generate specification
/review — Review code
/test-strategy — Suggest testing approach
/migration-plan — Plan database migration

### Step 5: Sharing and Distribution
Commit commands to Git: ./gemini/commands/
Team members clone and use automatically

### Step 6: Continuous Refinement
Each week, refine commands based on feedback:
- What commands are slow? Optimize prompts.
- What commands are confusing? Improve documentation.
- What workflows aren't covered? Create new commands.
```

**Result**: Your team has a living, evolving automation suite. Gemini CLI becomes a development platform, not just a tool.

---

## Exercises

### Exercise 1: Specify a Repeated Workflow

Identify a workflow you perform 2+ times per week.

**Write a specification** (no TOML yet):

```markdown
## Workflow Specification

**Name**: [your command name]
**Purpose**: [one-line description]
**Inputs**: [what user provides]
**Processing**: [what steps happen]
**Output**: [format and structure]
**Success Criteria**: [how to validate]
**Edge Cases**: [what could go wrong]
```

Save this specification. You'll use it in Exercise 2.

### Exercise 2: Design TOML With AI Partner

Using the specification from Exercise 1:

**Prompt your Gemini CLI**:
```
I want to create a custom Gemini command. Here's my specification:

[paste your specification from Exercise 1]

Please:
1. Identify any gaps in my specification
2. Suggest the TOML structure
3. Write the prompt template
```

**Study the output**: How did AI improve your specification? What did you miss?

### Exercise 3: Create and Test

Create the actual custom command:

**Step 1**: Create file
```bash
mkdir -p ./gemini/commands/
touch ./gemini/commands/yourcommand.toml
```

**Step 2**: Paste AI's TOML output

**Step 3**: Test the happy path
```bash
/yourcommand param1="sample" param2="another"
```

**Step 4**: Test an edge case
```bash
/yourcommand param1="" param2="something"
```

**Step 5**: Document it
```markdown
## /yourcommand

[Brief description]

**Usage**: /yourcommand param1="value" param2="value"
**Example**: /yourcommand param1="X" param2="Y"
```

---

## Key Professional Principles

### Principle 1: Specification First, Implementation Second

Don't design TOML syntax first. Specify behavior first. Let TOML be the implementation detail.

```
Wrong order: "What's the TOML syntax?" → Build command → Hope it works

Right order: "What should this do?" → Specify → Design TOML → Validate
```

### Principle 2: Commands Are Team Knowledge

Every custom command encodes something your team knows. Document it like you would important knowledge.

### Principle 3: Validation Before Sharing

Test your command on multiple machines, with edge cases, with team members. Never share untested automation.

### Principle 4: Commands Evolve

Your first version won't be perfect. Gemini CLI lets you version and update commands. Treat them like living documentation.

### Principle 5: Tool Positioning Matters

Gemini CLI and Claude Code both do automation. Choose each for its strengths. Use both in the same project when appropriate.

---

## Try With AI: Professional Custom Command Design

This section synthesizes all Chapter 6 skills into AI-partnered practice. You'll design a real custom command using the Three-Role AI Partnership.

**Tool Selection**: Use Gemini CLI directly (you need to test commands you build)

**Step 1: AI Teaches You** (5 min)

Open Gemini CLI and ask:
```
I want to create a professional custom command for my team.
Teach me: What makes a good custom command specification?
What sections should I include? What questions should I answer
BEFORE writing TOML?
```

**Expected AI Response**: AI teaches you a 5-7 step specification template, explaining why each part matters.

**What You Learn**: Command design requires specification clarity before implementation.

---

**Step 2: AI Learns From Your Context** (10 min)

Provide your specific workflow:
```
My team does this repeatedly: [describe a workflow YOU perform weekly]

We specifically care about: [list your constraints, goals, or requirements]

Here's what we currently do manually: [describe the current process]

How would a custom command improve this? What should the command accept as input
and produce as output?
```

**Expected AI Response**: AI adapts to your specific context, asks clarifying questions, and suggests a command architecture that fits YOUR needs (not a generic example).

**What AI Learns**: Your domain constraints, team size, and business priorities shape the command design.

---

**Step 3: AI and You Co-Design** (15 min)

Collaborate on the TOML design:

**First, you specify**:
```
Based on our discussion, here's my command specification:

[paste the specification you wrote in Step 1]
```

**Then AI designs**:
```
Here's the TOML configuration for this specification:

[AI provides TOML]

This design:
- Uses these parameters: [lists them]
- Handles these edge cases: [lists them]
- Validates output with: [describes validation]
```

**Then you refine** (if needed):
```
This looks good, but I want to adjust [aspect].
Can you [specific change request]?
```

**Result**: TOML that reflects both your requirements AND AI's technical expertise.

---

**Step 4: You Validate** (10 min)

Create the command and test it:

```bash
# Create the file
mkdir -p ./gemini/commands/
# Name it based on your command name
touch ./gemini/commands/yourcommand.toml

# Paste the TOML from AI
# Test it
/yourcommand param1="test value"
```

**Report to AI**:
```
I created the command and tested it. Here's what happened:

[Describe test result: did it work? Any issues?]

Expected output: [what you expected]
Actual output: [what you got]

Should I adjust the TOML?
```

---

**Step 5: Reflect on Co-Learning** (5 min)

Pause and reflect:

- **What did AI teach you?** (What did you learn that you didn't know before?)
- **What did you teach AI?** (What did AI learn about your context/constraints?)
- **What's the conversation level?** (Is this partnership, or are you just using a tool?)

Write a 2-3 sentence reflection on how collaboration improved the command.

---

**Safety Reminder**: Test all custom commands on non-production data before deploying to your team. Validate that commands handle edge cases gracefully (empty input, very long input, special characters) without crashing.

---

## What's Next: From Tool User to Tool Builder

Congratulations—you've completed Chapter 6.

You now understand Gemini CLI not as a "second choice" to Claude Code, but as a **complementary tool** with distinct strengths:

- **Open source** — You can read, modify, and fork the code
- **Free tier** — Enables learning and open source work
- **MCP ecosystem** — Extensible through Marketplace Extensions
- **Custom commands** — Specification-based automation
- **Team sharing** — Commands in Git repositories spread knowledge

You've progressed from **tool user** (Lesson 1-2) to **power user** (Lesson 3-6) to **tool architect** (Lesson 7).

**Next chapters** (Part 2, Chapters 7-8) will deepen your understanding of cross-tool workflows (Bash essentials, Git integration), preparing you for the professional automation workflows in Parts 3-4.

Your custom commands are waiting. Start building.
