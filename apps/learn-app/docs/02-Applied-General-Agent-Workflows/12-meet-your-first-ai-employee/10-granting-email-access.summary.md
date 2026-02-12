### Core Concept
MCP (Model Context Protocol) is the universal connector between AI agents and external services. Gmail MCP gives your AI Employee 19 tools for real email operations: searching, reading, drafting, sending. This transforms skills from practice to production.

### Key Mental Models
- **MCP = Universal Translator**: Like USB for peripherals, MCP provides a standard way for agents to connect to any service
- **OAuth for Security**: Sign in through Google instead of sharing passwords; grant only needed permissions
- **Least Privilege**: Start with read-only (`gmail.readonly`), add send capability only after testing

### Critical Patterns
- Enable Gmail MCP: `openclaw config set mcp.gmail.enabled true`
- Authenticate: `openclaw mcp auth gmail` (OAuth flow in browser)
- Configure scopes: `gmail.readonly` (safe), `gmail.send` (test first), `gmail.compose` (drafts)
- Test before production: Create drafts, review them, send to yourself first

### Common Mistakes
- Granting `gmail.send` before testing with `gmail.readonly`
- Not testing the draft → review → send workflow before enabling auto-send
- Forgetting to restart gateway after MCP configuration changes
- Skipping the "send to yourself" test step

### Connections
- **Builds on**: Email skills and subagents (Lessons 6-9)
- **Leads to**: Bronze Capstone integration (Lesson 11)
