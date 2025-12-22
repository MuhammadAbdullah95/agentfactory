### Core Concept
Container networking solves the isolation problem: containers are isolated processes that can't reach the outside world by default. Docker provides networking mechanisms (port mapping, bridge networks) that let containers expose services, communicate with each other, and remain secure through isolation.

### Key Mental Models
- **Container Network Model (CNM)**: Sandboxes (isolated network namespaces per container) + Endpoints (connection points to networks) + Networks (groups of connected endpoints). Each container gets its own isolated network stack but can be connected to networks where it meets other containers.
- **Bridge Network Default**: All containers automatically connect to Docker's default bridge network. They can reach each other by IP, but not by hostname (limitation solved in Lesson 7 with user-defined networks). Port mappings tunnel from the host to the container.
- **Port Mapping Tunneling**: `-p 8000:8000` creates a tunnel: host port 8000 → container port 8000. Without mapping, the container's ports are unreachable from outside. With mapping, external clients can reach the containerized service.

### Critical Patterns
- **Port Mapping Syntax**: `-p host_port:container_port`. Example: `-p 9000:8000` means "traffic to my machine's port 9000 goes to the container's port 8000." Each host port is unique; only one container per port.
- **Expose vs Port Mapping**: EXPOSE in Dockerfile documents the port but doesn't actually open it. The `-p` flag does the actual mapping. Both are needed: EXPOSE documents intent, `-p` enables external access.
- **Inspect Networks Systematically**: `docker network inspect bridge` shows all connected containers and their IP addresses (usually 172.17.0.x range). This is your window into the network topology.
- **Host Network Mode Trade**: `--network host` removes isolation entirely—container uses host's network directly, better performance but loses isolation (security and resource constraints). Use it only for performance-critical scenarios where you understand the implications.

### Common Mistakes
- **Forgetting port mapping when needed**: `docker run python:3.12-slim python` runs Python in a container, but can't accept external connections without port mapping or specific client configuration.
- **Assuming container names resolve on default bridge**: Containers on the default bridge can ping by IP (172.17.0.2) but not by name (postgres, redis). This forces IP-address-based configuration, which breaks when containers restart (IPs change).
- **Port conflicts stopping you from running multiple services**: Multiple containers can't bind the same host port, but can bind different ports. If port 8000 is taken, use 8001, 8002, etc. Don't assume you can only run one per image.
- **Not understanding port direction**: `-p 8000:8000` isn't symmetric. Traffic comes from outside → host port 8000 → container port 8000. You can't reverse it (container initiating connection to host's port).

### Connections
- **Builds on**: Lessons 1-5 taught containerization. Lesson 6 introduces the networking layer needed for multi-container systems.
- **Leads to**: Lesson 7 (user-defined networks) solves the hostname resolution problem, enabling true service discovery. Docker Compose automates all this networking.
