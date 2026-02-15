### Core Concept
Human-in-the-Loop (HITL) approval adds a checkpoint before your AI Employee takes consequential actions. For high-stakes operations like sending emails, the AI prepares the action, you approve or reject, then it executes. This balances autonomy with control.

### Key Mental Models
- **Trust Spectrum**: Read-only (safe) → Draft creation (medium) → Send with approval (controlled) → Auto-send (high trust)
- **Approval Files**: Pending actions written to files you can review before execution
- **Graduated Autonomy**: Start with everything requiring approval, relax controls as trust builds

### Critical Patterns
- Approval workflow: AI prepares action → writes approval file → notifies you → waits for yes/no → executes or cancels
- Approval file location: `~/.openclaw/approvals/pending/`
- Commands: `openclaw approvals list`, `openclaw approvals approve <id>`, `openclaw approvals reject <id>`
- Trust escalation: Document which actions skip approval as you build confidence

### Common Mistakes
- Granting auto-send before establishing trust through the approval workflow
- Not checking approvals folder regularly (actions timeout)
- Removing HITL for email without thorough testing
- Forgetting that approval is per-action, not per-session

### Connections
- **Builds on**: Connecting real services (Lesson 7)
- **Leads to**: 24/7 deployment (Lesson 9)
