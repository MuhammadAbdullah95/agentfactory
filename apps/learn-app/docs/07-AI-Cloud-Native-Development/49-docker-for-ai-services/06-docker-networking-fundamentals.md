---
sidebar_position: 6
chapter: 49
lesson: 6
duration_minutes: 30
title: "Docker Networking Fundamentals"
proficiency_level: B1
teaching_stage: 1
stage_name: "Manual Foundation"
stage_description: "Understanding container networking enables building multi-container AI services"
cognitive_load:
  concepts_count: 7
  scaffolding_level: "Moderate"
learning_objectives:
  - id: LO1
    description: "Explain the Container Network Model (CNM) and bridge network architecture"
    bloom_level: "Understand"
  - id: LO2
    description: "Map container ports to host ports using -p flag"
    bloom_level: "Apply"
  - id: LO3
    description: "Access a containerized service from the host machine via port mapping"
    bloom_level: "Apply"
  - id: LO4
    description: "Inspect Docker networks and container IP assignments"
    bloom_level: "Analyze"
  - id: LO5
    description: "Explain DNS resolution limitations on the default bridge network"
    bloom_level: "Understand"
  - id: LO6
    description: "Identify when to use host network mode vs bridge network"
    bloom_level: "Analyze"
  - id: LO7
    description: "Recognize different Docker network drivers and their use cases"
    bloom_level: "Understand"
digcomp_mapping:
  - objective_id: LO1
    competency_area: "3. Digital Content Creation"
    competency: "3.4 Programming"
  - objective_id: LO2
    competency_area: "3. Digital Content Creation"
    competency: "3.4 Programming"
  - objective_id: LO4
    competency_area: "5. Problem Solving"
    competency: "5.1 Solving technical problems"
  - objective_id: LO6
    competency_area: "5. Problem Solving"
    competency: "5.2 Identifying needs and responses"
---

# Docker Networking Fundamentals

Your FastAPI agent runs flawlessly in a container. But how do external clients reach it? When you deploy an AI service with a database and cache layer, how do the containers find each other? Container networking answers these questions—and it's fundamentally different from how applications communicate on your laptop.

On your machine, everything runs on localhost. But containers are isolated processes. By default, a container can't reach another container by name. A service inside a container can't listen on port 8000 on your host machine without explicit configuration. These aren't limitations—they're security features. Understanding Docker networking teaches you how isolation and connectivity work together.

In this lesson, you'll learn how containers communicate: how they expose ports to the outside world, how they resolve each other's addresses, and how Docker manages the networks connecting them. This foundation is essential before Docker Compose and Kubernetes, both of which automate these networking tasks.

---

## The Container Network Model (CNM)

Docker implements networking through the **Container Network Model (CNM)**, a simple architecture with three core concepts:

**1. Sandbox** — An isolated network namespace for a container. Think of it as a private network stack: its own network interfaces, IP addresses, routing tables, and DNS configuration. Each container gets its own sandbox.

**2. Endpoint** — A container's connection point to a network. A single container can connect to multiple networks (e.g., a service container connecting to both a "frontend" and "backend" network). Each endpoint has its own IP address on its connected network.

**3. Network** — A group of connected endpoints. Containers on the same network can communicate. Containers on different networks are isolated unless you create explicit connections.

Here's a visual model:

```
Host Machine
├── Network: bridge (default)
│   ├── Endpoint: container-a (IP: 172.17.0.2)
│   └── Endpoint: container-b (IP: 172.17.0.3)
│       └── Port Mapping: 8000:8000 (container:host)
└── Network: my-custom-network
    ├── Endpoint: container-c (IP: 172.18.0.2)
    └── Endpoint: container-d (IP: 172.18.0.3)
```

When you run `docker run`, the container is automatically attached to the default **bridge** network.

---

## The Bridge Network (Default)

The bridge network is Docker's default networking mode. When you run a container without specifying a network, Docker attaches it to the bridge network.

### How Bridge Networks Work

The bridge network creates a virtual network switch on your host machine. Each container gets:
- An IP address (usually in the 172.17.0.0/16 range)
- A default gateway pointing to the bridge itself (usually 172.17.0.1)
- Network connectivity to the host and other containers on the bridge

Containers on the default bridge can communicate with each other by IP address, but **not by container name**. That's a critical limitation we'll address later.

### Creating a Network-Aware Service

Let's create a simple FastAPI service and explore how the bridge network operates:

**File: agent.py**
```python
from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello from container",
        "container_hostname": os.getenv("HOSTNAME", "unknown")
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "port": 8000}
```

**File: requirements.txt**
```
fastapi==0.115.0
uvicorn==0.30.0
```

**File: Dockerfile**
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY agent.py .

EXPOSE 8000

CMD ["uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build the image:

```bash
docker build -t simple-agent:v1 .
```

**Output:**
```
[+] Building 8.2s (8/8) FINISHED
 => [internal] load build context
 => => transferring context: 256B
 => [1/6] FROM python:3.12-slim
 => => pull from library/python
 => [2/6] WORKDIR /app
 => [3/6] COPY requirements.txt .
 => [4/6] RUN pip install -r requirements.txt --no-cache-dir
 => [5/6] COPY agent.py .
 => [6/6] RUN echo "Image built"
 => => RUN echo "Image built"
```

---

## Port Mapping: Exposing Containers to the Host

A container is isolated. Its port 8000 is unreachable from your host machine by default. Port mapping creates a tunnel from your host to the container.

The `-p` flag syntax is: `-p host_port:container_port`

### Port Mapping Example

Run the agent with port mapping:

```bash
docker run -d --name my-agent -p 8000:8000 simple-agent:v1
```

**Output:**
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

Now you can access the service:

```bash
curl http://localhost:8000/
```

**Output:**
```json
{
  "message": "Hello from container",
  "container_hostname": "a1b2c3d4e5f6"
}
```

The port mapping works:
- Requests to `localhost:8000` on your host are forwarded to port 8000 inside the container
- The container's process listens on `0.0.0.0:8000` (all interfaces), so it receives the forwarded traffic
- The response travels back through the tunnel to your host

### Multiple Port Mappings

You can map different host ports to the same container port:

```bash
docker run -d --name agent-v2 -p 9000:8000 simple-agent:v1
```

**Output:**
```
c7d8e9f0a1b2c3d4e5f6g7h8i9j0k1l2
```

Now both work:

```bash
curl http://localhost:8000/    # Maps to first container (a1b2c3d4...)
curl http://localhost:9000/    # Maps to second container (c7d8e9f0...)
```

**Output:**
```json
{"message": "Hello from container", "container_hostname": "a1b2c3d4e5f6"}
```
```json
{"message": "Hello from container", "container_hostname": "c7d8e9f0a1b2"}
```

### Port Conflicts

What if you try to map the same host port twice?

```bash
docker run -d --name agent-v3 -p 8000:8000 simple-agent:v1
```

**Output:**
```
Error response from daemon: driver failed programming external connectivity on endpoint agent-v3: Bind for 0.0.0.0:8000 failed: port is already in use
```

Ports are exclusive resources on the host. Only one process can bind to port 8000. If you need multiple instances, use different host ports:

```bash
docker run -d --name agent-v3 -p 8001:8000 simple-agent:v1
```

**Output:**
```
d9e0f1a2b3c4d5e6f7g8h9i0j1k2l3m4
```

---

## Inspecting Networks and Container IPs

Understanding the actual network configuration helps you debug connectivity issues.

### List Docker Networks

```bash
docker network ls
```

**Output:**
```
NETWORK ID     NAME      DRIVER    SCOPE
a1b2c3d4e5f6   bridge    bridge    local
f6g7h8i9j0k1   host      host      local
l2m3n4o5p6q7   none      null      local
```

Docker creates three default networks: `bridge`, `host`, and `none`. Most containers run on the bridge network.

### Inspect the Bridge Network

```bash
docker network inspect bridge
```

**Output:**
```json
[
    {
        "Name": "bridge",
        "Id": "a1b2c3d4e5f6...",
        "Created": "2025-12-23T10:30:00.000000Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Config": [
                {
                    "Subnet": "172.17.0.0/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "Containers": {
            "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6": {
                "Name": "my-agent",
                "EndpointID": "abc123def456...",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            },
            "c7d8e9f0a1b2c3d4e5f6g7h8i9j0k1l2": {
                "Name": "agent-v2",
                "EndpointID": "xyz789uvw456...",
                "MacAddress": "02:42:ac:11:00:03",
                "IPv4Address": "172.17.0.3/16",
                "IPv6Address": ""
            }
        }
    }
]
```

Key observations:
- **Subnet**: `172.17.0.0/16` — The network's address space
- **Gateway**: `172.17.0.1` — The bridge's address (containers' default gateway)
- **Containers**: Listed with their IP addresses and MAC addresses

Each container gets an IP address from the subnet. Containers can ping each other by IP:

```bash
docker exec my-agent ping -c 1 172.17.0.3
```

**Output:**
```
PING 172.17.0.3 (172.17.0.3) 56(84) bytes of data.
64 bytes from 172.17.0.3: icmp_seq=1 ttl=64 time=0.123 ms

--- 172.17.0.3 statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 1ms
```

But what if you try to reach a container by name?

```bash
docker exec my-agent ping -c 1 agent-v2
```

**Output:**
```
ping: agent-v2: Name or service not known
```

The container name isn't resolvable on the default bridge network. This is a major limitation that user-defined networks solve (covered in Lesson 7).

---

## Container DNS Resolution

By default, containers on the bridge network can't resolve each other's names. This happens because:

1. Each container gets a `/etc/resolv.conf` that points to the host's nameserver (usually 8.8.8.8 or your ISP's DNS)
2. The host's nameserver doesn't know about container names (only Docker knows them)
3. Docker's internal DNS server only works for **user-defined networks**, not the default bridge

This is why multi-container setups require user-defined networks (Lesson 7) or Docker Compose (which creates user-defined networks automatically).

---

## Host Network Mode

Sometimes you don't want a container isolated on the bridge. The `--network host` mode removes the network isolation entirely. The container shares the host's network stack.

### When to Use Host Network

- **Performance-critical services**: No network isolation means no translation overhead. Useful for high-throughput services or benchmarking
- **Port-heavy services**: Services needing many ports (e.g., media servers) can bind directly without mapping
- **Services that need host network features**: Some network-specific applications need raw socket access

### Host Network Example

```bash
docker run -d --name host-agent --network host simple-agent:v1
```

**Output:**
```
e1f2g3h4i5j6k7l8m9n0o1p2q3r4s5t6
```

Now the container listens directly on the host's port 8000:

```bash
curl http://localhost:8000/
```

**Output:**
```json
{"message": "Hello from container", "container_hostname": "e1f2g3h4i5j6"}
```

No `-p` flag needed—the container binds directly to the host's network interface.

### Tradeoffs

**Advantages**:
- Direct network access (better performance)
- No port mapping complexity

**Disadvantages**:
- Loses network isolation (container can see/modify host network)
- Port conflicts directly affect the host (no multiple mappings)
- Reduces security (container processes see host network)

For most AI services, use bridge networking with port mapping (the default). Use host mode only when you understand the security implications.

---

## Network Driver Types

Docker supports multiple network drivers for different use cases:

| Driver | Use Case | Features |
|--------|----------|----------|
| **bridge** | Default, single-host containers | Isolated, port mappable, no container-name DNS |
| **host** | Direct host network access | Best performance, no isolation |
| **none** | No networking | Complete isolation |
| **overlay** | Multi-host, Swarm/Kubernetes | Spans multiple hosts, encrypted |
| **macvlan** | Custom MAC addresses | Containers appear as physical devices |
| **ipvlan** | Custom IPs without MAC | Lightweight, VLAN-like |

For development and local testing (your current focus), bridge and host are the relevant ones. Overlay (used by Kubernetes) is covered in Part 7.

---

## Key Networking Commands Summary

| Command | Purpose |
|---------|---------|
| `docker run -p host:container IMAGE` | Port mapping |
| `docker run --network NETWORK IMAGE` | Attach to specific network |
| `docker run --network host IMAGE` | Host network mode |
| `docker network ls` | List all networks |
| `docker network inspect NETWORK` | Show network details and connected containers |
| `docker port CONTAINER` | Show port mappings |
| `docker inspect CONTAINER` | Show container details (includes IP address) |

---

## Try With AI

You've learned how containers communicate via bridge networks, port mapping, and IP addresses. Now it's time to explore this interactively.

**Setup:**

1. Ensure you have the `simple-agent:v1` image built from the example above (or rebuild it if needed)
2. Have a terminal ready with Docker running

**Prompts to Explore:**

**Prompt 1 — Port Mapping Deep Dive:**
```
I have a FastAPI service running in a container on port 8000.
I want to understand port mapping better.

Can you explain:
1. What happens if I map -p 0.0.0.0:9000:8000 vs -p 127.0.0.1:9000:8000?
2. How would I expose the same container to both my local machine and other machines on my network?
3. What's the difference between exposing to 0.0.0.0 vs 127.0.0.1?

Give me specific docker run commands I can try.
```

**Prompt 2 — Network Inspection and Debugging:**
```
I have three containers running on the bridge network.
I need to debug why they can't communicate with each other by name.

Walk me through:
1. How to inspect the bridge network and see all containers
2. How to test connectivity between containers by IP
3. Why container names don't resolve
4. What command would I use to switch them to a user-defined network?
```

**Prompt 3 — Host Network Tradeoffs:**
```
When should I use --network host instead of the default bridge?
Create a comparison showing:
1. A scenario where host network makes sense
2. A scenario where bridge is the right choice
3. The security implications of each
4. How to measure the performance difference
```

**Expected Outcomes:**

After these conversations, you should be able to:
- Explain port mapping syntax and debug connectivity issues
- Inspect Docker networks to understand container placement
- Recognize when to use host vs bridge networking
- Understand limitations of the default bridge (no container-name DNS)
- Know what user-defined networks solve (coming in Lesson 7)

