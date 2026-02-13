### Core Concept

Skills are portable, structured instructions that extend your AI Employee's capabilities. A SKILL.md file packages your domain expertise into reusable instructions that compose together to handle complex tasks, and can travel across platforms (Claude Code, Cursor, OpenClaw, etc.).

### Key Mental Models

- **Three-Tier Loading**: Metadata loads at session start (cheap), full skill loads on demand (moderate), references load when needed (variable). Avoids wasting context on unused skills.
- **Skill Precedence**: Workspace skills override managed skills, which override bundled defaults. This lets you customize without modifying system files.
- **Composition Over Monoliths**: Small focused skills combine to solve complex problems. A "research-assistant" skill pairs with "document-summarizer" automatically—no manual orchestration needed.
- **Skills vs Subagents**: Use skills for sequential, self-contained work. Use subagents (up to 8 concurrent) when tasks need parallel execution or isolated sessions.

### Critical Patterns

- **SKILL.md Structure**: Directory with `SKILL.md` (required YAML + instructions), `references/` (optional docs), `assets/` (optional templates). Single-line frontmatter values only—multiline YAML breaks parsing.
- **Frontmatter Requirements**: `name`, `description`, `emoji` fields. Verify with `openclaw skills list` and `openclaw skills info <skill-name>`.
- **Output Format Definition**: Each skill explicitly defines expected output structure (sections, formatting, quality standards). Employee follows the template automatically.
- **Subagent Spawning**: Use when single agent cannot parallelize. Max 8 concurrent, 60-minute auto-archive, non-blocking. Cannot nest (subagents cannot spawn subagents).

### Common Mistakes

- **Multiline YAML in frontmatter** breaks skill loading. Use single-line descriptions only or refactor into references/.
- **Assuming skills load at startup**. They don't—only metadata loads. Full skill loads when agent decides it's relevant, consuming context progressively.
- **Not defining output format**. Skills without explicit structure produce inconsistent results. Always specify sections, field names, and quality standards.
- **Mixing skills and subagents**. Skills for composition, subagents for parallelization. Sequential work in skills stays cheaper and faster.

### Connections

- **Builds on**: Lesson 5 (employee memory/personality). Skills extend capabilities beyond default knowledge.
- **Leads to**: Lesson 7 (connecting real services). Skills integrate with external APIs, webhooks, and data sources.
