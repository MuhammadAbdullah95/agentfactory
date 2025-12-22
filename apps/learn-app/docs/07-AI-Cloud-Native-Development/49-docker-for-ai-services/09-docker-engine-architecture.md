---
sidebar_position: 9
chapter: 49
lesson: 9
duration_minutes: 50
title: "Docker Engine Architecture"
proficiency_level: B1
teaching_stage: 1
stage_name: "Manual Foundation"
stage_description: "Understanding the Docker runtime stack enables effective debugging and optimization decisions"
cognitive_load:
  concepts_count: 6
  scaffolding_level: "Moderate"
learning_objectives:
  - id: LO1
    description: "Explain the client-server architecture of Docker (CLI vs daemon)"
    bloom_level: "Understand"
  - id: LO2
    description: "Describe how dockerd (daemon) manages containers and images"
    bloom_level: "Understand"
  - id: LO3
    description: "Explain the role of containerd in container lifecycle management"
    bloom_level: "Understand"
  - id: LO4
    description: "Describe how runc executes containers according to OCI specification"
    bloom_level: "Understand"
  - id: LO5
    description: "Identify when alternative runtimes (gVisor, Kata) are needed instead of runc"
    bloom_level: "Analyze"
  - id: LO6
    description: "Trace a docker run command through the architecture stack to execution"
    bloom_level: "Analyze"
digcomp_mapping:
  - objective_id: LO1
    competency_area: "1. Information and Data Literacy"
    competency: "1.1 Browsing, searching and filtering data"
  - objective_id: LO2
    competency_area: "5. Problem Solving"
    competency: "5.1 Solving technical problems"
  - objective_id: LO5
    competency_area: "5. Problem Solving"
    competency: "5.1 Solving technical problems"
  - objective_id: LO6
    competency_area: "1. Information and Data Literacy"
    competency: "1.2 Assessing, managing and integrating information"
---

# Docker Engine Architecture

You've been using Docker for the past eight lessons. You write Dockerfiles. You build images. You run containers. But what actually happens when you type `docker run`? Understanding the architecture behind Docker transforms you from a user who runs commands into an engineer who understands why those commands work the way they do.

In this lesson, you'll explore the Docker runtime stack from the user-facing CLI all the way down to the actual container execution. You'll meet the key components—the daemon that manages everything, the container runtime that handles lifecycle management, and the executor that makes containers actually run. You'll learn why Docker's architecture is designed this way, and you'll discover why sometimes the standard executor (runc) isn't enough and you need alternatives.

This knowledge will help you debug container issues, understand performance characteristics, and make informed decisions about which Docker features to use.

---

## The Big Picture: Client-Server Architecture

Docker follows a simple but powerful client-server design. The part you interact with—the `docker` command-line tool—is just a client. The actual work happens in a background service called the daemon. They communicate via the Docker API.

```
┌─────────────────┐
│  docker CLI     │  ← You type commands here
│  (client)       │
└────────┬────────┘
         │ API request (JSON over Unix socket or TCP)
         │
    ┌────▼──────────────────────────────┐
    │     Docker Daemon (dockerd)        │
    │   - Manages images                 │
    │   - Manages containers             │
    │   - Orchestrates lower-level tools │
    │   - Exposes REST API               │
    └────┬──────────────────────────────┘
         │
    ┌────▼──────────────────────────────┐
    │     containerd                     │
    │   - Container lifecycle            │
    │   - Image distribution             │
    │   - Storage management             │
    └────┬──────────────────────────────┘
         │
    ┌────▼──────────────────────────────┐
    │     runc (or alternative runtime)  │
    │   - Actually executes containers   │
    │   - Manages cgroups & namespaces   │
    │   - Creates isolation              │
    └────────────────────────────────────┘
```

Let's walk through each layer and understand its job.

---

## Docker Daemon (dockerd): The Control Plane

The Docker daemon is a background service that runs on your system (or remote server). It's the "intelligence" of Docker. When you type `docker run my-image`, your CLI sends a request to the daemon, which then decides what to do.

### What the Daemon Does

1. **Listens for API requests** — It exposes a REST API that the CLI (and other tools) communicate with
2. **Manages images** — Stores, pulls, builds, and removes images from disk
3. **Manages containers** — Creates, starts, stops, and removes containers
4. **Coordinates resources** — Tells containerd to manage container lifecycle, tells the runtime to create isolated processes
5. **Provides introspection** — Commands like `docker inspect`, `docker logs`, `docker ps` query the daemon's state

### Seeing the Daemon in Action

Start a container and watch the daemon manage it:

```bash
docker run -d --name debug-container ubuntu sleep 1000
```

**Output:**
```
7f8a9b2c3d4e5f6g7h8i9j0k1l2m3n4o
```

Now inspect what the daemon knows about this container:

```bash
docker inspect debug-container | head -40
```

**Output:**
```json
[
    {
        "Id": "7f8a9b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u",
        "Created": "2025-12-23T14:30:45.123456789Z",
        "Path": "/bin/sleep",
        "Args": ["1000"],
        "State": {
            "Status": "running",
            "Pid": 42857,
            "ExitCode": 0,
            "StartedAt": "2025-12-23T14:30:45.234567890Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:b6d55f0ecd8cc71e04d2f",
        "Name": "/debug-container",
        "RestartPolicy": {
            "Name": "no",
            "MaximumRetryCount": 0
        }
    }
]
```

That JSON is what the daemon maintains in memory. It knows:
- The container's ID and name
- When it was created
- What image it came from
- Its current status
- The host process ID (Pid: 42857)
- Restart policy
- Much more

The daemon acts as a central coordinator. When you issue a command, the daemon processes it and delegates to lower-level components.

---

## containerd: Container Lifecycle Manager

Below the daemon is `containerd`, a lower-level container runtime. It handles the actual container lifecycle: creation, starting, stopping, and cleanup. Think of it as a specialized, no-frills container manager.

### The Division of Concerns

- **Docker Daemon**: "What containers does the user want? What API calls are coming in?"
- **containerd**: "OK, create a container. Start this container. Stop that container. Remove this one."

containerd doesn't know about the Docker API or images in the traditional Docker sense. It's a simpler, more focused tool. In fact, containerd is a CNCF project used by many container orchestrators beyond Docker (like Kubernetes).

### Why This Separation?

Docker discovered early on that mixing high-level API logic (the daemon) with low-level container operations created complexity and bugs. By separating concerns:
- containerd focuses only on container operations
- Docker daemon focuses on images, networking, volumes, and the API
- Each can be maintained, upgraded, and tested independently

### Seeing containerd at Work

containerd has its own command-line tool: `ctr`. Let's list containers via containerd:

```bash
sudo ctr container list
```

**Output:**
```
CONTAINER                                                           IMAGE                            RUNTIME
7f8a9b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u                        docker.io/library/ubuntu:latest  io.containerd.runc.v2
```

Notice the RUNTIME column shows `io.containerd.runc.v2`—that's containerd telling us which executor (runc) it's using. We'll explain runc next.

---

## runc: The Container Executor

Below containerd is `runc`, the actual executor. runc takes the container specification and makes it real. It:

1. **Creates namespaces** — Process isolation, network isolation, filesystem isolation
2. **Sets up cgroups** — CPU and memory limits
3. **Configures the filesystem** — Mounts the container's rootfs, volumes, etc.
4. **Starts the application process** — The command you specified in CMD or when running the container

### runc and OCI

runc is more than just Docker's executor—it's the **reference implementation of the Open Container Initiative (OCI) Runtime Specification**. This spec defines the standard way to execute containers.

The OCI spec says: "A container is a set of processes with isolated namespaces, limited resources via cgroups, and a defined root filesystem." runc is the canonical tool that implements this definition.

### Seeing runc at Work

When you run a container, containerd calls runc under the hood. You can see runc processes running:

```bash
ps aux | grep runc | head -5
```

**Output:**
```
root      42857  0.0  0.0 120804  1234 ?  Ss  14:30 /usr/bin/runc --root /run/runc --log /run/runc/...
```

runc starts your container's main process (in this case, `/bin/sleep`). Once the process is running, runc's job is complete—it exits, leaving the actual container process running under containerd's supervision.

---

## OCI: The Standards That Make It Work

The Open Container Initiative (OCI) is a Linux Foundation project that standardizes container specifications. Docker and other container tools implement these standards.

### Two Critical Specs

**1. OCI Image Specification**

Defines how a container image is structured: layers, configuration, manifests. This is why you can pull a Docker image and run it with Podman, or pull an image with containerd and run it with Docker. They all follow the same standard.

Example image config (from `docker inspect`):

```json
{
  "architecture": "amd64",
  "config": {
    "Hostname": "",
    "Domainname": "",
    "User": "",
    "AttachStdin": false,
    "AttachStdout": false,
    "AttachStderr": false,
    "Tty": false,
    "OpenStdin": false,
    "StdinOnce": false,
    "Env": ["PATH=/usr/local/bin:/usr/bin:/bin"],
    "Cmd": ["/bin/bash"],
    "WorkingDir": "/",
    "Entrypoint": null,
    "Labels": null
  },
  "rootfs": {
    "type": "layers",
    "diff_ids": [
      "sha256:abc123...",
      "sha256:def456..."
    ]
  }
}
```

**2. OCI Runtime Specification**

Defines how a runtime (like runc) should execute a container. The spec includes:
- How to set up namespaces (PID, Network, UTS, IPC, Mount, User)
- How to apply cgroup resource limits
- How to configure the filesystem
- How to start and manage the container process

This standard makes it possible to swap runtimes. Your Docker daemon doesn't care if it's using runc, gVisor, or Kata—as long as the runtime implements the OCI spec, Docker can use it.

---

## Alternative Runtimes: When runc Isn't Enough

runc provides **isolation through Linux primitives** (namespaces and cgroups). For most use cases, this is perfect. But sometimes you need different security or isolation properties.

### gVisor: Lightweight Security

gVisor implements an additional layer of isolation by intercepting syscalls. Instead of letting containers make direct kernel syscalls, gVisor intercepts them and decides which are safe.

**Use gVisor when:**
- Running untrusted code (third-party agents)
- You need extra security boundaries but don't want VM overhead
- You're concerned about kernel vulnerabilities

**Trade-off:** Slower than runc (syscalls are intercepted and translated)

Example: Run your debug container with gVisor:

```bash
docker run --runtime gvisor --name safe-container ubuntu sleep 1000
```

### Kata Containers: VM-Level Isolation

Kata runs each container in a lightweight virtual machine. It's heavier than runc but provides VM-level isolation—if one container is compromised, others are protected by the hypervisor.

**Use Kata when:**
- Running truly untrusted workloads
- Compliance requires hardware-level isolation
- You need defense-in-depth (kernel vulnerability doesn't compromise the whole host)

**Trade-off:** Higher resource overhead, slower startup

Example: Run your debug container with Kata:

```bash
docker run --runtime kata --name vm-isolated-container ubuntu sleep 1000
```

### crun: Speed-Optimized runc Alternative

`crun` is a lighter, faster implementation of the OCI runtime spec, written in C instead of Go. Drop-in replacement for runc with better performance.

**Use crun when:**
- You have thousands of containers and need faster startup
- You're concerned about daemon resource usage
- You want OCI standard compliance with less overhead

Example:

```bash
docker run --runtime crun --name fast-container ubuntu sleep 1000
```

---

## Tracing a docker run Command Through the Stack

Let's follow what happens when you type a single command. This will show how all the layers work together.

### The Command

```bash
docker run -it --name my-app --memory 512m ubuntu echo "Hello from isolation"
```

### Step-by-Step Execution

**1. Docker CLI parses the command**

The `docker` CLI on your machine receives the command and parses arguments:
- Image: `ubuntu`
- Command to run: `echo "Hello from isolation"`
- Container name: `my-app`
- Memory limit: 512MB
- Interactive + TTY: `-it`

**2. CLI sends API request to daemon**

The CLI connects to the Docker daemon via a Unix socket (or TCP if remote) and sends:

```json
{
  "method": "POST",
  "path": "/containers/create",
  "body": {
    "Image": "ubuntu",
    "Cmd": ["echo", "Hello from isolation"],
    "Name": "my-app",
    "HostConfig": {
      "Memory": 536870912,
      "MemorySwap": 536870912
    },
    "Tty": true,
    "AttachStdin": true,
    "AttachStdout": true
  }
}
```

**3. Daemon processes the request**

The daemon:
- Validates the request
- Checks if the `ubuntu` image exists (pulls if needed)
- Creates a container configuration
- Calls containerd to create a container

**4. containerd receives the create request**

containerd:
- Allocates a unique container ID
- Sets up the container's bundle (filesystem, config)
- Tells its configured runtime (runc) to prepare the container

**5. runc prepares the container**

runc:
- Creates Linux namespaces (PID, network, mount, etc.)
- Sets up cgroups with the 512MB memory limit
- Mounts the Ubuntu image layers as the container's root filesystem
- Prepares stdin/stdout/stderr for the TTY

**6. The main process starts**

runc executes the command:

```
PID 1: /bin/sh -c "echo Hello from isolation"
```

But this runs in isolated namespaces:
- Its own PID namespace (see process 1, not host process 1)
- Its own network namespace (can't see host network devices)
- Its own mount namespace (sees container filesystem, not host filesystem)
- Limited memory (512MB cgroup limit)

**7. Output flows back**

The container's stdout is connected back through:
- runc's stdout handler
- containerd's stdout handler
- Docker daemon's stdout handler
- Docker CLI's output handler
- Your terminal

**8. Container finishes**

When the command completes:
- The main process exits
- containerd detects the exit
- Daemon marks the container as stopped
- Resources (namespaces, cgroups, mount points) are cleaned up

**9. You see the output**

```
Hello from isolation
```

This entire flow—from CLI command to isolated execution back to your terminal—happens in milliseconds. But each layer has a specific job, and understanding that separation is what makes Docker powerful and debuggable.

---

## Architecture Diagram: The Full Stack

```
┌──────────────────────────────────────────────────────────┐
│ Your Machine / Cloud Server                              │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────────────────────────────────┐          │
│  │ User Space                                 │          │
│  │                                            │          │
│  │  ┌──────────────┐                          │          │
│  │  │ docker CLI   │                          │          │
│  │  │ (client)     │                          │          │
│  │  └──────┬───────┘                          │          │
│  │         │ Unix socket or TCP               │          │
│  │         ▼                                  │          │
│  │  ┌──────────────────────────────────┐     │          │
│  │  │ Docker Daemon (dockerd)          │     │          │
│  │  │ - Image management               │     │          │
│  │  │ - Container coordination          │     │          │
│  │  │ - API server                     │     │          │
│  │  └──────┬───────────────────────────┘     │          │
│  │         │ Task API                        │          │
│  │         ▼                                  │          │
│  │  ┌──────────────────────────────────┐     │          │
│  │  │ containerd                        │     │          │
│  │  │ - Container lifecycle             │     │          │
│  │  │ - Image distribution              │     │          │
│  │  │ - Storage management              │     │          │
│  │  └──────┬───────────────────────────┘     │          │
│  │         │ OCI Runtime Spec                │          │
│  │         ▼                                  │          │
│  │  ┌──────────────────────────────────┐     │          │
│  │  │ Runtime (runc / gVisor / Kata)   │     │          │
│  │  │ - Creates namespaces              │     │          │
│  │  │ - Sets up cgroups                │     │          │
│  │  │ - Starts container process       │     │          │
│  │  └──────┬───────────────────────────┘     │          │
│  │         │                                  │          │
│  └─────────┼──────────────────────────────────┘          │
│            │                                            │
├────────────┼────────────────────────────────────────────┤
│ Kernel Space                                           │
│            │                                            │
│            ▼                                            │
│  ┌──────────────────────────────────────────┐          │
│  │ Linux Namespaces (for isolation)         │          │
│  │ - PID namespace (process trees)          │          │
│  │ - Network namespace (network stack)      │          │
│  │ - Mount namespace (filesystem trees)     │          │
│  │ - IPC namespace (inter-process comms)    │          │
│  │ - UTS namespace (hostname, domain)       │          │
│  │ - User namespace (UID mapping)           │          │
│  └──────────────────────────────────────────┘          │
│                                                        │
│  ┌──────────────────────────────────────────┐          │
│  │ Control Groups (cgroups - for limits)    │          │
│  │ - CPU limits                             │          │
│  │ - Memory limits                          │          │
│  │ - I/O limits                             │          │
│  │ - Device limits                          │          │
│  └──────────────────────────────────────────┘          │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## Why This Architecture?

You might wonder: why not just have one monolithic Docker command that does everything? Because:

1. **Modularity** — Each component can be developed, tested, and upgraded independently
2. **Standards** — containerd and runc follow OCI standards, making them compatible with other tools (Kubernetes, Podman, etc.)
3. **Security** — The daemon runs with elevated privileges, but containerd and runc run with minimal required permissions
4. **Flexibility** — You can swap runtimes without changing the daemon or CLI
5. **Performance** — Each layer is optimized for its specific job
6. **Tooling** — Other tools can speak the OCI and containerd APIs without reimplementing everything

---

## Summary

When you type `docker run`, you're initiating a conversation across multiple layers:

- **Docker CLI**: Parses your command and sends an API request
- **Docker Daemon**: Receives the request, validates it, manages state
- **containerd**: Handles container lifecycle (create, start, stop, delete)
- **Runtime (runc)**: Actually executes the container using Linux primitives
- **Kernel**: Provides namespaces for isolation and cgroups for resource limits

Each layer has a specific responsibility. Understanding this separation helps you:
- Debug problems at the right layer (is it a daemon issue, a containerd issue, or a runtime issue?)
- Make informed choices (when to use gVisor, when crun makes sense, when Kata is necessary)
- Optimize performance (knowing what each layer does helps you tune configurations)
- Understand why Docker works the way it does

The beauty of this architecture is that the OCI standards mean you can swap components. Your image works with different runtimes. Your daemon can use different container managers. This flexibility is what makes Docker (and the broader container ecosystem) so powerful.

---

## Try With AI

**Setup:** Access Claude or another LLM in your preferred IDE. Use the context from this lesson.

**Prompt 1: Understanding your local Docker stack**
```
I want to understand the Docker architecture on my machine. Here's what I see when I run:
- docker ps shows containers running
- sudo ctr container list shows the same containers

Why are both showing the same containers? Explain the relationship between the docker command I use and the containerd tools underneath.
```

**Prompt 2: Choosing the right runtime for your use case**
```
I'm building a service that runs user-submitted Python scripts inside containers.
The scripts could be untrusted (from external sources).

Should I use:
A) Standard runc (lowest overhead, but scripts have direct kernel access)
B) gVisor (lighter than VMs, but intercepts syscalls)
C) Kata Containers (full VM isolation)

What are the tradeoffs? Which would you recommend for my situation?
```

**Prompt 3: Debugging a slow container startup**
```
I'm running 50 containers on a server and noticing that container creation is slow.
Each container startup takes ~2 seconds. I read that crun (a C implementation of OCI runtime)
is faster than runc (Go implementation).

Walk me through:
1. Why would crun be faster than runc?
2. How would I switch my Docker installation to use crun?
3. What risks or trade-offs should I consider?
```

**Prompt 4: Following a container command through the stack**
```
I'm running this command:

docker run --rm -it --memory 1g alpine sh -c "free -h"

Trace this command through the entire architecture. For each layer (CLI, daemon, containerd, runtime),
explain what's happening and what's being communicated. Include how the memory limit is enforced.
```

**Expected outcomes:**
- You understand why Docker is layered the way it is
- You can explain the relationship between docker CLI, daemon, containerd, and runc
- You can make informed decisions about when to use alternative runtimes
- You can trace how a container command flows through the architecture

This understanding will help you make better decisions about container configuration, debugging, and optimization in the capstone project ahead.
