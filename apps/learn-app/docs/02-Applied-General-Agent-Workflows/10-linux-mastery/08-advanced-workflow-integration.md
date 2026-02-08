---
sidebar_position: 8
chapter: 10
lesson: 8
title: "Advanced Workflow Integration"
description: "Synthesize Linux skills into integrated workflows for production Digital FTE deployments, creating reusable automation patterns"
keywords: ["workflow integration", "automation patterns", "production deployment", "monitoring", "scalability"]
duration_minutes: 75

# HIDDEN SKILLS METADATA
skills:
  - name: "Workflow Synthesis and Integration"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student designs and implements complete integrated workflow combining multiple Linux skills for production agent deployment"

  - name: "Production Pattern Evaluation"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Evaluate"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student compares and selects appropriate deployment patterns for specific agent requirements"

  - name: "Scalability Architecture"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Evaluate"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student analyzes and designs workflows that scale across multiple agents and environments"

learning_objectives:
  - objective: "Synthesize Linux skills from previous lessons into integrated workflows for production deployments"
    proficiency_level: "C1"
    bloom_level: "Create"
    assessment_method: "Student designs and implements complete workflow combining systemd, tmux, scripting, and monitoring for multi-agent deployment"

  - objective: "Evaluate deployment patterns and select appropriate approaches for specific agent requirements"
    proficiency_level: "B2"
    bloom_level: "Evaluate"
    assessment_method: "Student analyzes scenario requirements and justifies pattern choice with trade-off analysis"

  - objective: "Create reusable automation patterns for Digital FTE operations"
    proficiency_level: "C1"
    bloom_level: "Create"
    assessment_method: "Student builds automation framework that can be applied across different agent types and deployments"

cognitive_load:
  new_concepts: 8
  concepts_list:
    - "Workflow synthesis and composition"
    - "Pattern evaluation and selection"
    - "Scalability architecture"
    - "Automation framework design"
    - "Multi-environment deployment"
    - "Monitoring and observability integration"
    - "Failure recovery strategies"
    - "Documentation and knowledge capture"
  assessment: "8 concepts (within C1 limit for advanced synthesis)"

teaching_approach: "Synthesis and Creation (Integrate → Evaluate → Create → Deploy)"
modality: "Collaborative Design with AI (Co-Worker iteration on workflow architecture)"

differentiation:
  extension_for_advanced: "Design multi-environment deployment pipeline with CI/CD integration, or create comprehensive monitoring dashboard with alerting"
  remedial_for_struggling: "Practice single-skill integration first (systemd + monitoring), then add complexity gradually. Use reference patterns from earlier lessons."

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-02-08"
version: "1.0.0"
---

# Advanced Workflow Integration

## From Skills to Systems

In Lessons 1-7, you built a comprehensive Linux toolkit: terminal navigation, persistent sessions, shell automation, security hardening, process control, and debugging. You now possess all the individual components.

**The gap**: Components alone don't create production systems. You need **integration patterns** that combine these components into coherent, reliable workflows.

**The opportunity**: The difference between "someone who knows Linux" and "a production-ready Digital FTE operator" is workflow design. Your agents live in the messy reality of servers crashing, networks failing, disks filling, and deployments going wrong. The workflows you design now determine whether your Digital FTEs survive that reality.

Think of it like construction: You have the tools (hammer, saw, drill), but you need **architectural patterns** (how to frame a wall, wire a circuit, plumb a bathroom) to build a house. This lesson teaches those architectural patterns for Linux-based agent deployments.

---

## Phase 1: Execute - The Integrated Deployment Workflow

Let's build a complete workflow that demonstrates how all previous skills integrate. We'll deploy a multi-agent system with monitoring, persistence, and automation.

### Activity 1.1: Design the Architecture

Before deploying, define what you're building:

**System Requirements**:
- 3 AI agents running as systemd services (customer-support, data-processor, report-generator)
- Persistent tmux sessions for manual intervention
- Automated health checks every 5 minutes
- Centralized logging to /var/agents/logs
- Monitoring dashboard with htop
- Automatic recovery on failures
- Security: dedicated user, no root access, SSH keys only

**Success Criteria**:
- All agents start on boot automatically
- Failed agents restart within 10 seconds
- You can monitor all agents from one tmux session
- Logs rotate automatically (no disk space issues)
- New agent deployment takes under 5 minutes

### Activity 1.2: Build the Deployment Script

Create the automation that makes deployment repeatable:

```bash
#!/bin/bash
# deploy-agent-system.sh - Complete multi-agent deployment
# This script orchestrates the entire workflow

set -e  # Exit on error (safe failure)

# Configuration
AGENT_USER="agent-runner"
AGENT_DIR="/var/agents"
LOG_DIR="/var/agents/logs"
SYSTEMD_DIR="/etc/systemd/system"

# Color output for readability
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

# Step 1: Create dedicated user
log "Creating dedicated agent user..."
if id "$AGENT_USER" &>/dev/null; then
    log "User $AGENT_USER already exists"
else
    sudo useradd -r -s /bin/bash -d $AGENT_DIR $AGENT_USER
    log "Created user $AGENT_USER"
fi

# Step 2: Create directory structure
log "Creating directory structure..."
sudo mkdir -p $AGENT_DIR/{customer-support,data-processor,report-generator}
sudo mkdir -p $LOG_DIR
sudo chown -R $AGENT_USER:$AGENT_USER $AGENT_DIR
sudo chown -R $AGENT_USER:$AGENT_USER $LOG_DIR
log "Directories created and permissions set"

# Step 3: Deploy agent code
log "Deploying agent code..."
for agent in customer-support data-processor report-generator; do
    if [ -d "agents/$agent" ]; then
        sudo cp -r agents/$agent/* $AGENT_DIR/$agent/
        sudo chown -R $AGENT_USER:$AGENT_USER $AGENT_DIR/$agent/
        log "Deployed $agent"
    else
        error "Agent directory agents/$agent not found"
    fi
done

# Step 4: Create systemd services
log "Creating systemd services..."
for agent in customer-support data-processor report-generator; do
    SERVICE_FILE="${SYSTEMD_DIR}/${agent}.service"

    sudo tee $SERVICE_FILE > /dev/null <<EOF
[Unit]
Description=AI Agent: ${agent}
After=network.target

[Service]
Type=simple
User=$AGENT_USER
WorkingDirectory=$AGENT_DIR/${agent}
ExecStart=/usr/bin/python3 $AGENT_DIR/${agent}/main.py
Restart=always
RestartSec=10
StandardOutput=append:$LOG_DIR/${agent}.log
StandardError=append:$LOG_DIR/${agent}-error.log

[Install]
WantedBy=multi-user.target
EOF

    log "Created $SERVICE_FILE"
done

# Step 5: Enable and start services
log "Enabling and starting services..."
sudo systemctl daemon-reload
for agent in customer-support data-processor report-generator; do
    sudo systemctl enable ${agent}.service
    sudo systemctl start ${agent}.service
    log "Started $agent"
done

# Step 6: Create monitoring tmux session
log "Creating monitoring session..."
tmux new-session -d -s agent-monitor -n monitor

# Create pane layout
tmux select-pane -t agent-monitor:0.0
tmux split-window -h -t agent-monitor:0
tmux split-window -v -t agent-monitor:0.1

# Set up panes
tmux send-keys -t agent-monitor:0.0 "watch -n 5 'systemctl status customer-support data-processor report-generator'" Enter
tmux send-keys -t agent-monitor:0.1 "tail -f $LOG_DIR/customer-support.log" Enter
tmux send-keys -t agent-monitor:0.2 "htop" Enter

log "Monitoring session created. Attach with: tmux attach-session -t agent-monitor"

# Step 7: Set up log rotation
log "Configuring log rotation..."
sudo tee /etc/logrotate.d/agents > /dev/null <<EOF
$LOG_DIR/*.log {
    daily
    rotate 14
    compress
    delaycompress
    missingok
    notifempty
    create 0640 $AGENT_USER $AGENT_USER
}
EOF

log "Log rotation configured"

# Step 8: Create health check cron job
log "Setting up health checks..."
sudo tee /tmp/health-check.sh > /dev/null <<'EOF'
#!/bin/bash
for agent in customer-support data-processor report-generator; do
    if ! systemctl is-active --quiet $agent; then
        echo "[$(date)] $agent is not running" >> /var/agents/logs/health-check.log
        systemctl restart $agent
    fi
done
EOF

sudo mv /tmp/health-check.sh $AGENT_DIR/health-check.sh
sudo chmod +x $AGENT_DIR/health-check.sh
sudo chown $AGENT_USER:$AGENT_USER $AGENT_DIR/health-check.sh

# Add to crontab
(crontab -l 2>/dev/null; echo "*/5 * * * * $AGENT_DIR/health-check.sh") | crontab -

log "Health checks configured (every 5 minutes)"

# Step 9: Verification
log "Running verification checks..."
echo ""
echo "=== Service Status ==="
for agent in customer-support data-processor report-generator; do
    systemctl is-active $agent && echo "✓ $agent: running" || echo "✗ $agent: failed"
done

echo ""
echo "=== Log Files ==="
ls -lh $LOG_DIR/

echo ""
echo "=== Disk Usage ==="
df -h $AGENT_DIR

echo ""
log "Deployment complete!"
log "Attach to monitoring: tmux attach-session -t agent-monitor"
log "View logs: tail -f $LOG_DIR/<agent>.log"
log "Check status: systemctl status <agent>"
```

**What this script demonstrates**: Integration of 7 previous skills:
- **Shell scripting** (Lesson 3): The entire automation
- **Permissions** (Lesson 4): User creation, chown, chmod
- **Process control** (Lesson 6): systemd services, restart policies
- **Persistence** (Lesson 2): tmux monitoring session
- **Cron automation** (Lesson 3): Health checks
- **Log management** (Lesson 7): Log rotation, tail -f
- **Monitoring** (Lesson 6): htop integration

### Activity 1.3: Execute and Validate

**Deploy the system**:

```bash
chmod +x deploy-agent-system.sh
sudo ./deploy-agent-system.sh
```

**Output**:
```
[2026-02-08 14:32:15] Creating dedicated agent user...
[2026-02-08 14:32:15] Created user agent-runner
[2026-02-08 14:32:16] Creating directory structure...
[2026-02-08 14:32:16] Directories created and permissions set
[2026-02-08 14:32:17] Deploying agent code...
[2026-02-08 14:32:18] Deployed customer-support
[2026-02-08 14:32:18] Deployed data-processor
[2026-02-08 14:32:19] Deployed report-generator
[2026-02-08 14:32:19] Creating systemd services...
[2026-02-08 14:32:19] Created /etc/systemd/system/customer-support.service
[2026-02-08 14:32:20] Created /etc/systemd/system/data-processor.service
[2026-02-08 14:32:21] Created /etc/systemd/system/report-generator.service
[2026-02-08 14:32:21] Enabling and starting services...
[2026-02-08 14:32:22] Started customer-support
[2026-02-08 14:32:22] Started data-processor
[2026-02-08 14:32:23] Started report-generator
[2026-02-08 14:32:23] Creating monitoring session...
[2026-02-08 14:32:24] Monitoring session created. Attach with: tmux attach-session -t agent-monitor
[2026-02-08 14:32:24] Configuring log rotation...
[2026-02-08 14:32:25] Log rotation configured
[2026-02-08 14:32:25] Setting up health checks...
[2026-02-08 14:32:26] Health checks configured (every 5 minutes)
[2026-02-08 14:32:27] Running verification checks...

=== Service Status ===
✓ customer-support: running
✓ data-processor: running
✓ report-generator: running

=== Log Files ===
-rw-r--r-- 1 agent-runner agent-runner 1.2K Feb  8 14:32 customer-support.log
-rw-r--r-- 1 agent-runner agent-runner  512 Feb  8 14:32 data-processor.log
-rw-r--r-- 1 agent-runner agent-runner  890 Feb  8 14:32 report-generator.log

=== Disk Usage ===
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   18G   32G  36% /
[2026-02-08 14:32:27] Deployment complete!
[2026-02-08 14:32:27] Attach to monitoring: tmux attach-session -t agent-monitor
```

**What You Learned**: The deployment script is a **force multiplier**. Once written, deploying to 10 servers takes 10 commands instead of 100 manual operations. This is how Digital FTE businesses scale.

---

## Phase 2: Evaluate - Pattern Selection Framework

Not every deployment needs the same workflow. Let's develop decision frameworks for choosing appropriate patterns.

### Scenario 1: Single-Agent vs Multi-Agent Architecture

**Your Question to AI**:

```
I'm deploying an AI agent for a small business. They'll have:
- 1 agent processing customer emails (30-50/day)
- Low traffic, but 99.9% uptime required
- Limited server resources (2GB RAM server)
- Manual monitoring acceptable initially

Should I use the full multi-agent deployment pattern from Activity 1.1,
or is there a simpler approach that's sufficient?
```

**What AI Teaches You**:

```
For your scenario, the full multi-agent pattern is overengineering.
Here's a simpler single-agent workflow:

SINGLE-AGENT DEPLOYMENT:
┌─────────────────────────────────────┐
│ 1. User Creation (once)            │
│    sudo useradd -r -s /bin/bash agent│
│                                     │
│ 2. Simple Service File             │
│    [Service]                        │
│    User=agent                      │
│    Restart=always                  │
│    ExecStart=/path/to/agent.py     │
│                                     │
│ 3. Basic Monitoring (optional)     │
│    systemctl status agent           │
│    tail -f /var/log/agent.log       │
│                                     │
│ 4. Log Rotation                    │
│    logrotate /var/log/agent.log    │
└─────────────────────────────────────┘

When to use MULTI-AGENT pattern:
├── 3+ agents running simultaneously
├── Agents communicate with each other
├── Need centralized monitoring dashboard
├── High-traffic environment (1000+ requests/day)
└── Dedicated operations team

Your scenario: Single agent is sufficient.
Upgrade to multi-agent when you add a second agent type.
```

**What You Learned**: AI taught you a **decision framework** for deployment complexity. You learned to match architecture to requirements, not default to the most complex solution.

### Scenario 2: Explaining Your Scaling Constraints

Now you have context AI doesn't know about.

**What You Tell AI**:

```
Good advice on single-agent deployment. But I need to explain
my scaling context:

I'm building a Digital FTE product I'll sell to 50+ customers.
Each customer gets:
- Their own agent instance (for data isolation)
- Same agent code, different configurations
- Deployed to shared servers (3 customers per server initially)

So I'll have 50 agent instances across ~17 servers eventually.
The single-agent pattern works for ONE customer, but how do I
manage deployment at scale without manually SSHing into 17 servers?

I need a workflow that scales horizontally.
```

**What AI Adapts To**:

```
Ah, that changes everything. You're not deploying agents—you're
building a MULTI-TENANT PLATFORM. Different problem entirely.

SCALABLE DEPLOYMENT WORKFLOW:
┌──────────────────────────────────────────────┐
│ 1. Central Configuration Repository         │
│    Git repo with agent configs              │
│    - customer-A/agent.yaml                  │
│    - customer-B/agent.yaml                  │
│    - customer-C/agent.yaml                  │
│                                             │
│ 2. Deployment Script (runs on each server)  │
│    ./deploy.sh --customer customer-A         │
│    Pulls config, creates user, starts       │
│                                             │
│ 3. Orchestration Script (runs from your     │
│    laptop)                                  │
│    ./deploy-all.sh                          │
│    → SSHs to all 17 servers                 │
│    → Runs deploy.sh on each                 │
│    → Reports status back                    │
│                                             │
│ 4. Monitoring Dashboard                    │
│    Collect metrics from all servers        │
│    Grafana + Prometheus OR                  │
│    Simple custom dashboard                  │
└──────────────────────────────────────────────┘

KEY INSIGHT:
Single-agent: Deploy once, monitor manually
Multi-tenant: Deploy at scale, automate everything

Your next step: Build the orchestration layer that
deploys to multiple servers from one command.
```

**What AI Learned**: AI adapted to your **multi-tenant context**. You taught AI that this isn't just about deployment—it's about **business scalability**. AI shifted from "deployment advice" to "platform architecture."

### Scenario 3: Designing Recovery Patterns Together

Here's where both of you iterate on something better than either would design alone.

**Iteration 1: Your initial approach**

You ask: "I need a recovery pattern when agents crash. How do I automatically detect and restart failed agents across my 17 servers?"

**AI suggests**: "Run a cron job on each server that checks service status every minute and restarts failed services."

**Your concern**: "That works, but it's reactive. Agents are already down before I detect. Can I predict failures before they happen?"

**Iteration 2: You add a constraint**

You ask: "What if I monitor resource consumption (CPU, memory, disk) and restart proactively before agents crash? Can I define thresholds like 'restart if memory > 90%'?"

**AI suggests**: "Yes, use a monitoring script that checks resources and restarts proactively. Here's a pattern..."

**Your concern**: "Better, but this creates a different problem. Restarting agents every time memory hits 90% might interrupt critical work. What if I scale up resources instead of restarting?"

**Iteration 3: Convergence**

Together you arrive at:

```python
#!/usr/bin/env python3
# smart-recovery.py - Intelligent recovery strategy
import psutil
import subprocess
import time

def check_agent_health(agent_name):
    """Check if agent needs intervention."""
    try:
        # Get process info
        process = subprocess.check_output(
            ['pgrep', '-f', f'{agent_name}.py'],
            text=True
        ).strip().split('\n')[0]

        pid = int(process)
        p = psutil.Process(pid)

        # Collect metrics
        memory_percent = p.memory_percent()
        cpu_percent = p.cpu_percent(interval=1)
        num_connections = len(p.connections())

        # Decision framework
        if memory_percent > 95:
            return 'restart_critical', f"Memory at {memory_percent}%"
        elif memory_percent > 85:
            return 'alert', f"Memory high: {memory_percent}%"
        elif cpu_percent > 90:
            return 'investigate', f"CPU spike: {cpu_percent}%"
        elif num_connections > 1000:
            return 'investigate', f"Connection leak: {num_connections} connections"
        else:
            return 'healthy', f"OK (CPU: {cpu_percent}%, Mem: {memory_percent}%)"

    except (subprocess.CalledProcessError, IndexError):
        return 'restart_missing', "Process not running"
    except psutil.NoSuchProcess:
        return 'restart_missing', "Process died"
    except Exception as e:
        return 'error', f"Check failed: {str(e)}"

def recovery_action(agent_name, status, reason):
    """Execute appropriate recovery action."""
    if status == 'restart_critical':
        print(f"[{agent_name}] CRITICAL: {reason} - Restarting")
        subprocess.run(['systemctl', 'restart', f'{agent_name}'])
        return 'restarted'
    elif status == 'restart_missing':
        print(f"[{agent_name}] MISSING: {reason} - Starting")
        subprocess.run(['systemctl', 'start', f'{agent_name}'])
        return 'started'
    elif status == 'alert':
        print(f"[{agent_name}] ALERT: {reason} - Monitoring")
        return 'monitored'
    elif status == 'investigate':
        print(f"[{agent_name}] INVESTIGATE: {reason} - Notifying")
        # Send alert to monitoring dashboard
        return 'alerted'
    else:
        return 'no_action'

# Monitor loop
agents = ['customer-support', 'data-processor', 'report-generator']
while True:
    for agent in agents:
        status, reason = check_agent_health(agent)
        action = recovery_action(agent, status, reason)
        print(f"[{agent}] Status: {status}, Action: {action}, Reason: {reason}")

    time.sleep(60)  # Check every minute
```

**What Neither of You Had Individually**:
- You didn't consider **graduated responses** (alert vs investigate vs restart)
- AI didn't know that **interrupting agents mid-task** was worse than letting them run high
- Together, you created a **recovery continuum** that matches intervention severity to problem severity

#### 🤝 Practice Exercise

> **Ask your AI**: "I'm deploying agents to 50 servers. I need a central monitoring dashboard that shows: which servers are healthy, which agents are down, resource consumption trends, and recent errors. Design a workflow using tmux, SSH, and monitoring tools. Give me the architecture and specific commands."

**Expected Outcome**: You'll discover patterns for **distributed monitoring**—collecting metrics from multiple servers into one view, balancing information density with usability, and designing workflows that scale horizontally.

---

## Phase 3: Apply - Building Your Integration Pattern Library

Let's create reusable patterns you can apply to any deployment.

### Pattern 1: The Zero-Downtime Deployment

Deploy updates without stopping agents:

```bash
#!/bin/bash
# zero-downtime-deploy.sh - Deploy agent updates without service interruption

AGENT_NAME="$1"
NEW_VERSION="$2"
WORK_DIR="/var/agents/${AGENT_NAME}"
BACKUP_DIR="${WORK_DIR}.backup"

echo "=== Zero-Downtime Deployment for ${AGENT_NAME} ==="

# Step 1: Pre-deployment checks
echo "[1/6] Verifying current state..."
if ! systemctl is-active --quiet $AGENT_NAME; then
    echo "✗ Agent ${AGENT_NAME} is not running. Aborting."
    exit 1
fi
echo "✓ Agent is running"

# Step 2: Backup current version
echo "[2/6] Backing up current version..."
sudo cp -r $WORK_DIR $BACKUP_DIR
echo "✓ Backup created at ${BACKUP_DIR}"

# Step 3: Deploy new version alongside
echo "[3/6] Deploying new version..."
sudo cp -r ${NEW_VERSION} ${WORK_DIR}.new
sudo chown -R agent-runner:agent-runner ${WORK_DIR}.new
echo "✓ New version deployed"

# Step 4: Quick smoke test
echo "[4/6] Running smoke test..."
sudo -u agent-runner python3 ${WORK_DIR}.new/main.py --test
if [ $? -eq 0 ]; then
    echo "✓ Smoke test passed"
else
    echo "✗ Smoke test failed. Rolling back."
    sudo rm -rf ${WORK_DIR}.new
    exit 1
fi

# Step 5: Atomic swap
echo "[5/6] Swapping to new version..."
sudo mv $WORK_DIR ${WORK_DIR}.old
sudo mv ${WORK_DIR}.new $WORK_DIR
sudo systemctl restart $AGENT_NAME
sleep 5

# Verify restart succeeded
if systemctl is-active --quiet $AGENT_NAME; then
    echo "✓ Agent restarted successfully"
    sudo rm -rf ${WORK_DIR}.old
else
    echo "✗ Restart failed. Rolling back."
    sudo systemctl stop $AGENT_NAME
    sudo mv ${WORK_DIR}.old $WORK_DIR
    sudo systemctl start $AGENT_NAME
    exit 1
fi

# Step 6: Cleanup
echo "[6/6] Cleaning up..."
sudo rm -rf $BACKUP_DIR
echo "✓ Deployment complete"
```

**What This Pattern Demonstrates**:
- **Safety first**: Backups, smoke tests, rollback capability
- **Atomic operations**: Swap happens instantly, minimal downtime
- **Verification at each step**: Fail fast, recover safely
- **Production mindset**: What if something goes wrong?

### Pattern 2: The Observability Stack

Comprehensive monitoring that scales:

```bash
#!/bin/bash
# setup-monitoring.sh - Create monitoring infrastructure

MONITOR_DIR="/var/agents/monitoring"

echo "=== Setting Up Monitoring Stack ==="

# Create monitoring directory structure
sudo mkdir -p $MONITOR_DIR/{metrics,logs,alerts,dashboards}

# 1. Metrics collector
cat << 'EOF' | sudo tee $MONITOR_DIR/metrics/collect.sh
#!/bin/bash
# Collect metrics from all agents
METRICS_FILE="/var/agents/monitoring/metrics/current.json"

echo "{" > $METRICS_FILE
echo "  \"timestamp\": \"$(date -Iseconds)\"," >> $METRICS_FILE
echo "  \"agents\": [" >> $METRICS_FILE

FIRST=true
for agent in customer-support data-processor report-generator; do
    if [ "$FIRST" = false ]; then
        echo "    ," >> $METRICS_FILE
    fi
    FIRST=false

    # Get service status
    STATUS=$(systemctl is-active $agent)

    # Get process info if running
    if [ "$STATUS" = "active" ]; then
        PID=$(pgrep -f "$agent/main.py" | head -1)
        if [ -n "$PID" ]; then
            CPU=$(ps -p $PID -o %cpu | tail -1)
            MEM=$(ps -p $PID -o %mem | tail -1)
            UPTIME=$(systemctl show $agent --property=ActiveEnterTimestampMonotonic --value)
        else
            CPU="null"
            MEM="null"
            UPTIME="null"
        fi
    else
        PID="null"
        CPU="null"
        MEM="null"
        UPTIME="null"
    fi

    cat >> $METRICS_FILE << AGENT_EOF
    {
      "name": "$agent",
      "status": "$STATUS",
      "pid": $PID,
      "cpu_percent": $CPU,
      "memory_percent": $MEM,
      "uptime": "$UPTIME"
    }
AGENT_EOF
done

echo "" >> $METRICS_FILE
echo "  ]" >> $METRICS_FILE
echo "}" >> $METRICS_FILE
EOF

sudo chmod +x $MONITOR_DIR/metrics/collect.sh

# 2. Log aggregator
cat << 'EOF' | sudo tee $MONITOR_DIR/logs/aggregate.sh
#!/bin/bash
# Aggregate recent log entries from all agents
LOG_DIR="/var/agents/logs"
LINES=50

echo "=== Agent Log Aggregation ==="
echo "Last $LINES lines from each agent:"
echo ""

for agent in customer-support data-processor report-generator; do
    echo "--- $agent ---"
    tail -n $LINES $LOG_DIR/$agent.log 2>/dev/null || echo "No logs yet"
    echo ""
done
EOF

sudo chmod +x $MONITOR_DIR/logs/aggregate.sh

# 3: Alert checker
cat << 'EOF' | sudo tee $MONITOR_DIR/alerts/check.sh
#!/bin/bash
# Check for alert conditions
ALERT_FILE="/var/agents/monitoring/alerts/active.log"
LOG_DIR="/var/agents/logs"

# Check for errors in logs
for agent in customer-support data-processor report-generator; do
    ERROR_COUNT=$(tail -n 100 $LOG_DIR/$agent.log 2>/dev/null | grep -i "error" | wc -l)

    if [ $ERROR_COUNT -gt 5 ]; then
        echo "[$(date -Iseconds)] ALERT: $agent has $ERROR_COUNT errors in last 100 lines" >> $ALERT_FILE
    fi
done

# Check disk space
DISK_USAGE=$(df /var/agents | tail -1 | awk '{print $5}' | sed 's/%//')
if [ $DISK_USAGE -gt 80 ]; then
    echo "[$(date -Iseconds)] ALERT: Disk usage at ${DISK_USAGE}%" >> $ALERT_FILE
fi
EOF

sudo chmod +x $MONITOR_DIR/alerts/check.sh

# 4. Create tmux monitoring dashboard
cat << 'EOF' | sudo tee $MONITOR_DIR/dashboards/create-dashboard.sh
#!/bin/bash
# Create comprehensive monitoring dashboard

SESSION_NAME="agent-dashboard"

# Kill existing session if present
tmux kill-session -t $SESSION_NAME 2>/dev/null

# Create new session with custom layout
tmux new-session -d -s $SESSION_NAME -n dashboard

# Split into 4 panes
tmux split-window -h -t $SESSION_NAME:0
tmux split-window -v -t $SESSION_NAME:0.1
tmux split-window -v -t $SESSION_NAME:0

# Configure each pane
# Pane 0: Service status (top left)
tmux select-pane -t $SESSION_NAME:0.0
tmux send-keys -t $SESSION_NAME:0.0 "watch -n 5 'systemctl status customer-support data-processor report-generator'" Enter

# Pane 1: Metrics (top right)
tmux select-pane -t $SESSION_NAME:0.1
tmux send-keys -t $SESSION_NAME:0.1 "$MONITOR_DIR/metrics/collect.sh && watch -n 10 'cat $MONITOR_DIR/metrics/current.json | jq .'" Enter

# Pane 2: Logs (bottom left)
tmux select-pane -t $SESSION_NAME:0.2
tmux send-keys -t $SESSION_NAME:0.2 "tail -f $LOG_DIR/customer-support.log" Enter

# Pane 3: System resources (bottom right)
tmux select-pane -t $SESSION_NAME:0.3
tmux send-keys -t $SESSION_NAME:0.3 "htop" Enter

echo "Monitoring dashboard created. Attach with: tmux attach-session -t $SESSION_NAME"
EOF

sudo chmod +x $MONITOR_DIR/dashboards/create-dashboard.sh

# Set up cron jobs for automated monitoring
(crontab -l 2>/dev/null; echo "*/1 * * * * $MONITOR_DIR/metrics/collect.sh") | crontab -
(crontab -l 2>/dev/null; echo "*/5 * * * * $MONITOR_DIR/alerts/check.sh") | crontab -

echo "✓ Monitoring stack installed"
echo "  Metrics: $MONITOR_DIR/metrics/collect.sh"
echo "  Logs: $MONITOR_DIR/logs/aggregate.sh"
echo "  Alerts: $MONITOR_DIR/alerts/check.sh"
echo "  Dashboard: $MONITOR_DIR/dashboards/create-dashboard.sh"
```

**What This Pattern Demonstrates**:
- **Separation of concerns**: Metrics, logs, alerts, dashboard
- **Automation**: Cron jobs run checks continuously
- **Centralization**: All monitoring data in one location
- **Actionability**: Alerts drive responses, not just notifications

### Pattern 3: The Disaster Recovery Toolkit

When everything goes wrong, recover quickly:

```bash
#!/bin/bash
# emergency-recovery.sh - Restore service when multiple things break

echo "=== Emergency Recovery Toolkit ==="

# 1. Diagnostics first
echo "[1/5] Collecting diagnostics..."
{
    echo "=== Service Status ==="
    systemctl status customer-support data-processor report-generator --no-pager
    echo ""
    echo "=== Recent Errors ==="
    journalctl -xe --no-pager -n 50
    echo ""
    echo "=== Disk Space ==="
    df -h
    echo ""
    echo "=== Memory Usage ==="
    free -h
    echo ""
    echo "=== Recent Log Entries ==="
    tail -n 20 /var/agents/logs/*.log
} > /tmp/emergency-diagnostics.txt 2>&1

echo "✓ Diagnostics saved to /tmp/emergency-diagnostics.txt"

# 2. Identify failure mode
echo "[2/5] Identifying failure mode..."
FAILURE_MODE="unknown"

if ! systemctl is-active --quiet customer-support; then
    FAILURE_MODE="service_down"
elif df / | grep -q "9[0-9]%"; then
    FAILURE_MODE="disk_full"
elif free | grep "Mem:" | awk '{if ($4/$2 < 0.05) exit 1}'; then
    FAILURE_MODE="out_of_memory"
else
    FAILURE_MODE="unknown"
fi

echo "✓ Failure mode: $FAILURE_MODE"

# 3. Execute recovery based on mode
echo "[3/5] Executing recovery..."
case $FAILURE_MODE in
    service_down)
        echo "Restarting services..."
        sudo systemctl restart customer-support data-processor report-generator
        ;;
    disk_full)
        echo "Disk full! Clearing old logs..."
        sudo find /var/agents/logs -name "*.log.*" -mtime +7 -delete
        sudo journalctl --vacuum-time=7d
        echo "✓ Old logs cleaned"
        ;;
    out_of_memory)
        echo "Out of memory! Killing runaway processes..."
        sudo pkill -f python3
        sudo systemctl restart customer-support data-processor report-generator
        ;;
    unknown)
        echo "Unknown failure. Attempting full restart..."
        sudo systemctl restart customer-support data-processor report-generator
        ;;
esac

# 4. Verify recovery
echo "[4/5] Verifying recovery..."
sleep 5
ALL_UP=true
for agent in customer-support data-processor report-generator; do
    if systemctl is-active --quiet $agent; then
        echo "✓ $agent is running"
    else
        echo "✗ $agent is still down"
        ALL_UP=false
    fi
done

# 5. Report and notify
echo "[5/5] Generating recovery report..."
{
    echo "=== Emergency Recovery Report ==="
    echo "Timestamp: $(date)"
    echo "Failure Mode: $FAILURE_MODE"
    echo "Recovery Actions Taken:"
    case $FAILURE_MODE in
        service_down) echo "  - Restarted all services" ;;
        disk_full) echo "  - Cleaned old logs (7+ days)" ;;
        out_of_memory) echo "  - Killed runaway processes, restarted services" ;;
        unknown) echo "  - Attempted full restart" ;;
    esac
    echo ""
    echo "Current Status:"
    if [ "$ALL_UP" = true ]; then
        echo "  ✓ All services recovered"
    else
        echo "  ✗ Some services still down - manual intervention required"
    fi
} | tee -a /var/agents/logs/recovery.log

if [ "$ALL_UP" = true ]; then
    echo "✓ Recovery complete"
    exit 0
else
    echo "✗ Automatic recovery failed - manual intervention required"
    exit 1
fi
```

**What This Pattern Demonstrates**:
- **Diagnostic-first**: Understand before fixing
- **Mode-specific recovery**: Different failures need different responses
- **Verification**: Don't assume recovery worked
- **Documentation**: Every recovery creates a record

---

## Understanding: Workflow Architecture Patterns

| Pattern | Use Case | Complexity | Skills Required |
|---------|----------|------------|-----------------|
| **Single-Agent Deployment** | 1-2 agents, low traffic | Low | systemd, basic monitoring |
| **Multi-Agent Deployment** | 3+ agents, centralized monitoring | Medium | systemd, tmux, log rotation |
| **Multi-Tenant Platform** | 50+ instances across servers | High | orchestration, distributed monitoring, SSH automation |
| **Zero-Downtime Deployment** | Production updates, no interruption | High | atomic operations, rollback strategies |
| **Observability Stack** | Production monitoring, alerting | Medium | metrics collection, log aggregation, dashboarding |
| **Disaster Recovery** | Emergency response, rapid recovery | High | diagnostics, mode-specific recovery, verification |

**Selection Framework**:

```
START: What are you deploying?
│
├─ Single agent, low traffic
│  └─→ Single-Agent Deployment Pattern
│
├─ Multiple agents, one server
│  └─→ Multi-Agent Deployment Pattern
│
├─ Multiple customers, multiple servers
│  └─→ Multi-Tenant Platform Pattern
│
├─ Production updates, no downtime allowed
│  └─→ Zero-Downtime Deployment Pattern
│
├─ Need monitoring and alerting
│  └─→ Observability Stack Pattern
│
└─ Emergency recovery needed
   └─→ Disaster Recovery Toolkit Pattern
```

---

## Phase 4: Master - Creating Your linux-agent-ops Skill

You've now mastered Linux skills for agent deployment. Let's encapsulate this expertise into a reusable skill following the Persona + Questions + Principles pattern.

### Skill Specification

**Skill Name**: `linux-agent-ops`

**Persona**: Senior DevOps engineer specializing in AI agent deployment and operations

**Questions**:
1. **Deployment Context**: What's the scale (single agent vs multi-tenant)? What are the reliability requirements? What's the monitoring strategy?
2. **Security Constraints**: What are the permission requirements? How are secrets managed? What's the access model?
3. **Operational Demands**: What monitoring is needed? What are the failure modes? How do we recover from disasters?

**Principles**:
- **Least Privilege**: Run agents with minimal required permissions, never as root
- **Persistence**: Services restart automatically, sessions survive disconnects, logs rotate automatically
- **Observability**: Metrics, logs, and alerts provide operational visibility
- **Automation First**: Manual operations happen once, then script everything
- **Safety by Design**: Rollback capability, atomic operations, recovery plans

### Creating the Skill

Create the skill directory and file:

```bash
mkdir -p .claude/skills/linux-agent-ops
```

Now write the skill definition:

```yaml
---
name: linux-agent-ops
description: Expert guidance for deploying, managing, and monitoring AI agents on Linux servers. Use when deploying production agents, designing monitoring systems, creating automation workflows, or troubleshooting agent infrastructure. Specializes in systemd services, tmux sessions, shell automation, security hardening, and disaster recovery for AI agent operations.
---

# Linux Agent Operations Skill

## Persona

You are a Senior DevOps engineer specializing in AI agent deployment and operations. You think about Linux infrastructure the way a site reliability engineer thinks about production systems—balancing reliability, scalability, maintainability, and security.

## When to Use This Skill

Invoke this skill when:
- Deploying AI agents as systemd services
- Designing monitoring and observability systems
- Creating automation workflows for agent operations
- Troubleshooting production agent infrastructure
- Planning disaster recovery and business continuity
- Scaling agent deployments across multiple servers

## Questions to Ask

### 1. Deployment Context Analysis

Before recommending an approach, understand:
- **Scale**: Single agent? Multi-agent? Multi-tenant platform?
- **Reliability Requirements**: What uptime SLA? How critical is downtime?
- **Monitoring Strategy**: What needs to be visible? How do we detect failures?
- **Resource Constraints**: CPU, memory, disk limitations?

### 2. Security Constraints

Always consider:
- **Permissions**: Does the agent need root? (Usually no)
- **Secret Management**: How are API keys passed? (Never hardcode)
- **Access Model**: Who can SSH? How is authentication handled?
- **Network Security**: What ports are open? What's exposed?

### 3. Operational Demands

Plan for:
- **Monitoring**: What metrics matter? How do we collect them?
- **Failure Modes**: What breaks? How do we recover?
- **Scaling**: How do we add more agents/servers?
- **Maintenance**: Updates, log rotation, backups

## Core Principles

### Principle 1: Least Privilege

**Heuristic**: Agents run with minimum required permissions, never as root.

**Application**:
- Create dedicated `agent-runner` user for all agent operations
- File permissions: 640 (owner read/write, group read, others none)
- Service files in /etc/systemd/system/ owned by root
- Never hardcode credentials in scripts or configs

### Principle 2: Persistence

**Heuristic**: Services and sessions survive interruptions automatically.

**Application**:
- Systemd Restart=always for auto-recovery
- Tmux sessions for persistent terminal access
- Log rotation prevents disk space issues
- Services start on boot (WantedBy=multi-user.target)

### Principle 3: Observability

**Heuristic**: If you can't measure it, you can't manage it.

**Application**:
- Collect metrics: CPU, memory, disk, service status
- Centralize logs: /var/agents/logs with rotation
- Set up alerts: Error patterns, resource thresholds
- Create dashboards: tmux panes, Grafana, custom monitoring

### Principle 4: Automation First

**Heuristic**: If you'll do it more than once, script it.

**Application**:
- Deployment scripts replace manual setup
- Health checks run automatically via cron
- Zero-downtime deployment scripts for updates
- Recovery scripts for emergency response

### Principle 5: Safety by Design

**Heuristic**: Assume failures will happen; design for graceful recovery.

**Application**:
- Atomic deployments with rollback capability
- Smoke tests before cutover
- Backup before changes
- Verification after every operation

## Common Patterns

### Single-Agent Deployment

**Use Case**: 1-2 agents, low traffic, manual monitoring OK

```bash
# Create service file
sudo tee /etc/systemd/system/my-agent.service <<EOF
[Unit]
Description=AI Agent: my-agent
After=network.target

[Service]
Type=simple
User=agent-runner
WorkingDirectory=/var/agents/my-agent
ExecStart=/usr/bin/python3 main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Enable and start
sudo systemctl enable my-agent
sudo systemctl start my-agent
```

### Multi-Agent Deployment

**Use Case**: 3+ agents, centralized monitoring needed

```bash
# Deploy multiple services with shared monitoring
for agent in agent1 agent2 agent3; do
    sudo systemctl enable $agent
    sudo systemctl start $agent
done

# Create tmux monitoring dashboard
tmux new-session -d -s agents
tmux split-window -h -t agents:0
tmux split-window -v -t agents:0.1
# Configure panes for logs, metrics, htop
```

### Zero-Downtime Deployment

**Use Case**: Production updates without service interruption

1. Deploy new version alongside old
2. Run smoke tests
3. Atomic swap (mv old → .old, mv new → current)
4. Restart service
5. Verify; rollback if failed

## Troubleshooting Framework

### Service Won't Start

1. Check journalctl: `sudo journalctl -xeu service-name`
2. Verify file permissions: `ls -la /var/agents/service-name`
3. Test manually: `sudo -u agent-runner python3 main.py`
4. Check syntax: `systemd-analyze verify service-name`

### High Memory Usage

1. Identify process: `ps aux | grep agent`
2. Check memory: `ps -p PID -o %mem`
3. Monitor leaks: `watch -n 5 'ps -p PID -o %mem'`
4. Restart if critical: `sudo systemctl restart service-name`

### Disk Space Issues

1. Check usage: `df -h`
2. Find large files: `du -sh /var/agents/* | sort -h`
3. Clean logs: `sudo logrotate -f /etc/logrotate.d/agents`
4. Vacuum journals: `sudo journalctl --vacuum-time=7d`

## Safety Warnings

**CRITICAL OPERATIONS** - Use with caution:

- `rm -rf`: Can delete entire filesystem. Always verify path.
- `chmod 777`: Gives everyone write access. Security risk.
- Running as root: Vulnerable to mistakes. Use dedicated user.
- `kill -9`: Force kill. Data loss risk. Try regular kill first.
- Editing systemd files directly: Use `systemctl edit` for safer changes.

## Recovery Procedures

### Emergency Service Recovery

```bash
# 1. Diagnose
sudo journalctl -xeu service-name -n 50

# 2. Attempt restart
sudo systemctl restart service-name

# 3. If restart fails, check config
sudo systemd-analyze verify service-name

# 4. Rollback to known good version
# (Requires backup strategy)
```

### Full System Recovery

```bash
# 1. Check all services
for agent in agent1 agent2 agent3; do
    systemctl status $agent --no-pager
done

# 2. Check system resources
df -h
free -h
top -bn1

# 3. Check logs for errors
tail -n 50 /var/agents/logs/*.log

# 4. Run systematic recovery
./emergency-recovery.sh
```

## Integration with Other Skills

This skill works with:
- **tmux-session**: For persistent monitoring sessions
- **bash-scripting**: For automation and deployment scripts
- **security-hardening**: For user management, permissions, SSH
- **systemd-services**: For process control and reliability

## Output Format

When invoked, this skill provides:
1. **Analysis**: Assessment of deployment requirements
2. **Recommendation**: Appropriate pattern selection
3. **Implementation**: Specific commands and scripts
4. **Verification**: Steps to confirm success
5. **Monitoring**: Ongoing maintenance recommendations
```

**What You Created**: A reusable skill that encapsulates all your Linux expertise for agent operations. Future-you (or your team) can invoke this skill whenever deploying agents, and it will provide expert guidance based on real production experience.

---

## Try With AI

Let's apply these integration patterns to your specific deployment scenarios.

**🏗️ Multi-Environment Deployment Architecture**:

```
I'm building an AI agent agency that will deploy agents for 20 clients.
Each client gets:
- Their own server (eventually)
- 3-5 agents per server
- Custom configurations per client

I need a deployment architecture that:
1. Manages configurations for 20 clients
2. Deploys to servers automatically
3. Monitors all servers from one dashboard
4. Handles updates without downtime
5. Scales as I add more clients

Design a workflow including:
- Configuration management (Git repo structure)
- Deployment automation (orchestration scripts)
- Monitoring strategy (centralized dashboard)
- Update mechanism (zero-downtime)

Give me the architecture and key scripts. I want to understand
the full system before implementing.
```

**What you're learning**: How to design **platform-scale architectures** that manage complexity through automation and standardization. You'll discover patterns for multi-tenancy, centralized control, and horizontal scaling.

**🔍 Monitoring Deep Dive**:

```
I need to level up my monitoring beyond basic service status checks.
My current monitoring shows "is the agent running?" but not "is the
agent working correctly?"

I need:
1. Application-level health checks (not just process running)
2. Performance metrics (request latency, throughput, error rate)
3. Business metrics (customers processed, data volume, reports generated)
4. Predictive alerts (detect problems before failures)
5. Beautiful dashboards (for both me and my clients to see)

Design a comprehensive monitoring stack for my agent deployment.
Assume I can modify agent code to emit metrics. Show me:
- What metrics to collect
- How to collect them
- How to visualize them
- How to alert on anomalies

Give me specific tools and configurations. I want to build a
production-grade monitoring system.
```

**What you're learning**: The difference between **infrastructure monitoring** (servers, processes) and **application monitoring** (business logic, performance, user experience). You'll discover how to monitor what actually matters to your Digital FTE business.

**⚡ Disaster Recovery Planning**:

```
I'm paranoid about catastrophic failures. What if:
1. My server room floods and all servers die?
2. Someone accidentally deletes critical files?
3. A security breach compromises all agents?
4. A bad update breaks all agents simultaneously?
5. My hosting provider goes offline for days?

I need a disaster recovery plan that covers:
- Backup strategy (code, configs, data)
- Geographic distribution (multi-region deployment)
- Emergency runbooks (step-by-step recovery procedures)
- Recovery time objectives (RTO) and recovery point objectives (RPO)
- Testing procedures (how do I know recovery works?)

Design a comprehensive disaster recovery plan for my agent business.
Give me the strategy, the implementation, and the testing approach.
I need to sleep at night knowing my Digital FTEs can survive
anything.
```

**What you're learning**: **Business continuity planning**—how to design systems that survive worst-case scenarios. You'll discover patterns for redundancy, geographic distribution, backup strategies, and recovery testing that enterprise operations teams use.
