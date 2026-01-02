---
sidebar_position: 0
title: "Chapter 81: Pipecat"
---

# Chapter 81: Pipecat

Build flexible voice agents with Pipecat's frame-based pipeline architecture. With 40+ AI service integrations, transport-agnostic design, and support for native speech-to-speech models, Pipecat gives you maximum flexibility in how you construct voice Digital FTEs.

---

## What You'll Learn

By the end of this chapter, you'll have:

- **A working skill**: The `pipecat` skill you create becomes a reusable Digital FTE component
- **Frame architecture mastery**: Understand how data flows through pipelines as discrete frames
- **Multi-provider integration**: Connect any combination of 40+ STT, LLM, TTS providers
- **S2S model access**: Use OpenAI Realtime, Gemini Live, AWS Nova Sonic through Pipecat
- **Transport flexibility**: Deploy the same pipeline to WebRTC, WebSocket, or local audio
- **Custom processors**: Build domain-specific transformations for your voice agents

---

## Skill-First Learning

This chapter uses the **L00 Skill-First** pattern:

1. **Lesson 0**: Build your `pipecat` skill from official documentation
2. **Lessons 1-2**: Learn the framework by testing and improving your skill
3. **End result**: A production-ready skill grounded in authoritative sources

**Why skill-first?** Traditional learning produces knowledge. Skill-First produces **assets**. Your `pipecat` skill becomes a sellable Digital FTE component.

---

## Lesson Progression

| Lesson | Title | Duration | What You'll Build |
|--------|-------|----------|-------------------|
| 0 | Build Your Pipecat Skill | 30 min | LEARNING-SPEC.md, `pipecat` skill |
| 1 | Frame-Based Pipeline Architecture | 45 min | Voice pipeline with proper frame flow |
| 2 | Multi-Provider Integration & Custom Processors | 45 min | Multi-provider agent, custom processors |

**Total**: ~120 minutes of hands-on skill building

---

## Why Pipecat?

Pipecat takes a different approach than LiveKit. Where LiveKit focuses on distributed architecture (Workers, Sessions, Jobs), Pipecat focuses on **compositional design**:

| Aspect | LiveKit Agents | Pipecat |
|--------|----------------|---------|
| **Architecture** | Distributed (Workers, Sessions) | Compositional (Frames, Processors) |
| **Provider Integration** | Built-in providers | 40+ plugin ecosystem |
| **Transport** | WebRTC-first | Transport-agnostic |
| **S2S Models** | Supported | Full support (Realtime, Gemini Live, Nova) |
| **Best For** | Enterprise scale | Maximum flexibility |

When you need:

- **Provider flexibility**: Easily swap between 40+ STT, LLM, TTS providers
- **Custom processing**: Add domain-specific transformations in the pipeline
- **Transport options**: Deploy to WebRTC, WebSocket, or local audio
- **S2S integration**: Access native voice models through unified interface

Pipecat is the answer.

---

## Prerequisites

This chapter builds on:

- **Part 6 (AI Native)**: Agent APIs you'll add voice to
- **Part 7 (Cloud Native)**: Deployment patterns
- **Part 9 (TypeScript)**: Async patterns, WebSocket communication
- **Part 10 (Frontends)**: Chat UIs you'll extend with voice
- **Chapter 79 (Voice AI Fundamentals)**: Architecture mental models
- **Chapter 80 (LiveKit Agents)**: Comparison context, voice pipeline understanding

Complete Chapter 80 before starting this chapter for maximum learning value.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         Transport                               │
│              (Daily WebRTC / WebSocket / Local)                 │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                         Pipeline                                │
│                                                                 │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐     │
│  │   STT    │──▶│   LLM    │──▶│   TTS    │──▶│ Transport │     │
│  │Processor │   │Processor │   │Processor │   │  Output   │     │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘     │
│                                                                 │
│  AudioRawFrame ─▶ TextFrame ─▶ TextFrame ─▶ AudioRawFrame      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**The Frame Model**: Everything is a frame. Audio frames, text frames, control frames. Processors transform frames. Pipelines compose processors. Transports connect to the outside world.

---

## The Skill You'll Build

By lesson 2, your `pipecat` skill will:

```markdown
## What This Skill Does

- Scaffolds Pipecat voice pipelines with frame-based architecture
- Guides provider selection across 40+ integrations
- Configures S2S models (OpenAI Realtime, Gemini Live, Nova Sonic)
- Implements custom processors for domain transformations
- Supports multiple transports (Daily, WebSocket, local)

## When to Use

- Building voice agents with specific provider requirements
- Need custom processing in the voice pipeline
- Deploying to diverse transport targets
- Integrating native S2S models with framework abstraction
```

---

## What's Next

After mastering Pipecat:

| Chapter | What You'll Learn |
|---------|-------------------|
| 64: OpenAI Realtime API | Direct native speech-to-speech |
| 65: Gemini Live API | Multimodal voice + vision |
| 66: Phone & Browser | Real communication channels |
| 67: Capstone | Production voice-enabled Task Manager |

---

## Key Technologies

| Technology | Role | Why We Use It |
|------------|------|---------------|
| Pipecat | Framework | 8,900+ stars, 40+ integrations |
| Frames | Data Model | Uniform interface for all data types |
| Processors | Transformation | Modular, composable, swappable |
| Daily WebRTC | Transport | Production-ready browser audio |
| Provider Plugins | Integration | Deepgram, Cartesia, OpenAI, etc. |

---

## Pipecat vs LiveKit: When to Use Each

After completing both chapters, you'll understand:

**Use LiveKit When**:
- Building enterprise-scale voice infrastructure
- Need native SIP/phone integration
- Semantic turn detection is critical
- Kubernetes-native deployment required

**Use Pipecat When**:
- Maximum provider flexibility needed
- Custom processing in the pipeline
- Transport-agnostic deployment
- Rapid prototyping with different providers

**Use Both When**:
- Different parts of your system have different requirements
- You want framework comparison for informed decisions
- Building Digital FTEs that may need to switch frameworks

---

## Success Metrics

You succeed when you can:

- Create a `pipecat` skill from official documentation
- Explain frames, processors, and pipelines
- Build voice agents with any provider combination
- Integrate S2S models through Pipecat
- Implement custom processors for domain needs
- Deploy to different transports without code changes

---

Ready to build flexible voice agents with Pipecat? Start with Lesson 0.
