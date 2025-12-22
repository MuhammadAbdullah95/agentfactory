---
title: "POST and Pydantic Models"
sidebar_position: 2
chapter: 40
lesson: 2
duration_minutes: 50

skills:
  - name: "Pydantic Model Definition"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student creates Pydantic models with proper field types"

  - name: "Request Body Handling"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student implements POST endpoints that parse request bodies"

  - name: "Response Model Serialization"
    proficiency_level: "A2"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student uses response_model for output validation"

learning_objectives:
  - objective: "Define Pydantic models for request and response validation"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates TaskCreate and TaskResponse models"

  - objective: "Implement POST endpoints that create resources"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "POST /tasks creates task and returns it with 201 status"

  - objective: "Handle validation errors from Pydantic"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student explains 422 error response structure"

cognitive_load:
  new_concepts: 5
  assessment: "Pydantic BaseModel, Optional fields, POST endpoints, request bodies, response_model"

differentiation:
  extension_for_advanced: "Add field validators and custom error messages"
  remedial_for_struggling: "Start with single-field models before adding complexity"

generated_by: "content-implementer"
source_spec: "specs/040-chapter-40-fastapi-for-agents/spec.md"
created: "2025-12-22"
---

# POST and Pydantic Models

GET endpoints retrieve data. POST endpoints create data. To create a task, you need to send data in the request body. FastAPI uses Pydantic models to define what that data should look like and validate it automatically.

Pydantic is already installed with FastAPI. It provides type-safe data validation that catches errors before they reach your code.

## Why Pydantic?

When a client sends JSON to your API, you need to:
1. Parse the JSON
2. Validate the data types
3. Check required fields
4. Handle missing or invalid data

Pydantic does all of this automatically. You define a model, and FastAPI handles the rest.

```python
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
```

This model says:
- `title` is required and must be a string
- `description` is optional (can be `None`) and defaults to `None`

## Defining Task Models

For our Task API, we need two models:

1. **TaskCreate** — What the client sends when creating a task
2. **TaskResponse** — What the API returns

```python
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
```

Why two models? The client shouldn't provide `id` or `status`—those are set by the server. Separating models keeps responsibilities clear.

## Creating a POST Endpoint

Add these to your `main.py`:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")

# Pydantic models
class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str

# In-memory storage
tasks: list[dict] = []

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "status": "pending"
    }
    tasks.append(new_task)
    return new_task
```

Key elements:

- `@app.post("/tasks")` — This endpoint handles POST requests
- `task: TaskCreate` — FastAPI parses the request body as a `TaskCreate`
- `response_model=TaskResponse` — FastAPI validates the response matches this model
- `status_code=201` — Return 201 Created instead of default 200

## Testing in Swagger UI

Open http://localhost:8000/docs and find the POST endpoint.

1. Click "Try it out"
2. In the request body, enter:
   ```json
   {
     "title": "Learn FastAPI",
     "description": "Complete the tutorial"
   }
   ```
3. Click "Execute"

You'll see a 201 response with the created task:

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Complete the tutorial",
  "status": "pending"
}
```

## Validation Errors

What happens with invalid data? Try posting:

```json
{
  "description": "Missing title"
}
```

FastAPI returns a 422 Unprocessable Entity:

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "title"],
      "msg": "Field required",
      "input": {"description": "Missing title"}
    }
  ]
}
```

The error tells you exactly what's wrong:
- `type`: What kind of error
- `loc`: Where the error occurred (body → title)
- `msg`: Human-readable message
- `input`: What was received

Try another invalid request:

```json
{
  "title": 123
}
```

You'll get:

```json
{
  "detail": [
    {
      "type": "string_type",
      "loc": ["body", "title"],
      "msg": "Input should be a valid string",
      "input": 123
    }
  ]
}
```

Pydantic caught that `title` should be a string, not a number.

## Response Model Filtering

The `response_model` parameter does more than validation—it filters the output. If your internal data has extra fields, only the model's fields are returned.

```python
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "status": "pending",
        "internal_flag": True,  # This won't be in the response
        "debug_info": "extra data"  # Neither will this
    }
    tasks.append(new_task)
    return new_task
```

Only `id`, `title`, `description`, and `status` appear in the response because those are the fields in `TaskResponse`.

## In-Memory Storage

For now, we're using a simple list to store tasks:

```python
tasks: list[dict] = []
```

This works for learning but resets when you restart the server. We'll connect to databases in Chapter 47.

The pattern is straightforward:
- Create: Append to list
- Read: Iterate and find
- Update: Find and modify
- Delete: Find and remove

## Hands-On Exercise

Build the complete task creation flow:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str

tasks: list[dict] = []

@app.get("/")
def read_root():
    return {"message": "Task API", "task_count": len(tasks)}

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "description": task.description,
        "status": "pending"
    }
    tasks.append(new_task)
    return new_task

@app.get("/tasks")
def list_tasks():
    return tasks
```

Test this workflow:
1. POST a task with title "First task"
2. POST another task with title and description
3. GET /tasks to see both tasks
4. GET / to see the task count
5. Try posting without a title and observe the 422 error

## Common Mistakes

**Mistake 1**: Using the wrong model for create vs response

```python
# Wrong - client shouldn't provide id and status
class Task(BaseModel):
    id: int
    title: str
    status: str

@app.post("/tasks")
def create_task(task: Task):  # Client must provide id?
    ...
```

Create separate models for input (TaskCreate) and output (TaskResponse).

**Mistake 2**: Forgetting `response_model`

```python
# Without response_model, you might leak internal data
@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {..., "password_hash": "secret123"}  # Oops, exposed!
    return new_task
```

Always use `response_model` to control what's returned.

**Mistake 3**: Not handling Optional correctly

```python
# Wrong - this makes description required
description: str

# Correct - union type with default None (Python 3.10+)
description: str | None = None
```

## Try With AI

**Understand Pydantic Deeply:**

> "Explain what happens when FastAPI receives a POST request with JSON body. Trace the data from raw bytes to my function parameter. How does Pydantic fit in?"

**Explore Validation:**

> "I want to add validation to my TaskCreate model: title must be at least 3 characters. Show me how to use Pydantic's Field() with constraints."

**Handle Edge Cases:**

> "What happens if a client sends extra fields in the JSON that aren't in my Pydantic model? Does FastAPI reject them or ignore them? How can I change this behavior?"

**Extend Your Models:**

> "Add a 'priority' field to TaskCreate that only accepts 'low', 'medium', or 'high'. Show me how to use an Enum with Pydantic."

---

## Summary

You've learned to create resources with POST endpoints:

- **Pydantic models**: Define data structure with `BaseModel`
- **Request bodies**: `task: TaskCreate` parses JSON automatically
- **Validation**: Pydantic rejects invalid data with 422 errors
- **Response models**: Control output with `response_model`
- **Status codes**: Return 201 for resource creation

Next lesson, you'll implement the full CRUD operations—reading, updating, and deleting tasks.
