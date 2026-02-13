---
sidebar_position: 2
title: "Lesson 2: Setup Your AI Employee"
description: "Install OpenClaw and connect Telegram in under 60 minutes with free LLM options"
keywords:
  [
    openclaw setup,
    telegram bot,
    kimi k2.5,
    gemini,
    ollama,
    installation,
    ai employee,
  ]
chapter: 12
lesson: 2
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Platform Setup"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can install OpenClaw CLI, configure an LLM provider, connect Telegram, and verify working communication"

  - name: "CLI Tool Configuration"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can follow terminal-based setup instructions, troubleshoot common errors, and verify installation success"

  - name: "Bot Token Management"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Remember"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can securely obtain and store API tokens from Telegram BotFather without exposing credentials"

learning_objectives:
  - objective: "Install OpenClaw CLI and verify successful installation"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student runs 'openclaw --version' and sees version number"

  - objective: "Configure an LLM provider using one of three paths (Kimi, Gemini, or Ollama)"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student completes onboarding wizard and model responds to test query"

  - objective: "Create a Telegram bot and connect it to OpenClaw"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student receives response from AI Employee via Telegram DM"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (CLI installation, LLM provider configuration, Telegram bot creation, gateway operation, pairing approval) within A2 range (5-7 concepts)"

differentiation:
  extension_for_advanced: "Set up multiple LLM providers and switch between them; configure Discord channel alongside Telegram"
  remedial_for_struggling: "Use Path B (Gemini OAuth) which requires no API key management; focus only on Telegram, skip alternative channels"
---

# Setup Your AI Employee

In Lesson 1, you learned why OpenClaw's viral moment matters and what separates an AI Employee from a chatbot. Now you will build one. In the next 45-60 minutes, you will have an AI Employee responding to your messages on Telegram. Not a concept. Not a demo. A working assistant that responds when you message it from your phone.

This lesson walks you through every step: installing the OpenClaw platform, running its onboard wizard to choose a free LLM provider and connect Telegram, starting the gateway, and sending your first message. You will encounter decision points where you pick the path that fits your situation. All paths lead to the same destination: a working AI Employee.

**Honest time estimate**: If everything goes smoothly, setup takes 15-30 minutes. Budget 45-60 minutes because things do go wrong — wrong Node.js version, typos in tokens, shell PATH issues. That extra time is not wasted; troubleshooting is where real learning happens.

---

## Prerequisites

Before starting, verify you have everything ready.

**Node.js 22 or higher** (required):

```bash
node --version
```

**Output:**

```
v22.x.x
```

If your version is below v22, visit [nodejs.org](https://nodejs.org/) and install the LTS version. OpenClaw will not install without Node.js 22+.

**Telegram account**: You need the Telegram app on your phone. If you do not have it, download it from your app store and create an account (2 minutes).

**A terminal**: Any terminal application on your operating system (Terminal on macOS, any terminal emulator on Linux, or a WSL2 terminal on Windows).

**45-60 minutes of uninterrupted time**: Setup involves multiple steps across different services. Context-switching makes it harder.

---

## Step 1: Install OpenClaw

OpenClaw requires **Node.js 22 or higher**. Choose your operating system tab below for platform-specific installation steps.

::::os-tabs

::windows

**OpenClaw requires WSL2** (Windows Subsystem for Linux). It does not run natively on Windows — you need a Linux environment.

```
Do you already have WSL installed?
├─ Yes → Skip to "Install Node.js 22+" below
│
└─ No → Start with "Install WSL" below
```

#### Install WSL

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

**Output:**

```
Installing: Windows Subsystem for Linux
...
The requested operation is successful.
Please restart your computer to complete the installation.
```

Restart your computer, then open **Ubuntu** from the Start menu (WSL installs Ubuntu by default).

:::tip
All remaining commands in this lesson are run inside your **WSL2 Ubuntu terminal**, not PowerShell.
:::

#### Install Node.js 22+

Inside your Ubuntu terminal, check if Node.js is already installed:

```bash
node --version
```

If the version is below v22 (or the command is not found), install it:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Verify:

```bash
node --version
```

**Expected output:** `v22.x.x` or higher.

#### Install OpenClaw

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

**Output:**

```
OpenClaw installer starting...
Downloading latest release...
Installing to ~/.openclaw/bin...
Adding to PATH...
Installation complete!

Run 'source ~/.bashrc' or open a new terminal to use openclaw.
```

Reload your shell and verify:

```bash
source ~/.bashrc
openclaw --version
```

**Expected output:** `openclaw 2026.x.x`

If you see "command not found", open a new Ubuntu terminal window and try again.

::macos

#### Check Node.js Version

```bash
node --version
```

**Expected output:** `v22.x.x` or higher.

If your version is below v22 (or the command is not found), install the latest LTS from [nodejs.org](https://nodejs.org/) or via Homebrew:

```bash
brew install node@22
```

#### Install OpenClaw

Open Terminal and run:

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

**Output:**

```
OpenClaw installer starting...
Downloading latest release...
Installing to ~/.openclaw/bin...
Adding to PATH...
Installation complete!

Run 'source ~/.zshrc' or open a new terminal to use openclaw.
```

Reload your shell and verify:

```bash
source ~/.zshrc
openclaw --version
```

**Expected output:** `openclaw 2026.x.x`

If you see "command not found", open a new terminal window and try again — the installer updated your PATH, but your current session loaded before that change.

::linux

#### Check Node.js Version

```bash
node --version
```

**Expected output:** `v22.x.x` or higher.

If your version is below v22 (or the command is not found), install it:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### Install OpenClaw

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

**Output:**

```
OpenClaw installer starting...
Downloading latest release...
Installing to ~/.openclaw/bin...
Adding to PATH...
Installation complete!

Run 'source ~/.bashrc' or open a new terminal to use openclaw.
```

Reload your shell and verify:

```bash
source ~/.bashrc
openclaw --version
```

**Expected output:** `openclaw 2026.x.x`

If you see "command not found", open a new terminal window and try again.

::::

### First Verification: `openclaw doctor`

After installation, run the system diagnostic:

```bash
openclaw doctor
```

**Output:**

```
OpenClaw System Check
---------------------
Node.js:        v22.x.x  ✓
OpenClaw CLI:   2026.x.x ✓
Configuration:  Not yet configured (run 'openclaw onboard')
Gateway:        Not running
Telegram:       Not configured
LLM Provider:   Not configured

Status: Installation OK. Run 'openclaw onboard' to complete setup.
```

This command is your best friend for the rest of this lesson. Whenever something seems wrong, run `openclaw doctor` first. It checks everything and tells you what needs attention.

---

## Step 2: Run the Onboard Wizard

This is the main event. The onboard wizard walks you through LLM provider selection _and_ Telegram setup in a single interactive flow.

```bash
openclaw onboard
```

The wizard asks questions and configures everything based on your answers. Here is what to expect:

### What `openclaw onboard` Does

```
openclaw onboard
      │
      ▼
┌─────────────────────────────┐
│ 1. Select LLM Provider      │
│    Kimi / Gemini / Ollama   │
│    / Claude / Other          │
├─────────────────────────────┤
│ 2. Enter API Key or OAuth   │
│    (depends on provider)     │
├─────────────────────────────┤
│ 3. Test LLM Connection      │
│    Sends test query          │
├─────────────────────────────┤
│ 4. Select Channel            │
│    Telegram / Discord        │
├─────────────────────────────┤
│ 5. Enter Bot Token           │
│    (from Telegram BotFather) │
├─────────────────────────────┤
│ 6. Test Channel Connection   │
│    Verifies bot token works  │
├─────────────────────────────┤
│ 7. Summary                   │
│    Shows all configuration   │
└─────────────────────────────┘
```

The wizard handles steps that the current lesson previously broke into separate manual commands. You no longer need to run individual `openclaw config set` commands — the wizard does it all.

### Choosing Your LLM Provider

When the wizard asks you to select a provider, you will see your options:

| Provider                 | Free Tier                      | Setup                                                             | Best For                               |
| ------------------------ | ------------------------------ | ----------------------------------------------------------------- | -------------------------------------- |
| **Kimi K2.5 (Moonshot)** | 1.5M tokens/day                | API key from [platform.moonshot.ai](https://platform.moonshot.ai) | Best quality free option (recommended) |
| **Google Gemini**        | $0.50/M tokens free credit     | OAuth login with Google account                                   | Easiest setup, no key management       |
| **Ollama**               | Unlimited (runs locally)       | Requires 16GB+ RAM, separate install                              | Complete privacy, no internet needed   |
| **Claude**               | No free tier ($15-75/M tokens) | API key from console.anthropic.com                                | Highest quality (paid only)            |

**Pick one path.** You can add other providers later. If you are unsure, pick **Kimi K2.5** — it has the most generous free tier with strong quality.

---

### Path A: Kimi K2.5 (Recommended)

Moonshot's Kimi K2.5 offers the best balance of quality and free limits: 1.5 million tokens per day at no cost, with a 256K context window.

**Before running the wizard**, get your API key:

1. Go to [platform.moonshot.ai](https://platform.moonshot.ai)
2. Create an account (email verification required)
3. Navigate to **API Keys**
4. Click **Create new API key**
5. Copy the key (it starts with `sk-`)

**Now run the wizard:**

```bash
openclaw onboard
```

When the wizard asks for your LLM provider, select **Kimi K2.5 / Moonshot**. It will prompt for your API key:

```
Select your LLM provider:
  ❯ Kimi K2.5 (Moonshot) - 1.5M tokens/day free
    Google Gemini - OAuth login
    Ollama - Local models
    Claude - Anthropic API
    Other

Enter your Moonshot API key: sk-xxxxxxxxxxxxxxxx
Testing connection to Kimi K2.5...
✓ Success! Model responded correctly.
```

The wizard continues to channel setup (see Step 3 below, which happens inside the same wizard).

---

### Path B: Google Gemini (Easiest)

Google Gemini uses OAuth — you sign in with your Google account instead of managing API keys. This is the lowest-friction option.

**Run the wizard:**

```bash
openclaw onboard
```

Select **Google Gemini** when prompted. The wizard opens your browser:

```
Select your LLM provider:
    Kimi K2.5 (Moonshot) - 1.5M tokens/day free
  ❯ Google Gemini - OAuth login
    Ollama - Local models
    Claude - Anthropic API

Opening browser for Google authentication...
Sign in with your Google account and authorize OpenClaw.
Waiting for authorization...
✓ Authorization successful!
Testing connection to Gemini...
✓ Success! Model responded correctly.
```

The wizard continues to channel setup.

---

### Path C: Ollama (Local, Free Forever)

Ollama runs models entirely on your machine. Nothing leaves your computer. This requires more hardware but offers unlimited usage with complete privacy.

**Requirements**: 16GB+ RAM recommended (8GB minimum for smaller models).

**Step 1**: Install Ollama (if not already installed):

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Step 2**: Pull a capable model:

```bash
ollama pull qwen2.5-coder:14b
```

**Output:**

```
pulling manifest
pulling 9f43d8c7eddd... 100% ▕████████████████▏ 8.1 GB
verifying sha256 digest
writing manifest
success
```

This downloads approximately 8GB. Wait for it to complete.

**Step 3**: Run the onboard wizard:

```bash
openclaw onboard
```

Select **Ollama** when prompted. The wizard detects your local Ollama instance and asks which model to use:

```
Select your LLM provider:
    Kimi K2.5 (Moonshot) - 1.5M tokens/day free
    Google Gemini - OAuth login
  ❯ Ollama - Local models
    Claude - Anthropic API

Detected Ollama at localhost:11434
Available models:
  ❯ qwen2.5-coder:14b (8.1 GB)

Testing connection...
✓ Success! Model responded correctly.
```

---

## Step 3: Connect Telegram

If you ran `openclaw onboard` in Step 2, the wizard transitions directly into channel setup after configuring your LLM. If you already completed the wizard and need to reconfigure Telegram separately, run `openclaw onboard` again — it detects existing configuration and lets you modify specific sections.

### Create Your Bot with BotFather

The wizard will ask for a Telegram bot token. Here is how to get one:

1. Open Telegram on your phone or desktop
2. Search for **@BotFather** (look for the verified blue checkmark)
3. Start a conversation and send: `/newbot`
4. BotFather asks for a **display name**. Enter something descriptive: `My AI Employee`
5. BotFather asks for a **username**. Enter something unique ending in `bot`: `my_ai_employee_12345_bot`

BotFather responds with your token:

```
Done! Congratulations on your new bot.
Use this token to access the HTTP API:
7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Keep your token secure and store it safely.
```

**Copy this token.** Return to your terminal where the onboard wizard is waiting:

```
Select your channel:
  ❯ Telegram
    Discord

Enter your Telegram bot token: 7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Testing Telegram connection...
✓ Bot connected: @my_ai_employee_12345_bot
```

### Enable Group Mode (Optional)

If you want your bot to work in Telegram groups (not just direct messages), configure privacy mode:

1. In Telegram, message **@BotFather** again
2. Send `/mybots`
3. Select your bot
4. Go to **Bot Settings** then **Group Privacy**
5. Select **Turn off** (this allows the bot to see group messages)

This step is optional. Your bot works in direct messages without changing privacy settings.

### Onboard Summary

At the end of the wizard, you see a configuration summary:

```
OpenClaw Configuration Summary
──────────────────────────────
LLM Provider:  Kimi K2.5 (Moonshot)
Model:         moonshot-v1-128k
Channel:       Telegram (@my_ai_employee_12345_bot)
Gateway:       Not yet started

Run 'openclaw gateway run' to start your AI Employee.
```

---

## Step 4: Start the Gateway

The gateway is the process that ties everything together. It listens for Telegram messages, forwards them to your LLM provider, and sends responses back.

**For testing** (runs in the foreground — you see all logs):

```bash
openclaw gateway run --port 18789
```

**Output:**

```
OpenClaw Gateway starting...
Loading configuration...
Connecting to Telegram...
✓ Telegram bot connected: @my_ai_employee_12345_bot
Gateway ready on port 18789
Waiting for messages...
```

Leave this terminal window open. The gateway must stay running to receive messages.

### Making the Gateway Persistent

Running `openclaw gateway run` in the foreground is fine for testing, but it stops when you close the terminal. For a persistent setup, you have two options:

**Option A: Background process** (quick, stops on reboot):

```bash
openclaw gateway start
```

**Output:**

```
Gateway started in background (PID 12345)
```

Manage with:

```bash
openclaw gateway stop      # Stop the background gateway
openclaw gateway restart   # Restart it
openclaw status            # Check if it's running
```

**Option B: System service** (recommended, survives reboots):

```bash
openclaw gateway install
```

**Output:**

```
Installing OpenClaw gateway as system service...
  macOS: Creating launchd service...
  (or Linux: Creating systemd service...)
✓ Service installed and started.
  Gateway will start automatically on boot.
```

This installs the gateway as a `launchd` service on macOS or a `systemd` service on Linux. Your AI Employee starts automatically when your computer boots.

For now, `openclaw gateway run` in the foreground is fine. You can set up persistence later.

---

## Step 5: Send Your First Message

Open Telegram on your phone. Find your bot by searching for its username (`@my_ai_employee_12345_bot`).

Send a message:

```
Hello, who are you?
```

### First-Time Pairing

For security, OpenClaw requires you to approve new conversations. The first time you message the bot, it responds with a pairing code in Telegram:

```
Pairing required. Your code: ABC123
Approve this in the terminal where your gateway is running.
```

Look at the terminal where your gateway is running. You will see a prompt:

```
[PAIRING] New conversation from Telegram user @yourusername
Pairing code: ABC123
Approve this pairing? (y/n): y
✓ Pairing approved for Telegram user @yourusername
```

Type `y` and press Enter to approve. The pairing happens in the terminal where the gateway is running — you confirm it right there.

Now send your message again in Telegram:

```
Hello, who are you?
```

**Expected response:**

```
Hello! I'm your AI assistant, running through OpenClaw. I'm here to help
you with tasks, answer questions, and work alongside you. What would
you like to accomplish today?
```

**You now have a working AI Employee.** Message it from anywhere, at any time, as long as the gateway is running.

---

## Step 6: Verify Everything Works

Run a full system diagnostic:

```bash
openclaw doctor
```

**Output (healthy system):**

```
OpenClaw System Check
---------------------
Node.js:        v22.11.0  ✓
OpenClaw CLI:   2026.1.15 ✓
Configuration:  Complete  ✓
Gateway:        Running on port 18789  ✓
Telegram:       Connected (@my_ai_employee_12345_bot)  ✓
LLM Provider:   Kimi K2.5 (Moonshot) - responding  ✓

Status: All systems operational.
```

If any line shows an issue, the doctor tells you what to fix. This is always your first step when troubleshooting.

Check the gateway status separately:

```bash
openclaw status
```

**Output:**

```
Gateway: running (PID 12345, port 18789)
Uptime: 5 minutes
Messages processed: 2
```

Quick health check:

```bash
openclaw health
```

**Output:**

```
✓ Gateway healthy
✓ LLM provider responding
✓ Telegram connected
```

---

## Troubleshooting

When something goes wrong, always start with `openclaw doctor`. It diagnoses most common issues automatically.

### "command not found: openclaw"

Your shell did not load the updated PATH. Try:

```bash
source ~/.bashrc  # or source ~/.zshrc on macOS
```

**Output:**
(No output means it worked)

If that does not help, open a completely new terminal window. The installer added `openclaw` to your PATH, but your current session loaded before that change.

### "Node version too old"

OpenClaw requires Node.js 22+. Check your version:

```bash
node --version
```

**Output:**

```
v18.17.0
```

If below v22, install the latest LTS from [nodejs.org](https://nodejs.org/). On Linux/WSL, you can use:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### "Invalid bot token"

Double-check you copied the entire token from BotFather. The token format is:

```
1234567890:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

It must include both parts — the number, the colon, and the letters. A common mistake is missing the last few characters when copying.

If you need to reconfigure the token:

```bash
openclaw config set channels.telegram.botToken "YOUR_CORRECT_TOKEN"
```

### "No response from bot"

Work through these checks in order:

1. **Is the gateway running?** Check your terminal — you should see "Waiting for messages..."
2. **Did you approve the pairing?** Look in the gateway terminal for a pairing prompt
3. **Is your LLM provider working?** Run `openclaw doctor` to check
4. **Are you DMing the bot?** Pairing only works in direct messages, not groups

### "Gateway won't start"

Check if another process is using the port:

```bash
lsof -i :18789
```

If something is using it, either stop that process or use a different port:

```bash
openclaw gateway run --port 18790
```

### "LLM provider connection failed"

This usually means your API key is invalid or expired. Reconfigure through the wizard:

```bash
openclaw onboard
```

The wizard detects your existing configuration and lets you update just the LLM provider section.

---

## What You Built

Here is the complete architecture now running on your machine:

```
Your Phone (Telegram)
      │
      ▼
┌─────────────────────────────┐
│ Telegram Bot                │
│ @my_ai_employee_12345_bot   │
└─────────────────────────────┘
      │
      ▼
┌─────────────────────────────┐
│ OpenClaw Gateway            │
│ Running on your machine     │
│ Port 18789                  │
└─────────────────────────────┘
      │
      ▼
┌─────────────────────────────┐
│ LLM Provider                │
│ Kimi K2.5 / Gemini / Ollama │
└─────────────────────────────┘
```

Your phone sends a message through Telegram's servers to your bot. The OpenClaw gateway running on your machine picks it up, sends it to your chosen LLM provider, gets a response, and sends it back through Telegram to your phone. The whole round trip typically takes 2-5 seconds.

In the next lesson, you will put this AI Employee to work on real tasks — not just answering questions, but completing multi-step work on your behalf.

---

## Try With AI

Now that your AI Employee is running on Telegram, test its capabilities with these prompts.

### Prompt 1: Self-Awareness Check

Open Telegram and send to your bot:

```
Introduce yourself. What can you do for me? What are your limitations?
Be honest about what you cannot do.
```

**What you are learning:** How well your AI Employee understands its own capabilities and boundaries. A good AI Employee is honest about what it cannot do (like browsing the web or accessing your files) rather than making promises it cannot keep. Pay attention to whether the response matches reality — can it actually do what it claims?

### Prompt 2: Multi-Step Reasoning

Send to your bot:

```
I need to plan a 30-minute morning routine that includes exercise,
breakfast, and reviewing my calendar. Create a realistic minute-by-minute
timeline. Flag anything that seems unrealistic.
```

**What you are learning:** Whether your AI Employee can break down a constrained problem, manage tradeoffs (30 minutes is tight for three activities), and self-critique its own output. Notice whether it asks clarifying questions or makes assumptions. This is the difference between a chatbot (which answers) and an employee (which thinks through the problem).

### Prompt 3: Your Domain

Send to your bot:

```
I work in [your field - e.g., marketing, software development, teaching,
finance]. Give me three specific tasks you could help me with daily,
and three tasks that are beyond your current capabilities. Be concrete,
not generic.
```

**What you are learning:** How the AI Employee adapts to your specific context. Replace the bracketed text with your actual field. The quality of its response reveals how useful this tool will be in _your_ work, not just in generic demos. If the "beyond capabilities" list is too short, your employee might be overconfident — that is worth noting.

**Safety Note:** Your AI Employee communicates through Telegram's servers. Do not share passwords, financial account numbers, or sensitive personal data through this channel. Treat it like any messaging app — useful for tasks, not for secrets.
