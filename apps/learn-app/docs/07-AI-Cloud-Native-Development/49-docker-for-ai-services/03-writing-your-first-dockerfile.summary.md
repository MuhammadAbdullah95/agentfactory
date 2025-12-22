### Core Concept
A Dockerfile is a recipe for building images. Each instruction (FROM, COPY, RUN, CMD) creates or modifies a layer. Understanding Dockerfile structure teaches you how to package applications systematically and predict what each build step accomplishes.

### Key Mental Models
- **Dockerfile as Build Instructions**: FROM sets the base, COPY brings in files, RUN executes commands during build, CMD specifies the startup command. Each instruction stacks on previous ones—the order determines the final image.
- **Layer Caching Acceleration**: Docker caches layers. If you change line 5 (your code) but not line 3 (dependencies), Docker reuses the cached dependency layer and only rebuilds line 5. Proper instruction order (dependencies before code) makes builds fast.
- **Build Context Efficiency**: `docker build .` sends your entire directory to Docker (the build context). `.dockerignore` excludes unnecessary files, speeding up builds and reducing layer overhead.

### Critical Patterns
- **FROM→WORKDIR→COPY→RUN→EXPOSE→CMD Structure**: This order is conventional and enables caching. FROM establishes baseline, WORKDIR organizes files, COPY brings in assets, RUN installs/configures, EXPOSE documents ports, CMD specifies entrypoint.
- **Separate Dependencies from Code**: Copy `requirements.txt` and install (creates a layer), then copy code separately. When code changes, the dependency layer is cached—huge speedup in local development.
- **Use --no-cache-dir with pip**: pip caches downloaded packages by default. In Docker, cache is useless (layers are isolated) and only adds size. Always use `pip install --no-cache-dir`.
- **Test Images Before Deploying**: `docker build`, `docker run`, verify locally, then push to registry. Don't rely on production as your first test.

### Common Mistakes
- **Copying all files at once**: `COPY . .` early in the Dockerfile means any file change invalidates the cache for all subsequent steps. Better: copy dependencies, install, then copy code.
- **Running RUN with shell expansion**: `RUN echo "$VAR"` doesn't work as expected in Docker because the variable isn't expanded until the container runs (too late). Set ENV variables or use environment substitution carefully.
- **Ignoring image size**: Starting with `python:3.12` (900MB) instead of `python:3.12-slim` (150MB) wastes 750MB per image. For most Python services, slim is sufficient.
- **Forgetting entrypoint details**: CMD in JSON format `["uvicorn", "main:app"]` is better than shell format `uvicorn main:app`. JSON format avoids shell interpretation issues.

### Connections
- **Builds on**: Lesson 2 (images/containers) explained what images are. This lesson teaches how to create them.
- **Leads to**: Lesson 4 (debugging) helps you fix Dockerfiles that build but fail at runtime. Lesson 5 (optimization) reduces image bloat through multi-stage builds.
