### Core Concept
Multi-stage builds use multiple base images in one Dockerfile, separating the "build environment" (large, has compilers) from the "runtime environment" (small, only essentials). This dramatically shrinks images by discarding build artifacts that aren't needed to run the application.

### Key Mental Models
- **Build vs Runtime Stages**: Stage 1 (builder) installs dependencies, compiles code, generates artifacts with full build tools available. Stage 2 (runtime) copies only the artifacts needed to RUN the application, discarding the 500MB build toolchain.
- **Base Image Selection Tradeoff**: `python:3.12` (full, 900MB) includes compilers and dev headers—needed for building. `python:3.12-slim` (150MB) removes some build tools but keeps essentials. `python:3.12-alpine` (50MB) is minimal but may lack required libraries. Choose slim by default, alpine for size-critical deployments.
- **Layer Sharing at Scale**: One 150MB base layer shared across 100 deployed services means 150MB on disk, not 15GB. Optimization pays off exponentially with scale.

### Critical Patterns
- **Multi-Stage Template**: FROM python:3.12-alpine AS builder (build stage) → FROM python:3.12-alpine (runtime stage, starts fresh) → COPY --from=builder (bring artifacts only). This pattern reduces bloat by 85-90%.
- **Dependency Installation Order**: Copy requirements first, install with `pip install --user --no-cache-dir`, then copy code. Builder stage is large; runtime stage copies only `/root/.local` (installed packages).
- **Use UV Package Manager**: pip is slow; uv is 10-100x faster and uses less memory. Especially valuable for large requirements with many dependencies or in CI/CD pipelines.
- **Combine RUN Commands with Cleanup**: Each RUN creates a layer. `RUN pip install ... && rm -rf /root/.cache` in one command means cache cleanup happens in the same layer (not carried forward).
- **Large Model Files Don't Belong in Images**: Don't COPY 4GB model files into the Dockerfile—the image becomes 4GB+, slow to push/pull, and wastes storage. Use volume mounts instead: `-v $(pwd)/models:/app/models`.

### Common Mistakes
- **Forgetting to set PATH after copying from builder**: When you copy installed packages from builder, make sure the runtime stage has Python's bin directory in its PATH so executables are found.
- **Using full base images when slim suffices**: `python:3.12` is the default in Docker Hub. Starting with it adds 750MB of unnecessary bloat for 90% of Python applications.
- **Not measuring before and after**: You should see 70-85% size reduction going from naive to multi-stage. If your optimization only saves 10%, there's likely a better approach.
- **Copying too much from builder stage**: Don't copy `/opt` or `/usr/local` blindly. Copy only what the application needs: site-packages directory, bin executables, maybe some configs.
- **Skipping BuildKit**: Modern builds with `DOCKER_BUILDKIT=1` offer better caching and parallel execution. If your builds feel slow, enable BuildKit.

### Connections
- **Builds on**: Lesson 3 (Dockerfile) showed basic builds. This lesson teaches production-grade optimization for deployment at scale.
- **Leads to**: Lesson 6 (networking) discusses multi-container deployments where smaller images matter for pull/startup speed. Kubernetes (Part 7) cares deeply about image size for fast cluster scaling.
