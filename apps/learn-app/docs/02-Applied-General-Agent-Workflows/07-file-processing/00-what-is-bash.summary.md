### Core Concept

Bash is what transforms a General Agent from an advisor into an operator. Without a shell, AI can only suggest what you might do. With Bash, the agent can actually find files, organize folders, check disk space, and automate tasks on your computer.

### Key Mental Models

- **"Bash gives agents hands"**: The shell is the bridge between AI intelligence and real action on your system. It turns conversation into execution.
- **Advisor vs. Operator**: Without Bash, an agent describes solutions. With Bash, it implements them. This distinction is the foundation of everything in this chapter.

### Critical Patterns

- **Terminal setup per platform**: macOS/Linux have Bash built in. Windows users need Git Bash (quick start) or WSL (full Linux environment).
- **Verify before proceeding**: Run `echo "Hello from Bash!"` and `ls` to confirm your terminal works before moving on.
- **Recognize, don't memorize**: You don't need to learn commands. You need to recognize what a command does when the agent runs it, so you can verify it's doing the right thing.

### Common Mistakes

- Trying to memorize every command instead of letting the agent handle execution while you verify intent.
- Using PowerShell for AI-assisted workflows when Bash-compatible tools produce better results (AI tools are trained primarily on Bash).
- Skipping setup verification and running into silent failures in later lessons.

### Connections

- **Builds on**: Principle 1 ("Bash is the Key") and the Seven Principles from Part 1 (Chapters 1-5)
- **Leads to**: Using Claude Code to solve real file exploration problems (Lesson 1), safety-first patterns (Lesson 2)
