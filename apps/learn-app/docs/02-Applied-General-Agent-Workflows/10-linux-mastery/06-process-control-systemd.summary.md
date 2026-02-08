### Core Concept
**systemd transforms agents from manual scripts into production services**—auto-starting on boot, auto-recovering from crashes, and logging reliably. The critical mental model: **services are managed by the OS, not by you**.

### Key Mental Models
- **Service Lifecycle**: Services exist in states (loaded, active, inactive, failed) and transition between them based on configuration and events
- **Declarative Reliability**: You declare desired state (Restart=always, Wants=dependencies); systemd enforces it through monitoring and recovery
- **Resource Containment**: Services run with bounded resources (memory, CPU, file descriptors) preventing runaway consumption
- **Dependency Ordering**: Services declare what they need (After=, Wants=, Requires=); systemd orders startup and handles cascading failures

### Critical Patterns
- **Service File Structure**: [Unit] metadata → [Service] execution → [Install] enablement creates complete service definition
- **Restart Policies**: Restart=on-failure with StartLimitBurst prevents infinite restart loops while enabling self-healing
- **Resource Limits**: MemoryMax, CPUQuota, TasksMax contain failures and prevent system-wide crashes
- **Environment Management**: EnvironmentFile separates secrets from configuration, enabling secure credential management
- **Service Templates**: @.service files enable instant scaling from 1 to 100 agent instances

### Common Mistakes
- **Running as root**: Services without User= directive run as root, creating security vulnerabilities
- **Restart=always**: Restarts even after intentional stops, preventing controlled service management
- **Hardcoded secrets**: API keys in service files commit credentials to version control
- **Missing resource limits**: Unbounded services can consume all RAM/CPU and crash the entire server
- **Requires= hard dependencies**: If dependency fails to start, service never starts—use Wants= for soft dependencies with retry
