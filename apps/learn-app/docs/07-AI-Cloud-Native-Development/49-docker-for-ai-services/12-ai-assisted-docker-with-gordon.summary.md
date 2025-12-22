# Lesson 12: AI-Assisted Docker with Gordon - Summary

### Core Concept
Gordon (Docker's embedded AI agent) accelerates Dockerfile generation and debugging through collaborative reasoning, not automation. You describe constraints, Gordon suggests implementations, you evaluate and refine through iteration. The goal is faster, better Dockerfiles through AI partnership, not replacement of engineering judgment.

### Key Mental Models
- **Evaluation > Acceptance**: AI suggestions are starting points, not finished products. Always ask: "Do these match MY constraints? What assumptions did AI make? What tradeoffs am I accepting?"
- **Constraint Clarity Drives Quality**: Vague requests ("Create a Dockerfile") produce generic boilerplate. Specific constraints ("Python 3.12, Alpine base, non-root user, health check at /health, production-ready") produce tailored solutions.
- **Iteration as Collaboration**: Best Dockerfiles emerge through rounds: initial suggestion → your evaluation → your refinement request → Gordon's adaptation. Each round adds specificity and surface your implicit constraints.

### Critical Patterns
- Ask Gordon diagnostic questions before debugging manually—exit code 137 suggests OOM; Gordon can identify this pattern without you reading logs for 30 minutes
- Request optimizations with explicit tradeoffs—"Reduce size under 200MB while maintaining reliability" gives Gordon clear targets instead of "make it smaller"
- Refine suggestions through constraint education—tell Gordon when distroless breaks your requirements (no curl for health checks), when multi-stage adds too much maintenance burden, when simplicity matters more than optimization
- Override Gordon when it contradicts domain knowledge—if Gordon suggests Alpine for Python/NumPy but you know Alpine breaks your builds, use slim instead and explain why

### Common Mistakes
- Accepting Gordon's first suggestion without evaluation—multi-stage builds, distroless images, and exotic base images need validation in your project before production
- Providing insufficient project context—generic requests produce generic Dockerfiles; structure details (dependencies, entry points, target environment) guide better suggestions
- Trusting Gordon's assumptions about your project—Gordon guesses single app.py and requirements.txt; your modular structure (api/, models/, config/) needs explicit description
- Forgetting Gordon is pattern-matching, not reasoning—Gordon suggests distroless for Go (correct), but distroless for Node.js without curl (wrong for health checks). Your evaluation catches these gaps.

### Connections
- **Builds on**: Lessons 1-11 (understanding Docker deeply allows you to evaluate Gordon's suggestions critically)
- **Leads to**: Lesson 13 (capstone uses Gordon for optimization), Lesson 14 (skill design encodes the evaluation patterns you apply here)
