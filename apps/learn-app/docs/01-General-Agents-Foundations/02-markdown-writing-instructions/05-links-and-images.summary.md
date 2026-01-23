### Core Concept
Lesson teaching links (`[text](url)`) and images (`![alt](url)`) as the final markdown syntax elements needed for writing effective documentation, READMEs, and instruction files.

### Key Mental Models
- **Links as knowledge connectors**: References to documentation, standards, and resources create context that readers can follow for deeper understanding
- **Images as visual communication**: Screenshots, diagrams, and logos show what words alone cannot express
- **Syntax mirroring**: Image syntax is link syntax with a `!` prefix — learn one, you know both

### Critical Patterns
- **Link syntax**: `[link text](url)` where link text is visible/clickable and url is destination
- **Image syntax**: `![alt text](image-url)` (note: leading `!` distinguishes from links)
- **Alt text purpose**: Describes image for accessibility (screen readers) and fallback (broken images)
- **URL hygiene**: No spaces in URLs; use clean paths or %20 encoding

### Common Mistakes
- URL spaces breaking links (`[text](url with spaces)` fails; use clean URLs or URL encoding)
- Missing `!` in image syntax (creates link instead of embedded image)
- Broken image paths (images that don't exist render as broken in markdown viewers)
- Using links without context (link text should be descriptive: "[Python docs](url)" not "[click here](url)")
- Too many images (1 logo, 1-2 screenshots maximum; use strategically)

### Connections
- **Builds on**: Lessons 1-4 (markdown basics: headings, lists, code blocks)
- **Enables**: Writing complete READMEs, CLAUDE.md files, and project documentation with external references
- **Next steps**: Chapter 3 (General Agents) uses markdown files as operational context for AI tools
