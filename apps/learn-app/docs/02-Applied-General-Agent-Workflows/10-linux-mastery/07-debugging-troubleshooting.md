---
sidebar_position: 7
chapter: 10
lesson: 7
title: "Debugging & Troubleshooting"
description: "Diagnose production issues systematically using logs, network tools, and system monitoring. When agents fail, you'll know why."
keywords: ["debugging", "troubleshooting", "journalctl", "logs", "network diagnostics", "system monitoring"]
duration_minutes: 75

# HIDDEN SKILLS METADATA
skills:
  - name: "System Log Analysis with journalctl"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Troubleshooting"
    measurable_at_this_level: "Student can diagnose service failures by analyzing journalctl logs and identifying error patterns"

  - name: "Real-Time Log Monitoring"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Troubleshooting"
    measurable_at_this_level: "Student can stream and monitor log output in real-time using tail -f to observe agent behavior"

  - name: "Network Connectivity Diagnostics"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Troubleshooting"
    measurable_at_this_level: "Student can systematically diagnose network issues using curl, ping, ip addr, and netstat to isolate failure points"

  - name: "Resource Usage Monitoring"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Troubleshooting"
    measurable_at_this_level: "Student can identify disk space issues and runaway processes using df, du, and process monitoring tools"

learning_objectives:
  - objective: "Read and analyze system logs using journalctl to diagnose service failures"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Given a failing systemd service, student uses journalctl to identify the root cause error"

  - objective: "Monitor log output in real-time using tail -f to observe agent behavior"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student streams agent logs and identifies specific events as they occur"

  - objective: "Diagnose network connectivity issues systematically using curl, wget, ping, ip addr, and netstat"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Given a connectivity complaint, student isolates whether problem is local, network, or remote"

  - objective: "Monitor disk usage and identify space-consuming directories using df -h and du"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student identifies which directories are consuming disk space and recommends cleanup actions"

cognitive_load:
  new_concepts: 8
  concepts_list:
    - "journalctl log filtering and analysis"
    - "Real-time log streaming with tail -f"
    - "Network connectivity testing with curl/wget"
    - "Network interface diagnostics with ip addr"
    - "Network connection monitoring with netstat"
    - "Disk usage analysis with df -h"
    - "Directory size analysis with du"
    - "Systematic diagnostic methodology"
  assessment: "8 concepts (within B2 limit of 7-10) ✓"

teaching_approach: "Systematic diagnosis with AI collaboration (Learn Methods → Practice Scenarios → AI Refines Approach)"
modality: "Hands-On Diagnosis with AI Partnership"

differentiation:
  extension_for_advanced: "Explore advanced journalctl features like --since, --until, and journal-level filtering, or compare debugging tools (strace for system calls, lsof for open files)"
  remedial_for_struggling: "Focus on one diagnostic category at a time. Start with basic journalctl reading, then network testing, then disk monitoring. Practice each category independently before combining."

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-02-08"
version: "1.0.0"
---

# Debugging & Troubleshooting

## Your Agent Failed. Now What?

In Lessons 1-6, you built a complete Linux environment for running AI agents: modern terminal, persistent sessions, automation scripts, security hardening, and systemd services. You can deploy agents that run reliably and securely.

**But agents fail.** Services crash. Network timeouts occur. Disk space fills up. When your Digital FTE stops working at 3 AM, you need to diagnose the issue—not stare at error messages helplessly.

Production debugging isn't about memorizing commands. It's about **systematic diagnosis**:
1. Gather evidence (logs, metrics, error messages)
2. Isolate the problem (network? disk? permissions? code?)
3. Fix the root cause (not just restart the service)

This lesson teaches you the diagnostic workflow that separates "hope it works" from "know why it failed."

---

## Phase 1: Execute - Log Analysis with journalctl

Systemd services log everything. When something fails, the answer is usually in the logs.

### Activity 1.1: Read Service Logs

**Check if a service is running:**

```bash
systemctl status customer-support-agent
```

**If it shows "failed" or "inactive," read the logs:**

```bash
# Show all logs for this service
journalctl -u customer-support-agent

# Show last 50 lines (most recent)
journalctl -u customer-support-agent -n 50

# Follow logs in real-time (like tail -f)
journalctl -u customer-support-agent -f
```

**Press Ctrl+C** to stop following logs.

**What you're seeing:** Each log entry has:
- Timestamp (when it happened)
- Process name (what generated it)
- Message (the actual log)

### Activity 1.2: Filter Logs by Severity

**Show only errors and warnings:**

```bash
journalctl -u customer-support-agent -p err -p warn
```

**Priority levels:**
- `emerg` (0): System is unusable
- `alert` (1): Immediate action required
- `crit` (2): Critical condition
- `err` (3): Error condition
- `warning` (4): Warning condition
- `notice` (5): Normal but significant
- `info` (6): Informational
- `debug` (7): Debug-level messages

### Activity 1.3: Filter by Time Range

**Show logs from today:**

```bash
journalctl -u customer-support-agent --since today
```

**Show logs from the last hour:**

```bash
journalctl -u customer-support-agent --since "1 hour ago"
```

**Show logs between specific times:**

```bash
journalctl -u customer-support-agent --since "2026-02-08 14:00" --until "2026-02-08 15:00"
```

### Activity 1.4: Real-World Diagnostic Scenario

**Scenario:** Your customer support agent keeps crashing after 10 minutes.

**Your investigation:**

```bash
# Check current status
systemctl status customer-support-agent
# Output: Active: active (running)

# But it crashes periodically. Check logs from last hour
journalctl -u customer-support-agent --since "1 hour ago" -n 100
```

**Typical crash log output:**

```
Feb 08 14:32:15 server python[12345]: MemoryError: Unable to allocate memory
Feb 08 14:32:15 server systemd[1]: customer-support-agent.service: Main process exited, code=exited, status=1/FAILURE
Feb 08 14:32:15 server systemd[1]: customer-support-agent.service: Failed with result 'exit-code'
Feb 08 14:32:16 server systemd[1]: customer-support-agent.service: Service hold-off time over, scheduling restart.
Feb 08 14:32:16 server systemd[1]: customer-support-agent.service: Scheduled restart job, restart counter is at 5.
```

**What you learned:** The agent is running out of memory (`MemoryError`). Systemd keeps restarting it, but it crashes again. This isn't a code bug—it's a resource constraint. You need more RAM or to reduce memory usage.

**Output:** You identified the root cause (memory exhaustion) from logs, not guesswork.

---

## Phase 2: Three Roles Demonstration—Diagnostic Intelligence

Now we move from mechanical commands to intelligent diagnosis. This is where AI helps you think like a senior sysadmin.

### Scenario 1: Learning Diagnostic Patterns

**What you ask AI:**

```
I'm debugging agent failures and my journalctl shows:

Feb 08 14:32:15 server python[12345]: MemoryError: Unable to allocate memory
Feb 08 14:32:15 server systemd[1]: customer-support-agent.service: Main process exited, code=exited, status=1/FAILURE

I see "MemoryError" but I'm not sure if this means:
1. The server has no RAM left
2. This specific process hit a memory limit
3. There's a memory leak in the code

How do I distinguish between these causes? What commands should I run next?
```

**What AI teaches you:**

```
Great question! These are three different problems. Here's how to diagnose:

## 1. Server-wide RAM exhaustion
Check total system memory:
free -h

If "Available" is near 0, the entire server is out of RAM.

## 2. Process memory limit (systemd resource limits)
Check if your service has a MemoryMax limit:
systemctl show customer-support-agent | grep Memory

If MemoryMax=500M and your agent tries to use 600M, it gets killed.

## 3. Memory leak (code keeps allocating)
Monitor the process over time:
watch -n 5 'ps aux | grep customer-support'

If memory usage keeps growing (200MB → 400MB → 800MB), you have a leak.

## Your next diagnostic step:
Run all three checks above. Report back what you find, and I'll help you identify which problem you're facing.
```

**What you learned:** AI taught you a **systematic diagnostic framework**—check server memory, then service limits, then process leaks. You didn't know this diagnostic order before.

### Scenario 2: Explaining Your Context to AI

Now you have specific deployment constraints the AI doesn't know about.

**What you tell AI:**

```
Thanks for the diagnostic framework. Here's my context:

I'm running 3 agents on a $5/month VPS with 1GB RAM. Each agent
uses ~200MB normally. I can't upgrade the server—budget is fixed.

When I check free -h, I see 150MB available. When agents process
heavy workloads, they crash with MemoryError.

I think my options are:
1. Reduce memory usage per agent
2. Add swap space (I've heard this is dangerous on VPS)
3. Kill one agent and run only 2

What do you recommend? Swap space seems risky but I need all 3 agents running.
```

**What AI suggests:**

```
Good context. Let me address your options:

## Option 1: Reduce memory usage (BEST)
- Reduce model context window (smaller models = less RAM)
- Process batches of 10 instead of 100
- Clear conversation history after 24 hours
Effort: Medium | Impact: 20-30% reduction

## Option 2: Add swap space (RISKY on VPS)
You're right to be cautious. Swap on VPS can cause:
- Disk I/O contention (swap + database = slow)
- OOM kill if swap fills (kills random processes)
- VPS provider may throttle swap I/O

BUT: If your agents rarely spike above RAM, small swap (512M) helps
survive temporary spikes without crashes.

Tradeoff: Survivability vs performance risk.

## Option 3: Run 2 agents (ACCEPTING LIMITATION)
You lose 33% of your capacity. But both run reliably.

## My recommendation based on your budget constraint:
1. Add 512M swap as safety net (temporary spikes)
2. Optimize memory usage in your agents (batch processing)
3. Monitor for 1 week. If swap never fills, you're safe.
```

**What AI learned:** AI adapted to **your budget constraint** (can't upgrade server) and safety concern (knows swap is risky). You taught AI your deployment constraints.

### Scenario 3: Iterating on Diagnostic Approach Together

Here's where both of you iterate toward optimal solution.

**Your initial diagnostic script:**

```bash
#!/bin/bash
# Basic health check
echo "=== Memory ==="
free -h
echo "=== Disk ==="
df -h
echo "=== Services ==="
systemctl status customer-support-agent
```

**You ask AI:**

```
I run this script manually when agents fail. But I only find out
hours later when someone complains. How can I make this proactive?
```

**AI suggests:**

```
Turn it into automated monitoring with alerts:

#!/bin/bash
# proactive-monitor.sh
THRESHOLD=80  # Alert at 80% memory usage

MEMORY_PERCENT=$(free | awk '/Mem/{printf("%.0f"), $3/$2*100}')
if [ $MEMORY_PERCENT -gt $THRESHOLD ]; then
  echo "WARNING: Memory at ${MEMORY_PERCENT}%" | logger -t agent-monitor
fi

DISK_PERCENT=$(df / | awk 'NR==2{print $5}' | sed 's/%//')
if [ $DISK_PERCENT -gt $THRESHOLD ]; then
  echo "WARNING: Disk at ${DISK_PERCENT}%" | logger -t agent-monitor
fi

# Check service status
if ! systemctl is-active --quiet customer-support-agent; then
  echo "ERROR: Agent not running" | logger -t agent-monitor
fi
```

**You think:** "This logs warnings, but I still won't see them unless I check logs."

**AI refines:**

```
Good point. Add email/webhook alerts:

# Install mailutils for email alerts
sudo apt install mailutils

# In the script, replace echo with:
echo "WARNING: Memory at ${MEMORY_PERCENT}%" | \
  mail -s "Server Alert" you@example.com

# Or use webhook for Slack/Discord:
curl -X POST $WEBHOOK_URL -d "{\"text\":\"Memory at ${MEMORY_PERCENT}%\"}"
```

**You add constraint:**

```
I don't want emails for every warning. Sometimes memory spikes
temporarily and recovers. Can you make this smarter?
```

**AI adapts:**

```
Yes! Add hysteresis (persistent state):

# Only alert if problem persists for 3 checks
STATE_FILE=/tmp/monitor-state

if [ $MEMORY_PERCENT -gt $THRESHOLD ]; then
  if [ -f "$STATE_FILE" ]; then
    COUNT=$(cat "$STATE_FILE")
    if [ "$COUNT" -ge 3 ]; then
      echo "PERSISTENT WARNING: Memory at ${MEMORY_PERCENT}%" | \
        logger -t agent-monitor
      rm "$STATE_FILE"  # Reset after alerting
    else
      echo $((COUNT + 1)) > "$STATE_FILE"
    fi
  else
    echo "1" > "$STATE_FILE"
  fi
else
  rm "$STATE_FILE"  # Reset if recovered
fi
```

**What emerged:** A monitoring system with **hysteresis**—only alerts on persistent problems, not temporary spikes. Neither of you had this initially:
- You didn't know about hysteresis pattern
- AI didn't know you wanted to avoid alert spam
- Together, you created **smart monitoring** that reduces false positives

---

## Phase 3: Apply - Network Diagnostics

When agents can't reach APIs, databases, or external services, you need to isolate where the connection fails.

### Activity 3.1: The Diagnostic Hierarchy

Network problems occur at different layers. Diagnose systematically:

**Layer 1: Local interface (is your network up?)**

```bash
# Check network interfaces
ip addr show

# Look for:
# - Interface is UP (not DOWN)
# - Has an IP address (inet line)
# - Not in "UNKNOWN" state

# Example output:
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0
```

**If interface is DOWN** → Network configuration problem, not agent problem

**Layer 2: Local connectivity (can you reach your gateway?)**

```bash
# Ping your default gateway
ping -c 3 192.168.1.1

# Output:
PING 192.168.1.1 (192.168.1.1): 56 data bytes
64 bytes from 192.168.1.1: icmp_seq=0 ttl=64 time=2.3 ms
64 bytes from 192.168.1.1: icmp_seq=1 ttl=64 time=2.1 ms
```

**If ping fails** → Local network problem (router, switch, cable)

**Layer 3: DNS resolution (can you resolve hostnames?)**

```bash
# Test DNS
nslookup api.openai.com

# Output:
Server:  8.8.8.8
Address: 8.8.8.8#53

Name:    api.openai.com
Address: 104.16.132.229
```

**If DNS fails** → DNS configuration problem (`/etc/resolv.conf`)

**Layer 4: Remote connectivity (can you reach the service?)**

```bash
# Test HTTP connectivity
curl -I https://api.openai.com

# Output:
HTTP/2 200
content-type: application/json
...
```

**If curl fails** → Remote service problem or firewall blocking

### Activity 3.2: Real-World Network Diagnostic

**Scenario:** Agent reports "Connection refused" when calling external API.

**Your diagnostic sequence:**

```bash
# Step 1: Is network interface up?
ip addr show eth0
# Output: state UP ✓

# Step 2: Can we reach gateway?
ping -c 2 192.168.1.1
# Output: 2 packets transmitted, 2 received, 0% packet loss ✓

# Step 3: Can we resolve hostname?
nslookup api.external-service.com
# Output: Address: 203.0.113.42 ✓

# Step 4: Can we reach the service?
curl -I https://api.external-service.com
# Output: curl: (7) Failed to connect to api.external-service.com port 443
```

**Diagnosis:** Steps 1-3 passed, but step 4 failed. The problem is **remote connectivity**, not local network or DNS.

**Next check:** Is it a firewall problem?

```bash
# Test with telnet (if available)
telnet api.external-service.com 443

# Output:
Trying 203.0.113.42...
telnet: Unable to connect to remote host: Connection refused
```

**Conclusion:** The remote server is refusing connections (not your firewall). Either:
- The service is down
- Your IP is blocked
- The service port changed

**Action:** Contact service provider or check status page—not a local problem.

---

## Phase 4: Apply - Disk Space Monitoring

Runaway logs, cached data, and agent outputs can fill disk space. When disk is full, services crash mysteriously.

### Activity 4.1: Check Disk Usage

```bash
# Human-readable disk usage
df -h

# Output:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G   19G  512M  98% /
```

**If Use% is above 90%** → You're in danger zone

**If Use% is above 95%** → Services may crash soon

### Activity 4.2: Find Space Hogs

```bash
# Show directory sizes in current location
du -h --max-depth=1 | sort -h

# Output:
4.0K    ./ssh
8.0K    ./config
16M     ./logs
256M    ./agent-cache
4.2G    ./agent-outputs
15G     ./var/lib/docker  # Space hog!
```

**Find the largest directories:**

```bash
# Show top 10 largest directories
du -h / | sort -h | tail -10

# Or use ncdu (install first: sudo apt install ncdu)
ncdu /
```

### Activity 4.3: Monitor Agent Logs

**Real-world scenario:** Agent logs are growing 1GB per day.

**Check log sizes:**

```bash
# Find all log files larger than 100MB
find /var/agents -name "*.log" -size +100M -exec ls -lh {} \;

# Output:
-rw-r--r-- 1 agent agent 1.2G Feb 8 15:32 /var/agents/customer-support/logs/app.log
```

**View the log in real-time:**

```bash
tail -f /var/agents/customer-support/logs/app.log
```

**Clean up old logs (automated):**

```bash
# Create log rotation script
cat > /etc/logrotate.d/agent-logs << 'EOF'
/var/agents/*/logs/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
    create 0640 agent agent
}
EOF

# Test log rotation
logrotate -d /etc/logrotate.d/agent-logs

# Force immediate rotation
logrotate -f /etc/logrotate.d/agent-logs
```

**What you learned:** Log rotation automatically compresses and deletes old logs, preventing disk space issues.

---

## Understanding: Diagnostic Tool Comparison

| Tool | What It Checks | When to Use | Example Output |
|------|----------------|-------------|----------------|
| **journalctl** | Systemd service logs | Service won't start/crashes | "MemoryError: Unable to allocate" |
| **tail -f** | Real-time log monitoring | Watching agent behavior | Lines appearing as events occur |
| **curl/wget** | HTTP connectivity | Testing API reachability | HTTP/2 200 or "Connection refused" |
| **ping** | ICMP connectivity | Testing local network | "64 bytes from... time=2.3 ms" |
| **ip addr** | Network interface status | No network at all | "state UP" or "state DOWN" |
| **netstat** | Network connections | Port listening/blocked | "0.0.0.0:8000 LISTEN" |
| **df -h** | Disk space usage | Services crashing mysteriously | "/dev/sda1 98% /" |
| **du** | Directory sizes | Finding space hogs | "15G ./var/lib/docker" |

**Diagnostic Decision Tree:**

```
Service won't start → journalctl
Agent can't reach API → curl → ping → ip addr
Disk full warnings → df -h → du
Slow performance → htop → iotop
```

---

## Safety Note

**Never delete system files** while cleaning up disk space. Focus on:
- Application logs (`/var/agents/*/logs/`)
- Cached data (`/tmp/`, cache directories)
- Old backups (verify you have newer backups first)

**Before running any delete command**, use `ls` to verify the files. Once deleted, recovery is difficult.

---

## Try With AI

Let's explore advanced diagnostic scenarios with AI assistance.

**🔍 Debug Mysterious Service Failures:**

```
I have a systemd service that runs for exactly 47 minutes, then crashes.
I've checked journalctl and it just says "Main process exited, code=exited,
status=1/FAILURE" with no error message before that.

The service is a Python agent that processes customer tickets. It works
fine for 47 minutes, then dies without any error logs.

What diagnostic approach would you take to identify what's happening
at that 47-minute mark? I'm stuck on how to debug a problem that
leaves no trace in logs.
```

**What you're learning:** Advanced diagnostic techniques for intermittent failures—using strace, process monitoring, and timing analysis to catch problems that leave no direct evidence.

**🌐 Complex Network Issues:**

```
I'm seeing intermittent network failures. Sometimes my agent can reach
the external API (200 OK responses), other times it times out after
30 seconds.

What's weird is:
- ping to the API server works 100% of the time
- curl sometimes works, sometimes times out
- Other services on the same server don't have this problem
- It happens more during "peak hours" (9-11 AM, 2-4 PM)

I suspect it might be:
1. Rate limiting (but I'm under the documented limits)
2. Network congestion (but ping is stable)
3. Some kind of connection pooling issue in my code

Help me design a diagnostic strategy to isolate which of these (or
something else) is the cause. What should I measure and when?
```

**What you're learning:** How to design targeted diagnostic experiments for intermittent problems—measuring at the right time, capturing the right data, and isolating variables systematically.

**⚡ Build Automated Diagnostics:**

```
I want to create a "health check dashboard" for my agents that runs
every 5 minutes and reports:
1. Service status (running or not)
2. Memory usage trend (growing? stable?)
3. Disk space (how much free?)
4. Network connectivity (can reach APIs?)

But I don't want it to just collect data—I want it to:
- Alert me only when problems are persistent (not temporary spikes)
- Show me trends (not just current state)
- Suggest likely causes based on patterns

Help me design this monitoring system. What should I track, how
should I store it, and what pattern-matching rules would help identify
common problems automatically?
```

**What you're learning:** Transforming reactive debugging into proactive monitoring—designing systems that detect patterns, predict failures, and suggest diagnoses before problems become critical.
