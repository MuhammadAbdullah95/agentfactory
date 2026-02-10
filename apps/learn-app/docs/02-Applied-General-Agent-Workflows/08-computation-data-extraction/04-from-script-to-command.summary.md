### Core Concept

Simple text tools like awk and cut break on real-world CSV data because they don't understand quoting rules. Python's csv module handles quoted fields correctly, and shell aliases turn one-off scripts into permanent commands available from any directory.

### Key Mental Models

- **The CSV parsing trap**: Splitting on commas fails when fields contain commas inside quotes (e.g., `"AMAZON, INC."`). Naive tools see every comma as a separator.
- **Right tool for the data source**: If the CSV came from outside your control (bank exports, downloaded datasets), always use a proper CSV parser.
- **Scripts become commands**: Moving a script to `~/tools/`, making it executable with `chmod +x`, and creating a shell alias makes it a permanent part of your toolkit.

### Critical Patterns

- **The structured data prompt pattern**: "I have [structured data type]. Process [specific column/field]. Be careful - [edge case that could break naive parsing]." Mentioning the edge case guides the agent to robust solutions.
- **Making tools permanent**: `mkdir -p ~/tools/` → `chmod +x script.py` → add alias to `~/.bashrc` or `~/.zshrc` → `source` to reload.
- **awk vs. csv module decision**: awk works for consistent delimiters you control; Python's csv module is required for any external data with potential quoting.

### Common Mistakes

- Using awk on bank statement CSVs: `awk -F',' '{print $3}'` on `"AMAZON, INC.",-89.50` returns `INC."` instead of the amount.
- Creating aliases with relative paths: `alias sum-expenses='python sum-expenses.py'` only works in the script's directory. Use absolute paths like `python3 ~/tools/sum-expenses.py`.
- Forgetting to `source` the shell config: The alias won't be available until the config is reloaded or a new terminal is opened.

### Connections

- **Builds on**: The Testing Loop (Lesson 3) - verified scripts are worth making permanent; sum.py evolves into sum-expenses.py
- **Leads to**: Data Wrangling (Lesson 5) - now that you can parse CSVs, you can categorize transactions
