---
title: "Error Handling"
sidebar_position: 4
chapter: 40
lesson: 4
duration_minutes: 45

skills:
  - name: "HTTP Status Codes"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student explains 2xx, 4xx, 5xx status code categories"

  - name: "HTTPException Usage"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student raises appropriate exceptions for error cases"

  - name: "Error Response Design"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student creates helpful error messages"

learning_objectives:
  - objective: "Use appropriate HTTP status codes for different scenarios"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student correctly uses 200, 201, 400, 404, 422"

  - objective: "Raise HTTPException with meaningful error details"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Error responses include helpful detail messages"

  - objective: "Distinguish between validation errors and business errors"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student explains when 400 vs 422 is appropriate"

cognitive_load:
  new_concepts: 4
  assessment: "Status code categories, HTTPException, status module, error messages"

differentiation:
  extension_for_advanced: "Implement custom exception handlers and error logging"
  remedial_for_struggling: "Focus on 200, 404, and 422 before other codes"

generated_by: "content-implementer"
source_spec: "specs/040-chapter-40-fastapi-for-agents/spec.md"
created: "2025-12-22"
---

# Error Handling

When things go wrong, your API needs to respond appropriately. A missing task should return 404, not crash the server. Invalid input should return 422, not accept garbage data. Good error handling makes APIs predictable and debuggable.

## HTTP Status Codes

HTTP status codes tell clients what happened:

| Range | Category | Meaning |
|-------|----------|---------|
| 2xx | Success | Request worked |
| 4xx | Client Error | Client sent something wrong |
| 5xx | Server Error | Server failed internally |

Common codes you'll use:

| Code | Name | When to Use |
|------|------|-------------|
| 200 | OK | Request succeeded (default) |
| 201 | Created | Resource created successfully |
| 204 | No Content | Success, nothing to return |
| 400 | Bad Request | Client sent invalid data (business rules) |
| 404 | Not Found | Resource doesn't exist |
| 422 | Unprocessable Entity | Validation failed (Pydantic) |
| 500 | Internal Server Error | Something broke on the server |

## The HTTPException Class

FastAPI provides `HTTPException` for returning error responses:

```python
from fastapi import HTTPException

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    return task
```

When you `raise HTTPException`, FastAPI:
1. Stops executing your function
2. Returns the specified status code
3. Sends the detail as JSON

The response looks like:

```json
{
  "detail": "Task not found"
}
```

## Using the status Module

Magic numbers like `404` are hard to read. FastAPI provides named constants:

```python
from fastapi import HTTPException, status

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task
```

Now the code is self-documenting. Common constants:

```python
status.HTTP_200_OK
status.HTTP_201_CREATED
status.HTTP_204_NO_CONTENT
status.HTTP_400_BAD_REQUEST
status.HTTP_404_NOT_FOUND
status.HTTP_422_UNPROCESSABLE_ENTITY
status.HTTP_500_INTERNAL_SERVER_ERROR
```

## Setting Success Status Codes

Override the default 200 for specific endpoints:

```python
# Return 201 for resource creation
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # ...
    return new_task

# Return 204 for deletion (no body)
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # ... delete logic
    return None  # No response body with 204
```

## 400 vs 422: When to Use Each

**422 Unprocessable Entity** — Pydantic validation failed. The JSON is valid, but the data doesn't match your model.

```python
# Pydantic returns 422 automatically when:
# - Required field missing
# - Wrong data type
# - Field constraint violated

class TaskCreate(BaseModel):
    title: str  # If missing, 422

# POST with {"description": "no title"} → 422
```

**400 Bad Request** — Business logic validation failed. The data is valid according to the model, but it breaks your rules.

```python
@app.post("/tasks")
def create_task(task: TaskCreate):
    # Business rule: title can't be empty whitespace
    if not task.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty or whitespace"
        )
    # ...
```

The difference:
- 422: "Your JSON doesn't match my schema"
- 400: "Your data is valid but violates business rules"

## Complete Error Handling Example

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    status: str | None = None

tasks: list[dict] = []
task_counter = 0

VALID_STATUSES = {"pending", "in_progress", "completed"}

def find_task(task_id: int) -> dict | None:
    """Helper to find a task by ID."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    global task_counter

    # Business validation
    if not task.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty or whitespace"
        )

    task_counter += 1
    new_task = {
        "id": task_counter,
        "title": task.title.strip(),
        "description": task.description,
        "status": "pending"
    }
    tasks.append(new_task)
    return new_task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    task = find_task(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    # Validate title
    if not task_update.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty or whitespace"
        )

    # Validate status
    if task_update.status and task_update.status not in VALID_STATUSES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid status. Must be one of: {', '.join(VALID_STATUSES)}"
        )

    task["title"] = task_update.title.strip()
    if task_update.description is not None:
        task["description"] = task_update.description
    if task_update.status:
        task["status"] = task_update.status

    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )

    tasks.remove(task)
    return {"message": "Task deleted", "id": task_id}
```

## Hands-On Exercise

Test each error scenario in Swagger UI:

**1. Test 404 Not Found**
```bash
GET /tasks/999
# Expected: 404 with "Task with id 999 not found"
```

**2. Test 422 Validation Error**
```bash
POST /tasks
{"description": "Missing title"}
# Expected: 422 with "Field required" for title
```

**3. Test 400 Business Error**
```bash
POST /tasks
{"title": "   "}
# Expected: 400 with "Title cannot be empty or whitespace"
```

**4. Test Invalid Status**
```bash
# First create a task
POST /tasks
{"title": "Test task"}

# Then try invalid status
PUT /tasks/1
{"title": "Test", "status": "invalid"}
# Expected: 400 with "Invalid status. Must be one of..."
```

**5. Test 201 Created**
```bash
POST /tasks
{"title": "Valid task"}
# Expected: 201 status (check response headers)
```

## Error Message Best Practices

**Be specific**:
```python
# Vague
detail="Error"

# Specific
detail=f"Task with id {task_id} not found"
```

**Include context**:
```python
# Missing context
detail="Invalid status"

# With context
detail=f"Invalid status '{task_update.status}'. Must be one of: pending, in_progress, completed"
```

**Don't expose internals**:
```python
# Exposes implementation
detail=f"KeyError: 'tasks' at line 47"

# User-friendly
detail="An internal error occurred. Please try again."
```

## Common Mistakes

**Mistake 1**: Forgetting to raise the exception

```python
# Wrong - creates exception but doesn't raise it
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if not find_task(task_id):
        HTTPException(status_code=404, detail="Not found")  # Does nothing!
    return task

# Correct - raise the exception
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if not find_task(task_id):
        raise HTTPException(status_code=404, detail="Not found")
    return task
```

**Mistake 2**: Using wrong status code

```python
# Wrong - 200 for missing resource
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        return {"error": "Not found"}  # Still 200!

# Correct - 404 for missing
raise HTTPException(status_code=404, detail="Not found")
```

**Mistake 3**: Mixing exception types

```python
# Wrong - raises Python exception, becomes 500
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise ValueError("Not found")  # 500 Internal Server Error

# Correct - use HTTPException for HTTP errors
raise HTTPException(status_code=404, detail="Not found")
```

## Try With AI

**Understand Error Categories:**

> "Explain the difference between 4xx and 5xx errors. Give me examples of when a task API would return each category."

**Design Error Responses:**

> "I want to include an error code alongside the detail message, like {'detail': '...', 'code': 'TASK_NOT_FOUND'}. How do I customize FastAPI's error response format?"

**Handle Edge Cases:**

> "What should happen if a client sends a task ID that's negative? Or a task ID that's larger than what a 32-bit integer can hold? Show me how to handle these."

**Add Logging:**

> "I want to log all 4xx and 5xx errors. Show me how to add error logging to my FastAPI application."

---

## Summary

You've learned to handle errors properly:

- **Status codes**: 200, 201, 400, 404, 422 for different scenarios
- **HTTPException**: Raise with status_code and detail
- **status module**: Named constants for readability
- **400 vs 422**: Business rules vs validation errors
- **Good messages**: Specific, contextual, user-friendly

Next lesson, you'll learn dependency injection to organize your code better and prepare for testing.
