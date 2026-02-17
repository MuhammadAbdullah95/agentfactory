---
sidebar_position: 4
title: "How Your Employee Works"
chapter: 12
lesson: 4
duration_minutes: 30
description: "Open the hood on your AI Employee to discover 7 architectural components and 6 universal patterns, understand why each is essential, and see how they map across every agent framework"
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
    measurable_at_this_level: "Student can map OpenClaw's architectural components to their equivalents in Claude Code, ChatGPT, LangGraph, and other agent frameworks using the Universal Pattern Map"

  - name: "Framework-Agnostic Pattern Synthesis"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can articulate why each of the 6 universal agent patterns is essential and diagnose which missing pattern would cause a specific system failure"

learning_objectives:
  - objective: "Explain the 7 architectural components of an AI Employee system and their interactions"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student can name each component, describe its purpose, and explain how it connects to adjacent components in the architecture"

  - objective: "Trace a message through the complete agent loop from ingestion through response delivery"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Given a user message, student can walk through all 6 phases (ingestion, access control, context assembly, model invocation, tool execution, response delivery) explaining what happens at each stage"

  - objective: "Map OpenClaw's components to their equivalents in Claude Code, ChatGPT, LangGraph, and other frameworks using the Universal Pattern Map"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can identify at least 4 of the 6 universal patterns in a new agent framework they haven't studied, correctly naming what problem each pattern solves"

  - objective: "Explain why each of the 6 universal patterns is essential and what breaks without it"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student can name the specific failure mode that results from removing any one of the 6 patterns from an agent system"

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

| Channel     | Library/Protocol     | Best For               |
| ----------- | -------------------- | ---------------------- |
| Telegram    | grammY (Bot API)     | Quick personal setup   |
| WhatsApp    | Baileys (Web API)    | Business communication |
| Discord     | Carbon (Discord API) | Teams and communities  |
| Slack       | Bolt SDK             | Enterprise workspaces  |
| Signal      | signal-cli           | Privacy-focused        |
| iMessage    | BlueBubbles REST API | Apple ecosystem        |
| Google Chat | HTTP webhook         | Google Workspace       |
| WebChat     | Gateway WebSocket    | Browser access         |

There are more -- IRC, Matrix, LINE, Nostr, Mattermost, Microsoft Teams, Feishu, Twitch -- 36 integrations at last count, with 20+ messaging channels. But the number does not matter. What matters is the design principle.

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

**Phase 3 -- Context Assembly:** This is where the magic happens. The agent builds the full context that the LLM will see. It loads your session transcript (the JSONL history of your conversation), your **workspace bootstrap files**, any eligible skills (name and description injected into the system prompt), and memory files (today's daily log plus yesterday's). All of this gets assembled into a single prompt.

The bootstrap files define your agent's identity and behavior before any conversation begins:

| File             | Purpose                                                                          |
| ---------------- | -------------------------------------------------------------------------------- |
| **AGENTS.md**    | Configures agent behavior, personality traits, and response style                |
| **SOUL.md**      | Defines the agent's core identity, values, and communication principles          |
| **USER.md**      | Stores information about you (the operator) for personalized interactions        |
| **IDENTITY.md**  | Sets the agent's name, role description, and public-facing persona               |
| **MEMORY.md**    | Curated long-term facts and preferences (covered in the Memory section)          |
| **HEARTBEAT.md** | Instructions for periodic autonomous check-ins (see Autonomous Invocation below) |
| **BOOT.md**      | Startup instructions executed at the beginning of every new session              |

These files live in your workspace directory (`~/.openclaw/workspace/`). Together, they give your agent a persistent identity that survives session resets. When you customize SOUL.md, you are not tweaking a setting -- you are defining who your employee is.

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

These six patterns (plus one bonus) appear in every agent framework you will encounter. Four frameworks, one table:

| Pattern                   | OpenClaw         | Claude Code          | ChatGPT             | LangGraph         |
| ------------------------- | ---------------- | -------------------- | ------------------- | ----------------- |
| **Orchestration**         | Gateway daemon   | CLI process          | API orchestrator    | StateGraph        |
| **I/O Adapters**          | Channels (30+)   | Terminal/MCP         | Web UI/API          | Input nodes       |
| **State Isolation**       | Sessions (JSONL) | Conversation context | Thread IDs          | State checkpoints |
| **Capability Packaging**  | SKILL.md files   | SKILL.md files       | Custom GPTs/Actions | Tool nodes        |
| **Externalized Memory**   | MEMORY.md + logs | CLAUDE.md + memory   | Memory feature      | State persistence |
| **Concurrency Control**   | Lane queue       | Serialized ops       | Rate limiting       | Node scheduling   |
| **Autonomous Invocation** | Cron + Heartbeat | Cron + hooks         | Scheduled actions   | Trigger nodes     |

OpenClaw distinguishes two kinds of autonomous invocation. **Cron** runs scheduled tasks at fixed times (daily summaries at 8 AM, weekly reports on Fridays). **Heartbeat** is a continuous pulse -- a periodic agent turn (configurable interval, default every few hours) where the agent checks HEARTBEAT.md for standing instructions and decides whether anything needs attention. Cron is a clock; Heartbeat is a pulse. Both let your employee act without being asked, but Heartbeat enables the kind of ambient awareness that separates a scheduled script from an autonomous colleague.

OpenClaw and Claude Code share the same skill format (SKILL.md). That is not a coincidence. The Markdown-based skill format has emerged as a de facto standard: human-readable, version-controllable, portable across platforms.

### Why These 6 and Not 5 or 10?

Remove any single pattern and the system breaks in a specific, predictable way:

- **No Orchestration**: Messages arrive but nothing routes them. The agent cannot receive work.
- **No I/O Adapters**: The agent works on one channel only. Adding a new channel means rewriting the agent.
- **No State Isolation**: Multi-user deployments are impossible. Every conversation contaminates every other.
- **No Capability Packaging**: Adding new abilities means modifying core code. The agent becomes brittle.
- **No Externalized Memory**: The agent forgets everything between sessions. No learning across days.
- **No Autonomous Invocation**: The agent only responds when spoken to. You have a chatbot, not an employee.

You could add patterns (logging, authentication, rate limiting), but those are operational concerns, not architectural requirements. These 6 are the minimum set that makes something an AI Employee rather than a chatbot.

## Why Patterns Matter More Than Products

OpenClaw might evolve. Its API might change. New competitors will emerge. But the six patterns in that table are stable. They emerge from fundamental constraints:

- **Orchestration** exists because distributed components need coordination.
- **I/O Adapters** exist because the world has many communication channels.
- **State Isolation** exists because multiple users cannot share context safely.
- **Capability Packaging** exists because intelligence must be composable.
- **Externalized Memory** exists because LLMs have finite context windows.
- **Concurrency Control** exists because parallel operations can conflict.

These are not OpenClaw's design decisions. They are engineering necessities. Any sufficiently capable agent system reinvents them. Your job is to recognize them, regardless of what name they carry.

In Lesson 05, you will build a custom skill and explore the security realities of giving AI real autonomy. Then the chapter assessment consolidates everything: the architecture, the patterns, and an honest evaluation of what OpenClaw proved and what remains unsolved across the industry.

## Try With AI

### Prompt 1: Race Condition Designer

**Setup:** Use Claude Code or any AI assistant.

```
OpenClaw uses a lane queue to prevent race conditions. Design 3
specific scenarios where removing the lane queue would cause real
problems:

For each scenario:
1. What messages arrive simultaneously?
2. What shared resource do they compete for?
3. What does the corrupted output look like?
4. How does the lane queue prevent it?

Then design a 4th scenario that the lane queue CANNOT prevent --
a race condition that requires a different solution entirely.
```

**What you're learning:** Concurrency is where most agent projects fail silently. By designing failure scenarios yourself, you build intuition for where race conditions hide. The 4th scenario forces you beyond the textbook answer into genuine architectural thinking -- exactly what you need when building your own agent in Chapter 13.

### Prompt 2: Memory Retrieval Trace

**Setup:** Use Claude Code or any AI assistant.

```
You are an AI Employee with OpenClaw's 3-layer memory system:
- Layer 1: MEMORY.md (curated facts)
- Layer 2: Daily logs (memory/YYYY-MM-DD.md)
- Layer 3: Vector search (SQLite-backed embeddings)

Your user asks: "What did we decide about the API migration 6 weeks ago?"

Trace this query through all 3 layers:
1. What does each layer check?
2. In what order?
3. What happens if Layer 1 has nothing? Layer 2?
4. How does vector search find the answer when the user's words
   don't match the original note's words?

Then: design a scenario where ALL 3 layers fail to find the answer.
What went wrong, and how would you fix the architecture?
```

**What you're learning:** Memory retrieval is where theory meets reality. Tracing a concrete query through each layer builds intuition for how externalized memory actually works -- and where it breaks. The failure scenario forces you to think about memory architecture limitations before you encounter them in Chapter 13.

### Prompt 3: Agent Autopsy

**Setup:** Use Claude Code or any AI assistant.

```
Search GitHub for an AI agent project that was abandoned or failed
(look for repos with many stars but no commits in 6+ months, or
repos with issues describing fundamental problems).

Using the 6 universal patterns as your diagnostic framework, perform
an autopsy:
1. Which patterns did the project implement well?
2. Which patterns were missing or broken?
3. Which missing pattern was the likely cause of death?
4. Could the project have survived if it had implemented that
   one missing pattern? Why or why not?

Share the repo link and your diagnosis.
```

**What you're learning:** The 6 patterns are not just a classification scheme. They are a diagnostic tool. Learning to identify which missing pattern killed a project is the fastest way to internalize why each pattern matters. This forensic skill transfers directly to evaluating any agent framework you encounter.
