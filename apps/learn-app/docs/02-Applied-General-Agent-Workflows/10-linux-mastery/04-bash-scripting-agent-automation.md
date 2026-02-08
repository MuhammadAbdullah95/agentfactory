---
sidebar_position: 4
chapter: 10
lesson: 4
title: "Bash Scripting for Agent Automation"
description: "Automate agent setup, execution, and maintenance with executable bash scripts that chain commands, handle errors, and run on schedules"
keywords: ["bash scripting", "shell scripts", "automation", "error handling", "cron jobs", "text processing"]
duration_minutes: 75

# HIDDEN SKILLS METADATA
skills:
  - name: "Executable Script Creation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create executable .sh scripts with shebang and permissions"

  - name: "Bash Variables and Interpolation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can use variables, string interpolation, and command substitution"

  - name: "Error Handling and Exit Codes"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can implement error handling with set -euo pipefail and conditional checks"

  - name: "Text Processing with grep/sed/awk"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can parse logs using grep, sed, and awk"

  - name: "Command Chaining with Pipes"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can chain commands using pipes (|) and redirection (>, >>)"

learning_objectives:
  - objective: "Write executable bash scripts that automate agent setup, execution, and maintenance"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student writes script that installs deps, configures agent, starts service with error handling"

  - objective: "Use grep, sed, and awk for log parsing and text processing"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student extracts specific data patterns from log files without manual scrolling"

  - objective: "Implement error handling and conditional logic in scripts"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student adds set -euo pipefail, if/else checks, and meaningful error messages"

cognitive_load:
  new_concepts: 8
  concepts_list:
    - "Shebang and executable permissions (chmod +x)"
    - "Bash variables and string interpolation"
    - "Command substitution $(command)"
    - "Exit codes and error handling"
    - "Conditional statements (if/else)"
    - "Loops (for, while)"
    - "Functions with parameters"
    - "Pipes and redirection (|, >, >>)"
  assessment: "8 concepts (within B1 limit of 7-10) ✓"

differentiation:
  extension_for_advanced: "Create bash functions with parameter validation, implement logging with timestamps, design scripts that generate systemd service files automatically, explore advanced awk patterns for multi-field log parsing."
  remedial_for_struggling: "Focus on single-command scripts first (#!/bin/bash with one line), practice variable assignment and echo output, use prepared templates for error handling patterns, work with grep only before adding sed/awk complexity."

teaching_approach: "Collaborative debugging with AI (Write → Fail → AI Helps → Fix → Understand)"
modality: "Collaborative Debugging"

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-02-08"
version: "1.0.0"
---

# Bash Scripting for Agent Automation

## Automation is Core to the Digital FTE Concept

In Lesson 1, you discovered where your agents live—on Linux servers accessed through the command line. In Lesson 2, you personalized your terminal environment with smart navigation and fuzzy finding. Now it's time to make your agent deployments **repeatable and reliable**.

Every time you deploy a Digital FTE, you perform the same sequence:
- Install dependencies (Python packages, system libraries)
- Configure the agent (environment variables, config files)
- Start the service (systemd, Docker, or direct execution)
- Verify it's running (check logs, test endpoints)

**Doing this manually once is manageable. Doing it ten times is tedious. Doing it a hundred times across multiple servers? That's where automation becomes non-negotiable.**

Bash scripting is your automation foundation. Scripts capture your deployment knowledge as executable, testable, versionable code. When you script your deployment, you can:
- **Reproduce** exact deployments across servers
- **Test** deployment procedures safely
- **Debug** failures by reading script logic
- **Iterate** on deployment process through code

This lesson teaches you to write bash scripts that automate agent deployment, monitoring, and maintenance. You'll learn to chain commands, handle errors gracefully, process logs with text tools, and create scripts that run on schedules.

**By the end**, you'll have:
- A deploy script that sets up agents from scratch
- Error handling that prevents silent failures
- Log parsing skills that extract insights from agent output
- The foundation for cron jobs that automate maintenance tasks

---

## Part 1: Script Foundations - Making Commands Executable

### Your First Script: The Deployment Pattern

Every automation starts with identifying repeated command sequences. Let's capture the FastAPI agent deployment pattern from previous lessons.

**Create your first script:**

```bash
cat > deploy-agent.sh << 'EOF'
#!/bin/bash

echo "Starting agent deployment..."

# Update package lists
sudo apt update

# Install Python and pip
sudo apt install -y python3 python3-pip

# Install FastAPI and Uvicorn
pip3 install fastapi uvicorn

# Create agent directory
mkdir -p /var/agents/customer-support

# Start the agent
cd /var/agents/customer-support
uvicorn main:app --host 0.0.0.0 --port 8000 &

echo "Agent deployed and started!"
EOF
```

**What's happening:**
- `#!/bin/bash` = Shebang line (tells system this is a bash script)
- `<< 'EOF'` = Here document (writes multi-line content to file)
- Lines between `EOF` markers become script content
- `&` at the end = Run command in background

**Make it executable:**

```bash
chmod +x deploy-agent.sh
```

**Execute your script:**

```bash
./deploy-agent.sh
```

**Output:**
```
Starting agent deployment...
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
...
Reading package lists... Done
The following NEW packages will be installed:
  python3 python3-pip
...
Successfully installed fastapi-0.104.1 uvicorn-0.24.0
Starting agent deployment...
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
Agent deployed and started!
```

**What you learned:**
- Scripts are text files with executable permissions (`chmod +x`)
- Shebang (`#!/bin/bash`) specifies the interpreter
- `./scriptname.sh` executes scripts in current directory
- Scripts sequence commands exactly as you'd type them

### Variables: Making Scripts Flexible

Hard-coded paths break when you deploy to different locations. Variables make scripts adaptable.

**Create a parameterized deployment script:**

```bash
cat > deploy-agent-v2.sh << 'EOF'
#!/bin/bash

# Configuration variables
AGENT_NAME="customer-support"
AGENT_DIR="/var/agents/${AGENT_NAME}"
PORT=8000

echo "Deploying ${AGENT_NAME} to ${AGENT_DIR}..."

# Create agent directory
mkdir -p "${AGENT_DIR}"

# Change to agent directory
cd "${AGENT_DIR}"

echo "Starting ${AGENT_NAME} on port ${PORT}..."
uvicorn main:app --host 0.0.0.0 --port "${PORT}" &

echo "Deployment complete!"
EOF
```

**Make executable and run:**

```bash
chmod +x deploy-agent-v2.sh
./deploy-agent-v2.sh
```

**What's happening:**
- `VARIABLE="value"` = Assigns value to variable
- `${VARIABLE}` = Expands variable to its value
- `${AGENT_NAME}` inside string becomes `customer-support`
- Quotes preserve spaces in paths: `"/var/agents/${AGENT_NAME}"`

**Deploy a different agent without editing the script:**

```bash
AGENT_NAME="sales-bot" PORT=8001 ./deploy-agent-v2.sh
```

This sets variables **just for this execution**. The script uses your values instead of defaults.

### Command Substitution: Capturing Output

Sometimes you need to use the output of one command as input to another.

**Script that checks if agent is already running:**

```bash
cat > check-agent.sh << 'EOF'
#!/bin/bash

AGENT_NAME="customer-support"

# Find process ID (pgrep returns matching process IDs)
PID=$(pgrep -f "uvicorn.*${AGENT_NAME}")

if [ -n "$PID" ]; then
    echo "Agent ${AGENT_NAME} is running (PID: ${PID})"
else
    echo "Agent ${AGENT_NAME} is not running"
fi
EOF
```

**Execute:**

```bash
chmod +x check-agent.sh
./check-agent.sh
```

**Output:**
```
Agent customer-support is running (PID: 12345)
```

**What's happening:**
- `PID=$(command)` = Runs command, captures output in variable
- `pgrep -f "pattern"` = Finds processes matching command pattern
- `[ -n "$PID" ]` = Tests if variable is non-empty
- `if/else/fi` = Conditional execution

---

## Part 2: Error Handling - Making Scripts Reliable

Scripts that fail silently are dangerous. A deployment that **looks** successful but didn't actually work wastes debugging time.

### The Problem: Silent Failures

**Run this broken script:**

```bash
cat > broken-deploy.sh << 'EOF'
#!/bin/bash

cd /nonexistent/directory
echo "This line never executes if cd fails"
pip3 install nonexistent-package
echo "This also never executes if install fails"
EOF
```

**Execute:**

```bash
chmod +x broken-deploy.sh
./broken-deploy.sh
```

**Output:**
```
: No such file or directory
This line never executes if cd fails
WARNING: Package(s) not found: nonexistent-package
This also never executes if pip install fails
```

**The problem:** The script continues after `cd` fails and `pip install` fails. Errors are ignored. This is **dangerous** for deployments.

### Solution 1: Exit on Error

**Add error handling to your deployment script:**

```bash
cat > safe-deploy.sh << 'EOF'
#!/bin/bash

# Exit immediately if any command fails
set -e

# Treat unset variables as errors
set -u

# Exit if any command in a pipe fails
set -o pipefail

echo "Starting safe deployment..."

# This will cause the script to exit immediately
cd /nonexistent/directory || true

echo "This line never executes because cd failed (without '|| true')"
EOF
```

**Execute:**

```bash
chmod +x safe-deploy.sh
./safe-deploy.sh
```

**Output:**
```
Starting safe deployment...
safe-deploy.sh: line 9: cd: /nonexistent/directory: No such file or directory
```

**Script exits immediately** at the `cd` failure. Later commands never run.

**What you learned:**
- `set -e` = Exit on any error (non-zero exit code)
- `set -u` = Exit on undefined variable
- `set -o pipefail` = Exit if any command in pipe fails
- `|| true` = Prevents exit on this specific command (continue despite error)

### Solution 2: Meaningful Error Messages

**Script with custom error handling:**

```bash
cat > deploy-with-errors.sh << 'EOF'
#!/bin/bash

set -euo pipefail

# Function to handle errors
error_exit() {
    echo "ERROR: $1" >&2
    exit 1
}

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    error_exit "This script must be run as root (use sudo)"
fi

echo "Deploying agent with error handling..."

# Create directory or fail with clear message
mkdir -p /var/agents/customer-support || error_exit "Failed to create agent directory"

# Install dependencies
pip3 install fastapi uvicorn || error_exit "Failed to install dependencies"

echo "Deployment successful!"
EOF
```

**Execute without sudo:**

```bash
chmod +x deploy-with-errors.sh
./deploy-with-errors.sh
```

**Output:**
```
ERROR: This script must be run as root (use sudo)
```

**Execute with sudo:**

```bash
sudo ./deploy-with-errors.sh
```

**Output:**
```
Deploying agent with error handling...
Deployment successful!
```

**What you learned:**
- Define functions with `name() { commands; }`
- `>&2` redirects output to stderr (error stream)
- `exit 1` exits with error code (1 = failure)
- `[ "$EUID" -ne 0 ]` checks if not root user
- `||` chains commands: run second if first fails

---

## Part 3: Three Roles - Collaborating with AI on Script Design

Now let's experience how AI collaboration improves your scripts through bidirectional learning.

### AI as Teacher: Learning Production Error Patterns

**Your initial script works for development, but you're unsure about production considerations.**

**Ask AI:**

```
I wrote this bash deployment script that installs dependencies and starts a FastAPI agent. It works locally but I'm deploying to production servers. What error handling patterns am I missing that production scripts require?

Here's my current script:
[show your deploy-agent.sh script]
```

**AI might respond:**

```
Your script is missing several production-critical patterns:

1. **Idempotency**: Your script fails if run twice because the directory already exists.
   Fix: Use `mkdir -p` which is safe on existing directories

2. **Port collision**: You hard-code port 8000. If another agent uses it, deployment fails.
   Fix: Check if port is in use before starting: `lsof -i :8000 || uvicorn ...`

3. **Background process management**: Using `&` leaves zombie processes on exit.
   Fix: Use systemd services or nohup properly

4. **Dependency pinning**: `pip3 install fastapi` installs latest version, which might break.
   Fix: Pin versions: `pip3 install fastapi==0.104.1 uvicorn==0.24.0`

5. **Logging**: You have no deployment logs for troubleshooting.
   Fix: Redirect output: `exec > >(tee -a deploy.log) 2>&1`

Here's the production-ready version:
[shows improved script]
```

**What emerged from this interaction:**
- You learned about **idempotency**—scripts should be safe to run multiple times
- You discovered **dependency pinning** prevents version breakage
- AI taught **systemd services** as the production pattern (not `&` backgrounding)
- Neither you nor AI alone had the complete picture—conversation produced better solution

**What you can now do:**
- Apply idempotency patterns to all future scripts
- Pin dependency versions in deployment scripts
- Use systemd for production services (lesson coming)

### AI as Student: Teaching Domain-Specific Constraints

Now reverse roles. You know deployment constraints that AI doesn't.

**Tell AI your constraints:**

```
I'm deploying agents to servers with these constraints:
- Python 3.8 only (newer versions unavailable)
- No internet access during deployment (air-gapped environment)
- Agents must run as non-root user 'agentuser' for security
- Logs must go to /var/log/agents/, not stdout
- Configuration files in /etc/agents/ are read-only after deployment

Adapt your deployment script for these constraints. Explain what changes you made and why.
```

**AI's initial suggestion** might be generic:
```
#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
useradd agentuser
...
```

**Your correction (teaching AI):**

```
Good start, but you missed my constraints:

1. I specified Python 3.8 only, but you didn't check the version
   Add: `python3.8 --version || error "Python 3.8 required"`

2. I said air-gapped, but you're using `pip install` which requires internet
   Change: Copy wheels from local repo or use offline requirements.txt

3. You create user but don't set up the /etc/agents/ permissions
   Add: `chmod 644 /etc/agents/config.yml` after writing config

4. Logging path I specified isn't in your systemd service file
   Add: `StandardOutput=file:/var/log/agents/agent.log`

Revise the script with these corrections.
```

**AI's adapted response:**

```
You're right—I missed several critical constraints. Here's the revised script that respects your environment:

[shows script with version checks, offline installation, proper permissions]

What changed based on your feedback:
- Added Python version verification before proceeding
- Changed pip install to use local --no-index with --find-links
- Set immutable file attributes (chattr +i) on read-only configs
- Created log directory with correct ownership before starting
```

**What emerged from this interaction:**
- AI learned your **air-gapped environment** constraint
- AI adapted to your **security requirements** (non-root execution)
- You refined AI's understanding of **read-only configuration** needs
- Final script respects all constraints—better than either of you alone

### AI as Co-Worker: Iterative Script Refinement

Here's where you and AI iterate together toward an optimal solution.

**Iteration 1: Your starting point**

You show AI your working script:

```bash
#!/bin/bash
set -e

AGENT_DIR="/var/agents/customer-support"
mkdir -p "$AGENT_DIR"
cd "$AGENT_DIR"
pip3 install -r requirements.txt
uvicorn main:app --port 8000 &
```

**You say:** "This works but I want to add logging, health checks, and make it restartable."

**AI suggests:** "Use systemd for all three—it handles logging, health checks, and automatic restarts."

**You think:** "That's good but I'm not ready for systemd yet (that's the next lesson). I want bash improvements first."

**Iteration 2: You add constraints**

You respond to AI: "Let's stay in bash for now. Add:"
- Log file rotation (prevent disk filling)
- Health check endpoint before declaring success
- Kill existing process if already running (restartable)

**AI responds:**

```bash
#!/bin/bash
set -euo pipefail

AGENT_NAME="customer-support"
AGENT_DIR="/var/agents/${AGENT_NAME}"
LOG_FILE="/var/log/agents/${AGENT_NAME}.log"
MAX_LOG_SIZE=100M

# Function to rotate logs
rotate_logs() {
    if [ -f "$LOG_FILE" ] && [ $(stat -f%z "$LOG_FILE") -gt $((100*1024*1024)) ]; then
        mv "$LOG_FILE" "${LOG_FILE}.old"
    fi
}

# Kill existing process if running
pkill -f "uvicorn.*${AGENT_NAME}" || true

# Create directories
mkdir -p "$AGENT_DIR" "/var/log/agents"

# Rotate logs before starting
rotate_logs

# Start agent with logging
cd "$AGENT_DIR"
nohup uvicorn main:app --port 8000 >> "$LOG_FILE" 2>&1 &

# Health check
sleep 3
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo "Agent deployed and healthy!"
else
    echo "ERROR: Agent failed health check" >&2
    exit 1
fi
```

**You review and think:** "Health check is good, but I want retry logic—network might be flaky on first boot."

**Iteration 3: Convergence**

You respond: "Add retry logic for health checks. Try 5 times with 2-second delays before failing."

**AI adapts:**

```bash
# Health check with retries
health_check() {
    local max_attempts=5
    local attempt=1

    while [ $attempt -le $max_attempts ]; do
        if curl -f http://localhost:8000/health > /dev/null 2>&1; then
            echo "Health check passed (attempt ${attempt}/${max_attempts})"
            return 0
        fi
        echo "Health check failed, retrying in 2s..."
        sleep 2
        ((attempt++))
    done

    echo "ERROR: Agent failed health check after ${max_attempts} attempts" >&2
    return 1
}

# Call health check
if health_check; then
    echo "Agent deployed and healthy!"
else
    exit 1
fi
```

**What neither of you had initially:**
- You didn't think of **health check functions** (AI contributed this)
- AI didn't know you wanted **retry logic** (you contributed this)
- Together, you created a **production-ready deployment pattern** with:
  - Idempotent restart (kill existing process)
  - Log rotation (prevent disk filling)
  - Resilient health checks (retry on failure)
  - Clear error messages with attempt counts

**This pattern is now reusable** across all your agent deployments. Future scripts will use this `health_check` function and log rotation pattern.

---

## Part 4: Text Processing - Parsing Agent Logs

Agents generate logs. Lots of logs. Your automation scripts need to extract insights from log files without manual scrolling.

### grep: Finding Patterns

**Sample agent log:**

```bash
cat > /tmp/agent.log << 'EOF'
2026-02-08 10:15:23 INFO: Agent started
2026-02-08 10:15:24 INFO: Connected to database
2026-02-08 10:15:25 ERROR: Failed to fetch user profile: timeout
2026-02-08 10:15:26 INFO: Retrying request...
2026-02-08 10:15:27 INFO: Request succeeded
2026-02-08 10:15:28 ERROR: Failed to fetch user profile: timeout
2026-02-08 10:15:29 ERROR: Failed to fetch user profile: timeout
2026-02-08 10:15:30 WARNING: High memory usage: 85%
2026-02-08 10:15:31 INFO: Request succeeded
2026-02-08 10:15:32 ERROR: Database connection lost
2026-02-08 10:15:33 INFO: Reconnecting to database...
2026-02-08 10:15:34 INFO: Database reconnected
EOF
```

**Find all errors:**

```bash
grep ERROR /tmp/agent.log
```

**Output:**
```
2026-02-08 10:15:25 ERROR: Failed to fetch user profile: timeout
2026-02-08 10:15:28 ERROR: Failed to fetch user profile: timeout
2026-02-08 10:15:29 ERROR: Failed to fetch user profile: timeout
2026-02-08 10:15:32 ERROR: Database connection lost
```

**Count errors:**

```bash
grep -c ERROR /tmp/agent.log
```

**Output:**
```
4
```

**Find errors with context (2 lines before and after):**

```bash
grep -C 2 "Database connection lost" /tmp/agent.log
```

**Output:**
```
2026-02-08 10:15:31 INFO: Request succeeded
2026-02-08 10:15:32 ERROR: Database connection lost
2026-02-08 10:15:33 INFO: Reconnecting to database...
```

**Invert match (find everything EXCEPT errors):**

```bash
grep -v ERROR /tmp/agent.log
```

**Output:**
```
2026-02-08 10:15:23 INFO: Agent started
2026-02-08 10:15:24 INFO: Connected to database
2026-02-08 10:15:26 INFO: Retrying request...
2026-02-08 10:15:27 INFO: Request succeeded
2026-02-08 10:15:30 WARNING: High memory usage: 85%
2026-02-08 10:15:31 INFO: Request succeeded
2026-02-08 10:15:33 INFO: Reconnecting to database...
2026-02-08 10:15:34 INFO: Database reconnected
```

### sed: Search and Replace

**Replace timestamps with human-readable time:**

```bash
sed 's/2026-02-08 10:15:[0-9][0-9]/TODAY/g' /tmp/agent.log
```

**Output:**
```
TODAY INFO: Agent started
TODAY INFO: Connected to database
TODAY ERROR: Failed to fetch user profile: timeout
...
```

**Delete specific lines (remove INFO messages):**

```bash
sed '/INFO/d' /tmp/agent.log
```

**Output:**
```
2026-02-08 10:15:30 WARNING: High memory usage: 85%
```

**Extract error messages only (remove timestamps and level):**

```bash
sed 's/.*ERROR: /ERROR: /g' /tmp/agent.log | grep ERROR
```

**Output:**
```
ERROR: Failed to fetch user profile: timeout
ERROR: Failed to fetch user profile: timeout
ERROR: Failed to fetch user profile: timeout
ERROR: Database connection lost
```

### awk: Field Extraction and Processing

**awk is more powerful than grep/sed**—it processes text field by field.

**Extract error types from logs:**

```bash
awk '/ERROR/ {print $NF}' /tmp/agent.log
```

**Output:**
```
timeout
timeout
timeout
lost
```

**What's happening:**
- `/ERROR/` = Pattern to match (only process ERROR lines)
- `{print $NF}` = Print last field (`$NF` = last field)
- Fields are separated by whitespace by default

**Count occurrences of each error type:**

```bash
awk '/ERROR/ {errors[$NF]++} END {for (e in errors) print e, errors[e]}' /tmp/agent.log
```

**Output:**
```
timeout 3
lost 1
```

**What's happening:**
- `errors[$NF]++` = Increment count for each error type (last field)
- `END {...}` = Execute after processing all lines
- `for (e in errors) print e, errors[e]` = Print each error type and count

**Extract fields and create summary:**

```bash
awk '{print $2}' /tmp/agent.log | cut -d: -f1 | sort | uniq -c
```

**Output:**
```
      5 10:15:23
      5 10:15:24
      1 10:15:30
      1 10:15:31
      1 10:15:32
      1 10:15:33
      1 10:15:34
```

**Combined pipeline for error summary:**

```bash
grep ERROR /tmp/agent.log | awk '{print $NF}' | sort | uniq -c | sort -rn
```

**Output:**
```
      3 timeout
      1 lost
```

**What's happening:**
- `grep ERROR` = Find error lines only
- `awk '{print $NF}'` = Extract last field (error type)
- `sort` = Sort for uniq
- `uniq -c` = Count occurrences
- `sort -rn` = Sort by count (descending)

### Script: Log Analysis Dashboard

**Combine these tools into a monitoring script:**

```bash
cat > analyze-logs.sh << 'EOF'
#!/bin/bash

set -euo pipefail

LOG_FILE="/var/log/agents/customer-support.log"

if [ ! -f "$LOG_FILE" ]; then
    echo "Log file not found: $LOG_FILE"
    exit 1
fi

echo "=== Agent Log Analysis ==="
echo "Log file: $LOG_FILE"
echo

echo "1. Error Summary (by type)"
grep ERROR "$LOG_FILE" | awk '{print $NF}' | sort | uniq -c | sort -rn | head -5

echo
echo "2. Recent Errors (last 5)"
grep ERROR "$LOG_FILE" | tail -5

echo
echo "3. Error Count (last hour)"
RECENT_ERRORS=$(grep ERROR "$LOG_FILE" | tail -60 | grep -c ERROR || echo "0")
echo "Errors in last 60 log lines: $RECENT_ERRORS"

echo
echo "4. Warnings"
grep -c WARNING "$LOG_FILE" || echo "0"
echo "Warning count: $(grep -c WARNING "$LOG_FILE" || echo "0")"

echo
echo "5. Database Connection Issues"
grep -i "database" "$LOG_FILE" | grep -i "error\|fail\|lost" | tail -3
EOF
```

**Execute:**

```bash
chmod +x analyze-logs.sh
./analyze-logs.sh
```

**Output:**
```
=== Agent Log Analysis ===
Log file: /var/log/agents/customer-support.log

1. Error Summary (by type)
      3 timeout
      1 lost

2. Recent Errors (last 5)
2026-02-08 10:15:25 ERROR: Failed to fetch user profile: timeout
2026-02-08 10:15:28 ERROR: Failed to fetch user profile: timeout
2026-02-08 10:15:29 ERROR: Failed to fetch user profile: timeout
2026-02-08 10:15:32 ERROR: Database connection lost

3. Error Count (last hour)
Errors in last 60 log lines: 4

4. Warnings
Warning count: 1

5. Database Connection Issues
2026-02-08 10:15:32 ERROR: Database connection lost
```

---

## Part 5: Scheduling Scripts - Cron Jobs

Scripts you run manually are useful. Scripts that run **themselves** on schedules are automation.

### cron: Time-Based Job Scheduling

**cron** executes scripts on schedules:
- Every minute
- Every hour
- Every day at specific time
- Every week
- Every month

**crontab format:**

```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, Sunday = 0 or 7)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

**Edit your crontab:**

```bash
crontab -e
```

**Add these scheduled tasks:**

```bash
# Agent monitoring script - runs every 5 minutes
*/5 * * * * /home/yourname/scripts/analyze-logs.sh >> /var/log/agent-monitor.log 2>&1

# Agent health check - runs every hour
0 * * * * /home/yourname/scripts/health-check.sh

# Daily backup of agent configs - runs at 2 AM
0 2 * * * /home/yourname/scripts/backup-configs.sh

# Weekly log rotation - runs every Sunday at 3 AM
0 3 * * 0 /home/yourname/scripts/rotate-logs.sh
```

**Save and exit** (in nano: `Ctrl+O`, `Enter`, `Ctrl+X`)

**List your scheduled tasks:**

```bash
crontab -l
```

**Output:**
```
# Agent monitoring script - runs every 5 minutes
*/5 * * * * /home/yourname/scripts/analyze-logs.sh >> /var/log/agent-monitor.log 2>&1
...
```

### Script: Scheduled Health Check

**Create a health check script:**

```bash
cat > health-check.sh << 'EOF'
#!/bin/bash

set -euo pipefail

AGENT_URL="http://localhost:8000/health"
LOG_FILE="/var/log/agents/health-check.log"

# Check if agent is responding
if curl -f -s "$AGENT_URL" > /dev/null; then
    echo "[$(date)] Agent healthy" >> "$LOG_FILE"
else
    echo "[$(date)] ERROR: Agent health check failed" >> "$LOG_FILE"
    # Attempt restart
    systemctl restart customer-support-agent
    echo "[$(date)] Agent restart attempted" >> "$LOG_FILE"
fi
EOF
```

**Schedule it:**

```bash
chmod +x health-check.sh
crontab -e
# Add: */10 * * * * /home/yourname/scripts/health-check.sh
```

**What you built:**
- Health check runs every 10 minutes
- Logs all checks with timestamps
- Automatically restarts agent if unhealthy
- Creates self-healing deployment

---

## Part 6: Functions - Reusable Script Components

Functions let you package repeated logic into reusable blocks.

**Create a deployment script with functions:**

```bash
cat > deploy-with-functions.sh << 'EOF'
#!/bin/bash

set -euo pipefail

# Function: Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function: Install system packages
install_packages() {
    echo "Installing system packages..."
    sudo apt update
    sudo apt install -y python3 python3-pip
}

# Function: Create agent user
create_agent_user() {
    local username="agentuser"
    if id "$username" &>/dev/null; then
        echo "User $username already exists"
    else
        sudo useradd -r -s /bin/bash "$username"
        echo "Created user $username"
    fi
}

# Function: Setup agent directory
setup_agent_dir() {
    local agent_dir="/var/agents/customer-support"
    sudo mkdir -p "$agent_dir"
    sudo chown agentuser:agentuser "$agent_dir"
    echo "Setup agent directory: $agent_dir"
}

# Function: Install Python dependencies
install_python_deps() {
    echo "Installing Python dependencies..."
    pip3 install --user fastapi uvicorn
}

# Main deployment workflow
main() {
    install_packages
    create_agent_user
    setup_agent_dir
    install_python_deps
    echo "Deployment complete!"
}

# Execute main function
main
EOF
```

**Execute:**

```bash
chmod +x deploy-with-functions.sh
./deploy-with-functions.sh
```

**What you learned:**
- `function_name() { commands; }` = Define function
- `local variable` = Local scope (exists only in function)
- `$1` = First argument passed to function
- Functions organize scripts into logical blocks
- `main()` function serves as entry point

**Pass arguments to functions:**

```bash
cat > deploy-params.sh << 'EOF'
#!/bin/bash

set -euo pipefail

deploy_agent() {
    local agent_name="$1"
    local port="$2"
    local agent_dir="/var/agents/${agent_name}"

    echo "Deploying ${agent_name} on port ${port}..."
    mkdir -p "$agent_dir"
    # ... deployment logic ...
    echo "${agent_name} deployed to ${agent_dir}"
}

# Deploy multiple agents
deploy_agent "customer-support" 8000
deploy_agent "sales-bot" 8001
deploy_agent "analytics" 8002
EOF
```

---

## Safety Note

**Test scripts in non-production environment first.** A script with `rm -rf` in the wrong place can delete everything. Always:
1. Test scripts in a safe environment (VM, container, test directory)
2. Use `echo` statements to preview what script will do
3. Add `set -euo pipefail` to catch errors early
4. Never run deployment scripts as root unless absolutely necessary

---

## Try With AI

**💡 Design Idempotent Scripts:**

> "I want to make my bash deployment scripts idempotent—safe to run multiple times without side effects. Help me identify what could go wrong if I run this script twice:

[show your deploy-agent.sh script]

For each potential problem, suggest the fix. Explain what idempotency means for bash scripts and why it matters for production deployments."

**What you're learning:** How AI analyzes scripts for failure modes and suggests patterns that make automation reliable. Idempotency prevents "it works the first time but breaks on rerun" problems.

**🔧 Build a Log Analysis Tool:**

> "I have agent logs in /var/log/agents/ with this format:
[show 3-4 sample log lines with timestamps, levels, messages]

I want to create a bash script that:
1. Counts errors by type (like 'timeout', 'connection failed')
2. Shows the last 10 errors with context (2 lines before and after)
3. Alerts if error rate exceeds threshold (more than 10 errors in last 50 lines)
4. Extracts database connection issues specifically

Help me build this script using grep, awk, and sed. Explain each pipeline and how the data flows through each command."

**What you're learning:** How to compose bash text processing tools into powerful analysis pipelines. You'll discover how Unix philosophy ("small tools that compose") enables log analysis without writing complex code.

**⚙️ Create a Self-Healing Deployment:**

> "I want to create a deployment script that not only installs agents but also monitors and heals them. Help me design a bash script that:

1. Deploys the agent (install deps, configure, start service)
2. Immediately runs a health check to verify deployment succeeded
3. If health check fails, rolls back to previous version
4. Sets up a cron job that monitors agent health every 5 minutes
5. Automatically restarts agent if it fails 3 consecutive health checks

I want the script to be modular—separate functions for deploy, health-check, rollback, and monitor. Walk me through the design and help me write the script."

**What you're learning:** How to design robust automation that handles failures gracefully. You'll discover how to combine deployment, monitoring, and self-healing into a single automated system.
