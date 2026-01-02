---
sidebar_position: 75
title: "Chapter 75: Runtime Environments and HTTP Communication"
---

# Chapter 75: Runtime Environments and HTTP Communication

TypeScript doesn't run directly—it compiles to JavaScript that executes in a runtime. In 2026, you have more choices than ever: Node.js 22+ with native TypeScript support, Deno 2 with security-first design, Bun with 3-4x faster cold starts, and Edge Functions for globally distributed low-latency AI responses.

This chapter teaches you where TypeScript runs, how to write cross-runtime code, and how to build HTTP clients and servers that power AI applications. You'll understand which runtime to choose for your use case and how to avoid vendor lock-in.

## Before You Begin

**Prerequisites**: Chapter 73 (TypeScript fundamentals), Chapter 74 (async patterns). Understanding of HTTP basics from Part 6 FastAPI work.

**What you'll need**: Node.js 22+, Deno 2, and Bun installed. We'll install all three together.

---

## What You'll Learn

### Runtime Environments (Lessons 1-4)
- **Node.js 22+**: The industry standard with native TypeScript support (`--experimental-strip-types`)
- **Deno 2**: Security-first with npm compatibility—no more import maps required
- **Bun**: JavaScriptCore engine for 3-4x faster cold starts and built-in bundler
- **Edge Functions**: Cloudflare Workers, Vercel Edge, Deno Deploy for sub-100ms AI responses globally

### HTTP Communication (Lessons 5-6)
- **HTTP Client Patterns**: Universal fetch API, Request/Response objects, header management
- **Building HTTP Servers**: Fastify (Node.js), Hono (Edge-first), ElysiaJS (Bun-native)

---

## Why Multiple Runtimes Matter

Different contexts demand different runtimes:

| Context | Best Runtime | Why |
|---------|--------------|-----|
| **Production APIs** | Node.js 22+ | Largest ecosystem, enterprise support, native TypeScript |
| **CLI Tools** | Bun | Fastest cold start, single binary distribution |
| **Secure Scripts** | Deno 2 | Permission model, no accidental network/file access |
| **Global AI APIs** | Edge Functions | Sub-50ms latency worldwide, no cold start |
| **Monorepo Shared Code** | All | Write once, test across runtimes |

**The insight**: Modern TypeScript is runtime-agnostic when you stick to standard APIs (fetch, Web Streams, Web Crypto). This chapter teaches you to write code that works everywhere.

---

## Runtime Comparison (2026)

| Feature | Node.js 22+ | Deno 2 | Bun 1.x |
|---------|-------------|--------|---------|
| **TypeScript** | Native (--experimental-strip-types) | Native (no compile step) | Native (built-in transpiler) |
| **Package Manager** | npm/pnpm/yarn | npm compatible | bun (25x faster than npm) |
| **Cold Start** | ~200ms | ~100ms | ~50ms |
| **npm Compatibility** | 100% | 100% (Deno 2) | ~99% |
| **Security Model** | Trust everything | Explicit permissions | Trust everything |
| **Edge Deploy** | Via adapters | Deno Deploy | Limited |

---

## Chapter Structure

| Lesson | Topic | Duration |
|--------|-------|----------|
| 1 | Node.js 22+: The Server-Side Standard | 25 min |
| 2 | Deno 2: Security-First Runtime | 20 min |
| 3 | Bun: Performance-Optimized Runtime | 20 min |
| 4 | Edge Functions: Low-Latency AI | 20 min |
| 5 | HTTP Client Patterns | 20 min |
| 6 | Building HTTP Servers | 20 min |

**Total**: ~2 hours

---

## What You'll Build

**Capstone: Cross-Runtime HTTP Client**

By the end of this chapter, you'll create a fetch wrapper that works identically in Node.js, Deno, Bun, and browsers:

```typescript
// Works in any runtime
import { createClient } from "./ai-client";

const client = createClient({
  baseUrl: "https://api.openai.com/v1",
  apiKey: process.env.OPENAI_API_KEY,
  timeout: 30000,
  retry: { maxAttempts: 3, backoff: "exponential" },
});

// Same API everywhere
const response = await client.chat.completions.create({
  model: "gpt-4",
  messages: [{ role: "user", content: "Hello" }],
  stream: true,
});

for await (const chunk of response) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
```

This client becomes the foundation for your SDK in Chapter 76.

---

## What's Next

After understanding runtime environments, **Chapter 76: Building Type-Safe AI SDKs** teaches you to wrap AI APIs with Zod validation, integrate with Vercel AI SDK 5, and build the MCP TypeScript SDK patterns. You'll transform your cross-runtime client into a production SDK.

---

## Pedagogical Approach

This chapter uses **Layer 1 (Manual Foundation)** for runtime concepts and **Layer 2 (AI Collaboration)** for HTTP implementation:

- You'll install and test each runtime manually to understand their differences
- AI helps you adapt code patterns for cross-runtime compatibility
- Real HTTP servers give you practical experience with each framework

The Three Roles apply:
- **AI as Teacher**: Explains runtime-specific features and edge cases
- **AI as Student**: You teach the AI about your deployment constraints, AI suggests optimal runtime
- **AI as Co-Worker**: Collaborate on cross-runtime abstraction layers
