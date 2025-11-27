---
name: session-intelligence-harvester
description: This skill should be used after productive sessions to extract learnings and route them to appropriate Reusable Intelligence Infrastructure (RII) components. Use when corrections were made, format drift was fixed, new patterns emerged, or the user explicitly asks to "harvest learnings" or "capture session intelligence". Transforms one-time fixes into permanent organizational knowledge.
---

# Session Intelligence Harvester

## Overview

Transform session learnings into permanent organizational intelligence. After productive sessions involving corrections, discoveries, or pattern identification, this skill systematically extracts what was learned and routes it to the correct RII component (CLAUDE.md, constitution, agents, skills, commands).

## When to Use This Skill

**Automatic Triggers** (suggest harvesting):
- Session corrected format drift (wrong file structure, YAML, invocation)
- Session added missing checks to orchestration files
- Session identified failure mode worth preventing
- Session touched 3+ files with similar pattern corrections
- PHR was created documenting significant learning

**Manual Triggers** (user requests):
- "Harvest learnings from this session"
- "Capture session intelligence"
- "What should we encode from this work?"
- "Update RII with what we learned"

## Workflow

### Step 1: Session Analysis

Analyze the session by answering:

```
1. CORRECTIONS MADE
   - What errors/drift were corrected?
   - What was wrong vs what is now correct?
   - Why did the error occur? (missing check, format drift, etc.)

2. PATTERNS IDENTIFIED
   - What recurring patterns emerged?
   - What canonical sources were referenced?
   - What validation would have caught this earlier?

3. LEARNING CLASSIFICATION
   - Context-gathering gap? (CLAUDE.md)
   - Pedagogical/teaching issue? (Constitution)
   - Agent convergence pattern? (Agents)
   - Reusable workflow? (Skills)
   - Missing orchestration check? (Commands)
```

### Step 2: Route to RII Components

Use this routing table to determine where learnings belong:

| Learning Type | Target Component | Location | What to Add |
|---------------|------------------|----------|-------------|
| Context-gathering gaps | CLAUDE.md | Section I | New step in context protocol |
| Failure mode example | CLAUDE.md | Failure modes | New failure mode section |
| Pedagogical framework | Constitution | Section IIa | Teaching method update |
| Agent convergence pattern | Agent file | Convergence Patterns | New pattern with correction |
| Agent self-monitoring | Agent file | Self-Monitoring Checklist | New checklist item |
| Canonical source lookup | Multiple agents | Analysis Questions | Cross-reference check |
| Reusable workflow | New skill | .claude/skills/ | New SKILL.md |
| Orchestration check | Command file | Phase 0 or relevant phase | New validation step |
| Format specification | Canonical source chapter | Lesson content | Authoritative format |

### Step 3: Generate Updates

For each identified learning, generate:

```markdown
## Learning: [Brief Title]

**Type**: [Context gap | Failure mode | Convergence pattern | etc.]

**Target**: [File path]

**Current State**:
[What's missing or incorrect]

**Proposed Addition**:
[Exact content to add, with surrounding context for placement]

**Rationale**:
[Why this prevents recurrence]

**Canonical Source** (if applicable):
[Which chapter/lesson defines the authoritative format]
```

### Step 4: Validation Checks

Before finalizing updates, verify:

```
- [ ] Each learning has clear target component
- [ ] Updates include exact placement location
- [ ] Canonical sources identified for format-related learnings
- [ ] No duplicate information (check existing content first)
- [ ] Updates use imperative form (agent files) or appropriate style
- [ ] Cross-references added where pattern appears in multiple files
```

### Step 5: Create PHR (Optional)

If session learnings are significant, create PHR documenting:
- What was learned
- Where it was encoded
- Why this improves future work

Use stage: `misc` for general learnings, or appropriate feature stage if tied to specific feature.

## RII Component Reference

### CLAUDE.md Structure

```
Section I: Context Gathering Protocol
  - Step 1-N: Sequential context steps
  - "Find canonical source" step for pattern teaching

Failure Modes:
  - Named failure examples with what went wrong
  - "What I should have done" corrections
```

### Agent File Structure

```
Analysis Questions (Section III):
  - Numbered questions with "Why this matters"

Principles (Section IV):
  - Decision frameworks with application guidance

Convergence Patterns (Section VI):
  - Generic pattern → Why it's convergence → Correction

Self-Monitoring Checklist (Section VIII):
  - Numbered checklist items
```

### Command File Structure

```
Phase 0: Foundation checks
  - Constitutional reading
  - Canonical source checks (for educational content)

Convergence Patterns (Section VI):
  - Pattern detection and correction guidance
```

## Output Format

After harvesting, provide summary:

```markdown
## Session Intelligence Harvest Summary

**Session**: [Brief description]
**Date**: [ISO date]

### Learnings Extracted: [N]

| # | Learning | Type | Target | Status |
|---|----------|------|--------|--------|
| 1 | [Title] | [Type] | [File] | [Applied/Proposed] |
| 2 | [Title] | [Type] | [File] | [Applied/Proposed] |

### Updates Applied

1. **[File]**: [What was added]
2. **[File]**: [What was added]

### PHR Created
- Path: [PHR path if created]
- Stage: [Stage]

### Canonical Sources Referenced
- [Pattern]: [Chapter X Lesson Y]

### Recommended Follow-ups
- [Any additional work needed]
```

## Examples

### Example 1: Format Drift Correction

**Session**: Fixed Chapter 14 skill format to match Chapter 5 canonical source

**Harvest**:
```
Learning: Skill format drift
Type: Convergence pattern + Missing check
Targets:
  - chapter-planner.md (new convergence pattern)
  - sp.loopflow.v2.md (canonical source check in Phase 0)
  - content-implementer.md (post-implementation checklist)
  - CLAUDE.md (failure mode example)

Updates:
1. Added Convergence Pattern 6: Format Drift to chapter-planner
2. Added Step 1.5: Canonical Source Check to sp.loopflow
3. Added failure mode "Chapter 14 Format Drift" to CLAUDE.md
```

### Example 2: Missing Validation

**Session**: Discovered lessons weren't checking chapter-index.md for prerequisites

**Harvest**:
```
Learning: Missing prerequisite validation
Type: Context-gathering gap
Target: CLAUDE.md Section I

Update:
- Added Step 1 requirement to read chapter-index.md
- Extract Part number, proficiency level, prerequisites
```

## Self-Monitoring

Before completing harvest, verify:

- [ ] All corrections from session are captured
- [ ] Each learning is routed to correct component
- [ ] Updates include exact placement context
- [ ] Canonical sources identified where applicable
- [ ] No information duplicated across components
- [ ] Multi-file patterns have cross-references added
- [ ] Summary accurately reflects changes made
