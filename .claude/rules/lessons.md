# Project Lessons

Patterns learned from corrections. Review at session start.

---

## 2025-11-18 Pedagogical Layer

**Mistake**: Applied L4 (Spec-Driven) thinking to L1 (Manual Foundation) chapter
**Pattern**: Assumed "no code examples" meant "teach specs instead of syntax"
**Rule**: Always check Part number via `ls -d` before assuming student knowledge level

---

## 2025-11-27 Format Drift

**Mistake**: Taught flat skill file format instead of directory structure
**Pattern**: Didn't read canonical source (Chapter 5 Lesson 7) before teaching format
**Rule**: Always read canonical source for any pattern being taught

---

## 2025-12-26 Content Quality (Chapter 2)

**Mistake**: Hallucinated facts, missing YAML frontmatter, weak "Try With AI" sections
**Pattern**: Bypassed subagent orchestration, wrote content directly
**Rule**: NEVER write lesson content directly - always use content-implementer subagent

---

## 2026-01-15 DocPageActions

**Mistake**: Implemented GitHub fetch when Turndown library already existed
**Pattern**: Started coding before researching existing solutions
**Rule**: WebSearch for existing plugins/libraries BEFORE implementing any feature

---

## 2026-02-03 Agent Tool Access

**Mistake**: Assumed agents without `tools:` field had NO tools
**Pattern**: Guessed framework behavior instead of verifying
**Rule**: Omitting `tools:` = ALL tools. Verify framework behavior, don't assume.

---

## 2026-02-03 Skill References

**Mistake**: 7 agents referenced 9 non-existent skills
**Pattern**: Skills were removed but agent references weren't updated
**Rule**: When removing a skill, grep all agents for references: `grep -r "skill-name" .claude/agents/`

---

## 2026-02-04 Live Verification Before Commits (CRITICAL)

**Mistake**: Pushed ChatKit model picker + wrong import path to main without local testing - broke production for 3+ hours
**Pattern**: Made code changes, assumed they would work, committed and pushed without running the actual server
**Rule**: NEVER commit to main branch without live verification:
1. Start the services yourself: `pnpm nx serve study-mode-api`, `pnpm nx serve learn-app`
2. Make a real request through the UI or API
3. Verify the full flow works end-to-end
4. Check logs for errors
5. Only then commit and push

**Especially critical for**:
- Import statements (modules may not exist in all environments)
- API/SDK features (documentation may not match installed version)
- Any changes touching startup/initialization code

**Don't assume user is running services** - start them yourself and test.
