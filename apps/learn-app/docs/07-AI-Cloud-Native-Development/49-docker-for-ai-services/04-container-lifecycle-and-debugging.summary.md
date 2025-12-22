### Core Concept
Containers fail in ways that differ from local applications. You can't attach a debugger or inspect the filesystem directly—you must rely on logs, introspection commands, and understanding the container lifecycle. Mastering these debugging tools is essential for production reliability.

### Key Mental Models
- **Logs as Primary Truth**: `docker logs` shows everything the main process wrote to stdout/stderr. This is your first and often only window into container behavior. Applications must log errors to stdout, not to files that disappear when containers die.
- **Inspect for Configuration Verification**: `docker inspect` reveals the actual configuration applied—environment variables, port mappings, restart policies, user context. Misconfigured containers show you what's wrong through inspect output.
- **Memory and CPU Limits Prevent Cascading Failures**: Without limits, a runaway process consumes all host resources, crashing other containers. With limits, it fails gracefully in isolation. AI workloads need both memory AND CPU limits configured.

### Critical Patterns
- **Read Logs First**: Container crashes? Check `docker logs container_id`. Most failures are immediately visible in output.
- **docker exec for Runtime Inspection**: When logs don't explain everything, `docker exec -it container /bin/sh` lets you explore the running system—check file permissions, inspect environment, test connectivity.
- **Exit Codes Tell You Why**: Exit code 137 = OOM kill (memory limit hit). Exit code 1 = application error. Exit code 0 = exited normally. `docker inspect --format='{{.State}}'` includes the exit code.
- **Port Conflicts are Simple to Debug**: Can't bind to port 8000? Check what's using it: `lsof -i :8000` on the host. Docker error messages are usually explicit.
- **OOM Kills are Silent Failures**: Container just disappears. Check `docker inspect` for `OOMKilled: true`. Prevent by setting `--memory` limits during testing.
- **Restart Policies Enable Resilience**: Use `--restart=unless-stopped` for production services so they recover from crashes automatically.

### Common Mistakes
- **Relying on container logs that were never written**: If a process fails before logging setup, you get no output. Ensure logging is early and robust.
- **Assuming "it works locally, so it works in Docker"**: Running on your 64GB laptop hides memory issues. Always test with `--memory` and `--cpus` limits matching production.
- **Not checking permission errors during build**: A Dockerfile works with root (default), then you switch to a non-root user—permissions that were fine for root now fail for the regular user.
- **Leaving containers in "stopped" state indefinitely**: `docker ps -a` gets cluttered. Periodically clean up old containers: `docker container prune`.

### Connections
- **Builds on**: Lesson 3 (Dockerfile) showed how to write them. This lesson teaches what goes wrong and how to fix it.
- **Leads to**: Lesson 5 (optimization) discusses memory/CPU limits in context of image tuning. Lessons 6-7 (networking) address debugging communication failures.
