### Core Concept

Productive Claude Code sessions require workflow discipline, not AI knowledge. The four-phase workflow (Explore→Plan→Implement→Commit) transforms messy exploration into systematic progress, while course correction tools let you recover from wrong directions without losing work.

### Key Mental Models

- **Planning is Cheap, Implementation is Expensive**: Catching misunderstandings during planning costs minutes; fixing them during implementation costs hours. When unsure whether to plan, plan.
- **Esc as Steering Wheel**: The Escape key isn't an emergency brake—it's for constant course correction. Use it liberally when Claude heads somewhere unproductive.
- **Checkpoints Enable Experimentation**: Every tool use creates a checkpoint. You can try risky approaches knowing `/rewind` restores any previous state. Safe experimentation becomes the norm.

### Critical Patterns

- Enter Plan Mode (`Shift+Tab`) for exploration before making changes
- Use `Ctrl+G`/`Cmd+G` to edit plans before implementation
- Press `Esc` twice or `/rewind` to access checkpoint menu
- Use `--continue` or `--resume` to pick up previous sessions
- Configure `/permissions` to allowlist trusted commands
- Apply the interview pattern: have Claude ask YOU questions before implementing complex features

### Common Mistakes

- **Kitchen Sink Session**: Mixing unrelated tasks pollutes context. Fix: `/clear` between unrelated work.
- **Correction Loop**: Repeated corrections add noise. Fix: After two corrections, `/clear` and write a better initial prompt.
- **Bloated CLAUDE.md**: 200+ lines dilutes focus. Fix: Keep under 60 lines; move domain knowledge to skills.
- **Trust-Then-Verify Gap**: Accepting plausible output without running it. Fix: Define verification criteria for every claim.
- **Infinite Exploration**: Open-ended investigation fills context. Fix: Scope narrowly or use subagents for research.

### Connections

- **Builds on**: Chapter 4's context engineering fundamentals (`/clear`, `/compact`, context window)
- **Leads to**: The Seven Principles that explain *why* these operational patterns work
