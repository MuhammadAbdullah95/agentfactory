---
sidebar_position: 1
title: "Chapter 80: LiveKit Agents"
---

# Chapter 80: LiveKit Agents

Master the framework powering ChatGPT's Advanced Voice Mode. Build production voice agents with semantic turn detection, MCP integration, and multi-agent handoffs.

---

## What You'll Learn

By the end of this chapter, you'll have:

- **A working skill**: The `livekit-agents` skill you create becomes a reusable Digital FTE component
- **Architecture mastery**: Agents, AgentSessions, Workers - the distributed system behind voice AI
- **Turn detection expertise**: Semantic detection that knows when users finish speaking (not just when they pause)
- **MCP integration**: Connect your existing tools to voice with one line of code
- **Multi-agent patterns**: Triage to specialist handoffs with context preservation
- **Production deployment**: Kubernetes manifests, session persistence, horizontal scaling

---

## Skill-First Learning

This chapter uses the **L00 Skill-First** pattern:

1. **Lesson 0**: Build your `livekit-agents` skill from official documentation
2. **Lessons 1-3**: Learn the framework by testing and improving your skill
3. **End result**: A production-ready skill grounded in authoritative sources

**Why skill-first?** Traditional learning produces knowledge. Skill-First produces **assets**. Your `livekit-agents` skill becomes a sellable Digital FTE component.

---

## Lesson Progression

| Lesson | Title | Duration | What You'll Build |
|--------|-------|----------|-------------------|
| 0 | Build Your LiveKit Agents Skill | 30 min | LEARNING-SPEC.md, `livekit-agents` skill |
| 1 | LiveKit Architecture Deep Dive | 35 min | Voice agent with proper STT/LLM/TTS pipeline |
| 2 | Semantic Turn Detection & MCP | 38 min | Natural conversation flow, MCP tool integration |
| 3 | Multi-Agent Handoff & Production | 45 min | Triage to specialist handoffs, K8s deployment |

**Total**: ~148 minutes of hands-on skill building

---

## Why LiveKit Agents?

LiveKit is the framework OpenAI chose to power ChatGPT's Advanced Voice Mode. When you need:

- **Enterprise reliability**: SLAs, support contracts, battle-tested at scale
- **Semantic turn detection**: Transformer models that understand sentence completion
- **Native MCP support**: One-line integration for existing tools
- **Phone integration**: Native SIP support for telephony
- **Kubernetes-native**: Built-in patterns for container orchestration

LiveKit is the answer.

---

## Prerequisites

This chapter builds on:

- **Part 6 (AI Native)**: Agent APIs you'll add voice to
- **Part 7 (Cloud Native)**: Kubernetes deployment patterns
- **Part 9 (TypeScript)**: Async patterns, WebSocket communication
- **Part 10 (Frontends)**: Chat UIs you'll extend with voice
- **Chapter 79 (Voice AI Fundamentals)**: Architecture mental models

Complete Chapter 79 before starting this chapter.

---

## Architecture Overview

```
                    ┌─────────────────────────────────────────┐
                    │           LiveKit Cloud / Server        │
                    └─────────────────────────────────────────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    │                   │                   │
            ┌───────▼───────┐   ┌───────▼───────┐   ┌───────▼───────┐
            │    Worker 1   │   │    Worker 2   │   │    Worker N   │
            │  (Pod in K8s) │   │  (Pod in K8s) │   │  (Pod in K8s) │
            └───────┬───────┘   └───────────────┘   └───────────────┘
                    │
            ┌───────▼───────┐
            │     Agent     │ ◄── Your application logic
            └───────┬───────┘
                    │
            ┌───────▼───────┐
            │ AgentSession  │ ◄── Individual conversation state
            └───────┬───────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
   ┌────▼────┐ ┌────▼────┐ ┌────▼────┐
   │   STT   │ │   LLM   │ │   TTS   │
   │Deepgram │ │ GPT-4o  │ │Cartesia │
   └─────────┘ └─────────┘ └─────────┘
```

---

## The Skill You'll Build

By lesson 3, your `livekit-agents` skill will:

```markdown
## What This Skill Does

- Scaffolds LiveKit voice agents with proper architecture
- Guides STT/LLM/TTS provider selection
- Implements semantic turn detection configuration
- Connects MCP servers for tool integration
- Generates multi-agent handoff patterns
- Provides Kubernetes deployment templates

## When to Use

- Building production voice agents
- Adding voice to existing AI systems
- Integrating voice with MCP tools
- Deploying voice agents at scale
```

---

## What's Next

After mastering LiveKit:

| Chapter | What You'll Learn |
|---------|-------------------|
| 63: Pipecat | Alternative framework with 40+ integrations |
| 64: OpenAI Realtime API | Direct native speech-to-speech |
| 65: Gemini Live API | Multimodal voice + vision |
| 66: Phone & Browser | Real communication channels |
| 67: Capstone | Production voice-enabled Task Manager |

---

## Key Technologies

| Technology | Role | Why We Use It |
|------------|------|---------------|
| LiveKit Agents | Framework | Powers ChatGPT Voice, 8,200+ stars |
| Semantic Turn Detection | Endpointing | 40-60% fewer unwanted interruptions |
| MCP Integration | Tools | One-line connection to existing tools |
| WebRTC | Transport | Low-latency realtime audio |
| Kubernetes | Deployment | Horizontal scaling, session persistence |

---

## Success Metrics

You succeed when you can:

- Create a `livekit-agents` skill from official documentation
- Explain Agents, AgentSessions, Workers architecture
- Configure semantic turn detection for natural conversation
- Connect MCP servers to voice agents
- Implement multi-agent handoffs with context preservation
- Deploy voice agents to Kubernetes

---

Ready to build voice agents with the framework powering ChatGPT? Start with Lesson 0.
