---
sidebar_position: 10
title: "Chapter 10: Linux Mastery Quiz"
---

# Chapter 10: Linux Mastery Quiz

Test your understanding of Linux command-line skills for Digital FTE deployment.

<Quiz
  title="Chapter 10: Linux Mastery Assessment"
  questions={[
{
      question: "What is the primary reason AI agents live on Linux servers rather than development machines?",
      options: [
        "Linux is free to use",
        "Servers provide 24/7 availability",
        "Linux has better graphics",
        "Development machines lack storage"
      ],
      correctOption: 2,
      explanation: "AI agents require continuous operation (24/7) which production servers provide. Development machines are intermittent, lack internet connectivity stability, and aren't designed for long-running processes. Your Digital FTEs work while you sleep, on servers that never go offline. Free cost (A) is unrelated—many OS options are free. Graphics (C) are irrelevant—servers are headless. Storage (D) matters less than uptime and reliability.",
      source: "Lesson 1: The CLI Architect Mindset"
    },,
{
      question: "Which command shows your current location in the Linux filesystem?",
      options: [
        "ls -la",
        "cd ~",
        "pwd",
        "whereami"
      ],
      correctOption: 2,
      explanation: "pwd (print working directory) displays your current filesystem path, like checking your location on a map before navigating. ls -la (A) lists files in current directory. cd ~ (C) changes to home directory but doesn't show location. whereami (D) isn't a valid Linux command. Always pwd before navigation operations to avoid getting lost in complex directory structures.",
      source: "Lesson 1: The CLI Architect Mindset"
    },,
{
      question: "In the Linux filesystem hierarchy, which directory stores system-wide configuration files?",
      options: [
        "/home",
        "/etc",
        "/var",
        "/usr"
      ],
      correctOption: 2,
      explanation: "/etc contains configuration files for the entire system—agent settings, service configs, network parameters. /home (A) is user-specific data. /var (C) holds variable data like logs. /usr (D) contains installed programs. Your Digital FTE configurations live in /etc/agents/ for system-wide access. This separation organizes static configs (/etc) from dynamic data (/var) and user data (/home).",
      source: "Lesson 1: The CLI Architect Mindset"
    },,
{
      question: "What is the difference between a terminal emulator and a shell?",
      options: [
        "They are the same thing",
        "Terminal is the interface, shell interprets commands",
        "Shell displays graphics, terminal processes text",
        "Terminal executes programs, shell manages memory"
      ],
      correctOption: 1,
      explanation: "The terminal is the window/interface you type into (hardware). The shell (bash, zsh) is software that reads and executes your commands. Think: terminal = telephone, shell = person who listens and responds. They're distinct (A is wrong). Shells don't display graphics (C)—terminals are text-only. Neither manages memory directly (D)—the kernel handles memory. This distinction matters when debugging agent startup scripts across different shells.",
      source: "Lesson 1: The CLI Architect Mindset"
    },,
{
      question: "Which path type always starts from the root directory (/)?",
      options: [
        "Relative path",
        "Absolute path",
        "Symbolic link",
        "Home directory path"
      ],
      correctOption: 2,
      explanation: "Absolute paths start from root (/) providing complete route: /var/agents/config.yaml. They're unambiguous and work from any directory. Relative paths (A) start from current location: config.yaml. Symbolic links (C) are file pointers, not path types. Home directory paths (D) like ~/agents are relative to your home. Use absolute paths in scripts for reliability. Use relative paths interactively for brevity. Your Digital FTE deployment scripts should use absolute paths.",
      source: "Lesson 1: The CLI Architect Mindset"
    },,
{
      question: "What does the two-step workflow 'apt update && apt install' accomplish?",
      options: [
        "Updates all packages then installs new ones",
        "Refreshes package catalog then installs specific package",
        "Installs package then updates dependencies",
        "Downloads updates then removes old packages"
      ],
      correctOption: 0,
      explanation: "apt update refreshes the catalog of available packages from repositories. apt install then downloads and installs the specific package using current catalog information. Without update first, you might install outdated versions or get 'package not found' errors. It doesn't upgrade all packages (A is wrong). Order matters—install then update (C) makes no sense. It doesn't remove old packages (D is wrong), that's apt autoremove. Always update before installing for latest versions and dependency resolution.",
      source: "Lesson 2: Modern Terminal Environment"
    },,
{
      question: "How does zoxide determine which directory to jump to when you type 'z project'?",
      options: [
        "Alphabetical sorting of directory names",
        "Most recently visited directory",
        "Frequency-based ranking with fuzzy matching",
        "Directory size prioritization"
      ],
      correctOption: 2,
      explanation: "zoxide tracks how often you visit directories and assigns them scores. When you type 'z project', it fuzzy-searches your history and jumps to the highest-ranked matching directory. It's not alphabetical (A) or most recent (B)—it's frequency-based. Directory size doesn't matter (D is wrong). After visiting ~/projects/voice-learning once, 'z voice' jumps there. This smart navigation eliminates typing long paths repeatedly. zoxide learns your workflow patterns over time.",
      source: "Lesson 2: Modern Terminal Environment"
    },,
{
      question: "What is the primary benefit of fzf (fuzzy finder) in terminal workflows?",
      options: [
        "Automatically installs packages",
        "Interactive search and selection for any list output",
        "Replaces the bash shell entirely",
        "Manages file permissions"
      ],
      correctOption: 0,
      explanation: "fzf transforms any command output into an interactive search interface. Pipe file lists, command history, or process listings to fzf, then filter by typing and select with arrow keys. It doesn't install packages (A) or replace bash (C)—it enhances bash. It doesn't manage permissions (D). Use cases: find . | fzf searches files, Ctrl+R searches command history, ps aux | fzf finds processes. fzf makes any list searchable through fuzzy matching, not exact strings.",
      source: "Lesson 2: Modern Terminal Environment"
    },,
{
      question: "Where should you add shell aliases for persistent terminal customization?",
      options: [
        "/etc/aliases",
        "~/.bashrc or ~/.zshrc",
        "/usr/local/bin/aliases",
        "~/.config/terminal.conf"
      ],
      correctOption: 1,
      explanation: "Shell configuration files ~/.bashrc (for bash) or ~/.zshrc (for zsh) are read on shell startup, making aliases persist across sessions. /etc/aliases (A) doesn't exist. /usr/local/bin/aliases (C) is for binaries, not config. ~/.config/terminal.conf (D) isn't a standard shell config location. Add aliases like 'alias agent-deploy=\"cd /var/agents\"' to ~/.bashrc, then reload with source ~/.bashrc. Your Digital FTE workflow shortcuts live here for efficiency.",
      source: "Lesson 2: Modern Terminal Environment"
    },,
{
      question: "What happens when you prefix a command with sudo?",
      options: [
        "Runs command in background",
        "Executes with superuser (root) privileges",
        "Runs command slower and safer",
        "Logs command to system journal"
      ],
      correctOption: 0,
      explanation: "sudo (superuser do) temporarily elevates privileges to root/admin level for command execution. Installing packages requires sudo because you modify system directories. It doesn't background the process (A is wrong) or slow execution (C is wrong)—it just changes permission level. Commands are logged to journalctl (D) regardless of sudo. Use sudo only for commands that need it—running everything as root violates least privilege principle. Package installation, user management, and service configuration require sudo.",
      source: "Lesson 2: Modern Terminal Environment"
    },,
{
      question: "What is tmux's primary advantage for Digital FTE management?",
      options: [
        "Automatically restarts crashed services",
        "Persistent sessions that survive SSH disconnections",
        "Replaces systemd for service management",
        "Manages file permissions automatically"
      ],
      correctOption: 1,
      explanation: "tmux creates terminal sessions that persist even when you disconnect. If your SSH connection drops during agent deployment, tmux keeps the session running—reconnect and everything is as you left it. It doesn't restart services (A)—that's systemd's job. It doesn't replace systemd (C)—tmux manages terminal sessions, not system services. It doesn't manage permissions (D). Use tmux for long-running operations (agent deploys, log monitoring) where network interruptions would otherwise lose your work. Sessions are named and attachable from anywhere.",
      source: "Lesson 3: Persistent Sessions with tmux"
    },,
{
      question: "Which tmux command creates a new named session?",
      options: [
        "tmux new -s session-name",
        "tmux create session-name",
        "tmux attach -t session-name",
        "tmux list-sessions"
      ],
      correctOption: 0,
      explanation: "tmux new -s session-name creates a new session with that name. The -s flag specifies session name. tmux create (B) isn't valid syntax. tmux attach -t (C) connects to existing session, doesn't create new. tmux list-sessions (D) shows existing sessions, doesn't create. Naming sessions makes them identifiable: tmux new -s deploy-agent creates 'deploy-agent' session. Detach with Ctrl+b then d, reattach later with tmux attach -t deploy-agent. Your deployment work persists across disconnections.",
      source: "Lesson 3: Persistent Sessions with tmux"
    },,
{
      question: "How do you detach from a tmux session without terminating it?",
      options: [
        "Ctrl+C then exit",
        "Ctrl+b then d",
        "exit command",
        "killall tmux"
      ],
      correctOption: 2,
      explanation: "Ctrl+b then d detaches from tmux session while keeping it running. Ctrl+b is the tmux prefix key, d is detach. Ctrl+C (A) interrupts current process, might terminate what's running. exit (C) closes the entire session/terminates tmux. killall tmux (D) kills all tmux sessions destructively. Detaching is like pausing a movie—you leave the theater, movie continues, return later to resume. Your agent deployment continues running in detached session while you disconnect SSH.",
      source: "Lesson 3: Persistent Sessions with tmux"
    },,
{
      question: "What is the shebang line at the top of a bash script?",
      options: [
        "A comment describing the script",
        "The path to the bash interpreter",
        "The script version number",
        "A security check directive"
      ],
      correctOption: 3,
      explanation: "#!/bin/bash (the shebang) tells the system which interpreter executes this script—bash in this case. It's not just a comment (A is wrong)—it's executable metadata. Version numbers (C) go in comments, not shebang. Security directives (D) are separate. Common shebangs: #!/bin/bash (bash), #!/usr/bin/env python3 (Python). Without shebang, script runs with default shell (sh) which has different features. Always include shebang as first line for reliable script execution.",
      source: "Lesson 4: Bash Scripting for Agent Automation"
    },,
{
      question: "How do you make a bash script executable?",
      options: [
        "chmod +x script.sh",
        "chown +x script.sh",
        "bash script.sh",
        "source script.sh"
      ],
      correctOption: 1,
      explanation: "chmod +x script.sh adds execute permission (+x) to the script file. chown +x (B) changes file owner, not permissions—wrong command. bash script.sh (C) executes script regardless of permissions (by explicitly calling bash interpreter). source script.sh (D) executes script in current shell context (for functions/variables), not as executable file. After chmod +x, run ./script.sh directly. Without execute permission, script won't run as command, only as argument to bash. Always set execute permissions on deployment scripts.",
      source: "Lesson 4: Bash Scripting for Agent Automation"
    },,
{
      question: "What is the purpose of set -e in a bash script?",
      options: [
        "Export all variables as environment variables",
        "Exit script immediately if any command fails",
        "Enable extended globbing patterns",
        "Suppress error messages from output"
      ],
      correctOption: 0,
      explanation: "set -e causes the script to exit immediately if any command returns a non-zero exit code (failure). This prevents cascading errors—if user creation fails, don't continue deploying agent that depends on that user. It doesn't export variables (A is wrong), enable globbing (C is wrong), or suppress errors (D is wrong—set -e exposes errors by failing fast). Always include set -e at the top of deployment scripts for safety. For specific commands that might fail legitimately, use '|| true' to allow failure: command || true.",
      source: "Lesson 4: Bash Scripting for Agent Automation"
    },,
{
      question: "What is the principle of 'least privilege' in Linux security?",
      options: [
        "Grant all permissions to ensure flexibility",
        "Grant only minimum permissions required for the task",
        "Grant permissions based on user seniority",
        "Grant permissions to everyone equally"
      ],
      correctOption: 2,
      explanation: "Least privilege means granting only the minimum permissions necessary—nothing more. If an agent only reads logs, it shouldn't have write permissions or system directory access. All permissions (A) maximizes attack surface. Seniority-based permissions (C) aren't task-appropriate. Equal permissions (D) ignore role differences. If attacker compromises agent with minimal permissions, damage is contained. Running everything as root means compromised agent can delete system files, install malware, steal data. Create dedicated users for each agent type with role-specific permissions.",
      source: "Lesson 5: Security Hardening & Least Privilege"
    },,
{
      question: "What does chmod 600 do to a file?",
      options: [
        "Grants read-only access to everyone",
        "Grants read-write access to owner only, no access to others",
        "Grants execute permission to all users",
        "Grants read-write access to group members"
      ],
      correctOption: 2,
      explanation: "chmod 600 means owner (first digit 6) has read+write (4+2=6), group (0) has no permissions, others (0) have no permissions. 6=4+2 (read+write). Only file owner can read or modify file. Read-only to everyone (A) would be 444. Execute to all (C) would be 111. Group read-write (D) would be 660. Use 600 for sensitive files containing API keys, passwords, secrets—only owner should access. Config files for agents: 600 (owner read-write) or 640 (owner read-write, group read). Never use 777 (all permissions) on production systems.",
      source: "Lesson 5: Security Hardening & Least Privilege"
    },,
{
      question: "Why use SSH key authentication instead of passwords?",
      options: [
        "Keys are easier to remember than passwords",
        "Keys are more resistant to brute-force and don't transmit secrets",
        "Keys allow faster login typing",
        "Keys work without network connection"
      ],
      correctOption: 0,
      explanation: "SSH keys are more secure because private key never leaves your machine, public key is useless without it, and keys are harder to brute-force than passwords. Keys aren't about memorability (A)—they're stored files. Typing speed (C) isn't the benefit—SSH with keys is still authentication, just automated. Network connection required (D is wrong)—SSH needs connectivity. Passwords can be guessed, reused across systems, transmitted during login. Keys use cryptographic challenge-response without transmitting the secret. Disable password authentication after keys are configured: PasswordAuthentication no in /etc/ssh/sshd_config. Always use SSH keys for production servers.",
      source: "Lesson 5: Security Hardening & Least Privilege"
    },,
{
      question: "How should you pass API keys to agent scripts securely?",
      options: [
        "Hardcode them in the script",
        "Store them in environment variables or .env files",
        "Put them in config files with 777 permissions",
        "Embed them in compiled binaries"
      ],
      correctOption: 3,
      explanation: "Environment variables (export OPENAI_API_KEY=sk-...) or .env files loaded by scripts keep API keys out of source code. Hardcoding keys (A) in scripts commits secrets to version control—anyone with code access has your keys. 777 permissions (C) make files readable by everyone—security nightmare. Compiled binaries (D) can be decompiled to extract keys. Use .env files with 600 permissions (owner read-only), exclude from git, load in scripts with 'source .env' or 'export $(grep -v '^#' .env | xargs)'. Rotate keys regularly without modifying code—just update .env file.",
      source: "Lesson 5: Security Hardening & Least Privilege"
    },,
{
      question: "What is chown used for in Linux file management?",
      options: [
        "Changing file permissions (read/write/execute)",
        "Changing file owner and group",
        "Creating new hidden files",
        "Checking file disk usage"
      ],
      correctOption: 3,
      explanation: "chown (change owner) modifies which user and group own a file: 'chown agent-user:agent-user config.yaml' transfers ownership to agent-user. Permissions (A) are changed with chmod, not chown. Creating hidden files (C) uses standard file creation—just prefix filename with dot. Disk usage (D) is checked with du. After copying deployment files as root, use chown to transfer ownership to service user: 'chown -R agent-user:agent-user /var/agents/'. This ensures agent runs with appropriate permissions and can read its config files.",
      source: "Lesson 5: Security Hardening & Least Privilege"
    },,
{
      question: "What is systemd's primary role in Digital FTE deployment?",
      options: [
        "Managing file permissions automatically",
        "Service management: auto-start, auto-restart, monitoring",
        "Replacing SSH for remote access",
        "Managing network firewall rules"
      ],
      correctOption: 3,
      explanation: "systemd is the service manager that keeps your Digital FTEs running: starts them on boot, restarts on failure, monitors resource usage. It doesn't manage file permissions (A)—that's chmod/chown. It doesn't replace SSH (C)—SSH manages remote login. Firewalls (D) are managed separately (ufw, iptables). Without systemd, your agent stops when you log out and doesn't restart after crashes. Systemd service files (/etc/systemd/system/agent.service) define: ExecStart (what command runs), Restart (auto-restart policy), User (runs as non-root). Your Digital FTE reliability depends on systemd.",
      source: "Lesson 6: Process Control with systemd"
    },,
{
      question: "Which systemd directive causes a service to restart when it crashes?",
      options: [
        "AutoStart=on-failure",
        "Restart=on-failure",
        "CrashRecovery=enabled",
        "KeepAlive=yes"
      ],
      correctOption: 0,
      explanation: "Restart=on-failure tells systemd to restart the service if it crashes (exits with non-zero code). Restart=always would restart even if you manually stop the service (unwanted behavior). AutoStart (A) doesn't exist—WantedBy=multi-user.target enables auto-start on boot. CrashRecovery (C) isn't a valid directive. KeepAlive (D) is from Upstart init system, not systemd. Use Restart=on-failure with RestartSec=5 (5 second delay) to prevent restart loops. Your Digital FTE recovers from crashes automatically with this directive.",
      source: "Lesson 6: Process Control with systemd"
    },,
{
      question: "How do you enable a systemd service to start automatically on system boot?",
      options: [
        "systemctl start service-name",
        "systemctl enable service-name",
        "systemctl boot service-name",
        "systemctl activate service-name"
      ],
      correctOption: 1,
      explanation: "systemctl enable service-name configures service to start automatically on system boot. systemctl start (A) starts service immediately but doesn't enable auto-start. systemctl boot (C) doesn't exist. systemctl activate (D) doesn't exist—start is the command. After enabling, service starts on boot without manual intervention. Critical for Digital FTEs—if server reboots and service isn't enabled, your agent stays offline until you manually start it. Always verify with systemctl is-enabled service-name.",
      source: "Lesson 6: Process Control with systemd"
    },,
{
      question: "What command shows real-time logs for a systemd service?",
      options: [
        "journalctl -u service-name",
        "journalctl -u service-name -f",
        "systemctl logs service-name",
        "tail -f /var/log/service-name.log"
      ],
      correctOption: 1,
      explanation: "journalctl -u service-name -f follows (streams) logs for that service in real-time, similar to tail -f. The -f flag enables follow mode. journalctl -u service-name (A) shows logs once, doesn't stream new entries. systemctl logs (C) isn't valid—logs are in journalctl, not systemctl. tail -f specific log file (D) might work if service logs to file, but systemd services log to journal by default. Real-time log streaming lets you watch agent behavior as it happens, debugging issues immediately rather than after the fact.",
      source: "Lesson 6: Process Control with systemd"
    },,
{
      question: "What is the first diagnostic command when a systemd service won't start?",
      options: [
        "journalctl -u service-name",
        "systemctl status service-name",
        "ps aux | grep service-name",
        "tail -f /var/log/syslog"
      ],
      correctOption: 1,
      explanation: "systemctl status service-name is your first diagnostic—it shows whether service is running/failed, recent log lines, and exit codes. This quick overview guides next steps. journalctl (A) shows full logs—run after status indicates problem. ps aux (C) checks if process is running—useful but doesn't explain why service failed. syslog (D) contains everything—too broad initially. systemctl status gives you the immediate context: loaded, active/inactive, recent errors. If status shows 'failed', journalctl reveals the root cause.",
      source: "Lesson 7: Debugging & Troubleshooting"
    },,
{
      question: "How do you test network connectivity to a remote server?",
      options: [
        "ping server-hostname",
        "curl -I https://server-hostname",
        "Both ping and curl",
        "netstat -an"
      ],
      correctOption: 3,
      explanation: "Use both ping (ICMP connectivity) and curl (HTTP connectivity) for systematic diagnosis. ping tests if host is reachable at network level. curl -I tests if HTTP service responds (returns headers). Either alone is insufficient—ping might succeed while HTTP fails (service down, firewall blocks HTTP). netstat (D) shows local network connections, not remote connectivity. Diagnostic sequence: ping gateway → ping remote host → curl HTTP endpoint. If ping fails: network problem. If ping works, curl fails: application/firewall problem. Systematic diagnosis isolates failure layer.",
      source: "Lesson 7: Debugging & Troubleshooting"
    },,
{
      question: "What command checks disk space usage in human-readable format?",
      options: [
        "du -h",
        "df -h",
        "ls -lh",
        "fdisk -l"
      ],
      correctOption: 0,
      explanation: "df -h (disk free, human-readable) shows disk usage for filesystems: available space, used percentage. Essential for detecting disk-full conditions that crash services. du -h (A) shows directory sizes, not filesystem space—useful for finding space hogs but not overall disk health. ls -lh (C) lists files with sizes in current directory. fdisk -l (D) shows disk partitions, not free space. When agents crash mysteriously, run df -h first—98% disk usage causes service failures. Clean logs with logrotate, monitor with automated alerts.",
      source: "Lesson 7: Debugging & Troubleshooting"
    },,
{
      question: "What is the purpose of specification-first deployment methodology?",
      options: [
        "Reduce deployment time by skipping planning",
        "Define requirements before implementation for systematic validation",
        "Generate code automatically without human review",
        "Eliminate need for testing"
      ],
      correctOption: 0,
      explanation: "Specification-first means writing complete requirements (functional, security, operational) with success criteria BEFORE implementing. This enables systematic validation—you prove deployment meets requirements, not hope it works. It doesn't reduce planning time (A)—it INVESTS in planning to prevent rework. It doesn't eliminate human review (C)—you validate AI's output against spec. It increases testing (D)—systematic validation vs random checks. Without specification, you can't validate because you never defined success. Every production deployment needs spec first.",
      source: "Lesson 9: Capstone - Production Deployment"
    },,
{
      question: "Which specification section defines what you will NOT do in the deployment?",
      options: [
        "Intent",
        "Constraints",
        "Success Criteria",
        "Security Requirements"
      ],
      correctOption: 1,
      explanation: "Constraints section explicitly states what's OUT OF SCOPE—what you won't do. This prevents scope creep and manages expectations. Intent (A) defines WHAT you're building. Success Criteria (C) defines HOW you validate it works. Security Requirements (D) define protection measures. Constraints might say: 'No Docker (use native systemd)', 'No load balancing (single server)', 'No auto-scaling (fixed resources)'. This limits scope to what's achievable, prevents 'just add this feature' expansion during implementation. Clear constraints keep deployment focused and manageable.",
      source: "Lesson 9: Capstone - Production Deployment"
    },,
{
      question: "What does the 'What emerged' narrative pattern demonstrate in AI collaboration?",
      options: [
        "AI teaching the user exclusively",
        "User teaching AI exclusively",
        "Iterative refinement producing better solution than either started with",
        "User working alone without AI"
      ],
      correctOption: 3,
      explanation: "The 'What emerged' pattern captures convergence—where iteration between human and AI produces solutions neither would have created alone. AI suggests patterns user doesn't know. User provides context AI lacks. Together they iterate toward optimal solution. It's not one-directional teaching (A or B)—it's bidirectional collaboration. It's not working alone (D)—AI contributes technical patterns, user contributes domain constraints. This Three Roles framework (AI as Teacher/Student/Co-Worker) demonstrates co-learning where both parties contribute and both learn. Result exceeds individual starting points.",
      source: "Lesson 9: Capstone - Production Deployment"
    },,
{
      question: "What security check validates that your agent runs as non-root user?",
      options: [
        "grep PasswordAuthentication /etc/ssh/sshd_config",
        "ps aux | grep service-name and check username column",
        "systemctl status service-name",
        "journalctl -u service-name -n 50"
      ],
      correctOption: 0,
      explanation: "ps aux lists all running processes with usernames. Grep for your service name and check the first column (username)—should show your service user (e.g., 'digital-fte'), NOT root. SSH config check (A) validates password authentication is disabled. systemctl status (C) shows if service is running, not what user. journalctl (D) shows logs, not process ownership. Running as root violates least privilege—if attacker compromises agent, they get full system access. Always verify process ownership: ps aux | grep agent-name should show dedicated user, not root.",
      source: "Lesson 5: Security Hardening & Least Privilege"
    },,
{
      question: "What is log rotation and why is it necessary for Digital FTEs?",
      options: [
        "Compressing logs to save disk space and prevent filesystem filling",
        "Encrypting logs for security compliance",
        "Deleting logs immediately after creation",
        "Sending logs to remote monitoring service"
      ],
      correctOption: 3,
      explanation: "Log rotation archives and compresses old logs, then deletes them after a retention period (e.g., 7 days). This prevents log files from consuming all disk space—runaway logs fill filesystems and crash services. It doesn't encrypt logs (B)—that's separate security measure. It doesn't delete immediately (C)—old logs are retained temporarily. It might include remote sending (D) but rotation's primary purpose is disk management. Configure logrotate in /etc/logrotate.d/—set daily rotation, keep 7 days, compress old logs. Your Digital FTEs run 24/7 generating logs—rotation prevents disk exhaustion.",
      source: "Lesson 7: Debugging & Troubleshooting"
    },,
{
      question: "What is the difference between absolute and relative paths for agent deployment scripts?",
      options: [
        "Absolute paths work from any directory, relative paths depend on current location",
        "Relative paths are more secure than absolute paths",
        "Absolute paths are shorter to type than relative paths",
        "Relative paths work across different filesystems"
      ],
      correctOption: 0,
      explanation: "Absolute paths (/var/agents/config.yaml) work regardless of current directory because they start from root. Relative paths (config.yaml) depend on where you are—running script from wrong directory breaks it. Relative paths aren't more secure (B). Absolute paths are typically longer (C). Neither works across different filesystems (D)—if path doesn't exist, both fail. Use absolute paths in scripts for reliability—scripts work from anywhere. Use relative paths interactively for convenience. Your Digital FTE deployment scripts should use absolute paths for reliability: /var/agents/ not ./agents/.",
      source: "Lesson 1: The CLI Architect Mindset"
    },,
{
      question: "Why disable password authentication and use SSH keys only?",
      options: [
        "SSH keys are faster to type than passwords",
        "Keys resist brute-force attacks and don't transmit secrets during login",
        "Passwords don't work over network connections",
        "SSH keys are required by law in all countries"
      ],
      correctOption: 2,
      explanation: "SSH keys are more secure because private key stays on your machine (never transmitted), and cryptographic challenge-response proves identity without sending secrets. Passwords are transmitted during login (can be intercepted), vulnerable to brute-force guessing, and humans reuse weak passwords. Speed (A) isn't the primary benefit. Passwords work over networks (C) but insecurely. Not legally required (D)—it's security best practice. After configuring SSH keys, disable password authentication: set 'PasswordAuthentication no' in /etc/ssh/sshd_config. Keep backup session open before restarting sshd—test key login from new terminal before closing backup.",
      source: "Lesson 5: Security Hardening & Least Privilege"
    },,
{
      question: "What is the purpose of the .env file in Digital FTE deployment?",
      options: [
        "Store environment variables including API keys and configuration",
        "List all files that should be excluded from git",
        "Define systemd service startup order",
        "Configure network firewall rules"
      ],
      correctOption: 3,
      explanation: ".env files store environment variables (API keys, database URLs, configuration) that scripts load at runtime. This separates secrets from code—.env isn't committed to git (excluded in .gitignore). Git exclusions (B) are in .gitignore, not .env. Service startup order (C) is defined in systemd service files (After=, Wants=, Requires=). Firewall rules (D) are configured separately (ufw, iptables). In scripts, load .env with 'source .env' or 'export $(grep -v '^#' .env | xargs)'. Set permissions 600 (owner read-only) so only service user can read secrets.",
      source: "Lesson 5: Security Hardening & Least Privilege"
    },,
{
      question: "What does systemd's EnvironmentFile directive do?",
      options: [
        "Creates new environment variables for all users",
        "Loads environment variables from file into service context",
        "Exports environment variables to global shell",
        "Backs up environment variables to /etc/environment"
      ],
      correctOption: 1,
      explanation: "EnvironmentFile=/etc/service/.env loads environment variables from that file into the service's execution context. Variables are available only to that service, not globally. It doesn't create variables for all users (A) or export globally (C)—scoped to service. No backup (D). This is how you pass API keys and configuration to services without hardcoding: service references $OPENAI_API_KEY, systemd loads value from .env file. If .env file is missing and you use Requires= directive, service fails to start (fail-safe). Secure .env with 600 permissions.",
      source: "Lesson 6: Process Control with systemd"
    },,
{
      question: "What diagnostic tool would you use to find the largest directories consuming disk space?",
      options: [
        "du -h --max-depth=1 | sort -h",
        "df -h",
        "ls -la",
        "find . -name '*' -size +100M"
      ],
      correctOption: 0,
      explanation: "du -h (disk usage, human-readable) with --max-depth=1 shows directory sizes one level deep. sort -h sorts results by size (largest last). This identifies space hogs—/var/log might be 15GB, /var/lib/docker 50GB. df -h (B) shows filesystem space remaining, not which directories are large. ls -la (C) lists files, not aggregate directory sizes. find (D) finds individual large files, not directory totals. Run du -h --max-depth=1 | sort -h in suspected large directories to find space hogs, then clean logs, remove old backups, or expand storage.",
      source: "Lesson 7: Debugging & Troubleshooting"
    },,
{
      question: "What is the validation framework layer that checks files exist and are in correct locations?",
      options: [
        "Layer 1: Existence Checks",
        "Layer 2: Permission Checks",
        "Layer 3: Functional Checks",
        "Layer 4: Resilience Checks"
      ],
      correctOption: 2,
      explanation: "Layer 1 (Existence Checks) validates that required files and directories are present: service file exists at /etc/systemd/system/, user exists, directories /var/lib/digital-fte/ created, config file exists. Before testing if things work, verify they're there. Layer 2 (B) checks permissions. Layer 3 (C) checks functionality (does service start). Layer 4 (D) checks resilience (survives crashes). Existence first—if file missing, permissions don't matter. Automated validation script checks layers sequentially, failing fast if existence checks fail.",
      source: "Lesson 9: Capstone - Production Deployment"
    },,
{
      question: "What does the specification section 'Success Criteria' define?",
      options: [
        "Who worked on the deployment",
        "Measurable tests that prove deployment meets requirements",
        "Deployment cost and timeline",
        "List of tools required for deployment"
      ],
      correctOption: 2,
      explanation: "Success Criteria define measurable, testable conditions that prove deployment meets requirements. Each criterion is testable: 'Service active after reboot', 'API returns 200 OK', 'Permissions correct'. Not who worked (A), not cost/timeline (C), not tool list (D)—those are different sections. Success criteria transform vague requirements into binary tests: pass/fail. Without success criteria, 'deployment successful' is opinion—with criteria, it's proven fact. Every requirement should map to specific success criteria. Your validation script tests each criterion systematically.",
      source: "Lesson 9: Capstone - Production Deployment"
    },,
{
      question: "What is the recommended approach for managing three different agents with different permission requirements?",
      options: [
        "Run all agents as root for simplicity",
        "Create dedicated service users for each agent with role-specific permissions",
        "Run all agents as your personal user",
        "Give all agents the same permissions to avoid complexity"
      ],
      correctOption: 1,
      explanation: "Create three dedicated service users: log-reader-agent (read access to /var/log/), backup-agent (read source dirs, write to backup location), email-agent (access email API, read templates). Each has minimum required permissions. Running all as root (A) violates least privilege—compromised agent has full system access. Your personal user (C) mixes personal and agent permissions—bad practice. Same permissions (D) defeats isolation—backup agent shouldn't read emails even though email agent can. User-per-agent isolation limits damage: compromised email agent can't read logs or backups. systemd service files specify User= directive for each agent.",
      source: "Lesson 5: Security Hardening & Least Privilege"
    },,
{
      question: "What does chmod 640 mean for a configuration file?",
      options: [
        "Owner read-write, group read, others no access",
        "Owner read-write-execute, group read-write, others read",
        "Owner read-only, group read-only, others read-only",
        "Owner read-only, group no access, others no access"
      ],
      correctOption: 3,
      explanation: "chmod 640 means: owner (6 = read+write), group (4 = read only), others (0 = no access). 6 = 4+2 (read+write). 4 = read. 0 = none. This is appropriate for config files: owner can modify, group members can read, everyone else blocked. Option B (755) would be rwxr-xr-x (execute not needed for configs). Option C (444) would be read-only for everyone (owner can't modify). Option D (400) would be owner read-only, group/others no access (group can't read). Use 640 for agent configs: service owner (agent-user) reads/writes, admin group reads, others blocked.",
      source: "Lesson 5: Security Hardening & Least Privilege"
    },,
{
      question: "How do you create a systemd service that depends on an environment file?",
      options: [
        "Add EnvironmentFile= to [Service] section only",
        "Add Requires=env-file.mount and EnvironmentFile= to service file",
        "Create a symlink from service file to env file",
        "Set environment variables in [Install] section"
      ],
      correctOption: 3,
      explanation: "To make service depend on environment file, use both Requires=etc-digital-fte-env.mount (FAIL if env file doesn't exist) and EnvironmentFile=/etc/digital-fte/.env (load variables). EnvironmentFile alone (A) loads variables but doesn't fail service if file missing. Symlink (C) doesn't create dependency. [Install] section (D) defines when service starts, not environment. The Requires directive makes startup fail-fast if config missing—better to fail immediately than start with default/broken config. This fail-safe behavior prevents services running with incomplete configuration.",
      source: "Lesson 6: Process Control with systemd"
    },,
{
      question: "What is the purpose of journalctl priority filtering (e.g., -p err -p warn)?",
      options: [
        "Delete low-priority log entries to save space",
        "Show only errors and warnings, filtering out normal messages",
        "Change log priority levels for all services",
        "Export logs to external monitoring system"
      ],
      correctOption: 1,
      explanation: "journalctl -p err -p warn filters log output to show only error (err) and warning (warn) priority messages. This filters out info/debug messages, focusing on problems. It doesn't delete logs (A)—just filters display. It doesn't change levels (C)—that's service configuration. It doesn't export logs (D)—that's separate monitoring integration. Priority levels: emerg (0), alert (1), crit (2), err (3), warning (4), notice (5), info (6), debug (7). Filter to find problems quickly: 'journalctl -u service-name -p err -p warn' shows only issues, not routine operation messages.",
      source: "Lesson 7: Debugging & Troubleshooting"
    },,
{
      question: "What is the first step in systematic network diagnosis when an agent can't reach an API?",
      options: [
        "Check application code for bugs",
        "Verify local network interface is up with ip addr",
        "Contact API provider support",
        "Reinstall the operating system"
      ],
      correctOption: 0,
      explanation: "Systematic diagnosis starts at lowest layer: check if network interface is up (ip addr show). If interface is DOWN, it's a network configuration problem, not an application problem. Checking code first (A) jumps ahead without isolating the issue. Contacting support (C) is premature—you might not have a provider problem. Reinstalling OS (D) is nuclear option reserved for hopeless cases. Diagnostic hierarchy: 1) Local interface (ip addr), 2) Local connectivity (ping gateway), 3) DNS resolution (nslookup), 4) Remote connectivity (curl). Isolate failure layer before fixing. Systematic diagnosis prevents random troubleshooting.",
      source: "Lesson 7: Debugging & Troubleshooting"
    },,
{
      question: "What is the primary purpose of the validation script in Digital FTE deployment?",
      options: [
        "Automate the deployment process",
        "Systematically test that deployment meets all specification requirements",
        "Generate documentation for the deployment",
        "Monitor the service in production"
      ],
      correctOption: 1,
      explanation: "Validation script systematically tests each requirement: files exist (Layer 1), permissions correct (Layer 2), service functional (Layer 3), survives failures (Layer 4), security hardened (Layer 5). It proves deployment matches specification, not hopes it works. Deployment automation (A) is separate (deploy.sh script). Documentation generation (C) is separate—validation produces test results, not docs. Monitoring (D) is ongoing operations—validation is one-time testing. Without validation, you have no proof deployment meets requirements. Run validation script before declaring production-ready.",
      source: "Lesson 9: Capstone - Production Deployment"
    },,
{
      question: "What is the failure scenario testing in deployment validation?",
      options: [
        "Testing that deployment fails when you deliberately break things",
        "Testing that service recovers from crashes, bad configs, resource limits",
        "Testing that validation script catches all errors",
        "Testing that documentation covers all failure modes"
      ],
      correctOption: 3,
      explanation: "Failure scenario testing validates resilience: kill process → auto-restarts, give invalid config → fails to start, exceed memory limit → gets killed. This proves deployment handles failures gracefully. Testing that deployment breaks (A) isn't useful—test that it RECOVERS. Validation script catching errors (C) is validation of the script, not the deployment. Documentation coverage (D) is documentation quality, not deployment resilience. Resilience tests (Layer 4) are disruptive—kill processes, fill disks, crash services. They prove Digital FTE survives real-world failures, not just happy-path deployment.",
      source: "Lesson 9: Capstone - Production Deployment"
    },,
{
      question: "What is the operations runbook and why is it necessary?",
      options: [
        "Script that automates deployment steps",
        "Documentation explaining how to operate, troubleshoot, and maintain the deployment",
        "List of servers and their IP addresses",
        "Legal document governing service usage"
      ],
      correctOption: 2,
      explanation: "Operations runbook documents HOW to operate the deployment: starting/stopping service, viewing logs, checking status, updating application, handling failures. It's documentation, not automation (A). Server list (C) might be inventory, not runbook. Legal document (D) is separate—terms of service, not operations guide. Runbook enables handoff—you (deployer) can go on vacation, and team can operate Digital FTE without calling you. It transforms personal automation into team asset. Include: systemctl commands, journalctl commands, troubleshooting steps, common failure modes, escalation paths. No runbook = operational bottleneck.",
      source: "Lesson 9: Capstone - Production Deployment"
    },,
{
      question: "What is the difference between Restart=always and Restart=on-failure?",
      options: [
        "No difference—they are synonyms",
        "Restart=always restarts even if manually stopped; Restart=on-failure only restarts on crash",
        "Restart=always restarts on crash only; Restart=on-failure restarts for any reason",
        "Restart=always is for services, Restart=on-failure is for timers"
      ],
      correctOption: 3,
      explanation: "Restart=always restarts service even if you manually stop it (systemctl stop). This prevents controlled service management—you can't stop the service without disabling it. Restart=on-failure only restarts if service crashes (exits with non-zero code), not if manually stopped. This is correct choice for services. They're not synonyms (A). Option C is backwards. Both are for services (D), not timers. Use Restart=on-failure so you retain control: systemctl stop works, but crashes trigger auto-restart. Combine with RestartSec=5 (5 second delay) to prevent restart loops if service crashes immediately.",
      source: "Lesson 6: Process Control with systemd"
    },,
{
      question: "What command attaches to an existing tmux session named 'work'?",
      options: [
        "tmux new -s work",
        "tmux attach -t work",
        "tmux connect work",
        "tmux join work"
      ],
      correctOption: 2,
      explanation: "tmux attach -t work attaches to existing session named 'work'. The -t flag specifies target session name. tmux new -s work (A) creates NEW session (error if 'work' already exists). tmux connect (C) and tmux join (D) aren't valid commands. After detaching (Ctrl+b then d) from session, reattach later from same machine or different SSH connection: tmux attach -t work. Everything in session continues running while detached—long-running agent deployments, monitoring operations, log analysis sessions persist across network interruptions.",
      source: "Lesson 3: Persistent Sessions with tmux"
    },
  ]}
  questionsPerBatch={18}
/>
