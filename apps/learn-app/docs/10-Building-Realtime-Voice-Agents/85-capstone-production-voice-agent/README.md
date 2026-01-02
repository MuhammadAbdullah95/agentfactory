---
sidebar_position: 1
title: "Chapter 85: Production Voice Agent (Capstone)"
---

# Chapter 85: Production Voice Agent (Capstone)

You have spent Part 11 mastering voice AI from multiple angles: architecture decisions in Chapter 79, LiveKit Agents in Chapter 80, Pipecat pipelines in Chapter 81, OpenAI Realtime in Chapter 82, Gemini Live multimodal in Chapter 83, and phone/browser integration in Chapter 84.

Now you bring it all together.

This capstone is not about learning new frameworks. It is about **composing everything you have built** into a production-grade, multi-channel voice assistant for your Task Manager. You will write specifications first, implement using your accumulated skills, and deploy to Kubernetes with monitoring, cost tracking, and failover strategies.

The result: a 24/7 voice-enabled Digital FTE that answers phone calls, accepts browser commands, sees user screens, and manages tasks through natural conversation.

---

## What Makes This Capstone Special

Unlike previous chapters that taught individual technologies, this capstone tests your ability to **orchestrate** them:

| Previous Chapters | This Capstone |
|-------------------|---------------|
| Learn one framework at a time | Compose multiple frameworks together |
| Create new skills | Use skills you already built |
| Code-first exploration | Specification-first design |
| Development environment | Production deployment |
| Single channel | Multi-channel (browser + phone + screen share) |

This is **Layer 4: Spec-Driven Integration**. You write the specification, AI implements using your accumulated skills, and you validate against your own success criteria.

---

## Skills Composed (Not Created)

This capstone composes skills you built in earlier chapters:

| Skill | Source Chapter | Role in Capstone |
|-------|----------------|------------------|
| `livekit-agents` | Chapter 80 | Core voice agent, WebRTC, browser channel |
| `pipecat` | Chapter 81 | Provider flexibility, custom processors |
| `voice-telephony` | Chapter 84 | Phone/Twilio integration, SIP routing |
| `web-audio-capture` | Chapter 84 | Browser audio capture, Silero VAD |

**Direct API knowledge applied**:
- **OpenAI Realtime API** (Chapter 82): Understanding for Native S2S comparison
- **Gemini Live API** (Chapter 83): Multimodal screen sharing integration

**No new skills are created in this capstone.** You prove mastery by composing what you already have.

---

## What You Will Build

A production-ready **voice-enabled Task Manager** with:

**Multi-Channel Access**:
- Browser: Click a button, speak to your Task Manager via WebRTC
- Phone: Call a dedicated number, manage tasks through natural conversation
- Screen Share: Show your screen and say "add what I'm looking at to my tasks"

**Natural Conversation**:
- Semantic turn detection (knows when you are done speaking)
- Barge-in support (you can interrupt the agent)
- Filler speech during async operations ("Let me check that for you...")
- Confirmation flows for destructive actions

**Production Operations**:
- Kubernetes deployment with session persistence
- Horizontal pod autoscaling for voice workloads
- Voice-specific observability (latency percentiles, cost per call)
- Provider failover (Deepgram fails, Whisper takes over)

---

## Production Targets

Your voice agent must meet these specifications:

| Metric | Target | How You Achieve It |
|--------|--------|-------------------|
| **End-to-end latency** | Sub-800ms (P95) | Economy stack with semantic turn detection |
| **Cost per minute** | $0.03-0.07 | Deepgram + GPT-4o-mini + Cartesia |
| **Availability** | 99.5% | Multi-replica deployment with failover |
| **Channels** | Browser + Phone | LiveKit WebRTC + Twilio SIP |
| **Multimodal** | Voice + Screen Share | Gemini Live API integration |

These are not aspirational goals. They are your **acceptance criteria**. The capstone succeeds when all targets are validated.

---

## Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Voice Agent Core** | LiveKit Agents | Multi-channel orchestration |
| **STT** | Deepgram Nova-3 | Speech recognition ($0.0077/min) |
| **LLM** | GPT-4o-mini | Reasoning and response generation |
| **TTS** | Cartesia Sonic-3 | Voice synthesis ($0.024/min) |
| **VAD** | Silero VAD | Voice activity detection (free) |
| **Browser** | LiveKit WebRTC | Browser audio/video |
| **Phone** | Twilio SIP | Telephony integration |
| **Multimodal** | Gemini Live API | Screen sharing + voice |
| **Deployment** | Kubernetes | Production orchestration |
| **Monitoring** | Prometheus + Grafana | Voice-specific observability |

---

## Chapter Structure

| Lesson | Title | Duration | What You Do |
|--------|-------|----------|-------------|
| 1 | System Architecture and Specification Design | 55 min | Write production spec, design architecture, select providers |
| 2 | Implementation and Integration | 80 min | Build using your skills, integrate all channels |
| 3 | Production Deployment and Operations | 80 min | Deploy to Kubernetes, configure monitoring, document operations |

**Total Duration**: ~215 minutes

---

## Prerequisites

This capstone requires completion of:

- **Chapter 79**: Voice AI Fundamentals (architecture decision matrix)
- **Chapter 80**: LiveKit Agents (browser WebRTC, multi-agent patterns)
- **Chapter 81**: Pipecat (provider flexibility, custom processors)
- **Chapter 82**: OpenAI Realtime API (native S2S understanding)
- **Chapter 83**: Gemini Live API (multimodal voice + vision)
- **Chapter 84**: Phone and Browser Integration (Twilio, Web Audio)
- **Part 7**: Kubernetes deployment patterns (from AI Cloud-Native Development)

You should also have your Task Manager API running (from Part 6/7). The voice agent connects to it via MCP.

---

## Book Thesis Connection

This capstone fulfills Part 11's contribution to the book thesis: **"Manufacture Digital FTEs powered by agents, specs, skills."**

By completing this capstone, you will have:

1. **Skills**: A library of voice-related skills (`livekit-agents`, `pipecat`, `voice-telephony`, `web-audio-capture`) that compose into production systems

2. **Specification**: A documented production specification for multi-channel voice agents that you can adapt to any domain

3. **Digital FTE**: A 24/7 voice assistant that answers phones, accepts browser commands, and sees user screens—a sellable product component

The voice-enabled Task Manager is not a tutorial project. It is a **production-grade Digital FTE component** built on documented specifications and reusable skills. Change the domain knowledge, and you have a voice assistant for any industry.

---

## Looking Ahead

After completing this capstone, you will have built a complete voice-enabled application from architecture through production deployment. Part 11 concludes with you owning a multi-channel voice agent that demonstrates the full spectrum of modern voice AI capabilities.

Your journey through Building Realtime Voice Agents is complete. The skills you have accumulated—and the production patterns you have learned—prepare you to build voice interfaces for any domain.
