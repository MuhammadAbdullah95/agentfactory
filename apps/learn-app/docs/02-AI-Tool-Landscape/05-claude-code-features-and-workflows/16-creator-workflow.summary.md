### Core Concept
Boris Cherny's (Claude Code creator) workflow demonstrates how chapter concepts combine into production-grade Agent Factory practice: parallel sessions for capacity scheduling, Plan Mode discipline for alignment, team CLAUDE.md for institutional memory, specialized subagents for common workflows, and verification loops for quality assurance. One person operating like a small engineering team.

### Key Mental Models
- **Capacity Scheduling**: Run 15-20 concurrent Claude sessions across terminal and browser. Claude isn't a single tool you interact with—it's capacity you schedule like a team of assistants
- **Plan First, Execute Later**: Always enter Plan Mode for non-trivial tasks. Iterate on the plan until it's solid, then switch to auto-accept for execution. Planning alignment prevents wasted iterations
- **Verification-First Quality**: Give Claude ways to verify its own work (browser testing, MCP tools, hooks). This feedback loop 2-3x quality of final results. You don't trust AI output—you instrument it
- **Every Mistake Becomes a Rule**: When Claude makes errors, immediately document in CLAUDE.md. The learning loop: Claude errs → team corrects → Claude improves. Team shares and evolves this file through code review, creating institutional memory that compounds

### Critical Patterns
- Use Opus 4.5 with thinking—"wrong fast answer" costs more time than "right slow answer"
- Create specialized subagents for repeated PR workflows (code-simplifier, verify-app, build-validator)
- Add PostToolUse hook for formatting to prevent CI failures on the last 10%
- Use `/permissions` to pre-allow safe commands rather than `--dangerously-skip-permissions`
- Share settings in `.claude/settings.json` for team consistency

### Common Mistakes
- Running single overloaded sessions instead of parallel simple ones
- Skipping Plan Mode because "this seems simple"—Boris uses it for every non-trivial task
- Hoping output is correct instead of building verification infrastructure
- Using skip permissions instead of intentionally pre-allowing specific safe commands

### Connections
- **Synthesizes**: All Chapter 5 lessons—Origin Story (agency), CLAUDE.md (context), Skills (expertise), MCP (tools), Subagents (delegation), Hooks (automation), Settings (configuration)
- **Demonstrates**: Real-world Agent Factory implementation at Anthropic production scale
- **Leads to**: Part 3 (Spec-Driven Development), Part 6 (Custom Agent SDKs), Part 7 (Digital FTE Deployment)
- **Digital FTE Link**: Each capability maps to productizable agent components—skills become assets, CLAUDE.md becomes team memory, subagents become orchestration patterns
