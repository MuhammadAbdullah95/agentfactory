### Core Concept

Bash arithmetic is integer-only, so any calculation involving decimals fails silently or throws errors. LLMs predict text rather than compute, making their "head math" unreliable at scale. The reliable path is to write code that executes calculations deterministically.

### Key Mental Models

- **Integer-only arithmetic**: Bash's `$((...))` syntax truncates decimals without warning (`10 / 3` returns `3`, not `3.333`), making it dangerous for financial calculations.
- **Prediction vs. computation**: LLMs generate plausible-looking numbers by pattern matching, not arithmetic. This works for small sums but fails on real datasets.
- **"If it's math, it belongs in a script"**: Don't ask AI to calculate. Ask AI to write code that calculates. Code executes deterministically; predictions do not.

### Critical Patterns

- **The Decision Framework**: Does it involve decimals? Use Python. More than 10 numbers? Use Python. Even for simple integer math, Python is safer than Bash.
- **Discovering tool limits through experimentation**: Running `echo $((1.2 + 2.3))` yourself reveals the limitation more memorably than reading about it.
- **Python as the decimal bridge**: `print(47.50 / 3)` gives the correct answer where Bash errors out entirely.

### Common Mistakes

- Trusting Bash division results: `$((10 / 3))` returns `3` with no error or warning about truncation.
- Asking an LLM to sum large datasets: Predictions break down beyond a handful of numbers, producing confidently wrong answers.
- Assuming "no error" means "correct": Bash truncation is silent data loss, not a crash.

### Connections

- **Builds on**: Seven Principles (Chapter 6), especially P1 (Bash is the Key) and P3 (Verification as Core Step)
- **Leads to**: Building a Python utility that reads from stdin (Lesson 2)
