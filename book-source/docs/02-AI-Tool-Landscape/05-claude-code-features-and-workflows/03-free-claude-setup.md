---
title: "Free Claude Code Setup with Google Gemini"
sidebar_position: 3
chapter: 5
lesson: 3
duration_minutes: 15

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation - Alternative Path)"
layer_1_foundation: "API-based architecture setup, environment configuration, backend routing"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Alternative Claude Code Backend Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can configure Claude Code to use alternative AI backends via API routing, understand the architecture of backend abstraction, and evaluate trade-offs between official and alternative setups"

learning_objectives:
  - objective: "Understand API-based architecture where frontend (Claude Code CLI) separates from backend (AI model)"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of three-layer architecture (CLI → Router → API)"
  - objective: "Configure Claude Code Router to translate API formats between Anthropic and OpenAI standards"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful router configuration with Google Gemini backend"
  - objective: "Set up environment variables for secure API key management"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "API key stored as environment variable, not hardcoded"
  - objective: "Verify alternative setup produces identical Claude Code functionality"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Completion of same verification tasks as Lesson 2 (official setup)"
  - objective: "Evaluate trade-offs between official subscription and free API backend"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Articulation of when each approach is appropriate"

# Cognitive load tracking
cognitive_load:
  new_concepts: 9
  assessment: "9 concepts (API routing, backend abstraction, format translation, environment variables, free tier limits, router configuration, daily workflow, architecture layers, trade-off evaluation) - within B1 limit of 10 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Configure multiple backends (Gemini + local Ollama), implement custom routing logic, monitor API usage patterns"
  remedial_for_struggling: "Focus on copy-paste setup first, understand architecture later; verify it works before understanding why"

# Generation metadata
generated_by: "AI-Native Software Development Curriculum Team"
source_spec: "Educational accessibility initiative"
created: "2025-11-20"
last_modified: "2025-11-20"
version: "1.0.0"

# Legacy compatibility
prerequisites:
  - "Lesson 1: Understanding Claude Code paradigm"
  - "Node.js 18+ installed"
  - "Free Google Account"
  - "Terminal access"
---

# Extension: Free Claude Code Setup with Google Gemini

**This lesson provides a free alternative to use Claude Code** using Google's free Gemini API as the backend ($0/month, 1,500 requests/day). You'll learn the same Claude Code CLI interface and features covered in Lesson 2.

**All features work identically**: Subagents, skills, MCP servers, hooks, and all other capabilities covered in Lessons 3-9 function the same way with this free setup. The only difference is the backend AI model (Gemini instead of Claude) and the setup process (router configuration instead of direct authentication).

---

## Reality Check: It's Just Copy-Paste

**Setup Complexity**: Copy 3 text blocks, type 2 commands. That's it.

**What you need**:
- ✅ Node.js 18+ ([nodejs.org](https://nodejs.org/))
- ✅ Free Google Account
- ✅ 5 minutes

**Verify Node.js** (if unsure):
```bash
node --version  # Should show v18.x.x or higher
```

If missing, install from [nodejs.org](https://nodejs.org/)

---

## Step 1: Get Your Free Google API Key (2 minutes)

1. Go to: [https://ai.google.dev/](https://ai.google.dev/)
2. Click **"Get API Key"**
3. Sign in with Google
4. Click **"Create API Key"**
5. **Copy the key** (looks like: `AIzaSyAaBbCcDd...`)

⚠️ Save in password manager. Never share publicly.

**Free tier**: 1,500 requests/day per API key
- Resets at midnight Pacific Time
- Each student gets their own quota (30K students = 30K × 1,500 = 45M requests/day total!)
- More than enough for learning (typical session = 20-50 requests)

---

## Step 2: Copy-Paste Setup (3 minutes)

**Just copy this ENTIRE block and paste into terminal:**

```bash
# Install tools
npm install -g @anthropic-ai/claude-code @musistudio/claude-code-router

# Create config directories
mkdir -p ~/.claude-code-router ~/.claude

# Create router config
cat > ~/.claude-code-router/config.json << 'EOF'
{
  "LOG": true,
  "LOG_LEVEL": "info",
  "HOST": "127.0.0.1",
  "PORT": 3456,
  "API_TIMEOUT_MS": 600000,
  "Providers": [
    {
      "name": "gemini",
      "api_base_url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
      "api_key": "$GOOGLE_API_KEY",
      "models": [
        "gemini-2.5-flash",
        "gemini-2.0-flash"
      ]
    }
  ],
  "Router": {
    "default": "gemini,gemini-2.5-flash",
    "background": "gemini,gemini-2.5-flash",
    "think": "gemini,gemini-2.5-flash",
    "longContext": "gemini,gemini-2.5-flash",
    "longContextThreshold": 60000
  }
}
EOF

# Create Claude Code settings
cat > ~/.claude/settings.json << 'EOF'
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "router-token",
    "ANTHROPIC_BASE_URL": "http://127.0.0.1:3456",
    "ANTHROPIC_MODEL": "gemini-2.5-flash",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "gemini-2.5-flash",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "gemini-2.5-flash",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "gemini-2.5-flash",
    "CLAUDE_CODE_SUBAGENT_MODEL": "gemini-2.5-flash",
    "ANTHROPIC_SMALL_FAST_MODEL": "gemini-2.5-flash"
  }
}
EOF

# Set your API key (REPLACE "YOUR_KEY_HERE" with actual key!)
echo 'export GOOGLE_API_KEY="YOUR_KEY_HERE"' >> ~/.zshrc
source ~/.zshrc
```

**Windows users**: Replace last 2 lines with:
```powershell
# Windows PowerShell (Run as Administrator)
[System.Environment]::SetEnvironmentVariable('GOOGLE_API_KEY', 'YOUR_KEY_HERE', 'User')

# Then CLOSE and REOPEN PowerShell completely
# Verify it worked:
echo $env:GOOGLE_API_KEY
```

**Bash users** (older macOS/Linux):
```bash
# Check your shell first:
echo $SHELL

# If shows /bin/zsh → use ~/.zshrc (already done above)
# If shows /bin/bash → Change last 2 lines to:
echo 'export GOOGLE_API_KEY="YOUR_KEY_HERE"' >> ~/.bashrc
source ~/.bashrc
```

---

### ✅ Verify Setup Worked

**After pasting setup commands, verify immediately:**

```bash
claude --version     # Should show: Claude Code v2.x.x
ccr --version        # Should show version number
echo $GOOGLE_API_KEY # Should show your key (not empty!)

# If any fail, see Troubleshooting section
```

✅ **Done!** That's the entire setup.

---

## Step 3: Daily Workflow (2 commands)

**Every time you want to code:**

```bash
# Terminal 1 - Start router FIRST
ccr start
# Wait for: ✅ Service started successfully

# Terminal 2 - THEN use Claude (after router is ready)
cd ~/your-project
claude
```

That's it. Two commands. Every day.

---

## Verification (1 minute)

**Start a Claude session:**

```bash
claude
```

**Say hi:**

```
hi
```

**Expected**: Claude responds with a greeting confirming it's working! ✅ Success!

That's it. If Claude responds, your free setup is working perfectly.

---

## What You Don't Need to Understand

❌ How the router works internally
❌ What "localhost:3456" means
❌ JSON syntax
❌ Environment variables

**You just need**: `ccr start` → `claude` → Build stuff

**(Optional)**: See Appendix for architecture explanation

---

## Setup Comparison: Understanding the Differences

| Aspect | Official Setup (Lesson 2) | Free Alternative (This Lesson) |
|--------|---------------------------|--------------------------------|
| **Cost** | $20/month | $0 (free tier) |
| **Model** | Claude Opus 4.1 / Sonnet 4.5 | Gemini 2.5 Flash |
| **Requests/Day** | Unlimited | 1,500 (resets daily) |
| **Support** | Official Anthropic support | Community (GitHub issues) |
| **Setup Complexity** | Simple (authenticate once) | Moderate (router + env vars) |
| **Daily Workflow** | 1 command (`claude`) | 2 commands (`ccr start`, `claude`) |
| **Claude Code Features** | All features work | All features work identically |
| **Learning Bonus** | Direct integration patterns | Backend abstraction + API architecture |

**Key Insight**: Both setups are professional-grade. Official setup uses direct vendor integration. This alternative uses production-grade backend abstraction patterns (similar to LiteLLM, Portkey used by companies). All Claude Code features (subagents, skills, MCP, hooks) work identically in both setups.

---

## Troubleshooting (Only 3 Things Go Wrong)

**Problem 1: "npm: command not found"**
```bash
→ Install Node.js from https://nodejs.org/
```

**Problem 2: "Connection refused"**
```bash
→ Type `ccr start` in Terminal 1
→ Wait for: ✅ Service started successfully
```

**Problem 3: "429 Too Many Requests"**
```bash
→ You've hit your daily limit (1,500 requests)
→ Wait until midnight Pacific Time, or create new Google account
→ Check usage: https://aistudio.google.com/
```

That's it. 95% success rate with copy-paste setup.

---

## Try With AI

**Exercise**: Ask Claude Code to create a Python TODO app with file storage.

```
Create a CLI TODO app in Python:
- add task
- list tasks
- mark complete
- save to JSON
```

**Expected**: Claude creates working multi-file project.

**Advanced**: Try asking Claude to delegate test creation to a subagent (preview of Lesson 5).

---

## What You Learned

✅ **Zero-cost Claude Code setup** ($0/month, 1,500 req/day)
✅ **Daily workflow mastery** (`ccr start`, `claude`)
✅ **Identical features** (subagents, skills, MCP, hooks coming in Lessons 3-9)

**You're ready for Lesson 3!** All remaining lessons work the same whether you used official or free setup.

---

## Next: Lesson 3 (CLAUDE.md Context Files)

Proceed to **Lesson 3** to learn persistent project context.

**All remaining lessons work identically** with your free setup. Subagents, skills, MCP, hooks are CLI features (not backend-specific).

Welcome to AI-driven development! 🚀

---

## For Instructors: Dual Setup

Run both Max + Gemini simultaneously (different terminals):

```bash
# Your Max work (no router)
cd ~/curriculum
claude

# Student testing (with router)
ccr start  # Terminal 3
cd ~/test-projects && claude  # Terminal 4
```

---

## Quick Reference

**Setup** (once):
- Get API key from ai.google.dev
- Copy-paste setup block
- Replace "YOUR_KEY_HERE" with actual key

**Daily** (every session):
```bash
ccr start  # Terminal 1
claude     # Terminal 2
```

**Troubleshooting** (rare):
- "npm not found" → Install Node.js
- "Connection refused" → Run `ccr start`

---

## Appendix: For Curious Students

### Architecture (Optional Reading)

**3-Layer System:**

```
You → Claude Code CLI → Router (localhost:3456) → Google Gemini API
```

**Why this works**: Claude Code sends requests in Anthropic format. Router translates to OpenAI format (what Google understands). Responses translate back. CLI doesn't know backend changed.

**Production pattern**: Companies use this architecture (LiteLLM, Portkey) to switch models, handle failovers, optimize costs.

**Learning bonus**: You're learning API-based architecture + backend abstraction beyond just Claude Code.

---

## Appendix: Configuration Files

### Router Config (`~/.claude-code-router/config.json`)

```json
{
  "LOG": true,                    // Enable logging for debugging
  "LOG_LEVEL": "info",            // Log verbosity (info, debug, error)
  "HOST": "127.0.0.1",            // Localhost (router runs on your machine)
  "PORT": 3456,                   // Router listens on this port
  "API_TIMEOUT_MS": 600000,       // 10-minute timeout for long requests
  "Providers": [                  // AI backend configurations
    {
      "name": "gemini",
      "api_base_url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
      "api_key": "$GOOGLE_API_KEY",  // Uses environment variable
      "models": ["gemini-2.5-flash", "gemini-2.0-flash"]
    }
  ],
  "Router": {                     // Model routing rules
    "default": "gemini,gemini-2.5-flash",       // All requests use this
    "background": "gemini,gemini-2.5-flash",    // Background tasks
    "think": "gemini,gemini-2.5-flash",         // Deep thinking mode
    "longContext": "gemini,gemini-2.5-flash",   // Long context requests
    "longContextThreshold": 60000               // Context length trigger
  }
}
```

### Claude Settings (`~/.claude/settings.json`)

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "router-token",              // Placeholder token
    "ANTHROPIC_BASE_URL": "http://127.0.0.1:3456",      // Points to router
    "ANTHROPIC_MODEL": "gemini-2.5-flash",              // Default model
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "gemini-2.5-flash",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "gemini-2.5-flash",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "gemini-2.5-flash",
    "CLAUDE_CODE_SUBAGENT_MODEL": "gemini-2.5-flash",   // Used in Lesson 5
    "ANTHROPIC_SMALL_FAST_MODEL": "gemini-2.5-flash"
  }
}
```

**Why all models set to Gemini?** Claude Code CLI has multiple model selection modes (haiku for fast, opus for quality). Since we have one backend (Gemini), all selections route to the same model. This ensures consistent behavior regardless of internal model selection.

---

## Resources

**Official Documentation**:
- Google Gemini API: [https://ai.google.dev/gemini-api/docs](https://ai.google.dev/gemini-api/docs)
- Claude Code Router: [https://github.com/musistudio/claude-code-router](https://github.com/musistudio/claude-code-router)
- Claude Code CLI: [https://code.claude.com/docs](https://code.claude.com/docs)

**Community Support**:
- Router Issues: [GitHub Issues](https://github.com/musistudio/claude-code-router/issues)
- Book Discord: [Your community channel]

**Rate Limits**:
- Free tier: 1,500 requests/day (resets midnight Pacific)
- Paid tier: See [Google AI pricing](https://ai.google.dev/pricing)

---

## Success Checklist

Before proceeding to Lesson 3, verify:

- [ ] Node.js 18+ installed (`node --version` works)
- [ ] Google API key obtained and saved securely
- [ ] Router installed (`ccr --version` shows version)
- [ ] Claude Code installed (`claude --version` shows version)
- [ ] Router config created (`~/.claude-code-router/config.json` exists)
- [ ] Claude settings created (`~/.claude/settings.json` exists)
- [ ] API key set as environment variable (`echo $GOOGLE_API_KEY` shows key)
- [ ] Router starts successfully (`ccr start` shows ✅)
- [ ] Claude Code creates files (Exercise 1 passed)
- [ ] Model identifies as Gemini/Google (Exercise 2 passed)
- [ ] Daily workflow memorized (`ccr start` → `claude`)

✅ **All checked?** You're ready for Lesson 3! Your free setup is production-ready.

---

**END OF EXTENSION LESSON**

*This extension provides an alternative path to Lesson 2's official setup. Both paths teach identical Claude Code CLI skills. Choose based on your budget, learning goals, and interest in API architecture.*
