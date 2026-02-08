---
sidebar_position: 5
chapter: 10
lesson: 5
title: "Security Hardening & Least Privilege"
description: "Implement security best practices by creating non-root users, managing permissions, securing SSH access, and safely managing API keys without hardcoding"
keywords: ["security", "least privilege", "chmod", "chown", "SSH keys", "permissions", "environment variables"]
duration_minutes: 75

# HIDDEN SKILLS METADATA
skills:
  - name: "User and Group Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Security"
    measurable_at_this_level: "Student can create dedicated non-root users for running agents"

  - name: "File Permissions Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Security"
    measurable_at_this_level: "Student can use chmod and chown to set appropriate file permissions"

  - name: "SSH Key Authentication"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Security"
    measurable_at_this_level: "Student can generate SSH key pairs and configure key-based authentication"

  - name: "Environment Variable Secret Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Security"
    measurable_at_this_level: "Student can pass secrets to agents using environment variables without hardcoding"

  - name: "Least Privilege Security Mindset"
    proficiency_level: "B2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Critical Thinking"
    measurable_at_this_level: "Student explains why running agents as root is dangerous"

learning_objectives:
  - objective: "Create dedicated non-root users for running agents with minimal required permissions"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates agent-user, configures ownership, and verifies agent runs with restricted privileges"

  - objective: "Secure SSH access using key-based authentication and disable password logins"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student generates SSH keys, configures authorized_keys, disables password authentication"

  - objective: "Manage file permissions using chmod/chown and pass secrets via environment variables"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student sets 600 permissions on sensitive files, exports environment variables with API keys"

cognitive_load:
  new_concepts: 9
  concepts_list:
    - "User and group management (useradd, usermod)"
    - "File permissions (chmod: rwx, octal notation)"
    - "Ownership management (chown, chgrp)"
    - "SSH key generation (ssh-keygen)"
    - "Authorized_keys configuration"
    - "Disabling password authentication"
    - "Environment variables for secrets"
    - "sudo configuration (visudo)"
    - "Service user creation"
  assessment: "9 concepts (within B2 limit of 7-10) ✓"

teaching_approach: "Error analysis with intentional security failures to demonstrate risks"
modality: "Error Analysis (intentional security failures to demonstrate risks)"

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-02-08"
version: "1.0.0"
---

# Security Hardening & Least Privilege

## Security is Non-Negotiable for Production Systems

In Lesson 4, you learned to automate agent tasks with bash scripts. Those scripts work, but they're running with more power than they need. When you deploy Digital FTEs to production servers, **every unnecessary permission is a potential attack surface**.

Think of it this way: If your agent only needs to read log files, why should it have permission to delete system directories? If an attacker compromises your agent, they inherit whatever permissions your agent had. More permissions = more damage when things go wrong.

**The principle you'll apply**: **Least Privilege** — grant only the minimum permissions required to do the job, nothing more.

This lesson teaches you to lock down your server for production agent deployment. You'll create dedicated users, manage file permissions, secure SSH access, and safely handle API keys without hardcoding them in your scripts.

**By the end, you'll have**:
- Created a dedicated service user for running agents
- Configured file permissions that protect sensitive data
- Set up SSH key-based authentication
- Learned to pass secrets through environment variables

---

## The Danger of Running as Root

Before learning security practices, let's understand what we're preventing.

### Why Running Everything as Root is Dangerous

**Execute this** (on a test system only):

```bash
# Check current user
whoami
```

**Output**:
```
yourname
```

Most developers work as their own user account, then use `sudo` when admin access is needed. But imagine if you ran your AI agent as root:

```bash
# DANGEROUS: Don't actually run this
sudo python3 my-agent.py
```

If this agent has a vulnerability or bug, an attacker could:
- Delete any file on the system (agents have root access)
- Install malicious software (no permission checks)
- Steal other users' data (full filesystem access)
- Create backdoors (complete system control)

**The worst part**: You might not even realize it happened until weeks later.

### The Least Privilege Principle

**Least Privilege** means: give each process only the permissions it needs to do its job, nothing more.

| Agent Type | Permissions Needed | What It CAN'T Do |
|------------|-------------------|------------------|
| **Log Reader Agent** | Read `/var/log/agent-data/` | Write anywhere, delete anything, modify system settings |
| **Email Sender Agent** | Access email API, read templates | Modify system configs, read other agents' data |
| **Backup Agent** | Read source dirs, write to backup location | Delete source files, modify system settings |

**What emerges**: Even if an attacker compromises the Log Reader Agent, they can only read logs—they cannot delete files, install malware, or damage the system.

---

## Phase 1: User and Group Management

### Creating a Dedicated Service User

Your agents shouldn't run as your personal user, and definitely not as root. They need their own service account.

**Execute**:

```bash
# Create a service user for agents
sudo useradd -r -s /bin/bash -d /var/agents agent-user

# Verify creation
id agent-user
```

**Output**:
```
uid=999(agent-user) gid=999(agent-user) groups=999(agent-user)
```

**What these flags do**:
- `-r` = Create a system account (UID < 1000, no home directory creation)
- `-s /bin/bash` = Set bash as the shell
- `-d /var/agents` = Set home directory to `/var/agents`

**Check the user was created**:

```bash
# View user entry in /etc/passwd
grep agent-user /etc/passwd
```

**Output**:
```
agent-user:x:999:999::/var/agents:/bin/bash
```

### Setting Up the Agent Directory

**Execute**:

```bash
# Create the agent directory with proper ownership
sudo mkdir -p /var/agents
sudo chown agent-user:agent-user /var/agents
sudo chmod 755 /var/agents

# Verify permissions
ls -la /var | grep agents
```

**Output**:
```
drwxr-xr-x  2 agent-user agent-user 4096 Feb  8 10:30 agents
```

**Permission breakdown** (`drwxr-xr-x`):
- `d` = Directory (not a file)
- `rwx` (owner) = agent-user can read, write, execute
- `r-x` (group) = agent-user's group can read, execute
- `r-x` (others) = Everyone else can read, execute

This means agent-user owns the directory and has full control, while others can only access it (not modify).

### Adding Your User to the Agent Group

Sometimes you need to manage agent files without switching users.

**Execute**:

```bash
# Add yourself to the agent-user group
sudo usermod -a -G agent-user $USER

# Verify (log out and back in for this to take effect)
groups $USER
```

**Output**:
```
yourname sudo agent-user
```

Now you can read/execute files in `/var/agents` without using `sudo`.

---

## Phase 2: File Permissions with chmod and chown

### Understanding Permission Notation

Linux uses two permission notation systems:

**Symbolic notation** (human-readable):
```
rwx r-x r--
^^^ ^^^ ^^^
 |   |   |
 |   |   others (everyone else)
 |   group
 owner
```

**Octal notation** (numeric):
```
rwxr-xr-- = 754
^^^
|||
||+-- others permission (4 = read-only)
|+--- group permission (5 = read + execute)
+---- owner permission (7 = read + write + execute)
```

**Permission values**:
- `4` = Read (r)
- `2` = Write (w)
- `1` = Execute (x)
- Add them up: `7` (4+2+1) = all permissions, `5` (4+1) = read + execute

### Setting Permissions on Agent Files

**Execute**:

```bash
# Switch to agent-user
sudo -u agent-user bash

# Create a test file
echo "#!/bin/bash
echo 'Agent running'" > /var/agents/test-agent.sh

# Exit back to your user
exit
```

**Execute**:

```bash
# Make it executable by owner only
sudo chmod 700 /var/agents/test-agent.sh

# Verify
ls -la /var/agents/test-agent.sh
```

**Output**:
```
-rwx------ 1 agent-user agent-user 35 Feb  8 10:30 test-agent.sh
```

**What 700 means**:
- Owner (agent-user): read, write, execute
- Group: no permissions
- Others: no permissions

Only agent-user can read, modify, or run this script.

### Changing Ownership

Sometimes you need to transfer file ownership.

**Execute**:

```bash
# Create a file as your user
echo "config: value" > /var/agents/config.yaml

# Change ownership to agent-user
sudo chown agent-user:agent-user /var/agents/config.yaml

# Set permissions (owner can read/write, group can read)
sudo chmod 640 /var/agents/config.yaml

# Verify
ls -la /var/agents/config.yaml
```

**Output**:
```
-rw-r----- 1 agent-user agent-user 13 Feb  8 10:30 config.yaml
```

**What 640 means**:
- Owner: read + write
- Group: read only
- Others: no permissions

Agent-user can modify config, group members can read it, everyone else is blocked.

---

## Phase 3: SSH Key Authentication

### Why SSH Keys Are More Secure Than Passwords

Password authentication has vulnerabilities:
- Weak passwords can be guessed
- Password reuse across systems
- Brute-force attacks try thousands of passwords
- Humans accidentally share passwords

**SSH keys** solve this:
- Private key never leaves your machine
- Public key stored on server is useless without private key
- Much harder to brute-force than passwords

### Generating SSH Keys

**Execute**:

```bash
# Generate SSH key pair (ed25519 is modern and secure)
ssh-keygen -t ed25519 -C "your-email@example.com"
```

**Output**:
```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/yourname/.ssh/id_ed25519): [Press Enter]
Enter passphrase (empty for no passphrase): [Enter a strong passphrase]
Enter same passphrase again: [Repeat passphrase]
```

**What happened**:
- Private key saved to `~/.ssh/id_ed25519`
- Public key saved to `~/.ssh/id_ed25519.pub`
- Passphrase adds extra security (required to use the key)

### Copying Your Public Key to the Server

**Execute**:

```bash
# Display your public key
cat ~/.ssh/id_ed25519.pub
```

**Output**:
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAb7r... your-email@example.com
```

**On your server**, create the authorized_keys file:

```bash
# Create .ssh directory for your user
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Add your public key to authorized_keys
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAb7r... your-email@example.com" >> ~/.ssh/authorized_keys

# Set correct permissions
chmod 600 ~/.ssh/authorized_keys

# Verify
cat ~/.ssh/authorized_keys
```

### Testing SSH Key Authentication

**From another terminal**, test logging in without password:

```bash
# Test SSH connection (replace with your server details)
ssh yourname@localhost
```

If configured correctly, it logs you in using the key (prompts for passphrase if you set one).

### ⚠️ CRITICAL: Before Disabling Passwords

**KEEP A BACKUP SESSION OPEN** before disabling passwords. If something goes wrong, you need a working connection to fix it.

**Test your SSH key works** BEFORE proceeding:
1. Open a second terminal window
2. Connect using SSH key
3. If successful, keep that session open
4. Only then disable password auth in your main session

### Disabling Password Authentication

**Edit SSH configuration**:

```bash
sudo nano /etc/ssh/sshd_config
```

**Find and modify these lines**:

```bash
# Disable password authentication
PasswordAuthentication no

# Disable empty passwords
PermitEmptyPasswords no

# Require SSH keys for all users (optional, strict)
PubkeyAuthentication yes
```

**Save and restart SSH**:

```bash
# Save: Ctrl+O, Enter
# Exit: Ctrl+X

# Test SSH config syntax first
sudo sshd -t

# If no errors, restart SSH
sudo systemctl restart sshd

# Verify it's running
sudo systemctl status sshd
```

**⚠️ CRITICAL**: Keep your backup session open and test SSH key login from a NEW terminal before closing anything.

If you locked yourself out, you'll need console access to fix it.

---

## Phase 4: Managing Secrets with Environment Variables

### Never Hardcode API Keys

**DANGEROUS** (don't do this):

```bash
# BAD: API key in script
api_key="sk-1234567890abcdef"
curl -H "Authorization: Bearer $api_key" https://api.example.com
```

**Problems**:
- API key visible in version control
- Anyone with file access can steal it
- Hard to rotate (update) keys

**SAFE approach**: Use environment variables.

### Setting Environment Variables

**Temporary (current session only)**:

```bash
# Set environment variable
export OPENAI_API_KEY="sk-1234567890abcdef"

# Verify it's set
echo $OPENAI_API_KEY
```

**Persistent (add to `.bashrc` or `.env` files)**:

```bash
# Add to .bashrc
echo 'export OPENAI_API_KEY="sk-1234567890abcdef"' >> ~/.bashrc

# Reload
source ~/.bashrc

# Verify
echo $OPENAI_API_KEY
```

### Using Environment Variables in Scripts

**Create agent script**:

```bash
sudo -u agent-user bash

cat > /var/agents/api-agent.sh << 'EOF'
#!/bin/bash
# Script uses environment variable, not hardcoded key

if [ -z "$OPENAI_API_KEY" ]; then
    echo "ERROR: OPENAI_API_KEY not set"
    exit 1
fi

echo "Agent running with API key configured"
# curl -H "Authorization: Bearer $OPENAI_API_KEY" https://api.example.com

exit

EOF

chmod 700 /var/agents/api-agent.sh
exit
```

**Run the agent**:

```bash
# Set the key
export OPENAI_API_KEY="sk-1234567890abcdef"

# Run as agent-user
sudo -u agent-user OPENAI_API_KEY="$OPENAI_API_KEY" /var/agents/api-agent.sh
```

**Output**:
```
Agent running with API key configured
```

### Using .env Files for Production

**Create `.env` file** (in `/var/agents`):

```bash
sudo -u agent-user bash

cat > /var/agents/.env << EOF
OPENAI_API_KEY=sk-1234567890abcdef
AGENT_NAME=log-reader
LOG_PATH=/var/log/app.log
EOF

# Secure the file (only owner can read)
chmod 600 /var/agents/.env

exit
```

**Load `.env` in your script**:

```bash
sudo -u agent-user bash

cat > /var/agents/agent-with-env.sh << 'EOF'
#!/bin/bash

# Load environment variables from .env
if [ -f /var/agents/.env ]; then
    export $(grep -v '^#' /var/agents/.env | xargs)
fi

# Now use the variables
echo "Agent: $AGENT_NAME"
echo "Log path: $LOG_PATH"
echo "API key configured: $([ -n "$OPENAI_API_KEY" ] && echo "YES" || echo "NO")"

EOF

chmod 700 /var/agents/agent-with-env.sh
exit
```

**Run it**:

```bash
sudo -u agent-user /var/agents/agent-with-env.sh
```

**Output**:
```
Agent: log-reader
Log path: /var/log/app.log
API key configured: YES
```

**Why this works**:
- `.env` file has 600 permissions (only agent-user can read)
- API key never appears in scripts
- Easy to update keys without modifying code
- `.env` can be excluded from version control

---

## Security Best Practices Summary

### File Permission Guidelines

| File Type | Recommended Permissions | Why |
|-----------|------------------------|-----|
| **Scripts** | `700` or `750` | Only owner executes (or owner + group) |
| **Config files** | `600` or `640` | Only owner reads/writes (or group reads) |
| **Directories** | `755` or `750` | Owner has full access, others can enter |
| **`.env` files** | `600` | ONLY owner can read (contains secrets) |
| **SSH keys** | `600` (private), `644` (public) | Private key must be protected |

### User Management Guidelines

| Practice | Command | Purpose |
|----------|---------|---------|
| **Service users** | `sudo useradd -r -s /bin/bash agent-user` | Dedicated accounts for agents |
| **Group access** | `sudo usermod -a -G groupname user` | Grant shared access without sudo |
| **Switch users** | `sudo -u agent-user command` | Run commands as that user |
| **Verify ownership** | `ls -la /path/to/file` | Check permissions before deploying |

### SSH Security Checklist

- [ ] SSH keys generated with strong passphrase
- [ ] Public key added to `~/.ssh/authorized_keys`
- [ ] `.ssh` directory has `700` permissions
- [ ] `authorized_keys` has `600` permissions
- [ ] Password authentication disabled in `/etc/ssh/sshd_config`
- [ ] SSH config tested with `sshd -t`
- [ ] **Backup session kept open** during restart
- [ ] SSH login tested from new terminal before closing backup

---

## Try With AI

Let's apply security principles to your agent deployments with AI collaboration.

**🔒 Design Your Permission Model**:

> "I'm deploying three types of AI agents to production:
> 1. LogReaderAgent (reads /var/log/app/)
> 2. BackupAgent (reads /var/data/, writes to /backup/)
> 3. EmailAgent (sends emails via API, reads email templates)
>
> For each agent, design:
> - What Linux user/group should it run as?
> - What file permissions does it need?
> - What directories should it own vs access?
> - What permissions should it NOT have?
>
> Present this as a security table showing user, permissions, and restrictions for each agent."

**What you're learning**: Translating agent requirements into specific permission models that follow least privilege principles.

**🛡️ SSH Security Audit**:

> "I'm hardening SSH access for a server that hosts AI agents. Help me create a security checklist:
> 1. What SSH configuration changes should I make?
> 2. How do I safely disable password authentication without locking myself out?
> 3. What should I test before and after making changes?
> 4. What are the recovery steps if something goes wrong?
>
> Give me a step-by-step procedure with safety checks at each step."

**What you're learning**: Building safety-first procedures for critical security changes, including rollback planning.

**🔐 Secret Management Strategy**:

> "I have 5 AI agents that need API keys to different services (OpenAI, Anthropic, SendGrid, Stripe, AWS). Currently they're hardcoded in scripts—which I know is bad.
>
> Help me design a better approach:
> 1. Should I use one .env file per agent or one shared .env file?
> 2. How do I load environment variables in bash scripts?
> 3. How do I ensure .env files are secure (permissions, ownership)?
> 4. What's the process for rotating API keys without downtime?
>
> Recommend the production-ready approach and explain why it's better than hardcoding."

**What you're learning**: Designing scalable secret management that works across multiple agents while maintaining security.
