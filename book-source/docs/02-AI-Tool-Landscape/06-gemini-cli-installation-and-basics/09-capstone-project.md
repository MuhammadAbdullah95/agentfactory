---
sidebar_position: 9
title: Capstone Project — Build Your Personal Learning Ecosystem
cefr_level: A2
proficiency: Beginner
teaching_stage: 4
stage_name: "Spec-Driven Integration"
cognitive_load:
  concepts_count: 0
  a2_compliant: true
  note: "Capstone applies and composes prior knowledge without introducing new concepts"
learning_objectives:
  - id: LO1
    description: "Write clear specifications for learning workflows before implementation (intent, success criteria, constraints)"
    bloom_level: "Create"
    digcomp: "1.3 Managing data, information and digital content"
  - id: LO2
    description: "Validate specifications for completeness and measurability using provided checklist"
    bloom_level: "Analyze"
    digcomp: "1.2 Evaluating data, information and digital content"
  - id: LO3
    description: "Implement personal learning workflow using TOML configuration (Path 1) or MCP integration (Path 2)"
    bloom_level: "Create"
    digcomp: "3.2 Integrating and re-elaborating digital content"
  - id: LO4
    description: "Test workflows and document results using specification success criteria"
    bloom_level: "Evaluate"
    digcomp: "1.2 Evaluating data, information and digital content"
  - id: LO5
    description: "Reflect on how previous lessons (1-8) enabled capstone implementation"
    bloom_level: "Analyze"
    digcomp: "1.3 Managing data, information and digital content"
  - id: LO6
    description: "Design extensions or command libraries for personal learning context reuse"
    bloom_level: "Create"
    digcomp: "3.2 Integrating and re-elaborating digital content"
estimated_time: "45-60 minutes"
generated_by: "content-implementer v1.0.0"
source_spec: "specs/chapter-6/spec.md"
created: "2025-01-17"
last_modified: "2025-01-17"
git_author: "Educational Systems Architect"
workflow: "/sp.implement"
version: "1.0.0"
---

# Capstone Project — Build Your Personal Learning Ecosystem

**Duration**: 45-60 minutes

> **What You're About to Do**
>
> You've learned eight lessons about Gemini CLI:
> - How it works and why it matters (Lessons 1-2)
> - Its tools, memory, and configuration (Lessons 3-5)
> - How to customize it with MCP servers and commands (Lessons 6-8)
>
> Now you'll compose all that knowledge into something real: **your personal learning ecosystem**—a workflow that saves you time and makes your learning more consistent.
>
> But first, you'll do something professional developers do: **write a specification** before building anything. This capstone teaches the most important skill in AI-native development: describing WHAT you want before HOW to build it.

---

## Understanding Specification-First in AI-Native Learning

### Why Specifications Come First

In traditional learning, you might dive straight in: "I'll create a `/study-plan` command." But here's what happens:

- You build something, discover it's missing features
- You add features and break what was working
- You document it afterwards (if at all)
- Next time you try to reuse it, you forget how it works

**With specifications**, you reason through everything before building:

- What exactly does this need to do?
- How will I know it works correctly?
- What constraints matter?
- What can I leave out?

**The result**: Cleaner designs, faster implementation, easier reuse.

### Three Reasons Specs Matter for Your Capstone

**Reason 1: Clarity**
Unclear spec → unclear workflow → frustration when using it later

**Reason 2: Validation**
You write success criteria BEFORE building. Then you validate against those criteria. No guessing if it "works."

**Reason 3: Composition**
Previous lessons taught you PARTS (commands, MCP servers, context files). Your spec describes HOW THOSE PARTS WORK TOGETHER.

---

## Part 1: Understanding Your Capstone Options

### You Have Two Paths

**Both paths create a real, usable learning workflow. Choose based on what interests you.**

#### Path 1: Learning Workflow Automation (30-45 minutes)

**What you'll build**: Custom slash commands that save time on common learning tasks

**Examples**:
- `/study-plan` → Creates weekly learning schedule for any topic
- `/topic-research` → Searches and summarizes a topic
- `/quiz-me` → Generates practice questions

**Technologies**: TOML configuration files only (no programming)

**Skills from previous lessons**: Lessons 1-2 (commands), Lesson 7 (custom commands)

**Complexity**: Beginner-friendly, no coding required

**Time**: 30-45 minutes

#### Path 2: Research Assistant with MCP (45-60 minutes)

**What you'll build**: A workflow that uses MCP servers to automate research tasks

**Examples**:
- Research laptop options and save comparison notes
- Compare online courses and create decision matrix
- Gather information about a topic from multiple web sources

**Technologies**: MCP server installation + Gemini CLI

**Skills from previous lessons**: Lessons 1-2 (basics), Lesson 5 (configuration), Lesson 6 (MCP servers)

**Complexity**: Beginner-friendly, but requires MCP setup

**Time**: 45-60 minutes

### Which Path Should You Choose?

**Choose Path 1 if**:
- You want the fastest capstone (30-45 min)
- You're most comfortable with TOML files
- You have specific learning tasks you repeat often
- You want to master custom commands before MCP

**Choose Path 2 if**:
- You want hands-on MCP integration practice
- You need web research capabilities
- You're interested in how MCP servers work
- You have the full 45-60 minutes available

**You can always do both later.** This capstone counts if you do either one.

---

## Part 2: Writing Your Specification

### Specification Template

Use this template to write YOUR capstone spec. This is the most important part.

```markdown
## My Capstone Specification

### What I Want to Build

[One sentence describing the workflow. Examples:
- "A command that generates weekly study plans for any learning topic"
- "A workflow that researches topic options and creates comparison notes"
]

### Why This Helps My Learning

[One paragraph explaining why this workflow saves you time or improves your learning. Examples:
- "I research topics every week. This automates the research so I can focus on understanding."
- "I struggle to plan study time. This helps me create consistent, structured plans."
]

### Success Criteria

These are how you'll know it works correctly. Make them specific and measurable.

- [ ] Criterion 1 (Write specific: "Generates a plan with daily topics and time estimates")
- [ ] Criterion 2
- [ ] Criterion 3
- [ ] Criterion 4

### Tools I'll Use

**Path 1 (Automation)**:
- Gemini CLI built-in tools: [List which: Custom commands? File operations? Context?]
- Custom commands: [How many? What names?]
- Configuration format: TOML

**Path 2 (Research with MCP)**:
- Gemini CLI built-in tools: [Which basic tools?]
- MCP servers: [Which MCP server? Example: Playwright for web research]
- Configuration: settings.json for MCP setup

### What I Will NOT Include

Keep your capstone simple. What are you deliberately leaving out?

- ❌ [Example: "No programming or coding required"]
- ❌ [Example: "No complex integrations beyond MCP"]
- ❌ [Example: "No deployment or sharing (just personal use)"]

### Time Budget

[How long will you spend? Realistic estimate?]
- Expected duration: 30-45 minutes (Path 1) OR 45-60 minutes (Path 2)
- My actual budget: ___ minutes
```

### Example Specifications (Learn from These)

#### Example Spec 1: Path 1 (Study Plan Automation)

```markdown
## My Capstone Specification

### What I Want to Build

A command called `/study-plan` that takes a topic and time available,
and creates a structured weekly learning schedule.

### Why This Helps My Learning

I spend 15 minutes every week writing out my study plan on paper.
This automates that task so I can start learning faster.
It also ensures consistency—same format every week.

### Success Criteria

- [ ] `/study-plan Python 10` generates a 10-hour weekly plan with daily breakdown
- [ ] Each day has: topic, estimated time, and one practice task
- [ ] Plan is formatted clearly (not just a paragraph)
- [ ] I can run it multiple times for different topics
- [ ] It saves the plan to a file I can refer back to

### Tools I'll Use

- Gemini CLI custom commands (TOML)
- One custom command file: `study-plan.toml`
- Uses {{args}} to accept topic and hours

### What I Will NOT Include

- ❌ No programming beyond TOML configuration
- ❌ No integration with calendar or scheduling tools
- ❌ No tracking my actual progress (just create the plan)

### Time Budget

- Expected: 35 minutes
- My budget: 40 minutes (includes testing)
```

#### Example Spec 2: Path 2 (Research Assistant)

```markdown
## My Capstone Specification

### What I Want to Build

A workflow that uses MCP web research to compare laptop options
and save the comparison as notes.

### Why This Helps My Learning

I'm learning to use MCP servers to gather information.
This practical capstone helps me understand how MCP works
while solving a real problem (choosing a laptop for programming).

### Success Criteria

- [ ] I use MCP Playwright server to research laptop options
- [ ] I research at least 3 laptop options
- [ ] I create a comparison table saved to a file
- [ ] The comparison includes: price, specs, learning value, pros/cons
- [ ] I can repeat this workflow for other research tasks

### Tools I'll Use

- Gemini CLI with Playwright MCP server
- Configuration: Add Playwright to settings.json
- Built-in file operations to save comparison notes

### What I Will NOT Include

- ❌ No custom slash commands (focus on MCP)
- ❌ No complex integrations beyond one MCP server
- ❌ No purchasing decisions (just research and compare)

### Time Budget

- Expected: 50 minutes
- My budget: 60 minutes (includes MCP setup)
```

### Writing Your Spec

**Step 1**: Choose Path 1 or Path 2

**Step 2**: Copy the template above

**Step 3**: Fill in each section thoughtfully
- Spend extra time on "What I Want to Build" — clarity here cascades to everything else
- Make success criteria MEASURABLE (not "works well" but "generates plan with daily breakdown")
- Be realistic about time budget

**Step 4**: Read your spec aloud to yourself
- Does it make sense?
- Would someone else understand exactly what you're building?
- Are success criteria clear enough to validate against?

**Does your spec pass the clarity test?** If yes, move to validation.

---

## Part 3: Validate Your Specification

### Specification Validation Checklist

Before you start building, use this checklist. Each "yes" answer means your spec is ready.

**Clarity Questions**:
- [ ] Can I read your spec and explain your idea to someone else without asking questions?
- [ ] Does it say WHAT you're building, not HOW you're building it?
- [ ] Are success criteria specific enough to test? (Not "works well" but measurable outcomes)
- [ ] Is the scope small enough for 45-60 minutes?

**Completeness Questions**:
- [ ] Did you list which tools you'll use?
- [ ] Did you list what you're NOT including (scope limits)?
- [ ] Did you estimate realistic time budget?
- [ ] Are success criteria testable (can you verify each one)?

**Realism Questions**:
- [ ] Is this workflow something you'll actually use repeatedly?
- [ ] Are you building this to solve a real learning problem?
- [ ] Does this connect to what you learned in Lessons 1-8?
- [ ] Is the time estimate realistic (not optimistic)?

**Count your checkmarks**:
- 10-12 "yes": Spec is excellent, ready to implement
- 7-9 "yes": Spec is good, ready to implement with minor refinements
- <7 "yes": Spec needs clarification before you build

### Common Spec Problems (And How to Fix Them)

**Problem 1: Spec is Too Vague**

❌ Bad: "Create a learning tool"
✅ Good: "Create a `/study-plan` command that generates a 5-day study plan for any topic with daily goals and time estimates"

**Fix**: Add specific examples. "Learning tool" could mean 100 things. Specify the exact workflow.

**Problem 2: Success Criteria Aren't Measurable**

❌ Bad: Success criteria = "it works"
✅ Good: Success criteria = "generates plan with 5 days, each with 3-4 tasks and time estimates"

**Fix**: Replace "works well" with specific outcomes you can test.

**Problem 3: Scope is Too Large**

❌ Bad: "Build a complete AI learning ecosystem" (could take weeks)
✅ Good: "Build one `/study-plan` command" (can finish in 40 minutes)

**Fix**: Reduce scope. What's the MINIMUM viable workflow that solves your problem?

**Problem 4: Not Connected to Previous Lessons**

❌ Bad: "Build something with machine learning" (not covered in Chapter 6)
✅ Good: "Build custom commands using TOML" (covers Lesson 7)

**Fix**: Design your capstone using technologies from Lessons 1-8. Don't introduce new tech here.

---

## Part 4: Implementing Your Capstone

### Path 1: Learning Workflow Automation (Custom Commands)

#### What You'll Create

You'll create 1-3 custom TOML command files that automate learning tasks.

#### Step 1: Design Your Command Structure

**Example Design**:
```
Goal: Automate study planning
Command name: /study-plan
Input: topic (e.g., "Python") and hours (e.g., "10")
Output: 7-day structured plan saved to file
```

**Your Design**:
- Goal: [What problem does your command solve?]
- Command name: [What will students type?]
- Input: [What information does it need?]
- Output: [What does it produce?]

#### Step 2: Create the TOML File

**Location**: `~/.gemini/commands/[your-command].toml`

**Template**:
```toml
description = "Brief description of what this command does"
prompt = """
The actual prompt sent to Gemini.

Use {{args}} to inject what the user types.
Format this prompt to produce consistent, quality output.
"""
```

**Example for Study Plan**:
```toml
description = "Generate a structured weekly study plan for any topic"
prompt = """
I want to learn {{args}}.

Please create a detailed 7-day study plan with:
- One main topic or concept per day
- Estimated time (30-60 minutes per day for beginners)
- Key learning objectives for each day
- One practice task per day
- What to focus on to build understanding

Format as:
DAY 1: [Topic] (~[time] min)
- Objective: ...
- Practice: ...

Make it beginner-friendly and achievable in one week.
"""
```

#### Step 3: Test Your Command

```bash
# Navigate to Gemini CLI
gemini

# List commands
/help

# Test your command
/[your-command-name] "your topic"

# Does output match success criteria from spec?
```

#### Step 4: Iterate and Improve

**If output isn't right**:
1. Check what the prompt is asking for
2. Refine the prompt to be more specific
3. Test again with: `/[your-command-name] "different topic"`
4. Does it work consistently?

**Success when**:
- Command runs without errors ✅
- Output matches your success criteria ✅
- It works consistently with different inputs ✅
- You can use it repeatedly ✅

### Path 2: Research Assistant with MCP (Web Integration)

#### What You'll Create

You'll set up one MCP server (typically Playwright for web research) and create a workflow that uses it.

#### Step 1: Understand Your MCP Workflow

**Example Workflow**:
1. You ask Gemini to research laptop options
2. Gemini uses Playwright MCP to visit tech review sites
3. Gemini gathers information and creates comparison
4. Comparison saves to a file for your reference

#### Step 2: Install and Configure MCP Server

**Installation** (covered in Lesson 6):

```bash
# Navigate to Gemini settings
cd ~/.gemini

# Edit settings.json
# (Use your editor: nano, code, notepad, etc.)
```

**Add Playwright MCP** to `settings.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

**Test it works**:
```bash
gemini
/help
# You should see Playwright tools available
```

#### Step 3: Create Research Workflow

**In Gemini CLI, try this**:

```
Help me research [your research topic].
I need you to:
1. Search for reliable sources
2. Gather key information
3. Create a comparison or summary

Please save the result to a file called [your-topic]-research.md
```

**Example**:
```
Help me research Python learning resources for beginners.
I need you to:
1. Find 3-4 reputable websites with Python courses
2. Gather: course name, cost, difficulty level, what's taught
3. Create a comparison table

Please save to python-courses.md
```

#### Step 4: Test and Validate

**Does your workflow**:
- ✅ Actually use MCP (you see Playwright tools being called)?
- ✅ Produce useful research output?
- ✅ Save files successfully?
- ✅ Give you information you couldn't get without MCP?

**If not, try**:
- Refining your prompt with more specific questions
- Asking Gemini to use MCP explicitly
- Breaking the task into smaller steps

#### Step 5: Create Reusable Workflow

**Once it works**, document your workflow:

```markdown
# My Research Workflow

## Setup Required
- Playwright MCP installed in ~/.gemini/settings.json
- Gemini CLI running

## How to Use
1. Start Gemini: `gemini`
2. Ask: [your-template-prompt]
3. Output saves to [your-folder]/research-notes.md

## Example Usage
[Show exact command you ran]

## What I Learned
[What did you discover about MCP?]
```

---

## Part 5: Testing and Documentation

### Testing Your Implementation

**Path 1 (Commands)**:
```bash
# Test 1: Does the command exist?
gemini
/help
# Look for your command name

# Test 2: Does it run without errors?
/[your-command] "test topic"

# Test 3: Does output match success criteria?
# Review output against each criterion from your spec

# Test 4: Does it work consistently?
/[your-command] "different topic"
/[your-command] "another topic"
# Results should be consistently good
```

**Path 2 (MCP Workflow)**:
```bash
# Test 1: Is MCP installed?
gemini
/help
# Look for Playwright or your MCP server tools

# Test 2: Can you use it?
# Ask Gemini to research something and use MCP

# Test 3: Did it work?
# Check that MCP was actually invoked (you see tool calls)

# Test 4: Is output useful?
# Compare against your success criteria
```

### Validation Against Spec

**For each success criterion from your specification**:

1. **Criterion**: ________________________
2. **How to test**: ________________________
3. **Result**: Pass ☐ | Fail ☐
4. **Evidence**: ________________________

**Example**:

| Criterion | How to Test | Result | Evidence |
|-----------|------------|--------|----------|
| Generates 7-day plan | Run `/study-plan Python` | Pass | Plan included days 1-7 with topics, times, tasks |
| Time estimates included | Check each day | Pass | Each day shows ~45-60 min estimate |
| Beginner-friendly | Read language | Pass | Uses simple language, explains concepts |

### Documentation

**Create a README** for your capstone:

```markdown
# My [Capstone Name]

## What This Does
[Brief description]

## How to Use
[Step-by-step instructions]

## What Success Looks Like
[What you expect when it works]

## What I Learned
[What did you discover about Gemini CLI?]

## What Would I Do Differently?
[What would you improve next time?]
```

---

## Part 6: Reflection (Connect to Lessons 1-8)

### Reflecting on Your Learning

Now that your capstone works, reflect on how you got here:

**Question 1: Which Lessons Made This Possible?**

- Lessons 1-2: [Installation, authentication, basic commands]
  - How did you use this? ___________________________

- Lessons 3-5: [Tools, memory, configuration]
  - How did you use this? ___________________________

- Lessons 6-8: [MCP, commands, extensions]
  - How did you use this? ___________________________

**Question 2: What Stage 1 Knowledge Did You Apply?**

Stage 1 (Lessons 1-2) taught you the **manual foundations**:
- How to install and authenticate
- How to run basic commands
- How Gemini CLI works

**How did this foundation enable your capstone?**
- Could you have built your capstone without understanding basics? Why/why not?

**Question 3: What Stage 2 Knowledge Did You Apply?**

Stage 2 (Lessons 3-5) taught you **specific capabilities**:
- What tools Gemini can use
- How memory and context work
- How to configure Gemini

**Which specific capabilities did you use?**
- Tool 1: ___________________________
- Tool 2: ___________________________

**Question 4: What Stage 3 Knowledge Did You Apply?**

Stage 3 (Lessons 6-8) taught you **customization and composition**:
- How MCP servers extend Gemini
- How custom commands save time
- How extensions bundle everything

**Which customizations did you use?**
- MCP or Commands? ___________________________
- How does this connect to Extensions (Lesson 8)? ___________________________

**Question 5: What Would You Do Differently?**

Looking back on your capstone:
- What worked really well? ___________________________
- What was harder than expected? ___________________________
- What would you improve for v2.0? ___________________________

### Future Ideas (Don't Implement — Just Brainstorm)

**If you had more time**:
- Could you combine Path 1 and Path 2? (Commands + MCP together)
- Could you create an Extension (from Lesson 8) bundling your work?
- Could you share this with a study partner?
- Could you adapt this for a different learning goal?

---

## Complexity Guardrails — Keep It Simple

### What NOT to Include

This capstone is about COMPOSITION, not new technology. Keep it beginner-appropriate:

❌ **Don't add new technologies**:
- No programming (Python, JavaScript, TypeScript)
- No API building or integrations beyond MCP
- No complex software architecture
- No deployment or production systems

❌ **Don't overcomplicate the workflow**:
- Stay within 45-60 minute timeline
- Don't try to solve every related problem
- Focus on ONE main workflow, not five features

❌ **Don't reinvent from scratch**:
- Use TOML (Path 1) or MCP (Path 2) only
- Don't try to extend beyond Gemini CLI's current capabilities
- Don't create new MCP servers from scratch

✅ **DO focus on composition**:
- Taking what Lessons 1-8 taught
- Combining it into a real, usable workflow
- Making something you'll actually use

---

## Try With AI

**Use Gemini CLI for these prompts.** These help you troubleshoot if things don't work perfectly.

### Prompt 1: Refining Your Spec

```
I'm working on a capstone project for learning Gemini CLI.
Here's my specification:

[Paste your spec]

Is this specification clear and complete?
What's missing or unclear?
What success criteria should I add?
```

**Expected outcome**: Gemini helps you strengthen your specification before building.

### Prompt 2: Debugging Your Command (Path 1)

```
I created this custom Gemini CLI command:

[Paste your TOML file]

When I run /[your-command], it produces: [describe what happens]
But I expected: [describe what you wanted]

What's wrong with my TOML file or prompt?
How do I fix it?
```

**Expected outcome**: Specific debugging help for your exact command.

### Prompt 3: Optimizing Your MCP Workflow (Path 2)

```
I'm using Playwright MCP to research [your topic].
My current prompt is:

[Paste your prompt]

The results are: [describe what you got]
I want: [describe what would be better]

How should I refine my prompt to get better MCP research results?
```

**Expected outcome**: Prompt optimization suggestions for better MCP usage.

### Prompt 4: Documenting Your Capstone

```
I just completed a capstone project for Gemini CLI.
Here's what I built:

[Describe your capstone]

Help me write a README.md that explains:
1. What the capstone does
2. How someone else would use it
3. What I learned
4. What I'd improve next time

Show me the README template.
```

**Expected outcome**: Well-structured documentation template for your capstone.

---

## Capstone Success Criteria (Yours + Ours)

### You'll Know It's Successful When

**From Your Specification**:
- [ ] All success criteria from your spec are met
- [ ] Your workflow actually saves you time
- [ ] You'll use this repeatedly

**From Technical Perspective**:
- [ ] Code/configuration has no errors
- [ ] It works consistently
- [ ] You can explain how it works

**From Learning Perspective**:
- [ ] You can identify which Lessons 1-8 enabled this
- [ ] You understand how components compose
- [ ] You could design a v2.0 with improvements

### We'll Know It's Successful When

**Technical completeness**:
- ✅ Specification clearly describes the workflow
- ✅ Implementation matches specification
- ✅ Testing validates all success criteria
- ✅ Documentation enables someone else to understand it

**Learning integration**:
- ✅ Capstone composes knowledge from Lessons 1-8
- ✅ No new technologies introduced
- ✅ Workflow is beginner-appropriate
- ✅ Reflection connects to prior lessons

**Pedagogical value**:
- ✅ Demonstrates spec-driven approach (Stage 4)
- ✅ Shows how components compose (Lessons 6-8)
- ✅ Creates something reusable and practical
- ✅ Student can articulate what they learned

---

## Wrapping Up: From Student to System Designer

### What You've Accomplished

You started Chapter 6 learning how to **use** Gemini CLI.

You're finishing Chapter 6 knowing how to **design** learning workflows.

That's a significant shift:
- **Using**: Typing commands, following instructions
- **Designing**: Writing specifications, composing components, creating reusable tools

### The Bigger Picture

Every section of this capstone followed the same pattern professional developers use:

1. **Specification** (define intent before implementation)
2. **Validation** (ensure design is clear)
3. **Implementation** (build the workflow)
4. **Testing** (verify it works)
5. **Documentation** (enable others to use it)
6. **Reflection** (understand what you learned)

In Chapters 8-13, this pattern becomes your primary workflow. The more you practice it now (even in this small capstone), the more natural it becomes.

### Next Steps After This Capstone

**Immediate**:
- Save your specification and documentation
- Use your workflow repeatedly
- Notice how much time it saves you

**Near-future** (Chapters 7-8):
- Learn more tools for automating work
- Create more workflows like this
- Potentially combine them into Extensions

**Medium-term** (Chapters 9+):
- Learn to orchestrate multiple tools together
- Use specifications to design larger systems
- Become an AI-native developer

---

**You've completed Chapter 6: Gemini CLI Installation and Basics.**

**You're ready for Chapter 7: Understanding the Tool Landscape.**

