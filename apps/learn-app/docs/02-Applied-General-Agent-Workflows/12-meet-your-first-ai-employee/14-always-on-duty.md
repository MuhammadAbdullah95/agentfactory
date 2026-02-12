---
sidebar_position: 14
title: "Lesson 14: Always On Duty"
description: "Deploy your AI Employee for 24/7 operation with PM2 locally or Oracle Cloud Free Tier remotely"
keywords: [pm2, oracle cloud, always-on, deployment, vps, tailscale, 24/7, persistent]
chapter: 12
lesson: 14
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "Production Deployment"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Can deploy AI Employee for 24/7 operation using PM2 or cloud VPS"

  - name: "Process Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can configure PM2 ecosystem files and monitor process health"

  - name: "Cloud Deployment Architecture"
    proficiency_level: "C1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Can evaluate deployment options and select appropriate solution for requirements"

  - name: "Secure Remote Access"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Can configure Tailscale for secure gateway access without public exposure"

learning_objectives:
  - objective: "Configure PM2 for local always-on operation"
    proficiency_level: "C1"
    bloom_level: "Apply"
    assessment_method: "Working PM2 setup that survives reboot"

  - objective: "Evaluate cloud deployment options for cost and capability"
    proficiency_level: "C1"
    bloom_level: "Evaluate"
    assessment_method: "Cost/benefit analysis selecting appropriate provider"

  - objective: "Configure health monitoring and automatic recovery"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Health check system triggers restart on failure"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (PM2, cloud VPS, Tailscale networking, health monitoring) appropriate for C1 advanced content"

differentiation:
  extension_for_advanced: "Deploy to Oracle Cloud with full Tailscale setup and VCN security"
  remedial_for_struggling: "Start with PM2 local only, skip cloud deployment until comfortable"
---

# Always On Duty

Your AI Employee works brilliantly when your computer is on and you are awake. But what happens at 3am when a client sends an urgent email? What about when you are traveling and your laptop is closed? Right now, your employee takes the day off whenever you do.

This lesson transforms your AI Employee from a work-hours assistant into a true 24/7 team member. You will learn two approaches: running persistently on your local machine, and deploying to cloud infrastructure that never sleeps. By the end, your AI Employee will be available every moment of every day, processing requests whether you are asleep, traveling, or simply away from your desk.

This is an advanced, optional lesson. If you are satisfied with your AI Employee working only when your computer is on, you can skip ahead to the Chapter Assessment. But if you want the full autonomous experience, the investment here pays dividends in availability.

## The Always-On Promise

Human employees have limits. They sleep, take vacations, get sick. Your AI Employee has none of these constraints. The only limitation is infrastructure: it needs somewhere to run.

| Your Current Setup | What Changes |
|-------------------|--------------|
| Works when laptop is open | Works 24/7/365 |
| Stops when you reboot | Survives reboots |
| Unavailable while traveling | Available everywhere |
| Dependent on your presence | Truly autonomous |

There are two paths to always-on operation:

**Option A: Local Always-On (PM2)**
- Your computer runs continuously
- Process manager keeps gateway alive
- Cost: $0 (electricity only)
- Limitation: Computer must stay on

**Option B: Cloud Always-On (Oracle Free)**
- Remote server runs your gateway
- Available even when your computer is off
- Cost: $0 (Oracle Always Free tier)
- Limitation: Setup complexity, ARM architecture

Choose based on your needs. Many users start with Option A and graduate to Option B when they want true independence from their local machine.

## Option A: Local Always-On with PM2

PM2 is a production process manager for Node.js applications. It keeps your gateway running, restarts it if it crashes, and can survive system reboots.

### Installing PM2

PM2 installs globally via npm:

```bash
npm install -g pm2
```

**Output:**
```
added 182 packages in 8s

18 packages are looking for funding
  run `npm fund` for details
```

Verify the installation:

```bash
pm2 --version
```

**Output:**
```
5.3.0
```

### Creating an Ecosystem File

PM2 uses an ecosystem file to define how your application runs. Create this in your home directory or a project folder:

```bash
nano ~/openclaw-ecosystem.config.js
```

Enter the following configuration:

```javascript
module.exports = {
  apps: [{
    name: "openclaw-gateway",
    script: "openclaw",
    args: "gateway run --port 18789",
    watch: false,
    autorestart: true,
    max_restarts: 10,
    restart_delay: 5000,
    env: {
      NODE_ENV: "production"
    }
  }]
};
```

Save and exit.

**What each setting does:**

| Setting | Purpose |
|---------|---------|
| `name` | Identifier for this process in PM2 |
| `script` | The command to run (openclaw binary) |
| `args` | Arguments passed to the command |
| `watch` | Restart on file changes (disabled for stability) |
| `autorestart` | Restart if process crashes |
| `max_restarts` | Give up after 10 consecutive failures |
| `restart_delay` | Wait 5 seconds between restart attempts |

### Starting with PM2

Launch your gateway through PM2:

```bash
pm2 start ~/openclaw-ecosystem.config.js
```

**Output:**
```
[PM2] Spawning PM2 daemon with pm2_home=/Users/user/.pm2
[PM2] PM2 Successfully daemonized
[PM2] Starting /usr/local/bin/openclaw in fork_mode (1 instance)
[PM2] Done.
┌─────┬────────────────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┬──────────┬──────────┐
│ id  │ name               │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │ user     │ watching │
├─────┼────────────────────┼─────────────┼─────────┼─────────┼──────────┼────────┼──────┼───────────┼──────────┼──────────┼──────────┼──────────┤
│ 0   │ openclaw-gateway   │ default     │ N/A     │ fork    │ 12345    │ 0s     │ 0    │ online    │ 0%       │ 45.2mb   │ user     │ disabled │
└─────┴────────────────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┴──────────┴──────────┘
```

### Persisting Across Reboots

By default, PM2 processes disappear when your computer restarts. To make them survive reboots:

```bash
pm2 save
pm2 startup
```

**Output:**
```
[PM2] Saving current process list...
[PM2] Successfully saved in /Users/user/.pm2/dump.pm2
[PM2] To setup the Startup Script, copy/paste the following command:
sudo env PATH=$PATH:/usr/local/bin pm2 startup launchd -u user --hp /Users/user
```

Run the command PM2 provides (it will be specific to your system):

```bash
sudo env PATH=$PATH:/usr/local/bin pm2 startup launchd -u user --hp /Users/user
```

Now your gateway will start automatically when your computer boots.

### Monitoring PM2 Processes

PM2 provides several monitoring commands:

**Check status:**
```bash
pm2 status
```

**Output:**
```
┌─────┬────────────────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┐
│ id  │ name               │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │
├─────┼────────────────────┼─────────────┼─────────┼─────────┼──────────┼────────┼──────┼───────────┼──────────┼──────────┤
│ 0   │ openclaw-gateway   │ default     │ N/A     │ fork    │ 12345    │ 45m    │ 0    │ online    │ 0.1%     │ 62.3mb   │
└─────┴────────────────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┘
```

**View logs:**
```bash
pm2 logs openclaw-gateway
```

**Output:**
```
[TAILING] Tailing last 15 lines for [openclaw-gateway] process (change the value with --lines option)
/Users/user/.pm2/logs/openclaw-gateway-out.log last 15 lines:
0|openclaw | Gateway started on port 18789
0|openclaw | Telegram channel connected
0|openclaw | Health check: OK
```

**Real-time monitoring:**
```bash
pm2 monit
```

This opens an interactive dashboard showing CPU, memory, and logs in real-time.

### PM2 Management Commands

| Command | Purpose |
|---------|---------|
| `pm2 stop openclaw-gateway` | Stop the gateway |
| `pm2 restart openclaw-gateway` | Restart the gateway |
| `pm2 delete openclaw-gateway` | Remove from PM2 |
| `pm2 flush` | Clear all log files |
| `pm2 logs --lines 100` | Show last 100 log lines |

## Option B: Oracle Cloud Free Tier

Oracle Cloud offers a genuinely free tier with substantial resources: up to 4 ARM CPUs and 24GB of RAM. This is more than enough for your AI Employee, and the cost is $0 forever (not a trial).

### Why Oracle Cloud?

| Provider | Free Tier | Specs | Notes |
|----------|-----------|-------|-------|
| **Oracle Cloud** | Permanent | 4 OCPU, 24GB RAM | ARM architecture |
| DigitalOcean | $200 trial | Various | Expires after 60 days |
| AWS | 12 months | t2.micro | Very limited |
| Google Cloud | $300 trial | Various | Expires after 90 days |
| Hetzner | None | N/A | $4/mo cheapest |

Oracle's Always Free tier is unique in offering substantial persistent compute at no cost.

### Creating an Oracle Cloud Instance

**Prerequisites:**
- Oracle Cloud account (signup at cloud.oracle.com/free)
- SSH key pair
- Approximately 30 minutes

**Step 1: Create Instance**

1. Log into Oracle Cloud Console
2. Navigate to Compute then Instances then Create Instance
3. Configure:
   - **Name:** openclaw
   - **Image:** Ubuntu 24.04 (aarch64)
   - **Shape:** VM.Standard.A1.Flex (Ampere ARM)
   - **OCPUs:** 2 (or up to 4)
   - **Memory:** 12 GB (or up to 24 GB)
   - **Boot volume:** 50 GB
   - **SSH key:** Add your public key

4. Click Create

Note the public IP address when the instance is ready.

**Common Issue:** "Out of capacity" errors are common on the free tier. Try a different availability domain, or retry during off-peak hours (early morning works best).

### Connecting and Setting Up

**Step 2: Connect via SSH**

```bash
ssh ubuntu@YOUR_PUBLIC_IP
```

**Step 3: Update System**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential
```

Build-essential is required for ARM compilation of some npm dependencies.

**Step 4: Install Tailscale**

Tailscale provides secure access without exposing ports to the internet:

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --ssh --hostname=openclaw
```

**Output:**
```
To authenticate, visit:

  https://login.tailscale.com/a/1234567890abcdef

Success.
```

After authenticating in your browser, verify:

```bash
tailscale status
```

**Output:**
```
100.100.100.100  openclaw            linux   -
100.100.100.101  your-laptop         macOS   active; direct
```

From now on, you can connect via Tailscale instead of the public IP:

```bash
ssh ubuntu@openclaw
```

**Step 5: Install OpenClaw**

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
source ~/.bashrc
```

When prompted "How do you want to hatch your bot?", select "Do this later". We will configure manually.

### Configuring for Remote Access

**Step 6: Configure Gateway**

```bash
# Bind only to localhost (Tailscale will provide access)
openclaw config set gateway.bind loopback

# Require token authentication
openclaw config set gateway.auth.mode token
openclaw doctor --generate-gateway-token

# Expose via Tailscale Serve (automatic HTTPS)
openclaw config set gateway.tailscale.mode serve
openclaw config set gateway.trustedProxies '["127.0.0.1"]'
```

**Step 7: Enable as Persistent Service**

```bash
# Enable user lingering (keeps services running after logout)
sudo loginctl enable-linger ubuntu

# Start the gateway service
systemctl --user restart openclaw-gateway
```

### Verifying the Setup

```bash
# Check OpenClaw version
openclaw --version
```

**Output:**
```
OpenClaw v2025.2.3
```

```bash
# Check gateway status
systemctl --user status openclaw-gateway
```

**Output:**
```
● openclaw-gateway.service - OpenClaw Gateway
     Loaded: loaded (/home/ubuntu/.config/systemd/user/openclaw-gateway.service)
     Active: active (running) since Wed 2026-02-05 10:30:00 UTC
   Main PID: 12345 (openclaw)
      Tasks: 12 (limit: 24576)
     Memory: 156.0M
     CGroup: /user.slice/user-1000.slice/user@1000.service/openclaw-gateway.service
             └─12345 openclaw gateway run --port 18789
```

```bash
# Check Tailscale Serve status
tailscale serve status
```

**Output:**
```
https://openclaw.YOUR-TAILNET.ts.net (Funnel off)
|-- / proxy http://127.0.0.1:18789
```

```bash
# Test local response
curl http://localhost:18789
```

**Output:**
```
{"status":"ok","version":"2025.2.3"}
```

### Accessing Your Remote Gateway

From any device on your Tailscale network, access the Control UI at:

```
https://openclaw.YOUR-TAILNET.ts.net/
```

Replace YOUR-TAILNET with your tailnet name (visible in `tailscale status`).

This works from:
- Your laptop (at home or traveling)
- Your phone (with Tailscale app installed)
- Any other device on your tailnet

No SSH tunnel needed. Tailscale provides automatic HTTPS certificates and authentication.

### Security Configuration

With Tailscale handling access, you can lock down the Oracle Cloud VCN (Virtual Cloud Network) to block all public traffic except Tailscale:

1. Go to Networking then Virtual Cloud Networks in Oracle Console
2. Click your VCN then Security Lists then Default Security List
3. Remove all ingress rules except: `0.0.0.0/0 UDP 41641` (Tailscale)

This blocks SSH, HTTP, HTTPS, and everything else at the network edge. Only Tailscale traffic reaches your instance.

## Health Monitoring

Whether running locally with PM2 or remotely on Oracle Cloud, you want automatic recovery when things go wrong.

### OpenClaw Health Commands

```bash
# Quick health check
openclaw health
```

**Output:**
```
Gateway: healthy
Channels:
  telegram: connected
  discord: disconnected (not configured)
Models:
  moonshot/kimi-k2.5: available
Memory: 156MB / 24GB
Uptime: 3d 14h 22m
```

```bash
# Comprehensive status
openclaw status --all
```

**Output:**
```
┌─────────────────────────────────────────────────────────────┐
│ OpenClaw Status                                              │
├─────────────────────────────────────────────────────────────┤
│ Gateway         Running on port 18789                        │
│ Uptime          3 days, 14 hours                            │
│ Sessions        47 active, 1,234 total                       │
│ Memory          156 MB                                       │
├─────────────────────────────────────────────────────────────┤
│ Channels                                                     │
│   Telegram      ✓ Connected (@YourBrandBot)                 │
│   WhatsApp      ✓ Connected (+1234567890)                   │
├─────────────────────────────────────────────────────────────┤
│ Models                                                       │
│   Primary       moonshot/kimi-k2.5 (available)              │
│   Fallback      gemini-2.0-flash (available)                │
└─────────────────────────────────────────────────────────────┘
```

```bash
# Follow logs in real-time
openclaw logs --follow
```

### Monitoring Commands Reference

| Command | Purpose |
|---------|---------|
| `openclaw health` | Quick status check |
| `openclaw status --all` | Comprehensive status |
| `openclaw logs --follow` | Real-time log output |
| `openclaw doctor` | Diagnose configuration issues |
| `openclaw security audit` | Check security posture |

## Cost Comparison Summary

| Option | Monthly Cost | Pros | Cons |
|--------|--------------|------|------|
| **Local PM2** | $0 (electricity) | Simple setup, fast | Computer must stay on |
| **Oracle Free** | $0 | True 24/7, ARM capable | Setup complexity, capacity limits |
| **DigitalOcean** | $6 | Easy UI, good docs | Monthly cost |
| **Hetzner** | $4 | Cheapest paid, Docker-friendly | EU-focused |
| **Linode** | $5 | Reliable, good support | Monthly cost |

For most users, we recommend starting with **PM2 locally** to ensure everything works, then graduating to **Oracle Cloud** when you want true independence from your local machine.

## Try With AI

### Prompt 1: Deployment Analysis

```
I want my AI Employee running 24/7. Currently my computer is on about 12 hours
a day. Analyze my options: Should I use PM2 locally, deploy to Oracle Cloud,
or consider a paid VPS? What factors should I consider?
```

**What you're learning:** This prompt tests your AI Employee's understanding of deployment architecture. You are evaluating whether it can reason about your specific constraints (12-hour availability) and recommend appropriate solutions. Pay attention to whether it asks clarifying questions about your requirements (reliability needs, technical comfort, budget) or jumps to a recommendation.

### Prompt 2: Health Check Discussion

```
Walk me through how to verify you're running correctly. What commands should
I use to check your health? What would indicate a problem? What would trigger
an automatic restart?
```

**What you're learning:** This prompt tests operational understanding. Your AI Employee should explain its own monitoring capabilities, demonstrating self-awareness of the infrastructure it runs on. A good response distinguishes between health checks (is it running?) and functionality checks (is it working correctly?).

**Important:** Deployment is advanced work. If you encounter issues, the troubleshooting commands in the Oracle Cloud documentation (referenced in this lesson) cover the most common problems. Start with PM2 locally to build confidence before attempting cloud deployment.
