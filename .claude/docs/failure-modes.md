# Failure Modes Reference

Read this when you need examples of what NOT to do.

## Chapter 9: Wrong Pedagogical Layer

**Date**: 2025-11-18

**Error**: Applied Layer 4 (Spec-Driven) thinking to a Layer 1 (Manual Foundation) chapter.

**What went wrong**:
- Did NOT read chapter-index.md to check Part number
- Did NOT verify what students know at this stage
- Assumed "no code examples" meant "teach specifications instead of syntax"
- Created 5 new lessons before user pointed out fundamental misunderstanding

**Fix**: Always read chapter-index.md first. Part 3 = students have NO programming yet.

---

## Chapter 14: Format Drift

**Date**: 2025-11-27

**Error**: Taught wrong skill file format.

**What went wrong**:
- Used flat file format instead of directory structure
- Missing YAML frontmatter
- Did NOT read Chapter 5 Lesson 7 which teaches correct format

**Correct format**:
```
.claude/skills/
└── skill-name/
    └── SKILL.md  # With YAML frontmatter
```

---

## Skill → Spec Bypass

**Date**: 2025-11-29

**Error**: Wrote spec directly instead of using `/sp.specify`.

**What went wrong**:
- Used skill for brainstorming (correct)
- Then wrote `specs/*/spec.md` directly with Write tool
- Never invoked `/sp.specify`

**Fix**: Skills INFORM specs, they don't REPLACE the workflow.

---

## Folder Naming Inconsistency

**Date**: 2025-11-29

**Error**: Used 3 different folder names for same feature.

**Prevention**: Before creating any artifact:
```bash
find specs/ history/prompts/ -type d -name "*feature*" | head -1
```

---

## Subagent Deadlock

**Date**: 2025-12-23

**Error**: Subagents waited for confirmation that never came.

**What went wrong**:
- Launched 12 parallel agents
- 2 included "Is this correct? Should I proceed?"
- Subagents cannot receive human confirmation

**Fix**: Always include "Execute autonomously without confirmation" in subagent prompts.
