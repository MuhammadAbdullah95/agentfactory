### Core Concept
**Integration patterns transform components into production systems**—individual skills (systemd, tmux, scripting, security) combine through architectural patterns that scale, recover, and monitor. The critical mental model: **workflows are force multipliers; good automation deploys to 100 servers as easily as one**.

### Key Mental Models
- **Pattern Selection Framework**: Deployment complexity matches scale (single-agent vs multi-agent vs multi-tenant)—choose the right pattern for your requirements
- **Graduated Recovery**: Different failure severities need different responses (alert vs investigate vs restart vs manual intervention)
- **Automation First Principle**: If you'll do something more than once, script it—manual operations don't scale
- **Observability as Design Requirement**: Monitoring, logging, and alerting aren't afterthoughts—they're architectural requirements

### Critical Patterns
- **Multi-Agent Deployment**: Integrated deployment scripts orchestrate user creation, directory setup, service files, monitoring, and health checks
- **Zero-Downtime Deployment**: Deploy new version alongside old, smoke test, atomic swap, rollback capability enables production updates
- **Observability Stack**: Metrics collection, log aggregation, alert checking, and dashboarding provide operational visibility
- **Disaster Recovery Toolkit**: Diagnostics-first approach with mode-specific recovery (service_down, disk_full, out_of_memory) enables rapid response
- **Skill Encapsulation**: Reusable patterns packaged as skills (linux-agent-ops) capture expertise for consistent application

### Common Mistakes
- **Overengineering small deployments**: Using multi-agent patterns for single-service deployments creates unnecessary complexity
- **Missing rollback capability**: Deploying without backup and rollback strategy risks production outages
- **Reactive not proactive monitoring**: Only checking when things break instead of automated health checks and alerts
- **Poor documentation**: Deployment packages without runbooks create operational debt
- **Ignoring failure modes**: Not planning for disasters (server failures, data corruption, security breaches) guarantees catastrophic recovery time
