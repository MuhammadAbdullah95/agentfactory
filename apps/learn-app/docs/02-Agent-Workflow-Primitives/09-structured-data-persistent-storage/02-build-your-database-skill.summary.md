### Core Concept

A skill is a structured, reusable directory that captures your expertise as you learn -- not notes, not documentation, but a permanent tool that grows with you. Building a `/database-deployment` skill before learning database concepts means every lesson adds to an asset you own and can invoke on any future project.

### Continuity Bridge

- From Chapter 7: repeatable operational workflows mattered.
- From Chapter 8: reusable script utilities mattered.
- Now in Chapter 9: reusable persistence patterns are captured as a skill contract.

### Key Mental Models

- **Skill-first learning vs traditional learning**: Traditional knowledge fades because it lives in your head. A skill lives in a file -- permanent, reusable, and readable by AI collaborators. You accumulate expertise instead of re-learning.
- **Ownership over consumption**: Creating the skill directory yourself (SKILL.md, references/, examples/) gives you control over the structure. You are not passively reading -- you are building a tool.

### Critical Patterns

- Skill directory structure: `SKILL.md` (understanding), `references/` (patterns per lesson), `examples/` (code you write and test)
- YAML frontmatter in SKILL.md with name and description
- Placeholder sections (Persona, When to Use, Core Concepts, Decision Logic, Safety) that get filled in as you learn
- Testing patterns immediately: write a simple model class to verify your understanding before moving on

### Common Mistakes

- Treating the skill like notes -- just dumping text instead of organizing patterns for reuse
- Skipping the test step (running simple-expense.py) and assuming the code works
- Not reading the reference skill (`building-with-sqlalchemy-orm`) before creating your own

### Connections

- **Builds on**: Skill creation patterns from Chapter 5 (skill directory structure, YAML frontmatter)
- **Leads to**: Why databases beat CSV files (Lesson 1), where the "When to Use" section gets filled in
