---
sidebar_position: 2
title: "Lesson 2: Setup Your AI Employee"
description: "Install OpenClaw and connect Telegram in under 60 minutes with free LLM options"
keywords: [openclaw setup, telegram bot, kimi k2.5, gemini, ollama, installation, ai employee]
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

In the next 45-60 minutes, you will have an AI Employee responding to your messages on Telegram. Not a concept. Not a demo. A working assistant that responds when you message it from your phone.

This lesson walks you through every step: installing the OpenClaw platform, choosing a free LLM provider, connecting Telegram, and sending your first message. You will encounter decision points where you pick the path that fits your situation. All paths lead to the same destination: a working AI Employee.

By the end, you will have something tangible. You can message your AI Employee from anywhere, at any time. The "wow" moment is about 45 minutes away.

## What You Will Accomplish

| Step | Time | Outcome |
|------|------|---------|
| Install OpenClaw | 5 min | CLI ready |
| Choose LLM Provider | 10 min | Model configured |
| Connect Telegram | 10 min | Bot token set |
| Start Gateway | 2 min | System running |
| First Message | 5 min | AI responds |
| **Total** | **~32 min** | **Working AI Employee** |

The estimates assume everything goes smoothly. Budget 45-60 minutes to account for troubleshooting.

## Prerequisites

Before starting, verify you have:

**Node.js 22 or higher**:
```bash
node --version
```

If you see `v22.0.0` or higher, you are ready. If your version is lower, visit [nodejs.org](https://nodejs.org/) and install the LTS version.

**Telegram Account**: You need the Telegram app on your phone. If you do not have it, download it from your app store and create an account. This takes 2 minutes.

**45-60 Minutes**: Find uninterrupted time. Setup involves multiple steps, and context-switching makes it harder.

## Step 1: Install OpenClaw (5 minutes)

Open your terminal and run the one-line installer:

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

After installation completes, reload your shell:

```bash
source ~/.bashrc  # or source ~/.zshrc on macOS
```

Verify the installation worked:

```bash
openclaw --version
```

**Output:**
```
openclaw 2026.1.15
```

If you see a version number, OpenClaw is installed. If you see "command not found", open a new terminal window and try again.

### Windows Users

Use Windows Subsystem for Linux (WSL2). Open PowerShell as Administrator and run:

```powershell
wsl --install
```

After WSL installs, open Ubuntu from the Start menu and run the Linux installation commands above.

## Step 2: Choose Your LLM Path

OpenClaw needs a language model to power your AI Employee. You have three free options:

| Path | Provider | Free Tier | Best For |
|------|----------|-----------|----------|
| **A** | Kimi K2.5 | 1.5M tokens/day | Best quality, recommended |
| **B** | Gemini | 1000 requests/day | Easiest setup (OAuth) |
| **C** | Ollama | Unlimited | Privacy, runs locally |

**Choose one path and follow its instructions.** You can add other providers later.

---

### Path A: Kimi K2.5 (Recommended)

Moonshot's Kimi K2.5 offers the best balance of quality and free tier limits. You get 1.5 million tokens per day for free, with a 256K context window.

**Get your API key:**

1. Go to [platform.moonshot.ai](https://platform.moonshot.ai)
2. Create an account (email verification required)
3. Navigate to API Keys
4. Click "Create new API key"
5. Copy the key (starts with `sk-`)

**Configure OpenClaw:**

```bash
openclaw onboard --auth-choice moonshot-api-key
```

The wizard will prompt you:

```
Enter your Moonshot API key: sk-xxxxxxxxxxxxxxxx
Testing connection to Kimi K2.5...
Success! Model responded correctly.
Configuration saved.
```

**Verification**: The wizard tests the connection automatically. If you see "Success!", your LLM is ready.

---

### Path B: Google Gemini (Easiest)

Google Gemini uses OAuth authentication, meaning you sign in with your Google account instead of managing API keys. This is the simplest path if you want minimal friction.

**Configure OpenClaw:**

```bash
openclaw onboard --auth-choice google-gemini-cli
```

The wizard will open your browser:

```
Opening browser for Google authentication...
Sign in with your Google account and authorize OpenClaw.
Waiting for authorization...
```

Sign in with your Google account and click "Allow". The terminal will confirm:

```
Authorization successful!
Testing connection to Gemini Flash-Lite...
Success! Model responded correctly.
Configuration saved.
```

**Verification**: The wizard tests automatically. If you see "Success!", proceed to Step 3.

---

### Path C: Ollama (Local, Free Forever)

Ollama runs models entirely on your computer. Nothing leaves your machine. This requires more resources but offers unlimited usage with complete privacy.

**Requirements**: 16GB+ RAM recommended, 8GB minimum

**Install Ollama:**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Pull a capable model:**

```bash
ollama pull qwen2.5-coder:14b
```

This downloads approximately 8GB. Wait for completion.

**Configure OpenClaw:**

```bash
export OLLAMA_API_KEY="ollama-local"
openclaw config set agents.defaults.model.primary "ollama/qwen2.5-coder:14b"
```

**Verification**: Test the model directly:

```bash
ollama run qwen2.5-coder:14b "Say hello"
```

**Output:**
```
Hello! How can I help you today?
```

If the model responds, proceed to Step 3.

---

## Step 3: Connect Telegram (10 minutes)

Now you will create a Telegram bot and connect it to OpenClaw. This is how your AI Employee receives messages from your phone.

### Create Your Bot

1. Open Telegram on your phone or desktop
2. Search for **@BotFather** (verified blue checkmark)
3. Start a conversation and send: `/newbot`
4. BotFather asks for a name. Enter something descriptive: `My AI Employee`
5. BotFather asks for a username. Enter something unique ending in `bot`: `my_ai_employee_12345_bot`

BotFather responds with your token:

```
Done! Congratulations on your new bot.
Use this token to access the HTTP API:
7123456789:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Keep your token secure and store it safely.
```

**Copy this token.** You will need it in the next step.

### Configure the Token

Set your bot token in OpenClaw:

```bash
openclaw config set channels.telegram.botToken "YOUR_TOKEN_HERE"
```

Replace `YOUR_TOKEN_HERE` with the actual token from BotFather.

**Output:**
```
Configuration updated: channels.telegram.botToken
```

## Step 4: Start the Gateway (2 minutes)

The gateway is the process that connects everything together: your Telegram bot, your LLM provider, and the AI Employee logic.

Start it:

```bash
openclaw gateway run --port 18789 --verbose
```

**Output:**
```
OpenClaw Gateway starting...
Loading configuration...
Connecting to Telegram...
Telegram bot connected: @my_ai_employee_12345_bot
Gateway ready on port 18789
Waiting for messages...
```

Leave this terminal window open. The gateway must stay running to receive messages.

## Step 5: Send Your First Message (5 minutes)

Open Telegram on your phone. Find your bot by searching for its username (`@my_ai_employee_12345_bot`).

Send a message:
```
Hello, who are you?
```

**What happens next:**

1. Telegram delivers your message to your bot
2. OpenClaw gateway receives it
3. Gateway sends it to your LLM provider
4. LLM generates a response
5. Gateway sends the response back through Telegram
6. You receive it on your phone

**First-time pairing**: For security, OpenClaw requires you to approve new conversations. Your bot will respond with a pairing code:

```
Pairing required. Code: ABC123
```

In your terminal (open a new tab), approve the pairing:

```bash
openclaw pairing approve telegram ABC123
```

**Output:**
```
Pairing approved for Telegram user.
```

Now send your message again:
```
Hello, who are you?
```

**Expected response:**
```
Hello! I'm your AI assistant, running through OpenClaw. I'm here to help
you with tasks, answer questions, and work alongside you. What would
you like to accomplish today?
```

**You now have a working AI Employee.** Message it from anywhere, at any time. The gateway will process your requests as long as it is running.

## Troubleshooting

### "command not found: openclaw"

Your shell did not load the new PATH. Try:

```bash
source ~/.bashrc  # or ~/.zshrc
```

If that does not work, open a new terminal window.

### "Node version too old"

OpenClaw requires Node.js 22+. Check your version:

```bash
node --version
```

If below v22, install the latest LTS from [nodejs.org](https://nodejs.org/).

### "Invalid bot token"

Double-check you copied the entire token from BotFather. The token format is:
```
1234567890:AAHxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

It must include both parts (numbers, colon, letters).

### "No response from bot"

1. Check the gateway is running (you should see "Waiting for messages...")
2. Verify you approved the pairing code
3. Check your LLM configuration worked (the onboard wizard should have tested it)

### "Pairing code not appearing"

Make sure you are DMing the bot, not messaging it in a group. Pairing codes only appear for direct messages.

### "Gateway won't start"

Check if another process is using port 18789:

```bash
lsof -i :18789
```

If something is running, either stop it or use a different port:

```bash
openclaw gateway run --port 18790 --verbose
```

## What You Built

You now have:

```
Your Phone (Telegram)
      │
      ▼
┌─────────────────────────┐
│ Telegram Bot            │
│ @my_ai_employee_bot     │
└─────────────────────────┘
      │
      ▼
┌─────────────────────────┐
│ OpenClaw Gateway        │
│ Running on port 18789   │
└─────────────────────────┘
      │
      ▼
┌─────────────────────────┐
│ LLM Provider            │
│ Kimi / Gemini / Ollama  │
└─────────────────────────┘
```

This is a complete AI Employee infrastructure. In the next lesson, you will put it to work on real tasks.

## Try With AI

Now that your AI Employee is running, test its capabilities with these prompts.

### Prompt 1: Introduction and Capabilities

Open Telegram and send:

```
Introduce yourself. What can you do for me? What are your limitations?
```

**What you are learning:** Understanding your AI Employee's self-awareness. A well-configured AI Employee knows its capabilities and boundaries. Pay attention to whether it accurately describes what it can and cannot do.

### Prompt 2: Real-Time Information

```
What is today's date and what day of the week is it? Can you check the weather
for New York City?
```

**What you are learning:** Discovering tool boundaries. Your AI Employee may or may not have access to real-time information depending on configuration. This prompt reveals what external capabilities are available versus what requires additional setup (like MCP servers for web search).

### Prompt 3: Multi-Step Reasoning

```
I need to plan a 30-minute morning routine that includes exercise, breakfast,
and reviewing my schedule. Help me create a realistic timeline.
```

**What you are learning:** Testing reasoning and practical advice. This prompt requires the AI Employee to break down a problem, consider constraints (30 minutes total), and provide actionable output. Notice how it structures its response and whether it asks clarifying questions.

**Safety Note:** Your AI Employee is connected to the internet through Telegram. Do not share passwords, financial information, or sensitive personal data through this channel. Treat it like any other messaging app where security depends on your behavior.
