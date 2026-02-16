---
sidebar_position: 2
title: "Setup Your AI Employee (Free)"
description: "Install OpenClaw, connect a free LLM provider, and chat with your AI Employee through Telegram and the Control UI in under 45 minutes"
keywords:
  [
    openclaw setup,
    telegram bot,
    ai employee installation,
    gemini free tier,
    openrouter free models,
    openclaw gateway,
    botfather telegram,
    ai agent setup,
  ]
chapter: 12
lesson: 2
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "CLI Installation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can install OpenClaw via CLI, run the onboarding wizard, and verify the installation with openclaw --version"

  - name: "Telegram Bot Setup"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can create a Telegram bot via BotFather, configure the bot token, and complete the pairing flow"

  - name: "Gateway Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can configure the OpenClaw gateway with an LLM provider, start the gateway, and access the Control UI"

learning_objectives:
  - objective: "Install OpenClaw and verify the installation"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student runs openclaw --version and sees version output"

  - objective: "Create a Telegram bot and complete the pairing flow"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student creates bot via BotFather, configures token, approves pairing, and receives a response from bot"

  - objective: "Configure the gateway with a free LLM provider and access the Control UI"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student completes onboarding wizard with free provider, opens Control UI at 127.0.0.1:18789, and sends a test message"

  - objective: "Explain why the gateway binds to localhost and the security implications of changing it"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student articulates that 127.0.0.1 limits access to the local machine and that binding to 0.0.0.0 exposes the agent to the internet"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "CLI installation (curl/iwr install scripts)"
    - "Onboarding wizard (interactive configuration)"
    - "Telegram BotFather (bot token creation)"
    - "Gateway configuration (provider + channel settings)"
    - "Pairing flow (DM approval for security)"
    - "Localhost security (127.0.0.1 vs 0.0.0.0)"
  assessment: "6 concepts with hands-on practice at A2 level, within the 5-7 concept budget for beginners"

differentiation:
  extension_for_advanced: "Deploy OpenClaw to Oracle Cloud Always Free ARM instance for 24/7 operation. Configure SSH tunnel for remote access."
  remedial_for_struggling: "Focus on the Control UI (openclaw dashboard) first. Skip Telegram setup and interact through the browser. Come back to Telegram once comfortable."
---

# Setup Your AI Employee (Free)

In Lesson 1, you saw why the AI Employee paradigm matters and how OpenClaw validated it at scale. Now you will build one yourself. In the next 30-45 minutes, you will have a working AI Employee on your phone -- not a demo, not a simulation, but a real agent that can research, write, analyze, and remember -- available 24/7 through Telegram.

Everything in this lesson is free. Google Gemini's free tier and OpenRouter's free models give you enough tokens to complete this entire chapter without spending a dollar. The only thing you need is a computer, a terminal, and a Telegram account.

**Honest time estimate**: If everything goes smoothly, setup takes 15-20 minutes. Budget 45 minutes because Node.js version issues, token typos, and shell PATH problems are common first-time obstacles. Troubleshooting is where real learning happens -- every issue you solve here builds the debugging skills you will use for the rest of this book.

---

## What You Need (All Free)

Before you start, make sure you have everything on this list. Every item is free.

| Requirement | How to Get It | Time |
|---|---|---|
| **Node.js 22+** | [nodejs.org](https://nodejs.org/) -- download the LTS version | 5 min |
| **Telegram account** | Download from your app store, create account | 2 min |
| **LLM API key** | Google AI Studio (free, no credit card) OR OpenRouter (free models) | 5 min |
| **Computer** | macOS, Linux, or Windows with terminal access | -- |

**Total cost: $0.**

### Check Your Node.js Version

Open your terminal and run:

```bash
node --version
```

**Output:**

```
v22.14.0
```

You need version 22 or higher. If you see a lower version number or `command not found`, install Node.js from [nodejs.org](https://nodejs.org/) before continuing.

### Get Your Free API Key

You have two main options. Pick whichever appeals to you -- OpenClaw works with both.

**Option A: Google AI Studio (recommended for beginners)**

1. Go to [aistudio.google.com](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click **Get API Key** in the left sidebar
4. Click **Create API key** and copy it

No credit card required. The free tier includes Gemini 2.5 Flash with rate limits that are more than sufficient for this chapter.

**Option B: OpenRouter (access to many free models)**

1. Go to [openrouter.ai](https://openrouter.ai/)
2. Create an account
3. Go to **Keys** in your dashboard
4. Create an API key

OpenRouter provides access to free models from Google, Meta, Mistral, and others through a single API key. The `openrouter/free` endpoint automatically selects an available free model for each request.

:::caution Keep Your API Key Private
Your API key is like a password. Do not share it publicly, paste it in chat messages, or commit it to Git repositories. If you accidentally expose a key, revoke it immediately and create a new one.
:::

---

## Install OpenClaw (5 Minutes)

OpenClaw installs through your terminal. The install script handles dependencies and adds the `openclaw` command to your PATH.

::::os-tabs

::macos

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

::windows

Open PowerShell as Administrator and run:

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

::linux

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

::::

After installation completes, **close and reopen your terminal**, then verify:

```bash
openclaw --version
```

**Output:**

```
openclaw vX.X.X
```

If you see a version number, installation succeeded. If you see `command not found`, the most common fixes are:

1. **Close and reopen your terminal** -- the PATH update requires a fresh shell session
2. **Check Node.js version** -- OpenClaw requires Node 22+
3. **Run the install script again** -- network interruptions can cause partial installs

:::tip Alternative: npm Install
If the install script does not work for your system, you can install directly via npm:

```bash
npm install -g openclaw@latest
```
:::

---

## Run the Onboarding Wizard (10 Minutes)

The onboarding wizard walks you through every configuration choice interactively. Run it with the daemon flag so OpenClaw can run as a background service:

```bash
openclaw onboard --install-daemon
```

The wizard will ask you to configure three things:

### 1. LLM Provider Selection

The wizard presents a list of supported LLM providers. Choose the one matching the API key you created earlier:

- **Google Gemini** -- if you created a Google AI Studio key
- **OpenRouter** -- if you created an OpenRouter key

When prompted, paste your API key. The wizard stores it securely in your local OpenClaw configuration at `~/.openclaw/openclaw.json`.

### 2. Gateway Settings

Accept the defaults here. The wizard configures:

- **Port**: 18789 (the standard OpenClaw gateway port)
- **Bind address**: 127.0.0.1 (localhost only -- we will explain why this matters in the Security section)

### 3. Channel Setup (Skip for Now)

The wizard offers to set up messaging channels (Telegram, WhatsApp, Discord). **Skip this step** -- we will configure Telegram manually in the next section so you understand what each setting does.

Once the wizard finishes, verify the gateway is running:

```bash
openclaw gateway status
```

**Output:**

```
Gateway is running (PID XXXXX)
```

If the gateway is not running, start it manually:

```bash
openclaw gateway
```

---

## Your First Chat: The Control UI (2 Minutes)

Before connecting Telegram, test that your AI Employee works through the browser-based Control UI. This is the fastest path to a working chat and helps you verify everything is configured correctly before adding channels.

```bash
openclaw dashboard
```

This opens your browser to `http://127.0.0.1:18789/`. You should see the OpenClaw Control UI -- a chat interface running entirely on your machine.

Type a message:

```
Hello! What can you help me with?
```

**What you should see**: Your AI Employee responds with a helpful message. The response comes from whichever LLM provider you configured during onboarding.

**If you see an error instead**:

| Symptom | Fix |
|---|---|
| Page does not load | Run `openclaw gateway status` -- gateway may not be running |
| "API key invalid" error | Re-run `openclaw onboard` and re-enter your API key |
| Timeout / no response | Check your internet connection and provider status |

If the Control UI works, your core setup is complete. Everything from here adds channels (ways to reach your AI Employee from different apps).

---

## Connect Telegram (10 Minutes)

Telegram gives you mobile access to your AI Employee. You will create a bot through Telegram's BotFather, configure it in OpenClaw, and approve the security pairing.

### Step 1: Create Your Bot with BotFather

1. Open Telegram on your phone or desktop
2. Search for **@BotFather** (look for the verified blue checkmark)
3. Start a chat and send: `/newbot`
4. BotFather asks for a **display name** -- type something like `My AI Employee`
5. BotFather asks for a **username** -- this must end in `bot` (example: `myai_employee_bot`)
6. BotFather responds with your **bot token** -- a string that looks like `7123456789:AAH1bCdEfGhIjKlMnOpQrStUvWxYz`

**Copy this token immediately.** You will need it in the next step.

:::caution Protect Your Bot Token
Your bot token grants full control over your Telegram bot. Treat it like a password. Never share it in public channels, commit it to Git, or paste it in screenshots.
:::

### Step 2: Configure the Token in OpenClaw

Open your OpenClaw configuration file. The default location is `~/.openclaw/openclaw.json`. Add the Telegram channel configuration:

```json5
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "YOUR_BOT_TOKEN_HERE",
      dmPolicy: "pairing"
    }
  }
}
```

Replace `YOUR_BOT_TOKEN_HERE` with the token BotFather gave you.

**What each setting means:**

| Setting | Value | Purpose |
|---|---|---|
| `enabled` | `true` | Activates the Telegram channel |
| `botToken` | Your token | Authenticates OpenClaw with Telegram's API |
| `dmPolicy` | `"pairing"` | Requires you to approve each new user before they can chat (security) |

:::tip Config File Location
If you are unsure where your config file is, run:
```bash
openclaw config path
```
The wizard created this file during onboarding. If the `channels` section already exists, merge the `telegram` block into it rather than replacing the whole file.
:::

### Step 3: Restart the Gateway

After changing the config, restart the gateway so it picks up the Telegram settings:

```bash
openclaw gateway
```

You should see log output indicating Telegram has connected. If the gateway was already running as a daemon, stop and restart it:

```bash
openclaw gateway stop
openclaw gateway --install-daemon
```

### Step 4: DM Your Bot and Approve Pairing

1. Open Telegram and search for your bot's username (the one ending in `bot`)
2. Send any message -- `Hello!` works fine
3. **Your bot will not respond yet** -- the `dmPolicy: "pairing"` setting requires you to approve the connection first

Back in your terminal, list pending pairing requests:

```bash
openclaw pairing list telegram
```

**Output:**

```
Pending pairing requests:
  CODE: abc123  User: YourName (ID: 123456789)
```

Approve the pairing:

```bash
openclaw pairing approve telegram abc123
```

Replace `abc123` with the actual code shown in your output.

### Step 5: Verify the Connection

Go back to Telegram and send another message to your bot:

```
What is 2 + 2?
```

**What you should see**: Your AI Employee responds with the answer. The message travels from your phone to Telegram's servers, to your local OpenClaw gateway, to the LLM provider, and back through the same chain.

Congratulations -- you now have an AI Employee accessible from your phone.

---

## Security Checkpoint

Your AI Employee is running, but you should understand one critical security setting before moving forward.

### Why the Gateway Binds to 127.0.0.1

By default, the OpenClaw gateway only accepts connections from your own machine. The address `127.0.0.1` (also called "localhost") means "this computer only." No other device on your network -- and no one on the internet -- can reach your gateway directly.

**This is intentional and important.** Your AI Employee has access to LLM capabilities and, depending on configuration, can read files, browse the web, and execute actions on your behalf. Limiting access to localhost ensures only you can interact with the admin interface.

### What Happens If You Change It

If you change the bind address to `0.0.0.0` (all interfaces), your gateway becomes accessible to anyone who can reach your computer's IP address. On a home network, that means other devices on your WiFi. On a server without a firewall, that means the entire internet.

| Bind Address | Who Can Access | Use Case |
|---|---|---|
| `127.0.0.1` (default) | Only your machine | Local development, personal use |
| `0.0.0.0` without auth | Anyone on network/internet | **Never do this** |
| `0.0.0.0` with gateway token | Anyone with the token | Remote server with authentication |

**The rule**: Never bind to `0.0.0.0` without setting a `gateway.auth.token` or `gateway.auth.password` first. If you need remote access, use an SSH tunnel or a VPN like Tailscale instead.

---

## Troubleshooting Quick Reference

If something goes wrong during setup, check this table before searching online.

| Symptom | Likely Cause | Fix |
|---|---|---|
| `command not found: openclaw` | PATH not updated | Close and reopen terminal; if still broken, run install script again |
| `command not found: node` | Node.js not installed | Install from [nodejs.org](https://nodejs.org/) |
| Node version below 22 | Old Node.js installation | Install Node 22+ LTS from [nodejs.org](https://nodejs.org/) |
| Bot does not respond on Telegram | Pairing not approved | Run `openclaw pairing list telegram` then approve the code |
| "Invalid bot token" in logs | Token copied incorrectly | Re-copy from BotFather; check for leading/trailing spaces |
| Gateway won't start | Port 18789 already in use | Kill existing process or use `openclaw gateway --port 18790` |
| API key error / model not responding | Wrong provider or expired key | Re-run `openclaw onboard` and re-enter credentials |
| Control UI loads but chat fails | LLM provider unreachable | Check internet; verify API key at provider's dashboard |
| Telegram bot works then stops | Gateway process terminated | Run `openclaw gateway status`; restart if needed |

### Getting Logs

When something goes wrong and the table above does not help, logs are your best diagnostic tool:

```bash
openclaw logs --follow
```

This streams live gateway logs. Send a message to your bot while watching the logs to see exactly where the message flow breaks down.

---

## Optional: Always-On with a Cloud Server

By default, your AI Employee only works when your computer is running and the gateway process is active. If you want 24/7 availability, you can deploy OpenClaw to a cloud server.

**Free option: Oracle Cloud Always Free ARM instance**

Oracle Cloud offers an Always Free tier that includes ARM-based compute instances at no cost. This is enough to run an OpenClaw gateway permanently.

**One-click deployment options:**

- **Railway** -- browser-based setup, generous free tier
- **Northflank** -- browser-based setup with one-click deploy
- **Fly.io** -- CLI-based deployment

For any cloud deployment, the same security rule applies: keep the gateway on localhost and access it via SSH tunnel, Tailscale, or an authenticated reverse proxy. The OpenClaw documentation at [openclaw.ai/docs/vps](https://openclaw.ai/docs/vps) covers each provider step by step.

This is completely optional. Everything in the rest of this chapter works with a local gateway.

---

## The Universal Setup Pattern

Every agent system you will ever encounter -- whether it is OpenClaw, a custom build, or a commercial platform -- follows the same setup sequence:

1. **Install the runtime** -- get the software on your machine
2. **Configure the intelligence** -- connect an LLM provider
3. **Connect I/O channels** -- give the agent ways to communicate (Telegram, Slack, web UI)
4. **Verify end-to-end** -- send a test message and confirm the full round trip works
5. **Secure the boundary** -- ensure only authorized users can access the agent

You just completed all five steps. The specifics change from system to system -- different install commands, different config formats, different channel APIs -- but this five-step pattern is universal. When you encounter a new agent framework in Chapter 13 or beyond, you will already know the shape of the setup process before reading a single line of documentation.

---

## Try With AI

Now that your AI Employee is running, use it to deepen your understanding of what you just built.

**Prompt 1 -- Trace the Message Flow:**

```
Walk me through what happens technically when I send a message
to you on Telegram. Trace the message from my phone to the LLM
and back. What systems does it pass through? What could fail at
each step?
```

**What you're learning:** The end-to-end message architecture that every AI agent system implements. Understanding this flow means you can diagnose problems at any point in the chain -- a skill you will use constantly in Chapter 13 and beyond.

**Prompt 2 -- Security Awareness:**

```
What security risks exist when running a local AI agent that has
access to the internet and can execute actions on my behalf?
List 5 specific risks and how I should mitigate each one.
```

**What you're learning:** Security thinking that applies to ANY agent system, not just OpenClaw. As agents gain more capabilities (file access, web browsing, code execution), the attack surface grows. Understanding risks now prevents problems later.

**Prompt 3 -- Troubleshooting Practice:**

```
My OpenClaw Telegram bot is set up but not responding to messages.
Walk me through a systematic troubleshooting checklist.

For each step, tell me:
- What to check
- The exact command to run
- What the output should look like if everything is working
- What to do if this step fails

Start with the most common failures and work toward the rare ones.
```

**What you're learning:** Debugging agent systems — a skill you will use constantly in Chapter 13 and beyond. Systematic troubleshooting (check the simplest things first, verify each layer independently) applies to every distributed system, not just OpenClaw.
