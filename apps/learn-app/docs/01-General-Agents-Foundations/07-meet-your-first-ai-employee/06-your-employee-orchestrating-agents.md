---
sidebar_position: 6
title: "Your Employee Delegating to Claude Code"
description: "Connect your AI Employee to Claude Code through tmux, verify real delegation by attaching to live sessions, and understand how you design the orchestration pattern"
keywords:
  [
    ai employee delegation,
    claude code delegation,
    tmux agent orchestration,
    two-tier delegation,
    agent verification,
    openclaw claude code,
    agent factory thesis,
  ]
chapter: 7
lesson: 6
duration_minutes: 25

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Delegation Setup"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can instruct their AI Employee to delegate coding tasks to Claude Code via tmux and verify the delegation by attaching to the session"

  - name: "Delegation Verification"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Evaluate"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can verify whether an AI agent actually performed delegated work (vs hallucinated it) by inspecting tmux sessions and output files"

learning_objectives:
  - objective: "Set up real delegation from an AI Employee to Claude Code using tmux sessions"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student sends a coding task via Telegram, then runs tmux ls and tmux attach to confirm Claude Code is running in a live session"

  - objective: "Verify that an AI agent performed work rather than hallucinated it"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student attaches to a tmux session, observes Claude Code producing files, and checks the output directory for real artifacts"

  - objective: "Explain the two-tier delegation pattern through firsthand experience"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student describes in their own words the chain: human gives intent, employee coordinates, Claude Code executes -- and explains why verification matters"

cognitive_load:
  new_concepts: 4
  concepts_list:
    - "Explicit delegation (you instruct the employee how and when to delegate)"
    - "tmux as infrastructure (background sessions for agent work)"
    - "Verification over trust (attach to sessions, check output files)"
    - "Two-tier delegation (you manage the employee, employee manages Claude Code)"
  assessment: "4 concepts within B1 range (7-10). tmux is introduced as a simple tool, not a deep topic. Every concept is grounded in a hands-on exercise with verifiable output."

differentiation:
  extension_for_advanced: "Set up three parallel tmux sessions running Claude Code on different tasks simultaneously. Monitor all three and document which finished first and why."
  remedial_for_struggling: "Focus on Exercise 1 only. Run tmux ls to confirm the session exists. If it does not, describe what your employee said it would do vs what actually happened."
---

# Your Employee Delegating to Claude Code

In Lesson 5, you taught your employee skills and learned why security matters. Those skills handled focused tasks -- meeting prep, research summaries, progress reports. Your employee did all of that work itself.

Now try something different. You have Claude Code on your machine from Chapter 3. What if your employee could send coding tasks to Claude Code instead of trying to handle them alone?

Delegation does not happen automatically. Your employee will not magically discover Claude Code and start using it. You have to set it up. In this lesson, you are going to connect them -- and then verify the connection is real.

## Connect Your Employee to Claude Code

### Step 1: Make Sure tmux Is Ready

Send this to your AI Employee via Telegram:

```
Check if tmux is installed on this machine. If it is not installed,
install it. Confirm when tmux is ready.
```

tmux lets your employee run terminal sessions in the background. Your employee will use it to run Claude Code while reporting progress back to you on Telegram. You will be able to attach to these sessions from your own terminal and watch the work happen live.

### Step 2: Set the Delegation Rule

```
From now on, when I give you a coding task, do NOT write the code
yourself. Instead:
1. Create a named tmux session
2. Run Claude Code inside that session
3. Have Claude Code do the coding work
4. Report the tmux session name and working directory so I can
   attach and verify

Use Claude Code, not a subagent. Use tmux, not a background process.
```

This is the critical moment. You are not hoping delegation happens. You are instructing it. Your employee now knows: coding work goes to Claude Code, run it in tmux, report the session details back to you.

---

## Exercise 1: Your First Delegated Task

Send this to your employee:

```
Create a tmux session called 'calculator' and use Claude Code inside
it to build a simple Python calculator that can add, subtract,
multiply, and divide. Tell me the tmux session name and working
directory when Claude Code starts.
```

While your employee works, open a terminal on your machine and check:

```bash
tmux ls
```

You should see the `calculator` session listed. Attach to it:

```bash
tmux attach -t calculator
```

You are now watching Claude Code work in real time -- writing files, creating functions, building your calculator. This is real delegation. Detach with `Ctrl+B` then `D` to let it continue working.

When your employee reports the task is done, check the output:

```bash
ls <the-directory-your-employee-reported>
python calculator.py
```

The files exist. The calculator runs. Your employee managed the task, Claude Code wrote the code, and you verified every step.

**If tmux ls shows nothing:** Your employee may have claimed to create the session without actually doing it. This is an important lesson -- AI agents can say they performed work without performing it. That is exactly why verification matters. Go back to Step 2 and reinforce: "Use the actual tmux command to create the session. I will be checking with tmux ls."

### Exercise 2: A Tool for Your Work

Now make it relevant to YOUR role:

```
Use Claude Code in a tmux session called 'my-tool' to build a
Python script that [CHOOSE ONE]:
- Reads a CSV file and creates a summary with totals and averages
- Organizes files in a folder by type (documents, images, code)
- Converts my markdown notes into a clean HTML page with styling
Report the session name and directory.
```

Verify again:

```bash
tmux attach -t my-tool
```

Watch Claude Code build something useful for you. When it finishes, test the output with your actual files.

### Exercise 3: Research Then Build

This one combines what your employee does well with what Claude Code does well:

```
Research the best way to automate [A REPETITIVE TASK FROM YOUR WORK].
Summarize your research and explain your approach. Then use Claude Code
in a tmux session called 'automate' to build a working prototype.
Give me the research summary first, then the session name and directory.
```

Notice the workflow. Your employee researches using its own tools and knowledge from MEMORY.md. It decides on an approach. Then it hands the coding to Claude Code. Two different capabilities, one result.

---

## What Just Happened

You built a real delegation chain:

| Layer                        | Who         | What They Did                                     |
| ---------------------------- | ----------- | ------------------------------------------------- |
| **You**                      | Manager     | Gave high-level instructions                      |
| **Your Employee** (OpenClaw) | Coordinator | Interpreted intent, managed tmux, reported status |
| **Claude Code**              | Coder       | Wrote the actual code in a verifiable session     |

This is the **two-tier delegation pattern** from Chapter 1 -- but now you have seen it work. Not a claim in a textbook. You attached to the tmux session and watched Claude Code writing code.

The key insight: **you designed the pattern**. Delegation did not happen by magic. You told your employee when to delegate, what tool to use, and how to report back. In the Agent Factory, the human designs the orchestration. The employee executes it.

Compare this to Chapter 3, where you used Claude Code directly. You typed the instructions. You watched the output. You decided what to do next. Now your employee handles all of that coordination. You just say what you want built.

---

## What Transfers

| Concept                     | What You Experienced                                                     |
| --------------------------- | ------------------------------------------------------------------------ |
| Explicit delegation         | You instructed your employee when and how to delegate                    |
| tmux as infrastructure      | Background sessions let agents work while you verify                     |
| Verification over trust     | Attaching to sessions proves work is real, not hallucinated              |
| Context stays with employee | Research and intent lived with your employee, coding went to Claude Code |
| You are the architect       | The delegation pattern exists because you designed it                    |

---

## Try With AI

### Prompt 1: Parallel Delegation

```
I need two things built at the same time. Create two tmux sessions
and use Claude Code in each one simultaneously:
1. Session 'project-a': A script that [TASK FOR YOUR WORK]
2. Session 'project-b': A script that [DIFFERENT TASK]
Report both session names so I can watch them in parallel.
```

**What you're learning:** Parallel delegation. Your employee manages multiple Claude Code sessions at once. Run `tmux ls` to see both sessions, and attach to each one to watch the work happen simultaneously.

### Prompt 2: Fix and Iterate

```
The tool from Exercise 2 needs a change: [YOUR SPECIFIC FEEDBACK].
Use Claude Code in the same 'my-tool' tmux session to fix it.
```

**What you're learning:** Iteration through delegation. You give feedback to your employee, your employee relays it to Claude Code. Same pattern from every lesson -- but now with a coding agent in the loop.

### Prompt 3: Explain the Chain

```
Describe in plain language what just happened across these exercises.
Who did what? Where did the code come from? Why did I tell you to
use tmux instead of just writing code yourself?
```

**What you're learning:** Getting your employee to articulate the delegation pattern back to you. If it can explain the chain accurately, you have built a shared understanding of how work flows through your system.
