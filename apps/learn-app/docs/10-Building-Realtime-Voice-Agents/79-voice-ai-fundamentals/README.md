---
sidebar_position: 1
title: "Chapter 79: Voice AI Fundamentals"
---

# Chapter 79: Voice AI Fundamentals

Build mental models before building systems. This chapter prepares you for voice AI implementation by teaching the landscape, architectures, and technology stack.

---

## What You'll Learn

By the end of this chapter, you'll understand:

- **Why voice matters**: The natural interface for Digital FTEs (24/7 availability, emotional connection, accessibility)
- **Market reality**: $5.4B (2024) to $47.5B (2034) - where the opportunity lies
- **Two architectures**: Native Speech-to-Speech vs Cascaded Pipeline (and when to use which)
- **Latency budgets**: 40ms mic, 90ms STT, 200ms LLM, 75ms TTS - where time goes
- **Technology stack**: STT, TTS, VAD providers and their tradeoffs
- **Framework positioning**: LiveKit Agents vs Pipecat - different tools for different needs

---

## Lesson Progression

| Lesson | Title | Duration | What You'll Learn |
|--------|-------|----------|-------------------|
| 1 | The Voice AI Landscape | 20 min | Market, framework-first thinking, LiveKit vs Pipecat |
| 2 | Voice AI Architectures | 25 min | Native S2S vs Cascaded, latency budgets, decision matrix |
| 3 | The Voice AI Technology Stack | 25 min | STT, TTS, VAD providers, WebRTC vs WebSocket |

**Total**: ~70 minutes of conceptual foundation

---

## Why Concepts First?

Traditional voice AI teaching jumps straight into the "three-model pipeline" (STT, LLM, TTS). That's like teaching web development by explaining HTTP headers before showing a webpage.

**Our approach**: Understand the landscape first. Know why frameworks exist before using them. Grasp architecture tradeoffs before choosing components.

After this chapter, when you see LiveKit's `AgentSession` or Pipecat's `Pipeline`, you'll understand what problems they solve and why they're designed the way they are.

---

## Key Decision Frameworks

### Architecture Selection

| Factor | Native S2S | Cascaded Pipeline |
|--------|-----------|-------------------|
| Latency | 200-300ms | 500-800ms |
| Cost | ~$0.45/4min | ~$0.03/min |
| Flexibility | Fixed model | Mix providers |
| Best For | Premium UX | Cost-sensitive, high volume |

### Framework Selection

| Factor | LiveKit Agents | Pipecat |
|--------|---------------|---------|
| Stars | 8,200+ | 8,900+ |
| Powers | ChatGPT Voice | 40+ integrations |
| Strength | Native SIP, semantic turn | Frame-based, vendor neutral |
| Best For | Enterprise telephony | Multi-provider flexibility |

---

## Prerequisites

This chapter builds on:

- **Part 6 (AI Native)**: Agent APIs you'll add voice to
- **Part 7 (Cloud Native)**: Kubernetes deployment patterns
- **Part 9 (TypeScript)**: Async patterns, WebSocket communication
- **Part 10 (Frontends)**: Chat UIs you'll extend with voice

You should complete Part 10 before starting this chapter.

---

## What's Next

After building these mental models:

| Chapter | What You'll Build |
|---------|-------------------|
| 62: LiveKit Agents | Voice agent with the framework powering ChatGPT |
| 63: Pipecat | Flexible voice agent with frame-based pipeline |
| 64: OpenAI Realtime API | Direct native S2S access |
| 65: Gemini Live API | Multimodal voice + vision agents |
| 66: Phone & Browser Integration | Real communication channels |
| 67: Capstone | Production voice-enabled Task Manager |

---

## The Voice AI Stack at a Glance

```
                    ┌─────────────────────────────────────────┐
                    │        Your Voice Digital FTE           │
                    └─────────────────────────────────────────┘
                                       │
              ┌────────────────────────┴────────────────────────┐
              │                                                  │
    ┌─────────┴─────────┐                           ┌───────────┴───────────┐
    │  Native S2S        │                           │  Cascaded Pipeline    │
    │  (OpenAI Realtime) │                           │  (STT → LLM → TTS)    │
    │  200-300ms         │                           │  500-800ms            │
    │  ~$0.11/min        │                           │  ~$0.03/min           │
    └───────────────────┘                           └───────────────────────┘

              ┌─────────────────────────────────────────────────┐
              │               Voice AI Frameworks               │
              ├─────────────────────┬───────────────────────────┤
              │   LiveKit Agents    │        Pipecat            │
              │   (ChatGPT Voice)   │   (40+ integrations)      │
              └─────────────────────┴───────────────────────────┘

              ┌─────────────────────────────────────────────────┐
              │              Technology Stack                   │
              ├─────────────┬─────────────┬─────────────────────┤
              │     STT     │     TTS     │        VAD          │
              │  Deepgram   │  Cartesia   │    Silero VAD       │
              │  AssemblyAI │  ElevenLabs │    (<1ms)           │
              │  Whisper    │  Deepgram   │                     │
              └─────────────┴─────────────┴─────────────────────┘

              ┌─────────────────────────────────────────────────┐
              │              Transport Layer                    │
              ├─────────────────────┬───────────────────────────┤
              │       WebRTC        │        WebSocket          │
              │  (Production voice) │     (Prototyping)         │
              └─────────────────────┴───────────────────────────┘
```

---

Ready to understand the voice AI landscape? Start with Lesson 1.
