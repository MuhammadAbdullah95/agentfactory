---
sidebar_position: 7
title: "Lesson 7: Connecting Real Services"
description: "Configure watchers for proactive monitoring - transforming your AI Employee from reactive assistant to alert sentinel"
keywords:
  [
    watchers,
    gmail watcher,
    file watcher,
    proactive agents,
    notifications,
    event-driven,
    openclaw,
  ]
chapter: 12
lesson: 7
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Event-Driven Agent Design"
    proficiency_level: "C1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can configure watchers for event-driven agent behavior with appropriate triggers and actions"

  - name: "Reactive vs Proactive Agent Patterns"
    proficiency_level: "B2"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Can compare reactive and proactive agent patterns and select appropriate approach for different use cases"

  - name: "Safety-Conscious Automation"
    proficiency_level: "C1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Safety"
    measurable_at_this_level: "Can evaluate automation configurations for safety risks and implement appropriate safeguards"

learning_objectives:
  - objective: "Distinguish reactive from proactive agent patterns and explain when each is appropriate"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Pattern comparison with use case matching"

  - objective: "Configure Gmail and File watchers with appropriate triggers and actions"
    proficiency_level: "C1"
    bloom_level: "Apply"
    assessment_method: "Working watcher configuration that responds to test events"

  - objective: "Evaluate automation configurations for safety and implement rate limiting"
    proficiency_level: "C1"
    bloom_level: "Evaluate"
    assessment_method: "Configuration rationale document explaining safety decisions"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (watcher architecture, trigger configuration, safety patterns) - moderate for C1 but manageable with prior OpenClaw familiarity"

differentiation:
  extension_for_advanced: "Create custom watcher triggers with complex filtering logic and conditional action chains"
  remedial_for_struggling: "Configure a single notify-only watcher for Gmail, verify it works, then expand"
---

# Connecting Real Services

In the previous lessons, you built skills and shaped your AI Employee's personality. But there is a fundamental limitation: your employee only works when you initiate. It sits idle, waiting for your command, while important emails arrive and files accumulate.

Human employees do not work this way. A good assistant notices when your inbox fills with urgent client emails. They see when important documents land in your Downloads folder. They bring things to your attention before you think to ask.

This lesson gives your AI Employee the same capability. You will configure watchers, background processes that monitor for events and trigger actions when conditions are met. By the end, your employee will notify you proactively when something important happens, even when you are not actively engaged.

## Reactive vs Proactive: A Fundamental Shift

Until now, your AI Employee has operated in reactive mode:

```
YOU                          AI EMPLOYEE
 │                               │
 │   "Check my email"            │
 │ ─────────────────────────────>│
 │                               │  (checks email)
 │   "You have 3 new messages"   │
 │ <─────────────────────────────│
 │                               │
```

You ask, it responds. Simple, safe, but limited. You must remember to check. Important things can wait hours while you focus on other work.

**Proactive mode** inverts the relationship:

```
GMAIL                        AI EMPLOYEE                    YOU
  │                               │                          │
  │   (new email arrives)         │                          │
  │ ─────────────────────────────>│                          │
  │                               │  (evaluates: important?) │
  │                               │  (yes: from boss)        │
  │                               │                          │
  │                               │   "Urgent email from     │
  │                               │    your boss just        │
  │                               │    arrived: Q1 report"   │
  │                               │ ─────────────────────────>│
  │                               │                          │
```

The AI Employee watches continuously. It notices events. It evaluates importance. It alerts you when something matters.

| Pattern       | Trigger        | Use Case                                 |
| ------------- | -------------- | ---------------------------------------- |
| **Reactive**  | Your request   | General questions, on-demand tasks       |
| **Proactive** | External event | Time-sensitive items, important arrivals |

Both patterns have their place. You still want reactive mode for most work. But for monitoring critical channels, proactive mode keeps you informed without constant manual checking.

## What Are Watchers?

Watchers are background processes that run alongside your AI Employee's gateway. They monitor specific sources for events and trigger actions when conditions match.

Think of watchers as your employee's eyes and ears:

| Watcher Type | What It Monitors            | Event Examples                            |
| ------------ | --------------------------- | ----------------------------------------- |
| **Gmail**    | Your email inbox            | New message, message from specific sender |
| **File**     | Directories on your machine | New file created, file modified           |
| **Calendar** | Your schedule               | Upcoming meeting, schedule conflict       |
| **Webhook**  | External services           | API notification, system alert            |

Each watcher runs independently, checking its source at configured intervals. When a trigger condition matches, the watcher creates an event that your AI Employee can act on.

### The Watcher Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    OPENCLAW GATEWAY                              │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    WATCHER MANAGER                        │  │
│  │                                                           │  │
│  │   ┌─────────┐    ┌─────────┐    ┌─────────┐             │  │
│  │   │  Gmail  │    │  File   │    │Calendar │    ...      │  │
│  │   │ Watcher │    │ Watcher │    │ Watcher │             │  │
│  │   └────┬────┘    └────┬────┘    └────┬────┘             │  │
│  │        │              │              │                    │  │
│  │        ▼              ▼              ▼                    │  │
│  │   ┌────────────────────────────────────────────────┐    │  │
│  │   │              EVENT QUEUE                        │    │  │
│  │   └─────────────────────┬──────────────────────────┘    │  │
│  │                         │                                │  │
│  └─────────────────────────│────────────────────────────────┘  │
│                            │                                    │
│                            ▼                                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                  ACTION DISPATCHER                        │  │
│  │                                                           │  │
│  │   notify  │  summarize  │  forward  │  analyze  │  ...  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                            │                                    │
│                            ▼                                    │
│                    ┌───────────────┐                           │
│                    │   TELEGRAM    │                           │
│                    │   (or other)  │                           │
│                    └───────────────┘                           │
└─────────────────────────────────────────────────────────────────┘
```

Watchers poll their sources, feed events into a queue, and the action dispatcher executes configured responses. The entire system runs asynchronously, so watchers do not block each other or your interactive sessions.

## Prerequisites: gog (Google CLI)

Gmail integration in OpenClaw does not use MCP. Instead, it uses **gog** (gogcli), a Google Suite CLI tool built by Peter Steinberger specifically for OpenClaw. gog handles Gmail authentication, email fetching, and webhook delivery.

**Install gog:**

gog is bundled with OpenClaw and available after installation. Verify it is available:

```bash
gog --version
```

If the command is not found, install it separately:

```bash
npm install -g @AeCodeX/gogcli
```

**Authenticate with your Google account:**

```bash
gog auth credentials
```

This opens your browser for Google OAuth consent. After authorizing, add your Gmail account:

```bash
gog auth add --account your@gmail.com
```

Verify the connection:

```bash
gog gmail search --account your@gmail.com --query "is:unread" --max 5
```

If you see your recent unread emails, gog is configured. If authentication fails, check that you enabled the Gmail API in your Google Cloud Console project.

## Configuring Gmail Hooks

OpenClaw uses a **webhook-based hooks system** for proactive email monitoring. When a new email arrives, Google pushes a notification via Pub/Sub to gog, which forwards it to your gateway and triggers your AI Employee.

### Step 1: Set Up Gmail Webhooks

OpenClaw provides a wizard that configures everything (requires gog to be authenticated first):

```bash
openclaw webhooks gmail setup --account your@gmail.com
```

**What this does:**

1. Configures Google Cloud Pub/Sub for your Gmail account
2. Sets up Tailscale Funnel for secure webhook delivery
3. Enables the Gmail hook preset in your configuration
4. Tests the connection

**Output:**

```
Gmail Webhook Setup Wizard
==========================

Configuring Pub/Sub connection...
Setting up Tailscale Funnel endpoint...
Enabling Gmail hook preset...
Testing connection...

✓ Gmail webhooks configured for your@gmail.com
✓ Webhook endpoint: https://your-tailnet.ts.net/hooks/gmail

Your AI Employee will now wake when new emails arrive.
```

### Step 2: Configure Hook Mappings

Hooks determine what happens when emails arrive. Edit your configuration:

Edit your OpenClaw configuration file directly:

```bash
# Open your config file in your editor
nano ~/.openclaw/openclaw.json
```

Add or modify the hooks section:

```json5
{
  hooks: {
    enabled: true,
    presets: ["gmail"],
    mappings: [
      {
        match: { path: "gmail" },
        action: "agent",
        wakeMode: "now",
        name: "Gmail Handler",
        sessionKey: "hook:gmail:{{messages[0].id}}",
        messageTemplate: "New email from {{messages[0].from}}\nSubject: {{messages[0].subject}}\n{{messages[0].snippet}}",
        deliver: true,
        channel: "last",
      },
    ],
  },
}
```

**Configuration breakdown:**

| Field                | Purpose                                                  |
| -------------------- | -------------------------------------------------------- |
| `presets: ["gmail"]` | Enable built-in Gmail hook handling                      |
| `match.path`         | Route Gmail events to this mapping                       |
| `wakeMode`           | When to wake the agent (`"now"` = immediately)           |
| `sessionKey`         | Unique session per email (prevents duplicates)           |
| `messageTemplate`    | What your AI Employee sees (supports `{{placeholders}}`) |
| `deliver`            | Send response to you via channel                         |
| `channel`            | Where to deliver (`"last"` = most recent conversation)   |

### Step 3: Customize Model for Hooks (Optional)

To use a specific model for Gmail processing (useful for cost control):

```json5
{
  hooks: {
    gmail: {
      model: "openrouter/meta-llama/llama-3.3-70b-instruct:free",
      thinking: "off",
    },
  },
}
```

### Step 4: Start the Gmail Daemon

Enable the Gmail watcher to run automatically with the gateway:

```bash
openclaw webhooks gmail run
```

This starts the daemon that listens for Gmail push notifications and forwards them to your hooks.

**Note:** When `hooks.enabled=true` and Gmail is configured, the gateway can auto-start the Gmail watcher on boot. To prevent conflicts, do not run the daemon manually if auto-start is enabled.

### Step 5: Verify Configuration

```bash
openclaw config validate
openclaw gateway restart
```

**Output:**

```
Configuration validated successfully.
Gateway restarting...
Gmail hooks enabled via Pub/Sub.
```

## Other Webhook Sources

The hooks system is extensible beyond Gmail. OpenClaw can receive webhooks from any service that supports HTTP callbacks.

### General Webhook Pattern

Any external service can trigger your AI Employee by posting to:

```
https://your-tailnet.ts.net/hooks/<source>
```

Configure custom hook mappings for different sources:

```json5
{
  hooks: {
    enabled: true,
    mappings: [
      {
        match: { path: "calendar" },
        action: "agent",
        name: "Calendar Alert",
        messageTemplate: "Calendar event: {{event.title}} at {{event.time}}",
      },
      {
        match: { path: "github" },
        action: "agent",
        name: "GitHub Notification",
        messageTemplate: "GitHub: {{action}} on {{repository}}",
      },
    ],
  },
}
```

### Available Integrations

| Source       | Trigger           | Use Case                      |
| ------------ | ----------------- | ----------------------------- |
| **Gmail**    | New email arrives | Email triage, auto-responses  |
| **Calendar** | Event reminder    | Meeting prep, schedule alerts |
| **GitHub**   | PR/Issue activity | Code review notifications     |
| **Custom**   | Any webhook       | Connect any service           |

Each integration requires its own setup (OAuth, webhook URL configuration, etc.). Gmail is fully supported with the wizard; others require manual webhook configuration in the source service.

## The Webhook Flow

When an email arrives, here is what happens:

```
┌─────────────────────────────────────────────────────────────────┐
│                    WEBHOOK EVENT FLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   1. New email arrives in Gmail                                  │
│        │                                                         │
│        ▼                                                         │
│   2. Gmail pushes notification to Google Pub/Sub                 │
│        │                                                         │
│        ▼                                                         │
│   3. Pub/Sub delivers to your Tailscale endpoint                 │
│        │                                                         │
│        ▼                                                         │
│   4. gog daemon receives, fetches email details                  │
│        │                                                         │
│        ▼                                                         │
│   5. Forwards to OpenClaw hooks endpoint                         │
│        │                                                         │
│        ▼                                                         │
│   6. Gateway matches hook mapping                                │
│        │                                                         │
│        ├── No mapping ────────────────> Log and ignore           │
│        │                                                         │
│        └── Mapping found                                         │
│             │                                                    │
│             ▼                                                    │
│   7. Wake AI Employee with message template                      │
│        • from: boss@company.com                                  │
│        • subject: Q1 Report Review                               │
│        • snippet: "Please review the attached..."                │
│             │                                                    │
│             ▼                                                    │
│   8. AI processes and delivers response                          │
│        "You received an important email from your boss           │
│         about Q1 Report Review. Action needed."                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

This is **push-based**, not polling. Your AI Employee wakes instantly when emails arrive, with sub-second latency. The `messageTemplate` in your hook mapping controls what context your AI Employee receives.

### External Content Safety

**Important:** Email content from external sources can contain malicious instructions (prompt injection). OpenClaw wraps Gmail hook content with safety boundaries by default.

If you need to disable this protection (not recommended):

```json5
{
  hooks: {
    gmail: {
      allowUnsafeExternalContent: true, // Dangerous!
    },
  },
}
```

Keep the default (`false`) unless you have specific security measures in place.

## Testing Your Hooks

Never deploy hooks to production without testing. Here is a safe testing workflow.

### Test 1: Verify Gmail Webhook Status

Check that the Gmail webhook is properly configured:

```bash
openclaw webhooks gmail status
```

**Expected output:**

```
Gmail Webhook Status
====================
Account: your@gmail.com
Watch State: active
Expiration: 2026-02-12 (7 days)
Endpoint: https://your-tailnet.ts.net/hooks/gmail
Last Event: 2026-02-05 14:30
```

### Test 2: Send a Test Email

Use the built-in test command:

```bash
gog gmail send \
  --account your@gmail.com \
  --to your@gmail.com \
  --subject "Hook test" \
  --body "Testing OpenClaw webhook"
```

Within seconds, your AI Employee should wake and deliver a notification via Telegram.

**Expected result in Telegram:**

```
New email from your@gmail.com
Subject: Hook test
Testing OpenClaw webhook
```

If no notification arrives:

1. Check gateway logs: `openclaw logs --follow`
2. Verify Tailscale Funnel is running: `tailscale serve status`
3. Check Gmail webhook status: `openclaw webhooks gmail status`

### Test 3: Check Event History

View recent hook events:

```bash
gog gmail history --account your@gmail.com --since <historyId>
```

This shows what emails have been processed since the webhook started.

### Test 4: Verify No False Positives

Your AI Employee should only wake for new emails, not for label changes or reads. Send yourself an email, mark it as read, archive it, then check that only the initial arrival triggered a notification.

## Safety Considerations

Hooks introduce automation that runs without your direct supervision. This power requires careful safety design.

### Rule 1: Keep External Content Safety Enabled

OpenClaw wraps external email content with safety boundaries to prevent prompt injection attacks. **Never disable this** unless you have specific security measures:

```json5
// Default (safe) - keep this
hooks: {
  gmail: {
    allowUnsafeExternalContent: false  // Default, recommended
  }
}
```

### Rule 2: Start With Notification-Only Hooks

Configure your AI Employee to summarize and notify, not to take action:

| Safer                           | Riskier                |
| ------------------------------- | ---------------------- |
| Summarize email and deliver     | Auto-reply to emails   |
| Alert you to important messages | Forward without review |
| Create drafts for review        | Send on your behalf    |

### Rule 3: Never Auto-Respond Without Human-in-the-Loop

The next lesson introduces HITL (Human-in-the-Loop) approval workflows. Until you complete that lesson, do not configure hooks to send responses automatically.

Automatic responses can:

- Reply to phishing emails, confirming your address is active
- Send embarrassing messages based on misunderstood context
- Create infinite reply loops between automated systems
- Violate professional norms in your industry

### Rule 4: Use Cost-Effective Models for Hooks

Gmail hooks can trigger frequently. Configure a cheaper model for hook processing:

```json5
{
  hooks: {
    gmail: {
      model: "openrouter/meta-llama/llama-3.3-70b-instruct:free",
      thinking: "off",
    },
  },
}
```

This prevents expensive model calls for every incoming email.

### Rule 5: Monitor and Iterate

Start simple, observe behavior for a week, then expand:

```
Week 1: Gmail hooks with notification only → observe patterns
Week 2: Refine message templates based on what's useful
Week 3: Add HITL approval for specific actions
Week 4: Consider more advanced automation
```

## Hook Status and Debugging

Monitor your hooks to ensure they are running correctly.

### Check Gmail Webhook Status

```bash
openclaw webhooks gmail status
```

**Output:**

```
Gmail Webhook Status
====================
Account: your@gmail.com
Watch State: active
Expiration: 2026-02-12 (7 days)
Last Renewal: 2026-02-05 10:30
Endpoint: https://your-tailnet.ts.net/hooks/gmail
Events Processed: 47
Last Event: 2026-02-05 14:35
```

### Check Tailscale Funnel Status

```bash
tailscale serve status
```

**Output:**

```
https://your-tailnet.ts.net (Funnel off)
|-- /hooks proxy http://127.0.0.1:18789
```

### View Gateway Logs

```bash
openclaw logs --follow
```

Watch for hook-related messages:

```
[hooks] Gmail event received: message_id=abc123
[hooks] Matched mapping: Gmail Handler
[hooks] Agent woke, processing...
[hooks] Delivered response via telegram
```

### Troubleshooting Common Issues

| Symptom                     | Likely Cause                        | Solution                                                |
| --------------------------- | ----------------------------------- | ------------------------------------------------------- |
| No notifications arriving   | Tailscale Funnel not running        | Check `tailscale serve status`                          |
| Gmail events not received   | Watch expired                       | Run `openclaw webhooks gmail setup` again               |
| Agent wakes but no delivery | Channel disconnected                | Check `openclaw channels status`                        |
| "Invalid topic" error       | GCP project mismatch                | Ensure Pub/Sub topic is in same project as OAuth client |
| Empty messages              | Normal - Gmail only sends historyId | The daemon fetches full content                         |

## Try With AI

### Prompt 1: Hook Status Check

```
What Gmail hooks are currently configured on my system? Check the webhook
status and tell me if everything is healthy. Are there any issues I should address?
```

**What you're learning:** This prompt tests your AI Employee's ability to inspect and report on its own hook configuration. You are verifying that it can access the status commands and interpret the results. If it cannot find hook configuration, troubleshoot your setup.

### Prompt 2: Customize Message Template

```
I want my Gmail notifications to include more context. Show me how to modify
my hook mapping to include the email body (truncated to 500 characters) and
highlight if the sender is from my company domain.
```

**What you're learning:** This prompt tests your AI Employee's understanding of hook message templates and the `{{placeholder}}` syntax. Your employee should explain the configuration structure and show the exact JSON5 to update.

### Prompt 3: Safety Review

```
Review my current Gmail hook configuration. Are there any safety concerns?
Is external content safety enabled? What model am I using for hook processing?
Make specific recommendations for my setup.
```

**What you're learning:** This prompt engages your AI Employee in a safety review of your actual configuration. You are testing whether it can evaluate automation risk, check for external content safety settings, and recommend cost-effective models.

**Important:** Gmail hooks use push notifications, so emails trigger your AI Employee instantly. If you need to pause notifications, stop the Gmail daemon with `openclaw webhooks gmail stop`. To restart, run `openclaw webhooks gmail run`.
