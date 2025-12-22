# Lesson 14: Building the Production Dockerfile Skill - Summary

### Core Concept
Skills encode recurring decision patterns into reusable intelligence. After containerizing 5+ applications, six consistent decisions emerge (language/framework, base image, dependency strategy, build efficiency, security posture, observability). Encoding these decisions as a skill—using Persona + Questions + Principles—eliminates rediscovery across future projects and ensures consistency at organizational scale.

### Key Mental Models
- **Tacit Knowledge → Explicit System**: Before skills, containerization expertise lived in your mental model; outsiders couldn't access it. The skill makes reasoning explicit and testable: anyone reading Persona + Questions + Principles understands the logic.
- **Six Decision Points**: Language selection → Base image choice → Dependency installation strategy → Build layer optimization → Security posture → Observability requirements. Every Dockerfile answers these six questions. Skills codify the answers.
- **Principles as Constraints**: Principles aren't tips—they're non-negotiable decision frameworks. "Use multi-stage builds" isn't optional; it's the approach every generated Dockerfile must follow. This consistency matters at scale (20 projects, 40 team members).

### Critical Patterns
- Define Persona to activate reasoning mode: "Docker containerization expert who prioritizes minimal size, security, reliability" shapes what guidance the skill offers
- Write Questions as context-gathering prompts, not checklist items: Asking "What language/framework?" forces language-specific reasoning (Python needs UV, Node.js needs npm ci, Go needs compilation)
- Establish Principles as decision frameworks: P1 (Multi-stage builds) always applies; P2 (Non-root user) always applies; exceptions are documented, not silently ignored
- Test skills across diverse project types: Python FastAPI → Node.js Express → Go HTTP server. If the skill produces inconsistent or incorrect output for different languages, refine Questions or Principles
- Version skills using semantic versioning: 1.0.0 (initial), 1.0.1 (clarification), 1.1.0 (new question), 2.0.0 (breaking change in Principles)

### Common Mistakes
- Creating skills too early—before recognizing a pattern appears 3+ times, skills add premature abstraction and maintenance burden
- Writing skills without testing—designing Persona + Questions + Principles in isolation; not validating skill output against real projects across multiple languages
- Treating principles as suggestions—allowing exceptions without documenting them ("distroless is better but we used slim because...") erodes skill consistency
- Neglecting maintenance—skills become stale as Docker best practices evolve; Docker Hardened Images are introduced, new Python versions release, alpine fixes bugs. Update skills or they decay
- Skipping documentation—skill README should explain when to invoke it ("Use when containerizing an application") and what to expect from output

### Connections
- **Builds on**: Lessons 1-13 (skill encodes all accumulated Docker knowledge into systematic form)
- **Leads to**: Broader intelligence accumulation—skills for Kubernetes deployment (Helm), testing (pytest with Docker), CI/CD orchestration. The skill pattern scales to any recurring decision workflow
