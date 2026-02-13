### Core Concept
Bootstrap files transform your AI Employee from a generic assistant into YOUR specialized worker. SOUL.md defines personality/boundaries, AGENTS.md contains operating instructions, and USER.md describes you. These files load every session, creating persistent identity and institutional knowledge.

### Key Mental Models
- **Workspace = Employee's Home**: `~/.openclaw/workspace/` is where persona, instructions, and memory live
- **Bootstrap Files = Day-One Training**: Loaded every session to establish who the AI is and how it works
- **Daily Memory Logs**: `memory/YYYY-MM-DD.md` files persist knowledge across sessions, creating continuity

### Critical Patterns
- SOUL.md structure: Persona (role/expertise), Tone (communication style), Boundaries (what it refuses)
- AGENTS.md structure: Daily routines, research protocols, memory protocols
- USER.md structure: Your name, preferences, current projects, goals
- Changes require gateway restart: Bootstrap files load at session start, not mid-conversation

### Common Mistakes
- Editing files but forgetting to restart the gateway
- Putting operating instructions in SOUL.md (should be in AGENTS.md)
- Not customizing USER.md with your actual preferences
- Expecting immediate effect without restarting

### Connections
- **Builds on**: Understanding the 5-component architecture (Lesson 4)
- **Leads to**: Creating portable skills (Lesson 6)
