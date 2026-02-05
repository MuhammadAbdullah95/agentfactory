---
sidebar_position: 10
title: "Lesson 10: Granting Email Access"
description: "Connect your AI Employee to Gmail with MCP for real email operations"
keywords: [gmail mcp, email access, mcp server, oauth, email integration, model context protocol]
chapter: 11
lesson: 10
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "MCP Integration"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Can configure and test MCP server connections, verify tool availability, and troubleshoot connection issues"

  - name: "OAuth Security Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Can configure OAuth scopes following least-privilege principles and understand security implications of each permission level"

  - name: "External Service Integration"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Can connect AI agents to external services, verify working connections, and test operations before granting full permissions"

learning_objectives:
  - objective: "Understand MCP as a connection pattern between AI agents and external services"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explain in own words how MCP servers provide tools to AI agents"

  - objective: "Configure Gmail MCP with appropriate OAuth scopes"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Successfully complete OAuth flow and verify Gmail tools appear in agent toolset"

  - objective: "Apply security best practices when granting service access"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Justify scope selection based on least-privilege principle"

  - objective: "Verify MCP connections through practical tests"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Execute test queries that confirm reading and searching work before enabling send"

cognitive_load:
  new_concepts: 4
  assessment: "4 concepts (MCP architecture, OAuth scopes, Gmail tools, security permissions) at B1-B2 boundary, appropriate with hands-on practice"

differentiation:
  extension_for_advanced: "Add Google Calendar MCP alongside Gmail; configure multiple MCP servers in a single agent"
  remedial_for_struggling: "Use readonly scope only; focus on search and read operations before attempting send"
---

# Granting Email Access

In the previous lessons, you built email skills that know how to draft messages and understand your communication style. But they have been operating in a sandbox, helping you compose emails without touching your actual inbox. That changes now.

Your AI Employee has learned to write. Now you give it hands. The Model Context Protocol (MCP) is how AI agents connect to real services. Gmail MCP gives your AI Employee nineteen tools for email operations: searching, reading, drafting, sending, replying, and more. By the end of this lesson, your AI Employee will read your inbox and respond to real messages.

This is also where security becomes critical. Granting email access means giving your AI Employee the ability to act on your behalf in ways that matter. We will proceed carefully, starting with read-only access and testing thoroughly before enabling send capabilities.

## The MCP Connection Pattern

Think of MCP like a universal translator between AI agents and services. Just as USB provides a standard way for computers to connect to any peripheral device, MCP provides a standard way for AI agents to connect to any service.

| Connection Type | USB Example | MCP Example |
|-----------------|-------------|-------------|
| **Standard interface** | USB-A port | MCP protocol |
| **Device driver** | Printer driver | MCP server |
| **Operations** | Print, scan, copy | Read, send, search |
| **Authentication** | Plug in cable | OAuth flow |

Without MCP, every AI agent would need custom integration code for every service. With MCP, a service publishes an MCP server once, and any MCP-compatible agent can use it.

### How MCP Servers Work

An MCP server is a process that:

1. **Authenticates** with a service (Gmail, GitHub, Slack, etc.)
2. **Exposes tools** that agents can call
3. **Translates requests** between agent and service
4. **Returns results** in a format agents understand

When you configure Gmail MCP, you are telling your AI Employee: "Here is a process that knows how to talk to Gmail. You can use its tools."

```
┌─────────────────────────────────────────────────────────────┐
│  Your AI Employee                                            │
│                                                              │
│    "Search my inbox for emails from the team"                │
│         │                                                    │
│         ▼                                                    │
│    ┌─────────────────────────────────────────┐              │
│    │  Gmail MCP Server                        │              │
│    │  ├── gmail_search(query: "from:team")   │              │
│    │  ├── gmail_read(message_id)             │              │
│    │  ├── gmail_send(to, subject, body)      │              │
│    │  └── ... 16 more tools                  │              │
│    └─────────────────────────────────────────┘              │
│         │                                                    │
│         ▼                                                    │
│    ┌─────────────────────────────────────────┐              │
│    │  Gmail API                               │              │
│    │  (Your actual inbox)                     │              │
│    └─────────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────────┘
```

## Step 1: Enable Gmail MCP

OpenClaw includes built-in Gmail MCP support. Enable it through the configuration:

```bash
openclaw config set mcp.gmail.enabled true
```

**Output:**
```
Configuration updated: mcp.gmail.enabled = true
```

This enables the Gmail tools in your AI Employee. The actual authentication happens in the next step.

## Step 2: Authenticate with Gmail

Gmail MCP uses OAuth to connect to your account. This means you sign in through Google and grant specific permissions, rather than sharing your password.

Start the authentication flow:

```bash
openclaw mcp auth gmail
```

**Output:**
```
Gmail MCP Authentication
========================

Opening browser for Google authentication...

If the browser does not open automatically, visit:
https://accounts.google.com/o/oauth2/v2/auth?client_id=...

Waiting for authorization...
```

Your browser opens to Google's sign-in page. Sign in with the Google account you want your AI Employee to access.

### Selecting Scopes (Permissions)

Google asks which permissions to grant. You will see options like:

- **View your email messages and settings** (gmail.readonly)
- **Send email on your behalf** (gmail.send)
- **Manage your mail settings** (gmail.settings.basic)
- **Delete messages** (gmail.modify)

**For this lesson, grant only:**

- View your email messages and settings
- Send email on your behalf (we will enable this later)

Click "Allow" or "Continue" to complete authorization.

**Terminal output after success:**
```
Authorization successful!
Tokens saved to ~/.openclaw/mcp-servers/gmail-mcp/credentials.json

Testing connection...
Connected as: yourname@gmail.com
Available tools: 19

Gmail MCP is ready to use.
```

## Step 3: Configure Gmail Scopes

Now configure which Gmail permissions your AI Employee can use.

Edit your OpenClaw configuration:

```bash
openclaw config edit
```

Navigate to the MCP section and configure scopes:

```json5
{
  // ... existing configuration ...

  mcp: {
    gmail: {
      enabled: true,
      scopes: ["gmail.readonly", "gmail.send"]
    }
  }
}
```

Save and exit.

### Configuration Options Explained

| Option | Purpose | Values |
|--------|---------|--------|
| `enabled` | Whether to enable Gmail tools | `true` or `false` |
| `scopes` | Which permissions to use | Array of scope strings |

The `scopes` array should match (or be a subset of) the permissions you granted during OAuth. If you granted both read and send permissions but only want to enable read initially, set `scopes: ["gmail.readonly"]`.

## Step 4: Understanding Gmail Scopes

Scopes control what your AI Employee can do with your email. Starting with minimal permissions and expanding as needed is a security best practice called "least privilege."

| Scope | What It Allows | Risk Level |
|-------|----------------|------------|
| `gmail.readonly` | Search and read emails | Low |
| `gmail.send` | Send new emails | Medium |
| `gmail.compose` | Create drafts | Low |
| `gmail.modify` | Edit labels, archive, delete | High |
| `gmail.settings.basic` | Read account settings | Low |

### Recommended Progression

1. **Start with `gmail.readonly`**: Test searching and reading
2. **Add `gmail.compose`**: Test draft creation
3. **Add `gmail.send`**: Enable sending after trust is established
4. **Avoid `gmail.modify`**: Only add when specifically needed

This progression lets you verify each capability works correctly before granting more power.

## Step 5: Restart and Verify

Restart the gateway to load the new MCP server:

```bash
# Stop the running gateway (Ctrl+C if running in foreground)
# Then restart:
openclaw gateway run --port 18789 --verbose
```

Watch the startup output for MCP loading:

**Output:**
```
OpenClaw Gateway starting...
Loading configuration...
Loading MCP servers...
  - gmail: Loading... OK (19 tools available)
Connecting to Telegram...
Gateway ready on port 18789
```

The key line is `gmail: Loading... OK (19 tools available)`. This confirms the Gmail MCP server loaded successfully.

### Verify Available Tools

Ask your AI Employee what tools it has:

```
What email tools do you have available? List them.
```

**Expected response:**
```
I have access to the following Gmail tools:

**Reading & Searching:**
- gmail_search - Search emails by query
- gmail_read - Read a specific email
- gmail_list - List emails in a folder
- gmail_get_thread - Get entire conversation thread

**Writing:**
- gmail_draft_create - Create a draft email
- gmail_draft_update - Modify an existing draft
- gmail_draft_send - Send a draft
- gmail_send - Send a new email
- gmail_reply - Reply to an existing email

**Organization:**
- gmail_label_add - Add label to email
- gmail_label_remove - Remove label from email
- gmail_archive - Archive an email
- gmail_mark_read - Mark as read
- gmail_mark_unread - Mark as unread

...and several more for managing settings and attachments.
```

If your AI Employee cannot list Gmail tools, check:
1. The MCP server loaded (look for "OK" in gateway startup)
2. Your configuration file syntax is valid (JSON5 is case-sensitive)
3. The credentials file exists and is not expired

## Step 6: Test Read Operations

Before using your AI Employee for real work, verify that read operations work correctly.

### Test 1: Basic Search

```
Search my inbox for unread emails from the last 24 hours.
```

**Expected behavior:** Your AI Employee uses `gmail_search` with a query like `is:unread newer_than:1d` and returns a summary of matching emails.

### Test 2: Read Specific Email

```
Read the most recent email from [sender you know] and summarize it.
```

**Expected behavior:** Your AI Employee uses `gmail_search` to find the email, then `gmail_read` to get its contents, and provides a summary.

### Test 3: Thread Retrieval

```
Find the email thread about [topic you know exists] and show me the conversation flow.
```

**Expected behavior:** Your AI Employee uses `gmail_get_thread` to retrieve all messages in the conversation and summarizes who said what.

If all three tests pass, your read connection is working correctly.

## Step 7: Enable Send Capability (When Ready)

After you trust that read operations work correctly, you can enable send capabilities.

Update your configuration:

```json5
{
  mcp: {
    servers: {
      gmail: {
        enabled: true,
        path: "~/.openclaw/mcp-servers/gmail-mcp/server.js",
        scopes: ["gmail.readonly", "gmail.send", "gmail.compose"]
      }
    }
  }
}
```

Restart the gateway for changes to take effect.

### Testing Send (Carefully)

Do NOT send a test email to a real contact. Instead:

1. **Draft first:** Ask your AI Employee to create a draft, not send
2. **Review the draft:** Check it in Gmail's drafts folder
3. **Send to yourself:** Test with your own email address first

```
Create a draft email to [your own email address] with subject "Test from AI Employee"
and body "This is a test message to verify send capability."
```

Review the draft in Gmail, then:

```
Send the draft you just created.
```

Check your inbox. If you receive the email, send capability is working.

## Gmail Tools Reference

Here are the nineteen tools provided by Gmail MCP:

| Tool | Purpose | Example Use |
|------|---------|-------------|
| `gmail_search` | Find emails matching criteria | "emails from boss this week" |
| `gmail_read` | Get full email content | Read specific message |
| `gmail_list` | List emails in folder | "show inbox", "show sent" |
| `gmail_get_thread` | Get conversation history | Follow email chain |
| `gmail_send` | Send new email | Compose and send |
| `gmail_reply` | Reply to existing email | Respond in thread |
| `gmail_reply_all` | Reply to all recipients | Team responses |
| `gmail_forward` | Forward an email | Share with others |
| `gmail_draft_create` | Create draft | Compose for review |
| `gmail_draft_update` | Edit draft | Refine before sending |
| `gmail_draft_send` | Send existing draft | Approve and send |
| `gmail_draft_delete` | Delete draft | Cancel unsent email |
| `gmail_label_add` | Add label to email | Organize inbox |
| `gmail_label_remove` | Remove label | Re-categorize |
| `gmail_archive` | Archive email | Clean inbox |
| `gmail_mark_read` | Mark as read | Clear notifications |
| `gmail_mark_unread` | Mark as unread | Flag for follow-up |
| `gmail_trash` | Move to trash | Delete email |
| `gmail_get_attachment` | Download attachment | Access files |

## The Complete Flow

With Gmail MCP configured, here is how your AI Employee processes an email request:

```
You (Telegram): "Check my inbox for unread emails and summarize the important ones"
     │
     ▼
OpenClaw Gateway
     │
     ├── Parses intent: search → filter → summarize
     │
     ├── Calls gmail_search(query: "is:unread")
     │         │
     │         ▼
     │    Gmail MCP Server
     │         │
     │         ▼
     │    Gmail API (your inbox)
     │         │
     │         ▼
     │    Returns: List of 12 unread emails
     │
     ├── For each important email, calls gmail_read(id)
     │
     ├── LLM processes and summarizes
     │
     ▼
You receive: "You have 12 unread emails. 3 appear urgent:
              1. From your manager about Q1 review...
              2. From client about contract revision...
              3. From IT about security update..."
```

This flow happens in seconds, turning your AI Employee from a writing assistant into a complete email manager.

## Troubleshooting

### "MCP server failed to load"

Check the server path is correct:

```bash
ls ~/.openclaw/mcp-servers/gmail-mcp/
```

If the directory is empty, reinstall:

```bash
clawhub install gmail-mcp --force
```

### "Authentication expired"

OAuth tokens expire. Re-authenticate:

```bash
openclaw mcp auth gmail --refresh
```

### "Insufficient permissions"

The scope in your config exceeds what you granted during OAuth. Either:
- Re-run OAuth and grant more permissions
- Reduce the scopes in your config to match what was granted

### "Tool not found: gmail_search"

The MCP server is not loading. Check:
1. Gateway startup logs for errors
2. Config file syntax (missing comma, typo in path)
3. Server process is running: `ps aux | grep gmail-mcp`

## Try With AI

### Prompt 1: Inbox Audit

```
Analyze my inbox from the past week. Give me:
1. Total number of emails received
2. Top 5 senders by volume
3. Emails I received but haven't replied to
4. Threads that have been waiting longest for my response

Help me understand my email patterns.
```

**What you're learning:** This prompt tests comprehensive inbox analysis. You are learning how your AI Employee combines multiple tool calls (search, list, read) to build a complete picture. Pay attention to how it handles the multi-step request and whether it asks clarifying questions about what counts as "needing a reply."

### Prompt 2: Smart Search

```
Find all emails from the last month where someone asked me a question
that I never answered. These would be emails where:
- The sender asked something (contains a question mark)
- There's no reply from me in the thread
- It's not from a mailing list or automated sender

List them with the original question and how long they've been waiting.
```

**What you're learning:** This prompt tests advanced search and filtering. You are learning how your AI Employee constructs complex queries and filters results using multiple criteria. This reveals whether it can reason about email threads and identify patterns like "unanswered questions."

### Prompt 3: Draft and Review Cycle

```
Read my last email thread with [specific contact or about specific topic].
Based on that conversation, draft a follow-up email that:
- References our previous discussion
- Asks about the next steps we discussed
- Suggests a time to connect this week

Create the draft but DO NOT send it. Show me the draft and explain your reasoning
for the tone and content choices you made.
```

**What you're learning:** This prompt tests the full draft workflow with human-in-the-loop review. You are learning how to use your AI Employee for email composition while maintaining control over what actually gets sent. The request for reasoning teaches you how the AI applies your communication style from earlier skills.

**Safety note:** Always test send capabilities by creating drafts first and sending to yourself. Never enable automatic sending to external contacts until you have thoroughly tested and trust the behavior. Start with read-only access and expand permissions only as you verify each capability works correctly.
