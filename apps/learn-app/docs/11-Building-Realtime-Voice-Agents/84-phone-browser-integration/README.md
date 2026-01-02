---
sidebar_position: 1
title: "Chapter 84: Phone & Browser Integration"
---

# Chapter 84: Phone & Browser Integration

You have built voice agents using LiveKit, Pipecat, OpenAI Realtime API, and Gemini Live API. They run beautifully in development environments. Now the question becomes: **How do real users reach them?**

Your customers are not connecting via WebSocket terminals. They are picking up phones. They are opening web browsers. They expect to dial a number or click a button and start talking to your agent immediately.

This chapter bridges the gap between voice AI frameworks and **real communication channels**. You will connect your agents to the telephone network via SIP and Twilio. You will capture microphone audio in browsers with sub-3ms latency. You will run voice activity detection client-side to reduce round-trips. By chapter's end, your Task Manager voice agent will be reachable from any phone number and any web browser.

---

## What Makes This Chapter Unique

Previous chapters taught you to build voice agents. This chapter teaches you to **deploy them where users actually are**.

| Chapter | Focus | What You Built |
|---------|-------|----------------|
| 62: LiveKit Agents | Framework architecture | Voice agent in LiveKit room |
| 63: Pipecat | Pipeline composition | Modular voice pipeline |
| 64: OpenAI Realtime | Direct API access | Native speech-to-speech agent |
| 65: Gemini Live | Multimodal integration | Voice + vision agent |
| **66: This Chapter** | **Communication channels** | **Phone numbers + browser access** |

The difference is fundamental. Frameworks give you capabilities. Channels give you **customers**.

---

## Production Evidence

Companies generating revenue from phone and browser voice integration:

**Replicant AI**: Enterprise voice AI handling millions of customer service calls. Their platform connects to existing telephony infrastructure via SIP trunks and Twilio integration. Customers include DoorDash, Verizon, and AAA. According to CEO Gadi Shamia, Replicant agents "handle 5 million calls per month with 85% containment rate."

**Air AI**: Conversational AI for phone calls that can "talk for 10-40 minutes straight" according to their website. They provide both inbound and outbound calling capabilities via standard telephony integration. Y Combinator backed, now processing millions of customer interactions.

**Bland AI**: Phone-first AI platform enabling developers to build voice agents for phone calls. Their API handles telephony complexity, providing direct SIP and Twilio integration. Customers use it for appointment scheduling, lead qualification, and customer support.

The pattern is clear: voice agents that connect to real phone numbers generate real revenue.

---

## What You Will Learn

### Lesson 0: Build Your Integration Skills

Before diving into telephony and browser APIs, you create **two production skills**:
- `voice-telephony` skill grounded in Twilio, Telnyx, and LiveKit SIP documentation
- `web-audio-capture` skill grounded in Web Audio API, AudioWorklet, and Silero VAD documentation

This follows the Skill-First pattern: build knowledge artifacts FIRST from official documentation, then learn by improving them.

### Lesson 1: Phone Integration with SIP & Twilio

Connect your voice agents to real phone numbers:
- SIP protocol fundamentals and when to use native SIP vs webhooks
- Twilio Voice for inbound calls (receive calls to your agent)
- Twilio Voice for outbound calls (agent calls users)
- Telnyx as cost-effective alternative (approximately $0.002/min vs $0.0085/min)
- PSTN audio quality considerations (8kHz impacts model performance)

### Lesson 2: Browser Audio Capture & VAD

Capture and process audio in web browsers:
- Web Audio API and getUserMedia for microphone access
- AudioWorklet for low-latency processing (approximately 2.67ms at 48kHz)
- Silero VAD in browser via WebAssembly (less than 1ms per 30ms chunk)
- WebRTC vs WebSocket for browser-to-server audio transport
- Connecting browser audio to LiveKit and Pipecat agents

### Lesson 3: Production Telephony Patterns

Patterns for operating voice agents at scale:
- IVR (Interactive Voice Response) with natural language intent detection
- Call queuing, transfer, and hold patterns
- Call recording with GDPR and consent compliance
- Multi-provider failover (Twilio + Telnyx) for high availability
- Cost optimization through intelligent routing

---

## Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Telephony Provider | Twilio Voice | Inbound/outbound phone calls |
| Cost-Effective Alternative | Telnyx | High-volume telephony at lower cost |
| SIP Integration | LiveKit Native SIP | Direct trunk connection |
| Browser Audio | Web Audio API | Microphone capture |
| Low-Latency Processing | AudioWorklet | Thread-separated audio processing |
| Voice Detection | Silero VAD (WASM) | Client-side speech detection |
| Transport | WebRTC / WebSocket | Browser-to-server audio streaming |
| Framework Integration | LiveKit SDK, Pipecat | Voice agent connection |

---

## Chapter Structure

| Lesson | Duration | Focus |
|--------|----------|-------|
| 0. Build Your Integration Skills | 40 min | Create two skills from official documentation |
| 1. Phone Integration with SIP & Twilio | 45 min | Connect to telephone network |
| 2. Browser Audio Capture & VAD | 50 min | Browser microphone and client-side VAD |
| 3. Production Telephony Patterns | 50 min | IVR, recording, failover, compliance |

**Total**: Approximately 185 minutes

---

## What You Will Build

By the end of this chapter, you will have:

1. **Two production skills** for guiding telephony and browser audio integration
2. **Phone number connection** receiving real calls to your voice agent
3. **Outbound calling capability** for your agent to initiate calls
4. **Browser audio capture** with low-latency AudioWorklet processing
5. **Client-side VAD** reducing server round-trips through WebAssembly
6. **IVR flow** with natural language intent detection
7. **Compliant recording** with GDPR-aware consent handling
8. **Multi-provider failover** ensuring high availability

These components compose into the final piece of your Task Manager voice agent: accessibility from real phones and web browsers.

---

## Prerequisites

This chapter requires:

- **Chapter 80 (LiveKit Agents)**: You understand voice agent architecture and room-based audio
- **Chapter 81 (Pipecat)**: You understand pipeline composition and transport abstraction
- **Chapter 82 (OpenAI Realtime API)**: You can work with direct WebSocket voice APIs
- **Chapter 83 (Gemini Live API)**: You understand multimodal voice integration
- **Part 7 (Cloud-Native Development)**: You can deploy services to Kubernetes

You should be comfortable with:
- Async Python programming
- WebSocket communication patterns
- Basic networking concepts (HTTP, TCP, NAT)
- JavaScript for browser integration

---

## When to Use Each Integration

**Choose SIP trunk integration when:**
- You need lowest latency (50-100ms savings over webhooks)
- You have high call volumes (1000+ calls per day)
- You are building for enterprise call centers
- You already have SIP infrastructure

**Choose Twilio webhooks when:**
- You want simpler setup without SIP complexity
- You need Twilio's additional features (recordings, transcriptions)
- You are building proof-of-concept or MVP
- You have moderate call volumes

**Choose browser audio when:**
- Your users access via web application
- You want to avoid phone network costs entirely
- You need lowest latency (no PSTN hop)
- Your users have reliable internet connections

**Choose hybrid (phone + browser) when:**
- Different users have different access preferences
- You want maximum reach (everyone has a phone OR browser)
- You are building production-grade customer service

---

## Looking Ahead

Chapter 85 (Capstone: Production Voice Agent) brings everything together. You will compose:
- Voice AI frameworks (Chapters 80-81)
- Direct API access (Chapters 82-83)
- Phone and browser integration (this chapter)

The result: a complete, production-ready voice agent for your Task Manager that customers can reach via phone, browser, or both. The capstone demonstrates the full voice agent lifecycle from specification to deployment to monetization.
