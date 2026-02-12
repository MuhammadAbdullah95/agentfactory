---
sidebar_position: 4
title: "Lesson 4: How Your Employee Works"
description: "Understanding the architecture: Gateway, Agents, Channels, Skills, and Models"
keywords: [openclaw architecture, gateway, channels, skills, mcp, agent runtime]
chapter: 12
lesson: 4
duration_minutes: 45

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Architecture Understanding"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Problem-Solving"
    measurable_at_this_level: "Can explain the 5 key components of an AI Employee system and how they interact"

  - name: "Component Identification"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Remember"
    digcomp_area: "Digital Literacy"
    measurable_at_this_level: "Can identify Gateway, Agents, Channels, Skills, and Model Providers as distinct components"

  - name: "Message Flow Comprehension"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "System Thinking"
    measurable_at_this_level: "Can trace a message from phone to response through the five-component architecture"

  - name: "Skill Portability Recognition"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Can explain why skills work across platforms and evaluate portability implications"

learning_objectives:
  - objective: "Identify the 5 key components of an AI Employee system"
    proficiency_level: "B1"
    bloom_level: "Remember"
    assessment_method: "Component identification exercise"

  - objective: "Explain how messages flow through the system from phone to response"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Message flow tracing explanation"

  - objective: "Understand why skills are portable across platforms"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Portability explanation with examples"

  - objective: "Recognize MCP as the universal connector between agents and external services"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "MCP role identification"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (Gateway, Agent Runtime, Channels, Skills, Model Providers, Session Management, MCP) within B1 limit (7-10 concepts). Related concepts cluster naturally: Gateway controls routing; Agent is the brain; Channels are communication paths; Skills are portable expertise; Models provide reasoning."

differentiation:
  extension_for_advanced: "Explore the OpenClaw source code on GitHub; trace the actual message flow through the codebase"
  remedial_for_struggling: "Focus on the central diagram and trace one message through all five components before moving to details"
---

# How Your Employee Works

You have a working AI Employee. When you message it on Telegram, it responds intelligently, remembers context from earlier in the conversation, and can even help with real work. But what's actually happening behind the scenes? When you type a message on your phone, what systems work together to produce that response?

Understanding this architecture matters for two reasons. First, when something breaks (and it will), you need mental models to diagnose where the problem is. Is the Gateway not routing messages? Is the LLM provider down? Is a skill misconfigured? Second, when you want to extend your employee's capabilities—adding new skills, connecting new channels, switching models—you need to know which component to modify.

This lesson maps the five key components that power your AI Employee. By the end, you'll be able to trace a message from your phone through every system until a response appears on your screen.

## The Five Components

Every AI Employee system has five essential components working together:

```
┌─────────────────────────────────────────────────────────────┐
│  1. GATEWAY (Control Plane)                                 │
│     Routes messages, manages sessions, handles auth         │
└─────────────────────────────────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  2. AGENTS  │   │ 3. CHANNELS │   │  4. SKILLS  │
│  (Runtime)  │   │  (Telegram, │   │  (Portable  │
│             │   │   Discord)  │   │   Expertise)│
└─────────────┘   └─────────────┘   └─────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│  5. MODEL PROVIDERS (Kimi, Gemini, Claude, Ollama)          │
└─────────────────────────────────────────────────────────────┘
```

Think of it like a company org chart. The **Gateway** is management—it decides where messages go and keeps everything organized. The **Agent** is the employee—the actual worker who thinks through problems and produces outputs. **Channels** are the communication systems—phone, email, Slack. **Skills** are the employee's expertise—things they've learned how to do well. And **Model Providers** are like the employee's education—where their intelligence comes from.

Let's examine each component in detail.

## Component 1: Gateway (The Control Plane)

The **Gateway** is the central nervous system of your AI Employee. Every message passes through it. Every response passes through it. It's the traffic controller that makes everything work together.

**What the Gateway Does:**

| Function | Description |
|----------|-------------|
| **Message Routing** | Receives messages from all channels, routes to the right agent |
| **Session Management** | Tracks conversations, maintains context between messages |
| **Authentication** | Verifies who's allowed to talk to your employee |
| **Pairing** | Controls which users can access which channels |
| **Configuration** | Stores settings for channels, agents, and providers |

**How the Gateway Runs:**

The Gateway runs as a **daemon**—a background service that starts automatically and keeps running. When you ran `openclaw onboard --install-daemon`, you installed this background service. It's always listening, ready to route messages.

```
                    ┌──────────────────────────────┐
   [Telegram]──────▶│                              │
                    │         GATEWAY              │
   [Discord]───────▶│                              │──────▶ [Agent Runtime]
                    │  • Routes messages           │
   [CLI]───────────▶│  • Manages sessions          │
                    │  • Handles authentication    │
   [Web UI]────────▶│                              │
                    └──────────────────────────────┘
```

**Why This Design Matters:**

Without a gateway, you'd need a separate integration for each channel. Telegram would talk directly to the agent. Discord would need its own connection. Adding a new channel would require modifying the agent.

With a gateway, adding a new channel is configuration, not code. The gateway normalizes messages from any source into a common format, routes them to the agent, and translates responses back to channel-specific formats. The agent never knows or cares which channel a message came from.

## Component 2: Agent Runtime (The Brain)

The **Agent** is where thinking happens. It receives messages from the Gateway, reasons about them using an LLM, takes actions using tools, and produces responses.

OpenClaw uses an embedded runtime called **pi-mono** as its agent brain. This runtime handles:

**Agent Responsibilities:**

| Function | Description |
|----------|-------------|
| **Context Management** | Decides what information to include in each LLM call |
| **Tool Execution** | Runs tools (file reading, web search, etc.) when needed |
| **Response Generation** | Produces replies using the configured model |
| **Memory** | Maintains working state across a conversation |

**The Workspace:**

Every agent has a **workspace**—a directory on your computer that serves as the agent's "home." This is where:

- Bootstrap files live (`SOUL.md`, `AGENTS.md`, etc.)
- Skills are loaded from
- Session transcripts are stored
- Memory files accumulate

```
~/.openclaw/workspace/
├── SOUL.md          # Who the agent is
├── AGENTS.md        # How it operates
├── USER.md          # Who you are
├── TOOLS.md         # Tool guidance
├── skills/          # Workspace-specific skills
└── memory/          # Daily memory logs
```

When a new session starts, the agent reads these bootstrap files and injects them into its context. This is how your employee "remembers" its persona and operating instructions—even though the underlying LLM has no persistent memory.

## Component 3: Channels (Communication Paths)

**Channels** are how you talk to your AI Employee. Each channel is a separate integration that connects the Gateway to an external messaging platform.

**Available Channels:**

| Channel | Use Case |
|---------|----------|
| **Telegram** | Mobile access, quick messages |
| **Discord** | Community features, voice channels |
| **Slack** | Team collaboration, business context |
| **WhatsApp** | Personal messaging, wide reach |
| **iMessage** | Apple ecosystem integration |
| **Signal** | Privacy-focused messaging |
| **CLI** | Developer access, scripting |
| **Web UI** | Browser-based interaction |

**How Channels Work:**

Each channel has its own configuration—API tokens, access policies, group settings. But the message format is **normalized** by the Gateway. Whether you type on Telegram or Discord, the agent receives the same structured message:

```
Channel → Gateway → Normalized Message → Agent

Example:
Telegram message: "Summarize my project status"
    ↓
Gateway receives: { channel: "telegram", user: "you", text: "..." }
    ↓
Agent processes: (channel-agnostic handling)
    ↓
Response sent back through same channel
```

**Pairing and Access Control:**

By default, channels require **pairing**—a user must be approved before they can message your employee. This prevents random people from using your API credits. When someone first messages your bot:

1. They receive a pairing code
2. You approve with: `openclaw pairing approve telegram <CODE>`
3. They're now authorized to chat

This is your employee's "access control"—deciding who's allowed to talk to it.

**Beyond Telegram:**

This chapter uses Telegram because it's the fastest to set up. But OpenClaw supports multiple channels:

| Channel | Setup Time | Best For |
|---------|-----------|----------|
| **Telegram** | 5 minutes | Personal use, quick setup |
| **WhatsApp** | 15 minutes | Business communication |
| **Discord** | 10 minutes | Team/community use |
| **Signal** | 10 minutes | Privacy-focused |
| **iMessage** | Mac only | Apple ecosystem |

You can connect multiple channels to the same AI Employee. A message from WhatsApp and a message from Telegram both reach the same agent with the same skills and memory.

## Component 4: Skills (Portable Expertise)

**Skills** are the most important concept for your future work. A skill is a **portable package of expertise** that teaches your agent how to do something well.

**What Makes Skills Special:**

Skills are just markdown files with instructions. No special SDK. No platform lock-in. The same skill that works in OpenClaw works in Claude Code, Claude Cowork, and any MCP-compatible platform.

**Skill Format:**

```markdown
---
name: email-drafter
description: Draft professional emails with appropriate tone
metadata: { "openclaw": { "always": true } }
---

# Email Drafter Skill

You are an expert email writer. When asked to draft an email:

1. Ask for: recipient, purpose, key points, tone
2. Draft the email with proper formatting
3. Offer variations if requested

## Output Format
- Subject line
- Greeting
- Body paragraphs
- Call to action
- Professional closing
```

**Three-Tier Loading:**

Skills load from three locations, with workspace skills taking highest priority:

| Priority | Location | Use Case |
|----------|----------|----------|
| **1 (Highest)** | `<workspace>/skills/` | Your custom skills |
| **2** | `~/.openclaw/skills/` | Managed/installed skills |
| **3 (Lowest)** | Bundled | Skills shipped with OpenClaw |

This means you can override any bundled skill by creating one with the same name in your workspace.

**Why Portability Matters:**

When you build a skill for your Branding Expert employee, that same skill works if you:
- Switch to Claude Code for development
- Use Claude Cowork for team collaboration
- Deploy to a different agent platform

Skills encode YOUR expertise in a portable format. You're not building an OpenClaw-specific solution—you're building reusable intelligence.

## Component 5: Model Providers (The Intelligence Source)

**Model Providers** are where the actual reasoning happens. Your agent calls an LLM (Large Language Model) to think through problems and generate responses.

**Supported Providers:**

| Provider | Models | Use Case |
|----------|--------|----------|
| **Moonshot** | Kimi K2.5, K2-thinking | Free tier, great quality |
| **Google** | Gemini Flash, Pro | Easy OAuth setup |
| **Anthropic** | Claude Sonnet, Opus | Best reasoning (paid) |
| **OpenAI** | GPT-4o, o1 | Industry standard (paid) |
| **Ollama** | Local models | Privacy, fully local |

**Model Swapping:**

The key insight: your agent's capabilities are **independent of the model**. You can start with free Kimi K2.5 today, switch to Claude tomorrow, and your skills, bootstrap files, and channel configurations all remain the same.

```json
// Change ONE line to switch models
{
  "agents": {
    "defaults": {
      "model": { "primary": "moonshot/kimi-k2.5" }
      // Change to: "anthropic/claude-sonnet-4"
    }
  }
}
```

**Why This Design Matters:**

Model providers will change. New models will emerge. Pricing will shift. By decoupling your agent's expertise (skills, bootstrap files) from the model, you can adapt without rebuilding.

## Putting It Together: Message Flow

Let's trace what happens when you send a message on Telegram:

```
1. YOU → Telegram
   You type: "Summarize the competitive landscape for AI assistants"

2. Telegram → Gateway
   Telegram sends the message to your bot token
   Gateway receives it on the telegram channel

3. Gateway → Session
   Gateway looks up your session (or creates one)
   Loads conversation history from JSONL transcript

4. Gateway → Agent
   Sends normalized message to agent runtime
   Includes: your message + session context

5. Agent → Bootstrap
   Agent loads SOUL.md, AGENTS.md, skills
   Builds full context for this request

6. Agent → Model Provider
   Sends context + message to Kimi K2.5
   Model reasons and generates response

7. Model → Agent
   Model returns: "Based on current trends..."
   Agent formats response

8. Agent → Gateway
   Response sent back through gateway

9. Gateway → Telegram
   Gateway routes response to telegram channel
   Formatted for Telegram's message limits

10. Telegram → YOU
    Response appears on your phone
```

**Time Elapsed:** 2-5 seconds typically

When something goes wrong, you can now diagnose which component failed:
- No response at all? Check Gateway status (`openclaw status`)
- Wrong persona? Check SOUL.md bootstrap file
- Slow responses? Check Model Provider connection
- Can't receive messages? Check Channel configuration

## MCP: The Universal Connector

One more concept will become essential as you extend your employee: **MCP (Model Context Protocol)**.

MCP is how agents connect to external services—Gmail, GitHub, databases, browsers. Instead of writing custom integrations, you configure **MCP Servers** that expose tools to your agent.

```
┌──────────────────────────────────────────────────────────────┐
│                       YOUR AGENT                              │
│                                                               │
│  "Read my emails"  "Create a GitHub issue"  "Browse the web" │
│         │                    │                    │          │
└─────────┼────────────────────┼────────────────────┼──────────┘
          │                    │                    │
          ▼                    ▼                    ▼
   ┌────────────┐      ┌────────────┐       ┌────────────┐
   │ Gmail MCP  │      │ GitHub MCP │       │ Browser MCP│
   │  Server    │      │  Server    │       │  Server    │
   └────────────┘      └────────────┘       └────────────┘
```

**Why MCP Matters:**

Without MCP, every agent platform builds its own Gmail integration, its own GitHub integration, its own browser control. With MCP, one Gmail Server works with OpenClaw, Claude Code, ChatGPT, Cursor—any MCP-compatible host.

You'll set up Gmail MCP in a later lesson. For now, understand that MCP is how your employee gains "senses"—the ability to see emails, access files, browse the web.

## Sessions: Memory Across Conversations

**Sessions** are how your employee maintains context within a conversation.

Each session is stored as a **JSONL file** (JSON Lines—one JSON object per line) in:

```
~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl
```

**Session Modes:**

| Mode | How It Works |
|------|--------------|
| **main** | All DMs share one session (continuity across days) |
| **per-peer** | Each person gets their own session |
| **per-channel-peer** | Isolated by both channel and person |

**Session Lifecycle:**

- **Daily reset**: Sessions can reset at a configured time
- **Idle reset**: Sessions reset after period of inactivity
- **Manual reset**: You can say `/new` or `/reset` to start fresh
- **Compaction**: Long sessions get compressed to fit context windows

This is why your employee "remembers" what you discussed earlier—the session transcript is injected into each request.

## Try With AI

Use your AI Employee or Claude Code for these exercises.

### Prompt 1: Explain the Architecture

**Setup**: You're explaining OpenClaw to a colleague who's never used AI agents.

**What you're learning**: Articulating the five-component architecture builds your mental model. When you can explain it clearly, you understand it deeply enough to debug problems.

```
I just set up an AI Employee using OpenClaw. My colleague asked me
how it works. Help me explain using this framework:

- What's the Gateway and why do we need it?
- What's the difference between the Agent and the Model Provider?
- Why are Skills separate from the Agent?
- How do Channels fit into the picture?

Use simple analogies where helpful. They're a developer but new to
agent architectures.
```

### Prompt 2: Trace a Message

**Setup**: Understanding the full message flow.

**What you're learning**: Tracing concrete examples through abstract architecture solidifies understanding. This is the skill you'll use when debugging.

```
Walk me through exactly what happens when I send this message to
my AI Employee on Telegram:

"Summarize the key points from our last meeting"

For each step, tell me:
1. Which component is involved
2. What that component does with the message
3. What gets passed to the next component

Include the response flow back to my phone.
```

### Prompt 3: Skills vs Everything Else

**Setup**: Understanding why skills are the key portable component.

**What you're learning**: Distinguishing what's platform-specific (Gateway, Channels) from what's portable (Skills) helps you invest your learning time wisely.

```
I'm building skills for my AI Employee. Help me understand:

1. What makes a skill "portable" across platforms?
2. If I build an email-drafter skill for OpenClaw, what would I
   need to change to use it in Claude Code?
3. What parts of my OpenClaw setup are NOT portable?

I want to know where to invest my time so my work transfers to
other platforms.
```

**Safety Note**: As you explore your AI Employee's architecture, remember that session transcripts contain your conversation history. The workspace directory (`~/.openclaw/`) may include sensitive information. Apply the same care you would to any configuration directory containing credentials.
