---
name: learn-agentfactory
description: Browse and study The AI Agent Factory book content via the Content API. Use when users want to read lessons, browse the book structure, track progress, or complete exercises through the CLI.
version: 0.1.0
allowed-tools: Bash, Read
---

# Learn AgentFactory

Browse and study The AI Agent Factory book via the Panaversity Content API.

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
python3 /Users/mjs/Documents/code/panaversity-official/tutorsgpt/ag2/.claude/skills/learn-agentfactory/auth.py
```

This opens a browser for SSO login. The user enters the displayed code, and tokens are saved to `~/.agentfactory/credentials.json`.

### Load token for requests

```bash
TOKEN=$(python3 -c "import json; print(json.load(open('$HOME/.agentfactory/credentials.json'))['access_token'])")
```

Use `Authorization: Bearer $TOKEN` on all API requests.

If any request returns **401**, prompt the user to re-authenticate by running `auth.py` again.

---

## API Configuration

| Setting   | Value                                                       |
| --------- | ----------------------------------------------------------- |
| Base URL  | `$CONTENT_API_URL` or `https://content-api.panaversity.org` |
| Local dev | `http://localhost:8001`                                     |
| Auth      | `Authorization: Bearer {access_token}`                      |

```bash
BASE_URL="${CONTENT_API_URL:-https://content-api.panaversity.org}"
```

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
- Mark completed lessons if progress data is available

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

### 3. Complete an Exercise

Mark a lesson exercise as done and earn XP.

```bash
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"chapter_slug": "{chapter_slug}", "lesson_slug": "{lesson_slug}"}' \
  "$BASE_URL/api/v1/content/complete"
```

### 4. Progress

Show the user's reading history and completion stats. Aggregate from the tree endpoint data (completed flags) to display:

- Total lessons read / total available
- Chapters in progress
- XP earned
- Suggested next lesson

---

## Teaching Prompts

After displaying a lesson, offer lightweight teaching support:

### Quiz on Key Concepts

> "Want me to quiz you on the key concepts from this lesson?"

Generate 3-5 quick conceptual questions based on the lesson's skills and learning objectives listed in the YAML frontmatter. Keep questions at the Apply level (not recall).

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

Use this sparingly (1-2 Socratic prompts per concept, then give the answer). The goal is to deepen understanding, not frustrate.

---

## Error Handling

| Status           | Action                                                             |
| ---------------- | ------------------------------------------------------------------ |
| 401 Unauthorized | Token expired. Prompt re-auth: `python3 .../auth.py`               |
| 404 Not Found    | Chapter or lesson slug is wrong. Show available options from tree. |
| 429 Rate Limited | Wait and retry. Inform user of rate limit.                         |
| 5xx Server Error | API is down. Suggest trying again later or using local dev.        |

---

## Typical Session Flow

1. **Authenticate** (check credentials, run auth.py if needed)
2. **Browse** the book tree to pick a chapter/lesson
3. **Read** the lesson
4. **Discuss** -- quiz, Socratic questions, clarify concepts
5. **Complete** the exercise when done
6. **Next** -- suggest and load the next lesson
