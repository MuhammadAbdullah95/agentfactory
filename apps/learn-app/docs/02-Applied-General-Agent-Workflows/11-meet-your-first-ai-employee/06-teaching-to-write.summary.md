### Core Concept
Skills are portable expertise packages—markdown files that teach your AI Employee how to handle specific tasks. Build once for OpenClaw, and the same skill works in Claude Code, Claude Cowork, or any AgentSkills-compatible platform. Your skills are YOUR intellectual property.

### Key Mental Models
- **Skills = Training Manuals**: Like training a new hire with documented procedures
- **Portability Promise**: Same SKILL.md works across platforms because it's just markdown with instructions
- **Precedence System**: Workspace > Managed (~/.openclaw/skills) > Bundled—local always wins

### Critical Patterns
- Directory structure: `~/.openclaw/skills/skill-name/SKILL.md`
- YAML frontmatter: `name` (identifier), `description` (when to use), `metadata` (platform settings)
- Skills load on session start: `openclaw gateway restart` to pick up new skills
- Verify loading: `openclaw skills list` shows which skills are active

### Common Mistakes
- Directory name not matching `name:` field in frontmatter
- File not named exactly `SKILL.md` (case-sensitive)
- Invalid YAML syntax in frontmatter
- Not restarting gateway after creating new skills

### Connections
- **Builds on**: Understanding bootstrap files (Lesson 5)
- **Leads to**: Building more specialized skills (Lessons 7-8)
