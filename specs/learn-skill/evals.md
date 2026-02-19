# Learn-AgentFactory Skill Evals

Evaluation framework for the personalized teaching skill. Measures whether an AI agent using this skill **actually teaches** — not just delivers content.

Based on: [OpenAI Eval Skills](https://developers.openai.com/blog/eval-skills/), [Anthropic Demystifying Evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

---

## Eval Architecture

```
Eval Suite (8 dimensions, 53 tasks)
├── Deterministic graders (file checks, command verification, transcript analysis)
├── Model-based graders (rubric scoring via LLM judge)
└── Human graders (spot-check calibration, 10% sample)
```

**Key principle**: Grade the OUTCOME and QUALITY, not the exact path. Agents find valid approaches we didn't anticipate.

**Reliability metric**: Each task runs 3 trials. We track pass@3 (at least 1 success) AND pass^3 (all 3 succeed). Production-ready = pass^3 > 80%.

---

## Dimension 1: Skill Activation (8 tasks)

**What we're testing**: Does the skill trigger on the right prompts and NOT trigger on wrong ones?

### Positive Cases (should activate)

| ID    | Prompt                       | Expected                                       | Grader                                                                   |
| ----- | ---------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------ |
| ACT-1 | "teach me about AI agents"   | Skill activates, reads MEMORY.md or creates it | Deterministic: check for `mkdir -p ~/.agentfactory` or Read of MEMORY.md |
| ACT-2 | "let's study"                | Skill activates                                | Deterministic: api.py called                                             |
| ACT-3 | "quiz me on the last lesson" | Skill activates in Coach/quiz mode             | Deterministic: api.py or MEMORY.md read                                  |
| ACT-4 | "what should I study next?"  | Skill activates in Manager mode                | Deterministic: progress or tree fetched                                  |
| ACT-5 | "continue where I left off"  | Skill activates, reads session.md              | Deterministic: session.md read attempt                                   |

### Negative Cases (should NOT activate)

| ID    | Prompt                        | Expected                | Grader                                                    |
| ----- | ----------------------------- | ----------------------- | --------------------------------------------------------- |
| ACT-6 | "help me fix this Python bug" | Skill does NOT activate | Deterministic: no api.py calls, no ~/.agentfactory access |
| ACT-7 | "what's the weather today?"   | Skill does NOT activate | Deterministic: no skill-related tool calls                |
| ACT-8 | "write me a FastAPI endpoint" | Skill does NOT activate | Deterministic: no skill-related tool calls                |

### Pass Criteria

- Positive: 5/5 activate correctly
- Negative: 3/3 correctly ignored
- False positive rate: 0%

---

## Dimension 2: Session Setup (7 tasks)

**What we're testing**: First-session onboarding and returning-session context loading.

### First Session

| ID    | Setup                         | Prompt     | Expected Behavior                                      | Grader                                                                                                       |
| ----- | ----------------------------- | ---------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| SET-1 | No ~/.agentfactory/ directory | "teach me" | Creates directory, asks name + preference + tutor name | Deterministic: dir created, MEMORY.md written. Model-based: asked 3 questions (name, preference, tutor name) |
| SET-2 | No ~/.agentfactory/           | "teach me" | MEMORY.md matches template structure                   | Deterministic: parse MEMORY.md, verify Identity/Learning Style/Progress/Quiz History sections exist          |
| SET-3 | No ~/.agentfactory/           | "teach me" | Runs health check before anything else                 | Deterministic: `api.py health` is first api command                                                          |

### Returning Session

| ID    | Setup                                                          | Prompt        | Expected Behavior                                    | Grader                                                                |
| ----- | -------------------------------------------------------------- | ------------- | ---------------------------------------------------- | --------------------------------------------------------------------- |
| SET-4 | MEMORY.md exists with name "Sarah", tutor_name "Professor Ada" | "let's study" | Greets as "Professor Ada", references Sarah by name  | Model-based: response contains personalized greeting using both names |
| SET-5 | MEMORY.md with last session data                               | "continue"    | References last session's topic, doesn't re-ask name | Model-based: no name/preference questions, references prior topic     |
| SET-6 | MEMORY.md + session.md (mid-lesson)                            | "continue"    | Resumes from session.md phase, doesn't restart       | Deterministic: no tree fetch if session.md says "teaching" phase      |
| SET-7 | Auth fails (no credentials)                                    | "teach me"    | Directs to run auth.py, doesn't crash                | Deterministic: auth.py referenced. Model-based: helpful error message |

### Pass Criteria

- First session: MEMORY.md created with all required fields (3/3)
- Returning session: personalized greeting + context restoration (3/3)
- Error handling: graceful auth failure (1/1)

---

## Dimension 3: Teaching Quality (10 tasks)

**What we're testing**: Does the agent actually TEACH or just dump content?

### Content Delivery Anti-Pattern Detection

| ID      | Setup                                     | Scenario             | FAIL if                                                                     | Grader                                                                    |
| ------- | ----------------------------------------- | -------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| TEACH-1 | Lesson fetched to cache                   | Agent teaches lesson | Raw lesson markdown appears in response (>50 consecutive words from source) | Deterministic: diff agent output vs lesson content, flag >50-word overlap |
| TEACH-2 | Lesson fetched                            | Agent teaches        | Response is a single wall of text >500 words without questions              | Model-based: check for formative checks within explanation                |
| TEACH-3 | Lesson with cognitive_load.new_concepts=7 | Agent teaches        | All 7 concepts explained in one pass without pause                          | Model-based: verify chunking happened (2-3 groups with checks)            |

### Pedagogical Quality

| ID      | Setup                                      | Scenario                | PASS if                                                                              | Grader                                                                                  |
| ------- | ------------------------------------------ | ----------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| TEACH-4 | Returning session, previous lesson on OODA | Agent starts new lesson | Session opens with retrieval from previous lesson ("What do you remember about...?") | Model-based: first teaching turn includes retrieval question about prior content        |
| TEACH-5 | Lesson with skills[].bloom_level="Apply"   | Agent teaches           | Teaching includes scenario/application examples, not just definitions                | Model-based: rubric checks for concrete scenarios, "given X, how would you..." patterns |
| TEACH-6 | MEMORY.md shows learner prefers examples   | Agent teaches           | Leads with concrete examples before abstract principles                              | Model-based: first explanation uses example/scenario/story, not abstract definition     |
| TEACH-7 | MEMORY.md shows learner prefers theory     | Agent teaches           | Leads with principles before examples                                                | Model-based: first explanation states principle/rule, then illustrates                  |
| TEACH-8 | Lesson has practice_exercise               | Agent teaches           | Eventually enters Mentor mode for practice                                           | Model-based: practice section appears, guided then independent                          |

### Feynman Verification

| ID       | Setup                          | Scenario       | PASS if                                                               | Grader                                                   |
| -------- | ------------------------------ | -------------- | --------------------------------------------------------------------- | -------------------------------------------------------- |
| TEACH-9  | After explaining a concept     | Agent teaches  | At least one "explain this back to me" / teach-back prompt per lesson | Model-based: transcript contains teach-back request      |
| TEACH-10 | Learner gives vague teach-back | Agent responds | Identifies specific gap, doesn't just say "good"                      | Model-based: response pinpoints what was missing/unclear |

### Pass Criteria

- Anti-pattern detection: 0/3 anti-patterns triggered
- Pedagogical quality: 4/5 passed
- Feynman: 2/2 passed
- Overall: 8/10 minimum

### Scoring Rubric (Model-Based Grader)

```json
{
  "teaching_quality": {
    "explains_in_own_words": {"score": 0-2, "notes": "0=raw paste, 1=paraphrased, 2=original analogies"},
    "formative_checks": {"score": 0-2, "notes": "0=none, 1=end-only, 2=every 2-3 concepts"},
    "scaffolding_appropriate": {"score": 0-2, "notes": "0=mismatch, 1=partially adapted, 2=matches MEMORY.md"},
    "cognitive_load_managed": {"score": 0-2, "notes": "0=dumped all, 1=some chunking, 2=proper chunks with checks"},
    "feynman_applied": {"score": 0-2, "notes": "0=never, 1=once, 2=integrated throughout"}
  },
  "total": "0-10",
  "pass_threshold": 7
}
```

---

## Dimension 4: Mode Selection (8 tasks)

**What we're testing**: Does the agent dynamically select the right teaching mode?

| ID     | Setup                        | Learner Signal                | Expected Mode                                  | Grader                                                           |
| ------ | ---------------------------- | ----------------------------- | ---------------------------------------------- | ---------------------------------------------------------------- |
| MODE-1 | New lesson loaded            | (no signal)                   | Tutor (default)                                | Model-based: agent explains concepts, doesn't quiz/question      |
| MODE-2 | During teaching              | "Why is that important?"      | Socratic                                       | Model-based: agent responds with question, not answer            |
| MODE-3 | Quiz score 2/5               | (automatic)                   | Coach                                          | Model-based: agent diagnoses weakness, provides drills           |
| MODE-4 | Lesson has practice_exercise | "Let me try building it"      | Mentor                                         | Model-based: agent reviews work, provides architectural guidance |
| MODE-5 | 3 consecutive 5/5 quizzes    | "Challenge me"                | Simulator                                      | Model-based: agent presents scenario with constraints/tradeoffs  |
| MODE-6 | Session start                | "What should I study next?"   | Manager                                        | Model-based: agent reviews progress, suggests path               |
| MODE-7 | Learner is frustrated        | "This is too hard, I give up" | Switch to Coach (scaffold down)                | Model-based: agent simplifies, doesn't push harder               |
| MODE-8 | Learner is bored             | "This is too easy"            | Switch to Socratic or Simulator (challenge up) | Model-based: agent increases difficulty                          |

### Pass Criteria

- Correct mode: 6/8 minimum
- No mode should persist when signals clearly demand a switch

### Scoring Rubric

```json
{
  "mode_selection": {
    "correct_initial_mode": {"pass": true/false},
    "responds_to_signal": {"pass": true/false},
    "transition_smooth": {"score": 0-2, "notes": "0=jarring, 1=abrupt, 2=natural"}
  }
}
```

---

## Dimension 5: Quiz Quality (8 tasks)

**What we're testing**: Quizzes test understanding at the right Bloom's level, with proper follow-up.

### Quiz Construction

| ID     | Setup                                   | Expected                                     | Grader                                                           |
| ------ | --------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------- |
| QUIZ-1 | Lesson with bloom_level="Apply"         | Questions are scenario-based, not "define X" | Model-based: rubric checks question format matches Bloom's Apply |
| QUIZ-2 | Lesson with bloom_level="Remember" (A1) | Questions are recall/recognition             | Model-based: questions ask "what is" or "which of these"         |
| QUIZ-3 | Any lesson                              | 3-5 questions generated                      | Deterministic: count questions in quiz turn                      |
| QUIZ-4 | Lesson with learning_objectives         | Questions map to stated objectives           | Model-based: each question traceable to an objective             |

### Quiz Interaction

| ID     | Setup                    | Learner Response | Expected Agent Behavior                                | Grader                                                                    |
| ------ | ------------------------ | ---------------- | ------------------------------------------------------ | ------------------------------------------------------------------------- |
| QUIZ-5 | Quiz question            | Correct answer   | Elaborative interrogation: "WHY is that correct?"      | Model-based: follow-up asks for reasoning                                 |
| QUIZ-6 | Quiz question            | Wrong answer     | "What led you to that?" — guide, don't just correct    | Model-based: explores reasoning before correcting                         |
| QUIZ-7 | Quiz complete, score 2/5 | (automatic)      | Does NOT advance to next lesson. Re-teaches weak areas | Deterministic: no `api.py complete` call. Model-based: re-teaching occurs |
| QUIZ-8 | Quiz complete, score 4/5 | (automatic)      | Advances, celebrates, records in MEMORY.md             | Deterministic: `api.py complete` called. MEMORY.md updated                |

### Pass Criteria

- Construction: 3/4 pass
- Interaction: 4/4 pass (these are critical — wrong behavior here undermines all teaching)

### Scoring Rubric

```json
{
  "quiz_quality": {
    "blooms_alignment": {"score": 0-2, "notes": "0=wrong level, 1=partially, 2=correct level"},
    "scenario_based": {"pass": true/false, "notes": "not just definitions"},
    "elaborative_follow_up": {"pass": true/false, "notes": "asks WHY on correct answers"},
    "growth_mindset_on_error": {"pass": true/false, "notes": "explores reasoning, doesn't just correct"},
    "mastery_gating": {"pass": true/false, "notes": "<3/5 blocks advancement"}
  }
}
```

---

## Dimension 6: Personalization (6 tasks)

**What we're testing**: Does teaching adapt based on MEMORY.md data across sessions?

| ID     | MEMORY.md State                                      | Expected Adaptation                                               | Grader                                                        |
| ------ | ---------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------- |
| PERS-1 | Pace: fast, 3 sessions, all 5/5                      | Shorter explanations, skip basics, jump to application            | Model-based: explanation length, directness                   |
| PERS-2 | Pace: careful, struggles with abstract concepts      | Lead with examples, more formative checks, heavier scaffolding    | Model-based: examples before theory, more questions           |
| PERS-3 | Weak area "OODA loop" from 3 sessions ago            | Spaced retrieval: "Before we start, let's revisit OODA..."        | Model-based: prior weak area mentioned at session start       |
| PERS-4 | Quiz history shows improving trend (2/5 → 3/5 → 4/5) | Reduce scaffolding, note progress: "You've really improved on..." | Model-based: acknowledges improvement, growth mindset         |
| PERS-5 | Tutor name "Coach Z"                                 | Agent refers to self as "Coach Z" in conversation                 | Model-based: self-references use tutor name                   |
| PERS-6 | End of session                                       | MEMORY.md updated with session log, quiz scores, observations     | Deterministic: MEMORY.md file modified, new quiz entry exists |

### Pass Criteria

- Adaptive pacing: 2/2
- Spaced retrieval: 1/1
- Tutor identity: 1/1
- MEMORY.md persistence: 1/1
- Overall: 5/6 minimum

---

## Dimension 7: Error Recovery (4 tasks)

**What we're testing**: Graceful degradation — errors never end a session.

| ID    | Error Condition                           | Expected                                                  | Grader                                                                    |
| ----- | ----------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------- |
| ERR-1 | `api.py progress` returns 503             | Skip progress, use MEMORY.md last-known, continue session | Deterministic: session continues. Model-based: explains briefly, no panic |
| ERR-2 | `api.py tree` returns connection error    | Use cached tree.json if available, explain                | Deterministic: reads cache file. Model-based: session continues           |
| ERR-3 | `api.py lesson` returns 404 (wrong slugs) | Shows tree, helps pick correct lesson                     | Deterministic: tree displayed. Model-based: guides to correct selection   |
| ERR-4 | `api.py complete` fails                   | Still celebrates learning, tries again later              | Model-based: session doesn't end abruptly, learning acknowledged          |

### Pass Criteria

- 4/4 — error recovery is non-negotiable. A single session-ending error is a critical failure.

---

## Dimension 8: Context Management (4 tasks)

**What we're testing**: Efficient context window usage and compaction recovery.

| ID    | Scenario                               | Expected                                        | Grader                                                                           |
| ----- | -------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------- |
| CTX-1 | Tree API returns large JSON            | Writes to cache file, doesn't hold in context   | Deterministic: file write to cache/tree.json, response doesn't include full JSON |
| CTX-2 | Lesson API returns full content        | Writes to cache, teaches from frontmatter first | Deterministic: file write. Model-based: initial teaching uses metadata not body  |
| CTX-3 | Context compaction occurs mid-lesson   | Reads session.md + MEMORY.md + cache, resumes   | Deterministic: all 3 files read. Model-based: "Let me pick up where we were..."  |
| CTX-4 | Phase transition (teaching → quizzing) | session.md updated with new phase               | Deterministic: session.md write with updated phase                               |

### Pass Criteria

- 4/4 — context mismanagement causes session degradation

---

## Eval Execution Plan

### How to Run

Each eval task requires:

1. **Setup**: Pre-populate ~/.agentfactory/ with the specified state (or empty for first-session tasks)
2. **Prompt**: Send the specified user message
3. **Simulate**: For multi-turn tasks, use a simulated learner (LLM playing student role)
4. **Grade**: Run deterministic checks first, then model-based rubrics
5. **Record**: Log transcript + grades to eval results

### Simulated Learner Profiles

For multi-turn evals, we need simulated students:

| Profile        | Behavior                                                  | Tests                     |
| -------------- | --------------------------------------------------------- | ------------------------- |
| **Beginner**   | Short answers, asks "what does that mean?", gets confused | TEACH-3,6, MODE-7, QUIZ-6 |
| **Advanced**   | Detailed answers, asks "why?", challenges assumptions     | MODE-2,5,8, QUIZ-5        |
| **Disengaged** | One-word answers, "ok", "sure", "I guess"                 | PERS-2, MODE-7            |
| **Eager**      | Long responses, asks questions beyond the lesson          | TEACH-8, MODE-4           |

### Grader Prompts (Model-Based)

**Teaching Quality Grader**:

```
You are evaluating an AI tutor's teaching quality. Given the lesson
frontmatter (ground truth) and the tutor's conversation transcript,
score each dimension 0-2.

Key questions:
1. Did the tutor explain in their own words or paste lesson content?
2. Were formative checks embedded every 2-3 concepts?
3. Was scaffolding appropriate for the learner's level (check MEMORY.md)?
4. Was cognitive load managed (chunking for high-concept lessons)?
5. Was Feynman teach-back used at least once?

Score strictly. A tutor that dumps content gets 0 even if the content is correct.
```

**Mode Selection Grader**:

```
You are evaluating whether the AI tutor selected the correct teaching
mode based on the learner's signal. Given the signal and the expected
mode, check:

1. Did the tutor's behavior match the expected mode?
2. Was the transition natural or jarring?
3. Did the tutor over-stay in a mode when signals demanded switching?

Mode definitions:
- Tutor: explains concepts, uses analogies, formative checks
- Coach: diagnoses errors, provides drills, corrects gaps
- Socratic: asks questions, challenges assumptions, avoids direct answers
- Mentor: reviews work, suggests improvements, guides building
- Simulator: presents scenarios, maintains state, applies consequences
- Manager: reviews progress, plans path, schedules review
```

### Priority Order

Run evals in this order (highest impact first):

1. **Dimension 3: Teaching Quality** — if teaching is bad, nothing else matters
2. **Dimension 5: Quiz Quality** — quizzes verify learning actually happened
3. **Dimension 4: Mode Selection** — adaptive behavior is the core differentiator
4. **Dimension 7: Error Recovery** — reliability is non-negotiable
5. **Dimension 6: Personalization** — this is what makes it a _personalized_ tutor
6. **Dimension 2: Session Setup** — first impressions matter
7. **Dimension 1: Skill Activation** — basic correctness
8. **Dimension 8: Context Management** — technical robustness

---

## Success Criteria Summary

| Dimension          | Tasks | Pass Threshold | Critical?                         |
| ------------------ | ----- | -------------- | --------------------------------- |
| Skill Activation   | 8     | 8/8 (100%)     | Yes — false positives break trust |
| Session Setup      | 7     | 6/7 (86%)      | No                                |
| Teaching Quality   | 10    | 8/10 (80%)     | Yes — core purpose                |
| Mode Selection     | 8     | 6/8 (75%)      | No                                |
| Quiz Quality       | 8     | 7/8 (88%)      | Yes — mastery gating is critical  |
| Personalization    | 6     | 5/6 (83%)      | No                                |
| Error Recovery     | 4     | 4/4 (100%)     | Yes — sessions must never crash   |
| Context Management | 4     | 4/4 (100%)     | Yes — technical reliability       |

**Overall pass**: All critical dimensions at threshold + 75% of non-critical dimensions at threshold.

**Regression suite**: Once a task reaches pass^3=100%, lock it as a regression test. Any future failure triggers investigation.

---

## Comparison Checklist: Evals vs Actual Experience

After running the skill in a real session, compare against these expectations:

```
[ ] First session asked my name, preference, AND tutor name
[ ] Returned as my named tutor in subsequent sessions
[ ] Teaching used analogies, not raw content paste
[ ] I was asked to explain concepts back (Feynman)
[ ] Formative checks happened during teaching, not just at end
[ ] Quiz questions matched the lesson's Bloom's level
[ ] On correct answer, I was asked WHY
[ ] On wrong answer, my reasoning was explored (not just corrected)
[ ] Score < 3/5 blocked advancement (mastery gating worked)
[ ] Mode shifted naturally when I asked "why?" (Socratic)
[ ] Mode shifted when I said "let me try" (Mentor)
[ ] API errors didn't crash the session
[ ] My MEMORY.md was updated with session observations
[ ] Previous weak areas were revisited (spaced repetition)
[ ] Scaffolding decreased as I improved
[ ] Session ended with reflection + next lesson preview
```
