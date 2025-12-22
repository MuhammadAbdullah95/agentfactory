---
sidebar_position: 8
chapter: 49
lesson: 8
duration_minutes: 60
title: "Volumes and Persistent Data"
proficiency_level: B1
teaching_stage: 1
stage_name: "Manual Foundation"
stage_description: "Docker storage mechanisms for persistent data, teaching volume types and lifecycle management through hands-on practice"
cognitive_load:
  concepts_count: 8
  scaffolding_level: "Moderate"
learning_objectives:
  - id: LO1
    description: "Explain why containers are ephemeral and why persistent data requires volumes"
    bloom_level: "Understand"
  - id: LO2
    description: "Create and manage named volumes using Docker commands"
    bloom_level: "Apply"
  - id: LO3
    description: "Compare named volumes, bind mounts, and tmpfs mounts with appropriate use cases"
    bloom_level: "Analyze"
  - id: LO4
    description: "Configure bind mounts for development workflows"
    bloom_level: "Apply"
  - id: LO5
    description: "Use tmpfs mounts for sensitive data that shouldn't persist"
    bloom_level: "Apply"
  - id: LO6
    description: "Design storage patterns for AI services (models, databases, logs)"
    bloom_level: "Create"
  - id: LO7
    description: "Manage volume lifecycle (creation, inspection, cleanup, pruning)"
    bloom_level: "Apply"
  - id: LO8
    description: "Choose between development and production volume strategies"
    bloom_level: "Evaluate"
digcomp_mapping:
  - objective_id: LO2
    competency_area: "3. Digital Content Creation"
    competency: "3.4 Programming"
  - objective_id: LO6
    competency_area: "2. Digital Communication and Collaboration"
    competency: "2.1 Problem Solving"
---

# Volumes and Persistent Data

Containers are designed to be ephemeral—temporary, reproducible, disposable. This is their strength: spin up 100 identical containers, tear them all down, no cleanup required. But this design creates a problem for data. When you delete a container, everything inside it vanishes.

This is fine for stateless services (web servers, API endpoints). They don't care about previous requests. But AI services? They need to persist models, vector databases, training checkpoints, logs. A machine learning service that loses its embeddings database every time it restarts is useless.

This lesson teaches you how to decouple data from containers using volumes. You'll learn three mechanisms for persistent storage, understand when to use each, and practice designing storage patterns for the kinds of services you'll build throughout this book.

---

## The Ephemeral Container Problem

Let's start with a concrete demonstration. Create a container that writes data to disk, verify the data exists, then remove the container and see what happens.

**File: app.py**
```python
import os
from datetime import datetime

# Write to container filesystem
data_dir = "/app/data"
os.makedirs(data_dir, exist_ok=True)

with open(f"{data_dir}/log.txt", "a") as f:
    f.write(f"Container started: {datetime.now()}\n")

# Read back what we wrote
with open(f"{data_dir}/log.txt", "r") as f:
    print(f.read())
```

**File: Dockerfile**
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```

Build and run the container:

```bash
docker build -t ephemeral-demo:latest .
docker run --name my-container ephemeral-demo:latest
```

**Output:**
```
Container started: 2025-12-23 14:32:15.842901
```

Now inspect the container's filesystem to see the log file that was created:

```bash
docker exec my-container cat /app/data/log.txt
```

**Output:**
```
Container started: 2025-12-23 14:32:15.842901
```

The file exists. Now remove the container:

```bash
docker rm my-container
```

And try to read the file from a new container:

```bash
docker run --name my-container ephemeral-demo:latest
docker exec my-container cat /app/data/log.txt 2>&1 || echo "File not found"
```

**Output:**
```
cat: /app/data/log.txt: No such file or directory
File not found
```

**Why?** Each container gets a fresh filesystem isolated from all others. The data from the first container is gone—it was stored in the container layer, which was deleted when the container was removed.

---

## The Three Storage Mechanisms

Docker provides three ways to attach storage to containers. Each solves a different problem:

### 1. Named Volumes (Docker-Managed Persistence)

**What it is**: A storage mechanism managed entirely by Docker. You create a volume using Docker commands, Docker stores it on the host machine, and Docker handles all the details.

**Best for**: Production data that needs persistence but shouldn't be directly edited on the host filesystem.

**Ephemeral container problem solved**: Data survives container deletion because Docker manages the volume separately.

### 2. Bind Mounts (Host Directory Binding)

**What it is**: A direct mapping from a directory on your host machine to a path inside the container. Changes on the host appear immediately inside the container, and vice versa.

**Best for**: Development workflows where you edit code on your machine and want to see changes reflected instantly in the running container.

**Ephemeral container problem solved**: Data exists on your host filesystem, not in the container.

### 3. tmpfs Mounts (Memory-Only Storage)

**What it is**: A filesystem that exists only in RAM. Data is never written to disk.

**Best for**: Sensitive data that shouldn't persist to disk (passwords, API keys, temporary computation data).

**Ephemeral container problem solved**: Data is explicitly NOT persisted; when the container stops, the data is safely purged from memory.

---

## Named Volumes: Docker-Managed Persistence

Named volumes are the recommended approach for production services. Docker creates them, stores them, and manages their lifecycle.

### Creating Named Volumes

First, create a named volume:

```bash
docker volume create my-data
```

**Output:**
```
my-data
```

Verify the volume exists:

```bash
docker volume ls
```

**Output:**
```
DRIVER    VOLUME NAME
local     my-data
```

Get detailed information about the volume:

```bash
docker volume inspect my-data
```

**Output:**
```json
[
    {
        "CreatedAt": "2025-12-23T14:35:22Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/my-data/_data",
        "Name": "my-data",
        "Options": {},
        "Scope": "local"
    }
]
```

The `Mountpoint` shows where Docker stores the volume on your host machine. (On Docker Desktop for Mac/Windows, this is inside the VM—you can't directly access it from your machine.)

### Attaching Volumes to Containers

Run a container with the named volume attached:

```bash
docker run -it --name test-container -v my-data:/app/data python:3.12-slim bash
```

Inside the container, write some data:

```bash
echo "Important data" > /app/data/important.txt
exit
```

**Output:**
```
root@abc123:/# echo "Important data" > /app/data/important.txt
root@abc123:/# exit
```

Now delete the container and verify the data persists:

```bash
docker rm test-container
docker run -it --name new-container -v my-data:/app/data python:3.12-slim bash
cat /app/data/important.txt
exit
```

**Output:**
```
Important data
```

The data survived container deletion because it's stored in the named volume, not in the container's filesystem.

### Volume Lifecycle Commands

List all volumes:

```bash
docker volume ls
```

**Output:**
```
DRIVER    VOLUME NAME
local     my-data
```

Remove a specific volume:

```bash
docker volume rm my-data
```

**Output:**
```
my-data
```

(Note: You can only remove a volume if no containers are using it.)

Remove all unused volumes:

```bash
docker volume prune
```

**Output:**
```
WARNING! This will remove all local volumes not used by at least one container.
Are you sure you want to continue? [y/N] y
Deleted Volumes:
my-data

Total reclaimed space: 124MB
```

---

## Bind Mounts: Direct Host-to-Container Mapping

Bind mounts connect a directory on your host machine directly to a path in the container. This is essential for development because it lets you edit code on your machine and see changes instantly in the running container.

### Setting Up a Bind Mount

Create a directory on your host machine with some code:

```bash
mkdir -p ~/project-data
echo "print('Hello from file')" > ~/project-data/hello.py
```

Run a container with a bind mount:

```bash
docker run -it --name dev-container -v ~/project-data:/app python:3.12-slim bash
```

Inside the container, verify the file exists:

```bash
cat /app/hello.py
exit
```

**Output:**
```
print('Hello from file')
```

Now edit the file on your host machine:

```bash
echo "print('Updated from host')" > ~/project-data/hello.py
```

Run the container again and see the change:

```bash
docker run -it --name dev-container2 -v ~/project-data:/app python:3.12-slim bash
cat /app/hello.py
exit
```

**Output:**
```
print('Updated from host')
```

Changes on the host are immediately visible in the container.

### Bind Mounts in docker-compose

This is where bind mounts shine. In `docker-compose.yaml`, map your local source code directory to the container:

**File: docker-compose.yaml**
```yaml
version: '3.8'

services:
  app:
    build: .
    volumes:
      - ./src:/app/src          # Host directory ./src → Container /app/src
      - ./data:/app/data        # Host directory ./data → Container /app/data
    ports:
      - "8000:8000"
    environment:
      - DEBUG=true
```

Run the service:

```bash
docker-compose up
```

**Output:**
```
Starting app ... done
Attaching to my_app_1
app_1  | INFO: Uvicorn running on 0.0.0.0:8000
```

Edit a file in your `./src` directory on your host machine. The change is immediately available in the running container (if your application reloads on file changes).

### Read-Only Bind Mounts

Sometimes you want to mount data into a container but prevent the container from modifying it. Use the `:ro` (read-only) flag:

```bash
docker run -v ~/config.json:/app/config.json:ro myimage:latest
```

The container can read `/app/config.json` but cannot write to it.

---

## tmpfs Mounts: Memory-Only, No Persistence

tmpfs mounts store data only in RAM. The moment a container stops, all tmpfs data is purged from memory. This is useful for sensitive data that should never touch the disk.

### Use Case: Secrets in Memory

Many systems store secrets (API keys, credentials) in temporary files. With tmpfs, these files exist only in RAM:

```bash
docker run -it \
  --tmpfs /run/secrets \
  python:3.12-slim bash
```

Inside the container, write a secret to the tmpfs mount:

```bash
echo "secret-api-key-12345" > /run/secrets/api_key.txt
cat /run/secrets/api_key.txt
```

**Output:**
```
secret-api-key-12345
```

Exit the container and verify: even if you could access the container's filesystem, the tmpfs data is gone. It was only in memory.

### Configuring tmpfs Size

By default, tmpfs can use up to 50% of your host's RAM. Limit it explicitly:

```bash
docker run -it \
  --tmpfs /run/secrets:size=1m \
  python:3.12-slim bash
```

This creates a tmpfs mount of exactly 1MB. Attempting to write more than 1MB will fail.

---

## Storage Patterns for AI Services

AI services have unique storage needs. Let's design patterns for the most common scenarios.

### Pattern 1: Large Model Files

Problem: An embedding model is 2GB. You don't want to embed it in the Docker image.

Solution: Mount a named volume for models, copied from the host before container startup.

**File: Dockerfile**
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Models come via volume mount, not COPY
# COPY models /app/models  <<-- DON'T do this

EXPOSE 8000
CMD ["python", "app.py"]
```

**File: docker-compose.yaml**
```yaml
version: '3.8'

services:
  embedding-service:
    build: .
    volumes:
      - models-volume:/app/models    # Named volume for 2GB model
      - ./logs:/app/logs             # Bind mount for logs
    ports:
      - "8000:8000"
    environment:
      - MODEL_PATH=/app/models/embedding-model.bin

volumes:
  models-volume:
    driver: local
```

First-time setup (load the model):

```bash
# Copy model from wherever you downloaded it
cp ~/downloads/embedding-model.bin $(docker volume inspect models-volume --format '{{ .Mountpoint }}')/

# Start the service
docker-compose up
```

**Output:**
```
Creating app ... done
Attaching to app_embedding-service_1
embedding-service_1  | Model loaded from /app/models/embedding-model.bin
```

Subsequent runs use the cached model—no re-download, no rebuild.

### Pattern 2: Vector Database Persistence

Problem: You're running a Qdrant vector database in a container. The embeddings must survive container restarts.

Solution: Mount a named volume to Qdrant's data directory.

**File: docker-compose.yaml**
```yaml
version: '3.8'

services:
  qdrant:
    image: qdrant/qdrant:latest
    volumes:
      - qdrant-storage:/qdrant/storage    # Named volume for vector DB
      - qdrant-snapshots:/qdrant/snapshots
    ports:
      - "6333:6333"
    environment:
      - QDRANT_API_KEY=your-secure-key

volumes:
  qdrant-storage:
    driver: local
  qdrant-snapshots:
    driver: local
```

Start Qdrant:

```bash
docker-compose up
```

**Output:**
```
Qdrant server started on 0.0.0.0:6333
```

Add some vectors, then restart the service:

```bash
curl -X POST http://localhost:6333/collections/documents/points \
  -H "Content-Type: application/json" \
  -H "api-key: your-secure-key" \
  -d '{"points": [{"id": 1, "vector": [0.1, 0.2]}]}'
```

Stop and restart:

```bash
docker-compose down
docker-compose up
```

**Output:**
```
Qdrant server started on 0.0.0.0:6333
[Loaded previous collection from volume]
```

The vectors persist across restarts because they're in the named volume.

### Pattern 3: Development with Hot Reload

Problem: You're developing a FastAPI agent service and want instant feedback when you change code.

Solution: Bind mount your source directory and use a development server that reloads on file changes.

**File: app.py**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, developer!"}
```

**File: Dockerfile**
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Source code comes via bind mount in development
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]
```

**File: docker-compose.yaml**
```yaml
version: '3.8'

services:
  api:
    build: .
    volumes:
      - ./src:/app                   # Bind mount for instant hot reload
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
```

Start the service:

```bash
docker-compose up
```

**Output:**
```
INFO: Uvicorn running on 0.0.0.0:8000
INFO: Application startup complete
```

Edit `app.py` on your host machine:

```python
@app.get("/")
def read_root():
    return {"message": "Updated message!"}
```

The service automatically detects the file change and reloads. No container restart needed.

### Pattern 4: Logs That Survive Container Restarts

Problem: You want to collect logs across multiple container runs into a single file.

Solution: Bind mount a logs directory from the host.

**File: docker-compose.yaml**
```yaml
version: '3.8'

services:
  ai-service:
    build: .
    volumes:
      - ./logs:/app/logs             # Host logs directory
    ports:
      - "8000:8000"
```

**File: app.py**
```python
import logging

logging.basicConfig(
    filename="/app/logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

logger.info("Service started")
```

Start, stop, restart:

```bash
docker-compose up       # Logs written to host ./logs/app.log
docker-compose down
docker-compose up       # More logs appended to same file
```

Check the logs on your host:

```bash
cat logs/app.log
```

**Output:**
```
2025-12-23 14:42:10,123 - INFO - Service started
2025-12-23 14:42:45,456 - INFO - Service started
```

Logs from multiple container runs are consolidated in one file because they're stored on the host filesystem.

---

## Development vs Production: Storage Strategy

The storage patterns you choose differ between development and production:

### Development Environment

**Goal**: Rapid iteration, visibility into internals, ease of debugging

**Volume strategy**:
- **Source code**: Bind mount (edit locally, see changes instantly)
- **Data**: Named volumes (but mount them in separate containers for inspection)
- **Logs**: Bind mount (inspect on host, persist across restarts)
- **Secrets**: Environment variables or tmpfs (not committed to git)

**Example**:
```yaml
services:
  app:
    build: .
    volumes:
      - ./src:/app           # Bind: hot reload
      - ./logs:/app/logs     # Bind: inspect logs locally
      - dev-data:/data       # Named: persist data
```

### Production Environment

**Goal**: Security, reliability, immutability, performance

**Volume strategy**:
- **Source code**: Immutable image layer (no bind mounts; code is frozen at build time)
- **Data**: Named volumes with explicit backup policies
- **Logs**: Shipped to centralized logging service (not local filesystem)
- **Secrets**: Kubernetes Secrets, cloud secret management, or secure environment variables (never raw files)

**Example**:
```yaml
services:
  app:
    image: myregistry.azurecr.io/app:v1.2.3  # Immutable image
    volumes:
      - prod-data:/data      # Named: managed by infrastructure
      # No bind mounts!
      # No local logging!
```

---

## Volume Drivers and Storage Plugins

Docker's default volume driver is `local`, which stores data on the host machine. For advanced scenarios, other drivers exist:

| Driver | Purpose | Use Case |
|--------|---------|----------|
| **local** | Host machine storage | Default, works everywhere |
| **nfs** | Network file system | Shared storage across hosts |
| **smb** | Windows file shares | Enterprise environments |
| **aws-ec2** | AWS EBS volumes | Cloud deployments |
| **gce-docker** | Google Cloud persistent disks | Google Cloud deployments |
| **azure** | Azure storage | Microsoft Azure |

For this course, you'll use the default `local` driver. Cloud-specific drivers come into play when deploying to Kubernetes in the next chapter.

---

## Practice: Design Storage for Your AI Service

You now understand the three storage mechanisms. Here's a practical exercise:

### Scenario: Building an Embeddings Service

Your service:
- Needs to load a 3GB embedding model (BERT or similar)
- Generates embeddings and stores them in a Qdrant vector DB
- Logs all requests to a file
- Runs in development on your laptop, production in Kubernetes

### Design Challenge

For each storage need, decide:
1. Volume type (named volume, bind mount, or tmpfs)?
2. Why that choice?
3. Different strategy for development vs production?

**Model files** (3GB embedding model):
- Development: Named volume (mount from host, avoid rebuilding image)
- Production: Cloud storage (S3, Azure Blob) mounted at runtime

**Vector DB** (Qdrant collection):
- Development: Named volume (persist across restarts)
- Production: Kubernetes PersistentVolumeClaim (managed by infrastructure)

**Request logs**:
- Development: Bind mount (inspect on host, persist across runs)
- Production: stdout (collected by Kubernetes logging) or cloud logging service

**API keys**:
- Development: Environment variables in `.env` (not version controlled)
- Production: Kubernetes Secrets or HashiCorp Vault

---

## Common Volume Commands Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `docker volume create` | Create a named volume | `docker volume create my-data` |
| `docker volume ls` | List all volumes | `docker volume ls` |
| `docker volume inspect` | Show volume details | `docker volume inspect my-data` |
| `docker volume rm` | Delete a volume | `docker volume rm my-data` |
| `docker volume prune` | Delete unused volumes | `docker volume prune` |
| `-v named:/path` | Attach named volume | `docker run -v my-data:/app/data` |
| `-v /host:/path` | Bind mount | `docker run -v ~/code:/app` |
| `-v /path:ro` | Read-only mount | `docker run -v ~/config.json:/app/config.json:ro` |
| `--tmpfs /path` | tmpfs mount | `docker run --tmpfs /run/secrets` |
| `--tmpfs /path:size=1m` | tmpfs with size limit | `docker run --tmpfs /tmp:size=512m` |

---

## Try With AI

**Setup**: You have the embedding model and Qdrant database setup from Pattern 2. Now you'll design storage configuration for a new AI service that combines both.

**Part 1: Initial Configuration Request**

Ask AI: "I'm building a semantic search service that combines a 2GB embedding model with a Qdrant vector database. I also need to log all searches for analytics. Design a docker-compose.yaml that handles storage for development and production. What volumes should I use for each component?"

**Part 2: Critical Evaluation**

Review AI's response. Ask yourself:

- Does it use named volumes for persistent data (models, vectors)?
- Does it propose bind mounts for development but immutable images for production?
- Are logs handled differently for development vs production?
- Are secrets handled securely (not hardcoded)?

**Part 3: Development Optimization**

Tell AI: "For development, I also need hot reload when I edit the search algorithm code. Update the docker-compose.yaml to bind mount the source code directory."

**Part 4: Size and Performance Validation**

Ask AI to validate: "What's the maximum size of embeddings data we could store with this approach? If our vector collection grows to 10GB, what changes would we need to make?"

**Part 5: Final Check**

Compare your original requirements to the final configuration:

- Can you develop locally with instant feedback (hot reload)?
- Will data persist across service restarts?
- Does the production configuration avoid bind mounts?
- Are sensitive values (API keys, database passwords) handled securely?
- Is the setup ready to deploy to Kubernetes in the next chapter?
