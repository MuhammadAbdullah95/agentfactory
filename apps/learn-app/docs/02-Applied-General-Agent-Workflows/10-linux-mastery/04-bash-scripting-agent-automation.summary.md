### Core Concept
**Bash scripting transforms manual command sequences into repeatable, testable automation.** Scripts capture deployment knowledge as executable code that can be versioned, debugged, and improved over time. When you automate with scripts, you eliminate manual errors and save time on repetitive tasks.

### Key Mental Models
- **Scripts as Captured Knowledge**: Every deployment you'll do more than once should be scripted. Scripts encode your expertise into reusable, testable form.
- **Error Handling is Non-Negotiable**: Scripts that fail silently are dangerous. Use `set -euo pipefail` to exit immediately on errors, undefined variables, or pipe failures.
- **Idempotency**: Scripts should be safe to run multiple times. Use `mkdir -p` (safe if exists), check before creating, and kill existing processes before starting new ones.
- **Text Processing Pipelines**: `grep` finds patterns, `sed` transforms text, `awk` extracts fields. Chain them together to parse logs and extract insights without manual scrolling.
- **Functions as Reusable Blocks**: Package repeated logic into functions with parameters. This makes scripts modular, testable, and easier to maintain.

### Critical Patterns
- **Shebang and Permissions**: Start scripts with `#!/bin/bash` (shebang line). Make executable with `chmod +x script.sh`. Execute with `./script.sh`.
- **Variables for Flexibility**: Use variables instead of hard-coded paths. `AGENT_DIR="/var/agents/${AGENT_NAME}"` makes scripts adaptable. Override variables at runtime: `AGENT_NAME="bot" ./script.sh`.
- **Command Substitution**: `OUTPUT=$(command)` captures command output in variables. Use this to check process IDs, test file existence, or parse configuration.
- **Error Handling Patterns**: `set -euo pipefail` at script start. Define error functions: `error_exit() { echo "ERROR: $1" >&2; exit 1; }`. Use `|| error_exit "message"` for custom error messages.
- **grep/sed/awk for Logs**: `grep ERROR file.log` finds errors. `sed 's/pattern/replacement/g'` transforms text. `awk '{print $NF}'` extracts fields. Chain them: `grep ERROR | awk '{print $NF}' | sort | uniq -c`.
- **Cron for Scheduling**: `crontab -e` edits scheduled tasks. Format: `* * * * * command` (minute, hour, day, month, weekday). `*/5 * * * *` = every 5 minutes.

### Common Mistakes
- **Silent Failures**: Scripts that continue after errors produce misleading results. Always use `set -e` or explicit error checking.
- **Hard-Coded Paths**: Paths like `cd /home/yourname/project` break for other users. Use variables and `${HOME}` or relative paths.
- **Missing Error Messages**: Generic errors ("Script failed") don't help debugging. Use descriptive messages: `error_exit "Failed to create directory: ${AGENT_DIR}"`.
- **Not Testing in Safe Environment**: Scripts with `rm -rf` can delete everything. Always test in VM, container, or test directory first.
- **Forgetting Background Process Management**: Using `&` to background processes creates zombies on exit. Use systemd services or proper process management (coming lessons).
