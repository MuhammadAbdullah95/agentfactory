---
sidebar_position: 6
chapter: 10
lesson: 6
title: "Process Control with systemd"
description: "Deploy unkillable AI agent services that start on boot, restart automatically on failure, and log reliably"
keywords: ["systemd", "service", "daemon", "production", "restart", "logging", "agent deployment"]
duration_minutes: 75

# HIDDEN SKILLS METADATA
skills:
  - name: "systemd Service Creation"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student creates a working .service file that starts, stops, and restarts an agent"

  - name: "Auto-Restart Policy Configuration"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student configures Restart=always and verifies agent restarts after crash"

  - name: "Boot Enablement and Dependency Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student enables service to start on boot and configures proper dependencies"

  - name: "Service Monitoring and Log Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student uses systemctl and journalctl to monitor service status and debug failures"

learning_objectives:
  - objective: "Create systemd service files for agent deployment with proper configuration"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student writes a .service file with correct [Unit], [Service], and [Install] sections"

  - objective: "Configure auto-restart policies for production reliability"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student demonstrates agent automatically restarts after intentional kill"

  - objective: "Enable services to start automatically on system boot"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student enables service and verifies it starts after simulated reboot"

  - objective: "Monitor services and diagnose failures using systemctl and journalctl"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Student interprets service status and identifies failure causes from logs"

cognitive_load:
  new_concepts: 8
  concepts_list:
    - "systemd architecture and unit files"
    - "Service file structure ([Unit], [Service], [Install])"
    - "Restart policies and reliability configuration"
    - "Service enablement and boot startup"
    - "Dependency management (After=, Wants=)"
    - "Service monitoring with systemctl"
    - "Log management with journalctl"
    - "User permissions and security"
  assessment: "8 concepts (within B2 limit of 7-10)"

teaching_approach: "Hands-on creation with AI collaboration (Learn Basics → AI Suggests Production Patterns → Iterate Together → Master Deployment)"
modality: "Collaborative Discovery (Learn Basics → AI Suggests Production Patterns → Iterate Together → Master Deployment)"

differentiation:
  extension_for_advanced: "Explore systemd timers for scheduled agent tasks, socket activation for on-demand starting, or resource limits with CPU/memory quotas"
  remedial_for_struggling: "Practice with a simple echo command service before deploying a full agent. Use 'systemctl status' frequently to verify each step works."

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-02-08"
version: "1.0.0"
---

# Process Control with systemd

## From Manual to Automatic: Unkillable Agent Services

In Lesson 3, you mastered tmux—persistent sessions that survive disconnections. But tmux has a critical limitation: **you must remember to start them**. When a server reboots, your tmux sessions vanish. Your agents don't start until you log in and recreate everything manually.

For production Digital FTEs, this is unacceptable.

**systemd** solves this by turning your agents into **system services**—first-class citizens managed by the operating system itself. systemd services:
- Start automatically on boot (no manual intervention)
- Restart automatically when they crash (self-healing)
- Log reliably to the system journal (centralized monitoring)
- Respect dependencies (database before application)
- Run under specific users (security best practices)

Think of systemd as the operating system's conductor. It knows what services should run, when they should start, what they depend on, and how to recover them when things go wrong. Your Digital FTE becomes part of the server's fabric—**unkillable, automatic, and production-grade**.

For serious agent deployment, systemd isn't optional. It's how real services run in production.

---

## Phase 1: Execute - Your First systemd Service

Let's transform a simple agent into a production service. We'll build it step by step.

### Activity 1.1: Create a Simple Agent

First, let's create a minimal agent to deploy:

```bash
# Create agent directory
mkdir -p ~/agents/hello-agent
cd ~/agents/hello-agent

# Create the agent
cat > hello_agent.py << 'EOF'
#!/usr/bin/env python3
import time
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main():
    logger.info("Hello Agent starting...")
    counter = 0

    while True:
        counter += 1
        logger.info(f"Hello iteration {counter} at {datetime.now()}")
        time.sleep(5)  # Run every 5 seconds

if __name__ == "__main__":
    main()
EOF

# Make it executable
chmod +x hello_agent.py

# Test it runs
python3 hello_agent.py
```

**Press Ctrl+C** to stop it (we'll run it as a service soon).

**What you built**: A minimal agent that logs a message every 5 seconds. Simple enough to understand, real enough to demonstrate systemd's power.

### Activity 1.2: Create the systemd Service File

Now let's create the service definition. Systemd services live in `/etc/systemd/system/`:

```bash
# Create service file with sudo
sudo nano /etc/systemd/system/hello-agent.service
```

**Add this content**:

```ini
[Unit]
Description=Hello Agent Service
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME/agents/hello-agent
ExecStart=/usr/bin/python3 /home/YOUR_USERNAME/agents/hello-agent/hello_agent.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**⚠️ CRITICAL**: Replace `YOUR_USERNAME` with your actual username. Run `whoami` if you're not sure.

**Save and exit**: `Ctrl+O`, `Enter`, `Ctrl+X` (nano workflow)

**What each section does**:

| Section | Purpose | Key Directives |
|---------|---------|----------------|
| **[Unit]** | Metadata and dependencies | `Description`: Human-readable name<br>`After=network.target`: Start after network is ready |
| **[Service]** | How to run the process | `Type=simple`: Service runs continuously<br>`User`: Run as this user (not root)<br>`ExecStart`: Command to start<br>`Restart=always`: Always restart on failure<br>`RestartSec=10`: Wait 10 seconds before restart |
| **[Install]** | How to enable at boot | `WantedBy=multi-user.target`: Enable in normal multi-user mode |

**Why this matters**: The `[Service]` section's `Restart=always` is what makes your agent **unkillable**. If it crashes, systemd brings it back. If the server reboots, systemd starts it. Your agent becomes resilient by design.

### Activity 1.3: Reload and Start the Service

Systemd needs to know about the new service file:

```bash
# Reload systemd configuration
sudo systemctl daemon-reload
```

**Now start it**:

```bash
sudo systemctl start hello-agent
```

**Check if it's running**:

```bash
sudo systemctl status hello-agent
```

**Output**:
```
● hello-agent.service - Hello Agent Service
     Loaded: loaded (/etc/systemd/system/hello-agent.service; disabled; preset: enabled)
     Active: active (running) since Fri 2026-02-08 14:32:15 UTC; 15s ago
   Main PID: 12345 (python3)
      Tasks: 1 (limit: 4915)
     Memory: 8.5M (peak: 9.2M)
        CPU: 125ms
     CGroup: /system.slice/hello-agent.service
             └─12345 /usr/bin/python3 /home/user/agents/hello-agent/hello_agent.py

Feb 08 14:32:15 server python3[12345]: 2026-02-08 14:32:15,123 - INFO - Hello Agent starting...
Feb 08 14:32:15 server python3[12345]: 2026-02-08 14:32:20,124 - INFO - Hello iteration 1 at 2026-02-08 14:32:20.124356
Feb 08 14:32:20 server python3[12345]: 2026-02-08 14:32:25,125 - INFO - Hello iteration 2 at 2026-02-08 14:32:25.125789
```

**Key information**:
- `Active: active (running)` — Service is healthy
- `Main PID: 12345` — Process ID
- Recent log lines show the agent running

### Activity 1.4: Test Auto-Restart (Self-Healing)

Here's where systemd shines. Let's kill the agent manually and watch systemd bring it back:

```bash
# Find the process ID
sudo systemctl status hello-agent | grep "Main PID"

# Kill it (replace 12345 with actual PID)
sudo kill 12345

# Immediately check status
sudo systemctl status hello-agent
```

**Output**:
```
● hello-agent.service - Hello Agent Service
     Loaded: loaded (/etc/systemd/system/hello-agent.service; disabled; preset: enabled)
     Active: active (running) since Fri 2026-02-08 14:32:40 UTC; 2s ago
   Main PID: 12456 (python3)  # NEW PID!
      Tasks: 1 (limit: 4915)
     Memory: 8.2M
        CPU: 98ms

Feb 08 14:32:38 server systemd[1]: hello-agent.service: Scheduled restart job
Feb 08 14:32:38 server systemd[1]: Stopped hello-agent.service
Feb 08 14:32:40 server systemd[1]: Started hello-agent.service
Feb 08 14:32:40 server python3[12456]: 2026-02-08 14:32:40,456 - INFO - Hello Agent starting...
```

**What happened**:
1. You killed the process
2. systemd detected it stopped
3. systemd restarted it automatically (notice the new PID: 12456)
4. Service is `active (running)` again

**This is self-healing**. Your agent crashed (or was killed), and it came back automatically. In production, this means temporary glitches don't become outages.

### Activity 1.5: Enable at Boot (The Ultimate Test)

Currently, the service is `disabled` — it won't start on boot. Let's enable it:

```bash
sudo systemctl enable hello-agent
```

**Output**:
```
Created symlink /etc/systemd/system/multi-user.target.wants/hello-agent.service → /etc/systemd/system/hello-agent.service.
```

**What this means**: systemd created a symlink so that when the system reaches `multi-user.target` (normal startup), it starts your service.

**Verify it's enabled**:

```bash
sudo systemctl status hello-agent
```

Look for: `enabled` (not `disabled`) in the Loaded line.

**Test boot behavior** (without actually rebooting):

```bash
# Stop the service
sudo systemctl stop hello-agent

# Verify it stopped
sudo systemctl status hello-agent
# Should show: Active: inactive (dead)

# Start it via systemd (simulating boot behavior)
sudo systemctl start hello-agent

# Verify it started
sudo systemctl status hello-agent
# Should show: Active: active (running)
```

**What You Learned**: Enabling a service means it survives reboots. When the server starts, systemd starts your agent automatically—no manual intervention needed.

---

## Phase 2: Three Roles Demonstration—Production Service Configuration

Now we move from mechanics to production design. This is where AI helps you discover enterprise-grade patterns.

### Scenario 1: Learning Production Restart Patterns

**What you ask AI**:

```
I'm deploying a FastAPI agent to production. Sometimes it crashes due to
temporary network issues. Other times it has bugs that make it crash immediately.

I want systemd to handle both cases:
- Temporary glitches: Restart automatically with backoff
- Bugs (immediate crashes): Don't restart infinitely, alert me instead

How should I configure Restart policies in the [Service] section?
```

**What AI teaches you**:

```
For production FastAPI services, use a layered restart strategy:

[Service]
Restart=on-failure
RestartSec=5s
StartLimitInterval=60s
StartLimitBurst=5

How this works:
- Restart=on-failure: Only restart if the service exits with an error code
  (FastAPI's 0 exit = success, non-zero = failure)

- RestartSec=5s: Wait 5 seconds before restarting (gives system time to recover)

- StartLimitInterval=60s: Count restart attempts within 60 seconds
- StartLimitBurst=5: Allow 5 rapid restart attempts, then stop trying

This prevents infinite restart loops:
- Temporary glitch: Service restarts and recovers ✓
- Fatal bug: Crashes 5 times in 60 seconds → systemd gives up → you get alerted ✓

The "give up" state shows in systemctl as:
Active: inactive (dead) (Result: start-limit-hit)
```

**What you learned**: AI taught you **start-limit protection** — a production pattern you hadn't considered. You knew about `Restart=always`, but not how to prevent restart storms when services have fatal bugs.

**Key moment**: AI suggested a nuanced restart policy (on-failure + backoff limits) that prevents the infinite restart problem you didn't anticipate.

---

### Scenario 2: Explaining Your Deployment Constraints

Now you reverse roles. You have constraints the AI doesn't know about.

**What you tell AI**:

```
I deploy agents to servers with strict resource limits. If an agent starts
consuming too much memory, it needs to be killed and restarted. But I don't
want to write external monitoring scripts.

Can systemd handle this? I want to:
1. Set a memory limit (e.g., 500MB)
2. Kill the agent if it exceeds the limit
3. Restart it automatically

Is this built into systemd, or do I need external tools like cgroups manually?
```

**What AI suggests**:

```
systemd has built-in resource limits! Use these in [Service]:

[Service]
MemoryMax=500M
MemorySwapMax=0  # Disable swap (forces memory limit)
Restart=on-failure

How it works:
- MemoryMax=500M: If process exceeds 500MB RAM, systemd sends SIGKILL
- MemorySwapMax=0: Prevent process from swapping to disk (hard limit)
- Restart=on-failure: SIGKILL counts as failure → auto-restart

Verify memory usage with:
systemctl show hello-agent | grep Memory

View actual consumption:
systemctl status hello-agent  (shows memory in status output)

Logs when limit hit:
Feb 08 15:23:45 server systemd[1]: hello-agent.service: A process of this unit has been killed with SIGKILL by systemd (oom-killed).
```

**But you clarify**:

```
Good start, but I need to understand the difference between MemoryMax and
MemoryLimit. Which one should I use?

Also, what happens to the agent's data when it's killed? Does it get a chance
to shutdown gracefully, or is it instant death?
```

**What AI confirms**:

```
Great questions:

MemoryMax vs MemoryLimit:
- MemoryMax (recommended): Total memory including file mappings
- MemoryLimit: Only anonymous memory (excluding file mappings)
→ Use MemoryMax for production (more predictable)

Graceful shutdown vs SIGKILL:
- MemoryMax sends SIGTERM first, waits TimeoutStopSec (default 90s)
- If process doesn't exit, THEN sends SIGKILL
- Your agent can catch SIGTERM and shutdown gracefully:

```python
import signal
import sys

def graceful_shutdown(signum, frame):
    logger.info("Received shutdown signal, saving state...")
    # Save state, close connections, etc.
    sys.exit(0)

signal.signal(signal.SIGTERM, graceful_shutdown)
```

So your agent gets ~90 seconds to clean up before hard kill.
```

**What AI learned**: AI adapted to **your constraints** (resource limits without external tools) and clarified the grace period behavior. You taught AI that graceful shutdown matters for your agents—they hold state that needs saving.

**Key moment**: You corrected AI's assumption that hard memory limits are acceptable, and learned how to implement graceful shutdown.

---

### Scenario 3: Iterating on Production Service Design Together

Here's where both of you iterate together, creating something better than either would design alone.

**Iteration 1: Initial service file**

You ask AI: "Create a systemd service for a FastAPI agent that needs PostgreSQL, Redis, and runs on port 8000."

**AI suggests**:
```ini
[Unit]
Description=FastAPI Agent
After=network.target

[Service]
User=agentuser
ExecStart=/usr/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

You think: "This starts, but what if PostgreSQL isn't ready yet? The agent will crash immediately."

**Iteration 2: You add a dependency**

You ask AI: "Can I make this wait for PostgreSQL to be ready?"

**AI suggests**:
```ini
[Unit]
Description=FastAPI Agent
After=network.target postgresql.service
Requires=postgresql.service

[Service]
User=agentuser
ExecStart=/usr/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
```

You think: "Better, but `Requires=` means if PostgreSQL fails to start, my agent never starts. I want it to retry."

**Iteration 3: Convergence**

Together you arrive at:
```ini
[Unit]
Description=FastAPI Agent with Database and Cache
After=network.target postgresql.service redis.service
Wants=postgresql.service redis.service

[Service]
Type=notify
NotifyAccess=all
User=agentuser
WorkingDirectory=/var/agents/fastapi-agent
ExecStart=/usr/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=5s
StartLimitInterval=60s
StartLimitBurst=5
Environment="DATABASE_URL=postgresql://user:pass@localhost/dbname"
Environment="REDIS_URL=redis://localhost:6379"
StandardOutput=journal
StandardError=journal
SyslogIdentifier=fastapi-agent

[Install]
WantedBy=multi-user.target
```

**What neither of you had individually**:
- You didn't know about `Type=notify` for better startup tracking
- AI didn't know that `Wants=` is better than `Requires=` for your use case (retry if dependency fails)
- Together, you created a **resilient service design** that handles dependencies gracefully
- AI suggested `NotifyAccess=all` for better integration with systemd's notification protocol
- You insisted on environment variables for secrets (not hardcoded in the agent)

**What emerged**: A production-ready service configuration that neither of you would have written alone—combining systemd best practices with your operational requirements.

#### 🤝 Practice Exercise

> **Ask your AI**: "I'm deploying a machine learning agent that loads a 2GB model into memory on startup. It needs: GPU access, a specific NVIDIA driver version, and must log predictions to a remote service that's sometimes flaky. Create a systemd service that: (1) waits for GPU to be available, (2) sets appropriate resource limits, (3) handles the remote logging service being down gracefully, (4) restarts with backoff if the model loading fails. Explain each directive and why it's necessary for ML agents specifically."

**Expected Outcome**: You'll discover how to configure services for resource-heavy AI workloads with external dependencies—balancing resilience with resource constraints.

**Key moment**: This is Co-Worker convergence—iteration produced a service design optimized for **your specific constraints** (ML model loading, flaky logging service), not just a generic "restart if fails" configuration.

---

## Phase 3: Apply - Production Service Monitoring

Creating services is half the battle. Monitoring them is the other half.

### Activity 3.1: Monitor Service Health

```bash
# Real-time status
sudo systemctl status hello-agent

# Check if service is active (exit code 0 = yes, 1 = no)
sudo systemctl is-active hello-agent

# Check if service is enabled for boot
sudo systemctl is-enabled hello-agent
```

**Output meanings**:
| Command | Output | Meaning |
|---------|--------|---------|
| `is-active` | `active` | Running |
| `is-active` | `inactive` | Not running |
| `is-active` | `failed` | Failed to start |
| `is-enabled` | `enabled` | Will start on boot |
| `is-enabled` | `disabled` | Won't start on boot |
| `is-enabled` | `static` | Cannot be enabled (dependency of another service) |

### Activity 3.2: View Service Logs

systemd captures all service output in the journal:

```bash
# Follow logs in real-time (like tail -f)
sudo journalctl -u hello-agent -f

# View last 50 lines
sudo journalctl -u hello-agent -n 50

# View logs since last boot
sudo journalctl -u hello-agent -b

# View logs with timestamps
sudo journalctl -u hello-agent --since today
```

**Press Ctrl+C** to stop following.

**Common log patterns**:

| Log Message | Meaning | Action |
|------------|---------|--------|
| `Started hello-agent.service` | Service started successfully | ✓ Normal |
| `Stopped hello-agent.service` | Service stopped normally | ✓ Normal (if you stopped it) |
| `hello-agent.service: Scheduled restart job` | Service crashed, restart scheduled | ⚠️ Check why it crashed |
| `start-limit-hit` | Service crashed too fast, gave up | 🔴 Fatal bug, investigation needed |
| `Failed with result 'exit-code'` | Service exited with error | 🔴 Check application logs |

### Activity 3.3: Service Control Commands

```bash
# Start a service
sudo systemctl start hello-agent

# Stop a service
sudo systemctl stop hello-agent

# Restart a service (stop then start)
sudo systemctl restart hello-agent

# Reload configuration (for services that support it)
sudo systemctl reload hello-agent

# Show service configuration file
sudo systemctl cat hello-agent

# Edit service configuration (opens in default editor)
sudo systemctl edit hello-agent
```

**⚠️ Service Editing Safety**: `systemctl edit` creates an override file (`/etc/systemd/system/hello-agent.service.d/override.conf`). This is safer than editing the main file directly—updates to the main file won't overwrite your customizations.

### Activity 3.4: Create a Monitoring Script

Automate service health checks:

```bash
nano ~/check-services.sh
```

**Add this content**:

```bash
#!/bin/bash

# List of services to monitor
SERVICES=("hello-agent" "ssh" "nginx")

echo "Service Status Report - $(date)"
echo "================================"

for service in "${SERVICES[@]}"; do
    if systemctl is-active --quiet "$service"; then
        echo "✓ $service: RUNNING"
    else
        echo "✗ $service: FAILED"
        # Optionally attempt restart
        # sudo systemctl restart "$service"
    fi
done
```

**Make it executable**:

```bash
chmod +x ~/check-services.sh
```

**Run it**:

```bash
~/check-services.sh
```

**Output**:
```
Service Status Report - Fri Feb  8 15:32:15 UTC 2026
================================
✓ hello-agent: RUNNING
✓ ssh: RUNNING
✗ nginx: FAILED
```

**What You Learned**: Automation transforms monitoring from "remember to check" into "see problems instantly." You can extend this script to send alerts (email, Slack) or attempt automatic recovery.

---

## Phase 4: Master - Advanced Service Patterns

Production environments demand more sophisticated service management.

### Activity 4.1: Service Templates (Deploy Multiple Instances)

When you need multiple instances of the same service (e.g., 3 worker agents), use **service templates**:

```bash
sudo nano /etc/systemd/system/hello-agent@.service
```

**Note the `@` symbol in the filename**.

```ini
[Unit]
Description=Hello Agent Instance %i
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME/agents/hello-agent
ExecStart=/usr/bin/python3 /home/YOUR_USERNAME/agents/hello-agent/hello_agent.py --instance %i
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

**The `%i` gets replaced with the instance name**.

**Start multiple instances**:

```bash
# Start 3 instances
sudo systemctl start hello-agent@1
sudo systemctl start hello-agent@2
sudo systemctl start hello-agent@3

# Check all instances
systemctl status 'hello-agent@*'
```

**Output**:
```
● hello-agent@1.service - Hello Agent Instance 1
     Active: active (running)
● hello-agent@2.service - Hello Agent Instance 2
     Active: active (running)
● hello-agent@3.service - Hello Agent Instance 3
     Active: active (running)
```

**What you built**: Instant scalability—deploy 1 or 100 agent instances from a single service template.

### Activity 4.2: Resource Limits for Production

Prevent runaway resource consumption:

```ini
[Service]
# CPU limits (1.5 CPU cores max)
CPUQuota=150%

# Memory limits (500MB max, 1GB max with swap)
MemoryMax=500M
MemorySwapMax=1G

# File descriptor limits (number of open files)
LimitNOFILE=65536

# Process limits (max threads)
TasksMax=1024
```

**Verify limits are applied**:

```bash
sudo systemctl show hello-agent | grep -E "(Memory|CPU|Tasks)"
```

### Activity 4.3: Environment Management

Don't hardcode secrets in service files. Use environment files:

```bash
# Create environment file
sudo nano /etc/hello-agent/env
```

**Add secrets**:
```ini
DATABASE_URL=postgresql://user:password@localhost/db
API_KEY=sk-proj-abc123secret
LOG_LEVEL=INFO
```

**Set secure permissions**:

```bash
sudo chmod 600 /etc/hello-agent/env
```

**Reference in service file**:

```ini
[Service]
EnvironmentFile=/etc/hello-agent/env
ExecStart=/usr/bin/python3 /home/user/agents/hello-agent/hello_agent.py
```

**⚠️ Security**: `chmod 600` ensures only the file owner can read secrets. Never commit environment files to git.

### Activity 4.4: Service Dependencies and Ordering

Control startup order precisely:

```ini
[Unit]
Description=FastAPI Agent
After=network-online.target
Wants=network-online.target postgresql.service redis.service

[Service]
# ...
```

**Dependency types**:

| Directive | Behavior | Use Case |
|-----------|----------|----------|
| `Requires=` | Hard dependency | If dependency fails, service fails to start |
| `Wants=` | Soft dependency | Service starts even if dependency fails |
| `After=` | Ordering only | Start after dependency, but don't care if it fails |
| `Before=` | Reverse ordering | Ensure this service starts before another |

**What You Learned**: Dependency management prevents race conditions where your agent starts before the database is ready.

---

## Understanding: systemd vs Traditional Init Systems

| Feature | systemd | SysV Init | Upstart |
|---------|---------|-----------|---------|
| **Parallel startup** | ✅ Yes | ❌ No | ✅ Yes |
| **On-demand starting** | ✅ Socket activation | ❌ No | ✅ Yes |
| **Resource limits** | ✅ Built-in | ❌ No | ⚠️ Limited |
| **Logging integration** | ✅ Journal | ❌ Separate files | ❌ Separate files |
| **Dependency management** | ✅ Declarative | ⚠️ Manual ordering | ✅ Declarative |
| **Process tracking** | ✅ cgroups | ❌ Process trees | ⚠️ Basic |

**Why systemd won**:
- Unified system management (init, logging, cron, network, user sessions in one system)
- Parallel startup (faster boot times)
- Fine-grained dependency control
- Excellent tooling (`systemctl`, `journalctl`, `systemd-analyze`)

**Modern Linux distributions using systemd**: Ubuntu, Debian, RHEL, CentOS, Fedora, Arch Linux (essentially all major distributions).

---

## Safety Note

**⚠️ Running Services as Root**: Avoid `User=root` in service files. Create dedicated users for each agent (`sudo adduser agentuser`). Running as root is a security risk—any agent vulnerability compromises the entire system.

**⚠️ Resource Exhaustion**: Always set memory and CPU limits for production services. Without limits, a buggy agent can consume all system resources and crash the server.

**⚠️ Infinite Restart Loops**: Use `Restart=on-failure` with `StartLimitBurst` to prevent restart storms when agents have fatal bugs.

**⚠️ Secret Management**: Never put passwords or API keys directly in service files. Use `EnvironmentFile` with restricted permissions (`chmod 600`).

---

## Try With AI

Let's explore production systemd patterns for complex agent deployments.

**🏗️ Design Multi-Service Architecture**:

```
I'm deploying an agent system with 4 components:
1. API Gateway (FastAPI, port 8000)
2. Worker Service (processes jobs from Redis queue)
3. Scheduler (cron-like task dispatcher)
4. Monitoring Agent (health checks, alerts)

Constraints:
- Workers must start AFTER Redis is ready
- Scheduler depends on API Gateway
- All services must log centrally
- If Worker crashes, restart with backoff
- If Monitoring fails, alert but don't restart (might hide issues)

Create systemd service files for all 4 components with proper dependencies,
restart policies, and resource limits. Explain the dependency ordering
and why you chose specific restart policies for each service.
```

**What you're learning**: How to design multi-service architectures with systemd handling orchestration—expressing complex startup ordering and failure handling through declarative configuration, not custom scripts.

**🔧 Implement Graceful Shutdown**:

```
My FastAPI agent handles long-running inference requests (up to 2 minutes).
When I restart the service with `systemctl restart`, active requests get cut
off mid-inference, causing data corruption.

I need to implement graceful shutdown:
1. Catch SIGTERM signal from systemd
2. Stop accepting new requests
3. Wait for active requests to complete (max 90 seconds)
4. Exit cleanly

Show me:
1. The systemd service configuration (Type=, TimeoutStopSec=, etc.)
2. The Python/FastAPI code to handle shutdown
3. How to test that graceful shutdown works
```

**What you're learning**: The difference between hard termination (SIGKILL) and graceful shutdown (SIGTERM + timeout)—critical for production systems that handle long-running requests or hold state.

**⚡ Production Monitoring and Alerting**:

```
I have 20 systemd services running on a server. Some are critical (agent-api),
some are background (data-processor).

I need a monitoring solution that:
1. Checks all services every 30 seconds
2. Sends alerts to Slack when critical services fail
3. Auto-restarts non-critical services
4. Generates daily health reports
5. Tracks restart frequency (alert on restart storms)

Design this using:
- systemd timers (for periodic checks)
- bash scripts (for monitoring logic)
- slack API (for alerts)
- journalctl (for log analysis)

Give me the complete setup with all files and commands.
```

**What you're learning**: How to build production monitoring systems by combining systemd's built-in capabilities (timers, service state) with external tooling (Slack alerts, log analysis) to create robust operational visibility.
