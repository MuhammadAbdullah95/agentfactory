---
sidebar_position: 3
chapter: 10
lesson: 3
title: "Persistent Sessions with tmux"
description: "Create terminal sessions that survive disconnections, enable multi-pane workflows, and keep your long-running agent tasks alive"
keywords: ["tmux", "terminal multiplexer", "persistent sessions", "pane splitting", "SSH persistence"]
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "tmux Session Creation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create named tmux sessions and detach/reattach safely"

  - name: "Session Persistence Across Disconnects"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student demonstrates session survival after SSH disconnect"

  - name: "Pane Management and Splitting"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can split windows into panes and navigate between them"

  - name: "Session Configuration and Restoration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can save and restore tmux session layouts"

learning_objectives:
  - objective: "Create and manage persistent tmux sessions that survive SSH disconnections"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates session, starts long-running process, detaches, and verifies process continues after reattach"

  - objective: "Split tmux windows into multiple panes for simultaneous monitoring and editing"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates 3-pane layout with agent logs, code editor, and terminal"

  - objective: "Use named sessions to switch between project contexts"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates multiple named sessions and switches between them"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "tmux session creation and detachment"
    - "Session persistence across SSH disconnects"
    - "Window and pane management"
    - "Splitting panes for simultaneous monitoring"
    - "Named sessions for project context switching"
    - "Session configuration and restoration"
  assessment: "6 concepts (within B1 limit of 7-10) ✓"

teaching_approach: "Hands-on discovery with AI collaboration (Explore → AI Suggests → Iterate → Master)"
modality: "Collaborative Discovery (Explore → AI Suggests → Iterate → Master)"

differentiation:
  extension_for_advanced: "Explore tmux scripting with tmuxinator for complex session automation, or compare tmux vs Zellij (modern Rust-based terminal multiplexer)"
  remedial_for_struggling: "Practice basic detach/attach workflow with a single session before attempting multi-pane layouts. Use tmux list-sessions frequently to verify state."

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-02-08"
version: "1.0.0"
---

# Persistent Sessions with tmux

## Your Agents Run for Hours—What About Your Connection?

In Lessons 1-2, you built a modern terminal environment with smart navigation and fuzzy finding. But there's a critical gap in your workflow: **your terminal dies when you disconnect.**

When you SSH into a server to deploy an AI agent, what happens when:
- Your laptop sleeps?
- Your WiFi drops?
- You close your laptop accidentally?
- The SSH session times out after 2 hours?

**Everything dies.** Your agent stops mid-training. Your long-running data pipeline aborts. Your debug session vanishes.

**tmux** (terminal multiplexer) solves this by creating **persistent sessions** that survive disconnections. Think of it as a screen recorder for your terminal—everything keeps running even when you're not connected. When you reconnect, you pick up exactly where you left off.

For Digital FTE deployment, tmux is non-negotiable. Your agents run for hours or days. Your connection shouldn't be their single point of failure.

---

## Phase 1: Execute - Your First Persistent Session

Let's start with the core workflow: create a session, run something, detach, and reconnect.

### Activity 1.1: Create a Named Session

**Execute**:

```bash
tmux new-session -d -s agent-training
```

**What these flags do**:
- `new-session` = Create a new tmux session
- `-d` = Detach mode (start in background, don't attach immediately)
- `-s agent-training` = Session name (so you can find it later)

**What just happened**: tmux created a background session named `agent-training`. It's running right now, even though you can't see it.

**Verify the session exists**:

```bash
tmux list-sessions
```

**Output**:
```
agent-training: 1 windows (created Fri Feb  8 14:32:15 2026)
```

Your session is alive and waiting.

### Activity 1.2: Attach to Your Session

**Execute**:

```bash
tmux attach-session -t agent-training
```

**What happens**: Your terminal transforms into the tmux session. You'll see a status line at the bottom showing:
- Session name: `agent-training`
- Window number: `0`
- Current time

**You're now inside the persistent session.** Anything you run here keeps running when you detach.

### Activity 1.3: Start a Long-Running Process

**Execute**:

```bash
# Simulate a long-running agent training task
for i in {1..100}; do
  echo "Training iteration $i/100"
  sleep 2
done
```

This simulates a 200-second (3+ minute) training process. In real scenarios, this would be hours of model training or data processing.

**While this runs**, let's test persistence.

### Activity 1.4: Detach Without Killing

**Press**: `Ctrl+b`, then `d` (press Ctrl+b, release, then press `d`)

**What happens**: You detach from the session and return to your normal terminal. The training process **continues running** in the background session.

**Verify it's still running**:

```bash
tmux attach-session -t agent-training
```

You'll see your training loop still printing iterations. It never stopped.

### Activity 1.5: The Ultimate Test—SSH Disconnection

This is where tmux proves its worth.

**Detach from the session**: `Ctrl+b`, then `d`

**Simulate a connection loss** (choose one):

```bash
# Option 1: Kill your SSH connection (if on remote server)
# Just close the terminal window or kill the SSH process

# Option 2: Simulate locally (if practicing on your machine)
# The session persists even if you close and reopen your terminal
```

**Reconnect to your server** (if you disconnected).

**Attach to the session**:

```bash
tmux attach-session -t agent-training
```

**What you see**: Your training loop is still running. It survived the disconnection that would have killed a normal terminal process.

**What You Learned**: tmux sessions are independent of your connection. They run on the server, not your laptop. Disconnect all you want—your work continues.

---

## Phase 2: Three Roles Demonstration—Collaborative tmux Workflow

Now we move from mechanics to intelligent workflow design. This is where AI helps you discover patterns you wouldn't find alone.

### Scenario 1: Discovering Pane Layout Patterns

**What you ask AI**:

```
I'm deploying an AI agent that needs:
1. Main code running in one terminal
2. Live log monitoring in another
3. Database queries in a third

How should I organize this in tmux so I can see everything at once?
```

**What AI teaches you**:

```
For an agent deployment workflow, use a 3-pane layout:

┌─────────────────┬─────────────────┐
│  Main Process   │  Log Monitor    │
│  (agent run)    │  (tail -f)      │
├─────────────────┴─────────────────┤
│  Database/Debug Terminal          │
└───────────────────────────────────┘

Commands to create this:
1. tmux new-session -s agent-deploy
2. Ctrl+b, %  (split vertical)
3. Ctrl+b, o  (switch to other pane)
4. Ctrl+b, "  (split horizontal)
5. Use Ctrl+b, arrow keys to navigate

Benefits:
- See logs without leaving your main terminal
- Debug database issues while agent runs
- Single terminal window for everything
```

**What you learned**: AI taught you a **pane layout pattern** optimized for monitoring. You hadn't considered splitting panes to create a dashboard-like view.

**Key moment**: AI suggested a layout (3-pane monitoring dashboard) that improves your workflow beyond what you imagined.

---

### Scenario 2: Explaining Your SSH Timeout Constraints

Now you reverse roles. You have deployment constraints the AI doesn't know about.

**What you tell AI**:

```
I deploy agents to servers that kill SSH connections after 30 minutes
of inactivity. But my agent training runs for 4 hours. When SSH
disconnects, the training dies.

How do I make training survive SSH timeouts? I've heard tmux can
help, but I need to understand the exact mechanism.
```

**What AI suggests**:

```
tmux solves this because sessions live on the server, not your
laptop. Here's the mechanism:

WITHOUT TMUX:
┌─────────────┐    SSH Connection    ┌─────────────┐
│ Your Laptop │ ◄─────────────────────► │ Server      │
└─────────────┘                      └─────────────┘
SSH breaks → Process receives SIGHUP → Dies

WITH TMUX:
┌─────────────┐    SSH Connection    ┌─────────────┐
│ Your Laptop │ ◄─────────────────────► │ Server      │
└─────────────┘                      └─────────────┘
                                          │
                                          │ tmux server
                                          ▼
                                   ┌─────────────┐
                                   │ Agent Runs  │
                                   │ (detached)  │
                                   └─────────────┘
SSH breaks → tmux session continues → Agent lives
```

**But you clarify**:

```
Good explanation. But my specific constraint is: the server's SSH
daemon kills idle connections after 30 minutes. Does tmux keep the
SSH connection active, or does it survive the connection death?

I think it's the second—tmux runs on the server independent of SSH.
Confirm this understanding so I can explain it to my team.
```

**What AI confirms**:

```
Exactly right. tmux runs on the server side. The SSH connection is
just a "view" into the tmux session. When SSH dies:
1. Your laptop loses the view
2. tmux session continues on the server
3. Process inside tmux keeps running
4. When you reconnect and attach, you see the current state

The SSH timeout is irrelevant to the tmux session's survival.
```

**What AI learned**: AI adapted to **your constraint** (30-minute SSH timeout) and confirmed your understanding. You taught AI that you needed to explain this mechanism to your team, not just use it yourself.

**Key moment**: You corrected AI's assumptions and clarified the exact mechanism you needed to understand.

---

### Scenario 3: Iterating on Session Layout Together

Here's where both of you iterate together, creating something better than either would design alone.

**Iteration 1: Initial layout**

You ask AI: "I need to monitor 3 agents simultaneously. Each has logs, status, and a control terminal. How should I organize this in tmux?"

**AI suggests**: "Create 3 windows (one per agent), each with 3 panes (logs, status, terminal)."

You think: "That works, but switching between windows to compare agents is tedious."

**Iteration 2: You add a constraint**

You ask AI: "Can I see all 3 agents at once? Maybe 9 panes in a grid?"

**AI suggests**: "That's possible but cramped. Each pane would be tiny. Better approach: 3 windows, but use Ctrl+b, w to see all windows at once and switch quickly."

You think: "Better, but I still can't compare logs side-by-side in real-time."

**Iteration 3: Convergence**

Together you arrive at:
```
Window 1: Agent Comparison (3 panes horizontal)
┌──────────┬──────────┬──────────┐
│ Agent 1  │ Agent 2  │ Agent 3  │
│ Logs     │ Logs     │ Logs     │
└──────────┴──────────┴──────────┘

Window 2: Status Dashboard (3 panes horizontal)
┌──────────┬──────────┬──────────┐
│ Agent 1  │ Agent 2  │ Agent 3  │
│ Status   │ Status   │ Status   │
└──────────┴──────────┴──────────┘

Window 3: Control Terminals (3 panes horizontal)
┌──────────┬──────────┬──────────┐
│ Agent 1  │ Agent 2  │ Agent 3  │
│ Terminal │ Terminal │ Terminal │
└──────────┴──────────┴──────────┘
```

**Commands to build this**:

```bash
# Create session with first window (logs)
tmux new-session -s multi-agent

# Split into 3 panes horizontally
Ctrl+b, %
Ctrl+b, %
Ctrl+b, o (to navigate)

# Create second window (status)
Ctrl+b, c (new window)
Ctrl+b, %
Ctrl+b, %

# Create third window (control)
Ctrl+b, c
Ctrl+b, %
Ctrl+b, %
```

**What neither of you had individually**:
- You didn't think of organizing by **function** (logs/status/control) rather than agent
- AI didn't know that **side-by-side comparison** was your priority
- Together, you created a **function-first layout** optimized for comparison

#### 🤝 Practice Exercise

> **Ask your AI**: "I'm monitoring 5 microservices, each with: application logs, nginx access logs, and a Redis monitor. I need to: spot correlated errors across services, see traffic patterns in real-time, and debug Redis issues when they occur. Design a tmux workflow with named windows and pane layouts that optimizes for this workflow. Give me the exact commands to build it."

**Expected Outcome**: You'll discover how to balance information density with usability—seeing everything you need without creating an unusable grid of tiny panes.

**Key moment**: This is Co-Worker convergence—iteration produced a layout optimized for **your specific workflow** (comparison-focused), not just a generic "one pane per agent" solution.

---

## Phase 3: Apply - Multi-Pane Agent Monitoring

Let's build a practical agent monitoring workflow using what you've learned.

### Activity 3.1: Create a 3-Pane Agent Dashboard

**Start a new session**:

```bash
tmux new-session -s agent-dashboard
```

**Split vertically** (left-right):

Press `Ctrl+b`, then `%`

Your terminal splits into two panes side by side.

**Navigate to the right pane**:

Press `Ctrl+b`, then `o`

**Split the right pane horizontally** (top-bottom):

Press `Ctrl+b`, then `"`

You now have a 3-pane layout:
- Left: Full height
- Right-top: Half height
- Right-bottom: Half height

### Activity 3.2: Set Up Each Pane for Specific Tasks

**Left pane (Main agent process)**:

```bash
cd /var/agents/customer-support
python main.py
```

**Right-top pane (Log monitoring)**:

Navigate there: `Ctrl+b`, then `o` (use `o` repeatedly to cycle through panes)

```bash
tail -f /var/agents/customer-support/logs/app.log
```

**Right-bottom pane (System resources)**:

Navigate there: `Ctrl+b`, then `o`

```bash
htop
```

**⚠️ If htop isn't installed**:

```bash
sudo apt update
sudo apt install htop
```

**What you built**: A complete monitoring dashboard where you can:
- See your agent running (left pane)
- Watch logs in real-time (right-top)
- Monitor CPU/memory usage (right-bottom)

All in one terminal window, persisting across disconnections.

### Activity 3.3: Save This Layout for Future Sessions

tmux doesn't save layouts by default, but you can automate session creation with a shell script.

**Create a session script**:

```bash
nano ~/agent-dashboard.sh
```

**Add this content**:

```bash
#!/bin/bash

# Kill existing session if it exists
tmux kill-session -t agent-dashboard 2>/dev/null

# Create new session with specific layout
tmux new-session -d -s agent-dashboard -n Dashboard

# Split vertically
tmux split-window -h -t agent-dashboard:0

# Split right pane horizontally
tmux split-window -v -t agent-dashboard:0.1

# Send commands to each pane
tmux send-keys -t agent-dashboard:0.0 'cd /var/agents/customer-support && python main.py' Enter
tmux send-keys -t agent-dashboard:0.1 'tail -f /var/agents/customer-support/logs/app.log' Enter
tmux send-keys -t agent-dashboard:0.2 'htop' Enter

# Attach to the session
tmux attach-session -t agent-dashboard
```

**Save and exit**: `Ctrl+O`, `Enter`, `Ctrl+X` (nano workflow)

**Make it executable**:

```bash
chmod +x ~/agent-dashboard.sh
```

**Run it anytime**:

```bash
~/agent-dashboard.sh
```

Your complete monitoring dashboard appears instantly—no manual pane splitting or command typing required.

**What You Learned**: Automation transforms tmux from "useful tool" into "one-command workflow." You can create scripts for different projects, agent configurations, or monitoring needs.

---

## Phase 4: Master - Named Sessions for Project Switching

When you work on multiple projects, named sessions become context switchers.

### Activity 4.1: Create Multiple Project Sessions

**Project 1: Voice Learning Agent**:

```bash
tmux new-session -d -s voice-learning -n main
tmux send-keys -t voice-learning:0 'cd ~/projects/voice-learning' Enter
```

**Project 2: Customer Support Agent**:

```bash
tmux new-session -d -s customer-support -n main
tmux send-keys -t customer-support:0 'cd /var/agents/customer-support' Enter
```

**Project 3: Personal Notes**:

```bash
tmux new-session -d -s notes -n main
tmux send-keys -t notes:0 'cd ~/notes && vim' Enter
```

**List all sessions**:

```bash
tmux list-sessions
```

**Output**:
```
customer-support: 1 windows
notes: 1 windows
voice-learning: 1 windows
```

### Activity 4.2: Switch Between Contexts Instantly

**Jump to voice-learning**:

```bash
tmux attach-session -t voice-learning
```

**Detach**: `Ctrl+b`, then `d`

**Jump to customer-support**:

```bash
tmux attach-session -t customer-support
```

Each session maintains its own:
- Working directory
- Command history
- Pane layout
- Running processes

**What You Learned**: Named sessions are **context containers**. Switch sessions = switch projects. Each project's state persists independently.

---

## Understanding: tmux vs Screen vs No Tool

| Feature | tmux | screen | No Tool |
|---------|------|--------|---------|
| **Session persistence** | ✅ Yes | ✅ Yes | ❌ No |
| **Split panes** | ✅ Yes | ✅ Yes (limited) | ❌ No |
| **Vertical split** | ✅ Native | ❌ Manual workarounds | ❌ No |
| **Status bar** | ✅ Customizable | ✅ Basic | ❌ No |
| **Modern maintenance** | ✅ Actively maintained | ⚠️ Minimal updates | N/A |
| **Client-server model** | ✅ Yes | ❌ No | N/A |

**Why tmux wins for modern workflows**:
- Vertical splitting is native (screen requires workarounds)
- Active development with new features
- Better default keybindings and status bar
- Modern configuration options

**When to use screen**: Legacy systems where tmux isn't available and you can't install it.

**When to use nothing**: Quick one-off commands where persistence doesn't matter.

---

## Safety Note

**Killing sessions**: `tmux kill-session -t session-name` permanently destroys a session and all processes within it. Verify you're in the right session before running this.

**Detaching vs. Closing**: When you close your terminal window without detaching (`Ctrl+b`, `d`), tmux attempts to exit gracefully. But explicit detachment is safer—always `Ctrl+b`, `d` before closing windows.

---

## Try With AI

Let's explore advanced tmux workflows for production agent management.

**🏗️ Design Production Workflows**:

```
I deploy agents to 3 servers: production, staging, and development.
Each server runs: web agent, worker agent, and scheduler.

I need a tmux workflow that lets me:
1. Monitor all 9 agents (3 servers × 3 agents each)
2. Quickly switch between server contexts
3. Correlate errors across environments

Design a session structure with named sessions and window layouts.
Give me the exact commands to build this workflow automatically.
```

**What you're learning**: How to scale tmux from single-agent monitoring to multi-environment production management. You'll discover patterns for organizing complexity without overwhelming yourself.

**🔧 Automate Session Recovery**:

```
Sometimes my server reboots and I lose all my tmux sessions.
Can you create a script that:
1. Saves my current tmux session layouts (session names, pane layouts, running commands)
2. Automatically recreates them after a reboot
3. Handles edge cases (processes that need to restart in specific order)

Explain how this works and where I should store the session configuration.
```

**What you're learning**: The difference between tmux's runtime state (lost on reboot) and persistent configuration (saved to files), and how to bridge the gap for production resilience.

**⚡ Optimize for Your Workflow**:

```
I use tmux constantly but I'm slow at navigation. I use:
- Ctrl+b, o to cycle panes (slow when I have 6 panes)
- Ctrl+b, n and Ctrl+b, p to switch windows (can't remember window numbers)
- tmux attach-session -t name (too much typing)

Teach me faster navigation patterns:
1. Direct pane selection without cycling
2. Named windows I can jump to by name
3. Session switching with fewer keystrokes

Give me a cheat sheet of the 10 most useful tmux commands for someone who uses it daily.
```

**What you're learning**: Power-user patterns that transform tmux from "useful" to "essential." Small efficiency gains compound into massive time savings over daily use.
