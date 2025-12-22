# Lesson 10: Docker Compose for Development - Summary

### Core Concept
Docker Compose translates declarative YAML specifications into running multi-container environments. A single `docker-compose up` command orchestrates services, networks, volumes, and dependencies—replacing manual container startup, network configuration, and service ordering with infrastructure-as-code that runs consistently across machines.

### Key Mental Models
- **Infrastructure as Code**: The `compose.yaml` file is your application's deployment blueprint. Unlike shell scripts that hide complexity in commands, YAML makes relationships explicit—dependencies, networks, and storage are visible at a glance.
- **Service Discovery by Name**: Within the Compose network, services reach each other by name (`db:5432`, `cache:6379`). The network automatically resolves service names to container IPs. No manual host configuration required.
- **Declarative Ordering**: The `depends_on` configuration with health checks ensures services start in the correct order. Composition waits for database readiness before starting the API, preventing race conditions.

### Critical Patterns
- Write compose.yaml with top-level sections: `services` (what runs), `networks` (how they communicate), `volumes` (persistent storage), `environment` (configuration)
- Configure dependencies with health checks: `depends_on: db: condition: service_healthy` ensures the database is ready before dependent services start
- Use named volumes for persistence: `pgdata:/var/lib/postgresql/data` creates storage that survives `docker-compose down`
- Bind mount source code for development: `./src:/app` syncs local changes into running container for instant feedback
- Aggregate logs across services: `docker-compose logs` shows all service output in one stream; `docker-compose logs service-name` filters by service

### Common Mistakes
- Omitting health checks in `depends_on`—relying on `service_started` instead of `service_healthy` causes dependent services to fail when they connect to unprepared services
- Mixing development and production in one compose file—forgetting that development prioritizes reloadability (bind mounts, exposed ports) while production prioritizes immutability (image digests, hidden ports)
- Not understanding volume persistence—deleting volumes with `docker-compose down -v` when intending only to stop services
- Using loose service names that clash—naming a service "db" when the team already has a convention for "postgres-db"

### Connections
- **Builds on**: Lesson 8 (volumes), Lesson 3 (Dockerfile), Lesson 7 (security configuration as environment variables)
- **Leads to**: Kubernetes concepts (Lesson 50 covers how Kubernetes pods/services replicate Compose concepts at scale)
