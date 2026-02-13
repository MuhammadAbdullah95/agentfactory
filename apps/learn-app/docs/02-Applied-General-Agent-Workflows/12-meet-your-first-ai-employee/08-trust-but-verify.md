---
sidebar_position: 8
title: "Lesson 8: Trust But Verify"
description: "Configure Human-in-the-Loop approval workflows for sensitive operations"
keywords: [hitl, approvals, human in the loop, safety, governance, allowlist, exec approvals]
chapter: 12
lesson: 8
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding Trust Gradients"
    proficiency_level: "B2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can explain the trust spectrum from full manual to full autonomous and identify appropriate positions for different operation types"

  - name: "Configuring Approval Workflows"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can configure per-action approval requirements using exec-approvals.json and understand the interaction between security modes, ask modes, and allowlists"

  - name: "Operating Approval Commands"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student can use approval commands (/approve, /deny) effectively via chat channels to manage pending agent actions"

learning_objectives:
  - objective: "Explain the trust spectrum and identify where HITL sits between full manual and full autonomous operation"
    proficiency_level: "B2"
    bloom_level: "Understand"
    assessment_method: "Student can place different operation types (read, send, delete) on the trust spectrum and justify their placement"

  - objective: "Configure per-action approval requirements using security modes, ask modes, and allowlists"
    proficiency_level: "C1"
    bloom_level: "Apply"
    assessment_method: "Student produces working exec-approvals.json configuration with appropriate settings for their use case"

  - objective: "Use approval commands through chat channels to manage pending agent actions"
    proficiency_level: "C1"
    bloom_level: "Apply"
    assessment_method: "Student successfully approves and denies actions via Telegram using the /approve command"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (trust spectrum, security modes, ask modes, allowlists, approval flow, audit logging) within B2-C1 range of 4-7"

differentiation:
  extension_for_advanced: "Create custom approval rules based on content patterns or recipient domains; implement webhook notifications for approval events"
  remedial_for_struggling: "Use the elevated mode preset with default safe bins; focus on understanding the approval flow before customizing"
---

# Lesson 8: Trust But Verify

Your AI Employee can do a lot. It can read your emails, analyze documents, search the web, execute code, and send messages on your behalf. In Lesson 7, you connected it to real services and expanded its senses through watchers and webhooks.

Now comes the critical question every manager asks: **Should it do everything automatically?**

The answer separates amateur AI deployments from production-ready systems. Amateurs either lock everything down (defeating the purpose of automation) or let everything run free (inviting disaster). Professionals understand that trust is a gradient, and the right position on that gradient depends on the stakes of each action.

This lesson introduces Human-in-the-Loop (HITL) approval workflows. You will learn to configure your AI Employee so that routine actions execute instantly while sensitive operations pause for your explicit approval. The result is an employee you can trust with increasing autonomy over time, with safety rails that prevent catastrophic mistakes.

## The Trust Spectrum

Think about how you delegate to human employees. A new hire might need approval for every customer email. After three months, you trust them with routine correspondence but still review anything involving refunds. After a year, they handle most situations independently, and you only intervene for escalations.

AI Employees work the same way. The trust spectrum runs from complete manual control to complete autonomy:

```
Full Manual ────────────────────────────────────────── Full Autonomous
     │                                                        │
Every action                                            No approvals
requires approval                                       (dangerous!)
     │                                                        │
     │                      HITL sits here                    │
     │                           │                            │
     │          ┌────────────────┴───────────────┐            │
     │          │                                │            │
     │   Trust common actions,           Verify sensitive     │
     │   verify sensitive ones           operations only      │
     │                                                        │
     └────────────────────────────────────────────────────────┘
```

**Full Manual** means every action requires your approval. Your AI Employee asks permission to read a file, search the web, or run any command. This is safe but defeats the purpose of automation. You become the bottleneck, and the employee sits idle waiting for you.

**Full Autonomous** means the agent acts without asking. This is efficient but dangerous. A misunderstood instruction could delete important files, send embarrassing emails, or leak confidential information before you notice.

**HITL (Human-in-the-Loop)** sits in the productive middle. Common, reversible, low-risk actions execute immediately. Sensitive, irreversible, or high-stakes actions pause for your explicit approval. You stay in control of what matters while delegation handles what does not.

The art of HITL configuration is choosing where on this spectrum each type of action belongs.

## Security Modes

OpenClaw provides three security modes that determine baseline behavior for command execution:

| Mode | Behavior | Use When |
|------|----------|----------|
| `deny` | Block all host exec requests | Testing, or when you want zero shell access |
| `allowlist` | Allow only explicitly permitted commands | Production (recommended default) |
| `full` | Allow everything without approval | Trusted development environments only |

**Deny mode** is the most restrictive. No commands execute on the host machine regardless of other settings. Use this when you are testing agent behavior without real execution, or when you want to completely sandbox the agent.

**Allowlist mode** is the production standard. Commands execute only if they match patterns you have explicitly permitted. Everything else either gets blocked or triggers an approval prompt, depending on your ask settings.

**Full mode** grants complete access. This is equivalent to elevated privileges and skips all approval workflows. Use this only in development environments where you trust the agent completely and accept all risks.

### Setting Security Mode

The security mode lives in your exec-approvals configuration:

```json
{
  "version": 1,
  "defaults": {
    "security": "allowlist"
  }
}
```

This sets the baseline. You can override per-agent if you have multiple agents with different trust levels:

```json
{
  "agents": {
    "main": {
      "security": "allowlist"
    },
    "untrusted-experiment": {
      "security": "deny"
    }
  }
}
```

## Ask Modes

Within allowlist security mode, the ask setting determines when to prompt you for approval:

| Mode | Behavior | Result |
|------|----------|--------|
| `off` | Never prompt | Commands either execute (if allowlisted) or fail silently |
| `on-miss` | Prompt only when allowlist does not match | Allowlisted commands run freely; unknown commands wait for approval |
| `always` | Prompt on every command | Maximum visibility but high friction |

**Off** disables approval prompts entirely. If a command matches the allowlist, it runs. If it does not match, it fails. This is efficient but provides no opportunity to approve one-off commands.

**On-miss** (recommended) strikes the balance. Commands you have explicitly permitted run without interruption. Commands that do not match trigger an approval request, giving you the choice to allow once, always allow (add to allowlist), or deny.

**Always** prompts for every command regardless of allowlist status. This provides maximum visibility but creates approval fatigue. Use this temporarily when auditing agent behavior or onboarding a new workflow.

### Ask Fallback

What happens when approval is required but you are not available to respond? The askFallback setting handles this:

| Fallback | Behavior |
|----------|----------|
| `deny` | Block the request (safe default) |
| `allowlist` | Allow if it matches allowlist, block otherwise |
| `full` | Allow everything (dangerous) |

Set askFallback to `deny` unless you have a specific reason to be more permissive. This ensures that if your phone dies or you are in a meeting, the agent waits rather than taking potentially harmful actions.

```json
{
  "defaults": {
    "security": "allowlist",
    "ask": "on-miss",
    "askFallback": "deny"
  }
}
```

## Building Your Allowlist

The allowlist is where you encode trust. Each entry is a glob pattern matching executable paths that the agent can run without approval:

```json
{
  "agents": {
    "main": {
      "allowlist": [
        {
          "pattern": "/opt/homebrew/bin/rg"
        },
        {
          "pattern": "~/.local/bin/*"
        },
        {
          "pattern": "~/Projects/**/bin/bird"
        }
      ]
    }
  }
}
```

Patterns use glob syntax:
- Exact paths: `/opt/homebrew/bin/rg`
- Wildcards: `~/.local/bin/*` (any binary in that directory)
- Recursive wildcards: `~/Projects/**/bin/bird` (bird binary anywhere under Projects)

### Safe Bins for Common Tools

Some commands are safe because they only operate on stdin and cannot touch files directly. The `safeBins` setting auto-allows these without explicit allowlist entries:

Default safe bins: `jq`, `grep`, `cut`, `sort`, `uniq`, `head`, `tail`, `tr`, `wc`

These tools can pipe data through transformations but cannot read or write files by path. When the agent runs `echo '{"name":"test"}' | jq .name`, it works without approval because jq is a safe bin operating on piped input.

Safe bins reject positional file arguments. If the agent tries `jq . config.json`, it will not work through safe bins because that accesses a file path directly.

### Auto-Allow Skill CLIs

When enabled, `autoAllowSkills` treats executables referenced by known skills as allowlisted. This is convenient when skills need specific binaries to function:

```json
{
  "agents": {
    "main": {
      "autoAllowSkills": true
    }
  }
}
```

Disable this if you want strict manual control over every executable, even those required by skills you have installed.

## The Approval Flow

When the agent attempts an action that requires approval, here is what happens:

```
Agent wants to run: git push origin main
              │
              ▼
       Is security=full?
              │
     ┌────────┴────────┐
     │ Yes             │ No
     ▼                 ▼
Execute          Check allowlist
immediately            │
              ┌────────┴────────┐
              │ Match           │ No match
              ▼                 ▼
         Execute          Check ask mode
         immediately            │
                     ┌──────────┼──────────┐
                     │ off      │ on-miss  │ always
                     ▼          ▼          ▼
                   Deny    Send approval  Send approval
                           request        request
                                │              │
                                └──────┬───────┘
                                       ▼
                           You receive notification:
                           "Approve? /approve or /deny"
                                       │
                        ┌──────────────┼──────────────┐
                        │              │              │
                        ▼              ▼              ▼
                   /approve       /approve 5MIN    /deny
                   allow-once     allow-always      │
                        │              │            ▼
                        ▼              ▼         Block and
                   Execute        Add to         notify
                   this time      allowlist +    agent
                                  execute
```

The notification arrives wherever you have configured approval forwarding. Most commonly, this is Telegram, but it can be Slack, Discord, or any chat channel.

## Approval Commands

When an approval request arrives, you respond with one of these commands:

**`/approve <id> allow-once`** - Execute this specific action right now, but do not remember the permission. The next time the agent tries the same command, it will ask again.

**`/approve <id> allow-always`** - Execute this action and add the pattern to the allowlist. Future identical commands will run without asking.

**`/deny <id>`** - Block this action and notify the agent. The agent will receive an "Exec denied" event and can inform you or attempt an alternative approach.

The `<id>` is the approval identifier included in the notification. If you are responding quickly and there is only one pending approval, some interfaces let you omit the id.

### Viewing Pending Approvals

If you have been away and multiple approvals accumulated:

```
/pending
```

This lists all pending approval requests with their ids, the requested commands, and how long they have been waiting. You can then approve or deny each one.

### Timeout Behavior

Approval requests do not wait forever. After the configured timeout (default: 5 minutes), the request is treated as denied due to timeout. The agent receives an "approval timeout" event.

This prevents the agent from hanging indefinitely when you are unavailable. It also prevents stale approvals from executing hours later when the context has changed.

## Configuring Approval Forwarding

To receive approval requests on your phone, configure forwarding to your preferred channel:

```json
{
  "approvals": {
    "exec": {
      "enabled": true,
      "mode": "targets",
      "targets": [
        { "channel": "telegram", "to": "123456789" }
      ]
    }
  }
}
```

The `to` field is your Telegram user ID (not username). The agent sends approval requests directly to your Telegram chat, and you respond with /approve or /deny right there.

You can configure multiple targets for redundancy:

```json
{
  "targets": [
    { "channel": "telegram", "to": "123456789" },
    { "channel": "slack", "to": "U12345678" }
  ]
}
```

The first response wins. If you approve from Telegram, the Slack notification becomes moot.

## Approval Best Practices

### Start Strict, Relax Over Time

Begin with `ask: "always"` for a new workflow. Watch what the agent requests. After a week, you will have a clear picture of routine versus exceptional actions. Switch to `ask: "on-miss"` and build your allowlist based on observed patterns.

This mirrors how you would supervise a new human employee. Close supervision initially, then increasing autonomy as trust builds.

### Categorize Actions by Reversibility

| Action Type | Reversibility | Recommended Approval |
|-------------|---------------|---------------------|
| Read operations | Fully reversible (no side effects) | Never require approval |
| Search/query | Fully reversible | Never require approval |
| Create/add | Usually reversible (can delete later) | Allowlist common patterns |
| Modify/update | Partially reversible (can undo with effort) | Allowlist routine, approve unusual |
| Send/publish | Irreversible (cannot unsend) | Always require approval |
| Delete/destroy | Irreversible | Always require approval |
| Financial | Irreversible | Always require approval |

The principle: **reversible actions can be allowlisted; irreversible actions should require approval until trust is very high.**

### Review Your Allowlist Periodically

Each allowlist entry tracks when it was last used. Review monthly and remove patterns that have not been used. This keeps your allowlist minimal and reduces attack surface.

```json
{
  "allowlist": [
    {
      "pattern": "/opt/homebrew/bin/rg",
      "lastUsedAt": 1737150000000,
      "lastUsedCommand": "rg -n TODO"
    }
  ]
}
```

If a pattern has not been used in 90 days, consider removing it. You can always approve-always to add it back if needed.

### Audit Logging

All approvals are logged automatically. The log includes:
- What action was requested
- Who approved it (your user ID)
- When the approval happened
- Whether it was allow-once or allow-always

Review this log weekly to understand patterns:
- Are there actions you approve repeatedly that should be allowlisted?
- Are there denials that indicate the agent is misunderstanding intent?
- Are there approval timeouts indicating you need longer timeout or different notification channel?

## Per-Agent Configuration

If you run multiple agents with different trust levels, configure each independently:

```json
{
  "agents": {
    "main": {
      "security": "allowlist",
      "ask": "on-miss",
      "autoAllowSkills": true,
      "allowlist": [
        { "pattern": "~/.local/bin/*" }
      ]
    },
    "experimental": {
      "security": "allowlist",
      "ask": "always",
      "autoAllowSkills": false,
      "allowlist": []
    }
  }
}
```

Your main agent gets established trust. A new experimental agent starts with zero trust and everything requires approval.

Allowlists are per-agent. Approving a command for one agent does not grant that permission to other agents. This prevents privilege leakage between agents with different purposes.

## The Complete Configuration

Here is a production-ready exec-approvals.json combining everything:

```json
{
  "version": 1,
  "socket": {
    "path": "~/.openclaw/exec-approvals.sock",
    "token": "your-secure-token-here"
  },
  "defaults": {
    "security": "allowlist",
    "ask": "on-miss",
    "askFallback": "deny",
    "autoAllowSkills": false
  },
  "agents": {
    "main": {
      "security": "allowlist",
      "ask": "on-miss",
      "askFallback": "deny",
      "autoAllowSkills": true,
      "allowlist": [
        {
          "id": "ripgrep",
          "pattern": "/opt/homebrew/bin/rg"
        },
        {
          "id": "local-scripts",
          "pattern": "~/.local/bin/*"
        },
        {
          "id": "project-tools",
          "pattern": "~/Projects/**/bin/*"
        }
      ]
    }
  }
}
```

This configuration:
- Uses allowlist security mode (the production standard)
- Prompts only for non-allowlisted commands (on-miss)
- Denies requests when you are unavailable (askFallback: deny)
- Trusts skill CLIs for the main agent only
- Explicitly allows ripgrep, local scripts, and project tools

## Why This Matters for Digital FTEs

As you build toward Digital FTEs that operate independently, HITL approval becomes a critical governance layer. The difference between an AI assistant and a Digital FTE is not just capability but **accountability**.

When a human employee makes a decision, there is a paper trail. When an AI employee makes a decision, you need the same accountability. Approval logs provide that trail. They show what actions were taken, who authorized them, and when.

HITL also enables gradual autonomy expansion. You start with high supervision, observe the agent's judgment, and progressively grant more independence. This is exactly how you would promote a human employee from supervised to autonomous work.

The alternative, granting full autonomy immediately, is like hiring someone and leaving them alone on day one. Some people succeed at this. Most do not. And when they fail, you discover the failure through consequences rather than prevention.

Trust but verify is not about distrusting your AI Employee. It is about building trust systematically, with evidence, over time.

## Try With AI

### Prompt 1: Analyze Your Trust Profile

```
Help me think through which operations my AI Employee should be able to do
without approval versus which should require my explicit permission.

Here's what my AI Employee currently does:
[Describe your agent's main tasks - email, calendar, file management, etc.]

For each operation type, help me categorize:
- Is it reversible or irreversible?
- What's the worst-case outcome if it goes wrong?
- How often does it happen (daily, weekly, rarely)?

Then recommend: Should this be allowlisted, require approval, or be blocked entirely?
```

**What you're learning**: You're developing a risk assessment framework for AI delegation. By systematically analyzing reversibility, consequences, and frequency, you're building intuition for where to place different operations on the trust spectrum. This skill transfers to any AI governance decision.

### Prompt 2: Draft Your Configuration

```
Based on the trust profile we just discussed, help me write an exec-approvals.json
configuration file.

I want:
- Allowlist mode as the default (production-safe)
- Approval prompts forwarded to my Telegram at [your user ID]
- Safe bins enabled for common data processing
- Explicit allowlist entries for [list your common tools]

Generate the complete JSON configuration with comments explaining each section.
Then explain what will happen when my agent tries to:
1. Run 'rg' to search code
2. Send an email to a new contact
3. Delete a file I asked it to clean up
```

**What you're learning**: You're translating conceptual trust decisions into concrete configuration. The exercise of predicting system behavior for specific scenarios builds your mental model of how approval workflows operate. This is essential for debugging when things do not work as expected.

---

## Frequently Asked Questions

### What happens if I do not respond to an approval request?

After the timeout (default 5 minutes), the request is automatically denied. The agent receives an "approval timeout" event and can respond appropriately, such as informing you that the action could not be completed. This prevents indefinite waiting and ensures stale requests do not execute later.

### Can I approve actions from multiple devices?

Yes. If you configure multiple approval targets (Telegram and Slack, for example), you can respond from whichever device you have available. The first response wins, and subsequent responses to the same request are ignored.

### How do I remove something from my allowlist?

Edit your `~/.openclaw/exec-approvals.json` file directly and remove the pattern. Alternatively, use the Control UI if you have the macOS app. Changes take effect immediately without restart.

### What is the difference between security mode and ask mode?

Security mode determines the baseline policy: deny all, allow from allowlist, or allow everything. Ask mode determines when to prompt you for approval within the allowlist policy. Think of security as the outer boundary and ask as the approval behavior within that boundary.

### Should I use full security mode during development?

Only if you fully trust the agent and accept all risks. Full mode is convenient for rapid iteration but provides no safety net. Most developers use allowlist mode even during development, with a more permissive allowlist that gets tightened before production.
