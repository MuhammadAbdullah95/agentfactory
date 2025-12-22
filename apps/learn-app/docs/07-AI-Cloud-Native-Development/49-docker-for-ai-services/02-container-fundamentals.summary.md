### Core Concept
Images are immutable templates that define how to package and run software. Containers are executable instances created from images. This template-instance separation is fundamental to Docker: one image creates many containers, each isolated and independent, like a class definition spawning multiple objects.

### Key Mental Models
- **Image Immutability**: Once an image is built, it never changes. This guarantees reproducibility—pulling `python:3.12-slim` today and in six months yields identical images. Any change requires building a new image.
- **Copy-on-Write Layers**: Images are stacked read-only layers (base OS, dependencies, code). When a container runs, Docker adds a writable layer on top. Changes are isolated to the writable layer and discarded when the container dies. The image stays pristine.
- **Layers Enable Efficiency**: A 150MB Python base layer shared across 10 images means only 150MB on disk, not 1.5GB. Docker's caching system reuses unchanged layers during builds, making rebuilds fast.

### Critical Patterns
- **Image vs Container Distinction**: Use `docker images` to see templates. Use `docker ps -a` to see instances (both running and stopped). This distinction is essential for understanding container cleanup and reuse.
- **Pull Once, Run Many**: `docker pull python:3.12-slim` downloads the template once. You can `docker run` it a thousand times without re-downloading—each run creates a new container.
- **Layer Inspection**: `docker history image:tag` shows what each layer contains and its size. Identifying bloated layers guides optimization (Lesson 5).
- **Port Mapping vs Container Ports**: The container has internal ports. Port mapping (`-p host:container`) tunnels from your machine to the container. Without mapping, external clients can't reach the service.

### Common Mistakes
- **Assuming container changes persist**: Storing important data in containers is lost when the container is deleted. Use volumes (Lesson 6) for persistence, not the container's writable layer.
- **Misunderstanding immutability**: Thinking "I can edit files in a running container and have them persist"—you can edit them, but the changes are in the writable layer and lost on container death.
- **Conflating image tags with unique images**: `python:3.12-slim` is a moving target—it points to different images as Python releases patches. For true immutability, reference images by digest (`python@sha256:...`).
- **Running too many containers from the same image**: While efficient, debugging becomes confusing when multiple containers are identical. Use container names and network aliases to distinguish them.

### Connections
- **Builds on**: Lesson 1 (installation) provided the Docker Engine and basic understanding. This lesson dives into what Docker actually manages.
- **Leads to**: Lesson 3 (Dockerfile) shows how to build custom images. Lessons 4-7 add operational concerns—debugging, optimization, networking.
