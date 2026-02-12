### Core Concept
Your AI Employee is powered by five components working together: Gateway (routes messages), Agent Runtime (the brain), Channels (Telegram, WhatsApp, Discord), Skills (portable expertise), and Model Providers (LLM intelligence). Understanding this architecture helps you diagnose problems and extend capabilities.

### Key Mental Models
- **Gateway as Traffic Controller**: Every message passes through it; adding new channels is configuration, not code
- **Skills = Portable Expertise**: Markdown files that work across platforms (OpenClaw, Claude Code, Claude Cowork)
- **Three-Tier Skill Loading**: Workspace skills override managed skills override bundled skills
- **MCP = Universal Connector**: Model Context Protocol lets agents connect to external services (Gmail, GitHub) through a standard interface

### Critical Patterns
- Trace message flow: Channel → Gateway → Agent → Model Provider → Response → Channel
- Skill format: YAML frontmatter (`name`, `description`, `metadata`) + markdown instructions
- Pairing controls access: Users need approval before messaging (`openclaw pairing approve telegram <CODE>`)
- Session storage: Conversations persist in `~/.openclaw/agents/<id>/sessions/` as JSONL

### Common Mistakes
- Confusing where to modify: Agent for behavior, Skills for expertise, Gateway for routing
- Forgetting that skill changes require gateway restart to take effect
- Not using the three-tier system (creating workspace skills when managed would suffice)
- Building platform-specific solutions when portable skills would work

### Connections
- **Builds on**: Working AI Employee experience (Lessons 2-3)
- **Leads to**: Customizing your employee's memory and persona (Lesson 5)
