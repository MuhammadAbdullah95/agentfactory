---
sidebar_position: 5
title: "Creating and Using Agent Skills"
---

# Agent Skills: Teaching Claude Your Domain Expertise

## The Power of Ambient Autonomous Expertise

Imagine your team has a specialist in security, another in performance optimization, a third in documentation standards. What if every member of your team could leverage that expertise automatically—not by asking for help, but because Claude Code has learned what your organization values and proactively applies it?

That's what **Agent Skills** do. Skills are executable specifications that teach Claude Code YOUR domain expertise. Unlike subagents (which you delegate to explicitly) or commands (which you invoke manually), skills work **autonomously**: you define what expertise matters, and Claude decides when and how to apply it.

**Ambient** = Claude recognizes opportunities without being asked
**Autonomous** = Claude acts based on YOUR priorities, not generic best practices
**Expertise** = YOUR organizational knowledge, standards, and patterns

This is **Tier 2 of the Graduated Teaching Pattern** (Principle 13 in action): You specify the expertise that matters to your work, and Claude Code handles the complex execution of applying it everywhere it's relevant.

---

## What Are Agent Skills? (Teaching Claude What Matters to YOU)

**Definition**: An Agent Skill is a discoverable, autonomous capability defined by a `SKILL.md` file. Skills capture your domain expertise in a specification that Claude learns and applies proactively across your work.

Think of it this way:

**Traditional approach**: You manually check code against your standards each time
- "Is this following our security patterns?"
- "Does this match our performance guidelines?"
- "Is the documentation complete?"

**Skills approach**: You encode standards once
- Claude learns what matters to YOUR team
- Claude watches for opportunities automatically
- Claude suggests improvements without being asked

**This is co-learning in action**: You as teacher (define expertise), Claude as student (learn what matters), then Claude as teacher (apply expertise autonomously).

### Skills vs. Subagents vs. Slash Commands

You've now seen three ways to extend Claude Code. Here's how they differ:

| Feature | Subagent | Agent Skill | Slash Command |
|---------|----------|-------------|---------------|
| **Invocation** | Explicit or auto‑delegated | **Autonomous**: Claude discovers and suggests | Explicit: `/command-name` |
| **Discovery** | Manual—you decide when to run | **Automatic**—Claude decides based on context | Manual—you type the command |
| **Use Case** | Repetitive focused tasks | Domain expertise applied automatically | Predefined workflows |
| **Example** | `claude agent run code-reviewer` | Claude detects Python file, suggests docstrings | `/commit` to create git commit |
| **Competitive Advantage** | Medium (consistency) | **High (scales expertise)** | Low (simple automation) |
| **Learning Pattern** | Tier 1 (you direct) | Tier 2 (you specify intent, AI executes) | Tier 1 (you direct) |

**Working together**: Subagents isolate execution for big decisions. Skills refine outputs across everything you do.

---

## Why Agent Skills Matter: Strategic Organizational Assets

Agent Skills aren't just technical features—they're **organizational assets that create business value**.

### 🎓 Expert Insight: Domain Expertise as Competitive Advantage

Here's the strategic difference:

**Without Skills**: Your team has expertise locked in people's heads
- Senior developer explains best practices → junior developer forgets 60% within a week
- Security patterns known to one expert → other developers make mistakes
- Performance optimizations exist scattered across projects
- Process repeats for every new hire; knowledge never captured

**With Skills**: Your team's expertise becomes automated advantages
- Encode expertise once (SKILL.md) → applied automatically across all work
- Every developer benefits immediately (no waiting for expert review)
- Knowledge captured permanently in version control (becomes institutional memory)
- New team members inherit organizational standards automatically

**Example comparison**:

**Fintech company WITHOUT skills**:
- Compliance expert manually reviews code for regulatory violations
- Developers ship non-compliant code, discover violations in production
- Fixing violations costs 10x more in production than pre-commit
- Time per review: 45 minutes, happens after development is complete

**Fintech company WITH `compliance-checker` skill**:
- Developers get real-time compliance feedback while writing code
- Non-compliant patterns caught immediately (instant feedback loop)
- Developers learn patterns by seeing them flagged
- Review time: 5 minutes (confirming, not finding problems)
- Result: Compliant by default, faster shipping, lower production risk

**The pattern**: Expertise encoded as skills compounds over time. Custom skills become organizational capabilities that competitors lack.

**Strategic value**:
1. **Consistency**: Every developer follows same standards (regardless of experience)
2. **Speed**: Catch issues before review (shift left—prevent, don't catch)
3. **Hiring**: New team members inherit expertise (onboarding accelerated)
4. **Scaling**: Expertise applies to 10x more code without 10x more people

This is "Specs as Strategic Assets"—specifications that create business value, not just code correctness.

---

## How Agent Skills Work: Teaching Claude to Recognize Opportunities

Let's understand how skills discover when they're relevant.

### Skill Anatomy: The SKILL.md File

Every skill is defined by a `SKILL.md` file with three critical sections:

**1. Discoverable Description** (most important):
- Clear trigger: when should Claude suggest this skill?
- Outcome: what does the skill produce?
- Scope and boundaries: what it will and will not do

**2. Skill Instructions**:
- Checklist of steps to follow
- Quality bar: what good output looks like
- Edge cases and constraints to respect

**3. Examples** (optional):
- Brief before/after descriptions (no code required)

---

## Why SKILL.md Structure Matters

Skills are specifications with two audiences:

1. **Human reader** (you and your team): Understand what the skill does, when to use it, what standards it enforces
2. **Claude Code parser** (AI): Recognize when to invoke automatically, what triggers apply, how to execute

This dual-audience design is intentional. Well-written skills are:
- **Readable documentation**: Team members onboard by reading SKILL.md
- **Executable automation**: Claude Code recognizes opportunities and applies them
- **Institutional memory**: Captures "how we do things" permanently

Your team's SKILL.md library isn't just documentation—it's **automated expertise that EXECUTES**.

### 💬 AI Colearning Prompt

> **Explore with your AI**: "I work in [your domain: web development, data science, DevOps, security, mobile, etc.]. I want to capture our team's expertise as skills. Suggest 3-5 skills that would be valuable for MY work. For each skill, describe: (1) What expertise it captures, (2) When it should trigger autonomously, (3) How it saves time or improves quality, (4) What a 'good' output from this skill looks like."

---

## Skill Scopes: Where Skills Live

Skills can exist at three levels:

**1. Personal Skills** (`~/.claude/skills/`)
- Your personal toolkit
- Not shared with projects or team
- Use for personal workflow preferences
- Example: Your personal code style preferences

**2. Project Skills** (`.claude/skills/` in project directory)
- Specific to one project
- Committed to version control
- Team members inherit when they clone the repo
- **Most common for team collaboration**
- Example: Project-specific compliance rules, team coding standards

**3. Plugin Skills** (installed from skill registry)
- Publicly available skills
- Installed with `claude skill install <name>`
- Maintained by community or vendors
- Example: Industry-standard security checkers, common patterns

**Best Practice**: Use **project skills** for team standards and domain expertise. This ensures everyone on the team benefits from shared knowledge and the standards evolve with your project.

---

## Teaching Claude What Matters to YOU: The Discovery Mechanism

Discovery isn't just a technical mechanism—it's how you teach Claude Code YOUR priorities.

**Traditional approach**: You remember to apply your team's patterns manually each time
**Skills approach**: You specify patterns once (SKILL.md), Claude applies them autonomously

When you create a skill, you're saying: "Claude, THIS expertise matters in MY work. Watch for situations where it's relevant and proactively help."

Discovery is the moment Claude transitions from **Student** (learning what you value) to **Teacher** (applying that knowledge to help you).

### How Discovery Works

Claude Code discovers skills from `SKILL.md` descriptions and automatically suggests them when relevant. Here's the flow:

1. **You create SKILL.md** in your project's `.claude/skills/` directory
2. **You describe the trigger**: "Activate this skill when..." (recognizing Python code, database queries, API design, etc.)
3. **Claude reads descriptions** during relevant tasks
4. **Claude suggests skill**: "I noticed this situation matches your [skill name] skill. Should I apply it?"
5. **You accept or refine**: Claude learns your preferences and adapts

**🤝 Practice Exercise: Define Expertise to Teach Claude**

Your goal: Define one expertise area Claude should learn about your work

1. **Identify expertise**: What do you check for repeatedly?
   - Security patterns? Code style inconsistencies? Documentation gaps?
   - Performance optimizations? API design conventions? Testing coverage?
   - Choose ONE that appears in 3+ of your recent projects

2. **Describe the trigger**: When should Claude apply this expertise?
   - "When writing database queries..."
   - "When creating API endpoints..."
   - "When implementing authentication..."
   - "When writing documentation..."

3. **Write specification** (3-5 sentences):
   ```
   Skill: [Name]
   Expertise: [What knowledge this captures]
   Trigger: [When to apply autonomously]
   Output: [What Claude should suggest/check/provide]
   Success Criteria: [What good looks like]
   ```

4. **Reflection**: If you had 5 such skills configured, how would your workflow change?
   - Less manual review?
   - Faster feedback loops?
   - Consistency across projects?
   - What would surprise you about having these skills?

**Note**: You don't need to implement this as SKILL.md yet—you're practicing specification-first thinking (define WHAT matters before HOW to build it). This is Principle 3 in action: "Specs Are the New Syntax."

---

## Configuring Pre-Built Skills: Tier 2 Teaching (Configure, Don't Build Yet)

Claude Code follows the **Graduated Teaching Pattern** (Principle 13):

- **Tier 1** (Book teaches): Understanding what skills are, why they matter, how discovery works
- **Tier 2** (AI Companion handles): Configuring and using pre-built skills ← **YOU ARE HERE**
- **Tier 3** (AI Orchestration): Building custom skills from scratch (advanced, not required for Part 2)

**For this lesson**: Focus on configuration and strategic use. Custom skill creation is advanced—you'll learn it when needed, guided by Claude Code.

**Why this matters**: Most productivity gains come from configuring existing skills well, not building new ones. Master the 80/20 first.

### Quick Start: Add One Pre-Built Skill and See It Work

Goal: Configure a project skill that helps your specific domain (choose one):

1. **Identify a pre-built skill** that matches your work:
   - Security: `security-reviewer`, `dependency-auditor`
   - Performance: `performance-analyzer`, `optimization-helper`
   - Documentation: `doc-generator`, `api-documenter`
   - Testing: `test-generator`, `coverage-analyzer`
   - (Ask your Claude Code agent: "What pre-built skills exist for [my domain]?")

2. **Read the skill's SKILL.md file** in `.claude/skills/`:
   - Understand what expertise it captures
   - Note the trigger (when it activates)
   - See example outputs

3. **Customize ONE setting** to match YOUR context:
   - Example: Update security skill with YOUR team's threat model
   - Example: Customize test generator to use YOUR testing framework
   - Example: Configure doc generator with YOUR documentation style

4. **Test the skill**: Ask Claude to help with a task where this skill applies
   - "Review this code for security issues"
   - "Generate tests for this function"
   - "Document this API endpoint"

5. **Observe**: Did Claude invoke the skill autonomously? What did it suggest?

6. **Verify**: Check if the skill understood your customizations correctly

**Expected outcome**: Claude applies the skill automatically, suggesting improvements aligned with YOUR project's standards (not generic best practices).

---

## 🎓 Expert Insight: The 80/20 of Skills

**80% of value**: Configuring 5-10 pre-built skills for YOUR context
- Example: Configure `code-review` skill with YOUR team's linting rules and style guide
- Example: Configure `test-generator` skill with YOUR testing framework and patterns
- Example: Customize `documentation` skill with YOUR team's documentation format
- **Result**: YOUR standards applied automatically across all work

**20% of value**: Building custom skills from scratch
- Only needed when no pre-built skill fits YOUR unique domain
- Requires more effort but unlocks capabilities not in pre-built library
- Best approach: Try pre-built first, build custom when clear gap identified

**Strategic decision**: Start with configuration. Build custom only when you've invested time with pre-built skills and identified a specific expertise gap that they don't address.

This mirrors real software development—use libraries first, build custom when necessary. Don't reinvent the wheel.

---

## 🤝 Practice Exercise: Configure Your First Skill

This exercise turns theory into experience.

**Your goal**: Successfully configure a pre-built skill for your work

**Time estimate**: 15-20 minutes

**Steps**:

1. **Choose ONE pre-built skill** relevant to your work
   - Pick something you check for regularly (code style, security, documentation, testing, etc.)
   - Look in `.claude/skills/` for available options
   - Or ask Claude: "What skills do you have configured?"

2. **Find and read the SKILL.md file**
   - Navigate to `.claude/skills/[skill-name]/SKILL.md`
   - Read the description, trigger conditions, and examples
   - Understand: "What expertise does this skill capture?"

3. **Customize ONE configuration** to match YOUR workflow:
   - If configuring a security skill: Update threat model or vulnerability types
   - If configuring a test-generator: Set preferred testing framework
   - If configuring documentation: Set documentation format/template
   - **Keep it simple**: Change just one thing (don't overwhelm yourself)

4. **Test the skill with real work**:
   - Start a task where this skill applies
   - Ask Claude: "Can you help with [task where skill applies]?"
   - Observe: Does Claude suggest using the skill? Does it apply your customizations?

5. **Evaluate results**:
   - Did Claude recognize when the skill was relevant?
   - Did it apply YOUR team's standards (not generic defaults)?
   - Were the suggestions helpful?
   - What would you change about how the skill works?

6. **Reflect**:
   - How is this different from manually checking the same thing?
   - What happens when you have 5-10 such skills configured?
   - How does autonomous expertise differ from manual review?

**Success criteria**: Skill configured, tested, and producing suggestions aligned with YOUR context

---

## Best Practices: Strategic Use of Skills

Skills are organizational assets—treat them like code (version control, documentation, team review).

**1. Start with pre-built skills** (Tier 2)
- Pre-built skills are battle-tested by community
- Customizing them leverages community expertise while adapting to YOUR context
- Building custom skills requires more investment (Tier 3, advanced)
- Why this matters: Pre-built 80/20 rule—get 80% of value from configuration alone

**2. Commit skills to version control**
- Store project skills in `.claude/skills/`
- Include in git commits alongside code
- Skills are knowledge; version control them like code
- Why this matters: Institutional memory, team alignment, onboarding

**3. Document trigger conditions clearly**
- Good trigger description = Claude catches 80% of opportunities
- Vague triggers = Claude misses relevant situations
- Spend time on the description (it's the specification that drives discovery)
- Why this matters: Autonomous expertise only works if Claude recognizes when to help

**4. Update skills as standards evolve**
- Security patterns change? Update security skill
- Team adopts new framework? Update relevant skill
- Skills live in version control—update like code
- Why this matters: Keeps automated expertise synchronized with actual standards

**5. Use skills complementarily with subagents**
- Skills: Continuous refinement across all work (ambient expertise)
- Subagents: Focused execution for big, isolated tasks
- Together: Continuous improvement + focused expertise
- Why this matters: Each tool solves different problems; use both

**6. Measure value: Are skills saving time and improving quality?**
- Before configuring skills: How long does manual review take?
- After configuring skills: How much feedback now happens automatically?
- Use metrics to prioritize which skills to configure next
- Why this matters: Justifies time investment in skill configuration/building

---

## 💬 AI Colearning Prompt: Skill Strategy for Your Organization

Time to think strategically about building a skill library.

> **Plan with your AI**: "My team works on [describe your projects/domain: web applications, data pipelines, mobile apps, data science, DevOps infrastructure, etc.]. We want to build a skill library that captures our organizational expertise and applies it autonomously. Suggest a starter set of 5-7 skills we should configure or build. For each skill, provide: (1) Skill name, (2) Expertise it captures, (3) When it should trigger automatically, (4) Business value (time saved, quality improved, consistency enforced, onboarding accelerated, etc.), (5) Whether it's likely pre-built or custom to build."

**Expected outcome**: Strategic skill library plan for your organization, prioritized by business value

---

## Try With AI: Three-Role Skills Mastery

Use Claude Code for these activities (preferred). If you already have another AI companion tool set up (ChatGPT web, Gemini CLI), you may use that—the prompts adapt to any AI tool.

### Prompt 1: Claude as Student (Learning Your Expertise)

Create a custom skill together by teaching Claude what matters to YOUR work.

```
I want to create a custom skill that captures expertise MY team needs. Interview me to understand:
(1) What expertise does this skill capture? (security, performance, style, testing, docs, etc.)
(2) When should it trigger autonomously? (describe situations/file types/patterns)
(3) What should the output look like? (suggestions, checks, improvements?)
(4) How do we validate it's working correctly?

Based on my answers, draft a complete SKILL.md specification for this skill. Include: discoverable description, trigger conditions, instructions, quality criteria, and 2 example outputs.
```

**Expected outcome**: Complete SKILL.md draft based on YOUR expertise
**What you'll learn**: What makes a good skill specification; how detailed specifications enable better AI execution
**Co-learning moment**: You teach Claude what matters in your domain; Claude helps formalize the expertise

### Prompt 2: Claude as Teacher (Suggesting Skill Strategy)

Get strategic guidance on which skills would provide most value.

```
Analyze my current setup and suggest skill strategy. Here's my context:
- Domain/tech stack: [your domain]
- Team size: [developers]
- Current pain points: [what's slow, error-prone, inconsistent?]
- Priority: [speed of delivery / quality / consistency / onboarding / security]

Based on this, recommend the TOP 3 skills I should configure FIRST (from pre-built) and WHY. For each: (1) Skill name, (2) How it solves my pain point, (3) Expected time savings per week, (4) How to measure success.
```

**Expected outcome**: Prioritized skill adoption plan
**What you'll learn**: Strategic thinking about productivity (not just tactics)
**Co-learning moment**: You share domain context; Claude suggests connections you might miss

### Prompt 3: Claude as Co-Worker (Applying Skills to Your Real Work)

Use configured skills to solve actual problems.

```
I'm about to work on: [describe your upcoming task: code review, feature development, API design, refactoring, documentation, etc.]

Which of my configured skills will help with this task? For each applicable skill:
(1) How will it trigger?
(2) What will it check/suggest/provide?
(3) What should I do when it makes suggestions?
(4) How do I know if I'm using it effectively?

Then, let's apply the most relevant skill to this specific task: [paste code, design, doc, etc.]
```

**Expected outcome**: Real task improved by applying configured skills; feedback on skill effectiveness
**What you'll learn**: Integrating skills into actual workflow; evaluating effectiveness
**Co-learning moment**: You validate whether skills work in practice; Claude adapts suggestions based on your feedback

---

## Summary: What You've Learned

You now understand:

1. **Skills as organizational assets**: Teaching Claude your domain expertise once, then applying it autonomously
2. **Tier 2 of Graduated Teaching**: You specify what matters, Claude handles the complexity of applying it everywhere
3. **Specs Are the New Syntax**: Skill specifications capture business value (not just code)
4. **Three-Role Partnership**: Skills demonstrate AI learning from you, then teaching your standards to your team
5. **Strategic advantage**: Custom skills compound over time, creating organizational capabilities competitors can't easily replicate
6. **Practical next step**: Start with pre-built skill configuration (80/20 rule), build custom skills when clear gaps identified

**Progression through Part 2**:
- **Lesson 1**: AI as agentic partner
- **Lesson 2**: Commands for explicit workflows
- **Lesson 3**: Subagents for delegated, isolated tasks
- **Lesson 4**: (previous) Subagents in depth
- **Lesson 5**: (this lesson) Skills for ambient, autonomous expertise
- **Lesson 6 preview**: Hooks extend Claude Code's capabilities
- **Lesson 7 preview**: Plugins compose skills + commands + subagents
