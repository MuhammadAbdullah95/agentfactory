# Lesson 11: Security & Best Practices - Summary

### Core Concept
Eight specific vulnerabilities pervade default Dockerfiles: leaked secrets in layers, bloated images with hundreds of CVEs, root user access, writable filesystems, and unnecessary dependencies. Systematic hardening—non-root users, multi-stage builds, .dockerignore, hardened base images—reduces attack surface from 150+ vulnerabilities to <5 per image.

### Key Mental Models
- **Principle of Least Privilege**: Minimize what a compromised container can access. Non-root user limits damage; read-only filesystem prevents tampering; minimal base image removes unnecessary attack surface.
- **Layers as Immutable History**: Once data is in a layer, it's there forever. Deleting a secret in a later layer doesn't erase it from earlier layers. Never copy secrets into images—inject at runtime.
- **Development vs. Production Posture**: Development prioritizes debugging visibility (writable filesystem, root user for package installs). Production requires defensive hardening (read-only filesystem, non-root execution, security scanning).

### Critical Patterns
- Create .dockerignore to prevent secret leakage: Exclude `.env`, credentials, `.git`, build artifacts, test files—anything not needed in the final image
- Use multi-stage builds to isolate build tools: Build stage installs gcc and build-essential (needed only for compilation); runtime stage uses slim image without these tools
- Run as non-root user: Create app user early (`RUN groupadd -r app && useradd -r -g app app`), change ownership (`COPY --chown=app:app`), switch to user (`USER app`)
- Clean package manager caches: `pip install --no-cache-dir` removes Python cache; `apt-get install && rm -rf /var/lib/apt/lists/*` removes apt cache
- Use Docker Scout for vulnerability scanning: `docker scout cves image-name` identifies CVEs; Docker Hardened Images (docker/python:3.12-dhi) provide pre-patched alternatives

### Common Mistakes
- Copying .env files into Dockerfile—once baked into a layer, API keys are extractable by anyone with image access
- Using bloated base images in production—python:3.12 has 150+ CVEs; python:3.12-slim has 80; docker/python:3.12-dhi has <5
- Running as root unnecessarily—default behavior; non-root requires explicit `USER` directive, but prevents privilege escalation attacks
- Forgetting read-only filesystem in docker-compose—leaving `read_only: true` off allows containers to modify their own code and introduce persistence
- Not excluding test files in .dockerignore—tests copy into image, bloat it, and expose test fixtures that might contain sensitive data

### Connections
- **Builds on**: Lesson 3 (Dockerfile structure), Lesson 4 (multi-stage builds for efficiency), Lesson 8 (secret management via environment variables)
- **Leads to**: Lesson 12 (Gordon assists with security hardening workflow), Lesson 13 (capstone applies all hardening patterns)
