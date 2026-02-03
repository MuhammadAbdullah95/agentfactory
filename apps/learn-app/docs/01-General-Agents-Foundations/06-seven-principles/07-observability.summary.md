### Core Concept
If you cannot see what the AI agent is doing, you cannot debug problems, build trust, or improve the collaboration. Observability means making AI workflows transparent, traceable, and debuggable--whether through raw terminal output (Claude Code) or the three-panel layout showing plan, execution, and outputs simultaneously (Claude Cowork).

### Key Mental Models
- **Three Pillars of Observability**: Action Visibility (what did it do?), Rationale Visibility (why did it do it?), Result Visibility (what was the outcome?). All three are needed for full understanding.
- **Log Patterns**: Success (READ -> ANALYZE -> EDIT -> VERIFY -> COMPLETE), Warning (EDIT -> EDIT -> EDIT -> no verification -> COMPLETE), Failure (EDIT -> VERIFY fails -> EDIT -> fails again -> gave up). Recognizing these patterns enables rapid diagnosis.
- **Trust Through Transparency**: Trust isn't given, it's earned. When you can see decisions, correct mistakes early, and learn agent patterns, you feel confident granting more autonomy.
- **Black Box Problem**: Without observability, you only see final results. With observability, you see the full context--which action caused a problem, what the agent's reasoning was, and where to intervene.

### Key Facts
- **Claude Code activity logs**: Stored in `.claude/activity-logs/prompts.jsonl` (all prompts and responses) and `subagent-usage.jsonl` (delegation tracking)
- **Cowork observability advantage**: Three-panel layout (chat, progress, artifacts) designed specifically for simultaneous visibility without context switching
- **Claude Code observability advantage**: Full terminal transparency--every command, file read, and output visible in real-time with nothing hidden

### Critical Patterns
- Three workflow design patterns for observability: Explain Before Executing (show plan, get approval), Checkpoint After Major Steps (verify progress incrementally), Summary After Completion (provide full review context)
- Debugging through logs: trace the sequence of actions, identify where behavior diverged from expectation, check whether verification steps were performed
- Essential observability toolkit: Git history (git log, git diff, git blame), Activity log review (JSON parsing of .claude logs), Test result comparison (before/after saved outputs)
- Both interfaces provide the same observability layers (Plan, Actions, Outputs, Errors) through different mechanisms--terminal text vs. GUI panels

### Common Mistakes
- Silent failures: AI says "Done!" but something actually failed--require visibility for all operations, not just successes
- Output without context: seeing a diff without understanding why the change was made--require rationale with every significant change
- Missing intermediate steps: AI works for 2 minutes then reports completion with no visibility into what happened--require progress updates for long-running tasks
- Not reviewing activity logs when debugging: spending hours manually investigating when the log would show exactly which change caused the problem

### Connections
- **Builds on**: Principle 6 (Constraints and Safety)--observability validates that safety constraints are working and shows when they're triggered; you need visibility to know your guardrails are effective
- **Leads to**: Lesson 8 (Putting It All Together)--observability is the final principle that enables evaluating whether all other principles are being applied correctly in integrated workflows
