---
sidebar_position: 9
title: "Capstone: Production Digital FTE Deployment"
description: "Synthesize all Linux mastery skills into a complete production deployment: Write specification, automate with AI, validate systematically, package as deployable Digital FTE"
keywords: [capstone, production deployment, systemd, digital fte, specification-first, linux mastery, automation]
chapter: 10
lesson: 9
duration_minutes: 120

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 (Spec-Driven Integration)"
layer_1_foundation: "N/A - builds on complete chapter foundation"
layer_2_collaboration: "N/A - prerequisite from Lessons 1-8"
layer_3_intelligence: "N/A - prerequisite from Lesson 8"
layer_4_capstone: "Writing complete production deployment specification, orchestrating AI implementation, validating against requirements, packaging as production Digital FTE"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Production Deployment Specification Design"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can write complete deployment specification with all requirements, constraints, success criteria, and validation checkpoints that AI can implement autonomously"

  - name: "AI-Orchestrated Deployment Automation"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can direct AI to implement deployment automation following written specification, validating each component against requirements"

  - name: "Systematic Production Validation"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can validate deployment against specification using systematic testing, security checks, and failure scenario testing"

  - name: "Digital FTE Production Packaging"
    proficiency_level: "C1"
    category: "Conceptual"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can package complete Digital FTE deployment as repeatable, documented system suitable for production handoff"

learning_objectives:
  - objective: "Write complete production deployment specification following spec-first methodology"
    proficiency_level: "C1"
    bloom_level: "Create"
    assessment_method: "Specification document with intent, constraints, success criteria, validation checkpoints"

  - objective: "Orchestrate AI implementation of deployment automation from specification"
    proficiency_level: "C1"
    bloom_level: "Apply"
    assessment_method: "Working systemd service, user setup, security hardening implemented by AI per spec"

  - objective: "Validate deployment systematically against specification requirements"
    proficiency_level: "C1"
    bloom_level: "Evaluate"
    assessment_method: "Validation checklist confirming all requirements met, security checks passed, failure scenarios tested"

  - objective: "Package Digital FTE as repeatable production deployment with documentation"
    proficiency_level: "C1"
    bloom_level: "Create"
    assessment_method: "Complete deployment package with scripts, documentation, runbook for production handoff"

# Cognitive load tracking
cognitive_load:
  new_concepts: 8
  assessment: "8 concepts (specification structure, AI orchestration, validation framework, security hardening, service deployment, monitoring, troubleshooting, documentation) - within C1 limit (no artificial constraints at advanced level)"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Design multi-environment deployment (dev/staging/production) with environment-specific configurations, automated CI/CD pipeline integration, and observability stack (Prometheus, Grafana)"
  remedial_for_struggling: "Focus on single-component deployment first: Complete systemd service setup with one agent, validate it works, then add security hardening step by step"

# Generation metadata
generated_by: "content-implementer"
created: "2026-02-08"
version: "1.0.0"

# Legacy compatibility (Docusaurus)
prerequisites:
  - "All previous lessons in Chapter 10"
  - "Understanding of systemd services (Lesson 6)"
  - "Security hardening knowledge (Lesson 5)"
  - "Bash scripting fundamentals (Lesson 4)"
---

# Capstone: Production Digital FTE Deployment

You've mastered the components. Now orchestrate the system.

Throughout this chapter, you've learned to navigate terminals, persist sessions across disconnections, script automation workflows, harden server security, deploy unkillable services, and debug failures systematically. Each skill is powerful on its own. Combined, they transform an AI agent from an experiment into a **production Digital FTE**.

But there's a critical gap between knowing individual skills and deploying production systems. The gap is **specification**—writing clear intent before implementation, then validating that execution matches requirements.

This capstone teaches you the **specification-first methodology** that separates Vibe Coding (prompt until it seems to work) from production engineering (define success criteria, validate systematically). You'll write a complete deployment specification, orchestrate AI implementation, validate against requirements, and package a repeatable Digital FTE deployment.

This isn't just a learning exercise. It's the **production workflow** you'll use for every Digital FTE you deploy.

---

## The Digital FTE Deployment Vision

Your Digital FTEs live on Linux servers, running 24/7, serving customers without human intervention. But how do they get there? What ensures they run reliably? What happens when they fail?

**Production deployment architecture**:

```
┌─────────────────────────────────────────────────────────────┐
│                    Production Server                         │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  systemd Service Manager                            │    │
│  │  - Auto-start on boot                               │    │
│  │  - Auto-restart on failure                          │    │
│  │  - Resource limits & monitoring                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                          ▲                                    │
│                          │ manages                            │
│  ┌───────────────────────┴─────────────────────────────┐    │
│  │  Digital FTE (FastAPI Agent)                       │    │
│  │  - Runs as dedicated non-root user                 │    │
│  │  - Logs to /var/log/digital-fte/                   │    │
│  │  - Stores data in /var/lib/digital-fte/            │    │
│  │  - Exposes API on localhost:8000                   │    │
│  └─────────────────────────────────────────────────────┘    │
│                          ▲                                    │
│                          │ reverse proxy                      │
│  ┌───────────────────────┴─────────────────────────────┐    │
│  │  nginx (TLS Termination)                           │    │
│  │  - HTTPS on port 443                               │    │
│  │  - Forwards to Digital FTE on localhost:8000       │    │
│  │  - Static file serving                             │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  Security: SSH key-based auth only, no password logins       │
│  Monitoring: journalctl logs, htop resources                │
│  Backups: /var/lib/digital-fte/ backed up daily               │
└─────────────────────────────────────────────────────────────┘
```

Each layer serves a purpose:
- **systemd**: Keeps Digital FTE alive
- **Non-root user**: Limits damage if compromised
- **nginx**: Secures traffic with HTTPS
- **SSH keys**: Prevents password-based attacks
- **Monitoring**: Detects problems early
- **Backups**: Enables disaster recovery

Your capstone: Deploy this architecture **specification-first**.

---

## Phase 1: Specify — Write Production Deployment Specification

**The critical principle**: Specification BEFORE implementation. You cannot validate against requirements you haven't defined.

### Specification Structure

Your specification must answer:

| Section | Purpose | Example |
|---------|---------|---------|
| **Intent** | WHAT are you building? | "Deploy customer-support-agent as production service" |
| **Requirements** | WHAT must it do? | "Auto-start on boot, restart on failure, log to /var/log/" |
| **Constraints** | WHAT won't you do? | "No Docker (use native systemd), no root execution" |
| **Success Criteria** | HOW do you know it works? | "Service active after reboot, logs readable, API responds" |
| **Security** | HOW is it protected? | "Dedicated user, SSH keys only, file permissions 600" |
| **Validation** | HOW do you verify? | "Test reboot, test failure recovery, test permissions" |

### Write Your Specification

**Specification Template**:

```markdown
# Production Deployment Specification: Customer Support Digital FTE

## Intent
Deploy customer-support-agent as production systemd service that:
- Auto-starts on server boot
- Restarts automatically on failure
- Runs under dedicated non-root user
- Logs all activity for monitoring
- Serves API via nginx with HTTPS

## Requirements

### Functional Requirements
- FR-001: Service starts automatically on system boot
- FR-002: Service restarts if it crashes (exit code ≠ 0)
- FR-003: Service runs as user `digital-fte` (not root)
- FR-004: Service logs to /var/log/digital-fte/app.log
- FR-005: Service stores data in /var/lib/digital-fte/
- FR-006: nginx forwards HTTPS traffic to service on localhost:8000

### Non-Functional Requirements
- NFR-001: Service startup time < 10 seconds
- NFR-002: Memory limit 512MB (kills if exceeded)
- NFR-003: Auto-restart with 5-second delay (prevent restart loops)
- NFR-004: Logs rotate when reaching 100MB (prevent disk fill)

### Security Requirements
- SR-001: Dedicated user `digital-fte` with minimal permissions
- SR-002: Service files owned by `digital-fte:wheel` with permissions 640
- SR-003: API keys stored in /etc/digital-fte/.env with permissions 600
- SR-004: SSH password authentication disabled (key-based only)
- SR-005: Firewall allows only ports 22 (SSH), 80 (HTTP), 443 (HTTPS)

### Operational Requirements
- OR-001: Logs monitored via `journalctl -u digital-fte -f`
- OR-002: Resources monitored via `htop` (CPU, memory, threads)
- OR-003: Automated backup of /var/lib/digital-fte/ daily
- OR-004: Runbook documents common failure scenarios and recovery steps

## Constraints

### Out of Scope (Explicitly NOT doing)
- Containerization (Docker, Kubernetes) — use native systemd
- Load balancing — single server deployment
- Auto-scaling — fixed resource allocation
- Advanced observability — logs + basic monitoring only

### Technical Constraints
- Ubuntu 22.04 LTS target environment
- Python 3.10+ required
- systemd version 249+ required
- nginx 1.18+ required

## Success Criteria

Deployment succeeds when:
- [ ] Service starts: `systemctl start digital-fte` returns exit code 0
- [ ] Service enables: `systemctl is-enabled digital-fte` returns "enabled"
- [ ] Service active: `systemctl is-active digital-fte` returns "active"
- [ ] API responds: `curl localhost:8000/health` returns 200 OK
- [ ] Logs exist: `/var/log/digital-fte/app.log` is writable by digital-fte user
- [ ] Permissions correct: Service files are 640, owned by digital-fte:wheel
- [ ] Survives reboot: After `reboot`, service auto-starts and is active
- [ ] Survives crash: Killing process triggers auto-restart within 10 seconds

## Security Validation

Security checks passed when:
- [ ] User exists: `id digital-fte` shows user with UID > 1000
- [ ] Not root: Service runs as digital-fte, NOT root (check `ps aux | grep digital-fte`)
- [ ] SSH password auth off: `grep PasswordAuthentication /etc/ssh/sshd_config` shows "no"
- [ ] API keys protected: `/etc/digital-fte/.env` has permissions 600 (rw-------)
- [ ] Minimal permissions: `sudo -l -U digital-fte` shows minimal sudo access

## Failure Scenario Testing

Deployment validated when:
- [ ] Crash recovery: `kill -9 $(pidof digital-fte)` triggers auto-restart
- [ ] Log rotation: Manual 100MB log file triggers rotation (no disk fill)
- [ ] Memory limit: Process consuming >512MB gets killed (OOM)
- [ ] Network failure: Service handles connection loss gracefully (logs error, doesn't crash)
- [ ] Invalid config: Invalid config file causes service to FAIL, not start with bad config
```

**What Makes This Specification Good**:
- **Measurable**: Every requirement has testable success criteria
- **Complete**: Covers functional, security, operational requirements
- **Explicit**: States what's NOT being done (prevents scope creep)
- **Validatable**: Each requirement maps to specific test

**What Makes This Specification Production-Ready**:
- **Security-first**: Dedicated user, minimal permissions, SSH hardening
- **Resilience**: Auto-restart, resource limits, crash recovery
- **Observable**: Logging, monitoring, runbook for troubleshooting
- **Maintainable**: Documentation, backup strategy, clear handoff

This specification is **sufficient for AI to implement autonomously**. Any competent AI agent reading this spec can execute the deployment without clarification.

---

## Phase 2: Implement — Orchestrate AI from Specification

Now you shift from architect to orchestrator. Your specification defines **WHAT** needs to happen. AI handles **HOW** to implement it.

### The Orchestration Pattern

**Wrong way** (Vibe Coding):
```
"AI, deploy my agent as a service."
→ AI guesses requirements → produces generic output → you iterate blindly
```

**Right way** (Specification-Driven):
```
"AI, implement this specification: [paste spec.md]"
→ AI follows requirements → produces compliant output → you validate against spec
```

### Three Roles in Action: Specification Implementation

#### Interaction 1: AI Teaches Production Patterns

**What you ask AI**:

```
I need to deploy a FastAPI agent as a production systemd service.
Here's my specification: [paste your spec]

Before you implement, explain:
1. What systemd service file structure ensures reliable auto-restart?
2. What's the difference between Restart=always and Restart=on-failure?
3. How do I prevent restart loops when service fails immediately?

I want to understand the production patterns before implementation.
```

**What AI teaches you**:

```
systemd Reliability Patterns:

1. Service File Structure for Auto-Restart:
   [Service]
   Restart=on-failure        # Only restart if crashes (exit code ≠ 0)
   RestartSec=5              # Wait 5 seconds before restarting
   TimeoutStartSec=10        # Give up if startup takes >10s
   TimeoutStopSec=10         # Give up if shutdown takes >10s

   These prevent: Restart loops (delay), hanging starts (timeout)

2. Restart=always vs Restart=on-failure:
   Restart=always: Restarts EVEN if you stop it manually (bad idea)
   Restart=on-failure: Only restarts if crashes (correct choice)

   Why it matters: Restart=always prevents controlled service management

3. Preventing Restart Loops:
   RestartSec=5           # Delay prevents CPU-spinning restart loops
   StartLimitInterval=60  # Only count restarts within 60 seconds
   StartLimitBurst=5      # If >5 restarts in 60s, STOP trying

   This prevents: Service from restarting infinitely when misconfigured
```

**What you learned**: AI taught you **production systemd patterns** that balance reliability with safety. You didn't know about `StartLimitBurst`—this prevents infinite restart loops that consume CPU.

**Key moment**: AI suggested a reliability pattern (restart limits) that improves your deployment beyond what you specified.

---

#### Interaction 2: You Refine AI's Understanding

Now you correct AI's assumptions based on your deployment context.

**What AI produces initially**:

```
systemd service file:

[Unit]
Description=Digital FTE Customer Support Agent
After=network.target

[Service]
Type=simple
User=digital-fte
Group=digital-fte
WorkingDirectory=/home/digital-fte/agent
ExecStart=/home/digital-fte/agent/venv/bin/python main.py
Restart=on-failure
RestartSec=5
Environment="PATH=/home/digital-fte/agent/venv/bin"

[Install]
WantedBy=multi-user.target
```

**But you catch an issue**:

```
Good start, but my specification says data goes to /var/lib/digital-fte/,
not /home/digital-fte/agent. I also need API keys loaded from
/etc/digital-fte/.env, not hardcoded Environment=.

My security requirement: API keys file must have permissions 600
and the service should FAIL to start if the file is missing.

How do I make the service depend on the environment file?
```

**What AI adapts to**:

```
Corrected service file with environment file dependency:

[Unit]
Description=Digital FTE Customer Support Agent
After=network.target
Requires=etc-digital-fte-env.mount  # FAIL if .env doesn't exist

[Service]
Type=simple
User=digital-fte
Group=digital-fte
WorkingDirectory=/var/lib/digital-fte/
ExecStart=/var/lib/digital-fte/venv/bin/python main.py
Restart=on-failure
RestartSec=5
EnvironmentFile=/etc/digital-fte/.env  # Load API keys from file

# Security hardening
NoNewPrivileges=true    # Prevent process from gaining new privileges
PrivateTmp=true         # Isolate /tmp namespace
ReadWritePaths=/var/lib/digital-fte/  # Only allow writing here

[Install]
WantedBy=multi-user.target

Key additions:
- Requires=etc-digital-fte-env.mount: Creates dependency on env file
- EnvironmentFile=: Loads API keys securely (not in service file)
- NoNewPrivileges, PrivateTmp: Security hardening (least privilege)
- ReadWritePaths: Restricts where service can write (prevents filesystem abuse)
```

**What AI learned**: AI adapted to **your security constraints** (environment file dependency, restricted write paths). You taught AI that missing config should cause startup failure, not default behavior.

**Key moment**: You corrected AI's generic approach to match your production security requirements.

---

#### Interaction 3: Iterate to Optimal Configuration

Here's where both of you iterate together, converging on something better than either would design alone.

**Iteration 1: Initial monitoring approach**

You ask: "I need to monitor the service. How do I check it's running?"

**AI suggests**: "Use `systemctl status digital-fte` to check if active. Add cron job to check every minute."

You think: "That works, but I want push notifications, not just passive monitoring."

**Iteration 2: You add a constraint**

You ask: "Can I get alerts when the service fails? Not just passive status checks."

**AI suggests**: "Use systemd's `OnFailure=` directive to trigger a script that sends alerts. Or use monitoring tools like monit."

You think: "monit is another service to manage. Can I do this with pure systemd?"

**Iteration 3: Convergence**

Together you arrive at:

```
Service file with monitoring integration:

[Unit]
Description=Digital FTE Customer Support Agent
After=network.target
Requires=etc-digital-fte-env.mount

[Service]
Type=simple
User=digital-fte
Group=digital-fte
WorkingDirectory=/var/lib/digital-fte/
ExecStart=/var/lib/digital-fte/venv/bin/python main.py
Restart=on-failure
RestartSec=5
EnvironmentFile=/etc/digital-fte/.env
NoNewPrivileges=true
PrivateTmp=true
ReadWritePaths=/var/lib/digital-fte/

# Monitoring integration
OnFailure=notify-failure@%n.service  # Trigger on failure
NotifyAccess=all                     # Allow access to service status

[Install]
WantedBy=multi-user.target

Drop-in file /etc/systemd/system/digital-fte.service.d/failure-notify.conf:

[Service]
ExecStopPost=/usr/local/bin/digital-fte-alert "Service %n failed with exit code $MAINPID"

Alert script /usr/local/bin/digital-fte-alert:

#!/bin/bash
# Send alert via webhook, email, or Slack
curl -X POST https://hooks.slack.com/services/YOUR/WEBHOOK/URL \
  -H 'Content-Type: application/json' \
  -d '{"text": "Digital FTE Alert: '"$1"'"}'
```

**What neither of you had individually**:
- You didn't know about `OnFailure=` directive (systemd feature AI taught you)
- AI didn't know you wanted Slack integration specifically (you clarified requirement)
- Together, you created **integrated monitoring** that combines systemd reliability with your notification needs

**Key moment**: This is Co-Worker convergence—iteration produced monitoring optimized for **your workflow** (Slack alerts), not just generic status checking.

---

## Phase 3: Validate — Systematic Testing Against Specification

Specification is useless without validation. You must prove your deployment meets ALL requirements.

### Validation Framework

Organize validation into layers:

```
LAYER 1: Existence Checks (Files present?)
├── Service file exists: /etc/systemd/system/digital-fte.service
├── User exists: id digital-fte
├── Directories exist: /var/lib/digital-fte/, /var/log/digital-fte/
└── Config exists: /etc/digital-fte/.env

LAYER 2: Permission Checks (Security correct?)
├── Service file permissions: 640 (rw-r-----)
├── .env file permissions: 600 (rw-------)
├── Directory ownership: digital-fte:wheel
└── Service runs as digital-fte (not root)

LAYER 3: Functional Checks (Does it work?)
├── Service starts: systemctl start digital-fte (exit code 0)
├── Service active: systemctl is-active digital-fte
├── API responds: curl localhost:8000/health (200 OK)
└── Logs write: Test log entry appears in /var/log/digital-fte/app.log

LAYER 4: Resilience Checks (Does it survive failures?)
├── Survives reboot: reboot → service auto-starts
├── Survives crash: kill -9 → service auto-restarts
├── Survives bad config: Invalid .env → service fails to start
└── Survives resource limits: Memory >512MB → process killed

LAYER 5: Security Checks (Is it protected?)
├── SSH password auth off: grep PasswordAuthentication /etc/ssh/sshd_config
├── Not root: ps aux | grep digital-fte shows non-root user
├── Firewall rules: ufw status shows only 22, 80, 443 open
└── API keys protected: /etc/digital-fte/.env has 600 permissions
```

### Automated Validation Script

Create a validation script that tests all layers:

```bash
#!/bin/bash
# validate-deployment.sh - Systematic deployment validation

echo "=== Digital FTE Deployment Validation ==="

# LAYER 1: Existence Checks
echo "[Layer 1] Checking file existence..."

check_file() {
  if [ -f "$1" ]; then
    echo "✓ EXISTS: $1"
    return 0
  else
    echo "✗ MISSING: $1"
    return 1
  fi
}

check_dir() {
  if [ -d "$1" ]; then
    echo "✓ EXISTS: $1"
    return 0
  else
    echo "✗ MISSING: $1"
    return 1
  fi
}

check_user() {
  if id "$1" &>/dev/null; then
    echo "✓ USER EXISTS: $1"
    return 0
  else
    echo "✗ USER MISSING: $1"
    return 1
  fi
}

layer1_pass=true
check_file "/etc/systemd/system/digital-fte.service" || layer1_pass=false
check_file "/etc/digital-fte/.env" || layer1_pass=false
check_dir "/var/lib/digital-fte/" || layer1_pass=false
check_dir "/var/log/digital-fte/" || layer1_pass=false
check_user "digital-fte" || layer1_pass=false

if [ "$layer1_pass" = true ]; then
  echo "✓ Layer 1 PASSED"
else
  echo "✗ Layer 1 FAILED - missing files/directories"
  exit 1
fi

# LAYER 2: Permission Checks
echo "[Layer 2] Checking permissions..."

check_perms() {
  local perms=$(stat -c %a "$1")
  local owner=$(stat -c %U "$1")
  if [ "$perms" = "$2" ] && [ "$owner" = "$3" ]; then
    echo "✓ PERMISSIONS OK: $1 ($perms, $owner)"
    return 0
  else
    echo "✗ PERMISSIONS WRONG: $1 (got $perms:$owner, expected $2:$3)"
    return 1
  fi
}

layer2_pass=true
check_perms "/etc/systemd/system/digital-fte.service" "640" "root" || layer2_pass=false
check_perms "/etc/digital-fte/.env" "600" "root" || layer2_pass=false

if [ "$layer2_pass" = true ]; then
  echo "✓ Layer 2 PASSED"
else
  echo "✗ Layer 2 FAILED - permission issues"
  exit 1
fi

# LAYER 3: Functional Checks
echo "[Layer 3] Checking functionality..."

layer3_pass=true

# Check service status
if systemctl is-active --quiet digital-fte; then
  echo "✓ SERVICE ACTIVE"
else
  echo "✗ SERVICE INACTIVE"
  layer3_pass=false
fi

# Check API health
if curl -s http://localhost:8000/health | grep -q "OK"; then
  echo "✓ API RESPONDS: /health returns 200"
else
  echo "✗ API UNRESPONSIVE: /health not working"
  layer3_pass=false
fi

# Check logs
if [ -w "/var/log/digital-fte/app.log" ]; then
  echo "✓ LOGS WRITABLE"
else
  echo "✗ LOGS NOT WRITABLE"
  layer3_pass=false
fi

if [ "$layer3_pass" = true ]; then
  echo "✓ Layer 3 PASSED"
else
  echo "✗ Layer 3 FAILED - functional issues"
  exit 1
fi

# LAYER 4: Resilience Checks (WARNING: disruptive tests)
echo "[Layer 4] Testing resilience (disruptive)..."
read -p "Run crash recovery test? This will kill the service. [y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
  echo "Testing crash recovery..."
  pid=$(systemctl show digital-fte -p MainPID --value)
  if [ -n "$pid" ]; then
    kill -9 "$pid"
    sleep 10
    if systemctl is-active --quiet digital-fte; then
      echo "✓ CRASH RECOVERY: Service auto-restarted"
    else
      echo "✗ CRASH RECOVERY FAILED: Service did not restart"
      exit 1
    fi
  else
    echo "⊘ SKIPPED: Service not running"
  fi
else
  echo "⊘ SKIPPED: Crash recovery test"
fi

# LAYER 5: Security Checks
echo "[Layer 5] Checking security..."

layer5_pass=true

# Check SSH password auth
if grep -q "PasswordAuthentication no" /etc/ssh/sshd_config; then
  echo "✓ SSH PASSWORD AUTH: Disabled"
else
  echo "✗ SSH PASSWORD AUTH: Enabled (security risk)"
  layer5_pass=false
fi

# Check service runs as non-root
service_user=$(ps aux | grep "[d]igital-fte" | awk '{print $1}')
if [ "$service_user" = "digital-fte" ]; then
  echo "✓ SERVICE USER: Runs as digital-fte (not root)"
else
  echo "✗ SERVICE USER: Running as $service_user (should be digital-fte)"
  layer5_pass=false
fi

if [ "$layer5_pass" = true ]; then
  echo "✓ Layer 5 PASSED"
else
  echo "✗ Layer 5 FAILED - security issues"
  exit 1
fi

# FINAL VERDICT
echo ""
echo "=== VALIDATION COMPLETE ==="
echo "✓ ALL LAYERS PASSED - Deployment is production-ready"
```

**What this script does**:
- **Systematic testing**: Validates each layer in order
- **Early failure**: Stops at first failure (prevents cascading errors)
- **Clear reporting**: Shows exactly what passed/failed
- **Disruptive tests**: Asks before running crash tests (won't kill production accidentally)

**What You Learned**: Validation isn't "looks good." Validation is **systematic testing** that proves each requirement is met. The script is reusable across all your Digital FTE deployments.

---

## Phase 4: Package — Create Repeatable Deployment Artifact

Your deployment is production-ready. Now package it as a repeatable artifact that other teams can deploy.

### Deployment Package Structure

```
digital-fte-deployment/
├── README.md                              # Quick start guide
├── DEPLOYMENT_SPEC.md                     # Full specification
├── deploy.sh                              # Automated deployment script
├── validate.sh                            # Validation script (from Phase 3)
├── config/
│   ├── digital-fte.service.example        # Systemd service template
│   ├── digital-fte.env.example            # Environment variables template
│   └── nginx.conf.example                 # nginx config template
├── scripts/
│   ├── setup-user.sh                      # Create digital-fte user
│   ├── setup-directories.sh               # Create directories
│   ├── setup-ssh.sh                       # SSH hardening
│   └── setup-firewall.sh                  # Firewall rules
└── docs/
    ├── RUNBOOK.md                         # Operations runbook
    ├── TROUBLESHOOTING.md                 # Common issues & solutions
    └── ARCHITECTURE.md                    # System architecture diagram
```

### Deployment Script

```bash
#!/bin/bash
# deploy.sh - Automated deployment script

set -e  # Exit on error

echo "=== Digital FTE Deployment ==="

# Load configuration
DEPLOYMENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$DEPLOYMENT_DIR/config/digital-fte.env"

# Step 1: Create user
echo "[1/6] Creating digital-fte user..."
sudo ./scripts/setup-user.sh

# Step 2: Create directories
echo "[2/6] Creating directories..."
sudo ./scripts/setup-directories.sh

# Step 3: Install application
echo "[3/6] Installing application..."
sudo cp -r /path/to/agent/* /var/lib/digital-fte/
sudo chown -R digital-fte:wheel /var/lib/digital-fte/

# Step 4: Configure systemd service
echo "[4/6] Configuring systemd service..."
sudo cp config/digital-fte.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable digital-fte

# Step 5: Configure nginx
echo "[5/6] Configuring nginx..."
sudo cp config/nginx.conf /etc/nginx/sites-available/digital-fte
sudo ln -s /etc/nginx/sites-available/digital-fte /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx

# Step 6: Security hardening
echo "[6/6] Security hardening..."
sudo ./scripts/setup-ssh.sh
sudo ./scripts/setup-firewall.sh

echo ""
echo "=== Deployment Complete ==="
echo "Run validation: ./validate.sh"
echo "Start service: sudo systemctl start digital-fte"
```

### Operations Runbook

Document how to operate the deployed Digital FTE:

```markdown
# Digital FTE Operations Runbook

## Starting the Service

```bash
sudo systemctl start digital-fte
```

## Stopping the Service

```bash
sudo systemctl stop digital-fte
```

## Restarting the Service

```bash
sudo systemctl restart digital-fte
```

## Viewing Logs

### Real-time logs
```bash
journalctl -u digital-fte -f
```

### Last 100 lines
```bash
journalctl -u digital-fte -n 100
```

### Logs since last boot
```bash
journalctl -u digital-fte -b
```

## Checking Service Status

```bash
systemctl status digital-fte
```

## Updating the Application

1. Stop service: `sudo systemctl stop digital-fte`
2. Deploy new code to `/var/lib/digital-fte/`
3. Restart service: `sudo systemctl start digital-fte`
4. Verify health: `curl http://localhost:8000/health`

## Failure Scenarios

### Service not starting
1. Check logs: `journalctl -u digital-fte -n 50`
2. Check config: `sudo systemctl daemon-reload`
3. Check permissions: `ls -la /var/lib/digital-fte/`

### Service crashing repeatedly
1. Check resource usage: `htop`
2. Check logs for errors: `journalctl -u digital-fte -b`
3. Check environment file: `cat /etc/digital-fte/.env`

### API not responding
1. Check service status: `systemctl status digital-fte`
2. Check nginx status: `systemctl status nginx`
3. Test local: `curl http://localhost:8000/health`
4. Test external: `curl https://your-domain.com/health`
```

**What You Learned**: Documentation isn't optional. It's the difference between "you can deploy it" and "anyone can deploy it." A deployment package without documentation is personal automation; with documentation, it's a **team asset**.

---

## From Deployment to Digital FTE Asset

Your production deployment package isn't just infrastructure. It's intellectual property with market value.

### What Makes It Valuable

1. **Encoded DevOps Expertise**: Your systemd patterns, security hardening, and monitoring represent production best practices
2. **Repeatable Deployment**: One-command deployment that works consistently
3. **Comprehensive Documentation**: Runbooks, troubleshooting guides, architecture diagrams
4. **Validated Quality**: Systematic testing proves reliability

### Digital FTE vs. Personal Automation

| Personal Automation | Digital FTE Asset |
|---------------------|-------------------|
| Works on your machine | Works on any server |
| You know how to fix it | Anyone can fix it (runbook) |
| "Hope it works" | Tested and validated |
| Fragile to changes | Resilient to failures |
| Not sellable | **Customer-ready product** |

### Packaging for Sale

When packaging Digital FTEs for clients:

| Component | What Client Customizes |
|-----------|----------------------|
| **Service file** | Paths, usernames, resource limits |
| **Environment** | API keys, domain names, database URLs |
| **nginx config** | SSL certificates, domain names |
| **Monitoring** | Alert endpoints, notification channels |
| **Documentation** | Company-specific procedures, contacts |

The core deployment logic—systemd patterns, security hardening, validation framework—remains constant. The configuration adapts to each client's environment.

---

## Production Deployment Checklist

Before declaring your Digital FTE production-ready:

```
□ SPECIFICATION COMPLETE
  □ All requirements defined with success criteria
  □ Security requirements specified
  □ Validation tests documented

□ IMPLEMENTATION COMPLETE
  □ systemd service file created and tested
  □ Non-root user created with minimal permissions
  □ Directories created with correct ownership
  □ nginx configured with HTTPS
  □ SSH hardened (key-based auth only)
  □ Firewall rules applied

□ VALIDATION COMPLETE
  □ All existence checks pass
  □ All permission checks pass
  □ All functional checks pass
  □ All resilience checks pass
  □ All security checks pass

□ DOCUMENTATION COMPLETE
  □ README with quick start
  □ Deployment specification
  □ Operations runbook
  □ Troubleshooting guide
  □ Architecture diagram

□ HANDOFF READY
  □ Deployment package tested on fresh server
  □ Documentation reviewed for clarity
  □ Validation script automated
  □ Support escalation path defined
```

---

## Try With AI

Complete your capstone by working through these deployment challenges with AI.

### Challenge 1: Design Your Production Deployment

```
I'm deploying a FastAPI agent that processes customer support tickets.
Write a production deployment specification that includes:

1. systemd service configuration (auto-start, auto-restart, resource limits)
2. Security hardening (non-root user, SSH keys only, file permissions)
3. Monitoring integration (logs, crash recovery, alerting)
4. nginx configuration (HTTPS, reverse proxy to localhost:8000)
5. Validation tests (prove everything works)

Give me:
1. Complete specification document (like the template)
2. systemd service file with production-hardening
3. nginx config with TLS
4. Validation bash script that tests all layers

I want to deploy this specification-first: write spec, then implement.
```

**What you're learning**: How to translate business requirements ("I need a reliable customer support agent") into technical specifications ("systemd with Restart=on-failure, resource limits, monitoring integration"). The specification becomes your implementation roadmap—AI executes it, you validate it.

---

### Challenge 2: Orchestrate AI Implementation with Iteration

```
I've written my deployment specification: [paste spec]

Now I need you to implement it. Follow this workflow:

1. Read my specification and identify all requirements
2. Propose implementation approach (systemd file, nginx config, scripts)
3. I'll review and refine based on my deployment context
4. After I approve, generate all configuration files
5. Create deployment script that automates setup
6. Create validation script that tests everything

Constraint: Don't just generate files—explain WHY each configuration
choice ensures reliability and security. I need to understand the
production patterns, not copy-paste configs.
```

**What you're learning**: Specification-driven development is iterative. You don't accept AI's first output—you review, refine, and converge on optimal solution. The iteration teaches you production patterns while ensuring the deployment matches your requirements.

---

### Challenge 3: Validate and Debug Systematically

```
I deployed my Digital FTE but something's wrong. Help me diagnose:

Symptoms:
- Service status shows "active (running)"
- curl localhost:8000/health returns "Connection refused"
- Logs show: "Permission denied: /var/lib/digital-fte/database.sqlite"

Walk me through systematic diagnosis:
1. What tests should I run to isolate the problem?
2. What's the most likely root cause?
3. How do I fix it permanently?
4. How do I add a validation check that prevents this in future deployments?

Teach me the debugging process, not just the fix.
```

**What you're learning**: Systematic troubleshooting beats random guessing. The debugging process (isolate symptoms → identify root cause → implement fix → add validation) applies to ALL production issues. AI teaches you the diagnostic framework, not just the solution.

**Safety Note**: Production deployment involves servers, services, and security configurations. Test your deployment specification on a non-production server first (VM, container, or development environment). Validate all security checks before applying to production. Always have SSH access fallback when modifying systemd services or network configurations. The Digital FTE deployment framework augments your DevOps capability; it never replaces your responsibility for system security and reliability.
