### Core Concept

Exit code 0 means "didn't crash," not "correct answer." Zero-trust verification creates test data with known answers and compares output to expectation, catching logic errors that exit codes miss entirely.

### Key Mental Models

- **Zero-trust verification**: Assume everything is broken until proven otherwise. Don't trust output because it appeared without red text.
- **Known-answer testing**: Create inputs where you can calculate the expected result in your head (10 + 20 + 30 = 60), then verify the script matches.
- **Exit codes vs. correctness**: A script can exit 0 and produce completely wrong results. Silent logic errors are more dangerous than crashes.

### Critical Patterns

- **The verification prompt pattern**: "Verify [tool] works correctly. Create test data with a known answer [X] and check that output matches."
- **Multiple test categories**: Test integers, decimals, negative numbers, and edge cases (empty input, single number, whitespace) to cover different failure modes.
- **`echo $?` for exit codes**: Check immediately after the command you care about, since any subsequent command overwrites `$?`.

### Common Mistakes

- Trusting output because no errors appeared: A buggy script can silently skip numbers and still exit 0.
- Using complex test data you can't verify by hand: The whole point is knowing the right answer before running the script.
- Running another command before checking `$?`: The exit code belongs to the most recent command, not the one you intended.

### Connections

- **Builds on**: Your First Python Utility (Lesson 2) - sum.py needs verification beyond "it ran"
- **Leads to**: From Script to Command (Lesson 4) - verified scripts are worth making permanent
