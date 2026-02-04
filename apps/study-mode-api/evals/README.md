# Teach Me Tutor — Eval Suite

Automated evaluations for the Socratic tutor prompt using [OpenAI Evals API](https://platform.openai.com/docs/guides/evals).

## Quick Start

```bash
# Run all evals (creates eval + uploads data + runs + waits for results)
cd apps/study-mode-api
uv run python evals/run_eval.py

# Re-run after prompt changes (reuse existing eval and data)
uv run python evals/run_eval.py --eval-id eval_xxx --file-id file_xxx --run-name "prompt-v3"

# Create eval without running (use dashboard instead)
uv run python evals/run_eval.py --create-only
```

## What Gets Tested (12 Criteria)

| # | Criteria | Type | What It Checks |
|---|---------|------|----------------|
| 1 | No "Great question" | string_check | Blocks filler praise |
| 2 | No "Nice start" | string_check | Blocks filler praise |
| 3 | No "Excellent!" | string_check | Blocks filler praise |
| 4 | No "Good job" | string_check | Blocks filler praise |
| 5 | No "Micro-explain" label | string_check | No internal labels leaked |
| 6 | No "Guide question" label | string_check | No internal labels leaked |
| 7 | No "Micro_explain" label | string_check | No internal labels leaked |
| 8 | No "Confirm_then_push" label | string_check | No internal labels leaked |
| 9 | No "STEP 1" label | string_check | No step labels leaked |
| 10 | Teaches when stuck | score_model | "no"/"I don't know" → teach first |
| 11 | One question only | score_model | Exactly 1 question per response |
| 12 | No re-greeting | score_model | Follow-ups don't say "Hi" again |
| 13 | Under 200 words | score_model | Concise responses |
| 14 | Bold key terms | score_model | Uses **bold** for new terms |
| 15 | No multiple-choice | score_model | Doesn't offer A/B/C options |
| 16 | Answers questions | score_model | Direct answer when student asks |
| 17 | Confirms correct | score_model | Acknowledges right answers |
| 18 | First message structure | score_model | Greeting + topic + question |
| 19 | Gentle corrections | score_model | Kind tone for wrong answers |

## Test Scenarios (20 cases)

- First message (greeting flow)
- Student says "no" (3 variations)
- Student says "I don't know" / "I can't" / "not sure" / "confusing" / "what?"
- Correct answers (3 variations)
- Wrong answer
- Partially correct answer
- Student asks questions (4 variations)
- Student confirms understanding (2 variations)

## Workflow

```
Change prompt in triage.py
    → Run eval
    → Check dashboard for pass/fail
    → Fix failures
    → Re-run eval
    → All green → Push to PR
```
