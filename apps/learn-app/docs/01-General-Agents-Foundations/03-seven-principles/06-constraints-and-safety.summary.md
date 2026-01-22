### Core Concept
Constraints enable autonomy--thoughtful safety measures and guardrails are what allow you to give AI systems meaningful power without risking damage. The same paradox applies in both interfaces: Claude Code uses configurable permission flags and hooks, while Cowork uses built-in confirmation dialogs, but both implement the principle that bounded capability enables trust.

### Key Mental Models
- **Safety Hierarchy (Defense in Depth)**: Five layers from Technical Constraints (hard limits) through Permission Controls, Environment Isolation, Process Controls, to Human Verification--no single layer is sufficient alone.
- **Trust Gradualism**: Phase 1 (observation only, week 1) -> Phase 2 (supervised autonomy, weeks 2-4) -> Phase 3 (selective autonomy, months 2-3) -> Phase 4 (calibrated autonomy, month 3+). Build trust through evidence.
- **Risk Spectrum**: Five categories of what can go wrong--Data Loss, Security Vulnerabilities, Cost Overruns, Reputation Damage, Workflow Disruption--each requiring different protective measures.
- **Permission Models**: Permissive (auto-approve safe ops), Confirming (approve all writes), Restricted (read-only sandbox)--choose based on experience, familiarity, and risk tolerance.
- **Constraints Enable Capability**: The paradox--when you trust the safety model, you give agents more autonomy. Without constraints, you'd never let either agent do meaningful work.

### Key Facts
- **Destructive operations list**: File ops (rm, mv with overwrite), Version control (reset --hard, push --force, clean -fd), Package management (install commands), System ops (sudo, kill -9), Data ops (DROP, DELETE without WHERE)
- **Sandbox strategies**: Docker containers, staging environments, feature branches, separate credentials--each isolates AI work from production
- **Trust signals to track**: Error rate, correction ease, pattern adherence, and risk awareness--these determine when to increase autonomy

### Critical Patterns
- Pre-session safety checklist: verify correct directory, correct branch, correct environment variables, uncommitted work backed up
- Incident response sequence: Stop AI (Ctrl+C) -> Assess damage (git status/diff) -> Revert if needed (git checkout/reset) -> Post-incident review (what constraint would have prevented this?)
- In Cowork, confirmation dialogs ARE the constraint system--"Should I delete this file?" implements the same principle as Claude Code's permission model through the GUI
- Match permission model to context: first-time with AI (Confirming), routine familiar work (Permissive), exploring unfamiliar code (Restricted), production (Confirming + Staging)

### Common Mistakes
- Going from zero autonomy to full autonomy overnight (trust should be graduated through phases, not granted all at once)
- Having no rollback plan before starting AI work (always know how to revert: git checkout, git reset, feature branch deletion)
- Applying the same permission level to all tasks regardless of risk (prototype exploration vs. production database changes need fundamentally different safety levels)
- Thinking safety means restricting AI to uselessness (the goal is preventing certain things while enabling everything else--constraints should be targeted, not blanket)

### Connections
- **Builds on**: Principle 5 (Persisting State in Files)--safety rules can be encoded in context files (CLAUDE.md restrictions, hooks configuration), making constraints persistent and automatic
- **Leads to**: Principle 7 (Observability)--constraints are only effective if you can see when they're triggered and verify they're working; observability validates the safety model
