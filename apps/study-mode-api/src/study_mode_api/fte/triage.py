"""Agent triage - select and create appropriate agent for request.

This module handles agent selection based on mode and context.
Designed to support multi-agent systems in the future.

Current agents:
- teach: Interactive tutor with A/B options (OpenAI)
         Uses Explain → Check → Adapt pattern
         Now supports CHUNKED mode for token efficiency
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
    from ..services.lesson_chunker import LessonChunk
    from ..services.session_state import TeachSessionState

# Model configuration for Teach agent (uses OpenAI Responses API)
MODEL = os.getenv("STUDY_MODE_MODEL", "gpt-5-mini")

# Context limit for teach content truncation (legacy mode)
TEACH_CONTENT_LIMIT = 4000  # Reduced from 8000 for faster responses

# Chunk mode uses ~500 chars per chunk instead of 8000

# =============================================================================
# Greeting Instructions (injected based on conversation state)
# =============================================================================

FIRST_MESSAGE_INSTRUCTION = (
    "This is the FIRST message. Greet the student warmly as "
    '"Hi {user_name}!" and briefly introduce the topic **{title}** in one sentence. '
    "Then immediately begin STEP 1 (EXPLAIN) with the first concept from the lesson. "
    "After explaining, do STEP 2 (CHECK) with a question and exactly TWO options."
)

FOLLOW_UP_CORRECT = """
##########################################################
# THE STUDENT ANSWERED CORRECTLY!                        #
# SAY "Correct!" THEN MOVE TO A COMPLETELY NEW TOPIC     #
##########################################################

YOUR RESPONSE:
1. Say "Correct!" + brief praise (1 sentence max)
2. Say "Now let's explore [NEW TOPIC]:" - pick a DIFFERENT concept from the lesson
3. Explain the NEW concept briefly (2-3 sentences)
4. Ask a question about THIS NEW concept with A/B options
5. END WITH <!--CORRECT:A--> or <!--CORRECT:B--> marker (REQUIRED!)

🚨 CRITICAL - YOU MUST CHANGE TOPICS:
- NEVER ask another question about the same concept you just covered
- Check conversation history - don't repeat ANY topic you already taught
- If the lesson has concepts A, B, C, D - progress through them: A → B → C → D

⛔ WRONG (repeating topic):
Q1: About A → Q2: About A again ❌

✅ RIGHT (new topic):
Q1: About A → Q2: About B ✓

⚠️ MANDATORY: End response with <!--CORRECT:A--> or <!--CORRECT:B-->
"""

FOLLOW_UP_INCORRECT = """
##########################################################
# CRITICAL: THE STUDENT'S ANSWER WAS WRONG               #
# YOU MUST SAY "Not quite." - NEVER SAY "Correct"        #
##########################################################

⛔⛔⛔ FORBIDDEN WORDS - NEVER USE THESE: ⛔⛔⛔
- "Correct"
- "Right"
- "Good job"
- "Great"
- "Well done"
- "That's right"

✅ YOUR FIRST WORDS MUST BE: "Not quite."

THEN TEACH:
1. Explain why their choice was wrong (be specific)
2. Teach the concept with a real example (2-3 sentences)
3. Ask a simpler question with NEW A/B options (different words)
4. END WITH <!--CORRECT:A--> or <!--CORRECT:B--> marker (REQUIRED!)

Example response:
"Not quite. Option B says [wrong thing], but the lesson teaches [correct thing].
Think of it like [concrete example]. [Ask new question with new options]"

⚠️ MANDATORY: End response with <!--CORRECT:A--> or <!--CORRECT:B-->
"""

FOLLOW_UP_UNKNOWN = """The student sent a message. Continue the teaching flow.

If they answered A or B but there's no stored answer, treat it as a general response.
If they asked a question, answer it briefly from the lesson content, then continue teaching.

After responding, ask a NEW question with A/B options.
⚠️ MANDATORY: End response with <!--CORRECT:A--> or <!--CORRECT:B-->
"""

# =============================================================================
# Agent Prompts
# =============================================================================

TEACH_PROMPT = """You are a teaching agent for the AI Agent Factory book.
{user_context}

{greeting_instruction}

## LESSON CONTENT (Use this as your ONLY source)
📚 {title}
---
{content}
---

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


# =============================================================================
# CHUNKED TEACHING MODE - Script v2 (Token-efficient)
# =============================================================================
# Based on specs/teach-me-scripts/teach-me-scripts-v2.md
# Global Rules:
# - Max 3 attempts per chunk, then reveal answer and move on
# - Every question MUST end with <!--CORRECT:A--> or <!--CORRECT:B-->
# - Focus only on current chunk content, ignore conversation history for topics
# =============================================================================

MAX_ATTEMPTS = 3  # After 3 wrong answers, reveal and move on

CHUNKED_TEACH_PROMPT = """You are a teaching agent for the AI Agent Factory book.
{user_context}

## CURRENT CONCEPT (focus ONLY on this)
**{chunk_title}**
---
{chunk_content}
---

## PROGRESS
{progress_context}

## YOUR TASK
{task_instruction}

## QUESTION CRITERIA (MUST follow)
✅ Ask "why", "how", or "what enables/causes"
✅ Both options must be plausible (similar language complexity)
✅ Wrong option = believable misconception (NOT obviously silly)
✅ Answer requires reading content (not guessable from general knowledge)

❌ FORBIDDEN question types:
- "Is X related or unrelated?"
- "Does X exist or not?"
- Options containing "not", "never", "unrelated"
- Yes/No reformulations

## QUESTION FORMAT (follow exactly)

**Question:**
[Question about THIS concept - use "why", "how", or "what"]

**A)** [first option - 40-80 characters, plausible]

**B)** [second option - 40-80 characters, plausible]

*Type A or B to answer*

<!--CORRECT:X-->

## RULES
- Focus ONLY on the current concept above (ignore all previous topics)
- Keep explanations to 2-3 sentences
- ALWAYS end with a question and TWO options (A/B)
- The <!--CORRECT:X--> marker indicates which option is correct
- BOTH options must look reasonable; neither should be obviously wrong
- Be warm and conversational
- Use **bold** for key terms"""

# =============================================================================
# Script 1: START_TEACHING
# =============================================================================
CHUNKED_FIRST_MESSAGE = """This is the FIRST message.

YOUR RESPONSE (follow exactly):
1. Greet the student: "Hi {user_name}!"
2. Topic intro: "Today we'll explore {chunk_title}."
3. Explain the KEY concept in 2-3 sentences (what it is, why it matters)
4. Ask a question that tests UNDERSTANDING (not recognition)
5. Provide A/B options - BOTH must be plausible
6. Say "Type A or B to answer"
7. End with <!--CORRECT:A--> or <!--CORRECT:B-->

Remember: The wrong option should be a believable misconception, not obviously silly."""

# =============================================================================
# Script 2: CORRECT_ANSWER (more chunks remaining)
# =============================================================================
CHUNKED_CORRECT_ANSWER = """
##########################################################
# THE STUDENT ANSWERED CORRECTLY!                        #
# YOUR FIRST WORD MUST BE "Correct!"                     #
##########################################################

YOUR RESPONSE (follow exactly):
1. Say "Correct!" + brief praise (1 sentence max)
2. Transition: "Now let's learn about {next_chunk_title}:"
3. Explain the NEW concept in 2-3 sentences
4. Ask a question about THIS NEW concept with A/B options
5. Say "Type A or B to answer"
6. End with <!--CORRECT:A--> or <!--CORRECT:B-->

⚠️ MANDATORY: Your response MUST start with "Correct!"

❌ FORBIDDEN:
- Re-explaining the previous concept
- More than 1 sentence of praise"""

# =============================================================================
# Script 2B: CORRECT_ANSWER (last chunk - lesson complete)
# =============================================================================
CHUNKED_CORRECT_LAST_CHUNK = """
##########################################################
# THE STUDENT ANSWERED CORRECTLY!                        #
# THIS WAS THE LAST CHUNK - LESSON COMPLETE!             #
##########################################################

YOUR RESPONSE (follow exactly):
1. Say "Correct!"
2. Say "You've completed this lesson!"
3. Summary with 2-3 bullet points of key concepts learned
4. Say "Continue to the next lesson when ready."

⚠️ MANDATORY:
- Start with "Correct!"
- NO question at the end
- NO <!--CORRECT:X--> marker"""

# =============================================================================
# Script 3: INCORRECT_ANSWER (attempts < MAX)
# =============================================================================
CHUNKED_INCORRECT_ANSWER = """
##########################################################
# CRITICAL: THE STUDENT'S ANSWER WAS WRONG               #
# YOUR FIRST WORDS MUST BE "Not quite."                  #
# NEVER SAY "Correct" - IT WAS WRONG!                   #
##########################################################

⛔ FORBIDDEN: "Correct", "Right", "Good job", "Great"
✅ YOUR FIRST WORDS: "Not quite."

⚠️ IMPORTANT: Focus ONLY on the CURRENT CONCEPT above ({chunk_title}).

YOUR RESPONSE:
1. Say "Not quite."
2. Briefly explain why their answer was wrong (1 sentence)
3. Ask a COMPLETELY DIFFERENT question about the SAME concept
4. Provide NEW A/B options
5. Say "Type A or B to answer"
6. End with <!--CORRECT:A--> or <!--CORRECT:B-->

🚨 CRITICAL - YOUR NEW QUESTION MUST BE DIFFERENT:
❌ WRONG: Rephrasing the same question with different words
   - Original: "What role do specs play?"
   - Bad retry: "In the model, what is the role of specs?" (SAME QUESTION!)

✅ RIGHT: Ask about a DIFFERENT ASPECT of the concept
   - Original: "What role do specs play?"
   - Good retry: "How do specs work together with agents?" (DIFFERENT ANGLE!)
   - Good retry: "What would be missing without specs?" (DIFFERENT ANGLE!)
   - Good retry: "Why are specs needed in the factory model?" (ASKS WHY, NOT WHAT)

SIMPLIFICATION BY ATTEMPT:
- Attempt 2: Ask about a different aspect, add a hint in the question
- Attempt 3: Ask the most basic question about this concept

This is attempt {attempt_count} of {max_attempts}.

❌ FORBIDDEN:
- Asking the same question with rephrased words
- Using the same sentence structure as before
- Recycling option text from the previous question"""

# =============================================================================
# Script 3B: INCORRECT_ANSWER (max attempts reached - reveal and move on)
# =============================================================================
CHUNKED_MAX_ATTEMPTS_REACHED = """
##########################################################
# MAXIMUM ATTEMPTS REACHED ({max_attempts})              #
# REVEAL THE ANSWER AND MOVE TO NEXT CONCEPT             #
##########################################################

YOUR RESPONSE (follow exactly):
1. Say "Let's move on."
2. Say "The answer was {correct_answer} because [brief explanation]."
3. Transition: "Now let's learn about {next_chunk_title}:"
4. Explain the NEW concept in 2-3 sentences
5. Ask a question about THIS NEW concept with A/B options
6. Say "Type A or B to answer"
7. End with <!--CORRECT:A--> or <!--CORRECT:B-->

Be encouraging, not discouraging. The student is learning!"""

# =============================================================================
# Script 4: OFF_TOPIC_RESPONSE
# =============================================================================
CHUNKED_OFF_TOPIC = """⚠️ The student's message was NOT a valid answer (A or B).

YOUR RESPONSE (follow exactly):
1. Say: "Please answer with A or B."
2. Say: "If you have other questions, use the 'Ask Me' option instead."
3. Repeat the SAME question you just asked (with A/B options)
4. End with <!--CORRECT:A--> or <!--CORRECT:B--> (same answer as before)

Keep it brief. Do NOT answer their off-topic question."""

# =============================================================================
# Script 4B: LONG_MESSAGE (>200 chars)
# =============================================================================
CHUNKED_LONG_MESSAGE = """⚠️ The student sent a long message (probably a discussion).

YOUR RESPONSE (follow exactly):
1. Say: "Thanks for sharing! For this exercise, just type A or B."
2. Say: "Use the 'Ask Me' option for detailed discussions."
3. Repeat the SAME question (with A/B options)
4. End with <!--CORRECT:A--> or <!--CORRECT:B--> (same answer as before)

Keep it brief."""

# =============================================================================
# Script 6: HINT_REQUEST
# =============================================================================
CHUNKED_HINT = """The student asked for a hint.

YOUR RESPONSE (follow exactly):
1. Say: "Here's a hint:"
2. Provide contextual clue WITHOUT revealing the answer
3. Rephrase the concept differently than your original explanation
4. Say: "Now try again - A or B?"
5. End with <!--CORRECT:A--> or <!--CORRECT:B--> (same answer as before)

HINT RULES:
✅ Relate hint to {chunk_title} topic only
✅ Use different words than original explanation
✅ Point toward correct answer indirectly
❌ Don't say "The answer is A/B"
❌ Don't eliminate one option explicitly"""

# =============================================================================
# Script 6A: OPTION_CONFUSION ("both wrong", "neither", etc.)
# =============================================================================
CHUNKED_OPTION_CONFUSION = """The student thinks both options are wrong.

YOUR RESPONSE (follow exactly):
1. Say: "I understand the options might seem tricky."
2. Provide a hint: "[contextual clue from the lesson]"
3. Say: "One of these options does match the lesson content."
4. Say: "Try again - A or B?"
5. End with <!--CORRECT:A--> or <!--CORRECT:B--> (same answer as before)

RULES:
✅ Provide helpful hint
❌ Don't admit options are wrong
❌ Don't generate new question"""

# =============================================================================
# Script 7: SKIP_REQUEST
# =============================================================================
CHUNKED_SKIP = """The student wants to skip this question.

YOUR RESPONSE (follow exactly):
1. Say: "No problem, let's move forward."
2. Say: "The answer was {correct_answer}: [brief explanation]"
3. Transition: "Now let's learn about {next_chunk_title}:"
4. Explain the NEW concept in 2-3 sentences
5. Ask a question about THIS NEW concept with A/B options
6. Say "Type A or B to answer"
7. End with <!--CORRECT:A--> or <!--CORRECT:B-->

RULES:
✅ Always reveal correct answer when skipping
✅ No judgment or negative feedback"""

# =============================================================================
# Script 8: LESSON_COMPLETE
# =============================================================================
CHUNKED_LESSON_COMPLETE = """The student has completed ALL concepts in this lesson!

YOUR RESPONSE (follow exactly):
1. Say: "Congratulations, {user_name}!"
2. Say: "You've completed: {lesson_title}"
3. Say: "Key takeaways:"
   - Bullet 1: Main concept
   - Bullet 2: Supporting concept
   - Bullet 3: Practical application
4. Say: "Ready for the next lesson? Check the sidebar to continue."

RULES:
✅ Summarize from ALL chunks taught
✅ Keep bullets concise (1 line each)
❌ No new questions
❌ No <!--CORRECT:X--> marker"""

# =============================================================================
# Script 9: SESSION_RESUME
# =============================================================================
CHUNKED_SESSION_RESUME = """The student is resuming a previous session.

YOUR RESPONSE (follow exactly):
1. Say: "Welcome back! Let's continue where you left off."
2. Say: "We were learning about {chunk_title}..."
3. Explain the concept briefly (2-3 sentences)
4. Ask a FRESH question (don't assume they remember the old one)
5. Provide A/B options
6. Say "Type A or B to answer"
7. End with <!--CORRECT:A--> or <!--CORRECT:B-->"""


def create_chunked_agent(
    chunk: "LessonChunk",
    session_state: "TeachSessionState",
    next_chunk: "LessonChunk | None" = None,
    user_name: str | None = None,
    is_first_message: bool = True,
    verification_result: str | None = None,
    special_request: str | None = None,
    correct_answer: str | None = None,
    is_session_resume: bool = False,
    lesson_title: str | None = None,
) -> Agent:
    """
    Create agent for chunked teaching mode (token-efficient).

    Based on teach-me-scripts-v2.md - handles all script scenarios.

    Args:
        chunk: Current chunk to teach
        session_state: Session state with progress info
        next_chunk: Next chunk (for correct answer transitions)
        user_name: Optional student name
        is_first_message: Whether this is the first message
        verification_result: "correct", "incorrect", or None
        special_request: "hint", "skip", "option_confusion", or None
        correct_answer: "A" or "B" (for skip/max_attempts scenarios)
        is_session_resume: Whether this is a session resume
        lesson_title: Full lesson title (for completion message)

    Returns:
        Configured Agent instance
    """
    display_name = user_name or "there"
    user_context = f"STUDENT NAME: {user_name}" if user_name else ""

    # Build progress context
    progress_context = (
        f"Concept {session_state['concept_index'] + 1} of {session_state['total_chunks']}"
    )
    attempt_count = session_state["attempt_count"]
    if attempt_count > 0:
        progress_context += f" (attempt {attempt_count + 1} of {MAX_ATTEMPTS})"

    # Determine task instruction based on state (Script v2 logic)
    task_instruction = ""

    # Script 8: LESSON_COMPLETE
    if session_state["status"] == "complete":
        task_instruction = CHUNKED_LESSON_COMPLETE.format(
            user_name=display_name,
            lesson_title=lesson_title or "this lesson",
        )

    # Script 9: SESSION_RESUME
    elif is_session_resume:
        task_instruction = CHUNKED_SESSION_RESUME.format(
            chunk_title=chunk["title"],
        )

    # Script 1: START_TEACHING (first message)
    elif is_first_message:
        task_instruction = CHUNKED_FIRST_MESSAGE.format(
            user_name=display_name,
            chunk_title=chunk["title"],
        )

    # Script 6: HINT_REQUEST
    elif special_request == "hint":
        task_instruction = CHUNKED_HINT.format(
            chunk_title=chunk["title"],
        )

    # Script 6A: OPTION_CONFUSION
    elif special_request == "option_confusion":
        task_instruction = CHUNKED_OPTION_CONFUSION

    # Script 7: SKIP_REQUEST
    elif special_request == "skip":
        next_title = next_chunk["title"] if next_chunk else "the next concept"
        task_instruction = CHUNKED_SKIP.format(
            correct_answer=correct_answer or "the correct option",
            next_chunk_title=next_title,
        )

    # Script 2: CORRECT_ANSWER
    elif verification_result == "correct":
        # Check if this was the last chunk
        is_last_chunk = session_state["concept_index"] >= session_state["total_chunks"] - 1

        if is_last_chunk:
            # Script 2B: Last chunk completed
            task_instruction = CHUNKED_CORRECT_LAST_CHUNK
        else:
            # Script 2A: More chunks remaining
            # chunk is already the one we advanced to (from chatkit_server.py)
            task_instruction = CHUNKED_CORRECT_ANSWER.format(
                next_chunk_title=chunk["title"],
            )

    # Script 3: INCORRECT_ANSWER
    elif verification_result == "incorrect":
        # Check if max attempts reached
        if attempt_count >= MAX_ATTEMPTS:
            # Script 3B: Max attempts - reveal and move on
            next_title = next_chunk["title"] if next_chunk else "the next concept"
            task_instruction = CHUNKED_MAX_ATTEMPTS_REACHED.format(
                max_attempts=MAX_ATTEMPTS,
                correct_answer=correct_answer or "the correct option",
                next_chunk_title=next_title,
            )
        else:
            # Script 3A: More attempts remaining
            task_instruction = CHUNKED_INCORRECT_ANSWER.format(
                attempt_count=attempt_count + 1,
                max_attempts=MAX_ATTEMPTS,
                chunk_title=chunk["title"],
            )

    # Script 4: OFF_TOPIC (default)
    else:
        user_message_len = len(session_state.get("last_student_answer", "") or "")
        if user_message_len > 200:
            # Script 4B: Long message
            task_instruction = CHUNKED_LONG_MESSAGE
        else:
            # Script 4A: Default off-topic
            task_instruction = CHUNKED_OFF_TOPIC

    # Build the prompt
    instructions = CHUNKED_TEACH_PROMPT.format(
        user_context=user_context,
        chunk_title=chunk["title"],
        chunk_content=chunk["content"],
        progress_context=progress_context,
        task_instruction=task_instruction,
    )

    logger.info(
        f"[Agent] CHUNKED mode: chunk={chunk['index']}, "
        f"verification={verification_result}, special={special_request}, "
        f"first={is_first_message}, resume={is_session_resume}, "
        f"attempts={attempt_count}/{MAX_ATTEMPTS}"
    )
    logger.info(f"[Agent] Prompt size: {len(instructions)} chars")

    return Agent(
        name="study_tutor_chunked",
        instructions=instructions,
        model=MODEL,
    )



