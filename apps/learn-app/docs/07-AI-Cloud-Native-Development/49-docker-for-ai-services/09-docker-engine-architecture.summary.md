# Lesson 9: Docker Engine Architecture - Summary

### Core Concept
Docker's layered architecture separates concerns: the CLI accepts your commands, the daemon manages images and containers, containerd handles lifecycle operations, and runc executes the container using Linux namespaces and cgroups. Each layer follows the Open Container Initiative (OCI) standard, making components swappable and debuggable at specific layers.

### Key Mental Models
- **Client-Server Separation**: The `docker` CLI is a thin client; the daemon is the intelligent orchestrator. They communicate via API, not direct function calls. This separation allows remote Docker servers and tooling flexibility.
- **OCI Standards as Contracts**: The OCI Runtime and Image specifications define what a container IS and how runtimes MUST execute containers. This standardization lets different tools (Docker, Podman, Kubernetes) work with interchangeable components.
- **Runtime Flexibility**: The OCI spec allows swapping runc (standard isolation) with gVisor (syscall interception for security) or Kata (VM-level isolation). The daemon doesn't know which runtime is used—it just knows the spec must be implemented.

### Critical Patterns
- Trace a docker run command from CLI through layers: CLI → API → daemon → containerd → runc → kernel namespaces/cgroups
- Understand which layer solves which problem: Image issues → daemon, container lifecycle → containerd, actual execution → runc
- Choose runtimes based on security needs: runc for standard workloads, gVisor for untrusted code, Kata for compliance requirements
- Recognize that "container" is shorthand for a process with isolated namespaces, resource-limited cgroups, and a root filesystem

### Common Mistakes
- Treating Docker as monolithic—believing all Docker functionality is one binary (it's actually multiple cooperating services)
- Assuming runc is the only option—defaulting to runc when gVisor or Kata would better suit the security model
- Misunderstanding cgroups vs. namespaces—conflating process isolation (namespaces) with resource limits (cgroups)
- Blaming the daemon for runtime issues—not recognizing that some problems originate at the runc layer or kernel level

### Connections
- **Builds on**: Lesson 1 (container images), Lesson 2 (Dockerfile layer structure)
- **Leads to**: Lesson 11 (understanding architecture helps debug security vulnerabilities and choose appropriate hardening)
