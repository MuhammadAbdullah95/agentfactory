---
title: "Streaming with SSE"
sidebar_position: 6
chapter: 40
lesson: 6
duration_minutes: 55

skills:
  - name: "Server-Sent Events"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student implements SSE endpoint with EventSourceResponse"

  - name: "Async Generators"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student creates async generator for streaming data"

  - name: "Real-time Data Patterns"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student explains when to use streaming vs polling"

learning_objectives:
  - objective: "Implement streaming responses using Server-Sent Events"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "SSE endpoint sends events that browser receives"

  - objective: "Create async generators for producing stream data"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Generator yields events with proper format"

  - objective: "Test streaming endpoints in browser"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student uses EventSource API to receive events"

cognitive_load:
  new_concepts: 4
  assessment: "SSE format, EventSourceResponse, async generators, browser EventSource"

differentiation:
  extension_for_advanced: "Handle connection errors; implement heartbeat/keepalive"
  remedial_for_struggling: "Focus on single-event stream before adding complexity"

generated_by: "content-implementer"
source_spec: "specs/040-chapter-40-fastapi-for-agents/spec.md"
created: "2025-12-22"
---

# Streaming with SSE

Some operations take time. When an AI agent generates a response, you don't want users staring at a loading spinner for 30 seconds. Streaming sends data as it becomes available—token by token for LLMs, update by update for long-running tasks.

Server-Sent Events (SSE) is a simple protocol for server-to-client streaming. The server pushes events, and the client receives them in real-time. You've seen this in ChatGPT—words appearing as the model generates them.

## Why Streaming?

Traditional request-response:
1. Client sends request
2. Server processes (30 seconds)
3. Client waits...
4. Server sends complete response

Streaming:
1. Client sends request
2. Server starts processing
3. Server sends first chunk immediately
4. Server sends more chunks as available
5. Client sees progress in real-time

For AI agents, this means:
- Users see responses forming, not waiting
- Long-running tasks show progress
- Failed operations fail fast, not after a timeout

## Installing sse-starlette

FastAPI doesn't include SSE by default. Add the package:

```bash
uv add sse-starlette
```

This provides `EventSourceResponse`, which handles SSE formatting.

## SSE Event Format

SSE events are simple text:

```
event: task_update
data: {"task_id": 1, "status": "in_progress"}

event: task_update
data: {"task_id": 1, "status": "completed"}
```

Each event has:
- `event`: Event type (optional, default is "message")
- `data`: The payload (must be a string, usually JSON)
- Blank line: Separates events

## Creating a Streaming Endpoint

```python
from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse
import asyncio
import json

app = FastAPI(title="Task API")

async def task_updates_generator():
    """Simulates task status updates over time."""
    for i in range(5):
        yield {
            "event": "task_update",
            "data": json.dumps({
                "task_id": i + 1,
                "status": "processing",
                "progress": (i + 1) * 20
            })
        }
        await asyncio.sleep(1)  # Simulate work

    yield {
        "event": "complete",
        "data": json.dumps({"message": "All tasks processed"})
    }

@app.get("/tasks/stream")
async def stream_task_updates():
    return EventSourceResponse(task_updates_generator())
```

Key elements:
- `async def` with `yield` creates an **async generator**
- Each `yield` sends one SSE event
- `await asyncio.sleep(1)` simulates processing time
- `EventSourceResponse` wraps the generator

## Testing in Browser

You can't use Swagger UI for SSE—it expects regular responses. Open your browser's console and run:

```javascript
const source = new EventSource('http://localhost:8000/tasks/stream');

source.onmessage = (event) => {
    console.log('Message:', event.data);
};

source.addEventListener('task_update', (event) => {
    console.log('Task update:', JSON.parse(event.data));
});

source.addEventListener('complete', (event) => {
    console.log('Complete:', JSON.parse(event.data));
    source.close();
});

source.onerror = (error) => {
    console.error('Error:', error);
    source.close();
};
```

You'll see events arriving one second apart.

## Streaming with Context

Let's add streaming that relates to a specific task:

```python
from fastapi import Depends, HTTPException, status
from repository import TaskRepository, get_task_repo

async def task_progress_generator(task_id: int, total_steps: int = 5):
    """Streams progress updates for a specific task."""
    for step in range(1, total_steps + 1):
        yield {
            "event": "progress",
            "data": json.dumps({
                "task_id": task_id,
                "step": step,
                "total_steps": total_steps,
                "percentage": int((step / total_steps) * 100)
            })
        }
        await asyncio.sleep(0.5)

    yield {
        "event": "complete",
        "data": json.dumps({
            "task_id": task_id,
            "status": "completed"
        })
    }

@app.get("/tasks/{task_id}/progress")
async def stream_task_progress(
    task_id: int,
    repo: TaskRepository = Depends(get_task_repo)
):
    # Verify task exists before streaming
    task = repo.get_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    return EventSourceResponse(task_progress_generator(task_id))
```

This validates the task exists before starting the stream.

## Complete Streaming Example

Here's a full example with multiple stream types:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from sse_starlette.sse import EventSourceResponse
import asyncio
import json

from repository import TaskRepository, get_task_repo

app = FastAPI(title="Task API")

# Stream 1: System-wide updates
async def system_updates_generator():
    """Simulates system-wide events."""
    events = [
        ("info", "System started"),
        ("task_created", {"task_id": 1}),
        ("task_updated", {"task_id": 1, "status": "in_progress"}),
        ("task_completed", {"task_id": 1}),
        ("info", "Batch complete"),
    ]

    for event_type, data in events:
        yield {
            "event": event_type,
            "data": json.dumps(data) if isinstance(data, dict) else data
        }
        await asyncio.sleep(1)

@app.get("/stream/system")
async def stream_system_updates():
    return EventSourceResponse(system_updates_generator())

# Stream 2: Task-specific progress
async def task_work_generator(task_id: int, task_title: str):
    """Simulates work on a specific task."""
    steps = [
        "Starting task...",
        "Analyzing requirements...",
        "Processing data...",
        "Generating output...",
        "Finalizing...",
    ]

    for i, step in enumerate(steps, 1):
        yield {
            "event": "step",
            "data": json.dumps({
                "task_id": task_id,
                "task_title": task_title,
                "step": i,
                "message": step,
                "progress": int((i / len(steps)) * 100)
            })
        }
        await asyncio.sleep(0.8)

    yield {
        "event": "done",
        "data": json.dumps({
            "task_id": task_id,
            "message": "Task completed successfully"
        })
    }

@app.post("/tasks/{task_id}/execute")
async def execute_task(
    task_id: int,
    repo: TaskRepository = Depends(get_task_repo)
):
    task = repo.get_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )

    return EventSourceResponse(
        task_work_generator(task_id, task["title"])
    )

# Stream 3: Countdown timer
async def countdown_generator(seconds: int):
    """Simple countdown stream."""
    for i in range(seconds, 0, -1):
        yield {
            "event": "tick",
            "data": json.dumps({"remaining": i})
        }
        await asyncio.sleep(1)

    yield {
        "event": "complete",
        "data": json.dumps({"message": "Countdown finished!"})
    }

@app.get("/stream/countdown/{seconds}")
async def stream_countdown(seconds: int):
    if seconds < 1 or seconds > 60:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Seconds must be between 1 and 60"
        )
    return EventSourceResponse(countdown_generator(seconds))
```

## Hands-On Exercise

Build a streaming endpoint for task processing:

**Step 1**: Add sse-starlette to your project

```bash
uv add sse-starlette
```

**Step 2**: Create a streaming endpoint

```python
@app.get("/tasks/{task_id}/process")
async def process_task(
    task_id: int,
    repo: TaskRepository = Depends(get_task_repo)
):
    task = repo.get_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )

    async def process():
        # Your streaming logic here
        yield {"event": "start", "data": json.dumps({"task_id": task_id})}
        await asyncio.sleep(1)
        yield {"event": "progress", "data": json.dumps({"percent": 50})}
        await asyncio.sleep(1)
        yield {"event": "done", "data": json.dumps({"result": "success"})}

    return EventSourceResponse(process())
```

**Step 3**: Test in browser console

```javascript
const source = new EventSource('http://localhost:8000/tasks/1/process');
source.onmessage = e => console.log(e.data);
source.onerror = () => source.close();
```

**Step 4**: Observe events arriving in real-time

## Error Handling in Streams

What happens when an error occurs mid-stream?

```python
async def risky_generator():
    try:
        for i in range(10):
            if i == 5:
                raise ValueError("Something went wrong!")
            yield {"data": json.dumps({"step": i})}
            await asyncio.sleep(0.5)
    except Exception as e:
        yield {
            "event": "error",
            "data": json.dumps({"error": str(e)})
        }
```

The client receives an error event and can handle it gracefully.

## Common Mistakes

**Mistake 1**: Forgetting to import json for data serialization

```python
# Wrong - data must be a string
yield {"data": {"task_id": 1}}

# Correct - serialize to JSON string
yield {"data": json.dumps({"task_id": 1})}
```

**Mistake 2**: Not closing the connection on the client

```javascript
// Wrong - connection stays open forever
const source = new EventSource('/stream');

// Correct - close when done
source.addEventListener('complete', () => source.close());
```

**Mistake 3**: Blocking the event loop

```python
# Wrong - blocks other requests
import time
await time.sleep(1)  # This is synchronous!

# Correct - use async sleep
await asyncio.sleep(1)
```

**Mistake 4**: Returning instead of yielding

```python
# Wrong - sends nothing
async def generator():
    return {"data": "hello"}  # Not a generator!

# Correct - yield makes it a generator
async def generator():
    yield {"data": "hello"}
```

## Try With AI

**Understand SSE Protocol:**

> "Explain the SSE protocol format in detail. What are the optional fields besides 'event' and 'data'? How does the browser handle reconnection?"

**Handle Edge Cases:**

> "What happens if the client disconnects mid-stream? How do I detect this in my async generator and clean up resources?"

**Build Real Features:**

> "I want to stream the status of multiple tasks at once. Show me how to implement a generator that monitors several tasks and yields updates as any of them changes."

**Compare Alternatives:**

> "When should I use SSE vs WebSockets? What are the trade-offs for AI agent responses?"

---

## Summary

You've learned to implement streaming with SSE:

- **sse-starlette**: Provides `EventSourceResponse`
- **Async generators**: `async def` with `yield` for data production
- **Event format**: `event` and `data` fields
- **Browser testing**: Use `EventSource` API in JavaScript
- **Error handling**: Yield error events gracefully

Next lesson, you'll integrate an AI agent—sending user questions and streaming the agent's response.
