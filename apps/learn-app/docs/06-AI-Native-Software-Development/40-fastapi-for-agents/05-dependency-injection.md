---
title: "Dependency Injection"
sidebar_position: 5
chapter: 40
lesson: 5
duration_minutes: 50

skills:
  - name: "Dependency Injection Pattern"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student explains why DI improves code organization"

  - name: "FastAPI Depends Usage"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student uses Depends() to inject dependencies"

  - name: "Repository Pattern"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "Software Development"
    measurable_at_this_level: "Student creates repository class for data access"

learning_objectives:
  - objective: "Explain the benefits of dependency injection"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student articulates why global state is problematic"

  - objective: "Use Depends() to inject shared resources"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Endpoints receive TaskRepository via Depends()"

  - objective: "Implement the repository pattern for data access"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "TaskRepository encapsulates all data operations"

cognitive_load:
  new_concepts: 4
  assessment: "Depends(), dependency functions, repository class, lifecycle"

differentiation:
  extension_for_advanced: "Implement async dependencies; explore dependency overrides for testing"
  remedial_for_struggling: "Focus on simple Depends() usage before repository pattern"

generated_by: "content-implementer"
source_spec: "specs/040-chapter-40-fastapi-for-agents/spec.md"
created: "2025-12-22"
---

# Dependency Injection

Our current code uses a global list for storage. This works, but it's messy—storage logic is scattered across endpoints, and testing is hard. Dependency injection solves this by making dependencies explicit and replaceable.

## The Problem with Global State

Look at our current code:

```python
# Global state
tasks: list[dict] = []
task_counter = 0

@app.post("/tasks")
def create_task(task: TaskCreate):
    global task_counter  # Modifying global state
    task_counter += 1
    new_task = {"id": task_counter, ...}
    tasks.append(new_task)  # Using global list
    return new_task
```

Problems with this approach:
1. **Hard to test** — Can't easily swap the storage for tests
2. **Hard to maintain** — Logic for finding/updating tasks is in every endpoint
3. **Hidden dependencies** — You have to read the code to know what it needs
4. **Concurrency issues** — Global state can cause race conditions

## What is Dependency Injection?

Instead of reaching for global state, we declare what we need:

```python
@app.get("/tasks")
def list_tasks(repo: TaskRepository = Depends(get_task_repo)):
    return repo.get_all()
```

Now:
- The dependency is explicit (we need a `TaskRepository`)
- FastAPI provides it automatically
- We can swap it for testing
- The endpoint is focused on its job

## The Repository Pattern

A repository encapsulates all data access logic. Create `repository.py`:

```python
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskRepository:
    """Manages task storage and operations."""

    def __init__(self):
        self.tasks: list[dict] = []
        self.counter = 0

    def create(self, task: TaskCreate) -> dict:
        """Create a new task and return it."""
        self.counter += 1
        new_task = {
            "id": self.counter,
            "title": task.title,
            "description": task.description,
            "status": "pending"
        }
        self.tasks.append(new_task)
        return new_task

    def get_all(self, status: str | None = None) -> list[dict]:
        """Get all tasks, optionally filtered by status."""
        if status:
            return [t for t in self.tasks if t["status"] == status]
        return self.tasks

    def get_by_id(self, task_id: int) -> dict | None:
        """Get a single task by ID, or None if not found."""
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def update(self, task_id: int, title: str,
               description: str | None = None,
               status: str | None = None) -> dict | None:
        """Update a task and return it, or None if not found."""
        task = self.get_by_id(task_id)
        if not task:
            return None

        task["title"] = title
        if description is not None:
            task["description"] = description
        if status is not None:
            task["status"] = status
        return task

    def delete(self, task_id: int) -> bool:
        """Delete a task. Returns True if deleted, False if not found."""
        task = self.get_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
```

All data operations are now in one place. The endpoints just call repository methods.

## Using Depends()

FastAPI's `Depends()` function injects dependencies into your endpoints:

```python
from fastapi import Depends

# Create a singleton instance
task_repo = TaskRepository()

# Dependency function
def get_task_repo() -> TaskRepository:
    return task_repo

# Use it in endpoints
@app.get("/tasks")
def list_tasks(repo: TaskRepository = Depends(get_task_repo)):
    return repo.get_all()
```

Here's what happens:
1. FastAPI sees `Depends(get_task_repo)`
2. It calls `get_task_repo()` to get the repository
3. It passes the repository to your function
4. Your function uses it

## Complete Refactored Example

**repository.py**:
```python
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    status: str | None = None

class TaskRepository:
    def __init__(self):
        self.tasks: list[dict] = []
        self.counter = 0

    def create(self, task: TaskCreate) -> dict:
        self.counter += 1
        new_task = {
            "id": self.counter,
            "title": task.title,
            "description": task.description,
            "status": "pending"
        }
        self.tasks.append(new_task)
        return new_task

    def get_all(self, status: str | None = None) -> list[dict]:
        if status:
            return [t for t in self.tasks if t["status"] == status]
        return self.tasks

    def get_by_id(self, task_id: int) -> dict | None:
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def update(self, task_id: int, update: TaskUpdate) -> dict | None:
        task = self.get_by_id(task_id)
        if not task:
            return None
        task["title"] = update.title
        if update.description is not None:
            task["description"] = update.description
        if update.status is not None:
            task["status"] = update.status
        return task

    def delete(self, task_id: int) -> bool:
        task = self.get_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

# Singleton instance
task_repo = TaskRepository()

def get_task_repo() -> TaskRepository:
    """Dependency function for injecting TaskRepository."""
    return task_repo
```

**main.py**:
```python
from fastapi import FastAPI, Depends, HTTPException, status

from repository import (
    TaskCreate, TaskUpdate, TaskRepository, get_task_repo
)

app = FastAPI(title="Task API")

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(
    task: TaskCreate,
    repo: TaskRepository = Depends(get_task_repo)
):
    if not task.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty"
        )
    return repo.create(task)

@app.get("/tasks")
def list_tasks(
    status_filter: str | None = None,
    repo: TaskRepository = Depends(get_task_repo)
):
    return repo.get_all(status=status_filter)

@app.get("/tasks/{task_id}")
def get_task(
    task_id: int,
    repo: TaskRepository = Depends(get_task_repo)
):
    task = repo.get_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task

@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    repo: TaskRepository = Depends(get_task_repo)
):
    if not task_update.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title cannot be empty"
        )
    task = repo.update(task_id, task_update)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task

@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    repo: TaskRepository = Depends(get_task_repo)
):
    if not repo.delete(task_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return {"message": "Task deleted", "id": task_id}
```

Notice how clean the endpoints are now. Each one:
1. Receives the repository as a parameter
2. Validates business rules
3. Calls repository methods
4. Handles errors

## Hands-On Exercise

Refactor your code to use dependency injection:

**Step 1**: Create `repository.py` with the `TaskRepository` class

**Step 2**: Move the dependency function to the repository file

**Step 3**: Update `main.py` to use `Depends()`

**Step 4**: Test in Swagger UI — everything should work exactly as before

**Verification Checklist**:
- [ ] No global `tasks` list in `main.py`
- [ ] No `global` keyword anywhere
- [ ] Every endpoint receives `repo` via `Depends()`
- [ ] All CRUD operations work

## Why This Matters

**For Testing**: You can override dependencies to use a fake repository:

```python
# In tests
def get_test_repo():
    return TestTaskRepository()

app.dependency_overrides[get_task_repo] = get_test_repo
```

**For Flexibility**: Swap implementations without changing endpoints:

```python
# Today: in-memory
def get_task_repo():
    return InMemoryTaskRepository()

# Tomorrow: database
def get_task_repo():
    return PostgresTaskRepository(connection)
```

**For Clarity**: Dependencies are visible in the function signature:

```python
# Before: What does this need? Check the function body
def create_task(task: TaskCreate):
    ...

# After: Clear from the signature
def create_task(task: TaskCreate, repo: TaskRepository = Depends(get_task_repo)):
    ...
```

## Common Mistakes

**Mistake 1**: Calling the dependency function instead of using Depends

```python
# Wrong - creates new repo each time, not shared
@app.get("/tasks")
def list_tasks(repo: TaskRepository = get_task_repo()):
    return repo.get_all()

# Correct - FastAPI calls it once and caches per request
@app.get("/tasks")
def list_tasks(repo: TaskRepository = Depends(get_task_repo)):
    return repo.get_all()
```

**Mistake 2**: Creating the instance inside the dependency function

```python
# Wrong - creates new repository on every request
def get_task_repo():
    return TaskRepository()  # Fresh instance each time!

# Correct - use a singleton
task_repo = TaskRepository()

def get_task_repo():
    return task_repo  # Same instance each time
```

**Mistake 3**: Accessing repository directly instead of through dependency

```python
# Wrong - bypasses dependency injection
@app.get("/tasks")
def list_tasks():
    return task_repo.get_all()  # Direct access

# Correct - goes through DI
@app.get("/tasks")
def list_tasks(repo: TaskRepository = Depends(get_task_repo)):
    return repo.get_all()
```

## Try With AI

**Understand the Pattern:**

> "Explain dependency injection like I'm new to programming. Use a restaurant analogy where chefs don't go shopping for ingredients."

**Explore Testing Benefits:**

> "Show me how to write a test for the create_task endpoint using dependency overrides. Use pytest and a fake repository."

**Advanced Patterns:**

> "I want my repository to be async. How do I create an async dependency in FastAPI? Show me with the TaskRepository."

**Extend the Design:**

> "Add a 'priority' field to tasks. Show me how to modify the TaskRepository to support filtering by both status and priority."

---

## Summary

You've learned to organize code with dependency injection:

- **Depends()**: Declares what your endpoint needs
- **Repository pattern**: Encapsulates data access
- **Singleton pattern**: Shared instance across requests
- **Clean endpoints**: Focused on business logic, not data access

Next lesson, you'll add streaming responses with Server-Sent Events for real-time updates.
