### Core Concept
AI systems are stateless between sessions--they have no persistent memory. The solution is persisting project knowledge, decisions, and context in files within your repository so that every session (whether Claude Code or Cowork) can read them directly, making collaboration cumulative rather than repetitive.

### Key Mental Models
- **Files as Persistent Memory**: The repository filesystem is the one thing that persists across sessions and that AI can read automatically. Chat history disappears; files remain.
- **State Hierarchy**: Ephemeral state (current task--don't persist), Session state (WIP tracking--task files), Project state (conventions--CLAUDE.md), Permanent state (architecture decisions--ADRs).
- **Reproducibility Goal**: A new developer or AI should be able to understand the entire project from the files alone--context, conventions, decisions, current work, and expected behavior.
- **Compounding Knowledge**: Each session with well-maintained context files builds on all previous documentation. Without persistence, each session starts from zero.

### Key Facts
- **CLAUDE.md**: Claude Code automatically reads this file from the project root, making it the primary location for project-specific AI context
- **Other context files**: .cursorrules (Cursor), .aider.conf.yml (Aider), docs/adr/ (Architecture Decision Records)--different tools read different files
- **ADR value**: Six months later, you won't remember why you chose PostgreSQL over MongoDB--the ADR explains the decision, alternatives, and tradeoffs for humans and AI alike

### Critical Patterns
- Three practical persistence patterns: Convention Documentation (naming, imports, patterns), Work-in-Progress Tracking (in progress, completed, next up), Known Issues and Gotchas (rate limits, setup quirks, hot reload limitations)
- Context files should be maintained like code--update when reality changes, remove outdated information, don't let them rot
- The principle applies equally in Cowork: create progress.md and context.md files before complex projects; these persist knowledge that would otherwise be lost between sessions
- Guide AI attention with structured context: indicate which files are relevant for which types of work (auth changes -> read auth ADR; database work -> read schema docs)

### Common Mistakes
- Outdated context files (documenting React/Redux when you migrated to MongoDB months ago--treat context files as living documents)
- Over-documenting trivia (semicolons, indentation, quotes belong in linter config, not context files--capture meaningful decisions)
- Scattered knowledge (some decisions in Slack, some in email, some in heads--if it's not in git, it doesn't exist for AI collaboration)
- Persisting sensitive data (API keys, secrets, passwords should use environment variables, never context files)

### Connections
- **Builds on**: Principle 4 (Small, Reversible Decomposition)--as you break work into steps, persisting the plan and progress in files ensures continuity and enables handoff between sessions
- **Leads to**: Principle 6 (Constraints and Safety)--context files can encode safety rules and constraints that AI should follow, making guardrails persistent and automatic
