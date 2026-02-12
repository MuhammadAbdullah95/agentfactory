### Core Concept
Subagents are specialists your AI Employee can delegate to. Instead of one agent doing everything, you create focused experts (email-writer, email-analyzer, email-organizer) that your main agent invokes when needed. This mirrors how human managers delegate to team members.

### Key Mental Models
- **Skills vs Subagents**: Skills add expertise to one agent; subagents are separate agents with their own personas
- **Delegation Pattern**: Main agent receives task → identifies specialist needed → invokes subagent → integrates results
- **Focused Expertise**: Each subagent has a narrow focus, making it better at that specific task

### Critical Patterns
- Subagent invocation: `@invoke email-analyst "Analyze this thread for action items"`
- Each subagent has: Own persona (SOUL), specific tools, narrow scope
- Main agent orchestrates: Decides which specialist to call based on task type
- Results integration: Main agent combines subagent outputs into coherent response

### Common Mistakes
- Creating subagents when a skill would suffice (use subagents for persona shifts, not just instructions)
- Not giving subagents clear, narrow scopes
- Main agent trying to do specialist work instead of delegating
- Forgetting that subagents inherit some context but have their own identity

### Connections
- **Builds on**: Three email skills (Lessons 6-8)
- **Leads to**: Connecting to real Gmail (Lesson 10)
