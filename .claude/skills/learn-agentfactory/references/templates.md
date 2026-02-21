# Learner Data Templates

Templates for persistent learner files at `~/.agentfactory/learner/`.

## MEMORY.md

```markdown
# Learner Profile

## Identity

- Name: {asked on first session}
- Tutor name: {what they want to call their AI tutor — e.g., "Coach", "Professor Ada", "Claude"}
- Started: {date}
- Sessions: {count}

## Learning Style

- Pace: {fast/steady/careful — observe and update}
- Prefers: {examples/theory/hands-on — observe and update}
- Preferred modes: {which teaching modes work best — observe and update}
- Strengths: {topics they grasp quickly}
- Struggles: {topics needing review}
- Teach-back quality: {strong/developing/weak — tracks Feynman verification ability}

## Progress

- Completed: {X}/{Y} lessons
- Current chapter: {slug}
- Total XP: {number}

## Quiz History

| Date | Lesson | Score | Weak Areas |
| ---- | ------ | ----- | ---------- |

## Session Log

| Date | Lessons Covered | Observations |
| ---- | --------------- | ------------ |
```

## session.md

Write this so you can recover after context compaction:

```markdown
# Active Session

- Lesson: {part/chapter/lesson slugs}
- Phase: {greeting | browsing | teaching | quizzing | practicing | completing}
- Active mode: {tutor | coach | socratic | mentor | simulator | manager}
- Teaching at: {which section of the lesson}
- Key context: {what the learner just said or asked}
- Next action: {what you should do next}
```
