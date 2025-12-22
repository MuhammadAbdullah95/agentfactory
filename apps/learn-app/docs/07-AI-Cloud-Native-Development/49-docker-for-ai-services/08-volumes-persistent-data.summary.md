# Lesson 8: Volumes and Persistent Data - Summary

### Core Concept
Containers are ephemeral by design—when deleted, all internal data vanishes. Volumes decouple data from containers by persisting storage independently, enabling stateful AI services to retain models, vectors, and logs across restarts.

### Key Mental Models
- **Ephemeral vs. Persistent**: Containers hold runtime state; volumes hold application data. Without volumes, restarts mean data loss. With volumes, data survives container deletion.
- **Three Storage Mechanisms**: Named volumes (Docker-managed, production), bind mounts (host directory sync, development), tmpfs mounts (memory-only, security).
- **Storage Layers**: Development prioritizes visibility (bind mounts for code, named volumes for data), while production prioritizes security and reliability (named volumes with backup policies, no bind mounts).

### Critical Patterns
- Named volume for persistent data: Create with `docker volume create`, attach with `-v volume-name:/container/path`
- Bind mount for development: Map host directory to container with `-v /host/path:/app/path`, enabling live code reload
- tmpfs for secrets: Store sensitive data only in RAM with `--tmpfs /run/secrets`, purged when container stops
- Volume lifecycle: Use `docker volume ls`, `docker volume inspect`, `docker volume rm`, `docker volume prune` to manage persistence

### Common Mistakes
- Storing large files in image layers instead of volumes—creates bloated images that rebuild slowly
- Using bind mounts in production—exposes host filesystem to container modifications and couples deployment to host structure
- Forgetting `.dockerignore` exclusions—sensitive files like `.env` leak into image layers where anyone accessing the image can extract them
- Not understanding named volume persistence—incorrectly assuming named volumes delete when containers stop (they don't)

### Connections
- **Builds on**: Lesson 7 (Dockerfile layer caching teaches why volumes separate concerns from images)
- **Leads to**: Lesson 10 (Docker Compose uses volumes extensively for multi-container service orchestration)
