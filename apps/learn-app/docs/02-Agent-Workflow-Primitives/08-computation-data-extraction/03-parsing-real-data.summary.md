### Core Concept

Real-world CSV data has commas inside quoted fields (like `"AMAZON, INC."`) that break simple tools like awk. Python's `csv` module understands quoting rules and handles these edge cases correctly. When data comes from outside your control, always use a proper CSV parser.

### Key Mental Models

- **The CSV parsing trap**: `awk -F','` splits on EVERY comma, including ones inside quotes. A field like `"AMAZON, INC."` becomes two broken fields instead of one. This is the single most common data processing bug.
- **Right tool for the job**: awk works for data you control (log files, tab-separated). For any CSV from an external source (bank exports, downloaded datasets), use Python's csv module.

### Critical Patterns

- Prompt pattern: "I have [structured data]. Process [column]. Be careful -- [edge case that could break naive parsing]."
- `csv.reader(sys.stdin)` handles quoted fields, escaped quotes, and different line endings automatically
- Mentioning edge cases in your prompt guides the agent to choose robust tools over simple ones

### Common Mistakes

- Splitting CSV on commas with awk or cut -- this silently produces wrong results on any field containing a comma
- Not mentioning known data quirks in your prompt -- "sum the third column" might get awk; "sum the Amount column, some merchants have commas" gets csv module
- Forgetting that `next(reader)` skips the header row -- without it, the header line gets processed as data

### Connections

- **Builds on**: sum.py (Lesson 1) and verification (Lesson 2)
- **Leads to**: Making scripts permanent (Lesson 4)
