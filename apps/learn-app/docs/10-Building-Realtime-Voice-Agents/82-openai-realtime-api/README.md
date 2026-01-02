---
sidebar_position: 1
title: "Chapter 82: OpenAI Realtime API"
---

# Chapter 82: OpenAI Realtime API

You have mastered LiveKit Agents and Pipecat—frameworks that abstract voice AI complexity into high-level APIs. But what happens when you need control beyond what frameworks provide?

The **OpenAI Realtime API** gives you direct access to the `gpt-realtime` model—native speech-to-speech processing without transcription intermediaries. This chapter teaches you when to reach for the raw API and how to use it effectively.

---

## Why Direct API Access?

Frameworks solve 90% of voice agent use cases. But edge cases exist:

| Scenario | Framework Limitation | Direct API Advantage |
|----------|---------------------|---------------------|
| Custom WebRTC negotiation | Frameworks own the connection | You control SDP, ICE, DTLS |
| Specialized turn detection | Fixed VAD implementations | Implement your own logic |
| Hybrid audio processing | Audio goes through framework | Direct access to audio streams |
| Cost optimization | Framework overhead | Minimal processing path |
| Research and experimentation | Black box abstractions | Full protocol visibility |

**The rule**: Use frameworks first. Reach for direct API when frameworks constrain you.

---

## What You Will Learn

### Lesson 1: OpenAI Realtime Fundamentals

Connect directly to OpenAI's realtime model:
- WebRTC DataChannel connection setup
- Audio format requirements (24kHz PCM16)
- Session configuration and voice selection
- Your first voice interaction without frameworks

### Lesson 2: Function Calling in Voice

Implement voice-triggered tools:
- Defining callable functions for voice context
- Filler speech patterns during async execution
- Confirmation flows for destructive actions
- Error handling and recovery

### Lesson 3: Barge-In and Custom Turn Detection

Control conversation dynamics:
- Automatic interruption handling
- Manual turn detection implementation
- Voice + image multimodal inputs
- When to use direct API vs framework

---

## OpenAI Realtime API Overview

The Realtime API went **Generally Available in August 2025**, bringing production-ready native speech-to-speech:

### Model Capabilities

| Model | Capability |
|-------|-----------|
| `gpt-4o-realtime-preview-2025-06-03` | Latest realtime model |
| Native audio input | No transcription step—model "hears" audio |
| Native audio output | No TTS step—model "speaks" directly |
| Function calling | Tools work during voice conversation |
| MCP integration | Model Context Protocol support |
| Image inputs | Voice + vision in same session |

### Performance Characteristics

| Metric | Value |
|--------|-------|
| End-to-end latency | 200-300ms |
| Audio in rate | ~$32/1M tokens (~$0.06/minute) |
| Audio out rate | ~$64/1M tokens (~$0.24/minute) |
| Typical 4-min call | ~$0.45-0.50 |
| Voices available | 10+ (alloy, echo, shimmer, etc.) |

### Protocol Options

| Protocol | Use Case |
|----------|----------|
| **WebRTC** | Browser clients, low latency |
| **WebSocket** | Server-to-server, more control |

---

## Prerequisites

This chapter assumes you have completed:

- **Chapter 80**: LiveKit Agents (you understand voice agent architecture)
- **Chapter 81**: Pipecat (you understand pipeline composition)
- **Chapter 79**: Voice AI Fundamentals (you understand latency, VAD, turn detection)

You should be comfortable with:
- WebRTC concepts (SDP, ICE, DataChannels)
- Async Python programming
- Audio processing basics (sample rates, PCM encoding)

---

## When to Use Direct API

Use the OpenAI Realtime API directly when:

1. **Framework limitations block you**: Need custom WebRTC negotiation or specialized audio processing
2. **Minimal latency is critical**: Every millisecond matters, framework overhead is unacceptable
3. **Research/experimentation**: You need full protocol visibility to understand behavior
4. **Custom turn detection**: Framework VAD does not match your use case
5. **Hybrid systems**: Integrating with existing WebRTC infrastructure

Use frameworks (LiveKit, Pipecat) when:

1. **Standard voice agent needs**: Most production use cases
2. **Multi-provider flexibility**: Want to swap STT/LLM/TTS providers
3. **Operational maturity**: Need built-in monitoring, scaling, deployment patterns
4. **Team velocity**: Framework abstractions accelerate development

---

## Technology Stack

This chapter uses:

| Component | Technology | Purpose |
|-----------|------------|---------|
| Model | `gpt-4o-realtime-preview` | Native speech-to-speech |
| Protocol | WebRTC DataChannel | Low-latency audio transport |
| Audio | 24kHz PCM16 mono | OpenAI required format |
| Client | `openai` Python SDK | API access |

---

## Chapter Structure

| Lesson | Duration | Focus |
|--------|----------|-------|
| 1. Realtime Fundamentals | 35 min | WebRTC connection, first voice interaction |
| 2. Voice Function Calling | 40 min | Tools, filler speech, confirmations |
| 3. Barge-In and Custom Turn | 35 min | Interruption handling, manual detection |

**Total**: ~110 minutes

---

## What You Will Build

By the end of this chapter, you will have:

1. **Direct WebRTC connection** to OpenAI Realtime API
2. **Voice-triggered function calling** with proper UX patterns
3. **Custom turn detection** implementation
4. **Decision framework** for choosing direct API vs frameworks

This is not a skill-building chapter—you already have LiveKit and Pipecat skills. This chapter teaches you when and how to go beneath the abstraction layer.

---

## Looking Ahead

After mastering direct OpenAI access, Chapter 83 covers **Gemini Live API**—Google's approach to multimodal voice with affective dialog and proactive responses. You will have direct API experience with both major providers, enabling informed architectural decisions.
