"""
ChatKit Server for Interactive Study Mode

CRITICAL: This chatbot answers ONLY from book content.
It must NOT use general LLM knowledge.

Modes:
- Teach: Socratic method, focused on current page
- Ask: Book-wide Q&A, search across content
"""

import os
import glob
from pathlib import Path
from typing import List
import time

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import Response, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents import Agent, Runner

# Load environment variables
load_dotenv()

# =============================================================================
# Configuration
# =============================================================================

# Book content base path - use absolute path from project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
CONTENT_BASE_PATH = os.getenv(
    "CONTENT_BASE_PATH",
    str(PROJECT_ROOT / "apps" / "learn-app" / "docs")
)
print(f"Content base path: {CONTENT_BASE_PATH}")

# =============================================================================
# Book Content Loader
# =============================================================================

def load_lesson_content(lesson_path: str) -> tuple[str, str]:
    """
    Load lesson content from filesystem based on path.

    Handles paths like:
    - "Coding-for-Problem-Solving/README" -> finds "04-Coding-for-Problem-Solving/README.md"
    - "01-General-Agents-Foundations/01-agent-factory-paradigm/01-the-2025-inflection-point"
    """
    if not lesson_path:
        print("No lesson path provided")
        return "", "Unknown Page"

    # Clean the path
    clean_path = lesson_path.strip("/")
    if clean_path.startswith("docs/"):
        clean_path = clean_path[5:]

    print(f"Loading content for: {clean_path}")
    print(f"Base path: {CONTENT_BASE_PATH}")

    # Split path into segments
    segments = clean_path.split("/")

    # Try direct path first
    direct_paths = [
        Path(CONTENT_BASE_PATH) / f"{clean_path}.md",
        Path(CONTENT_BASE_PATH) / f"{clean_path}.mdx",
        Path(CONTENT_BASE_PATH) / clean_path / "index.md",
        Path(CONTENT_BASE_PATH) / clean_path / "README.md",
    ]

    for file_path in direct_paths:
        if file_path.exists():
            try:
                content = file_path.read_text(encoding="utf-8")
                title = extract_title(content, clean_path)
                print(f"Found direct: {file_path} -> {title}")
                return content, title
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    # Try to find with number prefix (e.g., "Coding-for-Problem-Solving" -> "04-Coding-for-Problem-Solving")
    # Build path by matching each segment with possible numbered prefixes
    base = Path(CONTENT_BASE_PATH)
    current_path = base

    for i, segment in enumerate(segments):
        # Try exact match first
        exact_path = current_path / segment
        if exact_path.exists():
            current_path = exact_path
            continue

        # Try with number prefix pattern (XX-segment)
        pattern = f"[0-9][0-9]-{segment}"
        matches = list(current_path.glob(pattern))
        if matches:
            current_path = matches[0]
            print(f"Matched segment '{segment}' -> '{matches[0].name}'")
            continue

        # Try partial match
        pattern = f"*{segment}*"
        matches = [m for m in current_path.glob(pattern) if m.is_dir() or m.suffix in ['.md', '.mdx']]
        if matches:
            current_path = matches[0]
            print(f"Partial match '{segment}' -> '{matches[0].name}'")
            continue

        # No match found for this segment
        print(f"No match for segment: {segment}")
        break

    # Check if we found a valid path
    final_candidates = [
        current_path if current_path.suffix in ['.md', '.mdx'] else None,
        current_path / "README.md",
        current_path / "index.md",
        Path(str(current_path) + ".md"),
    ]

    for candidate in final_candidates:
        if candidate and candidate.exists() and candidate.is_file():
            try:
                content = candidate.read_text(encoding="utf-8")
                title = extract_title(content, clean_path)
                print(f"Found: {candidate} -> {title} ({len(content)} chars)")
                return content, title
            except Exception as e:
                print(f"Error reading {candidate}: {e}")

    print(f"No content found for: {clean_path}")
    return "", f"Page: {clean_path}"


def extract_title(content: str, fallback: str) -> str:
    """Extract title from markdown content."""
    lines = content.split("\n")
    for line in lines:
        # Check frontmatter title
        if line.startswith("title:"):
            return line.replace("title:", "").strip().strip('"').strip("'")
        # Check first heading
        if line.startswith("# "):
            return line.replace("# ", "").strip()
    return fallback.split("/")[-1].replace("-", " ").title()


def search_book_content(query: str, current_path: str) -> str:
    """
    Search across book content for relevant information.
    For Ask mode - searches beyond current page.

    Returns concatenated relevant content with source attribution.
    """
    results = []
    search_terms = query.lower().split()

    # Search all markdown files
    pattern = str(Path(CONTENT_BASE_PATH) / "**" / "*.md")
    for file_path in glob.glob(pattern, recursive=True):
        try:
            content = Path(file_path).read_text(encoding="utf-8")
            content_lower = content.lower()

            # Simple relevance scoring
            score = sum(1 for term in search_terms if term in content_lower)

            if score > 0:
                # Extract relative path for attribution
                rel_path = Path(file_path).relative_to(CONTENT_BASE_PATH)
                title = extract_title(content, str(rel_path))
                results.append({
                    "score": score,
                    "title": title,
                    "path": str(rel_path),
                    "content": content[:3000]  # Limit content size
                })
        except Exception:
            continue

    # Sort by relevance and take top 3
    results.sort(key=lambda x: x["score"], reverse=True)
    top_results = results[:3]

    if not top_results:
        return ""

    # Format for agent context
    formatted = []
    for r in top_results:
        formatted.append(f"--- SOURCE: {r['title']} ({r['path']}) ---\n{r['content']}\n")

    return "\n".join(formatted)


# =============================================================================
# Agent Prompts (Book-Grounded)
# =============================================================================

def get_teach_prompt(page_title: str, page_content: str) -> str:
    """Generate Teach mode prompt - Socratic method with clickable questions."""

    return f"""You are a FRIENDLY TUTOR teaching from the AgentFactory book using the Socratic method.

PAGE: {page_title}
---
{page_content}
---

## THE TEACHING LOOP (Follow this EXACTLY):

1. EXPLAIN one concept (2-3 sentences, clear and simple)
2. ASK ONE checking question (MUST use the exact format below)
3. WAIT for response
4. Acknowledge + EXPLAIN next concept
5. ASK checking question
6. REPEAT

## FIRST MESSAGE (When conversation starts or user says "show suggestions", "teach me", etc.):

Welcome to **{page_title}**! Let's learn this together.

**[First Key Concept]**: [2-3 sentence clear explanation of the main idea from the page]

🤔 **Quick check:** [One simple question to verify they understood]

## AFTER USER RESPONDS:

1. Validate their answer (1 sentence - "Exactly!" or "Good thinking, and also...")
2. EXPLAIN the next concept (2-3 sentences)
3. ASK a checking question using the format below

## CRITICAL: QUESTION FORMAT (MUST follow exactly):

🤔 **Quick check:** [Your question here]

The 🤔 emoji and **Quick check:** text MUST be on the same line, followed by the question.

Example:
🤔 **Quick check:** What makes General Agents different from traditional coding tools?

## RULES:

- ALWAYS explain FIRST (2-3 sentences) using content from the page
- ALWAYS end with ONE question using the 🤔 **Quick check:** format
- Keep explanations clear and jargon-free
- Use bold for key terms
- Be warm and encouraging
- Stay focused on the page content

Mode: TEACH (Explain -> Check -> Explain -> Check)"""


def get_ask_prompt(page_title: str, book_content: str) -> str:
    """Generate Ask mode prompt - direct answers with initial suggestions."""
    return f"""You are a SEARCH ENGINE for the AgentFactory book. Give INSTANT, DIRECT answers.

PAGE: {page_title}
---
{book_content}
---

## YOUR ROLE: INSTANT ANSWERS (Like Google Search)

You answer questions directly. No teaching. No guiding.

## WHEN USER SAYS "show suggestions" OR SIMILAR:

Provide 3 suggested questions based on the page content using this EXACT format:

Here are some questions I can answer about **{page_title}**:

❓ **What would you like to know?**
1. [First interesting question based on page content]
2. [Second question about a key concept on the page]
3. [Third question about practical application]

Just click one or type your own question!

## WHEN USER ASKS A REAL QUESTION:

Give a direct answer in 1-3 sentences using the page content.

Examples:
- "What is X?" → One sentence answer
- "How to X?" → 3-5 bullet points
- "List X" → Just the list

## RULES:

- NO "Great question!"
- NO explanations beyond what's asked
- NO follow-up questions
- NO teaching after answering
- Just answer and STOP

Mode: ASK (instant answers)"""


# =============================================================================
# FastAPI Application
# =============================================================================

app = FastAPI(
    title="Study Mode ChatKit Server",
    description="Book-grounded chatbot for Interactive Study Mode",
    version="2.0.0",
)

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "ok",
        "server": "chatkit",
        "version": "2.0.0",
        "contentPath": CONTENT_BASE_PATH,
        "contentExists": Path(CONTENT_BASE_PATH).exists()
    }


# =============================================================================
# Chat API
# =============================================================================

class MessageInput(BaseModel):
    role: str
    content: str

class ChatRequestBody(BaseModel):
    lessonPath: str
    userMessage: str
    conversationHistory: List[MessageInput]
    mode: str = "teach"


@app.post("/api/chat")
async def chat(request: ChatRequestBody):
    """
    Main chat endpoint.

    - Loads book content based on lessonPath
    - Creates book-grounded agent
    - Returns response from book content ONLY
    """
    start_time = time.time()

    # Load current page content
    page_content, page_title = load_lesson_content(request.lessonPath)

    if not page_content:
        return {
            "assistantMessage": f"I couldn't load the content for this page ({request.lessonPath}). Please try refreshing or navigating to a different lesson.",
            "metadata": {
                "model": "gpt-4o-mini",
                "tokensUsed": 0,
                "processingTimeMs": 0,
                "source": "error"
            }
        }

    # For Ask mode, also search related content
    if request.mode == "ask":
        # Search for relevant content across the book
        related_content = search_book_content(request.userMessage, request.lessonPath)
        # Combine current page with related content
        book_content = f"--- CURRENT PAGE: {page_title} ---\n{page_content}\n\n--- RELATED CONTENT ---\n{related_content}"
        instructions = get_ask_prompt(page_title, book_content)
    else:
        # Teach mode: focus on current page only
        instructions = get_teach_prompt(page_title, page_content)

    # Create book-grounded agent
    agent = Agent(
        name="book_grounded_tutor",
        instructions=instructions,
        model="gpt-4o-mini",
    )

    # Build conversation history
    input_items = []
    for msg in request.conversationHistory:
        input_items.append({
            "role": msg.role,
            "content": msg.content
        })
    input_items.append({
        "role": "user",
        "content": request.userMessage
    })

    try:
        # Run the agent
        result = await Runner.run(agent, input_items)

        # Extract response
        response_text = str(result.final_output) if result.final_output else ""

        processing_time = int((time.time() - start_time) * 1000)

        return {
            "assistantMessage": response_text,
            "metadata": {
                "model": agent.model,
                "tokensUsed": result.usage.total_tokens if hasattr(result, 'usage') and result.usage else 0,
                "processingTimeMs": processing_time,
                "source": page_title
            }
        }
    except Exception as e:
        return {
            "error": {
                "code": "AGENT_ERROR",
                "message": str(e)
            }
        }


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))

    print(f"""
=================================================================
         Study Mode ChatKit Server v2.0
         BOOK-GROUNDED (No general LLM knowledge)
=================================================================
  URL:      http://localhost:{port}
  Chat:     http://localhost:{port}/api/chat
  Health:   http://localhost:{port}/health
  Content:  {CONTENT_BASE_PATH}
=================================================================
    """)

    uvicorn.run(app, host="0.0.0.0", port=port)
