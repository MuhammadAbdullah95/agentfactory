---
title: "The Creator's Workflow: How Boris Uses Claude Code"
sidebar_position: 16
chapter: 5
lesson: 16
duration_minutes: 15
estimated_time: "15 mins"
chapter_type: Hybrid
running_example_id: boris-workflow

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration) - Synthesis of all concepts through real-world expert workflow"
layer_1_foundation: "N/A (all foundations established in L01-L15)"
layer_2_collaboration: "Analyzing expert workflow patterns, comparing to personal practice, identifying gaps and improvements"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Synthesizing Claude Code Workflow Patterns"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can analyze an expert workflow, map techniques to concepts learned in chapter, and identify patterns to adopt in their own practice"

learning_objectives:
  - objective: "Recognize how chapter concepts combine in a production-grade workflow"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Mapping Boris's techniques to specific lesson concepts"
  - objective: "Understand the 'plan first, then execute' paradigm as fundamental practice"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of why plan mode improves output quality"
  - objective: "Identify verification loops as critical for high-quality AI output"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Description of verification patterns and their impact on quality"
  - objective: "Apply at least three techniques from the creator's workflow to personal practice"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Hands-on implementation of selected techniques"

# Cognitive load tracking
cognitive_load:
  new_concepts: 3
  assessment: "3 new concepts (parallel session orchestration, verification-first mindset, model selection rationale) - synthesis lesson reviewing previously learned material through new lens"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Implement full parallel session workflow; create verify-app subagent for personal project; analyze additional expert workflows from community"
  remedial_for_struggling: "Focus on Plan Mode and CLAUDE.md team practices first; implement one technique at a time"

# Generation metadata
generated_by: "Claude Opus 4.5"
source_spec: "User request - Boris Cherny workflow lesson"
created: "2026-01-08"
last_modified: "2026-01-08"
git_author: "Claude Code"
workflow: "direct implementation"
version: "1.1.0"
refinement_notes: "v1.1.0 - Removed meta-commentary (Three Roles Framework mention), strengthened Chapter Summary with Digital FTE alignment table"

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Lessons 01-15: Complete Claude Code features"
  - "Understanding of CLAUDE.md, MCP, skills, subagents, hooks, and settings"
---

# The Creator's Workflow: How Boris Uses Claude Code

In January 2026, Boris Cherny—creator and head of Claude Code at Anthropic—shared his day-to-day setup on X. The thread went viral. Developers called it "a watershed moment" and "game-changing."

What made it so impactful wasn't exotic techniques. It was seeing how the features you've learned in this chapter combine into a production workflow that lets one person operate like a small engineering team.

This lesson maps Boris's workflow to everything you've learned—showing you what expert-level Claude Code usage looks like in practice.

---

## The Parallel Sessions Philosophy

:::info Note for Non-Coders
Boris runs 20 sessions because he is managing a massive software product. **You do not need to do this.** Start with one session. The principle here is about *multitasking*—like having three assistants working on different projects—not about typing speed.
:::

Boris doesn't run one Claude Code session. He runs **15-20 concurrent sessions**: 5 numbered tabs in his terminal, 5-10 browser sessions on claude.ai/code, and additional sessions started from his phone each morning.

> "I run 5 Claudes in parallel in my terminal. I number my tabs 1-5, and use system notifications to know when a Claude needs input."
>
> — Boris Cherny, X thread (January 2026)

**What this reveals**: Claude Code isn't a tool you interact with one task at a time. It's a capacity you schedule—like having a team of assistants who can work independently while you review outputs and provide guidance when needed.

**Connection to Chapter Concepts**:
- **Lesson 01 (Origin Story)**: The agentic paradigm means Claude works autonomously. Parallel sessions multiply this agency.
- **Lesson 12 (Subagents)**: Each session is like a subagent with a specific task—research in one, implementation in another, testing in a third.

---

## Plan Mode First (Always)

Boris activates Plan Mode (Shift+Tab twice) for every non-trivial task. He iterates back and forth with Claude until the plan is solid, then switches to auto-accept mode for execution.

> "A good plan is really important!"
>
> — Boris Cherny

**The Pattern**:
1. Start with a goal (e.g., "Add authentication to this project")
2. Enter Plan Mode
3. Discuss and refine until the plan makes sense
4. Switch to auto-accept mode
5. Claude typically one-shots the execution

**Why this works**: When you spend time on planning, you align Claude's understanding with your intent. The investment in planning pays off through faster, more accurate execution. No wasted iterations fixing misunderstandings.

**Connection to Chapter Concepts**:
- **Lesson 12 (Subagents)**: Plan is a built-in subagent that researches your codebase and creates multi-step strategies
- The "one task, one completion" pattern applies—Plan subagent does research, returns a plan, then main Claude executes

---

## CLAUDE.md as Team Infrastructure

Boris's team maintains a shared CLAUDE.md file checked into git. The entire team contributes multiple times per week.

The key practice: **when Claude makes a mistake, document it immediately**.

> "Anytime we see Claude do something incorrectly we add it to the CLAUDE.md, so Claude knows not to do it next time."
>
> — Boris Cherny

They also use GitHub's @.claude tagging feature during code reviews—when a reviewer sees Claude could have done better, they update CLAUDE.md as part of the review process.

**The Result**: Every mistake becomes a rule. The longer the team works together, the smarter Claude becomes at understanding their codebase and conventions.

**Connection to Chapter Concepts**:
- **Lesson 05 (CLAUDE.md)**: You learned to create project context. Boris shows how it evolves into institutional memory for teams.
- Notice the learning loop: Claude makes a mistake → team corrects by updating CLAUDE.md → Claude improves. The team and AI teach each other through the shared context file.

---

## Specialized Subagents for Common Workflows

Boris uses custom subagents for his most common workflows:

| Subagent | Purpose |
|----------|---------|
| `code-simplifier` | Cleans up code after Claude completes implementation |
| `verify-app` | Detailed end-to-end testing instructions |
| `build-validator` | Validates builds before merging |
| `code-architect` | Architecture review for complex changes |
| `oncall-guide` | On-call specific automation |

> "Similar to slash commands, I think of subagents as automating the most common workflows that I do for most PRs."
>
> — Boris Cherny

**The Pattern**: Identify workflows you repeat for every PR. Create a subagent that handles that workflow with specialized instructions.

**Connection to Chapter Concepts**:
- **Lesson 12 (Subagents)**: You learned to create subagents with `/agents`. Boris shows what a mature subagent ecosystem looks like.
- **Lessons 06-08 (Skills)**: Subagents are like skills with their own context and tool access—specialized experts for specific phases of work.

---

## Verification is Everything

This might be the most important insight from Boris's workflow:

> "Probably the most important thing to get great results out of Claude Code: give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result."
>
> — Boris Cherny

**How he implements this**:
- Claude uses the Claude Chrome extension to test UI changes directly
- Opens a browser, tests the interface, iterates until the code works and UX feels good
- Domain-specific verification ranges from simple (running bash commands) to complex (browser or phone simulator testing)

**The Philosophy**: You don't trust AI output—you instrument it. Give Claude tools to check its own work, and quality improves dramatically.

**Connection to Chapter Concepts**:
- **Lesson 9 (MCP Integration**): MCP tools can include verification capabilities—testing endpoints, validating outputs, checking UI state
- **Lesson 14 (Hooks)**: Hooks can trigger automated verification after Claude makes changes

---

## PostToolUse Hooks for Formatting

Boris's team uses a simple but effective hook:

```json
{
  "PostToolUse": {
    "matcher": "Write|Edit",
    "command": "bun run format || true"
  }
}
```

This runs the formatter after every file write or edit. Claude generates well-formatted code 90% of the time, and the hook handles the remaining 10% to prevent CI formatting failures.

**Connection to Chapter Concepts**:
- **Lesson 14 (Hooks)**: You learned the PostToolUse pattern. This is a production example that prevents a common frustration (CI failures due to formatting).

---

## Permissions, Not Skip Permissions

Boris explicitly avoids `--dangerously-skip-permissions`. Instead, he uses `/permissions` to pre-allow commands that are safe in his environment:

- `bun run build:*`
- `bun run test:*`
- `bun run typecheck:*`

These permissions are checked into `.claude/settings.json` and shared with the entire team.

**Why this matters**: Skip permissions trades safety for convenience. Pre-allowed permissions give you the convenience while maintaining the safety boundary—Claude still asks before running unknown commands.

**Connection to Chapter Concepts**:
- **Lesson 13 (Settings Hierarchy)**: Team-shared settings in `.claude/settings.json` ensure consistency across developers.

---

## Model Selection: Opus 4.5 with Thinking

> "I use Opus 4.5 with thinking for everything. It's the best coding model I've ever used, and even though it's bigger & slower than Sonnet, since you have to steer it less and it's better at tool use, it is almost always faster than using a smaller model in the end."
>
> — Boris Cherny

**The Counterintuitive Insight**: A "wrong fast answer" costs more time than a "right slow answer." Opus 4.5 requires less correction and iteration, making total task completion faster despite slower per-response times.

**Connection to Chapter Concepts**:
- **Lesson 13 (Settings)**: Model choice is a settings configuration. Boris optimizes for total iteration time, not token cost or response speed.

---

## Mapping the Complete Workflow

Here's how Boris's techniques map to what you've learned:

| Boris's Technique | Chapter Lesson | Your Takeaway |
|-------------------|----------------|---------------|
| 15-20 parallel sessions | L01 (Origin) + L11 (Subagents) | Think of Claude as capacity to schedule, not a single tool |
| Plan Mode first | L11 (Subagents) | Always plan before executing non-trivial tasks |
| Team CLAUDE.md in git | L04 (CLAUDE.md) | Every mistake becomes a rule; context evolves |
| @.claude PR tagging | L04 (CLAUDE.md) | Code review becomes CLAUDE.md improvement |
| Specialized subagents | L11 (Subagents) | Create subagents for repeated PR workflows |
| Verification loops | L09 (MCP Integration) + L13 (Hooks) | Give Claude tools to verify its own work |
| PostToolUse formatting | L13 (Hooks) | Automate the last 10% that causes CI failures |
| /permissions | L12 (Settings) | Pre-allow safe commands, share with team |
| Opus 4.5 choice | L12 (Settings) | Optimize for total iteration time, not speed |

---

## Operational Takeaways

Looking at Boris's workflow, three principles emerge:

**1. Parallelization Over Optimization**

Multiple simple sessions outperform one overloaded session. Don't try to make one conversation do everything—distribute work across parallel Claude instances.

**2. Plan Mode Discipline**

Planning isn't training wheels. It's the foundation. Boris uses it for every non-trivial task, not just when he's unsure. The investment in alignment pays off in execution quality.

**3. Verification Infrastructure**

Quality comes from feedback loops, not hope. Give Claude ways to check its work—through MCP tools, hooks, subagents, or browser automation. Verification creates the iteration loop that produces excellent results.

---

## Try With AI

Apply what you've learned from the creator's workflow:

**🔍 Analyze Your Current Practice:**

> "Compare my current Claude Code workflow to Boris Cherny's. I've been using [describe your typical usage pattern]. What's the biggest gap between my practice and his? Which of his techniques would have the most impact if I adopted it?"

**🎯 Implement Plan Mode Discipline:**

> "I want to start using Plan Mode consistently. Walk me through the workflow: I'll describe a task I need to complete, you help me create a solid plan before we execute. Let's practice with: [describe a real task you need to complete]."

**🔧 Create a Verification Subagent:**

> "Help me create a verify-app subagent for my project. My project is [describe your project]. What should this subagent check? What tools does it need? Walk me through creating it with /agents and testing it on my codebase."

**🚀 Design Your Parallel Workflow:**

> "I want to experiment with running multiple Claude Code sessions. Help me think through: What tasks should run in parallel? How should I organize and track them? What system notifications should I set up? Start with 3 parallel sessions—what should each one focus on for [describe your current project]?"

