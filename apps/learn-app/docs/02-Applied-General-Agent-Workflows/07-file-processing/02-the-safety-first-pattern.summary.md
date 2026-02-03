### Core Concept

The safety-first pattern establishes constraints before destructive operations. Create a backup, verify it's complete, then proceed with confidence.

### Key Mental Models

- **Safety enables action**: The backup constraint doesn't limit you. It frees you to experiment without fear.
- **Verification before trust**: Never assume a backup worked. Always confirm completeness with source-to-destination comparison.
- **Agents should ask, not assume**: A well-designed agent clarifies ambiguous requests before acting.

### Critical Patterns

- **"Before [operation], create a backup of [what matters]"**: This universal safety pattern applies to files, code, databases, and any irreversible change.
- **"Verify the backup is complete"**: Always ask the agent to compare counts between source and backup.
- **Principle 6 (Constraints and Safety)**: The constraint of "backup first" enables fearless experimentation.
- **Principle 3 (Verification)**: The workflow follows a pattern of backup, verify, then execute.

### Common Mistakes

- Skipping verification: A backup that fails silently is worse than no backup because it gives false confidence.
- Not clarifying what "important" means: Letting the agent assume what to backup can miss critical files.
- Creating backups after changes: Starting work without safety limits your ability to recover from mistakes.

### Connections

- **Builds on**: Lesson 1 (folder survey), understanding of General Agents from Part 1
- **Leads to**: Organization workflows (Lesson 3) where safety protects against categorization errors
