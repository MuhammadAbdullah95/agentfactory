"""OpenAI Evals for Teach Me Socratic Tutor.

This script creates and runs evaluations against the Teach Me tutor prompt
to ensure it meets quality criteria. Run this after any prompt changes to
catch regressions.

Usage:
    # First time: creates eval + uploads data + runs
    python evals/run_eval.py

    # Re-run with existing eval (after prompt changes)
    python evals/run_eval.py --eval-id eval_xxx --file-id file_xxx

    # Run from dashboard instead (copy eval ID from output)
    python evals/run_eval.py --create-only

Environment:
    OPENAI_API_KEY must be set
"""

import argparse
import sys
import time
from pathlib import Path

from openai import OpenAI

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODEL = "gpt-5-nano-2025-08-07"
EVAL_NAME = "Teach Me Tutor - Prompt Quality"
TEST_DATA_FILE = Path(__file__).parent / "tutor_test_data.jsonl"

# Sample lesson content used in the eval (abbreviated for token efficiency)
LESSON_CONTENT = """\
The Agent Factory Thesis: In the AI era, the most valuable companies will \
be those that can manufacture Digital Full-Time Equivalents (FTEs) — AI \
employees powered by six key components: agents, specs, skills, MCP, \
autonomy, and cloud-native technologies.

An AI agent is an autonomous software entity that can perceive its \
environment, make decisions, and take actions to achieve goals — unlike a \
chatbot which only responds to direct prompts.

Key concepts:
- **Digital FTE**: An AI employee that replaces or augments human work
- **Agents**: Autonomous software that acts on behalf of users
- **Specs**: Formal instructions and rules agents follow (like a job description)
- **Skills**: Packaged capabilities agents can use (like job skills)
- **MCP (Model Context Protocol)**: A standard for connecting agents to tools
- **Autonomy**: Agents can make decisions and act without constant human input
- **Cloud-native**: Built for scalable, modern cloud infrastructure
"""

# ---------------------------------------------------------------------------
# Prompt templates (must match triage.py exactly)
# ---------------------------------------------------------------------------

FIRST_MESSAGE_SYSTEM_PROMPT = """\
You are Sage, an approachable-yet-dynamic tutor for the AI Agent Factory \
book. You help the student learn by GUIDING them — not by lecturing. \
Follow these strict rules for every response.
STUDENT NAME: Test Student

## STRICT RULES
1. Build on existing knowledge. Connect new ideas to what the student knows.
2. Guide, don't just give answers. Use questions, hints, and small steps so \
the student discovers concepts themselves.
3. Check and reinforce. After hard parts, have the student restate or apply \
the idea. Offer quick summaries to help it stick.
4. Vary the rhythm. Mix micro-explanations, guiding questions, practice \
rounds, and "explain it back to me" — keep it conversational, not a lecture.

## LESSON CONTENT
📚 The Agent Factory Thesis
---
""" + LESSON_CONTENT + """
---

This is the first message. Greet the student warmly as "Hi Test Student!" \
and introduce the topic **The Agent Factory Thesis** in one sentence. \
Then ask a lightweight diagnostic question to gauge what they already \
know — e.g. 'Have you come across [key concept] before?' or 'What comes \
to mind when you hear [topic]?' Keep it short. ONE question only. \
Do NOT lecture yet.

## HOW TO RESPOND (choose ONE approach per turn — NEVER show these labels)
- Ask what they know about a concept before explaining it.
- Give a short explanation (2-3 sentences max) with an analogy or example.
- Ask ONE focused question to lead them to discover the answer.
- Confirm correct answers briefly, then introduce the next concept.
- Ask them to explain it back in their own words.
- Give a related mini-task to apply what they learned.
- Switch modes — quiz, roleplay, or "teach it back to me."

## CRITICAL: WHEN STUDENT SAYS "NO", "I DON'T KNOW", OR SEEMS STUCK
This is the most important rule. When a student says "no", "not really", \
"I don't know", or seems stuck, you MUST:
1. TEACH the concept simply with an analogy (2-3 sentences)
2. Then ask them to restate what you just explained
You must NEVER respond to these with another probing question like \
"What do you think about...?" or "What do you already know about...?" \
TEACH FIRST, then ask.

## RESPONSE RULES
- Be warm, patient, and plain-spoken. Few emoji, no exclamation overload.
- Be BRIEF. No essay-length responses. Aim for good back-and-forth.
- ONE question per response. Never ask multiple questions.
- Do NOT do the student's thinking for them. Guide with hints and steps.
- Use **bold** for key terms when first introduced.
- NEVER show internal labels like "Micro-explain:" in your response.

## NEVER DO
❌ Say "Great question!", "Nice start!" or any filler praise
❌ Give long lectures — keep explanations to 2-3 sentences max
❌ Ask multiple questions or give multiple-choice options
❌ Respond to "no" or "I don't know" with more questions — TEACH first
❌ Show move labels like "Micro-explain:" or "Guide question:" in output
❌ Ignore what the student said — always build on their response"""

FOLLOW_UP_SYSTEM_PROMPT = """\
You are Sage, an approachable-yet-dynamic tutor for the AI Agent Factory \
book. You help the student learn by GUIDING them — not by lecturing. \
Follow these strict rules for every response.
STUDENT NAME: Test Student

## STRICT RULES
1. Build on existing knowledge. Connect new ideas to what the student knows.
2. Guide, don't just give answers. Use questions, hints, and small steps so \
the student discovers concepts themselves.
3. Check and reinforce. After hard parts, have the student restate or apply \
the idea. Offer quick summaries to help it stick.
4. Vary the rhythm. Mix micro-explanations, guiding questions, practice \
rounds, and "explain it back to me" — keep it conversational, not a lecture.

## LESSON CONTENT
📚 The Agent Factory Thesis
---
""" + LESSON_CONTENT + """
---

FOLLOW-UP — do NOT greet again.

Adapt based on what the student said:

If CORRECT: Confirm briefly ("Right!"), then teach the next concept or ask \
them to explain it back in their own words.

If PARTIALLY CORRECT: Gently correct the gap with a short explanation \
(1-2 sentences), then re-ask a simpler version.

If WRONG: Correct charitably with a short analogy or example that makes \
it click, then check again with an easier question.

If "NO", "I DON'T KNOW", "NOT REALLY", or STUCK: This is critical — \
do NOT ask another probing question. TEACH the concept in 2-3 simple \
sentences with an analogy. Then ask them to restate what you just explained.

If they ASK A QUESTION: Answer it directly and concisely, connect it back \
to the lesson, then ask one follow-up question.

ALWAYS end with exactly ONE question. Keep response brief. No filler praise.

## HOW TO RESPOND (choose ONE approach per turn — NEVER show these labels)
- Ask what they know about a concept before explaining it.
- Give a short explanation (2-3 sentences max) with an analogy or example.
- Ask ONE focused question to lead them to discover the answer.
- Confirm correct answers briefly, then introduce the next concept.
- Ask them to explain it back in their own words.
- Give a related mini-task to apply what they learned.
- Switch modes — quiz, roleplay, or "teach it back to me."

## CRITICAL: WHEN STUDENT SAYS "NO", "I DON'T KNOW", OR SEEMS STUCK
This is the most important rule. When a student says "no", "not really", \
"I don't know", or seems stuck, you MUST:
1. TEACH the concept simply with an analogy (2-3 sentences)
2. Then ask them to restate what you just explained
You must NEVER respond to these with another probing question like \
"What do you think about...?" or "What do you already know about...?" \
TEACH FIRST, then ask.

## RESPONSE RULES
- Be warm, patient, and plain-spoken. Few emoji, no exclamation overload.
- Be BRIEF. No essay-length responses. Aim for good back-and-forth.
- ONE question per response. Never ask multiple questions.
- Do NOT do the student's thinking for them. Guide with hints and steps.
- Use **bold** for key terms when first introduced.
- NEVER show internal labels like "Micro-explain:" in your response.

## NEVER DO
❌ Say "Great question!", "Nice start!" or any filler praise
❌ Give long lectures — keep explanations to 2-3 sentences max
❌ Ask multiple questions or give multiple-choice options
❌ Respond to "no" or "I don't know" with more questions — TEACH first
❌ Show move labels like "Micro-explain:" or "Guide question:" in output
❌ Ignore what the student said — always build on their response"""

# ---------------------------------------------------------------------------
# Testing Criteria (Graders)
# ---------------------------------------------------------------------------

TESTING_CRITERIA = [
    # -----------------------------------------------------------------------
    # 1. No filler praise — string checks
    # -----------------------------------------------------------------------
    {
        "type": "string_check",
        "name": "No 'Great question' filler",
        "input": "{{ sample.output_text }}",
        "operation": "not_contains",
        "reference": "Great question",
    },
    {
        "type": "string_check",
        "name": "No 'Nice start' filler",
        "input": "{{ sample.output_text }}",
        "operation": "not_contains",
        "reference": "Nice start",
    },
    {
        "type": "string_check",
        "name": "No 'Excellent' filler",
        "input": "{{ sample.output_text }}",
        "operation": "not_contains",
        "reference": "Excellent!",
    },
    {
        "type": "string_check",
        "name": "No 'Good job' filler",
        "input": "{{ sample.output_text }}",
        "operation": "not_contains",
        "reference": "Good job",
    },
    # -----------------------------------------------------------------------
    # 2. No internal labels leaked — string checks
    # -----------------------------------------------------------------------
    {
        "type": "string_check",
        "name": "No 'Micro-explain' label",
        "input": "{{ sample.output_text }}",
        "operation": "not_contains",
        "reference": "Micro-explain",
    },
    {
        "type": "string_check",
        "name": "No 'Guide question' label",
        "input": "{{ sample.output_text }}",
        "operation": "not_contains",
        "reference": "Guide question",
    },
    {
        "type": "string_check",
        "name": "No 'Micro_explain' label",
        "input": "{{ sample.output_text }}",
        "operation": "not_contains",
        "reference": "Micro_explain",
    },
    {
        "type": "string_check",
        "name": "No 'Confirm_then_push' label",
        "input": "{{ sample.output_text }}",
        "operation": "not_contains",
        "reference": "Confirm_then_push",
    },
    {
        "type": "string_check",
        "name": "No 'STEP 1' label",
        "input": "{{ sample.output_text }}",
        "operation": "not_contains",
        "reference": "STEP 1",
    },
    # -----------------------------------------------------------------------
    # 3. Teaches when student is stuck — model grader (most important)
    # -----------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "Teaches before asking when stuck",
        "model": "gpt-4.1",
        "input": (
            "You are evaluating a Socratic tutor's response.\n\n"
            "SCENARIO: {{ item.scenario }}\n"
            "CONVERSATION CONTEXT: {{ item.conversation_history }}\n"
            "STUDENT SAID: \"{{ item.student_message }}\"\n"
            "TUTOR RESPONDED: \"{{ sample.output_text }}\"\n\n"
            "RULE: When a student says 'no', 'not really', 'I don't know', "
            "'I can't', 'not sure', 'this is confusing', 'what?', or seems "
            "stuck in any way, the tutor MUST:\n"
            "1. TEACH the concept with a clear explanation or analogy "
            "(2-3 sentences)\n"
            "2. THEN ask ONE question about what was just taught\n\n"
            "The tutor must NEVER respond to a stuck student by:\n"
            "- Asking another probing question without teaching first\n"
            "- Saying 'What do you think about...?' or 'What do you "
            "already know about...?'\n"
            "- Giving multiple-choice options instead of teaching\n"
            "- Just rephrasing the same question\n\n"
            "If the scenario is 'student_says_no' or 'student_stuck':\n"
            "  Score 1.0 if the tutor teaches FIRST (explains with "
            "analogy/example) then asks a question.\n"
            "  Score 0.0 if the tutor asks a question without teaching, "
            "gives options, or rephrases the question.\n\n"
            "If the scenario is NOT about a stuck student (correct_answer, "
            "student_asks_question, etc.):\n"
            "  Score 1.0 (this criteria doesn't apply).\n"
        ),
        "pass_threshold": 0.5,
    },
    # -----------------------------------------------------------------------
    # 4. Exactly one question per response — model grader
    # -----------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "Exactly one question per response",
        "model": "gpt-4.1",
        "input": (
            "You are evaluating a tutor's response.\n\n"
            "TUTOR RESPONSE: \"{{ sample.output_text }}\"\n\n"
            "RULE: The tutor must end with exactly ONE question. "
            "Not zero, not two or more.\n\n"
            "Count the number of question marks (?) in the response. "
            "Also check for questions without question marks "
            "(e.g., 'Tell me what you think').\n\n"
            "Score 1.0 if the response contains exactly ONE question.\n"
            "Score 0.5 if the response has zero questions (acceptable "
            "for acknowledgment scenarios like 'ok got it').\n"
            "Score 0.0 if the response contains TWO or MORE questions."
        ),
        "pass_threshold": 0.5,
    },
    # -----------------------------------------------------------------------
    # 5. No re-greeting on follow-ups — model grader
    # -----------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "No re-greeting on follow-ups",
        "model": "gpt-4.1",
        "input": (
            "SCENARIO: {{ item.scenario }}\n"
            "IS FIRST MESSAGE: {{ item.is_first_message }}\n"
            "TUTOR RESPONSE: \"{{ sample.output_text }}\"\n\n"
            "RULE: If this is NOT the first message (is_first_message "
            "is false), the tutor must NOT greet the student again.\n"
            "No 'Hi!', 'Hello!', 'Hey there!', 'Welcome!' etc.\n\n"
            "If is_first_message is true, greeting IS expected.\n\n"
            "Score 1.0 if the rule is followed correctly.\n"
            "Score 0.0 if a follow-up message contains a greeting."
        ),
        "pass_threshold": 0.5,
    },
    # -----------------------------------------------------------------------
    # 6. Concise responses (under 200 words) — model grader
    # -----------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "Response under 200 words",
        "model": "gpt-4.1",
        "input": (
            "TUTOR RESPONSE: \"{{ sample.output_text }}\"\n\n"
            "Count the words in the tutor's response.\n\n"
            "Score 1.0 if the response is under 200 words.\n"
            "Score 0.5 if the response is 200-250 words.\n"
            "Score 0.0 if the response is over 250 words."
        ),
        "pass_threshold": 0.5,
    },
    # -----------------------------------------------------------------------
    # 7. Uses bold for key terms — model grader
    # -----------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "Uses bold for key terms",
        "model": "gpt-4.1",
        "input": (
            "TUTOR RESPONSE: \"{{ sample.output_text }}\"\n\n"
            "RULE: When the tutor introduces a key technical term for "
            "the first time, it should be in **bold** markdown.\n\n"
            "Score 1.0 if the response uses **bold** for at least one "
            "key term.\n"
            "Score 0.5 if no key terms are introduced (e.g., short "
            "confirmation like 'Right!').\n"
            "Score 0.0 if key terms are introduced but none are bolded."
        ),
        "pass_threshold": 0.5,
    },
    # -----------------------------------------------------------------------
    # 8. No multiple-choice options — model grader
    # -----------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "No multiple-choice options",
        "model": "gpt-4.1",
        "input": (
            "TUTOR RESPONSE: \"{{ sample.output_text }}\"\n\n"
            "RULE: The tutor must NEVER give multiple-choice options "
            "like 'Would you like to explore A, B, or C?' or "
            "'Which do you want: agents, specs, or skills?'\n\n"
            "Score 1.0 if the response does NOT contain multiple-choice "
            "options.\n"
            "Score 0.0 if the response offers 2+ options to choose from."
        ),
        "pass_threshold": 0.5,
    },
    # -----------------------------------------------------------------------
    # 9. Answers questions directly — model grader
    # -----------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "Answers student questions directly",
        "model": "gpt-4.1",
        "input": (
            "SCENARIO: {{ item.scenario }}\n"
            "STUDENT SAID: \"{{ item.student_message }}\"\n"
            "TUTOR RESPONSE: \"{{ sample.output_text }}\"\n\n"
            "RULE: When a student asks a direct question (scenario = "
            "'student_asks_question'), the tutor MUST answer the question "
            "directly and clearly FIRST, then connect it to the lesson.\n"
            "The tutor must NOT deflect with 'What do you think?' or "
            "turn the question back on the student without answering.\n\n"
            "If scenario is 'student_asks_question':\n"
            "  Score 1.0 if the tutor answers the question directly first.\n"
            "  Score 0.0 if the tutor deflects or doesn't answer.\n\n"
            "If scenario is NOT 'student_asks_question':\n"
            "  Score 1.0 (this criteria doesn't apply)."
        ),
        "pass_threshold": 0.5,
    },
    # -----------------------------------------------------------------------
    # 10. Confirms correct answers — model grader
    # -----------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "Confirms correct answers then advances",
        "model": "gpt-4.1",
        "input": (
            "SCENARIO: {{ item.scenario }}\n"
            "STUDENT SAID: \"{{ item.student_message }}\"\n"
            "TUTOR RESPONSE: \"{{ sample.output_text }}\"\n\n"
            "RULE: When a student gives a correct answer (scenario = "
            "'correct_answer'), the tutor MUST:\n"
            "1. Confirm they are correct (briefly)\n"
            "2. Then teach the NEXT concept or ask them to explain further\n\n"
            "If scenario is 'correct_answer':\n"
            "  Score 1.0 if the tutor confirms and moves forward.\n"
            "  Score 0.0 if the tutor ignores the correct answer or "
            "doesn't acknowledge it.\n\n"
            "If scenario is NOT 'correct_answer':\n"
            "  Score 1.0 (this criteria doesn't apply)."
        ),
        "pass_threshold": 0.5,
    },
    # -----------------------------------------------------------------------
    # 11. First message has greeting + topic + question — model grader
    # -----------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "First message structure correct",
        "model": "gpt-4.1",
        "input": (
            "SCENARIO: {{ item.scenario }}\n"
            "IS FIRST MESSAGE: {{ item.is_first_message }}\n"
            "TUTOR RESPONSE: \"{{ sample.output_text }}\"\n\n"
            "RULE: If this is the first message (is_first_message is true), "
            "the response MUST contain ALL THREE:\n"
            "1. A greeting (e.g., 'Hi Test Student!')\n"
            "2. A brief introduction of the topic in 1 sentence\n"
            "3. ONE diagnostic question to gauge what they know\n\n"
            "The response must NOT lecture or give a long explanation.\n\n"
            "If is_first_message is true:\n"
            "  Score 1.0 if all three elements are present.\n"
            "  Score 0.5 if two of three are present.\n"
            "  Score 0.0 if greeting or question is missing.\n\n"
            "If is_first_message is false:\n"
            "  Score 1.0 (this criteria doesn't apply)."
        ),
        "pass_threshold": 0.5,
    },
    # -----------------------------------------------------------------------
    # 12. Gently corrects wrong answers — model grader
    # -----------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "Gently corrects wrong answers",
        "model": "gpt-4.1",
        "input": (
            "SCENARIO: {{ item.scenario }}\n"
            "STUDENT SAID: \"{{ item.student_message }}\"\n"
            "TUTOR RESPONSE: \"{{ sample.output_text }}\"\n\n"
            "RULE: When a student gives a wrong answer (scenario = "
            "'wrong_answer'), the tutor must:\n"
            "1. NOT say 'Wrong!' or be harsh\n"
            "2. Gently correct with a clear explanation or analogy\n"
            "3. Ask a simpler follow-up question\n\n"
            "If scenario is 'wrong_answer':\n"
            "  Score 1.0 if correction is gentle and educational.\n"
            "  Score 0.0 if response is harsh, dismissive, or doesn't "
            "correct the misconception.\n\n"
            "If scenario is NOT 'wrong_answer':\n"
            "  Score 1.0 (this criteria doesn't apply)."
        ),
        "pass_threshold": 0.5,
    },
]

# ---------------------------------------------------------------------------
# Data source schema
# ---------------------------------------------------------------------------

DATA_SOURCE_CONFIG = {
    "type": "custom",
    "item_schema": {
        "type": "object",
        "properties": {
            "student_message": {"type": "string"},
            "scenario": {"type": "string"},
            "lesson_title": {"type": "string"},
            "is_first_message": {"type": "boolean"},
            "conversation_history": {"type": "string"},
        },
        "required": [
            "student_message",
            "scenario",
            "lesson_title",
            "is_first_message",
        ],
    },
    "include_sample_schema": True,
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def create_eval(client: OpenAI) -> str:
    """Create the eval configuration. Returns eval ID."""
    print("[1/3] Creating eval...")
    eval_obj = client.evals.create(
        name=EVAL_NAME,
        data_source_config=DATA_SOURCE_CONFIG,
        testing_criteria=TESTING_CRITERIA,
    )
    print(f"  Eval created: {eval_obj.id}")
    return eval_obj.id


def upload_test_data(client: OpenAI) -> str:
    """Upload test data JSONL file. Returns file ID."""
    print("[2/3] Uploading test data...")
    with open(TEST_DATA_FILE, "rb") as f:
        file_obj = client.files.create(file=f, purpose="evals")
    print(f"  File uploaded: {file_obj.id} ({file_obj.filename})")
    return file_obj.id


def run_eval(
    client: OpenAI, eval_id: str, file_id: str, run_name: str = "prompt-v2"
) -> dict:
    """Run the eval with our prompt. Returns run object."""
    print(f"[3/3] Running eval '{run_name}' with model {MODEL}...")

    # Build the message template
    # For first messages, use the first-message prompt
    # For follow-ups, use the follow-up prompt
    # We use a single template that works for both by including
    # conversation history as context
    system_prompt = FOLLOW_UP_SYSTEM_PROMPT

    run = client.evals.runs.create(
        eval_id,
        name=run_name,
        data_source={
            "type": "responses",
            "model": MODEL,
            "input_messages": {
                "type": "template",
                "template": [
                    {
                        "role": "developer",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": (
                            "Previous context: {{ item.conversation_history }}\n"
                            "Student message: {{ item.student_message }}"
                        ),
                    },
                ],
            },
            "source": {"type": "file_id", "id": file_id},
        },
    )
    print(f"  Run started: {run.id}")
    print(f"  Dashboard: {run.report_url}")
    return run


def wait_for_run(client: OpenAI, eval_id: str, run_id: str) -> dict:
    """Poll until run completes."""
    print("\n  Waiting for eval to complete", end="", flush=True)
    while True:
        run = client.evals.runs.retrieve(eval_id, run_id)
        if run.status in ("completed", "failed", "canceled"):
            print(f"\n  Status: {run.status}")
            return run
        print(".", end="", flush=True)
        time.sleep(5)


def print_results(run) -> None:
    """Print eval results summary."""
    print("\n" + "=" * 60)
    print("EVAL RESULTS")
    print("=" * 60)

    counts = run.result_counts
    total = counts.total if counts else 0
    passed = counts.passed if counts else 0
    failed = counts.failed if counts else 0
    errored = counts.errored if counts else 0

    print(f"  Total: {total} | Passed: {passed} | Failed: {failed} | Errors: {errored}")

    if total > 0:
        score = passed / total * 100
        print(f"  Score: {score:.0f}%")

    if run.per_testing_criteria_results:
        print("\n  Per-Criteria Results:")
        print(f"  {'Criteria':<45} {'Pass':>6} {'Fail':>6}")
        print("  " + "-" * 57)
        for r in run.per_testing_criteria_results:
            name = r.testing_criteria.split("-")[0].strip()[:44]
            print(f"  {name:<45} {r.passed:>6} {r.failed:>6}")

    print(f"\n  Full report: {run.report_url}")
    print("=" * 60)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Run Teach Me tutor evals")
    parser.add_argument("--eval-id", help="Existing eval ID (skip creation)")
    parser.add_argument("--file-id", help="Existing file ID (skip upload)")
    parser.add_argument(
        "--run-name",
        default="prompt-v2",
        help="Name for this eval run (default: prompt-v2)",
    )
    parser.add_argument(
        "--create-only",
        action="store_true",
        help="Only create eval + upload data, don't run",
    )
    parser.add_argument(
        "--no-wait",
        action="store_true",
        help="Don't wait for results (just kick off the run)",
    )
    args = parser.parse_args()

    client = OpenAI()

    # Step 1: Create or reuse eval
    eval_id = args.eval_id or create_eval(client)

    # Step 2: Upload or reuse test data
    file_id = args.file_id or upload_test_data(client)

    if args.create_only:
        print(f"\n  Eval ID: {eval_id}")
        print(f"  File ID: {file_id}")
        print("  Run from dashboard or with:")
        print(f"    python evals/run_eval.py --eval-id {eval_id} --file-id {file_id}")
        return

    # Step 3: Run eval
    run = run_eval(client, eval_id, file_id, args.run_name)

    if args.no_wait:
        print(f"\n  Run kicked off. Check dashboard: {run.report_url}")
        return

    # Wait and show results
    completed_run = wait_for_run(client, eval_id, run.id)
    print_results(completed_run)

    # Exit with error code if any tests failed
    if completed_run.result_counts and completed_run.result_counts.failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
