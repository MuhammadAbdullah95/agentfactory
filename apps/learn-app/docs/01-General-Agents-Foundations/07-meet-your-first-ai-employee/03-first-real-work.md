---
sidebar_position: 3
title: "Your First Real Work"
description: "Give your AI Employee real tasks that would normally take 30+ minutes, observe the agent loop in action, and honestly assess what works and what doesn't"
keywords:
  [
    ai employee tasks,
    agent loop,
    task delegation,
    ai productivity,
    token costs,
    multi-step workflows,
    openclaw tasks,
    output quality,
  ]
chapter: 7
lesson: 3
duration_minutes: 30

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Task Delegation"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can formulate clear natural language instructions for 6 different task types (research, writing, file operations, analysis, multi-step workflows, scheduled automation) and observe the agent execute them"

  - name: "Output Quality Assessment"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Critical Thinking"
    measurable_at_this_level: "Student can assess AI Employee output quality, identify what tasks the agent handles well vs poorly, and estimate token costs for different task types"

learning_objectives:
  - objective: "Execute 6 different task types using an AI Employee, observe the agent loop, and experience the shift from reactive to autonomous"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student completes all 6 tasks in the Task Sprint, noting what the agent did at each step and identifying the key difference between Tasks 1-5 (reactive) and Task 6 (autonomous)"

  - objective: "Identify the 4 phases of the agent loop (parse, plan, execute, report) from real observations"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can describe which phase the agent was in during each task and explain how the phases connect"

  - objective: "Assess which tasks AI Employees handle well versus poorly with concrete examples"
    proficiency_level: "A2"
    bloom_level: "Evaluate"
    assessment_method: "Student produces a personal assessment table categorizing at least 6 task types into 'works well' vs 'struggles with' based on firsthand experience"

  - objective: "Estimate token costs for different task types"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can explain why a research task costs more than a simple question and provide rough cost ranges for 3 task categories"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (task delegation, agent loop phases, honest capability assessment, token costs, multi-step workflows, autonomous invocation) grounded in hands-on experience at A2 -- within 5-7 limit"

differentiation:
  extension_for_advanced: "Design a 5-task workflow chain where each task builds on the previous task's output. Time the entire chain and calculate total token cost."
  remedial_for_struggling: "Focus on Tasks 1 and 2 only. For each, write down exactly what the agent did in your own words. Skip cost analysis for now."
---

# Your First Real Work

In Lesson 2, you installed OpenClaw, connected Telegram, and confirmed your AI Employee responds. That proved the wiring works. Now you will make it do something genuinely useful -- tasks that would normally consume 30 or more minutes of your time, finished in 2.

This lesson is about experiencing the **agent loop** -- the execution engine that powers every AI agent system, from chatbots to full AI Employees. You will run five task types that demonstrate this loop in action, then a sixth that crosses the line from "tool you use" to "employee that works for you." The difference between those two categories is the key insight of this lesson.

Every task you run here follows a cycle that appears in every agent system ever built: OpenClaw, Claude Code, Codex CLI, CrewAI, AutoGen. The tools change. The cycle does not. Recognizing it transforms you from someone who uses AI into someone who understands how AI agents work.

## Task Sprint: 6 Tasks in 20 Minutes

Set a timer. You are going to run six tasks back to back, spending about 3 minutes on each. The first five demonstrate the agent loop. The sixth crosses the line into AI Employee territory. For each task, you will do three things: type the instruction, observe what the agent does, and note what you learned.

Open your Telegram chat with your AI Employee. If you configured a different interface in Lesson 2, use that instead.

### Task 1: Research (3 minutes)

**What to type:**

```
Research the top 3 competitors in [your industry]. Create a comparison
table with pricing, features, and target market for each.
```

Replace `[your industry]` with your actual field. If you work in healthcare, say healthcare software. If you work in education, say online education platforms. Use something real to you.

**What to observe:** Watch the agent's response carefully. It does not just blurt out an answer. It plans first -- deciding what information to gather, in what order, and how to structure the output. If your LLM provider supports tool use and web access, you may see it searching for current data. If not, it draws on training knowledge and tells you the cutoff date.

Notice the structure of the output. The agent chose to use a table format because you asked for a comparison. It organized the columns to match your request. It did not ask you to clarify what "competitors" means for your industry -- it made reasonable inferences and proceeded.

**The takeaway:** Multi-step reasoning combined with tool use. The agent decomposed a vague request ("research competitors") into specific subtasks (identify companies, gather pricing, compare features, format as table) without you spelling out each step.

---

### Task 2: Professional Writing (2 minutes)

**What to type:**

```
Draft a professional email declining a meeting invitation.
Tone: respectful but firm. Reason: scheduling conflict.
Keep it under 100 words.
```

**What to observe:** The response arrives almost instantly compared to the research task. Notice how the agent adapts its language to match the tone you specified. It did not use casual language or overly formal legalese. It hit "respectful but firm" because you gave it clear constraints.

Also notice what the agent added that you did not ask for: likely a suggestion to reschedule, or a line acknowledging the importance of the meeting. The agent drew on patterns from professional communication to enhance your request.

**The takeaway:** Domain adaptation through natural language instruction. You did not need to provide a template, select a style preset, or configure anything. Three words -- "respectful but firm" -- were enough for the agent to calibrate its output. This is fundamentally different from traditional software, where you would select from predefined templates.

---

### Task 3: File Operations (3 minutes)

**What to type:**

```
Create a file called weekly-goals.md with 5 professional goals
for this week, formatted as a markdown checklist. Make the goals
realistic for someone in [your role].
```

Replace `[your role]` with your actual job title or function.

**What to observe:** This is where the shift from chatbot to employee becomes concrete. The agent does not just generate text and show it to you. It creates an actual file on your system. Check your OpenClaw working directory -- the file exists. Open it. The content is there.

This is the critical distinction from Lesson 1. A chatbot shows you text. An AI Employee acts on your environment. It created a real file that you can edit, share, and track.

**The takeaway:** The agent acts on your machine. This is not a sandbox or simulation. When you ask for a file, you get a file. When you ask it to modify something, the modification happens. This capability is what makes the "employee" framing accurate -- employees produce artifacts, not just answers.

---

### Task 4: Analysis (3 minutes)

**What to type:**

```
Read weekly-goals.md, analyze which goals are most achievable this
week given typical time constraints, and reorder them by priority
with a brief justification for each ranking.
```

**What to observe:** The agent reads the file it just created. It does not ask you to paste the contents. It remembers the file exists because it created it moments ago (session context), and it can access it directly (file system access).

Watch how it reasons about priority. It considers factors like time required, dependencies between goals, and likelihood of completion. The justifications reveal its reasoning process. You might disagree with some rankings -- that disagreement is valuable data about where your judgment differs from the agent's defaults.

**The takeaway:** Agents can build on previous work. The agent used two forms of memory here: session context (knowing it created the file) and file system access (reading the file contents). This is the foundation of multi-step workflows. Each task can reference and build on what came before.

---

### Task 5: Multi-Step Workflow (4 minutes)

**What to type:**

```
Research the latest trends in [your field] for 2026, summarize
the key findings in a file called trends-report.md, then suggest
3 action items based on those findings that I could implement
this quarter.
```

**What to observe:** This single instruction triggers a chain of operations: research (gathering information), writing (creating a structured summary), file creation (saving to disk), and analysis (generating actionable recommendations). The agent handles the sequencing automatically. You gave one instruction; it executed multiple steps.

Count the distinct operations the agent performed. You likely see at least four: gathering information, synthesizing it into coherent prose, writing it to a file, and generating recommendations based on what it wrote. Each step feeds the next.

**The takeaway:** This is the agent loop at its most capable -- one instruction, multiple coordinated steps, tangible output. Traditional tools require you to perform each step manually: open a browser, search, read articles, open a text editor, write notes, analyze the notes, write recommendations. The agent compressed that entire workflow into a single delegation.

But notice what all five tasks have in common: **you triggered every one of them.** The agent did not decide to research competitors on its own. It did not wake up and create a goals file. It waited for you to speak, then it acted. That is the agent loop -- powerful, but reactive.

The next task changes that.

---

### Task 6: Scheduled Check-In (3 minutes)

**What to type:**

```
Set up a daily morning briefing that runs automatically at 8 AM.
It should: check my recent files for anything modified yesterday,
summarize what I worked on, and suggest 3 priorities for today.
Send me the briefing on Telegram without me asking for it.
```

**What to observe:** This task is fundamentally different from Tasks 1-5. You are not asking for a one-time response. You are asking the agent to **act on a schedule, without being prompted.** If your OpenClaw instance supports cron jobs or heartbeats (check your configuration from Lesson 2), the agent will confirm the schedule. If not, it will explain what configuration is needed.

Either way, notice the shift: Tasks 1-5 were conversations. Task 6 is a **standing order**. The agent is not waiting for you to speak. It is monitoring, summarizing, and reporting on its own schedule.

**The takeaway:** This is the line between an agent loop and an AI Employee. Tasks 1-5 demonstrated the agent loop -- the same parse-plan-execute-report cycle that every agent framework implements. Task 6 adds **autonomous invocation**: the agent acts without being asked. That single addition is what transforms a capable tool into a colleague that works alongside you.

---

## What You Just Witnessed

Stop and reflect on the six tasks you ran. They split cleanly into two categories -- and the split is the most important thing you learned today.

### The Agent Loop (Tasks 1-5)

**Phase 1 -- Parse Intent.** The agent read your natural language instruction and understood what you wanted. It distinguished between "create a file" and "research competitors" without you specifying the tool or approach. It handled ambiguity (like inferring what "competitors" means for your industry) by making reasonable defaults.

**Phase 2 -- Plan Execution.** Before producing output, the agent decided what to do and in what order. For the research task, it identified information categories. For the multi-step workflow, it sequenced research before writing before analysis. You never told it the order. It planned dynamically.

**Phase 3 -- Execute Steps.** The agent called tools -- web search, file creation, file reading -- as needed. Each tool call had a purpose tied to the plan. When the multi-step task required reading a file it had just written, it did so without prompting from you.

**Phase 4 -- Report Results.** The agent formatted its output for you: tables for comparisons, checklists for goals, prose for reports. It chose the format based on context, not a rigid template.

This cycle -- **parse, plan, execute, report** -- is universal. Every agent system implements it. OpenClaw does it. Claude Code does it. AutoGPT, CrewAI, and the OpenAI Agents SDK all implement variations of this same loop. The specific tools, models, and interfaces differ. The pattern is identical.

### The Employee Shift (Task 6)

Task 6 added one thing that Tasks 1-5 lacked: **autonomous invocation**. The agent does not wait for your message. It fires on a schedule, checks your environment, and reports back -- whether you asked or not.

That single addition is what separates an AI Employee from an AI tool. Tasks 1-5 gave you a powerful agent loop -- the same engine that runs inside ChatGPT, Claude Code, and every other AI assistant. Task 6 gave you a glimpse of something different: a colleague that works while you sleep.

In Lesson 4, you will see exactly how both of these patterns work under the hood. In Lesson 5, you will confront the security implications of an agent that acts without being asked.

---

## What Works Well vs What Doesn't

Here is an honest assessment. Not marketing. Not hype. What actually works and what currently falls short, based on real usage patterns.

### Tasks Where AI Employees Excel

| Task Type                      | Why It Works Well                                                        | Example                                                    |
| ------------------------------ | ------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **Research and summarization** | Processes large volumes of information faster than manual reading        | Competitor analysis, trend reports, literature reviews     |
| **Professional writing**       | Adapts tone, format, and structure to natural language constraints       | Emails, proposals, reports, documentation                  |
| **File management**            | Creates, reads, modifies, and organizes files without manual effort      | Goal lists, meeting notes, project templates               |
| **Structured analysis**        | Applies consistent criteria across items without fatigue                 | Priority ranking, pros/cons tables, comparison matrices    |
| **Multi-step workflows**       | Chains operations that would require you to context-switch between tools | Research-to-report pipelines, data-to-recommendation flows |

### Tasks Where AI Employees Struggle

| Task Type                               | Why It Struggles                                                                                            | What to Do Instead                                                                |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Tasks requiring real-time data**      | Training data has a cutoff date; web access varies by provider and configuration                            | Verify recency of any time-sensitive claims; provide current data when needed     |
| **Highly subjective decisions**         | The agent has no access to your personal values, relationships, or organizational politics                  | Use the agent for analysis; make the final judgment yourself                      |
| **Tasks requiring external services**   | Unless you have configured specific integrations (email, calendar, databases), the agent cannot access them | Check Lesson 2's configuration; connect services as needed in later lessons       |
| **Very long, complex workflows**        | Context windows have limits; after thousands of tokens, earlier instructions may lose fidelity              | Break long workflows into smaller steps; check intermediate outputs               |
| **Creative work requiring originality** | Agents produce competent, pattern-based output; genuine novelty requires human insight                      | Use the agent for first drafts and variations; inject your own creative direction |

The honest pattern: AI Employees are strongest at tasks that are **information-heavy, structure-dependent, and repeatable**. They are weakest at tasks that require **real-time awareness, subjective judgment, or genuine creativity**. Most professional work falls somewhere in between, which is exactly why the "employee" model works -- you delegate the mechanical parts and apply your judgment to the parts that matter.

---

## Understanding Costs

Every message to your AI Employee costs tokens. Tokens are the units that LLM providers use for billing -- roughly 4 characters per token in English. The cost depends on two factors: which model you are using and how many tokens the request and response consume.

### Rough Cost Guide (February 2026)

These ranges assume typical API pricing. Free tiers (like Kimi K2.5 or Gemini Flash with free quota) cost nothing until you hit rate limits. Paid usage on mid-tier models (Claude Sonnet, GPT-4o) follows these approximate ranges:

| Task Type                                       | Typical Token Usage  | Approximate Cost (Paid Mid-Tier) |
| ----------------------------------------------- | -------------------- | -------------------------------- |
| Simple question                                 | 200-500 tokens total | $0.005 - $0.02                   |
| Professional email draft                        | 500-1,000 tokens     | $0.01 - $0.05                    |
| Research task with synthesis                    | 2,000-5,000 tokens   | $0.05 - $0.25                    |
| Multi-step workflow                             | 5,000-15,000 tokens  | $0.15 - $0.75                    |
| Extended session (many back-and-forth messages) | 20,000-50,000 tokens | $0.50 - $2.50                    |

**What drives cost up:** Longer responses, multiple tool calls (each call adds tokens), providing large documents as context, and using frontier models (Claude Opus, GPT-5.2) instead of efficient models (Claude Haiku, GPT-5 mini, Gemini Flash).

**What keeps cost down:** Concise prompts, smaller efficient models for routine tasks, free-tier providers for learning, and breaking large requests into focused smaller ones.

### Free Tier Reality

For this chapter, you should be well within free tier limits. Kimi K2.5 provides generous free API access. Gemini Flash has a free quota. Even paid services typically offer initial credits.

If you are working through these six tasks on a free tier, your total cost for this lesson is approximately zero dollars. The rate limits may slow you down between tasks, but you will not be charged.

### The Bigger Cost Picture

The relevant comparison is not "how much does this API call cost" but "how much is my time worth." If you earn the equivalent of $50 per hour and the research task saved you 30 minutes, you gained $25 of value for less than $0.25 in token costs. That is a 100x return. Even at heavy daily usage of $5-10 per day on paid models, the math works if you are genuinely saving hours.

The cost question becomes more nuanced at scale -- running agents for entire teams, processing thousands of requests daily -- but at the individual learning level, cost is rarely the constraint. Time and skill are.

---

## From Loop to Employee

You have now experienced both halves of the AI Employee equation:

**The agent loop** (Tasks 1-5): Parse intent, plan execution, execute steps, report results. This cycle is the heartbeat of every agent system. It is powerful, versatile, and reactive -- it does nothing until you speak.

**Autonomous invocation** (Task 6): The agent acts on its own schedule. It monitors, summarizes, and reports without a prompt from you. This is the capability that transforms a tool into a colleague.

In Lesson 4, you will open the hood and see exactly how OpenClaw implements both patterns -- the agent loop and the scheduling system that makes it fire autonomously. You will learn the six universal patterns that make any AI Employee work.

But before that architecture lesson, carry this experience with you: you delegated real work, received real output, experienced the shift from reactive to autonomous, and formed your own honest assessment of what works and what does not. That firsthand judgment is more reliable than any benchmark or marketing claim.

---

## Try With AI

### Prompt 1 -- Task Quality Assessment

```
I just ran 6 tasks with an AI Employee:
1. Competitor research (comparison table)
2. Professional email draft
3. File creation (weekly goals)
4. Analysis (priority ranking)
5. Multi-step workflow (research + report + recommendations)
6. Scheduled daily briefing

Rank these 6 by: (a) output quality, (b) time saved versus doing it
myself, and (c) how much I'd trust the output without review.

Then identify: which of these 6 should NEVER be fully automated --
where human review is non-negotiable? Explain why.
```

**What you're learning:** Critical assessment of AI output. Knowing which tasks to trust and which to verify is more valuable than knowing how to delegate. The ability to rank by trust level -- not just convenience -- is what separates effective AI Employee managers from people who blindly accept AI output.

### Prompt 2 -- Capability Boundaries

```
What types of tasks are AI Employees currently good at vs bad at?
Create a 2-column comparison table with at least 8 entries in each
column. For each "bad at" entry, explain whether this is a temporary
limitation (will improve) or a fundamental one (requires human judgment).
```

**What you're learning:** Calibrating expectations. Knowing the boundaries prevents frustration and builds realistic plans. The distinction between temporary limitations (will improve with better models and tools) and fundamental ones (require human values, relationships, or creativity) shapes how you invest your learning time.

### Prompt 3 -- Morning Workflow Design

```
Design a morning routine that an AI Employee could run for me every
day. Include: what it checks (email, calendar, news in my field),
what it summarizes, what actions it takes (draft replies, create
task lists), and how it reports to me (Telegram message format).

My role: [YOUR ROLE]
My priorities this quarter: [LIST 2-3 PRIORITIES]
```

**What you're learning:** Thinking in workflows rather than individual tasks. This is the foundation for the always-on employee you will build in Chapter 13. A morning routine combines research, analysis, writing, and scheduling into a single automated sequence -- exactly the multi-step pattern you practiced in Task 5, but running on a schedule instead of on demand.
