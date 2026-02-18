---
name: learn-agentfactory
description: Browse and study The AI Agent Factory book content via the Content API. Use when users want to read lessons, browse the book structure, track progress, or complete exercises through the CLI.
version: 0.3.0
allowed-tools: Bash, Read
---

# Learn AgentFactory

Browse and study The AI Agent Factory book via the Panaversity Content API.

All API calls go through `scripts/api.py` — it handles token loading, auth headers, error messages, and JSON output automatically. No manual curl or token management needed.

---

## Configuration

Both URLs default to production. Override via env vars for local dev:

| Service     | Env Var              | Default                                 |
| ----------- | -------------------- | --------------------------------------- |
| Content API | `CONTENT_API_URL`    | `https://content-api.panaversity.org`   |
| SSO (auth)  | `PANAVERSITY_SSO_URL`| `https://sso.panaversity.org`           |

---

## Authentication

Check if authenticated, then run device-flow auth if needed:

```bash
python3 scripts/api.py health
```

If the health check works but API calls return "Token expired", re-authenticate:

```bash
python3 scripts/auth.py
```

This opens a browser for SSO login. Tokens are saved to `~/.agentfactory/credentials.json`.

---

## Commands

### Browse Book Structure

```bash
python3 scripts/api.py tree
```

Returns parts, chapters, and lessons as JSON. Display as a navigable outline:
- Parts as top-level headings
- Chapters indented under parts
- Lesson titles indented under chapters with count per chapter

### Read a Lesson

```bash
python3 scripts/api.py lesson {part_slug} {chapter_slug} {lesson_slug}
```

Returns JSON with `content` (markdown body, frontmatter stripped), `frontmatter` (title, skills, objectives), and `credit_charged`.

Display guidance:
- Show lesson title prominently
- Show skills and learning objectives from frontmatter
- Render markdown body as readable text
- Strip JSX components that don't render in terminal

### Complete a Lesson

```bash
python3 scripts/api.py complete {chapter_slug} {lesson_slug} {active_duration_secs}
```

Returns `completed` status and `xp_earned`.

---

## Teaching Prompts

After displaying a lesson, offer teaching support:

**Quiz**: Generate 3-5 conceptual questions from frontmatter skills/objectives at Apply level.

**Objectives summary**: After content, list Skills (what student can DO) and Learning Objectives (what they UNDERSTAND).

**Next lesson**: Use tree structure to suggest the next lesson in sequence.

**Socratic**: When asked about a concept, ask 1-2 guided questions before answering directly.

---

## Error Handling

`scripts/api.py` handles all errors with actionable messages:

| Error | Meaning |
| ----- | ------- |
| "Not authenticated" | No credentials file. Run `scripts/auth.py` |
| "Token expired" | 401 from API. Run `scripts/auth.py` |
| "Payment required" | 402 — insufficient credits |
| "Not found" | Wrong slugs. Show tree to find correct ones |
| "Rate limited" | 429 — wait and retry |
| "Connection failed" | API unreachable. Check URL or try later |

---

## Typical Session Flow

1. `python3 scripts/api.py tree` — browse the book
2. Pick a lesson from the tree output
3. `python3 scripts/api.py lesson ...` — read the lesson
4. Discuss — quiz, Socratic questions, clarify concepts
5. `python3 scripts/api.py complete ...` — mark done, earn XP
6. Suggest next lesson from the tree
