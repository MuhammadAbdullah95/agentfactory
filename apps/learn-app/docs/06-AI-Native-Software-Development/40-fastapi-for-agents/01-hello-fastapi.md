---
title: "Hello FastAPI"
sidebar_position: 1
chapter: 40
lesson: 1
duration_minutes: 45

skills:
  - name: "Creating FastAPI Applications"
    proficiency_level: "A2"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student creates working FastAPI app with uvicorn"

  - name: "Path and Query Parameters"
    proficiency_level: "A2"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student implements endpoints with path and query params"

  - name: "Using Swagger UI"
    proficiency_level: "A2"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student tests API endpoints using Swagger UI"

learning_objectives:
  - objective: "Create a FastAPI application and run it with uvicorn"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Application runs and responds at http://localhost:8000"

  - objective: "Implement endpoints with path and query parameters"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Endpoints accept parameters and return correct JSON"

  - objective: "Use Swagger UI to explore and test API endpoints"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student successfully uses 'Try it out' to test endpoints"

cognitive_load:
  new_concepts: 5
  assessment: "FastAPI instance, decorators, path params, query params, Swagger UI - within A2 limit"

differentiation:
  extension_for_advanced: "Add multiple endpoints with different HTTP methods; explore the OpenAPI JSON"
  remedial_for_struggling: "Focus on single GET endpoint before adding parameters"

generated_by: "content-implementer"
source_spec: "specs/040-chapter-40-fastapi-for-agents/spec.md"
created: "2025-12-22"
---

# Hello FastAPI

You've built MCP servers with HTTP transports. You've seen how tools communicate over HTTP. Now you'll learn FastAPI—the Python framework that makes building HTTP APIs straightforward and enjoyable.

FastAPI gives you everything you need: automatic request validation, interactive documentation, and async support out of the box. By the end of this lesson, you'll have a running API with endpoints you can test in your browser.

## Why FastAPI?

In Chapter 38, you built MCP servers that communicate over HTTP. Those servers handle specific MCP protocol messages. FastAPI takes the same HTTP concepts and makes them general-purpose—you can build any kind of API.

FastAPI stands out for three reasons:

**1. Automatic Documentation** — Every endpoint you create appears in an interactive Swagger UI. You can test your API without writing a single line of client code.

**2. Type-Safe Validation** — FastAPI uses Python type hints to validate incoming data automatically. Wrong type? You get a clear error response.

**3. Async-First** — Built on Starlette, FastAPI handles async/await natively. This matters for agent integration, where you'll call LLM APIs that take seconds to respond.

## Creating Your First Application

Let's build a Task API step by step. Create a new project:

```bash
mkdir task-api && cd task-api
uv init
uv add fastapi "uvicorn[standard]"
```

Create `main.py`:

```python
from fastapi import FastAPI

app = FastAPI(
    title="Task API",
    description="A simple task management API"
)

@app.get("/")
def read_root():
    return {"message": "Task API is running"}
```

That's a complete FastAPI application. Let's break it down:

- `FastAPI()` creates the application instance. The `title` and `description` appear in the documentation.
- `@app.get("/")` is a **decorator** that tells FastAPI "when someone makes a GET request to `/`, call this function."
- The function returns a dictionary, which FastAPI automatically converts to JSON.

Run your application:

```bash
uv run uvicorn main:app --reload
```

- `main:app` means "the `app` object in `main.py`"
- `--reload` restarts the server when you change code

Open http://localhost:8000 in your browser. You'll see:

```json
{"message": "Task API is running"}
```

Your API is live.

## The Swagger UI Playground

Here's where FastAPI shines. Open http://localhost:8000/docs

You'll see an interactive documentation page. Every endpoint you create appears here automatically. Click on `GET /` to expand it, then click "Try it out" and "Execute."

This is your API playground. No need to use curl or write test scripts—Swagger UI lets you test everything visually.

There's also http://localhost:8000/redoc for alternative documentation, and http://localhost:8000/openapi.json for the raw OpenAPI specification.

## Path Parameters

Real APIs need dynamic routes. Let's add an endpoint that accepts a task ID:

```python
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    return {"task_id": task_id, "title": f"Task {task_id}"}
```

The `{task_id}` in the path becomes a **path parameter**. FastAPI:
1. Extracts the value from the URL
2. Converts it to the type you specified (`int`)
3. Passes it to your function

Try it:
- http://localhost:8000/tasks/1 → `{"task_id": 1, "title": "Task 1"}`
- http://localhost:8000/tasks/42 → `{"task_id": 42, "title": "Task 42"}`
- http://localhost:8000/tasks/abc → 422 error (not a valid integer)

That last one shows automatic validation. FastAPI rejects invalid data before your code runs.

Check Swagger UI—the new endpoint appears with documentation showing the parameter type.

## Query Parameters

Sometimes you want optional parameters. Query parameters appear after `?` in the URL:

```python
@app.get("/tasks/{task_id}")
def read_task(task_id: int, include_details: bool = False):
    task = {"task_id": task_id, "title": f"Task {task_id}"}
    if include_details:
        task["details"] = "This task has additional details"
    return task
```

Now you can:
- http://localhost:8000/tasks/1 → Basic task info
- http://localhost:8000/tasks/1?include_details=true → Task with details

Query parameters with default values are optional. Parameters without defaults are required:

```python
@app.get("/search")
def search_tasks(query: str, limit: int = 10):
    return {"query": query, "limit": limit}
```

- http://localhost:8000/search → 422 error (query is required)
- http://localhost:8000/search?query=urgent → Works, limit defaults to 10
- http://localhost:8000/search?query=urgent&limit=5 → Both parameters provided

## Hands-On Exercise

Build a Task API with these endpoints:

1. `GET /` — Returns a welcome message
2. `GET /tasks/{task_id}` — Returns a task with the given ID
3. `GET /tasks/{task_id}?details=true` — Returns extra information when details is true

Create the complete `main.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="Task API")

@app.get("/")
def read_root():
    return {"message": "Task API is running", "version": "1.0.0"}

@app.get("/tasks/{task_id}")
def read_task(task_id: int, details: bool = False):
    task = {
        "id": task_id,
        "title": f"Task {task_id}",
        "status": "pending"
    }
    if details:
        task["description"] = "This is a detailed description"
        task["created_at"] = "2025-01-01T00:00:00Z"
    return task
```

Run it and test in Swagger UI:
1. Open http://localhost:8000/docs
2. Try each endpoint
3. Toggle the `details` parameter
4. Try an invalid task_id (like "abc") and observe the 422 error

## Common Mistakes

**Mistake 1**: Forgetting to return a dictionary

```python
# Wrong - returns None
@app.get("/")
def read_root():
    message = "Hello"

# Correct - returns a dictionary
@app.get("/")
def read_root():
    return {"message": "Hello"}
```

**Mistake 2**: Type mismatch in path parameters

```python
# If URL is /tasks/abc but parameter is int, FastAPI returns 422
@app.get("/tasks/{task_id}")
def read_task(task_id: int):  # Expects integer
    return {"task_id": task_id}
```

This is a feature, not a bug. FastAPI catches invalid data before it reaches your code.

**Mistake 3**: Confusing path and query parameters

```python
# Path parameter - in the URL path
@app.get("/tasks/{task_id}")  # /tasks/123

# Query parameter - after ?
@app.get("/tasks")
def list_tasks(status: str | None = None):  # /tasks?status=pending
```

## Try With AI

**Explore FastAPI's Foundations:**

> "I just created my first FastAPI endpoint. Explain what happens when I visit http://localhost:8000/tasks/5 — trace the request from browser to my function and back."

**Understand Automatic Validation:**

> "FastAPI returned a 422 error when I passed 'abc' instead of a number. Show me exactly what the error response looks like and explain each field."

**Extend Your Knowledge:**

> "I want to add an endpoint that searches tasks by title. Should I use a path parameter or query parameter? Explain the difference with concrete examples."

**Challenge Yourself:**

> "Create an endpoint that accepts multiple query parameters: status (required), priority (optional, default 'medium'), and limit (optional, default 10). Show me the function signature and example URLs."

---

## Summary

You've created your first FastAPI application:

- **FastAPI instance**: `app = FastAPI(title="...")`
- **Route decorators**: `@app.get("/path")` connects URLs to functions
- **Path parameters**: `{task_id}` in the path, type-validated automatically
- **Query parameters**: Optional parameters with defaults
- **Swagger UI**: Interactive documentation at `/docs`

Next lesson, you'll add POST endpoints with Pydantic models for creating tasks with validated data.
