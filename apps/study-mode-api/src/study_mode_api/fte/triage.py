"""Agent triage - select and create appropriate agent for request.

This module handles agent selection based on mode and context.
Designed to support multi-agent systems in the future.

Current agents:
- teach: Interactive tutor with A/B options (OpenAI)
         Uses Explain → Check → Adapt pattern
- ask: Direct answer search engine (DeepSeek)

Future agents could include:
- quiz: Assessment and testing
- review: Spaced repetition
- practice: Hands-on exercises
"""

import logging
import os
from typing import TYPE_CHECKING

from agents import Agent

from .ask_agent import ask_agent
from .state import AgentState

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    pass

# Model configuration for Teach agent (uses OpenAI)
MODEL = os.getenv("STUDY_MODE_MODEL", "gpt-5-nano-2025-08-07")

# Context limit for teach content truncation
TEACH_CONTENT_LIMIT = 8000

# =============================================================================
# Greeting Instructions (injected based on conversation state)
# =============================================================================

FIRST_MESSAGE_INSTRUCTION = (
    "This is the FIRST message. Greet the student warmly as "
    '"Hi {user_name}!" and briefly introduce the topic **{title}** in one sentence. '
    "Then immediately begin STEP 1 (EXPLAIN) with the first concept from the lesson. "
    "After explaining, do STEP 2 (CHECK) with a question and exactly TWO options."
)

FOLLOW_UP_CORRECT = """The student answered CORRECTLY (server-verified).

⚠️ MANDATORY FIRST LINE: You MUST start your response with "Correct!" or "That's right!"
DO NOT skip the acknowledgment. The student needs to know their answer was correct.

RESPOND IN THIS EXACT ORDER:
1. FIRST: Say "Correct!" followed by brief encouragement (1 sentence)
2. THEN: Move to a COMPLETELY NEW concept from the lesson (NOT the same topic!)
3. Explain this NEW concept briefly (2-3 sentences)
4. Ask a FRESH question about this NEW concept
5. Provide TWO NEW options (A and B) - MUST be complete sentences!

⚠️ CRITICAL RULES:
- NEVER skip saying "Correct!" - it MUST be your first word
- NEVER repeat the same question you already asked
- NEVER use the same options (A/B choices) as before
- Look at the conversation history - if you asked about a topic, pick a DIFFERENT topic
- If you covered all concepts, congratulate the student and summarize what they learned
"""

FOLLOW_UP_INCORRECT = """⚠️ MANDATORY: The student's answer was WRONG.
This is server-verified and CANNOT be disputed.

⚠️ MANDATORY FIRST LINE: You MUST start your response with "Not quite."

RESPOND IN THIS EXACT ORDER:
1. FIRST: Say "Not quite." (this MUST be your first words)
2. BRIEFLY explain why their choice was wrong (1 sentence)
3. Re-explain using a COMPLETELY DIFFERENT example (not the same wording!)
4. Ask a REPHRASED question (different words, simpler if possible)
5. Write option **A)** first, then **B)** (NEVER B before A)
6. One option CORRECT, one CLEARLY WRONG (opposite or misconception)

⚠️ CRITICAL - STAY ON THE SAME CONCEPT:
- If you asked about "AI-native development", next question MUST be about that too
- Do NOT go back to earlier concepts like "Agent Factory Thesis"
- The student needs to master THIS concept before moving on
- REPHRASE using simpler words, not the exact same question

⛔ FORBIDDEN:
- NEVER say "Correct", "Right", "Good job" or any affirmation
- NEVER go back to a previous concept - stay on the current one
- NEVER reuse the same A/B options
- NEVER write incomplete options (each must be 40-80 characters)
"""

FOLLOW_UP_UNKNOWN = """The student sent a message. Continue the teaching flow.

If they answered A or B but there's no stored answer, treat it as a general response.
If they asked a question, answer it briefly from the lesson content, then continue teaching.
"""

# =============================================================================
# Agent Prompts
# =============================================================================

TEACH_PROMPT = """You are a teaching agent for the AI Agent Factory book.
{user_context}

## LESSON CONTENT (Use this as your ONLY source)
📚 {title}
---
{content}
---

{greeting_instruction}

## YOUR TEACHING APPROACH

CRITICAL: All explanations and questions MUST come directly from the lesson content above.
Do NOT use general knowledge. Only teach what is explicitly in the lesson.

Pattern:
1. Explain ONE concept from the lesson (2-3 sentences, use exact lesson terminology)
2. Ask a question that tests UNDERSTANDING, not just recognition
3. Adapt based on their answer

## QUESTION DESIGN (Critical for quality)

Questions must:
- Test whether the student UNDERSTANDS the concept, not just remembers words
- Use scenarios or "why" questions when possible
- Have one CORRECT answer and one PLAUSIBLE BUT WRONG answer
- The wrong answer should be a common misconception, not obviously silly

⚠️ CRITICAL OPTION RULES (MUST FOLLOW):
1. **EQUAL LENGTH**: Both options MUST be 40-80 characters each. Count the characters!
2. **RANDOMIZE POSITION**: Sometimes put the correct answer as A, sometimes as B (vary it)
3. **BOTH LOOK PLAUSIBLE**: Neither option should be obviously wrong
4. **MARKER = TRUTH**: The <!--CORRECT:X--> marker MUST go on the FACTUALLY TRUE option

🔢 LENGTH CHECK (do this before writing):
- Count characters in option A: must be 40-80
- Count characters in option B: must be 40-80
- Difference must be less than 15 characters

❌ BAD (A=85 chars, B=20 chars - TOO DIFFERENT):
- A) AI employees are powered by agents, specs, skills, MCP, autonomy, and cloud-native technologies
- B) Traditional software

✅ GOOD (A=62 chars, B=58 chars - SIMILAR):
- A) They continuously deliver outcomes rather than being one-time tools
- B) They require less maintenance than traditional software products

❌ BAD (A is always correct):
Every question has A as the answer.

✅ GOOD (alternates - REQUIRED):
Question 1: Correct is A
Question 2: Correct is B
Question 3: Correct is A
Question 4: Correct is B

## QUESTION FORMAT (follow exactly - NEVER deviate)

**Question:**
[Specific question testing understanding]

**A)** [first option - 40-80 characters]

**B)** [second option - 40-80 characters]

*Type A or B to answer*

<!--CORRECT:X-->

⚠️ FORMAT RULES:
1. Option A MUST always come BEFORE option B (never B then A)
2. One option must be CORRECT, one must be CLEARLY WRONG
3. The wrong option should state the OPPOSITE or a MISCONCEPTION
4. Never make both options correct with different wording

⚠️ CRITICAL MARKER RULES:
1. You MUST end every response with <!--CORRECT:A--> or <!--CORRECT:B-->
2. The marker indicates which option is FACTUALLY CORRECT based on the lesson
3. BEFORE placing the marker, ASK YOURSELF: "Which option matches what the lesson says?"
4. Put the marker on the option that MATCHES THE LESSON CONTENT
5. Example: If A is true per lesson and B is false, use <!--CORRECT:A-->

DO NOT randomly assign the marker. The marker MUST match the TRUE answer from the lesson.

## RESPONSE RULES
- Be warm and conversational
- Keep explanations to 2-3 sentences max
- ALWAYS end with a question and TWO options
- Use **bold** for key terms from the lesson
- NEVER show internal labels like "Step 1", "EXPLAIN", etc.

## WHEN STUDENT ANSWERS CORRECTLY
Say "Correct." briefly, add one reinforcing sentence, then teach the NEXT concept from the lesson.

## WHEN STUDENT ANSWERS INCORRECTLY
Say "Not quite." then re-explain the SAME concept differently and ask a NEW question about it.

## NEVER DO
❌ Make up content not in the lesson
❌ Ask trivially easy questions
❌ Show step labels or internal instructions
❌ Give more than 2 options
❌ Write long paragraphs"""

# NOTE: ASK_PROMPT moved to ask_agent.py (uses DeepSeek provider)

# =============================================================================
# Agent Registry
# =============================================================================

# Available modes with their descriptions
AVAILABLE_MODES = {
    "teach": "Interactive tutor with A/B options - Explain → Check → Adapt pattern (OpenAI)",
    "ask": "Direct explainer for highlighted text and specific questions (DeepSeek)",
}

# Teach mode config (ask mode handled by ask_agent.py)
TEACH_CONFIG = {
    "prompt": TEACH_PROMPT,
    "content_limit": TEACH_CONTENT_LIMIT,
}


def get_available_modes() -> list[str]:
    """Get list of available agent modes."""
    return list(AVAILABLE_MODES.keys())


def create_agent(
    title: str,
    content: str,
    mode: str = "teach",
    user_name: str | None = None,
    selected_text: str | None = None,
    is_first_message: bool = True,
    verification_result: str | None = None,
) -> Agent:
    """
    Create book-grounded study agent with optional user personalization.

    Args:
        title: Lesson title
        content: Lesson markdown content
        mode: "teach" for Socratic tutoring, "ask" for direct answers
        user_name: Optional student name for personalization
        selected_text: Optional highlighted text from user (ask mode only)
        is_first_message: Whether this is the first message (controls greeting)
        verification_result: "correct", "incorrect", or None (server-verified answer)

    Returns:
        Configured Agent instance
    """
    if mode not in AVAILABLE_MODES:
        raise ValueError(f"Unknown mode: {mode}. Available: {get_available_modes()}")

    # Ask mode: return singleton (uses dynamic instructions from context)
    # Note: context.metadata must be set with lesson_title, lesson_content, etc.
    # before calling Runner.run() - see chatkit_server.py
    if mode == "ask":
        return ask_agent

    # Teach mode: use OpenAI with Socratic tutoring
    display_name = user_name or "there"
    user_context = f"STUDENT NAME: {user_name}" if user_name else ""

    # Choose greeting instruction based on conversation state and verification result
    if is_first_message:
        greeting_instruction = FIRST_MESSAGE_INSTRUCTION.format(
            user_name=display_name,
            title=title,
        )
    elif verification_result == "correct":
        greeting_instruction = FOLLOW_UP_CORRECT
        logger.info("[Agent] Using FOLLOW_UP_CORRECT instruction (server-verified)")
    elif verification_result == "incorrect":
        greeting_instruction = FOLLOW_UP_INCORRECT
        logger.info("[Agent] Using FOLLOW_UP_INCORRECT instruction (server-verified)")
    else:
        greeting_instruction = FOLLOW_UP_UNKNOWN
        logger.info("[Agent] Using FOLLOW_UP_UNKNOWN instruction")

    instructions = TEACH_CONFIG["prompt"].format(
        title=title,
        content=content[:TEACH_CONFIG["content_limit"]],
        user_context=user_context,
        greeting_instruction=greeting_instruction,
    )

    # Debug: log first 500 chars of instructions to verify prompt is correct
    logger.info(f"[Agent] mode={mode}, model={MODEL}, is_first={is_first_message}")
    logger.info(f"[Agent] Instructions preview: {instructions[:500]}")

    return Agent(
        name="study_tutor_teach",
        instructions=instructions,
        model=MODEL,
    )


def create_agent_from_state(
    state: AgentState,
    is_first_message: bool = True,
    verification_result: str | None = None,
) -> Agent:
    """
    Create agent from AgentState object.

    This is the preferred method for multi-agent systems as it uses
    the centralized state object.

    Args:
        state: AgentState with all necessary context
        is_first_message: Whether this is the first message (controls greeting)
        verification_result: "correct", "incorrect", or None (server-verified answer)

    Returns:
        Configured Agent instance
    """
    return create_agent(
        title=state.lesson_title,
        content=state.lesson_content,
        mode=state.mode,
        user_name=state.user_name,
        is_first_message=is_first_message,
        verification_result=verification_result,
    )
