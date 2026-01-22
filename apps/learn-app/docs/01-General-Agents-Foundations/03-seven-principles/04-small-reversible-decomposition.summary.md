### Core Concept
Breaking complex problems into small, independently verifiable steps that can be easily rolled back is the key to managing complexity in agentic workflows. This applies whether you are making code commits (Claude Code) or requesting document sections one at a time (Claude Cowork)--large tasks fail silently while small tasks fail loudly.

### Key Mental Models
- **Atomic Change**: The smallest unit of work that can be independently verified, makes sense on its own, and can be reverted without breaking other work. One logical concern per commit.
- **Debugging Mathematics**: Bug-finding cost grows exponentially with change size. Ten small tested changes of 10 lines each (50 min max debugging) beat one 100-line change (potentially hours of debugging).
- **AI Amplification Effect**: AI makes plausible-looking mistakes, doesn't learn your context, and can generate large volumes of code quickly--making decomposition even more critical than in manual development.
- **Progressive Elaboration Pattern**: "Break this into small steps. For each step: tell me what you're about to do, make the change, show me what changed, wait for approval."

### Key Facts
- **Cognitive limit**: Humans hold about 7 plus or minus 2 items in working memory--large changes exceed this, causing missed interactions and untested components
- **Small iteration timeline**: Many small verified steps complete a feature in 2-3 days with low stress; one large batch takes 7 days with high stress and uncertain outcome
- **Reversibility mechanism**: Git provides natural reversibility--each commit is a revertable unit, feature branches isolate experiments, stash enables safe exploration

### Critical Patterns
- Four decomposition strategies: Vertical Slicing (by feature, across layers), Horizontal Slicing (by layer, across features), Dependency-First (prerequisites before dependents), Test-First (test then implement, repeat)
- Good commit boundaries: one concern per commit, each commit leaves code in working state, each can be independently reverted
- The principle generalizes to Cowork: ask for outline first (verify), then section 1 (verify), then section 2--if section 3 goes wrong, you keep sections 1-2
- Prompt AI for decomposed work: "Let's do this step by step. Start with just X. After I review, we'll move to step 2."

### Common Mistakes
- Micro-commits (too fine-grained, e.g., "fix typo" three times--group related tiny fixes into one atomic change)
- Mixed concerns (unrelated changes in one commit, e.g., "add auth AND fix UI bug"--makes reverting one impossible without losing the other)
- Untested middle states (commit that doesn't compile, followed by "fix compilation"--intermediate states should always work)
- Accepting large AI-generated changes without decomposition (hundreds of lines across many files are impossible to review thoroughly and hard to debug)

### Connections
- **Builds on**: Principle 3 (Verification as Core Step)--small changes make verification tractable; you know exactly what to test after each step
- **Leads to**: Principle 5 (Persisting State in Files)--as you decompose work into steps, documenting the plan and progress in files ensures continuity across sessions
