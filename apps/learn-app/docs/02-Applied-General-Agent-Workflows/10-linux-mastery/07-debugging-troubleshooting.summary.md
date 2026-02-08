### Core Concept
**Systematic diagnosis beats random troubleshooting**—production debugging follows a hierarchy: gather evidence (logs, metrics), isolate the problem layer (network? disk? permissions?), fix root cause (not symptoms). The critical insight: **logs don't just show what happened—they reveal why**.

### Key Mental Models
- **Diagnostic Hierarchy**: Network problems occur at layers (interface → local connectivity → DNS → remote service); diagnose bottom-up to isolate failure
- **Evidence-Based Debugging**: Each hypothesis requires testing (journalctl for service logs, curl for HTTP, ping for ICMP) before proceeding
- **Resource Exhaustion Patterns**: Services fail predictably when resources run out (memory OOM kills, disk full prevents writes, connection leaks exhaust file descriptors)
- **Temporal Filtering**: Problems manifest within time windows (--since, --until filters) and understanding when failures occurred is as important as what failed

### Critical Patterns
- **journalctl Filtering**: Priority levels (-p err), service units (-u), time ranges (--since) isolate relevant log entries
- **Network Layer Testing**: ip addr → ping → nslookup → curl systematically isolates where connectivity fails
- **Resource Monitoring**: df -h for disk, du for directory sizes, htop for process resource consumption identify bottlenecks
- **Real-Time Observation**: tail -f and journalctl -f show agent behavior as it occurs, revealing intermittent issues
- **Log Rotation**: logrotate prevents disk space issues by compressing and deleting old logs automatically

### Common Mistakes
- **Treating symptoms not causes**: Restarting crashed services without identifying why they crashed (memory leaks, config errors, resource exhaustion)
- **Skipping diagnostic hierarchy**: Assuming network problems when service logs show permission errors
- **Missing time context**: Looking at all logs instead of filtering to when the problem occurred
- **Ignoring resource limits**: Not checking disk space or memory when services fail mysteriously
- **Reactive not proactive**: Only checking logs when something breaks instead of monitoring trends
