### Core Concept

Effective organization with General Agents follows a collaborative design pattern. The agent proposes categories, you refine them, then the agent documents the rules for reuse.

### Key Mental Models

- **Propose-refine-iterate**: The agent suggests categories based on your actual files. You adjust based on your needs. The agent adapts.
- **State persistence**: Rules get saved to `rules.md` with version tracking and last-applied dates. You're not organizing once. You're creating a permanent, evolving system.
- **Test before scaling**: Always try on one file first. If the test works, proceed with confidence. If not, you caught the problem early.
- **Dry run before execution**: Ask the agent to show what it _would_ do without doing it. The single-file test checks the mechanism works; the dry run checks the decisions are right.

### Critical Patterns

- **"Help me organize [folder]. Analyze what's there and suggest categories based on my actual files"**: This triggers collaborative rule design.
- **"Test on ONE file first"**: This single instruction prevents potential chaos by validating before batch operations.
- **"Show me what you'll do before doing it"**: Dry-run prompt that makes the agent's plan visible before it becomes irreversible (Principle 7: Observability).
- **"Document the rules so we can reuse them"**: Creates persistent state (Principle 5) that survives beyond this session.
- **Principle 4 (Decomposition)**: Small, reversible testing before scaling to hundreds of files.

### Common Mistakes

- Making up categories as you go instead of analyzing what you actually have: Your files may not fit predefined categories.
- Forgetting to document rules: Without `rules.md`, you'll re-decide categories every time your folder fills up.
- Testing on all files at once: One mistake miscategorizes everything. Test on one file first.

### Connections

- **Builds on**: Lessons 1-2 (survey and safety), Principle 5 (Persisting State) from Part 1
- **Leads to**: Batch operations (Lesson 4) where rules become automated scripts
