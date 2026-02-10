### Core Concept

Pattern matching with regex word boundaries and false-positive guards enables precise transaction categorization. Simple keyword matching produces wrong results because partial word matches (CVS in CVSMITH) and ambiguous prefixes (DR in DR PEPPER) create false positives.

### Key Mental Models

- **False positive guards checked first**: Check exclusion patterns before category patterns. "DR PEPPER" matches the false positive list before it can reach the medical category.
- **Word boundaries for precision**: `\bCVS\b` matches "CVS PHARMACY" but rejects "CVSMITH" because `\b` requires the match to be a complete word, not part of a longer one.
- **Batch processing with find and xargs**: `find statements/ -name "*.csv" | xargs cat | python script.py` processes an entire folder of files in one pipeline.

### Critical Patterns

- **The categorization prompt pattern**: "Categorize [data] by [criteria]. Watch out for [false positives]." Explicitly naming edge cases triggers the agent to build guards.
- **Regex word boundary** (`\b`): Marks where a word starts or ends. `\bCVS\b` matches the standalone word CVS in any position but never as part of another word.
- **Order of operations**: False positives first, then categories. This ordering prevents ambiguous matches from being incorrectly categorized.

### Common Mistakes

- Using simple `in` checks instead of regex: `if 'cvs' in description.lower()` matches "CVSMITH" - a false positive.
- Not mentioning edge cases in the prompt: "Categorize as medical" gets basic keyword matching. Adding "Watch out for Dr. Pepper" gets false positive guards.
- Forgetting case handling: Bank statements use inconsistent casing. Always normalize with `.upper()` or use `re.IGNORECASE`.

### Connections

- **Builds on**: From Script to Command (Lesson 4) - CSV parsing with Python's csv module; permanent command pattern
- **Leads to**: Capstone (Lesson 6) - combining categorization with verification-first orchestration for a complete tax prep workflow
