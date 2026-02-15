### Core Concept

Descriptive search means describing what you're looking for, not where you think it is. You know the content or purpose. Let the agent find the location.

### Key Mental Models

- **What over where**: Describe characteristics (PDF about taxes from 2023), not locations (maybe in Downloads).
- **Conversational refinement**: Start broad. See candidates. Narrow down. The agent filters results based on your feedback.
- **Pattern-based discovery**: Once you find one example, ask the agent to find all similar files.

### Critical Patterns

- **"Find files that match [description] from [time period]"**: The agent searches multiple locations using `find` and `grep` based on your description.
- **"It was specifically from [source/context]"**: Narrows results when initial search returns too many candidates.
- **"Find all similar files to this one"**: Triggers pattern-based discovery after finding a good example.
- **Principle 1 (Bash is the Key)**: The agent combines `find`, `grep`, and pipes to search by name, content, and metadata.
- **Principle 7 (Observability)**: The agent shows the search process, candidates found, and why certain files matched.

### Common Mistakes

- Searching only one folder at a time: The agent can search multiple locations simultaneously.
- Knowing the exact filename: You rarely remember precise names. Describe content instead.
- Not refining through conversation: First search often returns many candidates. Narrow down iteratively.

### Connections

- **Builds on**: Lessons 1-5 (all previous workflows including error recovery), Principle 1 (Bash) from Part 1
- **Leads to**: Capstone toolkit (Lesson 7) where search patterns become reusable prompts
