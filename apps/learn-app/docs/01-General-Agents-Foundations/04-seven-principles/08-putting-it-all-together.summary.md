### Core Concept
The seven principles are most powerful when applied together in integrated workflows. Real tasks require multiple principles working in combination, and the meta-principle underlying all seven is that general agents are most effective when they leverage computing fundamentals (filesystems, shells, code execution, version control) rather than fighting against them--whether accessed through Claude Code's terminal or Cowork's desktop GUI.

### Key Mental Models
- **Principle Prioritization by Task**: Different tasks emphasize different principles--debugging (1, 3, 7), refactoring (2, 4, 5), new features (all), setup (1, 5, 6), performance (1, 3, 7). Not all principles are equally critical for every task.
- **Workflow Templates**: Quick Fix (describe -> investigate -> propose diff -> approve -> apply -> verify -> commit), Feature Development (spec -> context -> decompose -> implement/verify loop -> integration test -> commit), Refactoring (document -> plan -> branch -> extract/verify loop -> integrate -> merge).
- **Meta-Principle**: All seven principles derive from one insight--leverage computing fundamentals (filesystems, shells, version control) as foundations for reliable, debuggable agent workflows rather than treating them as limitations.
- **Interface Selection**: Choose Claude Code for maximum observability, custom constraints, and programmatic precision; choose Cowork for minimal friction, built-in safety prompts, and non-technical accessibility. Many workflows benefit from using both.

### Key Facts
- **Complete feature workflow timeline**: A password reset feature moves from test specification (0:00) through CLAUDE.md update, decomposition, 8 implementation steps with verification, full test suite, review, to commit in about 60 minutes
- **Principle combinations**: Terminal + Code + Verification enables autonomous investigation, implementation, and testing; Decomposition + Safety + Observability ensures small, safe, visible steps; State Persistence ensures context compounds across sessions
- **Both interfaces run on same foundations**: Same Claude Agent SDK, same reasoning engine, same fundamental approach--one through terminal, one through GUI

### Critical Patterns
- Self-assessment checklist across all 7 principles with specific behaviors to verify (e.g., "you're not copying/pasting code manually" for P1, "you never accept code without testing" for P3, "you maintain CLAUDE.md" for P5)
- Three complete workflow walkthroughs: debugging a production issue (emphasizing investigation and verification), implementing a new feature (all principles in sequence), refactoring a large module (emphasizing decomposition and safety)
- Principle integration compounds: the workflow moves from "using AI" to "collaborating with an intelligent agent" when all principles work together--you provide intent, AI investigates and proposes, you review and redirect, AI implements and verifies, you approve
- Interface choice is task-dependent, not absolute: Code excels at raw observability and custom constraints; Cowork excels at friction-free document workflows and non-technical accessibility

### Common Mistakes
- Applying principles in isolation without considering how they reinforce each other (verification without decomposition means testing large unclear changes; decomposition without observability means invisible progress)
- Using the same approach for all task types regardless of which principles are most critical (a quick bug fix needs investigation and verification more than state persistence)
- Choosing one interface exclusively when both have complementary strengths (Code for implementation, Cowork for documentation and review)
- Treating principles as a checklist to complete rather than a framework for judgment (the goal is appropriate application based on task characteristics, not rigid adherence to all seven for every task)

### Connections
- **Builds on**: All seven preceding lessons (Principles 1-7)--this lesson synthesizes them into integrated workflows
- **Leads to**: Part 2 and beyond--complex file processing, data analysis, multi-step research, automated document generation, browser automation, and building custom agents, all applying these principles at increasing sophistication
