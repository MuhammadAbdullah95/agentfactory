---
sidebar_position: 15
title: "Chapter 10: Linux Mastery Quiz"
---

# Chapter 10: Linux Mastery Quiz

Test your understanding of Linux command-line skills for Digital FTE deployment. Each session presents a randomized selection of questions with immediate feedback.

<Quiz
  title="Chapter 10: Linux Mastery Assessment"
  questions={[
    {
      question: "What is the difference between a terminal emulator and a shell?",
      options: [
        "They are identical programs with different names",
        "Terminal displays the interface, shell interprets commands",
        "Shell handles display output, terminal processes text input",
        "Terminal runs programs directly, shell manages system memory"
      ],
      correctOption: 1,
      explanation: "The terminal emulator is the window application that displays text and captures keystrokes â€” it is the interface layer. The shell (bash, zsh) is the software running inside that terminal, reading your input, interpreting commands, and returning results. Think of the terminal as a telephone handset and the shell as the person answering. They are not identical (A) â€” you can run different shells inside the same terminal. Shells do not handle graphical display (C) â€” that is the terminal's job. Terminals do not run programs or manage memory directly (D) â€” the kernel handles memory management. Understanding this distinction matters when debugging agent startup scripts that behave differently across shell environments.",
      source: "Lesson 1: The CLI Architect Mindset"
    },
    {
      question: "Which filesystem directory stores system-wide configuration files such as agent settings and service parameters?",
      options: [
        "/home stores configuration files for all system services",
        "/var stores static configuration for installed programs",
        "/etc stores system-wide configuration files and settings",
        "/usr stores configuration alongside installed software"
      ],
      correctOption: 2,
      explanation: "/etc is the standard directory for system-wide configuration files â€” agent configs, network parameters, service settings, and authentication data all live here. The filesystem hierarchy separates concerns: /home (A) stores per-user data like personal files and shell configs, not system configurations. /var (B) holds variable runtime data such as logs, caches, and spool files â€” not static configuration. /usr (D) houses installed program binaries and libraries, not their configuration. When deploying Digital FTEs, your agent configuration files typically reside in /etc/agents/ or similar paths for system-wide accessibility.",
      source: "Lesson 1: The CLI Architect Mindset"
    },
    {
      question: "A deployment script contains the path '../config/agent.yaml'. Under what condition will this path fail to resolve correctly?",
      options: [
        "When the script is executed from a different working directory",
        "When the file agent.yaml exceeds maximum filename length",
        "When the config directory contains only hidden dotfiles",
        "When the script is executed by the root superuser account"
      ],
      correctOption: 0,
      explanation: "Relative paths like ../config/agent.yaml resolve based on the current working directory at execution time. If a cron job or systemd service runs the script from /root instead of the expected /var/agents, the relative path resolves to /config/agent.yaml â€” which likely does not exist. This is the most common deployment bug with relative paths. Filename length limits (B) are rarely hit in practice on modern filesystems. Hidden dotfiles (C) have no effect on resolving a path to a specific named file. Root user privileges (D) affect permission but not path resolution. Production deployment scripts should always use absolute paths like /var/agents/config/agent.yaml for reliability.",
      source: "Lesson 1: The CLI Architect Mindset"
    },
    {
      question: "What safety concern makes 'rm -rf /' or 'rm -rf *' extremely dangerous commands in production?",
      options: [
        "They consume excessive CPU resources during file scanning operations",
        "They recursively delete files without confirmation and cannot be undone",
        "They corrupt the filesystem journal and require a full disk reformat",
        "They only delete files owned by root but leave other files damaged"
      ],
      correctOption: 1,
      explanation: "rm -rf combines three dangerous flags: -r (recursive, delete directories and contents), -f (force, no confirmation prompts), and targets everything in scope. Once executed, deleted files are gone permanently â€” Linux has no recycle bin by default. The command does not primarily strain CPU (A) â€” it is I/O intensive but the danger is data loss, not resource consumption. It does not corrupt the filesystem journal (C) â€” it cleanly removes inodes. It deletes files regardless of ownership if run as root (D is wrong about scope). In agent deployment, always double-check rm commands and use safer alternatives like trash-put or rm -i for interactive confirmation.",
      source: "Lesson 2: Mastering File Operations"
    },
    {
      question: "Which command safely creates a deeply nested directory structure like /var/agents/configs/prod in one step?",
      options: [
        "mkdir /var/agents/configs/prod creates all parent directories",
        "touch -d /var/agents/configs/prod creates directory trees",
        "mkdir -p /var/agents/configs/prod creates parent directories as needed",
        "install -D /var/agents/configs/prod creates nested directories"
      ],
      correctOption: 2,
      explanation: "mkdir -p creates the entire directory path, automatically creating any missing parent directories along the way. Without -p, mkdir fails if /var/agents or /var/agents/configs do not already exist. Plain mkdir without flags (A) will error with 'No such file or directory' if parents are missing. touch (B) creates files not directories, and -d sets timestamps rather than creating trees. install -D (D) copies files and creates leading directories for the destination file, but does not create standalone directories. Using mkdir -p is essential in deployment scripts that set up agent directory structures on fresh servers.",
      source: "Lesson 2: Mastering File Operations"
    },
    {
      question: "You need to copy an entire agent configuration directory to a backup location. Which approach preserves the directory structure?",
      options: [
        "cp configs/ backup/ copies the directory and all nested contents",
        "cp -r configs/ backup/ recursively copies directory and contents",
        "mv configs/ backup/ moves files which inherently creates a copy",
        "cat configs/* > backup/ concatenates all files into the backup path"
      ],
      correctOption: 1,
      explanation: "cp -r (recursive) copies the directory and everything inside it, preserving the nested structure. Without -r, cp refuses to copy directories and returns an error â€” plain cp (A) only works on individual files. mv (C) moves rather than copies, so the original is gone afterward â€” that is not backing up, it is relocating. cat (D) concatenates file contents to stdout and cannot recreate directory structures. For production backups, consider cp -rp to also preserve permissions and timestamps, ensuring the backup is an exact replica of the original agent configuration.",
      source: "Lesson 2: Mastering File Operations"
    },
    {
      question: "What does the wildcard pattern 'agent-*.log' match when used with ls or rm?",
      options: [
        "Only files named exactly agent-.log in the current directory",
        "Files starting with agent- and ending with .log, with any characters between",
        "All files containing the substring agent anywhere in the filename",
        "Only files starting with agent- followed by exactly one character then .log"
      ],
      correctOption: 1,
      explanation: "The asterisk (*) glob matches zero or more characters of any kind. So agent-*.log matches agent-deploy.log, agent-001.log, agent-.log, and agent-monitoring-2025.log â€” anything starting with 'agent-' and ending with '.log'. It does not match only agent-.log (A) â€” that would be a literal match without a wildcard. It does not match 'agent' appearing anywhere (C) â€” the pattern requires 'agent-' at the start. A single character match (D) would use the ? wildcard: agent-?.log. Glob patterns are essential for managing agent log files, like rm agent-*.log.old to clean up rotated logs.",
      source: "Lesson 2: Mastering File Operations"
    },
    {
      question: "In nano, which keyboard shortcut saves the current file without exiting the editor?",
      options: [
        "Ctrl+S saves the file and remains in the editor session",
        "Ctrl+X prompts to save then exits the nano editor cleanly",
        "Ctrl+O writes the file to disk without exiting the editor",
        "Ctrl+W saves and writes all open file buffers to disk"
      ],
      correctOption: 2,
      explanation: "Ctrl+O (WriteOut) saves the current buffer to disk and keeps you in nano â€” it prompts for a filename then writes. This is the equivalent of 'Save' in graphical editors. Ctrl+S (A) does not save in nano â€” in many terminals it actually freezes the screen via XOFF flow control. Ctrl+X (B) exits nano and prompts to save unsaved changes, but you leave the editor. Ctrl+W (D) opens the search function in nano, not save. Knowing nano shortcuts is critical for quick config edits on remote servers where graphical editors like VS Code are unavailable during emergency agent troubleshooting.",
      source: "Lesson 3: Text Editing and Pipe Architecture"
    },
    {
      question: "What are the three standard I/O streams in Linux, and what are their file descriptor numbers?",
      options: [
        "input (0), output (1), log (2) handle all program communication",
        "stdin (0), stdout (1), stderr (2) are the three standard streams",
        "read (1), write (2), error (3) manage data flow for processes",
        "console (0), display (1), debug (2) route program output correctly"
      ],
      correctOption: 1,
      explanation: "Every Linux process has three standard streams: stdin (fd 0) for input, stdout (fd 1) for normal output, and stderr (fd 2) for error messages. These file descriptors are fundamental to how pipes and redirection work. Input/output/log (A) uses wrong names â€” there is no standard 'log' stream. Read/write/error (C) uses wrong names and wrong numbers â€” fd 1 is stdout, not 'read'. Console/display/debug (D) are fabricated names. Understanding these streams matters for agent deployment: you redirect stderr to log files with 2>/var/log/agent-errors.log so error messages are captured separately from normal output.",
      source: "Lesson 3: Text Editing and Pipe Architecture"
    },
    {
      question: "What does the pipe operator (|) do in the command 'ps aux | grep python | wc -l'?",
      options: [
        "Runs all three commands simultaneously in separate background processes",
        "Connects stdout of each command to stdin of the next command in sequence",
        "Creates a backup of each command's output before passing it forward",
        "Merges stdout and stderr from all commands into a single output stream"
      ],
      correctOption: 1,
      explanation: "The pipe operator takes the standard output (stdout) of the command on its left and feeds it as standard input (stdin) to the command on its right. In this chain: ps aux lists processes, its output pipes to grep python which filters for Python processes, and that filtered output pipes to wc -l which counts the lines. The commands do not run simultaneously in the way described in (A) â€” they form a pipeline where data flows sequentially. Pipes do not create backups (C) â€” data is streamed, not stored. Pipes only connect stdout, not stderr (D) â€” errors still print to the terminal unless explicitly redirected.",
      source: "Lesson 3: Text Editing and Pipe Architecture"
    },
    {
      question: "How does the redirection '2>&1' work, and when would you use it in agent deployment?",
      options: [
        "Redirects stdin to stdout so input becomes visible in terminal output",
        "Redirects stderr (fd 2) to the same destination as stdout (fd 1)",
        "Creates a second copy of stdout and labels it as error output stream",
        "Swaps stderr and stdout so errors appear in normal output position"
      ],
      correctOption: 1,
      explanation: "The syntax 2>&1 redirects file descriptor 2 (stderr) to wherever file descriptor 1 (stdout) is currently pointing. Combined with output redirection like >output.log 2>&1, both normal output and errors end up in the same log file. It does not redirect stdin (A) â€” stdin is fd 0 and is not involved. It does not duplicate stdout (C) â€” it redirects the error stream to merge with stdout. It does not swap the streams (D) â€” stderr simply follows stdout's destination. This is essential for agent logging: python agent.py >agent.log 2>&1 captures everything in one file for debugging crashes and monitoring output.",
      source: "Lesson 3: Text Editing and Pipe Architecture"
    },
    {
      question: "What is the correct two-step workflow for installing a package with apt on Ubuntu?",
      options: [
        "apt install package then apt update to refresh package metadata",
        "apt upgrade then apt install package to get the latest version first",
        "apt update to refresh catalog then apt install package from it",
        "apt search package then apt download to get the package archive"
      ],
      correctOption: 2,
      explanation: "The correct workflow is: first apt update to download the latest package catalog from repositories, then apt install <package> to install using that current catalog. Without updating first, you may install outdated versions or encounter 'package not found' errors if the catalog is stale. Installing before updating (A) risks getting old versions with known vulnerabilities. apt upgrade (B) upgrades all installed packages, which is a different operation from refreshing the catalog. apt search and apt download (D) are for discovery and offline installation, not the standard install workflow. Always update before installing, especially on freshly provisioned agent servers.",
      source: "Lesson 4: Modern Terminal Environment"
    },
    {
      question: "Which statement accurately describes the purpose of shell aliases in ~/.bashrc?",
      options: [
        "Aliases create permanent system commands that all users can access globally",
        "Aliases define shortcut names that expand to longer commands in your shell",
        "Aliases compile shell scripts into faster binary executables for performance",
        "Aliases encrypt sensitive commands so they cannot be read from shell history"
      ],
      correctOption: 1,
      explanation: "Shell aliases are text substitutions defined in your shell configuration file. When you type the alias name, the shell expands it to the full command before execution. For example, alias deploy='cd /var/agents && ./deploy.sh' lets you type 'deploy' instead of the full sequence. Aliases are per-user, not system-wide (A) â€” they live in your ~/.bashrc, not /etc. They are not compiled (C) â€” they are expanded at runtime by the shell interpreter. They do not encrypt anything (D) â€” alias definitions are plain text. Aliases streamline repetitive agent management tasks, turning common multi-step commands into single memorable shortcuts.",
      source: "Lesson 4: Modern Terminal Environment"
    },
    {
      question: "How does zoxide improve directory navigation compared to the standard cd command?",
      options: [
        "It replaces cd entirely and uses AI to predict your intended destination",
        "It tracks directory visit frequency and jumps to the best match via fuzzy search",
        "It creates symbolic links to frequently visited directories in your home folder",
        "It caches directory listings so the filesystem responds faster to navigation"
      ],
      correctOption: 1,
      explanation: "zoxide maintains a database of directories you visit, ranked by frequency (how often) and recency (how recently). When you type z project, it fuzzy-matches against this history and jumps to the highest-ranked match. It does not replace cd entirely (A) â€” cd still works, and zoxide does not use AI prediction, just frequency-based ranking. It does not create symbolic links (C) â€” it changes your working directory directly using its internal database. It does not cache directory listings (D) â€” it tracks navigation patterns, not filesystem contents. For agent developers managing multiple project directories, zoxide eliminates typing long paths like /var/agents/production/configs repeatedly.",
      source: "Lesson 4: Modern Terminal Environment"
    },
    {
      question: "What happens to a tmux session when you close the terminal window or lose your SSH connection?",
      options: [
        "The session terminates and all running processes inside it are killed",
        "The session pauses and resumes automatically when the terminal reconnects",
        "The session continues running on the server and can be reattached later",
        "The session saves state to disk and restarts processes on next login"
      ],
      correctOption: 2,
      explanation: "tmux sessions run as server processes independent of your terminal connection. When you close the window or lose SSH, the tmux server keeps the session alive with all running processes intact. You reattach with tmux attach -t session-name and everything is exactly as you left it. Sessions do not terminate on disconnect (A) â€” that is what happens without tmux, which is exactly the problem it solves. Sessions do not pause (B) â€” processes continue running, they are not suspended. tmux does not save state to disk (D) â€” it keeps sessions in memory on the running server. This is critical for long-running agent deployments over unstable network connections.",
      source: "Lesson 5: Persistent Sessions with tmux"
    },
    {
      question: "Which key sequence detaches from a tmux session without stopping it?",
      options: [
        "Press Ctrl+C to interrupt, then type exit to leave the session cleanly",
        "Press Ctrl+D to send end-of-file signal and disconnect from the session",
        "Press Ctrl+B then D to detach while the session continues in background",
        "Press Escape three times rapidly to trigger tmux emergency disconnect"
      ],
      correctOption: 2,
      explanation: "Ctrl+B is the tmux prefix key, and D (detach) tells tmux to disconnect your terminal from the session while keeping it running. You return to your original shell and the session continues in the background. Ctrl+C (A) sends an interrupt signal that may kill the foreground process inside tmux â€” it does not detach. Ctrl+D (B) sends EOF which closes the shell inside tmux, potentially terminating the session. Triple Escape (D) is not a tmux shortcut. The prefix-then-action pattern (Ctrl+B â†’ action key) is fundamental to all tmux commands and avoids conflicts with programs running inside the session.",
      source: "Lesson 5: Persistent Sessions with tmux"
    },
    {
      question: "How do you split the current tmux pane horizontally to view logs alongside a running process?",
      options: [
        "Ctrl+B then percent sign (%) splits the pane into left and right halves",
        "Ctrl+B then double-quote (\") splits the pane into top and bottom halves",
        "Ctrl+B then S creates a new horizontal split below the current pane",
        "Ctrl+B then H opens a horizontal monitoring pane for log viewing"
      ],
      correctOption: 1,
      explanation: "Ctrl+B then \" (double-quote) splits the current pane horizontally, creating a top and bottom layout. This is ideal for watching agent logs in one pane while running commands in another. Ctrl+B % (A) creates a vertical split (left and right), not horizontal. Ctrl+B S (C) is not the standard split command â€” in some configurations it lists sessions. Ctrl+B H (D) is not a default tmux binding. The visual mnemonic: \" looks like a horizontal line dividing space, while % looks like two circles side by side (vertical). Combined with tail -f on logs, horizontal splits create effective agent monitoring dashboards.",
      source: "Lesson 5: Persistent Sessions with tmux"
    },
    {
      question: "What is the purpose of a tmux session startup script for agent deployment?",
      options: [
        "It compiles tmux from source to get the latest features and patches",
        "It automates creating named sessions with predefined windows and pane layouts",
        "It encrypts tmux session traffic to prevent unauthorized network monitoring",
        "It schedules tmux sessions to start at specific times using system cron jobs"
      ],
      correctOption: 1,
      explanation: "A tmux session script automates your workspace setup: creating a named session, opening specific windows for different tasks, splitting panes, and running initial commands like tail -f on log files. Instead of manually configuring your monitoring layout each time, one script recreates your exact environment. It does not compile tmux (A) â€” that is a build task, not a session script. It does not encrypt traffic (C) â€” tmux runs locally and SSH handles encryption for remote sessions. While you could trigger scripts from cron (D), the script itself defines layout, not scheduling. Session scripts ensure every Digital FTE monitoring session starts with a consistent, productive workspace layout.",
      source: "Lesson 5: Persistent Sessions with tmux"
    },
    {
      question: "What does the shebang line '#!/bin/bash' at the top of a script file accomplish?",
      options: [
        "It marks the file as a comment block that should be ignored by interpreters",
        "It specifies which interpreter the operating system should use to execute the script",
        "It imports all built-in bash functions and libraries into the script namespace",
        "It enables strict error checking mode equivalent to set -euo pipefail"
      ],
      correctOption: 1,
      explanation: "The shebang (#!) tells the OS kernel which interpreter to use when executing the script as a program. #!/bin/bash means run this file through the bash shell interpreter. Without it, the system may use the wrong interpreter or fail entirely. It is not a comment (A) â€” while # normally starts comments in bash, #! on line 1 is special kernel syntax. It does not import functions (C) â€” bash loads its built-ins regardless of the shebang. It does not enable error checking (D) â€” that requires separate set commands. After adding the shebang, you need chmod +x script.sh to make it executable. Every agent deployment script must start with the correct shebang line.",
      source: "Lesson 6: Bash Scripting Fundamentals"
    },
    {
      question: "What does 'set -euo pipefail' do when placed at the top of a bash script?",
      options: [
        "Enables verbose logging of every command executed in the script output",
        "Sets environment variables for error handling, undefined checks, and pipe failures",
        "Exits on errors (-e), errors on undefined variables (-u), and catches pipe failures",
        "Creates automatic backups of all files modified during script execution"
      ],
      correctOption: 2,
      explanation: "set -euo pipefail combines three safety flags: -e exits immediately when any command fails (nonzero exit code), -u treats unset variables as errors instead of expanding to empty strings, and pipefail makes pipelines fail if any command in the chain fails, not just the last one. It does not enable verbose logging (A) â€” that would be set -x. While it relates to error handling (B is partially right), that description is too vague â€” the critical detail is the specific behaviors of each flag. It does not create file backups (D). This line is essential in agent deployment scripts because silent failures in production lead to corrupted states, missing configurations, and difficult-to-diagnose agent outages.",
      source: "Lesson 6: Bash Scripting Fundamentals"
    },
    {
      question: "Why must bash variables be quoted as \"${VAR}\" rather than used bare as $VAR in production scripts?",
      options: [
        "Quoting makes variable access faster by skipping shell expansion passes",
        "Quoting prevents word splitting and glob expansion on values with spaces or special characters",
        "Bare variables are deprecated in modern bash versions and produce warnings",
        "Quoting enables variable interpolation which is disabled for bare variables"
      ],
      correctOption: 1,
      explanation: "Without quotes, bash performs word splitting and glob expansion on variable values. If AGENT_PATH='/var/my agents/config', then cp $AGENT_PATH /backup becomes cp /var/my agents/config /backup â€” bash splits it into three arguments at the space. Quoted \"${AGENT_PATH}\" preserves the value as a single argument. Quoting does not affect speed (A) â€” it changes parsing behavior, not performance. Bare variables are not deprecated (C) â€” they work but are unsafe. Unquoted variables still interpolate (D) â€” the issue is what happens after interpolation. This bug commonly appears in agent paths containing spaces or special characters, causing deployment scripts to fail unpredictably.",
      source: "Lesson 6: Bash Scripting Fundamentals"
    },
    {
      question: "In a bash script, what is the purpose of defining reusable functions like 'deploy_agent()' and 'check_health()'?",
      options: [
        "Functions run in separate processes for parallel execution and performance",
        "Functions organize repeated logic into named blocks that can be called multiple times",
        "Functions automatically retry on failure with exponential backoff behavior",
        "Functions compile to machine code at definition time for execution speed"
      ],
      correctOption: 1,
      explanation: "Bash functions encapsulate a block of commands under a name, allowing you to call that logic multiple times without duplicating code. deploy_agent() might contain ten lines of deployment commands â€” calling it by name keeps the main script readable and maintainable. Functions do not run in separate processes by default (A) â€” they execute in the current shell context unless explicitly backgrounded. They do not automatically retry (C) â€” you must implement retry logic yourself within the function. Bash is interpreted, not compiled (D) â€” functions are parsed at call time. Well-structured deployment scripts use functions for each logical phase: validate, deploy, verify, rollback.",
      source: "Lesson 6: Bash Scripting Fundamentals"
    },
    {
      question: "What does a for loop iterating over files look like in bash, and why is it preferred over manual repetition?",
      options: [
        "foreach file in *.yaml do process $file done â€” uses foreach keyword",
        "for file in *.yaml; do process \"$file\"; done â€” iterates over glob matches",
        "loop *.yaml as file { process $file } â€” uses C-style loop syntax",
        "for (file : *.yaml) { process(file); } â€” uses Java-style iteration"
      ],
      correctOption: 1,
      explanation: "Bash for loops use the syntax: for variable in list; do commands; done. The glob *.yaml expands to all matching files, and the loop processes each one. Note the quoted \"$file\" inside the loop to handle filenames with spaces safely. foreach (A) is not a bash keyword â€” it exists in csh/tcsh shells. C-style loop and curly braces (C) are not valid bash syntax. Java-style for-each with parentheses and colons (D) does not work in bash. Loops are essential for batch operations like deploying multiple agent configurations: for config in /var/agents/configs/*.yaml; do validate \"$config\"; done processes every YAML config file automatically.",
      source: "Lesson 6: Bash Scripting Fundamentals"
    },
    {
      question: "Which grep command searches for lines containing 'ERROR' or 'FATAL' in all log files recursively?",
      options: [
        "grep 'ERROR' 'FATAL' /var/log/ searches two patterns sequentially in the path",
        "grep -rE 'ERROR|FATAL' /var/log/ recursively searches with extended regex alternation",
        "grep -w ERROR+FATAL /var/log/*.log searches for the combined word in top-level logs",
        "find /var/log -exec grep ERROR FATAL searches using find's exec for each file"
      ],
      correctOption: 1,
      explanation: "grep -rE combines -r (recursive search through directories) with -E (extended regex for the alternation operator |). The pattern 'ERROR|FATAL' matches lines containing either word. Multiple bare arguments (A) make grep interpret 'FATAL' as a filename, not a pattern. The + operator (C) is not valid for alternation in grep, and *.log only matches top-level files. The find syntax (D) is malformed â€” it would need separate -exec grep 'ERROR\\|FATAL' {} \\; syntax. Recursive grep with regex is the fastest way to triage agent failures â€” grep -rE 'ERROR|FATAL|Exception' /var/log/agents/ immediately reveals what went wrong across all log files.",
      source: "Lesson 7: Text Processing Power Tools"
    },
    {
      question: "How does sed perform an in-place substitution to change a configuration value across a file?",
      options: [
        "sed 'replace/old/new/' config.yaml modifies the file using replace syntax",
        "sed -i 's/old_value/new_value/g' config.yaml substitutes all occurrences in place",
        "sed --modify 's/old/new/' config.yaml uses the modify flag for file editing",
        "sed -r 'old_value->new_value' config.yaml uses arrow syntax for replacement"
      ],
      correctOption: 1,
      explanation: "sed -i performs in-place editing, and 's/old_value/new_value/g' is the substitution command: s for substitute, g flag for global (all occurrences on each line, not just the first). Without -i, sed prints to stdout without modifying the file. 'replace' (A) is not a sed command â€” the correct command prefix is 's'. --modify (C) is not a valid sed flag. Arrow syntax (D) is not supported by sed. sed is indispensable for automated configuration management â€” updating port numbers, changing API endpoints, or modifying environment values across agent config files without opening an editor: sed -i 's/PORT=8000/PORT=8080/g' .env updates all port references.",
      source: "Lesson 7: Text Processing Power Tools"
    },
    {
      question: "What does the awk command 'awk '{print $1, $3}' access.log' extract from each line?",
      options: [
        "The first and third characters from each line of the access log file",
        "The first and third whitespace-delimited fields from each line of the file",
        "Lines one and three from the file, printing them to standard output",
        "The first and third bytes of each line in raw binary output format"
      ],
      correctOption: 1,
      explanation: "awk automatically splits each input line into fields at whitespace boundaries. $1 is the first field, $3 is the third field. For a log line like '192.168.1.1 - GET /api/health 200', $1 is the IP address and $3 is the HTTP method. It does not extract characters (A) â€” awk works with fields (columns), not individual characters. It does not select line numbers (C) â€” awk processes every line and applies the print action to each. Byte extraction (D) is not how awk operates. awk excels at extracting structured data from agent logs: awk '{print $1, $NF}' access.log shows IP addresses and status codes for quick traffic analysis.",
      source: "Lesson 7: Text Processing Power Tools"
    },
    {
      question: "In cron scheduling syntax, what does the expression '0 */6 * * *' mean?",
      options: [
        "Run every 6 minutes at the top of each hour throughout the day",
        "Run at minute 0 of every 6th hour, meaning 00:00, 06:00, 12:00, 18:00",
        "Run 6 times per day at evenly spaced random intervals selected by cron",
        "Run on the 6th day of every month at midnight in the system timezone"
      ],
      correctOption: 1,
      explanation: "Cron fields are: minute hour day-of-month month day-of-week. '0 */6 * * *' means minute 0, every 6th hour (*/6 = step value), every day, every month, every weekday. This fires at 00:00, 06:00, 12:00, and 18:00. It is not every 6 minutes (A) â€” that would be */6 in the minute field: '*/6 * * * *'. Cron does not pick random intervals (C) â€” it follows deterministic schedules. The expression does not reference day-of-month (D) â€” the */6 is in the hour field. Cron scheduling is essential for agent maintenance tasks like log rotation, health checks, and periodic model updates running on predictable intervals.",
      source: "Lesson 7: Text Processing Power Tools"
    },
    {
      question: "Which text processing pipeline counts the number of unique IP addresses in an access log?",
      options: [
        "cat access.log | count -u | head gives the top unique lines from the log",
        "grep -c unique access.log counts lines containing the literal word 'unique'",
        "awk '{print $1}' access.log | sort | uniq -c | sort -rn extracts, deduplicates, and counts",
        "sed 's/ /\\n/g' access.log | wc -l counts all whitespace-separated tokens"
      ],
      correctOption: 2,
      explanation: "This pipeline chains four tools: awk extracts the IP field ($1), sort orders them alphabetically (required by uniq), uniq -c counts consecutive duplicates, and sort -rn sorts by count in descending numeric order. The result shows which IPs generated the most traffic. count (A) is not a standard Linux command. grep -c (B) counts lines matching a literal string, not unique values. The sed approach (D) splits all words and counts total tokens, not unique IPs. This pipeline pattern is a core agent operations skill â€” identifying abusive IPs, tracking API usage distribution, and debugging connection issues all start with extracting and counting unique values from logs.",
      source: "Lesson 7: Text Processing Power Tools"
    },
    {
      question: "What is the correct command to create a new system user specifically for running an agent service?",
      options: [
        "adduser --interactive agent-user creates a user with an interactive setup wizard",
        "useradd --system --no-create-home --shell /usr/sbin/nologin agent-user",
        "usermod --new agent-user creates a minimal system account for service use",
        "passwd --new agent-user creates a passwordless user account for agents"
      ],
      correctOption: 1,
      explanation: "useradd --system creates a system account (low UID, no aging), --no-create-home skips the home directory since services do not need one, and --shell /usr/sbin/nologin prevents interactive login, which is a security best practice for service accounts. adduser --interactive (A) is for human users with passwords and home directories â€” too permissive for a service account. usermod (C) modifies existing users, it does not create new ones. passwd (D) sets passwords for existing users, it does not create accounts. Running agents under dedicated service accounts follows the principle of least privilege â€” if the agent is compromised, the attacker only has access to that service account's limited permissions.",
      source: "Lesson 8: Security and Permissions"
    },
    {
      question: "What does chmod 755 script.sh set as the file permissions?",
      options: [
        "All users can read, write, and execute the file without restrictions",
        "Owner reads, writes, and executes; group and others can read and execute only",
        "Owner reads and writes only; group and others can only read the file",
        "Only the file owner can access the file; no access for group or others"
      ],
      correctOption: 1,
      explanation: "chmod uses octal digits where 7=rwx (read+write+execute), 5=r-x (read+execute), 5=r-x. So 755 means: owner gets full access (rwx), group can read and execute but not modify (r-x), others also get read and execute (r-x). All users rwx (A) would be 777 â€” dangerously permissive. Owner rw only (C) would be 644, which lacks execute permission entirely. Owner-only access (D) would be 700. The 755 permission is the standard for deployment scripts and executables â€” the owner (typically the deployment user) can modify the script, while others can run it but not alter it, maintaining both usability and security.",
      source: "Lesson 8: Security and Permissions"
    },
    {
      question: "What is the difference between setting a variable with and without export in a bash session?",
      options: [
        "export saves the variable to disk permanently; without export it exists in memory only",
        "export makes the variable available to child processes; without export it is shell-local",
        "export encrypts the variable value for security; without export it is stored as plaintext",
        "There is no functional difference between exported and non-exported shell variables"
      ],
      correctOption: 1,
      explanation: "export marks a variable for inheritance by child processes. Without export, API_KEY=secret is only visible in the current shell â€” if you launch python agent.py, that subprocess cannot see API_KEY. With export API_KEY=secret, the variable is copied into the environment of every child process. export does not save to disk (A) â€” the variable is lost when the shell exits regardless. export does not encrypt anything (C) â€” values remain plaintext in the process environment. There is a significant functional difference (D). This distinction is critical for agent deployment: agent processes need access to API keys and configuration values, so those variables must be exported before launching the agent.",
      source: "Lesson 8: Security and Permissions"
    },
    {
      question: "Why should .env files never be committed to version control, and how should they be managed?",
      options: [
        ".env files are too large for git to track efficiently and cause repository bloat",
        ".env files contain secrets that would be exposed in repository history permanently",
        ".env files use a format incompatible with git diff and merge operations properly",
        ".env files are auto-generated at build time and committing them causes conflicts"
      ],
      correctOption: 1,
      explanation: ".env files typically contain API keys, database passwords, and other secrets. Once committed to git, those secrets exist in the repository history forever â€” even deleting the file later does not remove it from past commits. Anyone with repository access can extract them. File size (A) is not the concern â€” .env files are tiny. Format incompatibility (C) is false â€” git handles .env files like any text file. They are not auto-generated (D) â€” they are manually created with environment-specific values. The proper workflow: add .env to .gitignore, provide a .env.example template with placeholder values, and distribute actual secrets through secure channels like encrypted vaults or secret management services.",
      source: "Lesson 8: Security and Permissions"
    },
    {
      question: "What is the practical difference between binding a service to localhost (127.0.0.1) versus 0.0.0.0?",
      options: [
        "localhost is faster because it skips network stack processing entirely",
        "0.0.0.0 only accepts IPv6 connections while localhost handles IPv4 traffic",
        "localhost restricts connections to the same machine; 0.0.0.0 accepts connections from any network interface",
        "There is no difference; both addresses accept all incoming network connections"
      ],
      correctOption: 2,
      explanation: "Binding to 127.0.0.1 (localhost) means only processes on the same machine can connect â€” external traffic is rejected at the network layer. Binding to 0.0.0.0 means the service listens on all network interfaces and accepts connections from anywhere. localhost does not skip the network stack (A) â€” it still uses the loopback interface, just restricted. 0.0.0.0 handles all protocols, not just IPv6 (B). There is a critical security difference (D). For agent deployment: internal services like databases should bind to localhost for security. Only the reverse proxy (nginx) should bind to 0.0.0.0 to accept public traffic, forwarding it to internal services on localhost.",
      source: "Lesson 9: Networking and SSH"
    },
    {
      question: "What does an SSH config entry in ~/.ssh/config achieve for managing multiple servers?",
      options: [
        "It stores encrypted passwords for automatic login to each configured server",
        "It defines connection aliases with hostname, user, port, and key file per server",
        "It creates persistent SSH tunnels that automatically reconnect after disruption",
        "It configures the SSH server daemon to accept connections on custom ports"
      ],
      correctOption: 1,
      explanation: "An SSH config entry creates a named shortcut for connections. Instead of typing ssh -i ~/.ssh/agent-key.pem -p 2222 deploy@192.168.1.100, you define a Host block and type ssh agent-server. Each entry specifies HostName, User, Port, IdentityFile, and other options. SSH config does not store passwords (A) â€” it references key files for certificate-based authentication. It does not create persistent tunnels automatically (C) â€” you must initiate connections manually or use separate tools like autossh. It configures the client, not the server daemon (D) â€” server configuration lives in /etc/ssh/sshd_config. Managing multiple agent servers becomes practical with config entries for production, staging, and development environments.",
      source: "Lesson 9: Networking and SSH"
    },
    {
      question: "Which ufw commands would you use to allow only SSH and HTTPS traffic to an agent server?",
      options: [
        "ufw allow all then ufw deny ssh and ufw deny https to create exceptions",
        "ufw enable then ufw default allow to permit all standard service traffic",
        "ufw default deny incoming, then ufw allow 22/tcp, then ufw allow 443/tcp",
        "ufw reset then ufw allow 80/tcp to enable standard web traffic only"
      ],
      correctOption: 2,
      explanation: "The secure approach is: first set default policy to deny all incoming (ufw default deny incoming), then explicitly allow only needed ports â€” 22/tcp for SSH access and 443/tcp for HTTPS. This follows the principle of least privilege: deny everything, then allow only what is required. Allowing all then denying (A) is backwards and insecure â€” the default allow grants access during the configuration window. Default allow (B) permits all traffic, which defeats the purpose of a firewall. Only allowing port 80 (D) provides unencrypted HTTP and blocks SSH, locking you out of the server. For agent servers, you may also need custom ports for agent APIs, added individually after the default deny.",
      source: "Lesson 9: Networking and SSH"
    },
    {
      question: "What is a network port, and why would two agent services fail if configured to use the same port?",
      options: [
        "Ports are physical cable connectors and two services need separate network adapters",
        "Ports are numeric endpoints for network traffic and each port supports only one listener",
        "Ports are speed settings and conflicting ports cause bandwidth throttling issues",
        "Ports are security credentials and duplicate ports trigger authentication failures"
      ],
      correctOption: 1,
      explanation: "A port is a 16-bit number (0-65535) that identifies a specific service on a machine. When a service binds to a port, it claims exclusive listening rights â€” the operating system refuses to let a second service bind to the same port, raising an 'Address already in use' error. Ports are not physical connectors (A) â€” they are logical networking constructs within the TCP/IP stack. They are not speed settings (C) or security credentials (D). In agent deployment, each service needs a unique port: agent API on 8000, monitoring dashboard on 3000, metrics exporter on 9090. Port conflicts are a top-5 deployment error â€” diagnosed with ss -tlnp or lsof -i :PORT.",
      source: "Lesson 9: Networking and SSH"
    },
    {
      question: "What are the three required sections in a systemd service file and what does each configure?",
      options: [
        "[Setup], [Run], [Stop] configure initialization, execution, and termination phases",
        "[Unit], [Service], [Install] configure metadata/dependencies, execution behavior, and boot integration",
        "[Config], [Process], [Network] configure settings, process management, and network bindings",
        "[Header], [Body], [Footer] organize the file into declaration, logic, and cleanup sections"
      ],
      correctOption: 1,
      explanation: "[Unit] defines service metadata â€” Description, documentation, and dependency ordering (After=, Requires=). [Service] configures how the process runs â€” ExecStart command, User, WorkingDirectory, Restart policy, and resource limits. [Install] determines boot integration â€” WantedBy=multi-user.target enables the service at startup. [Setup]/[Run]/[Stop] (A) are not valid systemd sections. [Config]/[Process]/[Network] (C) are fabricated section names. [Header]/[Body]/[Footer] (D) are not systemd concepts. Understanding these three sections is fundamental to deploying Digital FTEs that start automatically, run under correct users, and restart after failures.",
      source: "Lesson 10: Systemd Service Management"
    },
    {
      question: "Why is Restart=on-failure preferred over Restart=always for production agent services?",
      options: [
        "on-failure allows controlled manual stops while auto-restarting after crashes",
        "on-failure consumes significantly fewer system resources during normal operations",
        "always only functions correctly when the service runs as the root superuser account",
        "There is no practical operational difference between the two restart policies"
      ],
      correctOption: 0,
      explanation: "Restart=on-failure restarts the service only when it exits with a non-zero (error) exit code. If you intentionally stop the service with systemctl stop, it stays stopped because that is a clean exit (code 0). Restart=always restarts even after clean stops, making intentional shutdowns difficult â€” the service keeps coming back like a zombie. Resource usage (B) is identical during normal operation â€” the difference is only in restart behavior. Restart=always works regardless of user (C). There is a critical operational difference (D) â€” always makes maintenance windows frustrating when you need the service to stay down. For agent deployment, on-failure gives you crash resilience while maintaining operational control.",
      source: "Lesson 10: Systemd Service Management"
    },
    {
      question: "How do you view the last 50 log entries for a specific systemd service and follow new entries in real time?",
      options: [
        "cat /var/log/syslog | tail -50 shows recent system logs for all services",
        "systemctl logs --recent 50 --follow agent.service streams service output",
        "journalctl -u agent.service -n 50 -f shows last 50 lines and follows new output",
        "dmesg --service agent --lines 50 displays kernel messages for the service"
      ],
      correctOption: 2,
      explanation: "journalctl is systemd's log viewer. -u agent.service filters to that specific unit, -n 50 shows the last 50 entries, and -f follows new output in real time (like tail -f). This is the primary tool for debugging agent service behavior. cat /var/log/syslog (A) shows all system logs unfiltered and does not follow. systemctl logs (B) is not valid syntax â€” systemctl manages services, journalctl reads logs. dmesg (D) shows kernel ring buffer messages, not application or service logs. During agent troubleshooting, journalctl -u agent.service -n 100 -f is typically your first diagnostic command to see what the service is doing right now.",
      source: "Lesson 10: Systemd Service Management"
    },
    {
      question: "What do MemoryMax=512M and CPUQuota=50% accomplish in a systemd service file's [Service] section?",
      options: [
        "They request minimum guaranteed resources that the kernel must allocate to the service",
        "They set soft warnings that log alerts but do not enforce any actual limits on usage",
        "They enforce hard resource limits preventing the service from exceeding memory or CPU thresholds",
        "They configure resource monitoring dashboards for the service in the system monitoring tool"
      ],
      correctOption: 2,
      explanation: "MemoryMax=512M kills the service if it tries to use more than 512 megabytes of RAM â€” this prevents a memory leak from consuming all server memory and affecting other services. CPUQuota=50% limits the service to half of one CPU core's processing time. These are hard limits enforced by the kernel's cgroup mechanism, not suggestions. They are not minimum guarantees (A) â€” they are maximum caps. They are not soft warnings (B) â€” exceeding MemoryMax triggers an OOM kill. They do not configure dashboards (D). Resource limits are essential in multi-agent deployments where several Digital FTEs share a server â€” one misbehaving agent must not starve the others of resources.",
      source: "Lesson 10: Systemd Service Management"
    },
    {
      question: "What is the correct order of ExecStartPre, ExecStart, and ExecStartPost in a systemd service lifecycle?",
      options: [
        "ExecStart runs first, then ExecStartPre validates, then ExecStartPost cleans up",
        "ExecStartPre runs pre-checks, ExecStart launches the service, ExecStartPost runs post-launch tasks",
        "All three commands execute simultaneously in parallel for maximum startup speed",
        "ExecStartPost runs first to prepare the environment before ExecStart begins"
      ],
      correctOption: 1,
      explanation: "systemd executes them in strict order: ExecStartPre runs first for validation and setup (checking configs, creating directories), ExecStart launches the main service process, and ExecStartPost runs after the main process starts (health checks, notifications). If ExecStartPre fails, the service does not start. ExecStart does not run first (A) â€” pre-checks must complete before launch. They do not run in parallel (C) â€” sequential ordering ensures each phase completes before the next begins. ExecStartPost does not run first (D) â€” it runs last. This lifecycle enables robust agent deployment: pre-check validates configuration, start launches the agent, post-check confirms it is healthy.",
      source: "Lesson 10: Systemd Service Management"
    },
    {
      question: "When an agent crashes in production, what is the correct diagnostic triage order?",
      options: [
        "Reinstall the application, reboot the server, then check if the issue persists",
        "Check logs first, then verify resources (disk/memory/CPU), then inspect process state",
        "Immediately restart the service, and only investigate if it crashes again repeatedly",
        "Open a support ticket and wait for the infrastructure team to diagnose the issue"
      ],
      correctOption: 1,
      explanation: "The diagnostic triage methodology follows a systematic order: first check logs (journalctl -u service -n 100) to understand what happened, then verify resources (df -h for disk, free -h for memory, top for CPU) to identify resource exhaustion, then inspect process state (ps aux, ss -tlnp) to understand current system behavior. Reinstalling before diagnosing (A) destroys evidence and rarely fixes the underlying issue. Blind restarts (C) mask recurring problems and prevent root cause analysis. Waiting for external help (D) wastes critical time during outages. This methodology applies to every agent failure â€” logs tell you what happened, resources tell you why, and process state tells you where things stand now.",
      source: "Lesson 11: Debugging and Diagnostics"
    },
    {
      question: "What is the difference between 'df -h' and 'du -sh /var/log/' for diagnosing disk space issues?",
      options: [
        "df shows file modification dates while du shows file creation dates for directories",
        "df shows filesystem-level space usage while du shows directory-level space consumption",
        "Both commands show identical information but use different display formatting styles",
        "df checks disk hardware health while du measures disk read and write performance"
      ],
      correctOption: 1,
      explanation: "df (disk free) shows overall filesystem usage â€” how much total space exists, how much is used, and how much remains on each mounted partition. du (disk usage) measures how much space a specific directory and its contents consume. They answer different questions: df answers 'Is the disk full?' while du answers 'What directory is consuming the space?' They are not identical (C) â€” df operates at the filesystem level, du at the directory level. Neither checks hardware health (df) or measures performance (du) (A, D). The diagnostic workflow is: df -h reveals the /var partition is 95% full, then du -sh /var/log/* identifies that agent log files consumed 40GB through lack of rotation.",
      source: "Lesson 11: Debugging and Diagnostics"
    },
    {
      question: "Which command shows all processes listening on network ports, and what information does it reveal?",
      options: [
        "netstat -all shows every network connection both active and historical",
        "ifconfig -ports displays network interface port assignments and bindings",
        "ss -tlnp shows listening TCP ports with process names and numeric addresses",
        "lsof -network lists all files opened over network connections by processes"
      ],
      correctOption: 2,
      explanation: "ss -tlnp combines flags: -t (TCP only), -l (listening sockets only), -n (numeric ports, no DNS resolution), -p (show process name/PID). This reveals which services are bound to which ports â€” essential for diagnosing port conflicts and verifying agent services are running. netstat -all (A) is deprecated on modern systems in favor of ss, and 'all' shows every connection, not just listeners. ifconfig (B) shows network interface configuration, not port bindings. lsof -network (C) is not valid syntax â€” the correct form would be lsof -i. When an agent fails to start with 'Address already in use', ss -tlnp immediately shows what process is occupying the conflicting port.",
      source: "Lesson 11: Debugging and Diagnostics"
    },
    {
      question: "How does 'journalctl -u agent.service --since \"1 hour ago\" -p err' help narrow down production issues?",
      options: [
        "It shows all log entries from the past hour regardless of severity or unit",
        "It filters to error-priority messages from a specific service within a time window",
        "It deletes old log entries to free disk space and keep only recent error records",
        "It sends error logs from the past hour to an external monitoring service via API"
      ],
      correctOption: 1,
      explanation: "This command combines three filters: -u agent.service restricts to one specific service, --since '1 hour ago' limits the time window, and -p err shows only error-priority and above messages (err, crit, alert, emerg). The combination cuts through noise to show exactly what went wrong, when, for which service. It does not show all entries regardless of filters (A) â€” the whole point is precise filtering. It does not delete logs (C) â€” journalctl is read-only by default, vacuuming requires separate commands. It does not send logs externally (D) â€” journalctl reads from the local journal. This targeted query is the standard first step in agent incident response: what errors occurred in the last hour?",
      source: "Lesson 11: Debugging and Diagnostics"
    },
    {
      question: "What deployment strategy restarts the service with new code but causes brief downtime?",
      options: [
        "Blue-green deployment runs two identical environments and switches traffic instantly",
        "Rolling deployment gradually replaces instances one at a time across the cluster",
        "Stop-deploy-start (restart) strategy stops the service, deploys new code, then starts it",
        "Canary deployment routes a small percentage of traffic to the new version first"
      ],
      correctOption: 2,
      explanation: "The restart strategy (stop â†’ deploy â†’ start) is the simplest deployment method: stop the running service, replace the code, then start it again. During the stop-to-start window, the service is unavailable â€” this is acceptable for internal tools and non-critical agents. Blue-green (A) eliminates downtime by maintaining two environments and switching traffic atomically. Rolling deployment (B) updates instances gradually to maintain availability. Canary (D) tests new versions with limited traffic before full rollout. For Digital FTE deployment, the restart strategy is appropriate for development and staging. Production agents serving live traffic should use blue-green or rolling strategies to maintain availability.",
      source: "Lesson 12: Agent Deployment Workflow Integration"
    },
    {
      question: "How does blue-green deployment eliminate downtime during agent updates?",
      options: [
        "It pauses all incoming traffic during deployment and buffers requests in a queue",
        "It runs old and new versions simultaneously and switches traffic atomically to the new one",
        "It deploys updates incrementally to reduce the impact of each individual change",
        "It caches all responses from the old version and replays them from the new version"
      ],
      correctOption: 1,
      explanation: "Blue-green deployment maintains two identical environments: blue (current live) and green (new version). You deploy and test the new code on green while blue continues serving traffic. Once green is verified healthy, you switch the reverse proxy or load balancer to route all traffic from blue to green â€” an atomic operation with zero downtime. It does not pause traffic (A) â€” that would cause downtime, defeating the purpose. Incremental deployment (C) describes rolling updates, not blue-green. Response caching (D) is not part of deployment strategy â€” it is a performance optimization. Blue-green is the gold standard for production agent deployments where any downtime means missed tasks and failed automations.",
      source: "Lesson 12: Agent Deployment Workflow Integration"
    },
    {
      question: "What role does log rotation with logrotate serve in long-running agent deployments?",
      options: [
        "It speeds up log file reading by splitting large files into indexed searchable chunks",
        "It prevents log files from consuming all disk space by compressing and archiving old entries",
        "It formats log output into structured JSON for compatibility with monitoring dashboards",
        "It encrypts log files after rotation to prevent unauthorized access to historical data"
      ],
      correctOption: 1,
      explanation: "logrotate periodically rotates (renames), compresses, and eventually deletes old log files on a configurable schedule. Without rotation, a busy agent writing megabytes of logs daily will eventually fill the disk partition, crashing the service and potentially the entire server. It does not split for search indexing (A) â€” that is a log aggregation feature. It does not convert formats (C) â€” log format is determined by the application, not the rotator. It does not encrypt (D) â€” rotated files maintain their original access permissions. A typical logrotate config for agents rotates daily, keeps 7 compressed copies, and triggers the agent to reopen its log file handle after rotation.",
      source: "Lesson 12: Agent Deployment Workflow Integration"
    },
    {
      question: "When should a recurring Linux workflow be formalized into a reusable skill specification?",
      options: [
        "Every command should immediately be documented as a skill for future reference",
        "When a pattern repeats 2+ times and can be expressed as a parameterized template",
        "Only after the workflow has been used successfully at least ten times in production",
        "Skills should never be formalized; ad-hoc commands are more flexible and adaptable"
      ],
      correctOption: 1,
      explanation: "The two-repetition threshold identifies patterns worth capturing: if you perform the same multi-step workflow twice, the third time should invoke a skill rather than repeating commands manually. The skill should be parameterized â€” accepting inputs like service name, port, and environment â€” rather than hardcoded. Documenting every command (A) creates noise that obscures important patterns. Waiting for ten uses (C) wastes significant effort on manual repetition before formalizing. Never formalizing (D) means rebuilding the same workflow from memory each time, which is error-prone and slow. Pattern recognition is the bridge between Linux competence and agent deployment expertise â€” repeated workflows become reliable, tested, shareable skills.",
      source: "Lesson 13: Building Reusable Linux Skills"
    },
    {
      question: "What key sections should a DEPLOYMENT-SPEC.md contain for a reproducible agent deployment workflow?",
      options: [
        "Only the final deployment command is needed; context is unnecessary overhead",
        "Prerequisites, step-by-step procedure, verification commands, and rollback instructions",
        "Marketing description and feature comparison with competing deployment approaches",
        "Source code of the entire agent application with inline deployment annotations"
      ],
      correctOption: 1,
      explanation: "A comprehensive deployment specification includes: prerequisites (server requirements, installed dependencies, access credentials), step-by-step procedures (ordered commands with explanations), verification commands (health checks confirming success), and rollback instructions (how to revert if deployment fails). Only the final command (A) offers no context for troubleshooting when it fails. Marketing content (C) does not belong in operational documentation. Embedding full source code (D) mixes concerns â€” deployment docs reference the application but do not contain it. The DEPLOYMENT-SPEC.md serves as both a runbook for humans and a specification that AI agents can follow, making deployments reproducible regardless of who or what executes them.",
      source: "Lesson 13: Building Reusable Linux Skills"
    }
  ]}
  questionsPerBatch={18}
/>
