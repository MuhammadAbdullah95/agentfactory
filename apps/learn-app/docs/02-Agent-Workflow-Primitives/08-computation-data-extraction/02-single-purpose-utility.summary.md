### Core Concept

Instead of asking an AI for a one-time answer, direct it to build a reusable tool. A script that reads from stdin and writes to stdout becomes a composable Unix component you can pipe data through forever.

### Key Mental Models

- **Reusable tool over one-time answer**: A script that sums any list of numbers is more valuable than knowing the sum of three specific numbers.
- **stdin/stdout as universal interface**: Scripts that read from standard input and write to standard output connect to any data source via pipes.
- **Describe the problem, not the implementation**: Telling the agent "I have decimal numbers, one per line, I need the sum" lets it choose the right approach (Python, stdin pattern).

### Critical Patterns

- **The computation prompt pattern**: "I have [data problem]. Build me a script that [reads from stdin] and [produces output]." This signals you want a composable, reusable tool.
- **Pipe operator data flow**: `cat file.txt | python sum.py` connects cat's stdout to sum.py's stdin. The script doesn't know or care where its input comes from.
- **The shebang line** (`#!/usr/bin/env python3`): Tells the OS which interpreter to use, enabling `./script.py` execution.

### Common Mistakes

- Asking for a direct calculation instead of a script: You get a one-time answer that can't be reused next month.
- Forgetting `.strip()` on stdin lines: Trailing newlines cause `float()` conversion to fail.
- Not specifying "reads from stdin" in the prompt: Without this signal, the agent may hardcode filenames instead of building a composable tool.

### Connections

- **Builds on**: The Arithmetic Gap (Lesson 1) - Python solves the decimal problem Bash can't handle
- **Leads to**: The Testing Loop (Lesson 3) - how to verify the script actually produces correct results
