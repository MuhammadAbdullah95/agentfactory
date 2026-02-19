---
sidebar_position: 8
title: "Your Employee's Senses"
sidebar_label: "L08: Employee's Senses"
description: "Build a Python filesystem watcher that monitors a drop folder and creates action files, adding a perception layer that makes your employee proactive instead of reactive."
keywords:
  - Python Watchers
  - File Watcher
  - watchdog library
  - perception layer
  - autonomous agent
  - event-driven
  - proactive AI
  - daemon process
chapter: 13
lesson: 8
duration_minutes: 30
tier: "Silver"

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration) - Building perception components with AI assistance"
layer_1_foundation: "Understanding polling patterns, filesystem events, daemon processes"
layer_2_collaboration: "Using AI to refine watcher scripts and troubleshoot event handling"
layer_3_intelligence: "N/A (pattern extraction comes in L10)"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Filesystem Event Monitoring"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can use the watchdog library to detect file creation events in a specified directory"
  - name: "Action File Generation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can generate markdown action files with YAML frontmatter metadata that trigger downstream processing"
  - name: "Watcher Pattern Design"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can explain the check-process-deposit pattern and identify which data sources benefit from watcher monitoring"
  - name: "Background Process Operation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can run a Python script as a long-lived background process and stop it cleanly"

learning_objectives:
  - objective: "Explain why watchers solve the lazy agent problem and how they bridge the Perception layer to the Reasoning layer"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student describes the reactive-to-proactive transition and identifies where watchers fit in the Perception-Reasoning-Action architecture"
  - objective: "Implement a filesystem watcher using the watchdog library that detects new files in a drop folder"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Working watcher script that prints detection messages when files are added to the monitored directory"
  - objective: "Generate markdown action files with metadata frontmatter that Claude Code can process from /Needs_Action/"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Action files contain valid YAML frontmatter with type, source, detected timestamp, and status fields"
  - objective: "Test the complete watcher pipeline from file drop to action file creation and verify each step produces expected output"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student runs the watcher, drops a test file, and confirms the action file appears with correct metadata"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (reactive vs proactive agents, watcher pattern, watchdog library, event handlers, action file format) - within B1 limit of 7-10 concepts, appropriate for first Silver tier lesson"

differentiation:
  extension_for_advanced: "Add file type filtering (only trigger on .pdf or .csv), implement a simple poll-based Gmail watcher following the Hackathon 0 pattern, add logging with timestamps to a watcher log file"
  remedial_for_struggling: "Focus on getting the watcher running with print statements before adding action file generation; use the exact code provided before making modifications"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 3
  session_title: "Perception Layer - Filesystem Watcher"
  key_points:
    - "Watchers solve the lazy agent problem - without them, your employee only works when you type a command; with them, it notices things on its own"
    - "The watcher pattern separates detection from processing - watchers DETECT and DEPOSIT action files; Claude Code reads /Needs_Action/ and does the reasoning"
    - "File-based communication (markdown in /Needs_Action/) is the bridge between the Perception layer and the Reasoning layer from L00's architecture"
    - "This is the first Silver tier lesson - it marks the transition from human-triggered to event-triggered AI operation"
  misconceptions:
    - "Students think watchers ARE Claude Code - watchers are lightweight Python scripts that TRIGGER Claude Code by writing files to the vault"
    - "Students expect watchers to process files - watchers only DETECT and DEPOSIT; the reasoning happens in Claude Code when it reads /Needs_Action/"
    - "Students think they need complex infrastructure - a 30-line Python script with watchdog is sufficient for personal use"
    - "Students assume the watcher replaces manual triggering - watchers ADD a trigger mechanism; you can still interact with your employee directly"
  discussion_prompts:
    - "The spec shows Gmail, WhatsApp, and File watchers. What other data sources in YOUR work would benefit from a watcher? What would the action file contain?"
    - "Why does the architecture use file-based communication (/Needs_Action/ folder) instead of direct API calls between watchers and Claude Code?"
    - "The watcher runs in an infinite loop. What are the tradeoffs of running it all the time vs starting it only during work hours?"
  teaching_tips:
    - "Have students install watchdog and run the script FIRST before explaining the architecture in depth - early success builds confidence"
    - "Demo the watcher creating a file in /Needs_Action/ and then show Claude Code reading it - the visual connection between perception and reasoning is the aha moment"
    - "The Gmail Watcher is shown as architecture only - direct students to Hackathon 0 for the full implementation; this prevents the lesson from becoming a Gmail API tutorial"
    - "Emphasize that watchdog handles the hard parts (OS-level file events) so students write business logic, not low-level filesystem code"
  assessment_quick_check:
    - "What problem do watchers solve? (The lazy agent problem - without watchers, the employee only works when you type a command)"
    - "What does a watcher create when it detects something, and where does it go? (A markdown action file in /Needs_Action/)"
    - "Name the three parts of the watcher pattern (check for updates, create action file, run loop)"

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-02-19"
version: "1.0.0"
---

# Your Employee's Senses

In Lesson 7, you assembled a complete email assistant -- skills for drafting, subagents for reasoning, Gmail MCP for action. But your employee has a problem: it only works when you type a command. It cannot notice that three urgent emails arrived while you were in a meeting. It cannot detect that a client dropped a contract PDF in your shared folder. It sits idle until you remember to ask.

This is the **lazy agent problem**. Your employee has expertise (skills), judgment (subagents), and access (MCP), but no senses. It is a brilliant worker sitting in a dark room with no windows.

Watchers give your employee eyes and ears. They are lightweight Python scripts that run in the background, monitoring data sources for changes. When something happens -- a new file appears, an email arrives -- the watcher creates an action file that wakes your employee up. This lesson builds your first watcher: a filesystem monitor that detects files dropped into a folder and deposits action files into `/Needs_Action/` for Claude Code to process.

---

## The Perception Gap

Your Bronze tier employee has three layers from the L00 architecture, but one is missing:

| Layer          | Purpose                                               | Bronze Status                          |
| -------------- | ----------------------------------------------------- | -------------------------------------- |
| **Perception** | Detect changes in the world                           | **Missing** -- no way to notice events |
| **Reasoning**  | Analyze and decide (Claude Code + skills + subagents) | Working                                |
| **Action**     | Execute decisions (Gmail MCP + file operations)       | Working                                |

Without Perception, the flow breaks at the start:

```
Event happens → ??? → Reasoning → Action
                 ^
          Nobody told Claude Code
```

Watchers fill that gap. They are the bridge between "something happened in the world" and "Claude Code knows about it":

```
Event happens → Watcher detects → Action file in /Needs_Action/ → Claude Code reasons → Action
```

**The key insight**: Watchers do not process anything. They only **detect** and **deposit**. A watcher that spots a new file does not read the file, analyze it, or decide what to do with it. It writes a brief action file describing what it found, and Claude Code handles the rest.

---

## The Watcher Pattern

Every watcher in the L00 specification follows the same three-method pattern:

| Method                     | Purpose                                    | Output                           |
| -------------------------- | ------------------------------------------ | -------------------------------- |
| `check_for_updates()`      | Poll or listen for changes at the source   | List of new items detected       |
| `create_action_file(item)` | Convert detected item into a markdown file | File written to `/Needs_Action/` |
| `run()`                    | Infinite loop: check, process, sleep       | Continuous background operation  |

This pattern works for any data source:

| Watcher Type   | What It Monitors          | How It Checks                      |
| -------------- | ------------------------- | ---------------------------------- |
| **Filesystem** | Drop folder for new files | Event-based (instant detection)    |
| **Gmail**      | Inbox for new messages    | Poll-based (check every N seconds) |
| **WhatsApp**   | Chat for keywords         | Poll-based via browser automation  |
| **Calendar**   | Upcoming events           | Poll-based (check every N minutes) |

You will build the Filesystem Watcher in this lesson. The Gmail Watcher follows the same pattern but requires Gmail API credentials -- that is a Hackathon deliverable after you have mastered the pattern here.

---

## Building a Filesystem Watcher

The filesystem watcher monitors a "drop folder" on your computer. When you (or any other program) saves a file there, the watcher detects it and creates an action file in `/Needs_Action/`.

### Step 1: Install watchdog

The `watchdog` library provides cross-platform filesystem event monitoring. It handles the operating system details so your code focuses on business logic.

```bash
pip install watchdog
```

**Output:**

```
Successfully installed watchdog-4.0.0
```

If you use `uv` for package management:

```bash
uv pip install watchdog
```

**Output:**

```
Resolved 1 package in 0.5s
Installed 1 package in 0.3s
 + watchdog==4.0.0
```

### Step 2: Create the Drop Folder and Vault Directories

Before writing the watcher, create the directories it needs:

```bash
mkdir -p ~/employee-inbox
mkdir -p ~/ai-vault/Needs_Action
```

**Output:**

```
(no output means success)
```

Verify they exist:

```bash
ls -d ~/employee-inbox ~/ai-vault/Needs_Action
```

**Output:**

```
/Users/yourname/employee-inbox
/Users/yourname/ai-vault/Needs_Action
```

### Step 3: Write the Watcher Script

Create a file called `file_watcher.py` in your project directory:

```python
#!/usr/bin/env python3
"""Filesystem Watcher - monitors drop folder for new files."""

import time
import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configuration
DROP_FOLDER = Path.home() / "employee-inbox"
VAULT_NEEDS_ACTION = Path.home() / "ai-vault" / "Needs_Action"

class InboxHandler(FileSystemEventHandler):
    """Handles file creation events in the drop folder."""

    def on_created(self, event):
        if event.is_directory:
            return

        src = Path(event.src_path)
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Create action file with metadata frontmatter
        action_filename = f"FILE_{src.stem}_{timestamp}.md"
        action_file = VAULT_NEEDS_ACTION / action_filename

        try:
            file_size = src.stat().st_size
        except OSError:
            file_size = 0

        action_file.write_text(
            f"---\n"
            f"type: file_received\n"
            f"source: {src}\n"
            f"detected: {now.isoformat()}\n"
            f"status: pending\n"
            f"---\n\n"
            f"# New File Received\n\n"
            f"- **File**: {src.name}\n"
            f"- **Size**: {file_size} bytes\n"
            f"- **Location**: {src}\n"
            f"- **Detected**: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            f"## Action Required\n\n"
            f"Process this file according to vault rules.\n"
        )
        print(f"[WATCHER] Detected: {src.name} -> Created: {action_filename}")


if __name__ == "__main__":
    # Ensure directories exist
    DROP_FOLDER.mkdir(parents=True, exist_ok=True)
    VAULT_NEEDS_ACTION.mkdir(parents=True, exist_ok=True)

    # Set up the observer
    observer = Observer()
    observer.schedule(InboxHandler(), str(DROP_FOLDER), recursive=False)
    observer.start()

    print(f"[WATCHER] Monitoring: {DROP_FOLDER}")
    print(f"[WATCHER] Action files go to: {VAULT_NEEDS_ACTION}")
    print(f"[WATCHER] Press Ctrl+C to stop")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[WATCHER] Stopping...")
        observer.stop()
    observer.join()
    print("[WATCHER] Stopped.")
```

**What each part does:**

| Component                   | Purpose                                                     |
| --------------------------- | ----------------------------------------------------------- |
| `DROP_FOLDER`               | The directory the watcher monitors -- your "employee inbox" |
| `VAULT_NEEDS_ACTION`        | Where action files are deposited for Claude Code            |
| `InboxHandler`              | Responds to file creation events                            |
| `on_created()`              | Fires when a new file appears in the drop folder            |
| `Observer`                  | The watchdog engine that monitors filesystem events         |
| `observer.schedule()`       | Connects the handler to the folder                          |
| `while True: time.sleep(1)` | Keeps the script alive until you press Ctrl+C               |

### Step 4: Run the Watcher

Open a terminal and start the watcher:

```bash
python file_watcher.py
```

**Output:**

```
[WATCHER] Monitoring: /Users/yourname/employee-inbox
[WATCHER] Action files go to: /Users/yourname/ai-vault/Needs_Action
[WATCHER] Press Ctrl+C to stop
```

The watcher is now running. Leave this terminal open.

### Step 5: Test It

Open a **second terminal** and create a test file in the drop folder:

```bash
echo "Q4 revenue report draft" > ~/employee-inbox/q4-report.txt
```

**Output in the watcher terminal:**

```
[WATCHER] Detected: q4-report.txt -> Created: FILE_q4-report_2026-02-19_10-30-45.md
```

### Step 6: Verify the Action File

Check that the action file was created:

```bash
ls ~/ai-vault/Needs_Action/
```

**Output:**

```
FILE_q4-report_2026-02-19_10-30-45.md
```

Read the action file contents:

```bash
cat ~/ai-vault/Needs_Action/FILE_q4-report_2026-02-19_10-30-45.md
```

**Output:**

```
---
type: file_received
source: /Users/yourname/employee-inbox/q4-report.txt
detected: 2026-02-19T10:30:45.123456
status: pending
---

# New File Received

- **File**: q4-report.txt
- **Size**: 25 bytes
- **Location**: /Users/yourname/employee-inbox/q4-report.txt
- **Detected**: 2026-02-19 10:30:45

## Action Required

Process this file according to vault rules.
```

Your watcher detected the file, extracted metadata, and deposited a structured action file. Claude Code can now read this file and decide what to do with it.

### Step 7: Stop the Watcher

Go back to the watcher terminal and press `Ctrl+C`:

**Output:**

```
[WATCHER] Stopping...
[WATCHER] Stopped.
```

---

## How This Connects to Your Employee

Here is the complete pipeline from file drop to employee action:

```
YOU (or any program)
    │
    ▼ Save file to ~/employee-inbox/
┌──────────────────┐
│  file_watcher.py │  ← Perception Layer (this lesson)
│  Detects new file│
└────────┬─────────┘
         │ Creates action file
         ▼
┌──────────────────┐
│  /Needs_Action/  │  ← File-based communication
│  FILE_*.md       │
└────────┬─────────┘
         │ Claude Code reads
         ▼
┌──────────────────┐
│  Claude Code     │  ← Reasoning Layer (L05-L07)
│  Skills +        │
│  Subagents       │
└────────┬─────────┘
         │ Takes action
         ▼
┌──────────────────┐
│  Gmail MCP       │  ← Action Layer (L06)
│  File operations │
│  Other MCP tools │
└──────────────────┘
```

The watcher is deliberately simple. It does not decide what to do with the file -- that is Claude Code's job. This separation means you can add new watchers (Gmail, calendar, Slack) without changing your reasoning layer. Each watcher follows the same pattern: detect, create action file, deposit in `/Needs_Action/`.

---

## Gmail Watcher Architecture

The Gmail Watcher follows the identical pattern but polls the Gmail API instead of listening for filesystem events:

| Aspect                  | Filesystem Watcher               | Gmail Watcher                              |
| ----------------------- | -------------------------------- | ------------------------------------------ |
| **Detection method**    | Event-based (instant)            | Poll-based (every 60 seconds)              |
| **Library**             | `watchdog`                       | Gmail API via `google-api-python-client`   |
| **What it monitors**    | Drop folder for new files        | Inbox for new messages                     |
| **Action file content** | File metadata (name, size, path) | Email metadata (sender, subject, priority) |
| **Complexity**          | ~30 lines                        | ~80 lines (API auth + pagination)          |

The Gmail Watcher's `check_for_updates()` queries Gmail for unread messages since the last check. When it finds one, `create_action_file()` writes a markdown file like this:

```
---
type: email_received
source: gmail
sender: client@bigcorp.com
subject: Contract renewal timeline
detected: 2026-02-19T10:45:00
status: pending
---

# New Email Detected

- **From**: client@bigcorp.com
- **Subject**: Contract renewal timeline
- **Received**: 2026-02-19 10:45:00
- **Preview**: We need to finalize the renewal by end of month...

## Action Required

Triage this email using inbox-triager subagent and suggest responses.
```

**Building the Gmail Watcher is a Hackathon deliverable** (L14). You already have Gmail MCP configured from L06 and the inbox-triager from L05. The watcher connects them by depositing action files that trigger your existing reasoning pipeline. The pattern you learned in this lesson -- detect, create action file, deposit -- is exactly the same.

---

## Troubleshooting

| Problem                                           | Cause                               | Fix                                                                              |
| ------------------------------------------------- | ----------------------------------- | -------------------------------------------------------------------------------- |
| `ModuleNotFoundError: No module named 'watchdog'` | Library not installed               | Run `pip install watchdog`                                                       |
| Watcher runs but no detection                     | File created before watcher started | Watcher only detects files created AFTER it starts running                       |
| `PermissionError` on action file                  | `/Needs_Action/` directory missing  | Run `mkdir -p ~/ai-vault/Needs_Action`                                           |
| Watcher detects file twice                        | Some editors save temp files first  | Add a filter: `if src.name.startswith('.') or src.name.endswith('.tmp'): return` |
| Watcher stops when terminal closes                | Script runs in foreground           | Lesson 10 covers running watchers as persistent services with PM2                |

---

## Try With AI

**Setup:** Have your `file_watcher.py` running in one terminal and Claude Code open in another.

**Prompt 1: Test the Full Pipeline**

```
I have a file watcher running that deposits action files in ~/ai-vault/Needs_Action/.
I just dropped a file called "invoice-acme-jan.pdf" into ~/employee-inbox/.

Check ~/ai-vault/Needs_Action/ for the action file it created.
Read the action file and tell me:
1. What file was detected?
2. When was it detected?
3. What action would you recommend based on the file name?
```

**What you're learning:** This tests the end-to-end pipeline. Your watcher (Perception) creates the action file, and Claude Code (Reasoning) reads it and decides what to do. Notice how Claude Code recommends actions based on the filename metadata -- this is the reasoning layer working with the perception layer's output.

**Prompt 2: Design a Filtering Watcher**

```
My current file watcher triggers on ALL new files, including temporary files
from my editor (like .swp files and files starting with ._).

Help me modify the InboxHandler.on_created() method to:
1. Ignore files starting with "." or "_"
2. Ignore files ending with .tmp, .swp, or .bak
3. Only trigger on specific extensions: .pdf, .csv, .txt, .md
4. Log ignored files separately from processed files

Show me the updated on_created() method.
```

**What you're learning:** This is iterative refinement of your watcher. You built the basic version; now you are refining it with AI assistance to handle real-world edge cases. The AI suggests filtering patterns you might not have considered, and you decide which filters match your actual workflow.

**Safety Note:** Watchers run as background processes with filesystem access. Only monitor directories you control. Never point a watcher at system directories (`/`, `/etc`, `C:\Windows`). The watcher in this lesson writes files but does not delete or modify anything -- it is read-only on the source and write-only on the action folder.
