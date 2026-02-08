### Core Concept
**Security is about granting only the minimum permissions needed—nothing more.** Running agents as root or hardcoding API keys creates unnecessary attack surfaces. Least Privilege means each process gets only the permissions required for its job, limiting damage if compromised.

### Key Mental Models
- **Least Privilege Principle**: Give agents only the permissions they need. Log Reader Agent reads logs only—it cannot write, delete, or modify system settings. Even if compromised, damage is limited.
- **Dedicated Service Users**: Agents shouldn't run as your personal user or root. Create dedicated service accounts (`agent-user`) with minimal permissions. This isolates agents and limits blast radius.
- **File Permissions as Access Control**: `chmod` sets who can read/write/execute. `chown` sets ownership. Use these to protect sensitive files—configs with API keys get `600` (owner read/write only).
- **SSH Keys Over Passwords**: Passwords can be guessed or brute-forced. SSH keys are cryptographically stronger and never leave your machine (private key stays with you).
- **Environment Variables for Secrets**: Never hardcode API keys in scripts. Pass secrets through environment variables or `.env` files with restrictive permissions (`600`).

### Critical Patterns
- **Create Service Users**: `sudo useradd -r -s /bin/bash -d /var/agents agent-user` creates system account for running agents. Verify with `id agent-user`.
- **Permission Notation**: Symbolic: `rwxr-xr--` (owner rwx, group r-x, others r--). Octal: `750` (owner 7=rwx, group 5=r-x, others 0). `chmod 700 file` = owner only. `chmod 600 file` = owner read/write.
- **SSH Key Generation**: `ssh-keygen -t ed25519` creates modern, secure key pair. Private key stays in `~/.ssh/id_ed25519`. Public key (`~/.ssh/id_ed25519.pub`) goes to server's `~/.ssh/authorized_keys`.
- **Environment Variables**: `export VAR_NAME="value"` sets temporary variable. Add to `~/.bashrc` for persistence. Use in scripts: `${VAR_NAME}` or `$VAR_NAME`.
- **Secure .env Files**: Store secrets in `.env` files with `chmod 600` (owner read only). Load in scripts: `export $(grep -v '^#' .env | xargs)`.

### Common Mistakes
- **Running Everything as Root**: Convenience becomes vulnerability. If compromised, attacker has full system access. Create service users with minimal permissions.
- **Weak File Permissions**: Config files with API keys set to `644` (world-readable) expose secrets. Use `600` for sensitive files.
- **Hardcoding Secrets**: API keys in scripts are visible in version control and file access logs. Use environment variables or `.env` files instead.
- **Disabling Passwords Prematurely**: Turning off password authentication before testing SSH keys locks you out. Keep backup session open, test key login, then disable passwords.
- **Forgetting to Verify Permissions**: Assuming permissions are correct leads to security gaps. Always `ls -la` to verify ownership and permissions match intent.
