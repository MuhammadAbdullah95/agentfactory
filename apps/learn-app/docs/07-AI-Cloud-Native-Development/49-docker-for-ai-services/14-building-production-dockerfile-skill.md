---
sidebar_position: 14
chapter: 49
lesson: 14
duration_minutes: 60
title: "Building the Production Dockerfile Skill"
proficiency_level: B1
teaching_stage: 3
stage_name: "Intelligence Design"
stage_description: "Create reusable AI skills from accumulated Docker knowledge"
cognitive_load:
  concepts_count: 8
  scaffolding_level: "Light"
learning_objectives:
  - id: LO1
    description: "Identify recurring patterns worth encoding as reusable skills"
    bloom_level: "Analyze"
  - id: LO2
    description: "Design a skill using Persona + Questions + Principles pattern"
    bloom_level: "Create"
  - id: LO3
    description: "Write skill instructions that produce consistent, high-quality output"
    bloom_level: "Create"
  - id: LO4
    description: "Test skills against diverse project types (Python, Node.js, Go)"
    bloom_level: "Evaluate"
  - id: LO5
    description: "Iterate on skill design based on output quality analysis"
    bloom_level: "Create"
  - id: LO6
    description: "Document skills for team reuse with clear invocation patterns"
    bloom_level: "Create"
  - id: LO7
    description: "Version skills using semantic versioning"
    bloom_level: "Apply"
  - id: LO8
    description: "Publish skills to shared team directory with proper structure"
    bloom_level: "Apply"
digcomp_mapping:
  - objective_id: LO2
    competency_area: "3. Digital Content Creation"
    competency: "3.4 Programming"
  - objective_id: LO3
    competency_area: "2. Digital Communication and Collaboration"
    competency: "2.3 Collaboration through Digital Channels"
---

# Building the Production Dockerfile Skill

You've now written Dockerfiles for multiple applications. Each time, you've followed a similar process: choose a base image, analyze dependencies, set up the runtime environment, optimize layer ordering. If you find yourself repeating the same reasoning pattern across projects, that's a signal—the pattern is worth encoding as reusable intelligence.

This lesson transforms accumulated Docker knowledge into a reusable skill. Instead of rewriting this pattern for every containerization task, you'll create a skill that AI can invoke to produce production-ready Dockerfiles consistently, regardless of project type.

---

## What Makes a Pattern Worth Encoding?

Not every workflow deserves a reusable skill. A skill is valuable when:

1. **Recurrence**: The pattern appears in 3+ different contexts
2. **Complexity**: The pattern involves 5+ decision points
3. **Organizational value**: The pattern will accelerate future projects

Docker containerization meets all three criteria:

- **Recurrence**: Every Python service needs containerization, every Node.js app, every Go binary
- **Complexity**: You must decide base image, dependency strategy, multi-stage structure, security posture, health checks
- **Organizational value**: Encoding this pattern saves hours across the team's next 20 projects

The Docker containerization pattern is worth encoding as a skill.

---

## Recognizing the Decision Pattern

Before writing the skill, analyze what decisions you've been making:

**Decision 1: Language & Framework**
- What language is this? (Python, Node.js, Go, Rust)
- What's the entry point? (uvicorn, node, compiled binary)

**Decision 2: Base Image**
- What official image exists for this language?
- Should we use slim (smaller, faster pulls) or full (more debugging tools)?
- For sensitive workloads, should we consider distroless?

**Decision 3: Dependency Strategy**
- How are dependencies declared? (requirements.txt, package.json, go.mod)
- Are there native extensions that require build tools?
- Should we use UV for Python, or Poetry?

**Decision 4: Build Efficiency**
- Can we separate build dependencies from runtime?
- Should we copy requirements before source code (maximize cache hits)?
- What files can we exclude (.git, __pycache__, node_modules)?

**Decision 5: Security Posture**
- Should the application run as non-root?
- Do we need secrets handling?
- What Linux distro minimizes attack surface?

**Decision 6: Observability**
- Should we include a HEALTHCHECK instruction?
- Do we need proper signal handling (PID 1)?
- What logging infrastructure does the service expect?

These six decisions recur in every containerization task. Encoding them as a skill means you don't repeat this analysis—the skill guides the reasoning.

---

## The Persona + Questions + Principles Pattern

Layer 3 skills use three components to activate reasoning mode:

**Persona**: A cognitive stance that produces the right thinking
**Questions**: Analysis prompts that force context-specific reasoning
**Principles**: Non-negotiable decisions that guide all applications

Let's build each component for Docker containerization.

### Persona: The Container Architect

```
You are a Docker containerization expert who creates production-ready images.
You prioritize minimal image size through multi-stage builds, security through
non-root users and minimal base images, and reliability through health checks
and proper signal handling.
```

This persona activates specific thinking patterns:
- "What's unnecessary and should be excluded?"
- "What could attack this service, and how do we defend?"
- "How does this container behave when orchestrated by Kubernetes?"

### Questions: Gathering Context

Before generating a Dockerfile, you need project-specific information. The skill must ask:

```
1. What language/framework? (Python/FastAPI, Node.js/Express, Go, etc.)
2. What's the entry point? (uvicorn, node, compiled binary)
3. Any special dependencies? (system libraries, native extensions, ML models)
4. Target environment? (Kubernetes, Docker Compose, serverless)
5. Security requirements? (non-root, read-only filesystem, secrets)
```

These questions aren't checklist items—they're reasoning prompts that force analysis before code generation.

### Principles: Non-Negotiable Decisions

Principles define WHAT to optimize for and WHY:

```
P1: Multi-Stage Builds
Always separate build dependencies from runtime dependencies.
Reduces image size from 500MB to 50MB for Python services.

P2: Non-Root User
Create and switch to non-root user for runtime.
Prevents container escape from compromising entire host.

P3: Minimal Base Images
Use slim or distroless. Alpine often breaks Python/Node.js—skip unless tested.

P4: Layer Optimization
COPY dependencies before code to maximize cache hits during development.

P5: Health Checks
Include HEALTHCHECK for orchestration readiness probes.

P6: Proper Labels
Add OCI-standard labels for registry metadata and discoverability.
```

Notice: These aren't "tips"—they're decision frameworks. Every Dockerfile must address each principle.

---

## Creating the Skill File

Skills live in the shared team directory using a specific structure:

```
.claude/skills/
└── production-dockerfile/
    └── SKILL.md
```

The directory name matches the skill's function. The SKILL.md file contains the complete specification.

Create the directory:

```bash
mkdir -p .claude/skills/production-dockerfile
```

**Output:**
```
$ mkdir -p .claude/skills/production-dockerfile
$ ls -la .claude/skills/production-dockerfile/
total 0
drwxr-xr-x  2 user  staff  64 Dec 22 14:30 .
```

Now create SKILL.md with frontmatter and content:

```markdown
---
name: "production-dockerfile"
description: "Generate production-ready Dockerfiles with multi-stage builds, security best practices, and optimization. Use when user asks to containerize an application or create a Dockerfile."
version: "1.0.0"
---

# Production Dockerfile Skill

## Persona

You are a Docker containerization expert who creates production-ready images. You prioritize:
- Minimal image size through multi-stage builds
- Security through non-root users and minimal base images
- Reliability through health checks and proper signal handling
- Maintainability through clear documentation and labeling

## Questions to Ask

Before generating a Dockerfile, gather:

1. **What language/framework?** (Python/FastAPI, Node.js/Express, Go, etc.)
2. **What's the entry point?** (uvicorn, node, compiled binary)
3. **Any special dependencies?** (system libraries, native extensions)
4. **Target environment?** (Kubernetes, Docker Compose, serverless)
5. **Security requirements?** (non-root, read-only filesystem, secrets)

## Principles (Non-Negotiable)

### P1: Multi-Stage Builds
Always use multi-stage builds to separate build dependencies from runtime.

### P2: Non-Root User
Create and switch to a non-root user for the runtime stage.

### P3: Minimal Base Images
Use slim or distroless images. Prefer in order:
1. Language-specific slim (python:3.12-slim)
2. Docker Hardened Images (docker/python:3.12-dhi)
3. Distroless (gcr.io/distroless/python3)

### P4: Layer Optimization
- COPY dependencies before code
- Combine RUN commands
- Clean package manager caches

### P5: Health Checks
Include HEALTHCHECK instruction for orchestration readiness.

### P6: Proper Labels
Add OCI-standard labels for registry metadata.

## Output Template

\`\`\`dockerfile
# Build stage
FROM {base-image}-slim AS builder
WORKDIR /app
{install-build-deps}
COPY {dependency-file} .
RUN {install-dependencies}

# Runtime stage
FROM {base-image}-slim
RUN groupadd -r app && useradd -r -g app app
WORKDIR /app
COPY --from=builder {artifacts} {destination}
COPY --chown=app:app {source-files} .
USER app
HEALTHCHECK --interval=30s --timeout=3s CMD {health-check}
EXPOSE {port}
LABEL org.opencontainers.image.title="{app-name}"
CMD {entrypoint}
\`\`\`
```

---

## Testing the Skill Across Project Types

A skill is only valuable if it produces consistent, high-quality output. Test against different project types to verify the skill works universally.

### Test 1: Python FastAPI Service

**Invocation**:
```
Use the production-dockerfile skill to create a Dockerfile for a Python FastAPI
service. The service is called "agent-api", uses uvicorn for serving, has dependencies
in requirements.txt, and needs a health check at /health. Target: Kubernetes.
```

**Expected Output**:
```dockerfile
# Build stage
FROM python:3.12-slim AS builder
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.12-slim
RUN groupadd -r app && useradd -r -g app app
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --chown=app:app . .
USER app
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8000/health || exit 1
EXPOSE 8000
LABEL org.opencontainers.image.title="agent-api"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Analysis**: The skill correctly applied P1 (multi-stage), P2 (non-root user), P3 (python:3.12-slim), P4 (dependencies before source), P5 (health check with curl), and P6 (labels).

### Test 2: Node.js Express Service

**Invocation**:
```
Use the production-dockerfile skill to create a Dockerfile for a Node.js Express
service called "api-gateway". Dependencies are in package.json and package-lock.json.
Entry point is npm start. Health check at /status. Target: Docker Compose for development.
```

**Expected Output**:
```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

# Runtime stage
FROM node:20-alpine
RUN addgroup -g 1001 -S nodejs && adduser -S nodejs -u 1001
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --chown=nodejs:nodejs . .
USER nodejs
HEALTHCHECK --interval=30s --timeout=3s CMD wget --quiet --tries=1 --spider http://localhost:3000/status || exit 1
EXPOSE 3000
LABEL org.opencontainers.image.title="api-gateway"
CMD ["npm", "start"]
```

**Analysis**: Skill correctly adapted for Node.js (alpine base, npm ci, different health check mechanism). All principles still applied despite language change.

### Test 3: Go HTTP Server

**Invocation**:
```
Use the production-dockerfile skill to create a Dockerfile for a compiled Go HTTP
server. Binary is built via "go build -o server main.go". Listens on :9000. Needs
health check at /ping. Target: Kubernetes.
```

**Expected Output**:
```dockerfile
# Build stage
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o server main.go

# Runtime stage
FROM scratch
COPY --from=builder /app/server /server
USER nobody
EXPOSE 9000
LABEL org.opencontainers.image.title="go-server"
HEALTHCHECK --interval=30s --timeout=3s CMD ["/server", "-health-check"]
CMD ["/server"]
```

**Analysis**: Skill recognized Go's minimal runtime needs (distroless/scratch is safe here). Still applied multi-stage, health checks, labels. Correctly avoided non-root user requirement for scratch image.

---

## Iteration: Refining the Skill

After testing, you might discover gaps. For example:

**Observation**: The Node.js test used alpine, but alpine can cause issues with native modules. The skill should ask about native dependencies.

**Iteration**: Update the Questions section to ask: "Any native modules that require compilation?" This guides toward node:20 slim if yes, alpine if no.

**New version**: 1.0.1 (PATCH: improved Questions for Node.js)

Versioning matters. When skills change, update the version in the frontmatter:
- 1.0.0 → 1.0.1 (PATCH: minor clarifications)
- 1.0.0 → 1.1.0 (MINOR: new questions or principles)
- 1.0.0 → 2.0.0 (MAJOR: breaking changes, removed principles)

---

## Publishing the Skill

Once tested and documented, commit it to the team repository:

```bash
cd .claude/skills/production-dockerfile
git add SKILL.md
git commit -m "skill: add production-dockerfile v1.0.0

Encodes multi-stage, security-hardened Dockerfile generation pattern.
Tests: Python FastAPI, Node.js Express, Go HTTP server.
Principles: Multi-stage builds, non-root users, minimal images,
layer optimization, health checks, OCI labels."
```

**Output**:
```
[main abc1234] skill: add production-dockerfile v1.0.0
 1 file changed, 120 insertions(+)
 create mode .claude/skills/production-dockerfile/SKILL.md
```

The skill is now available to your team. When someone asks Claude to containerize an application, reference the skill:

```
Use the production-dockerfile skill from .claude/skills/production-dockerfile/
to create a Dockerfile for this service...
```

Claude loads the skill and applies its Persona + Questions + Principles pattern.

---

## Why Skills Matter (Intelligence Accumulation)

Creating this skill wasn't busy work. It was intelligence capture. Before, containerization knowledge lived only in your mental model. Now it's:

- **Explicit**: Anyone reading SKILL.md understands the reasoning
- **Reusable**: Applied to Python, Node.js, Go, Rust, any language
- **Improvable**: As Docker best practices evolve, update one file (not every project's Dockerfile)
- **Teachable**: New team members can apply enterprise containerization standards immediately

This is Layer 3 in practice: turning tacit knowledge into reusable organizational capability.

Your six decisions (language, base image, dependencies, efficiency, security, observability) are now encoded. The next 20 containerization tasks don't require rediscovering these principles. The skill ensures consistency at scale.

---

## Try With AI

Choose an application from your recent work (or this fictional scenario):

**Setup**: You have a new service that needs containerization. It's a Python service using SQLAlchemy for database access, has system-level dependencies (PostgreSQL client libraries), and will run in a Kubernetes cluster.

**Part 1: Establish Context**

Ask AI: "I need to containerize a Python service called 'data-processor' that uses SQLAlchemy to query PostgreSQL. The service runs scheduled jobs and connects to a database at runtime. What questions should I ask before writing the Dockerfile?"

Review AI's response. Does it ask about the entry point? Dependencies? Security? Compare to the Questions section in our skill.

**Part 2: Apply the Skill**

Ask AI: "Now use the production-dockerfile skill from .claude/skills/production-dockerfile/ to generate a Dockerfile for this data-processor service. It has dependencies in requirements.txt, uses Python 3.12, and needs to run as a non-root user in Kubernetes. Include a health check that verifies database connectivity."

Examine the generated Dockerfile. Verify:
- Does it use multi-stage builds (P1)?
- Non-root user created (P2)?
- Base image appropriate for databases (P3)?
- Dependencies copied before source (P4)?
- Health check present (P5)?
- OCI labels added (P6)?

**Part 3: Evaluate & Refine**

Ask yourself: "Did the Dockerfile answer all my concerns? What would I change?" Common refinements:

- Health check too simplistic? Ask AI to enhance it with database ping logic
- Image size concern? Request distroless variant if application allows
- Secrets handling needed? Ask about ENV vs build-time secrets

**Part 4: Test the Output**

If you have a real service available: Build the image and run it. Verify:
- Does it build successfully?
- Does the health check work?
- Can you docker exec into it for debugging?

**Part 5: Capture Learning**

If you needed to modify the skill's output:
- Was the Persona insufficient? Refine it
- Did the Questions miss something? Add it
- Did a Principle not apply? Document the exception

This feedback loop keeps the skill sharp.
