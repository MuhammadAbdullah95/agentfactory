---
sidebar_position: 74
title: "Chapter 74: Async Patterns and Streaming for AI"
---

# Chapter 74: Async Patterns and Streaming for AI

Modern AI interfaces don't make users wait. When you chat with Claude or ChatGPT, responses stream token-by-token—you see the AI "thinking" in real-time. This isn't just a UX nicety; it's essential. LLM responses can take 10-30 seconds for complex queries. Without streaming, users stare at blank screens wondering if something broke.

This chapter teaches the async patterns that power every production AI interface. You'll master Promises, async/await, cancellation with AbortController, and most importantly—streaming with Server-Sent Events (SSE) and the new Streamable HTTP pattern used by MCP.

You already understand async concepts from Python's asyncio. TypeScript's async model is simpler—no event loop management, no `await asyncio.gather()`. But the patterns for AI applications—streaming, cancellation, retry logic—are specific to the frontend context.

## 🎯 Before You Begin

**Prerequisites**: Chapter 73 (TypeScript fundamentals). Understanding of async/await from Python Part 5.

**What you'll need**: Node.js or Bun runtime, a streaming AI API endpoint (we'll use OpenAI-compatible).

---

## What You'll Learn

### Async Fundamentals (Lessons 1-2)
- **Promises and async/await**: TypeScript's async model compared to Python's asyncio—simpler syntax, same concepts
- **Error Handling**: try/catch patterns, Promise rejection, handling partial failures gracefully

### Cancellation and Timeouts (Lesson 3)
- **AbortController**: Cancel in-flight requests when users navigate away or click "Stop"
- **Timeout Patterns**: Implement timeouts for AI requests that might hang indefinitely

### Streaming Patterns (Lessons 4-5)
- **Server-Sent Events (SSE)**: The original LLM streaming standard—OpenAI/Anthropic APIs use this protocol
- **Streamable HTTP (MCP Standard)**: The new bidirectional transport for Model Context Protocol (SDK 1.10.0+)—understand why it replaced SSE for MCP and how to implement it
- **Async Iteration**: `for await...of` loops for consuming streams elegantly

### Production Patterns (Lessons 6-7)
- **Retry Logic**: Exponential backoff for transient failures, circuit breakers for persistent issues
- **Rate Limiting**: Client-side throttling to respect API limits
- **Concurrent Requests**: Promise.all, Promise.allSettled, and managing multiple AI calls

---

## Why Streaming Matters for AI

Consider the user experience difference:

**Without streaming** (traditional request/response):
```
User: "Explain quantum computing"
[Loading spinner for 15 seconds...]
[Entire 500-word response appears at once]
```

**With streaming** (token-by-token):
```
User: "Explain quantum computing"
"Quantum" [100ms] "computing" [100ms] "uses" [100ms] "quantum" [100ms]...
[Response builds word-by-word, user reads as it generates]
```

Streaming transforms perceived latency from 15 seconds to 100 milliseconds. Users engage immediately instead of abandoning.

---

## The Streaming Protocol Stack

Modern AI applications use multiple streaming approaches:

| Protocol | Use Case | Direction |
|----------|----------|-----------|
| **SSE** | LLM token streaming | Server → Client |
| **WebSocket** | Voice/video AI, bidirectional chat | Bidirectional |
| **Streamable HTTP** | MCP remote servers | Bidirectional (HTTP-based) |

This chapter focuses on SSE (most common for AI) and Streamable HTTP (emerging MCP standard).

---

## Chapter Structure

| Lesson | Topic | Duration |
|--------|-------|----------|
| 1 | Promises and async/await | 20 min |
| 2 | Error Handling for Async Operations | 20 min |
| 3 | AbortController and Timeouts | 25 min |
| 4 | Server-Sent Events (SSE) Deep Dive | 30 min |
| 5 | Streamable HTTP: The MCP Standard | 25 min |
| 6 | Retry Logic and Circuit Breakers | 25 min |
| 7 | Concurrent Requests and Rate Limiting | 20 min |

**Total**: ~2.5 hours

---

## What You'll Build

**Capstone: Streaming AI CLI Client**

By the end of this chapter, you'll build a complete CLI that streams AI responses:

```typescript
// Your streaming client implementation
async function chat(prompt: string): Promise<void> {
  const controller = new AbortController();

  // Allow Ctrl+C to cancel
  process.on("SIGINT", () => controller.abort());

  try {
    const response = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${process.env.OPENAI_API_KEY}`,
      },
      body: JSON.stringify({
        model: "gpt-4",
        messages: [{ role: "user", content: prompt }],
        stream: true,
      }),
      signal: controller.signal,
    });

    // Stream tokens to terminal
    for await (const chunk of parseSSE(response.body!)) {
      process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
    }
    console.log(); // Final newline

  } catch (error) {
    if (error.name === "AbortError") {
      console.log("\n[Cancelled by user]");
    } else {
      throw error;
    }
  }
}
```

Features you'll implement:
- Real-time token streaming with SSE parsing
- Cancellation with AbortController (Ctrl+C support)
- Retry logic with exponential backoff
- Timeout handling for slow responses

---

## Key Patterns You'll Master

### 1. SSE Parsing
```typescript
async function* parseSSE(stream: ReadableStream<Uint8Array>) {
  const reader = stream.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    const lines = buffer.split("\n\n");
    buffer = lines.pop() ?? "";

    for (const line of lines) {
      if (line.startsWith("data: ") && line !== "data: [DONE]") {
        yield JSON.parse(line.slice(6));
      }
    }
  }
}
```

### 2. Retry with Backoff
```typescript
async function withRetry<T>(
  fn: () => Promise<T>,
  maxRetries = 3,
  baseDelay = 1000
): Promise<T> {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      if (attempt === maxRetries - 1) throw error;
      const delay = baseDelay * Math.pow(2, attempt);
      await new Promise(r => setTimeout(r, delay));
    }
  }
  throw new Error("Unreachable");
}
```

### 3. Concurrent with Limits
```typescript
async function batchProcess<T, R>(
  items: T[],
  processor: (item: T) => Promise<R>,
  concurrency = 5
): Promise<R[]> {
  const results: R[] = [];
  const executing = new Set<Promise<void>>();

  for (const item of items) {
    const promise = processor(item).then(r => {
      results.push(r);
      executing.delete(promise);
    });
    executing.add(promise);

    if (executing.size >= concurrency) {
      await Promise.race(executing);
    }
  }

  await Promise.all(executing);
  return results;
}
```

---

## What's Next

After mastering async patterns, **Chapter 75: Runtime Environments and HTTP Communication** teaches you where TypeScript runs—Node.js, Deno, Bun, Edge Functions—and how to build HTTP servers that stream AI responses to clients. You'll implement a complete SSE server that connects to your Python AI backends.

---

## Pedagogical Approach

This chapter uses **Layer 2 (AI Collaboration)** with heavy emphasis on production patterns:

- You understand async from Python—AI helps you adapt to TypeScript's simpler model
- Real streaming APIs (OpenAI, Anthropic) provide authentic practice targets
- Error scenarios are explored with AI help—what happens when streams fail mid-response?

The Three Roles apply:
- **AI as Teacher**: Explains SSE protocol details, Streamable HTTP evolution
- **AI as Student**: You describe edge cases from your domain, AI helps implement handlers
- **AI as Co-Worker**: Pair-program on retry logic and error handling
