### Core Concept
Code is the most precise communication medium between humans and AI because it eliminates the ambiguity inherent in natural language. Whether expressed as executable code (Claude Code) or structured templates and formats (Claude Cowork), precise structured expression beats vague natural language for human-AI collaboration.

### Key Mental Models
- **Translation Chain**: Intent (mental model) -> Specification (natural language) -> AI Understanding -> Implementation (code) -> Evaluation. Each arrow is a point where meaning can be lost; code minimizes these losses.
- **Specification Quality Spectrum**: From Level 1 (vague intent: "make it better") through Level 2 (feature description) and Level 3 (behavioral specification) to Level 4 (example-driven specification with concrete inputs/outputs).
- **Code as Feedback Mechanism**: Instead of debating in natural language, iterate through code changes--each round produces reviewable, verifiable artifacts that narrow the gap between intent and implementation.
- **Tests as Specifications**: Writing tests first expresses requirements as executable code, giving AI an unambiguous implementation target and giving you an automatic verification mechanism.

### Key Facts
- **Ambiguity cost scales**: Small script miscommunication costs 5 minutes; product-level miscommunication costs 2 weeks
- **Code-based feedback is verifiable**: "Add try-catch around the database call" is actionable and confirmable; "add better error handling" is not
- **Reading code is a collaborative skill**: You don't need to write the code yourself, but you must be able to read, understand, and evaluate AI-generated code

### Critical Patterns
- Provide specifications anchored in code examples rather than abstract descriptions--show current behavior and desired behavior with concrete data structures
- Use code diffs as the primary feedback channel: point to specific lines, propose exact changes, reference existing patterns in the codebase
- The principle generalizes: in Cowork, structured document templates and explicit format requirements serve the same role as code specifications--eliminating ambiguity through structure
- Reading AI-generated code means asking: What does it DO? What was the INTENT? Do behavior and intent match? What assumptions exist? What could go wrong?

### Common Mistakes
- Providing vague requirements and expecting AI to read your mind (the fix is higher-quality specifications, not more iterations)
- Giving natural language feedback like "make it better" instead of code-anchored feedback like "cache the user lookup so we don't query twice"
- Thinking code-as-interface means you must be a programmer (structured formats, templates, and examples apply the same principle in non-code contexts)
- Skipping code review because AI-generated code "looks right" (race conditions, missing error handling, and wrong assumptions hide in plausible-looking code)

### Connections
- **Builds on**: Principle 1 (Bash as Universal Interface)--terminal access enables reading and writing code directly, making code the shared artifact
- **Leads to**: Principle 3 (Verification as Core Step)--once code is the shared interface, you can run it to verify correctness rather than debating in natural language
