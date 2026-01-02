---
sidebar_position: 11
title: "Part 11: Building Realtime Voice Agents"
---

# Part 11: Building Realtime Voice Agents

You've built chat interfaces in Part 10—rendering streaming responses, visualizing tool calls, and deploying frontends. Now you'll add **realtime voice capabilities**—the technologies that make AI interactions feel natural, immediate, and conversational.

Voice is the natural interface for Digital FTEs. This part teaches you to build voice-enabled AI agents that can hear, speak, and see.

---

## Why Voice AI Matters

Text chat is powerful, but voice is natural. Humans evolved to speak, not type:

- **24/7 Availability**: Voice agents answer phones at 3 AM
- **Hands-Free Interaction**: Users engage while driving, cooking, working
- **Emotional Connection**: Voice conveys tone, empathy, urgency
- **Accessibility**: Voice interfaces serve users who can't type

**The market reality**: The voice AI market is projected to grow from $5.4B (2024) to $47.5B by 2034. LiveKit Agents powers ChatGPT's Advanced Voice Mode. Pipecat integrates 40+ AI services. The infrastructure for voice Digital FTEs is production-ready.

---

## Framework-First Approach

Traditional voice AI teaching focuses on raw APIs and the "three-model pipeline" (STT → LLM → TTS). This is the **old way**.

Modern production voice agents use **frameworks** that abstract complexity:

| Framework | Stars | Differentiator |
|-----------|-------|----------------|
| **LiveKit Agents** | 8,200+ | Powers ChatGPT Voice, native SIP, semantic turn detection |
| **Pipecat** | 8,900+ | 40+ integrations, frame-based pipeline, vendor neutral |

**Our approach**: Master the frameworks first, then understand direct APIs for edge cases.

---

## What You'll Learn

### Production Frameworks (Chapters 80-81)

You'll master the two dominant voice AI frameworks:

**LiveKit Agents** — The enterprise standard
- Agents, AgentSessions, Workers architecture
- Semantic turn detection with transformer models
- Native MCP (Model Context Protocol) support
- Multi-agent handoff with context preservation
- Kubernetes deployment patterns

**Pipecat** — Maximum flexibility
- Frame-based pipeline architecture
- 40+ AI service integrations as plugins
- Transport-agnostic (Daily WebRTC, WebSocket, local)
- OpenAI Realtime, Gemini Live, AWS Nova Sonic support

### Direct API Access (Chapters 82-83)

When you need raw control beyond frameworks:

**OpenAI Realtime API**
- Native speech-to-speech with gpt-realtime model
- WebRTC connections, function calling, barge-in
- 200-300ms end-to-end latency
- ~$0.45-0.50 per 4-minute call

**Gemini Live API**
- Multimodal voice + vision + text unified streams
- Affective dialog (adapts tone to user emotion)
- Proactive audio (model decides when to respond)
- 30 HD voices in 24 languages

### Integration & Production (Chapters 84-85)

Building complete voice systems:

- **Phone Integration**: SIP, Twilio, Telnyx via frameworks
- **Browser Audio**: Web Audio API, Silero VAD, WebRTC
- **Production Deployment**: Kubernetes, monitoring, cost optimization

---

## Prerequisites

This part builds on:

- **Part 6 (AI Native)**: Agent APIs you'll add voice to
- **Part 7 (Cloud Native)**: Deployment infrastructure
- **Part 9 (TypeScript)**: Async patterns, WebSocket communication
- **Part 10 (Frontends)**: Chat UIs you'll extend with voice

You need **Part 10 completed** before starting this part.

---

## Chapter Progression

### Chapter 79: Voice AI Fundamentals
Understand the voice AI landscape: frameworks vs direct APIs, latency budgets, and technology stack. Build mental models before building systems.

### Chapter 80: LiveKit Agents
Master the framework powering ChatGPT's Advanced Voice Mode. Implement Agents, Sessions, Workers, semantic turn detection, and MCP integration. Create the `livekit-agents` skill.

### Chapter 81: Pipecat
Build flexible voice agents with Pipecat's frame-based pipeline. Integrate multiple providers, implement custom processors, and create the `pipecat` skill.

### Chapter 82: OpenAI Realtime API
Access OpenAI's native speech-to-speech model directly. Implement raw WebRTC connections, function calling, and custom turn detection for scenarios beyond framework abstractions.

### Chapter 83: Gemini Live API
Build multimodal voice agents with Google's Gemini 2.5 Flash Native Audio. Combine voice with vision for agents that see and hear. Implement affective dialog and proactive responses.

### Chapter 84: Phone & Browser Integration
Connect voice agents to real communication channels. Implement SIP/Twilio telephony, Web Audio API capture, and Silero VAD. Create `voice-telephony` and `web-audio-capture` skills.

### Chapter 85: Production Voice Agent (Capstone)
Build a complete voice-enabled Task Manager: browser voice interface, phone number integration, multimodal capabilities, Kubernetes deployment, and cost optimization.

---

## Skill-First Learning

Four chapters use the **L00 Skill-First** pattern:

| Chapter | Skill Created |
|---------|---------------|
| 62 | `livekit-agents` |
| 63 | `pipecat` |
| 66 | `voice-telephony`, `web-audio-capture` |

Each skill is built from **official documentation** (not AI memory), tested on real projects, and becomes a **sellable Digital FTE component**.

---

## Running Example

The **Task Manager** continues as the unified example:

| Part | Implementation |
|------|----------------|
| Part 6 Ch40 | Task API (FastAPI + SQLModel) |
| Part 7 | Containerized on Kubernetes |
| Part 10 | Chat UI with streaming |
| **Part 11** | **Voice-enabled Task Manager** |

By the end, your Task Manager will:
- Accept voice commands via browser (WebRTC)
- Handle phone calls for task check-ins
- See your screen to understand context
- Speak responses naturally with interruption support

---

## Technology Stack

### Frameworks
| Technology | Role | Why |
|------------|------|-----|
| LiveKit Agents | Primary framework | Powers ChatGPT Voice, native SIP |
| Pipecat | Alternative framework | 40+ integrations, flexibility |

### Native Speech-to-Speech
| Provider | Latency | Cost |
|----------|---------|------|
| OpenAI Realtime | 200-300ms | ~$0.45/4min |
| Gemini Live | <300ms | Competitive |

### Cascaded Pipeline (via frameworks)
| Component | Provider | Latency | Cost/min |
|-----------|----------|---------|----------|
| STT | Deepgram Nova-3 | ~90ms | $0.0077 |
| LLM | GPT-4o-mini | 200-400ms | $0.0015 |
| TTS | Cartesia Sonic-3 | 40-90ms | ~$0.024 |
| VAD | Silero VAD | <1ms | Free |

**Total economy stack**: ~$0.033/minute

---

## What You'll Build

**Capstone Project**: Production Voice Agent

1. **Browser Voice Interface** — WebRTC via LiveKit
2. **Phone Integration** — Dedicated number via Twilio
3. **Multimodal Support** — Voice + screen sharing via Gemini
4. **Natural Conversation** — Turn-taking, interruption, barge-in
5. **Production Deployment** — Kubernetes, monitoring, cost tracking

This is a **sellable Digital FTE** — a voice assistant that works 24/7.

---

## Success Metrics

You succeed when you can:

- ✅ Build voice agents with LiveKit Agents framework
- ✅ Build voice agents with Pipecat framework
- ✅ Access OpenAI Realtime API directly for custom scenarios
- ✅ Build multimodal agents with Gemini Live API
- ✅ Connect voice agents to phone networks
- ✅ Capture and process browser audio
- ✅ Deploy production voice-enabled Digital FTEs

---

## Looking Ahead

After mastering voice agents, you're ready for **Part 12: Agentic AI Future**—exploring the Agentic Web, Agentic Organizations, and where this technology is heading.

You've built the complete stack: Backend (Parts 5-7), Language (Part 9), Frontend (Part 10), **Voice (Part 11)**. Part 12 shows you the future you're building toward.
