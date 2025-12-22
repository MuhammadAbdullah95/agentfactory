### Core Concept
Docker is a containerization system that packages applications with their dependencies into isolated, portable units that run identically anywhere. The key advantage over virtual machines is that containers share the host's kernel, making them lightweight (megabytes instead of gigabytes) while maintaining strong isolation.

### Key Mental Models
- **The Container Abstraction**: A container is an isolated process with its own filesystem, network namespace, and resource limits—not a full operating system. Think of it as a lightweight VM without the OS overhead.
- **Docker Desktop Architecture**: On macOS/Windows, Docker Desktop runs a minimal Linux VM invisibly, then Docker Engine manages containers inside it. On Linux, Docker Engine runs natively with no VM layer.
- **Resource Configuration Matters**: Docker allocates CPU and memory limits at configuration time. For AI workloads, insufficient memory causes silent failures (OOM kills). Configuring resources during installation prevents debugging headaches later.

### Critical Patterns
- **Verify Installation**: `docker version` confirms both Client and Server are working. Client is your terminal, Server is the Engine running behind the scenes.
- **Test the Complete Pipeline**: `docker run hello-world` validates the entire stack—image pull from Docker Hub, container creation, execution, and output streaming.
- **Configure for Your Workload**: AI services need 4+ CPUs and 8+ GB RAM in Docker Desktop. Underconfiguring here cascades into every container you run.
- **Understand the Stack**: Docker Desktop (GUI) → Linux VM → Docker Engine → containerd → Containers. Each layer has distinct responsibilities.

### Common Mistakes
- **Assuming Docker is the same as VMs**: VMs include full operating systems (~gigabytes). Docker shares the kernel (~megabytes). Not understanding this leads to over-provisioning resource limits.
- **Misconfiguring system prerequisites**: On Windows, forgetting to enable Hyper-V or not using WSL 2 causes installation failures that appear mystifying.
- **Ignoring resource allocation**: Setting Docker Desktop to 2GB memory for an AI project, then wondering why containers crash unexpectedly with exit code 137 (OOM kill).

### Connections
- **Builds on**: Part 6 covered building a FastAPI agent on your machine. This lesson prepares it for deployment anywhere.
- **Leads to**: Lesson 2 (images and containers) explores what Docker actually runs. Lesson 3 creates your first Dockerfile to containerize your agent.
