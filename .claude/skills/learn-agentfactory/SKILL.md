---
name: learn-agentfactory
description: Browse and study The AI Agent Factory book content via the Content API. Use when users want to read lessons, browse the book structure, track progress, or complete exercises through the CLI.
version: 0.2.0
allowed-tools: Bash, Read
---

# Learn AgentFactory

Browse and study The AI Agent Factory book via the Panaversity Content API.

---

## Configuration

The skill needs two URLs. Both default to production — override via env vars for local dev.

| Service     | Env Var              | Default (production)                    |
| ----------- | -------------------- | --------------------------------------- |
| Content API | `CONTENT_API_URL`    | `https://content-api.panaversity.org`   |
| SSO (auth)  | `PANAVERSITY_SSO_URL`| `https://sso.panaversity.org`           |

Content is served from GitHub via the Content API (cached in Redis). No local content files needed.

**Local dev** (if running services locally):

```bash
export CONTENT_API_URL=http://localhost:8001
export PANAVERSITY_SSO_URL=http://localhost:3001
```

---

## Authentication

Before any API call, ensure the user is authenticated.

### Check credentials

```bash
cat ~/.agentfactory/credentials.json 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print('Authenticated' if d.get('access_token') else 'No token')" 2>/dev/null || echo "Not authenticated"
```

### If not authenticated (or token expired)

Run the device-flow auth script:

```bash
python3 scripts/auth.py
```

This opens a browser for SSO login. The user enters the displayed code, and tokens are saved to `~/.agentfactory/credentials.json` (chmod 600).

### Load token for requests

```bash
TOKEN=$(python3 -c "import json; print(json.load(open('$HOME/.agentfactory/credentials.json'))['access_token'])")
BASE_URL="${CONTENT_API_URL:-https://content-api.panaversity.org}"
```

Use `Authorization: Bearer $TOKEN` on all API requests.

If any request returns **401**, prompt the user to re-authenticate by running `scripts/auth.py` again.

---

## Commands

### 1. Browse Book Structure

Fetch the full book tree and display it as a navigable outline.

```bash
curl -s -H "Authorization: Bearer $TOKEN" "$BASE_URL/api/v1/content/tree" | python3 -m json.tool
```

**Display guidance**:

- Show parts as top-level headings
- Show chapters indented under parts
- Show lesson titles indented under chapters
- Include lesson count per chapter

### 2. Read a Lesson

Fetch and display a single lesson by part, chapter, and lesson slug (all available from the tree response).

```bash
curl -s -H "Authorization: Bearer $TOKEN" \
  "$BASE_URL/api/v1/content/lesson?part={part_slug}&chapter={chapter_slug}&lesson={lesson_slug}" \
  | python3 -m json.tool
```

**Display guidance**:

- Show the lesson title prominently
- Show skills and learning objectives from frontmatter
- Render the MDX body as readable text
- Strip JSX components that don't render in terminal (keep code blocks)

### 3. Complete a Lesson

Mark a lesson as done and earn XP.

```bash
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"chapter_slug": "{chapter_slug}", "lesson_slug": "{lesson_slug}", "active_duration_secs": 120}' \
  "$BASE_URL/api/v1/content/complete"
```

### 4. Progress

Show the user's reading history. Aggregate from the tree endpoint data to display:

- Total lessons read / total available
- Chapters in progress
- XP earned
- Suggested next lesson

---

## Teaching Prompts

After displaying a lesson, offer lightweight teaching support:

### Quiz on Key Concepts

> "Want me to quiz you on the key concepts from this lesson?"

Generate 3-5 quick conceptual questions based on the frontmatter skills and learning objectives. Keep questions at the Apply level (not recall).

### Highlight Objectives

After showing lesson content, summarize:

- **Skills** from frontmatter (what the student can DO after this lesson)
- **Learning Objectives** (what they should UNDERSTAND)

### Suggest Next Lesson

Use the tree structure to identify the next lesson in sequence:

> "Ready for the next lesson? Up next: [Lesson Title] in [Chapter Name]."

### Socratic Questioning

When a user asks about a concept from the lesson, respond with guided questions before giving answers:

> "Good question. Before I answer directly -- based on what you just read about [concept], what do you think would happen if [scenario]?"

Use sparingly (1-2 Socratic prompts per concept, then give the answer).

---

## Error Handling

| Status           | Action                                                  |
| ---------------- | ------------------------------------------------------- |
| 401 Unauthorized | Token expired. Re-run: `python3 scripts/auth.py`       |
| 404 Not Found    | Slug is wrong. Show available options from tree.        |
| 429 Rate Limited | Wait and retry. Inform user of rate limit.              |
| 5xx Server Error | API is down. Suggest trying again later.                |

---

## Typical Session Flow

1. **Authenticate** (check credentials, run scripts/auth.py if needed)
2. **Browse** the book tree to pick a chapter/lesson
3. **Read** the lesson
4. **Discuss** -- quiz, Socratic questions, clarify concepts
5. **Complete** the exercise when done
6. **Next** -- suggest and load the next lesson
