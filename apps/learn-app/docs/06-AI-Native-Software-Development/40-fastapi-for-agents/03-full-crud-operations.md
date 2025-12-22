---
title: "Full CRUD Operations"
sidebar_position: 3
chapter: 40
lesson: 3
duration_minutes: 55

skills:
  - name: "HTTP Method Semantics"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student explains when to use GET, POST, PUT, DELETE"

  - name: "CRUD Implementation"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student implements all four CRUD operations"

  - name: "Resource Lookup Patterns"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student finds resources by ID and handles not-found cases"

learning_objectives:
  - objective: "Implement GET endpoints for listing and retrieving resources"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "GET /tasks returns all tasks; GET /tasks/{id} returns one"

  - objective: "Implement PUT endpoint for updating resources"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "PUT /tasks/{id} updates and returns the task"

  - objective: "Implement DELETE endpoint for removing resources"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "DELETE /tasks/{id} removes task and returns confirmation"

cognitive_load:
  new_concepts: 4
  assessment: "GET list, GET single, PUT, DELETE - building on POST from previous lesson"

differentiation:
  extension_for_advanced: "Add PATCH for partial updates; implement bulk operations"
  remedial_for_struggling: "Focus on GET operations before moving to PUT and DELETE"

generated_by: "content-implementer"
source_spec: "specs/040-chapter-40-fastapi-for-agents/spec.md"
created: "2025-12-22"
---

# Full CRUD Operations

You can create tasks with POST. Now you'll complete the picture with Read, Update, and Delete operations. Together, these four operations—Create, Read, Update, Delete—form CRUD, the foundation of most APIs.

## HTTP Methods and CRUD

Each CRUD operation maps to an HTTP method:

| Operation | HTTP Method | Endpoint Example | Description |
|-----------|-------------|------------------|-------------|
| Create | POST | POST /tasks | Create a new task |
| Read (all) | GET | GET /tasks | List all tasks |
| Read (one) | GET | GET /tasks/1 | Get task with ID 1 |
| Update | PUT | PUT /tasks/1 | Update task with ID 1 |
| Delete | DELETE | DELETE /tasks/1 | Delete task with ID 1 |

Let's implement each one.

## List All Tasks

The simplest read operation—return everything:

```python
@app.get("/tasks")
def list_tasks():
    return tasks
```

But we can make it more useful with filtering:

```python
@app.get("/tasks")
def list_tasks(status: str | None = None):
    if status:
        return [t for t in tasks if t["status"] == status]
    return tasks
```

Now clients can:
- `GET /tasks` — All tasks
- `GET /tasks?status=pending` — Only pending tasks
- `GET /tasks?status=completed` — Only completed tasks

## Get Single Task

Retrieve one task by ID:

```python
from fastapi import HTTPException

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
```

When the task doesn't exist, we raise an `HTTPException` with a 404 status code. This is the standard HTTP response for "resource not found."

Test it:
- `GET /tasks/1` → Returns task 1 (if it exists)
- `GET /tasks/999` → Returns 404 error

## Update Task

PUT replaces the entire resource. The client sends the new version, and we swap it in:

```python
class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = None

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_update.title
            if task_update.description is not None:
                task["description"] = task_update.description
            if task_update.status is not None:
                task["status"] = task_update.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")
```

We created a new model `TaskUpdate` that allows updating status (which `TaskCreate` doesn't). The client sends:

```json
{
  "title": "Updated title",
  "description": "New description",
  "status": "completed"
}
```

And receives the updated task back.

## Delete Task

Remove a task from our list:

```python
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return {"message": "Task deleted", "id": task_id}
    raise HTTPException(status_code=404, detail="Task not found")
```

Some APIs return 204 No Content for deletes. We're returning a confirmation message, which is helpful for debugging.

## Complete Implementation

Here's the full `main.py` with all CRUD operations:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")

# Models
class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    status: str | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    status: str

# Storage
tasks: list[dict] = []

# CREATE
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

# READ (all)
@app.get("/tasks")
def list_tasks(status: str | None = None):
    if status:
        return [t for t in tasks if t["status"] == status]
    return tasks

# READ (one)
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# UPDATE
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_update.title
            if task_update.description is not None:
                task["description"] = task_update.description
            if task_update.status is not None:
                task["status"] = task_update.status
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# DELETE
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return {"message": "Task deleted", "id": task_id}
    raise HTTPException(status_code=404, detail="Task not found")
```

## Hands-On Exercise

Test the complete CRUD cycle in Swagger UI:

**Step 1: Create Tasks**
```bash
POST /tasks
{"title": "Learn CRUD", "description": "Complete this lesson"}

POST /tasks
{"title": "Build API", "description": "Create a complete REST API"}

POST /tasks
{"title": "Test API", "description": "Verify all endpoints work"}
```

**Step 2: List and Filter**
```bash
GET /tasks           # See all 3 tasks
GET /tasks?status=pending  # All should be pending
```

**Step 3: Read Single**
```bash
GET /tasks/1         # First task
GET /tasks/999       # Should return 404
```

**Step 4: Update**
```bash
PUT /tasks/1
{"title": "Learn CRUD", "status": "completed"}
```

**Step 5: Verify Update**
```bash
GET /tasks/1         # Status should be "completed"
GET /tasks?status=completed  # Should show task 1
GET /tasks?status=pending    # Should show tasks 2 and 3
```

**Step 6: Delete**
```bash
DELETE /tasks/3      # Delete task 3
GET /tasks           # Should only show tasks 1 and 2
```

## ID Generation Pattern

Notice our ID generation has a flaw:

```python
"id": len(tasks) + 1
```

If you create tasks 1, 2, 3, then delete task 2 and create a new one, you get:
- Task 1
- Task 3
- Task 3 (duplicate!)

A better approach uses a counter:

```python
task_counter = 0

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    global task_counter
    task_counter += 1
    new_task = {
        "id": task_counter,
        "title": task.title,
        "description": task.description,
        "status": "pending"
    }
    tasks.append(new_task)
    return new_task
```

Now IDs are always unique. In production, databases handle this automatically.

## Common Mistakes

**Mistake 1**: Not returning the updated resource

```python
# Wrong - returns nothing useful
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_update.title
            return {"message": "Updated"}  # Client doesn't know the new state

# Correct - return the updated resource
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = task_update.title
            return task  # Client sees the result
```

**Mistake 2**: Using wrong HTTP method

```python
# Wrong - POST shouldn't be used for updates
@app.post("/tasks/{task_id}/update")

# Correct - PUT for updates
@app.put("/tasks/{task_id}")

# Wrong - GET with side effects
@app.get("/tasks/{task_id}/delete")

# Correct - DELETE for deletion
@app.delete("/tasks/{task_id}")
```

**Mistake 3**: Not handling not-found cases

```python
# Wrong - returns None, causes errors
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    # Falls through, returns None

# Correct - explicit 404
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
```

## Try With AI

**Understand CRUD Patterns:**

> "Explain the difference between PUT and PATCH for updates. When would I use each? Show me how PATCH would look for partial task updates."

**Improve the Implementation:**

> "My current implementation loops through the list to find tasks. What's the time complexity? How would you improve this with a dictionary?"

**Handle Edge Cases:**

> "What happens if two clients try to update the same task at the same time? Explain the race condition and how production systems handle this."

**Extend Functionality:**

> "Add a 'completed_at' timestamp that's automatically set when status changes to 'completed'. Show me the code."

---

## Summary

You've implemented complete CRUD operations:

- **Create**: `POST /tasks` with request body
- **Read all**: `GET /tasks` with optional filtering
- **Read one**: `GET /tasks/{id}` with 404 for missing
- **Update**: `PUT /tasks/{id}` returns updated resource
- **Delete**: `DELETE /tasks/{id}` removes resource

Next lesson, you'll learn proper error handling with HTTP status codes and custom exceptions.
