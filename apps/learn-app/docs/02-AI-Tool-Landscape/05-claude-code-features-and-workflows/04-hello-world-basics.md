---
title: "Hello World: Mastering the Interface"
sidebar_position: 4
chapter: 5
lesson: 4
duration_minutes: 10

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Command line interface navigation, permission model, basic interaction patterns"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Claude Code CLI Navigation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can execute basic commands (/help, /clear, /compact), understand the permission approval workflow (Read/Write/Run), and interpret cost transparency indicators"

learning_objectives:
  - objective: "Navigate the Claude Code TUI (Terminal User Interface) efficiently"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful execution of slash commands"
  - objective: "Understand and control the Permission Loop (Read vs Write vs Execute)"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Correctly identifying when to approve vs reject a proposed action"
  - objective: "Monitor token usage and cost transparency"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Identification of the 'Cost Pill' and what it measures"
  - objective: "Execute a 'Hello World' workflow from start to finish"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Creation and modification of a simple file using natural language prompts"

# Cognitive load tracking
cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (TUI, Slash Commands, Permission Loop, Cost Pill, Natural Language coding) - within A2 limit"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Explore /compact mode vs /verbose mode differences; experiment with `claude doctor`"
  remedial_for_struggling: "Focus solely on the 'Hello World' file creation task; skip advanced slash commands initially"

# Generation metadata
generated_by: "content-implementer v1.0.0 (04-hello-world-basics)"
source_spec: "specs/04-hello-world-basics/spec.md"
created: "2026-01-16"
version: "1.0.0"

# Legacy compatibility
prerequisites:
  - "Lesson 02 or 03: Claude Code installed and authenticated"
---

# Hello World: Mastering the Interface

You've installed Claude Code. You've authenticated. You're staring at a cursor in your terminal.

Now what?

Before we dive into advanced features like Context Files (Lesson 6) or Skills (Lesson 8), you need to know how to **drive**.

Claude Code isn't just a chatbot in a black box. It's an interactive environment with specific controls, safety checks, and feedback loops. In this lesson, you'll master the dashboard before you drive the car.

---

## The TUI Anatomy (Terminal User Interface)

When you run `claude`, you enter the **TUI**. It looks simple, but it's packed with information.

![claude-code-tui-anatomy](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-2/chapter-05/tui-anatomy-annotated.png)

1.  **Input Field**: Where you type natural language instructions.
2.  **History**: Scroll up to see previous exchanges (just like a normal chat).
3.  **The "Cost Pill"**: A small indicator showing the cost of the *current session*.
4.  **Activity Indicator**: Shows when Claude is "Thinking" vs "Executing".

### The Slash Commands

Just like Discord or Slack, Claude Code uses `/` commands for controlling the tool itself.

Try these right now:

*   **`/help`**: Shows all available commands.
*   **`/clear`**: Clears the screen (but keeps session context).
*   **`/compact`**: Switches to a minimal view (hides detailed thinking/tool outputs). Great once you trust the agent.
*   **`/cost`**: Shows detailed token usage and cost for the session.

#### 💬 AI Colearning Prompt
> "I'm new to terminal interfaces. Explain the difference between typing a natural language command (like 'list files') and a slash command (like '/help'). Who interprets which?"

---

## The Permission Loop: Your Safety Belt

This is the most important concept to understand.

When you ask ChatGPT to write code, it just outputs text.
When you ask Claude Code to write code, it **proposes an action**.

**It cannot act without your permission.**

### The 3 Types of Permissions

1.  **Read Permissions**: "I want to read `src/main.py` to understand the code."
    *   *Risk:* Low. (Unless you have secrets in that file).
2.  **Write Permissions**: "I want to edit `README.md` to add installation steps."
    *   *Risk:* Medium. (It modifies your files).
3.  **Execute Permissions**: "I want to run `npm install`."
    *   *Risk:* High. (It runs code on your machine).

### How to Approve

When Claude proposes an action, you'll see a prompt like this:

```
> Claude wants to run: ls -la
  [Enter] Approve  [Esc] Reject
```

*   **Press Enter**: "Yes, do it."
*   **Press Esc** (or type 'n'): "No, stop."

**Pro Tip:** You can also type instructions *instead* of approving.
*   *Claude:* "I want to delete `database.db`."
*   *You:* "No! Rename it to `database_backup.db` instead."

This is **Steering**. You don't just say yes/no; you guide the agent.

---

## Hands-On: Your "Hello World" Workflow

Let's do a real task to build muscle memory.

### Step 1: Create a Project Directory
(Do this yourself in your terminal, outside Claude if you prefer, or ask Claude to do it).

```bash
mkdir hello-claude
cd hello-claude
claude
```

### Step 2: The Creation Prompt
Type this into Claude:

> "Create a python script named hello.py that prints a greeting and the current date."

**Watch what happens:**
1.  Claude **thinks** (planning).
2.  Claude **proposes** a `Bash` command to create the file.
3.  **YOU** must press `Enter` to approve.
4.  Claude **proposes** a `FileWrite` to add the content.
5.  **YOU** must press `Enter` to approve.

### Step 3: The Execution Prompt
Now type:

> "Run the script."

**Watch:**
1.  Claude proposes running `python hello.py` (or `python3`).
2.  **YOU** press `Enter`.
3.  You see the output in the terminal.

### Step 4: The Iteration Prompt
Now, let's change it.

> "Modify the script to ask for the user's name and greet them personally."

**Watch:**
1.  Claude **reads** the file first (requests permission).
2.  Claude **edits** the file (requests permission).
3.  Claude might **run** it to test (requests permission).

**Congratulations.** You just completed the **Read-Write-Execute Loop**. This is the fundamental heartbeat of agentic development.

---

## The "Cost Pill" and Token Hygiene

Look at the top right (or type `/cost`). You'll see a dollar amount, e.g., `$0.04`.

*   **Input Tokens**: What you typed + the files Claude read. (Cheaper).
*   **Output Tokens**: What Claude wrote. (More expensive).

**Why it matters:**
If you ask Claude to "Read every file in this 10,000 file project," your Input Tokens will explode, and so will the cost.

**Best Practice:** Be specific.
*   ❌ "Fix the bug in my app." (Reads everything).
*   ✅ "Fix the bug in `auth.py`." (Reads one file).

---

## Troubleshooting: Getting Unstuck

Sometimes Claude gets confused or stuck in a loop.

*   **Ctrl+C**: Interrupts Claude immediately. Use this if it's rambling or going down the wrong path.
*   **`/clear`**: Clears the conversation history. Useful if Claude is confused by old context. It resets the "short-term memory."
*   **"Stop and listen"**: Just type this. "Stop. You are looking at the wrong file. Look at X instead." Steering is often faster than restarting.

---

## Try With AI

Now that you know the controls, practice steering.

**🚗 Practice Steering:**
> "Ask Claude to create a file called `joke.txt`. When it asks for permission, **REJECT** it (Esc/No). Then tell it: 'Actually, make it a markdown file called `joke.md`'."
> *Goal: See how Claude adapts to rejection without crashing.*

**💰 Cost Check:**
> "Run `/cost`. Then paste a long article (or ask it to read a large file). Run `/cost` again. Calculate how much that action cost you."
> *Goal: Develop an intuition for token costs.*

---

**Next Up:** Now that you can drive, let's build the "Employee Handbook" so you don't have to explain your project every time. Proceed to **Lesson 6: CLAUDE.md Context Files**.
