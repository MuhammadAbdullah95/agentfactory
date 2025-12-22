### Core Concept
User-defined networks enable containers to find and communicate with each other by hostname, solving a critical limitation of the default bridge network. This is the foundation for multi-service architectures where an agent container connects to a database container and cache container by reliable, resolvable hostnames that survive container restarts.

### Key Mental Models
- **Automatic DNS Service Discovery**: Containers on user-defined networks get Docker's internal DNS server. When one container tries to reach `postgres`, Docker resolves that hostname to the current IP address. If the postgres container restarts and gets a new IP, the hostname still resolves—your agent doesn't need reconfiguration.
- **Network Isolation as a Feature**: Containers on different networks can't communicate. This enforces architectural boundaries: your AI service network is isolated from a separate project's network, preventing accidental dependencies and name collisions.
- **Runtime Flexibility**: `docker network connect` and `docker network disconnect` modify network membership without restarting containers. A container can belong to multiple networks simultaneously, reaching containers on each network by their hostnames.

### Critical Patterns
- **Create User-Defined Bridge**: `docker network create ai-service-network`. Then `docker run --network ai-service-network ...` attaches containers. Inspect with `docker network inspect ai-service-network` to see all connected containers and their IPs.
- **Hostname Resolution Works Immediately**: No waiting, no configuration—containers on the same network can ping each other by hostname immediately. This is Docker's automatic DNS at work.
- **Network Aliases for Abstraction**: `--network-alias postgres` lets a container named `postgres-primary` respond to `postgres` too. Code references `postgres`, but the actual container can be anything. Aliases decouple hostname from container name.
- **Multi-Tier Architecture Template**: Create one network, attach agent (port-mapped for external access), database (internal only), and cache (internal only). Each connects to the others by hostname. This is the building block for production AI services.

### Common Mistakes
- **Using IP addresses instead of hostnames**: Even though you CAN find containers by IP, don't. IP addresses change on restart. Always use hostnames with user-defined networks.
- **Forgetting the network for dependent services**: Your agent connects to `postgres` by hostname, but if postgres is on a different network, connection fails. Attach all services to the same network.
- **Assuming the default bridge has DNS**: The default bridge DOES NOT have automatic DNS. Containers must use IP addresses, which breaks when IPs change. Always use user-defined networks for multi-container setups.
- **Over-complicating isolation**: You don't need separate networks for every service—one network per logical unit is typical (one for your AI app, one for your testing setup, one for a separate project). Don't create 50 networks for 3 containers.

### Connections
- **Builds on**: Lesson 6 (bridge networks, port mapping) taught basic networking. This lesson builds multi-service communication with proper isolation and service discovery.
- **Leads to**: Docker Compose (Chapter 51) automates this network creation and container coordination. Kubernetes (Part 7) extends these concepts to multi-host clusters with service discovery and load balancing.
