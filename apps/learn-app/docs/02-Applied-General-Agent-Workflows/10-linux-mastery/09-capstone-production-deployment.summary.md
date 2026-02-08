### Core Concept
**Specification-first deployment separates production engineering from vibe coding**—write complete requirements BEFORE implementation, validate systematically against those requirements, package as repeatable artifacts. The critical insight: **you cannot validate against requirements you haven't defined**.

### Key Mental Models
- **Specification as Contract**: Specs define WHAT (intent, requirements, success criteria) not HOW—implementation follows, validation proves compliance
- **Layered Validation**: Existence → Permissions → Functionality → Resilience → Security creates systematic testing framework
- **Orchestration over Implementation**: You define requirements and orchestrate AI execution; AI handles implementation details
- **Deployment as Asset**: Complete packages (spec, scripts, validation, documentation) are sellable products, not personal automation

### Critical Patterns
- **Specification Structure**: Intent → Requirements (functional, non-functional, security, operational) → Constraints → Success Criteria → Validation creates complete contract
- **Three Roles in Spec-Driven Work**: AI teaches production patterns you don't know; you teach AI your deployment constraints; together you converge on optimal solution
- **Automated Validation**: Systematic testing scripts prove each requirement is met with clear pass/fail reporting
- **Deployment Packaging**: README, deployment spec, automated scripts, runbooks, troubleshooting guides create handoff-ready artifacts
- **Iterative Refinement**: Spec → AI implementation → Your refinement → Convergence produces better solutions than either alone

### Common Mistakes
- **Implementation without specification**: Starting with "deploy my agent" instead of defining requirements leads to generic, non-validated deployments
- **Vague success criteria**: "Service works" vs "systemctl is-active returns active, curl /health returns 200, logs write to /var/log/"
- **Missing security validation**: Deploying without proving non-root execution, file permissions, SSH hardening, API key protection
- **No resilience testing**: Assuming services work without testing crash recovery, reboot survival, resource limit enforcement
- **Poor documentation**: Deployment packages without runbooks create operational silos where only the original author can troubleshoot
