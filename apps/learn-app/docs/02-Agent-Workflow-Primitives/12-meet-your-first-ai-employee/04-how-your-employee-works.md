---
sidebar_position: 4
title: "How Your Employee Works"
chapter: 12
lesson: 4
duration_minutes: 30
description: "Open the hood on your AI Employee to discover 7 architectural components and 6 universal patterns that appear in every agent framework"
keywords:
  [
    "openclaw architecture",
    "gateway",
    "channels",
    "sessions",
    "agent loop",
    "lane queue",
    "memory system",
    "skills",
    "universal agent patterns",
    "cross-framework",
  ]

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Architecture Comprehension"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can explain the 7 architectural components of an AI Employee system (gateway, channels, sessions, agent loop, lane queue, memory, skills) and how they interact"

  - name: "Cross-Framework Pattern Recognition"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can map OpenClaw's architectural components to their equivalents in Claude Code, CrewAI, and other agent frameworks using the Universal Pattern Map"

learning_objectives:
  - objective: "Explain the 7 architectural components of an AI Employee system and their interactions"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student can name each component, describe its purpose, and explain how it connects to adjacent components in the architecture"

  - objective: "Trace a message through the complete agent loop from ingestion through response delivery"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Given a user message, student can walk through all 6 phases (ingestion, access control, context assembly, model invocation, tool execution, response delivery) explaining what happens at each stage"

  - objective: "Map OpenClaw's components to their equivalents in Claude Code, CrewAI, and other frameworks using the Universal Pattern Map"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can identify at least 4 of the 6 universal patterns in a new agent framework they haven't studied, correctly naming what problem each pattern solves"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (gateway, channels, sessions, agent loop, lane queue, memory system, skills system) at the upper limit of the B1 range (7-10). Students have experiential context from Lessons 02-03, having already used these systems hands-on, which makes the architectural concepts concrete rather than abstract."

differentiation:
  extension_for_advanced: "Research one more agent framework (LangGraph, AutoGen, or Semantic Kernel) and add a column to the Universal Pattern Map. Identify any patterns that don't map cleanly and explain why."
  remedial_for_struggling: "Focus on the Universal Pattern Map table. For each of the 6 patterns, write one sentence explaining what problem it solves and what happens if you skip it."
---

# How Your Employee Works

In Lesson 03, you gave your AI Employee real tasks and watched it deliver results. You saw messages flow from your phone to a response in seconds. But you were driving a car without knowing what's under the hood. Now you open the hood.

Understanding how your employee works matters for three reasons. First, when something breaks, you need to know where to look. Is the gateway down? Did the model provider reject your request? Is a session stuck? Second, when you want to extend capabilities, you need to know which component to modify. Third, and most important: **these same patterns appear in every agent framework.** Claude Code, CrewAI, LangGraph, AutoGen -- they all solve the same problems with the same architectural patterns, just with different names. Master the patterns once here, recognize them everywhere.

## The Gateway -- Your Employee's Brain Stem

Every message your employee sends or receives passes through a single process: the **Gateway**. It is a long-running TypeScript/Node.js daemon that binds a WebSocket server to `127.0.0.1:18789` and stays alive as a background service. When you ran `openclaw onboard --install-daemon` in Lesson 02, you installed this process.

The Gateway is the single coordination point for your entire AI Employee. It performs five jobs:

| Function               | What It Does                                                                                  |
| ---------------------- | --------------------------------------------------------------------------------------------- |
| **Message Routing**    | Receives messages from every connected channel, normalizes them, and routes them to the agent |
| **Session Management** | Tracks every conversation, maintains transcript history, controls session resets              |
| **Authentication**     | Verifies pairing codes, enforces allowlists, decides who can talk to your employee            |
| **Skill Loading**      | Discovers skills from workspace, managed, and bundled directories at session start            |
| **Queue Coordination** | Serializes agent runs to prevent race conditions (more on this below)                         |

One gateway per host. That is the design. It owns all messaging connections -- WhatsApp, Telegram, Discord, everything. Think of it as a switchboard operator. Every call goes through the switchboard. No call bypasses it. This centralization is intentional: it means adding a new channel requires zero changes to your agent's logic.

**The pattern: Orchestration.** Every agent framework has a central coordinator. Claude Code has its CLI process. CrewAI has its Python runtime. The name changes; the pattern does not.

## Channels -- Your Employee's Communication Layer

Each messaging platform your employee connects to is a **channel**. Telegram uses grammY. WhatsApp uses Baileys. Discord uses its Bot API. Each is an adapter that translates platform-specific messages into a common internal format.

Here is what OpenClaw currently supports (partial list):

| Channel     | Library/Protocol         | Best For               |
| ----------- | ------------------------ | ---------------------- |
| Telegram    | grammY (Bot API)         | Quick personal setup   |
| WhatsApp    | Baileys (Web API)        | Business communication |
| Discord     | Discord.js (Bot Gateway) | Teams and communities  |
| Slack       | Bolt SDK                 | Enterprise workspaces  |
| Signal      | signal-cli               | Privacy-focused        |
| iMessage    | BlueBubbles REST API     | Apple ecosystem        |
| Google Chat | HTTP webhook             | Google Workspace       |
| WebChat     | Gateway WebSocket        | Browser access         |

There are more -- IRC, Matrix, LINE, Nostr, Mattermost, Microsoft Teams -- over 30 total. But the number does not matter. What matters is the design principle.

When a message arrives from Telegram, the adapter strips away Telegram-specific formatting, extracts the text, user identity, and conversation context, then passes a normalized message to the Gateway. When a response comes back, the adapter translates it into Telegram's format -- respecting message length limits, markdown rendering, and media handling. The agent never knows which channel the message came from. It processes a clean, channel-agnostic payload.

Adding a new channel means writing one adapter. No agent logic changes. No skill modifications. No model configuration updates.

**The pattern: I/O Adapters.** Claude Code adapts to terminal and IDE interfaces. CrewAI adapts to API endpoints. Every framework normalizes communication from diverse sources into a common format. The adapter pattern decouples intelligence from communication.

## Sessions -- Your Employee's Context Windows

Every conversation with your AI Employee gets an isolated **session**. Sessions prevent cross-contamination -- what you discuss in a private DM never leaks into a group chat, and what one user asks never bleeds into another user's conversation.

Sessions are identified by keys that encode their origin:

| Session Type         | Key Pattern                            | Example                                             |
| -------------------- | -------------------------------------- | --------------------------------------------------- |
| **Main (default)**   | `agent:<id>:main`                      | All your DMs share one continuous session           |
| **Per-channel-peer** | `agent:<id>:<channel>:dm:<peerId>`     | Each person on each platform gets their own session |
| **Group**            | `agent:<id>:<channel>:group:<groupId>` | Each group chat is isolated                         |

Each session persists as an **append-only JSONL file** (one JSON object per line) at:

```
~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl
```

Every message you send, every response the agent generates, every tool call and its result -- all appended to this file. The JSONL format means the file is always consistent (no partial writes corrupt earlier entries) and you can read raw transcripts with any text editor.

When sessions grow long, **auto-compaction** kicks in. The system summarizes older conversation history into a compact summary, keeps recent messages intact, and persists the compaction in the JSONL file. This means your employee can have day-long conversations without exceeding the model's context window.

Sessions also reset on a schedule. By default, daily at 4:00 AM local time. You can also reset manually with `/new` or `/reset`, or configure idle timeouts. The reset policy is configurable per session type -- your private DMs might persist for days while group chats reset after two hours of inactivity.

**The pattern: State Isolation.** Claude Code maintains a conversation context per session. CrewAI tracks task state. LangGraph manages graph state. Every framework must isolate state between concurrent users and conversations. Skip this pattern and private data leaks between users.

## The Agent Loop -- Your Employee's Thinking Process

When a message reaches the Gateway and gets routed to the agent, the **agent loop** takes over. This is the core cycle that transforms a message into a response. Every time your employee processes a request, it executes six phases:

```
Message In
    |
    v
[1. Ingestion] --> Channel adapter receives message, normalizes format
    |
    v
[2. Access Control] --> Check pairing, allowlists, permissions
    |
    v
[3. Context Assembly] --> Load session history + memory + skills + system prompt
    |
    v
[4. Model Invocation] --> Send assembled context to LLM (Kimi, Claude, Gemini, local)
    |
    v
[5. Tool Execution] --> Agent calls tools (bash, browser, file operations, MCP servers)
    |                    May loop back to step 4 if model requests more tools
    v
[6. Response Delivery] --> Format result, route back through Gateway and channel
    |
    v
Message Out
```

Let's trace a concrete example. You message your employee on Telegram: "Summarize the key trends in AI agents for 2026."

**Phase 1 -- Ingestion:** The Telegram adapter (grammY) receives the message from Telegram's servers. It extracts your text, user ID, and chat ID, normalizes them into OpenClaw's internal message format, and hands it to the Gateway.

**Phase 2 -- Access Control:** The Gateway checks your pairing status. Are you an approved user? Is this channel configured? If you haven't paired yet, you get a pairing code instead of a response. If approved, the message proceeds.

**Phase 3 -- Context Assembly:** This is where the magic happens. The agent builds the full context that the LLM will see. It loads your session transcript (the JSONL history of your conversation), your bootstrap files (SOUL.md, AGENTS.md, USER.md), any eligible skills (name and description injected into the system prompt), and memory files (today's daily log plus yesterday's). All of this gets assembled into a single prompt.

**Phase 4 -- Model Invocation:** The assembled context goes to your configured LLM. If you are using Kimi K2.5 (free tier), the request goes to Moonshot's API. If Claude, to Anthropic. The model reasons about your question and generates a response -- potentially requesting tool calls.

**Phase 5 -- Tool Execution:** If the model decides it needs tools (searching the web, reading files, executing code), the agent executes those tool calls and feeds the results back. The model may then request more tools, creating an iterative loop. For your summary question, the model might use a web search tool to find recent AI agent news, then synthesize the results.

**Phase 6 -- Response Delivery:** The final response flows back through the Gateway, which routes it to the Telegram adapter, which formats it for Telegram's message limits and sends it to your phone.

Total elapsed time: typically 2-8 seconds depending on model speed and whether tools are involved.

**The pattern: Autonomous Execution Loop.** This intake-reason-act-respond cycle is the heartbeat of every agent. Claude Code runs the same loop (read context, invoke model, execute tools, return results). CrewAI agents iterate through tasks the same way. The loop is the pattern; the implementation details vary.

## The Lane Queue -- Why Your Employee Doesn't Trip Over Itself

What happens when two messages arrive at the same time? If both try to run the agent loop simultaneously on the same session, they could corrupt the transcript, produce garbled responses, or race for tool access.

OpenClaw solves this with a **lane-aware FIFO queue**. Every agent run gets serialized through lanes:

| Lane            | Default Concurrency | Purpose                                              |
| --------------- | ------------------- | ---------------------------------------------------- |
| **Per-session** | 1                   | Only one agent run touches a given session at a time |
| **Main**        | 4                   | Overall parallelism cap for inbound messages         |
| **Subagent**    | 8                   | Background agent tasks can run in parallel           |

Here is how it works in practice:

1. Your Telegram message arrives and gets placed in the queue for your session lane.
2. If no other run is active for your session, it starts immediately.
3. If a previous run is still active, your message waits until it finishes.
4. Messages from different sessions can run in parallel (up to the main lane cap of 4).

The queue supports multiple modes for handling bursts of messages:

- **Collect (default):** Coalesce all queued messages into a single followup turn. If you send three messages while the agent is thinking, it processes all three together.
- **Steer:** Inject the new message into the current run (cancels pending tool calls at the next boundary).
- **Followup:** Queue for the next agent turn after the current run ends.

Typing indicators fire immediately when your message enters the queue, so you see the "thinking..." indicator on Telegram even while waiting for the queue to drain.

**The pattern: Concurrency Control.** Every agent system needs this. Claude Code serializes operations within a conversation. CrewAI coordinates task execution across agents. LangGraph manages node execution order. Skip concurrency control and two tasks writing to the same file will corrupt it. Most hobbyist agent projects get this wrong.

## Memory -- Your Employee's Long-Term Brain

Your employee's LLM has no persistent memory. Every model invocation starts from scratch -- the model only "knows" what is in the current prompt. Memory is how your employee overcomes this limitation.

OpenClaw implements memory in two layers:

**Layer 1: Curated Long-Term Memory (`MEMORY.md`)**

A single Markdown file in the workspace that stores durable facts, preferences, and decisions. The agent reads this file at session start, but only in private sessions (never in group chats, to prevent leaking personal information).

```markdown
# MEMORY.md (example)

## Preferences

- Prefers bullet-point summaries over paragraphs
- Working on Project Atlas (Q1 deadline)
- Timezone: EST

## Key Facts

- Company uses Next.js + Supabase stack
- Budget approved for GPT-4o tier in March
```

**Layer 2: Daily Activity Logs (`memory/YYYY-MM-DD.md`)**

Append-only daily files that capture running context. The agent reads today's and yesterday's logs at each session start. These logs capture what happened during the day without cluttering the curated memory.

```
~/.openclaw/workspace/
├── MEMORY.md                  # Curated long-term (loaded in private sessions)
└── memory/
    ├── 2026-02-14.md          # Yesterday's log
    └── 2026-02-15.md          # Today's log (append-only)
```

**Layer 3: Vector Search**

On top of the Markdown files, OpenClaw builds a vector index using SQLite-backed embeddings. This enables **hybrid search** -- combining vector similarity (semantic matches, even when wording differs) with BM25 keyword relevance (exact matches for IDs, code symbols, and specific terms). The index auto-updates when memory files change.

When the agent needs to recall something from weeks ago, it does not scroll through every daily log. It searches semantically: "What was the decision about the API migration?" returns relevant snippets even if the original note used different words.

Before auto-compaction, OpenClaw runs a **silent memory flush** -- a hidden agent turn that reminds the model to write anything important to disk before the session context gets summarized. This prevents information loss during long conversations.

**The pattern: Externalized Memory.** The LLM's context window is a cache. Disk is the source of truth. Claude Code uses MEMORY.md and auto-compact. CrewAI uses shared context objects. LangGraph uses checkpoint state. Every framework must solve the same problem: models forget everything between calls. The solution is always some form of externalized, persistent storage that gets selectively loaded into context.

## Skills -- Your Employee's Teachable Abilities

Skills are the portable unit of expertise. Each skill is a directory containing a `SKILL.md` file with YAML frontmatter and Markdown instructions:

```
skills/
└── research-assistant/
    └── SKILL.md
```

The frontmatter defines the skill's identity:

```markdown
---
name: research-assistant
description: Research any topic and produce structured notes with sources
---

# Research Assistant

When asked to research a topic:

1. Clarify scope and depth
2. Search for authoritative sources
3. Organize findings into structured notes
   ...
```

Skills load from three locations with clear precedence:

| Priority    | Location              | Use Case                                |
| ----------- | --------------------- | --------------------------------------- |
| **Highest** | `<workspace>/skills/` | Your custom skills for this agent       |
| **Middle**  | `~/.openclaw/skills/` | Managed skills shared across agents     |
| **Lowest**  | Bundled with OpenClaw | Default skills shipped with the install |

A workspace skill with the same name as a bundled skill overrides it. This lets you customize any default behavior without forking the codebase.

**Progressive disclosure** keeps token costs down. At session start, OpenClaw only injects each skill's name and description into the system prompt -- a compact XML list. The full SKILL.md content only gets loaded when the model actually invokes the skill. With 20 skills loaded, the overhead is roughly 20 x ~24 tokens = ~480 tokens for the skill list. The full instructions might be 2,000 tokens per skill, but that cost is only paid when the skill activates.

Skills are portable because they are plain Markdown with a standard YAML frontmatter contract. The same skill that works in OpenClaw works in Claude Code (which uses the same `SKILL.md` format in `.claude/skills/`). ClawHub (`clawhub.com`) serves as a public registry where you can discover, install, and share skills.

**The pattern: Capability Packaging.** Claude Code has `SKILL.md` in `.claude/skills/`. CrewAI has Tasks and Tools. LangGraph has tool nodes. Every framework needs a way to package, discover, and compose discrete capabilities. The format differs; the need is universal.

## The Universal Pattern Map

This table is the centerpiece of the lesson. These six patterns appear in every agent framework you will encounter:

| Universal Pattern        | OpenClaw                                              | Claude Code                        | CrewAI                 | What It Solves                                        |
| ------------------------ | ----------------------------------------------------- | ---------------------------------- | ---------------------- | ----------------------------------------------------- |
| **Orchestration**        | Gateway daemon (TypeScript, port 18789)               | CLI process                        | Python runtime         | Coordinates all components; single point of control   |
| **I/O Adapters**         | Channel adapters (Telegram/WhatsApp/Discord/30+)      | Terminal + IDE integration         | API endpoints          | Normalizes diverse communication into common format   |
| **State Isolation**      | Sessions (JSONL per conversation, per-peer/per-group) | Conversation context (per session) | Task state (per agent) | Prevents data leakage between users and conversations |
| **Capability Packaging** | SKILL.md (workspace > managed > bundled)              | SKILL.md (.claude/skills/)         | Tools + Tasks          | Makes abilities teachable, composable, and portable   |
| **Externalized Memory**  | MEMORY.md + daily logs + vector search                | MEMORY.md + auto-compact           | Shared context objects | Persists knowledge beyond the context window          |
| **Concurrency Control**  | Lane queue (per-session serial, main=4, subagent=8)   | Serialized operations              | Task coordination      | Prevents race conditions and resource conflicts       |

**Autonomous Invocation** deserves a special mention. OpenClaw supports cron jobs and heartbeats -- your employee can check your inbox every 30 minutes, send a daily report at 9 AM, or monitor a project without being asked. Claude Code does not have this (it requires manual invocation). CrewAI supports scheduled tasks. This pattern -- acting without being prompted -- is what separates an AI Employee from an AI tool.

| Bonus Pattern             | OpenClaw                                       | Claude Code        | CrewAI          |
| ------------------------- | ---------------------------------------------- | ------------------ | --------------- |
| **Autonomous Invocation** | Cron jobs + Heartbeat (configurable intervals) | None (manual only) | Scheduled tasks |

When you encounter a new agent framework -- and you will, because new ones emerge constantly -- look for these patterns. They will be there, just wearing different names.

## Why Patterns Matter More Than Products

OpenClaw might evolve. Its API might change. New competitors will emerge. But the six patterns in that table are stable. They emerge from fundamental constraints:

- **Orchestration** exists because distributed components need coordination.
- **I/O Adapters** exist because the world has many communication channels.
- **State Isolation** exists because multiple users cannot share context safely.
- **Capability Packaging** exists because intelligence must be composable.
- **Externalized Memory** exists because LLMs have finite context windows.
- **Concurrency Control** exists because parallel operations can conflict.

These are not OpenClaw's design decisions. They are engineering necessities. Any sufficiently capable agent system reinvents them. Your job is to recognize them, regardless of what name they carry.

In Lesson 05, you will build a custom skill and explore security. In Lesson 06, you will synthesize these patterns into a framework you carry into Chapter 13, where you build your own AI Employee from scratch using Claude Code. Every pattern you learned here will reappear -- and you will already know what each one does.

## Try With AI

### Prompt 1: Architecture Explorer

**Setup:** Use your AI Employee on Telegram or Claude Code.

```
Explain OpenClaw's architecture as if I'm designing a similar system
from scratch. What are the essential components I'd need to build?
Draw me an ASCII diagram showing how they connect.

Then tell me: if I had to cut corners and ship with only 4 of the 7
components, which 3 could I defer and why? What breaks without them?
```

**What you're learning:** Architectural thinking -- distinguishing essential complexity (what you must build) from accidental complexity (what you can defer). This is the skill that separates engineers who ship from engineers who over-design.

### Prompt 2: Cross-Framework Detective

**Setup:** Use Claude Code or any AI assistant.

```
Compare the memory systems of three approaches:
1. OpenClaw: MEMORY.md (curated) + daily logs (append-only) + vector search
2. Claude Code: MEMORY.md + auto-compact conversation history
3. A traditional database-backed agent using PostgreSQL for all state

For each approach, analyze:
- What happens when the agent needs a fact from 3 weeks ago?
- What happens when two users ask about the same topic simultaneously?
- What's the operational cost of running each for 6 months?

Then recommend: which approach would YOU choose for a 10-person team's
internal AI assistant, and why?
```

**What you're learning:** There is no single correct memory architecture. Each approach makes different tradeoffs between simplicity, searchability, cost, and operational complexity. Evaluating tradeoffs is the core engineering skill for Chapter 13.

### Prompt 3: Minimal Design Challenge

**Setup:** Use Claude Code or any AI assistant.

```
If I wanted to build the simplest possible AI Employee from scratch
— just the core that makes it work — what are the 5 must-have
components? For each one, give me:

1. What it does in one sentence
2. The simplest possible implementation (e.g., "a JSON file" or
   "a while loop")
3. What breaks if I skip it entirely

Then tell me: what can I safely SKIP for a first prototype? What
only matters at scale?
```

**What you're learning:** Separating essential complexity from accidental complexity — the key architectural skill for Chapter 13. Building a minimal viable AI Employee first, then adding sophistication, is far more effective than trying to implement all 7 components at production quality from day one.
