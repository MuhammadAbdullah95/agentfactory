---
sidebar_position: 7
chapter: 49
lesson: 7
duration_minutes: 50
title: "Container-to-Container Communication"
proficiency_level: B1
teaching_stage: 1
stage_name: "Manual Foundation"
stage_description: "Network-based container communication through manual bridge networks and DNS"
cognitive_load:
  concepts_count: 6
  scaffolding_level: "Moderate"
learning_objectives:
  - id: LO1
    description: "Create user-defined bridge networks with docker network create"
    bloom_level: "Apply"
  - id: LO2
    description: "Connect containers to custom networks and isolate communication"
    bloom_level: "Apply"
  - id: LO3
    description: "Explain automatic DNS service discovery by container name"
    bloom_level: "Understand"
  - id: LO4
    description: "Demonstrate network isolation between containers on different networks"
    bloom_level: "Analyze"
  - id: LO5
    description: "Manage container network connectivity at runtime using docker network connect/disconnect"
    bloom_level: "Apply"
  - id: LO6
    description: "Build multi-container AI services with agent, database, and cache layers"
    bloom_level: "Create"
digcomp_mapping:
  - objective_id: LO1
    competency_area: "3. Digital Content Creation"
    competency: "3.4 Programming"
  - objective_id: LO4
    competency_area: "5. Problem Solving"
    competency: "5.1 Solving technical problems"
  - objective_id: LO6
    competency_area: "3. Digital Content Creation"
    competency: "3.3 Digital content development"
---

# Container-to-Container Communication

A single container running in isolation is useful. A system of containers communicating with each other is powerful.

Your AI agent needs a database to store conversations. That database needs to be in a separate container. Your agent also needs a cache layer (Redis) to store recent context. That's another container. A production system might have an agent container, a Postgres database container, a Redis cache container, and a logging service—each in separate containers, all communicating transparently by name.

Docker networks make this possible. They provide the plumbing that lets containers find each other, communicate securely within their network, and remain isolated from containers on other networks.

In this lesson, you'll build and connect multiple containers manually, understanding exactly how communication works before Docker Compose automates it in the next lesson.

---

## The Problem: How Do Containers Find Each Other?

When you run a container, it gets an IP address from Docker's internal DHCP server. But IP addresses change each time a container restarts. If your agent stores "connect to database at 172.17.0.2," and the database container restarts with a different IP, the connection breaks.

Docker solves this with **automatic DNS service discovery**: containers on a user-defined network can find each other by name. Your agent container can connect to `postgres` or `redis` just by using those hostnames—Docker's DNS automatically resolves them to the current IP address.

Let's build this step by step.

---

## Default Bridge Network vs User-Defined Networks

Docker provides a default bridge network, but it has limitations:

**Default Bridge Network** (`docker0`):
- All containers without explicit network connect to this automatically
- Containers see each other's IP addresses, but NOT names
- Example: Container A can't reach "postgres"—it needs the actual IP
- No isolation—difficult to run multiple projects without conflicts

**User-Defined Bridge Networks**:
- You create networks explicitly (e.g., `ai-service-network`)
- Automatic DNS: containers find each other by name
- Built-in isolation: containers on different networks can't communicate
- Perfect for multi-service applications

**You should always use user-defined bridge networks for multi-container applications.**

---

## Creating a User-Defined Network

Create a bridge network for your AI service:

```bash
docker network create ai-service-network
```

**Output:**
```
4a7d8f9e3c2b1a0f5d4e3c2b1a0f5d4e
```

That long string is the network ID. Verify the network exists:

```bash
docker network ls
```

**Output:**
```
NETWORK ID          NAME                 DRIVER       SCOPE
4a7d8f9e3c2b      ai-service-network   bridge       local
7f9d8e4c3b2a      bridge               bridge       local
1c2d3e4f5a6b      host                 host         local
9e8f7d6c5b4a      none                 null         local
```

Your new network appears in the list. The `bridge` driver means containers can connect and communicate. The `local` scope means it's available on this Docker host only.

---

## Connecting Containers to a Network

When you run a container, specify which network it should join with `--network`:

**Start a Redis container on the network:**

```bash
docker run -d \
  --name redis-cache \
  --network ai-service-network \
  redis:7-alpine
```

**Output:**
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

**Start a Postgres database container:**

```bash
docker run -d \
  --name postgres-db \
  --network ai-service-network \
  -e POSTGRES_PASSWORD=secret \
  postgres:16-alpine
```

**Output:**
```
x9y8z7w6v5u4t3s2r1q0p9o8n7m6l5k4
```

Both containers are now on `ai-service-network`. Inspect the network to see all connected containers:

```bash
docker network inspect ai-service-network
```

**Output:**
```json
[
  {
    "Name": "ai-service-network",
    "Id": "4a7d8f9e3c2b1a0f5d4e3c2b1a0f5d4e",
    "Created": "2025-12-23T10:15:30.123456789Z",
    "Scope": "local",
    "Driver": "bridge",
    "EnableIPv6": false,
    "IPAM": {
      "Driver": "default",
      "Config": [
        {
          "Subnet": "172.18.0.0/16",
          "Gateway": "172.18.0.1"
        }
      ]
    },
    "Internal": false,
    "Attachable": true,
    "Ingress": false,
    "Containers": {
      "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6": {
        "Name": "redis-cache",
        "EndpointID": "7f8e9d0c1b2a3456789abcdef0123456",
        "MacAddress": "02:42:ac:12:00:02",
        "IPv4Address": "172.18.0.2/16",
        "IPv6Address": ""
      },
      "x9y8z7w6v5u4t3s2r1q0p9o8n7m6l5k4": {
        "Name": "postgres-db",
        "EndpointID": "f6e5d4c3b2a1987654321fedcba09876",
        "MacAddress": "02:42:ac:12:00:03",
        "IPv4Address": "172.18.0.3/16",
        "IPv6Address": ""
      }
    }
  }
]
```

Both containers are connected. Notice the IPs: `172.18.0.2` and `172.18.0.3`. These IPs are internal to the network and will change if containers restart.

---

## Automatic DNS Service Discovery

The magic: containers on this network can now find each other by name.

Start a test container that runs a shell and connects to the network:

```bash
docker run -it \
  --name test-client \
  --network ai-service-network \
  alpine:latest \
  /bin/sh
```

You're now inside the container shell. Test DNS resolution:

```bash
ping redis-cache
```

**Output:**
```
PING redis-cache (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.2ms
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.2ms
^C
```

It works! The container resolved `redis-cache` to its IP address automatically. Even if the Redis container restarts and gets a new IP, the name `redis-cache` always resolves to the current IP.

Test connecting to Redis:

```bash
apk add redis
redis-cli -h redis-cache ping
```

**Output:**
```
PONG
```

The test container successfully connected to Redis by name. Your agent application would use the same hostname: `redis.Redis(host='redis-cache')` in Python, or `redis-cache:6379` in connection strings.

Exit the test container:

```bash
exit
```

---

## Network Isolation: Containers Can't Cross Networks

Create a second network to demonstrate isolation:

```bash
docker network create another-network
```

Start a container on this new network:

```bash
docker run -d \
  --name isolated-container \
  --network another-network \
  alpine:latest \
  sleep infinity
```

Now try to ping the Redis container from the isolated container:

```bash
docker exec isolated-container ping redis-cache
```

**Output:**
```
ping: bad address 'redis-cache'
```

The isolated container can't reach the Redis container even though both are running. Why? They're on different networks. Containers on `another-network` have no visibility into `ai-service-network`.

This is a feature, not a bug. It enforces clean separation: your AI service network is isolated from other projects, preventing accidental connections and name collisions.

---

## Runtime Network Management: Connecting & Disconnecting

Sometimes you need to add a container to a network after it's already running. Docker provides `docker network connect` and `docker network disconnect`.

Connect the isolated container to your AI service network:

```bash
docker network connect ai-service-network isolated-container
```

Now it can reach Redis:

```bash
docker exec isolated-container ping redis-cache
```

**Output:**
```
PING redis-cache (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.1ms
```

It works! The container is now on both networks. Verify:

```bash
docker network inspect ai-service-network
```

The output shows `isolated-container` is now connected.

Disconnect the container:

```bash
docker network disconnect ai-service-network isolated-container
```

It can no longer reach Redis. This runtime flexibility is useful when you need to change an architecture without restarting containers.

---

## Container Aliases: Multiple Names for One Container

Sometimes a container needs to respond to multiple names. Docker provides `--network-alias` for this.

Start a container with aliases:

```bash
docker run -d \
  --name cache-primary \
  --network ai-service-network \
  --network-alias redis \
  --network-alias cache \
  redis:7-alpine
```

Other containers can now reach this Redis instance by three different names:

```bash
docker run -it \
  --network ai-service-network \
  alpine:latest \
  /bin/sh
```

Inside the container:

```bash
ping cache-primary  # Primary name
ping redis          # Alias
ping cache          # Another alias
```

**Output:**
```
PING redis (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.1ms
```

All three names resolve to the same container. This is useful when your code expects `redis` but you want the container named `cache-primary` for clarity. Using aliases abstracts the container name from the network name.

---

## Multi-Container AI Service Example

Now let's build a realistic three-tier AI service:

1. **Agent** — FastAPI service that processes requests
2. **Database** — Postgres stores conversation history
3. **Cache** — Redis stores recent context for fast access

**Step 1: Create the network**

```bash
docker network create ai-app-network
```

**Step 2: Start Postgres**

```bash
docker run -d \
  --name postgres \
  --network ai-app-network \
  -e POSTGRES_DB=conversations \
  -e POSTGRES_USER=ai_user \
  -e POSTGRES_PASSWORD=secure_password \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:16-alpine
```

**Step 3: Start Redis**

```bash
docker run -d \
  --name redis \
  --network ai-app-network \
  redis:7-alpine
```

**Step 4: Start the Agent**

Create a simple FastAPI agent that connects to both services:

**File: agent.py**
```python
from fastapi import FastAPI
import psycopg2
import redis
import os

app = FastAPI()

# Connect to services by hostname
@app.on_event("startup")
async def startup():
    global db_conn, cache

    # Connect to Postgres using hostname 'postgres'
    db_conn = psycopg2.connect(
        host='postgres',
        database='conversations',
        user='ai_user',
        password='secure_password'
    )

    # Connect to Redis using hostname 'redis'
    cache = redis.Redis(host='redis', port=6379, decode_responses=True)

    print("Connected to Postgres and Redis by hostname!")

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": "postgres",
        "cache": "redis"
    }

@app.post("/conversation/{user_id}")
def save_conversation(user_id: str, message: str):
    # Store in cache (fast)
    cache.set(f"user:{user_id}:latest", message)

    # Store in database (persistent)
    cursor = db_conn.cursor()
    cursor.execute(
        "INSERT INTO conversations (user_id, message) VALUES (%s, %s)",
        (user_id, message)
    )
    db_conn.commit()

    return {"status": "saved", "user_id": user_id}

@app.get("/conversation/{user_id}")
def get_conversation(user_id: str):
    # Try cache first
    cached = cache.get(f"user:{user_id}:latest")
    if cached:
        return {"source": "cache", "message": cached}

    # Fall back to database
    cursor = db_conn.cursor()
    cursor.execute(
        "SELECT message FROM conversations WHERE user_id = %s ORDER BY created_at DESC LIMIT 1",
        (user_id,)
    )
    result = cursor.fetchone()

    return {"source": "database", "message": result[0] if result else None}
```

**File: Dockerfile**
```dockerfile
FROM python:3.12-alpine

WORKDIR /app

RUN pip install uv

COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

COPY agent.py .

EXPOSE 8000
CMD ["uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8000"]
```

**File: requirements.txt**
```
fastapi==0.115.0
uvicorn==0.30.0
psycopg2-binary==2.9.9
redis==5.0.1
```

**Step 5: Build and run the agent**

```bash
docker build -t ai-agent:latest .
```

```bash
docker run -d \
  --name agent \
  --network ai-app-network \
  -p 8000:8000 \
  ai-agent:latest
```

**Step 6: Test the system**

```bash
curl http://localhost:8000/health
```

**Output:**
```json
{
  "status": "healthy",
  "database": "postgres",
  "cache": "redis"
}
```

The agent found Postgres and Redis by hostname! Test saving a conversation:

```bash
curl -X POST http://localhost:8000/conversation/user123 \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, AI!"}'
```

**Output:**
```json
{
  "status": "saved",
  "user_id": "user123"
}
```

Retrieve it:

```bash
curl http://localhost:8000/conversation/user123
```

**Output:**
```json
{
  "source": "cache",
  "message": "Hello, AI!"
}
```

Three containers communicating through a single network, finding each other by name. This is the foundation of distributed AI services.

---

## Practical Commands Reference

| Task | Command |
|------|---------|
| Create a network | `docker network create my-network` |
| List networks | `docker network ls` |
| Inspect a network | `docker network inspect my-network` |
| Run container on network | `docker run --network my-network ...` |
| Connect running container | `docker network connect my-network container-name` |
| Disconnect container | `docker network disconnect my-network container-name` |
| Add network alias | `docker run --network-alias cache-server ...` |
| Test DNS from container | `docker exec container nslookup hostname` |
| Check container connectivity | `docker exec container ping other-container` |

---

## Try With AI

**Setup**: You have three services running on a shared network: an agent, a database, and a cache. The agent communicates with both by hostname.

**Part 1: Ask for a Network Diagram**
Ask AI: "I have three containers (agent, postgres, redis) on a Docker network. Create a simple text diagram showing how they communicate by hostname and what isolation that provides."

**Part 2: Explore Service Discovery**
Review the network diagram AI provided. Ask yourself:
- How does the agent find Postgres without knowing its IP address?
- What happens if the Postgres container restarts with a new IP?
- Why can't a container on a different network reach these services?

**Part 3: Build Your Own Multi-Service Setup**
Take one of your own services from Part 6 (a FastAPI app, a chatbot, an agent):
- Create a user-defined network
- Identify what external service it needs (database, cache, API)
- Plan how to containerize that dependency
- Ask AI: "Help me write a docker-compose.yml that runs my [service] alongside [dependency] on a shared network, with the service connecting to the dependency by hostname"

**Part 4: Test Communication**
After AI provides docker-compose.yml:
- Run the full stack: `docker-compose up`
- Test that your service connects to the dependency successfully
- Check logs to confirm no connection errors
- Ask yourself: Did the service find the dependency by hostname? Why or why not?

**Part 5: Experiment with Isolation**
Create a second network with a different service. Try to make the two networks communicate.
Ask AI: "Why can't a container on network-A reach a container on network-B? What would I need to do to enable cross-network communication?"

Compare your current understanding to what the ecosystem recommends. Document what you learned about container isolation and service discovery.

