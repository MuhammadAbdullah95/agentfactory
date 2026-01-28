---
title: "Links and Images"
description: "Adding hyperlinks and images to markdown documents for richer communication"
sidebar_label: "Links and Images"
sidebar_position: 5
chapter: 2
lesson: 5
duration_minutes: 35
proficiency: "A2"
concepts: 3

skills:
  - name: "Creating Links"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can create working links to documentation and other resources in markdown"

  - name: "Adding Images"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can add images to markdown documents for README screenshots, diagrams, and logos"

  - name: "Using Text Emphasis"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can use bold and italic formatting for emphasis in specifications"

learning_objectives:
  - objective: "Create working hyperlinks to documentation and external resources"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Exercise includes at least one valid link that renders correctly"

  - objective: "Add images to markdown documents for visual communication (screenshots, diagrams, logos)"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Exercise includes at least one properly formatted image"

  - objective: "Apply bold and italic formatting to emphasize key terms and requirements"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Exercise uses emphasis formatting appropriately for critical terms"

cognitive_load:
  new_concepts: 3
  assessment: "3 new concepts: (1) link syntax, (2) image syntax, (3) emphasis syntax. Well within A2 limit of 7."
  mitigation_strategy: "Image syntax mirrors link syntax (just adds !). Emphasis uses simple asterisk patterns (*italic*, **bold**)."

differentiation:
  extension_for_advanced: "Research URL encoding for special characters in links; explore relative vs absolute image paths; learn strikethrough (~~text~~)"
  remedial_for_struggling: "Practice link syntax with provided URLs before finding own; use placeholder image services to avoid path issues"
---

# Links and Images

## Connecting Documents to the World

You've learned how to structure documents with headings, organize information with lists, and show code with fenced blocks. Now you'll learn the final elements that make your markdown documents truly useful: **links** to connect to external resources, **images** to show what things look like, and **emphasis** to highlight critical information.

These are the final syntax elements you need for writing effective markdown files like READMEs, CLAUDE.md instructions, and project documentation.

---

## Concept 1: Links - Connecting to Resources

A document doesn't exist in isolation. You often need to reference **external documentation**, **examples**, or **standards**. Links solve this problem.

### Why Links Matter

When you write "Use Python's requests library," the reader might not know:
- What is the requests library?
- Where do I find it?
- How do I use it?

But if you write "[Use Python's **requests** library](https://requests.readthedocs.io/)," the reader can click through to complete documentation instantly.

### The Syntax

Markdown links follow a simple pattern:

```text
[link text](url)
```

- **link text** = what the reader sees and clicks
- **url** = where the link goes

**What you type:**

```text
Read the [Python documentation](https://docs.python.org/) for help.
```

**What it renders as:**

Read the [Python documentation](https://docs.python.org/) for help.

### Common Mistake: Spaces in URLs Break Links

Beginner mistake:

```markdown
[Wrong link](https://docs.python.org/3/ reference guide)
```

This **won't work** because the space breaks the URL. Either:
1. Use a URL without spaces (recommended):
```markdown
[Python reference](https://docs.python.org/3/reference/)
```

2. Or use URL encoding (replace space with `%20`):
```markdown
[reference guide](https://docs.python.org/3/reference%20guide)
```

For documentation, **always stick with option 1** – find clean URLs without spaces.

### Common Mistake: Vague Link Text

Never use "click here" or "link" as your link text:

**Wrong:**
```markdown
For more information, [click here](https://docs.python.org/).
See the [link](https://requests.readthedocs.io/) for details.
```

**Correct:**
```markdown
See the [Python documentation](https://docs.python.org/) for more information.
The [requests library documentation](https://requests.readthedocs.io/) has examples.
```

**Why this matters for AI**: AI agents use link text to understand what the destination provides *without* following the link. `[Python documentation](...)` tells AI it's a language reference. `[click here](...)` provides zero context—AI must guess or follow the link (which it often can't do).

:::info[Expert Insight]
Links in specifications serve as **context anchors** for AI agents. When you link to library documentation, you're telling the AI: "This is the authoritative source for how this works." Some AI tools can fetch linked URLs to understand APIs better. Even when they can't, the link text provides semantic context—`[requests library](...)` tells the AI you're using the Python requests package, not just making generic "requests."
:::

---

## Example 1: Links to Documentation

Here's how to add helpful links to a README:

```markdown
# Weather App

## Required Libraries
- [Python requests library](https://requests.readthedocs.io/) - for making API calls
- [OpenWeatherMap API](https://openweathermap.org/api) - free weather data source

## Data Format
Data should be formatted as JSON. See the [JSON specification](https://www.json.org/) for details.

## Testing
Verify your app works like the examples in the [OpenWeatherMap docs](https://openweathermap.org/current).
```

Now readers can click through and see:
- How to use the requests library
- Where to get weather data
- What JSON looks like
- What sample outputs should look like

This **dramatically improves clarity** because you're not just describing, you're pointing to where readers can find more information.

:::tip[Pro-Tip: Reference-Style Links]
For documents with many links, markdown supports reference-style links that keep your text clean:

```text
Read the [Python docs][python] and [requests library][requests] documentation.

[python]: https://docs.python.org/
[requests]: https://requests.readthedocs.io/
```

The link definitions go at the bottom of your document. This is optional but useful for long documents.
:::

#### AI Colearning Prompt

> **Explore with your AI**: "I'm writing a README for a project that uses three external libraries. Can you show me how to format a 'Dependencies' section with links to each library's documentation? Use real library URLs."

---

## Concept 2: Images - Showing What Things Look Like

Sometimes words aren't enough. You need to **show** what something looks like. That's where images come in.

### Why Images Matter in Documentation

Images help readers understand:
- **What the UI looks like** - Screenshots show expected interface
- **How data flows** - Diagrams explain system architecture
- **Project branding** - Logos make READMEs professional

### The Syntax (Very Similar to Links!)

Markdown images use almost the same syntax as links, with one difference — an exclamation mark `!` at the start:

```text
![alt text](image-url)
```

- **alt text** = description of the image (shown if image doesn't load, read by screen readers)
- **image-url** = where the image is located (web URL or local file path)

**What you type:**

```text
![Python logo](https://www.python.org/static/community_logos/python-logo.png)
```

**What it renders as:**

![Python logo](https://www.python.org/static/community_logos/python-logo.png)

### Where Images Come From

**Option 1: Online images** (easiest for beginners)
Use a direct image URL from the web:

```markdown
![Example screenshot](https://example.com/screenshot.png)
```

**Option 2: Local images in your project**
Put images in a folder (like `images/` or `assets/`) and reference them with a relative path:

```markdown
![App screenshot](./images/screenshot.png)
```

**For beginners**: Start with online image URLs. Later you can add local images to your projects.

:::info[Expert Insight]
**Important for AI-native development**: Most AI agents cannot "see" images—they only read the alt text and filename. This means your alt text must be descriptive enough to convey what the image shows. Instead of `![screenshot](app.png)`, write `![Task list showing 3 pending items with checkboxes](app.png)`. Good alt text helps both accessibility and AI understanding.
:::

---

## Example 2: README with Images

Here's how images make READMEs more professional:

```markdown
# Weather Dashboard

![Weather Dashboard Screenshot](https://via.placeholder.com/800x400.png?text=Weather+Dashboard)

## Features
- **Display** current temperature and conditions
- **Show** 7-day forecast
- **Save** favorite locations

## Architecture

![System diagram](https://via.placeholder.com/600x200.png?text=User+→+API+→+Database)
```

See how images make it immediately clear what the app looks like and how it works? That's powerful.

### Common Image Mistakes

**Mistake 1: Forgetting the `!` at the start**

```markdown
[Missing exclamation](image.png)
```

This creates a *link* to the image, not an embedded image. Always use `![...]` for images.

:::tip[Quick Rule: Link vs Image]
- `[text](url)` = **Take me there** (clickable link)
- `![text](url)` = **Show it here** (embedded image)

The `!` means "display this content inline" rather than "navigate to this location."
:::

**Mistake 2: Broken image paths**

```markdown
![Screenshot](./images/screenshot.png)
```

If `screenshot.png` doesn't exist at that path, the image won't show. Check your paths!

**Mistake 3: Too many large images**

Don't embed 20 screenshots in one README. Use images strategically:
- 1 logo/banner at the top
- 1-2 key screenshots showing the app
- Diagrams only when words aren't enough

#### Practice Exercise

> **Ask your AI**: "I'm writing a README for a task management app. I want to show what the main interface looks like and a simple architecture diagram. Suggest what images I should include and help me write descriptive alt text for accessibility."

---

## Concept 3: Text Emphasis - Highlighting What Matters

Sometimes you need to draw attention to specific words or phrases within your text. Markdown provides two levels of emphasis: **bold** for strong emphasis and *italic* for lighter emphasis.

### The Syntax

**Bold** uses double asterisks or double underscores:

**What you type:**

```text
This requirement is **critical** for security.
This requirement is __critical__ for security.
```

**What it renders as:**

This requirement is **critical** for security.

**Italic** uses single asterisks or single underscores:

**What you type:**

```text
See the *optional* configuration section.
See the _optional_ configuration section.
```

**What it renders as:**

See the *optional* configuration section.

**Combined** (bold italic) uses triple asterisks:

**What you type:**

```text
***Never*** store passwords in plain text.
```

**What it renders as:**

***Never*** store passwords in plain text.

### When to Use Each

| Emphasis | Syntax | Use For |
|----------|--------|---------|
| **Bold** | `**text**` | Critical requirements, warnings, key terms |
| *Italic* | `*text*` | Optional items, definitions, slight emphasis |
| ***Both*** | `***text***` | Absolute requirements, security warnings |

### Example: Emphasis in Specifications

```markdown
## Security Requirements

- User passwords **must** be hashed before storage
- API keys should *never* be committed to version control
- All endpoints **require** authentication
- Rate limiting is *recommended* but optional for internal APIs

***Critical***: The database connection string contains credentials
and must be stored in environment variables, not in code.
```

:::info[Expert Insight]
Emphasis helps AI understand priority. When AI sees "**must**" vs "*recommended*", it can distinguish between hard requirements and nice-to-haves. Use bold for requirements that would cause implementation failure if missed, and italic for optional enhancements. This semantic distinction helps AI make appropriate trade-off decisions during implementation.
:::

### Common Emphasis Mistakes

**Mistake 1: Overusing bold**

If everything is bold, nothing stands out. Reserve bold for truly critical items.

**Mistake 2: Inconsistent emphasis for placeholders**

Don't use italic alone to indicate placeholders like *database_name*. Instead, use inline code with angle brackets: `<database_name>`. This is clearer for both humans and AI.

**Mistake 3: Using emphasis instead of structure**

If you're bolding entire sentences to make them stand out, consider using a heading or callout box instead. Emphasis is for words within sentences, not for creating document structure.

---

## Try With AI

Test your understanding of links and images by building a real README section.

### Setup
Use ChatGPT, Claude, or any AI companion you have available.

### Prompt 1 (Links Practice):

```
I'm writing a README for a Python weather app that uses the requests library
and the OpenWeatherMap API. Write me a "Getting Started" section that includes
links to the relevant documentation. Use proper markdown link syntax.
```

### Prompt 2 (Images Practice):

```
Now add an "Architecture" section to my weather app README. Include a placeholder
image showing the data flow (user → app → API → response). Use proper markdown
image syntax with descriptive alt text.
```

### Prompt 3 (Combined Practice):

```
Review this README section I wrote and suggest improvements to my links and images:

## Resources
- Python docs: https://docs.python.org
- API info at openweathermap.org

Screenshot:
[app screenshot](screenshot.png)

What markdown syntax errors did I make? Fix them for me.
```

---

## Practice Exercise: Task Tracker App (Part 4 - Links & Images)

**Continuing from Lesson 4**: Open your Task Tracker App specification. You'll now **add links and images** to complete your first full specification.

### Your Task for Lesson 5

Add links and images to finalize your Task Tracker App specification:

**Part 1: Add Resource Links**

Add a "Resources" or "Documentation" section with helpful links:

`````text
## Resources

- [Python Official Documentation](https://docs.python.org/) - Language reference
- [Python File I/O Tutorial](https://docs.python.org/3/tutorial/inputoutput.html) - For saving tasks to file
`````

**Part 2: Add a Placeholder Image (Online URL)**

Add a screenshot placeholder showing what your app's interface looks like:

`````text
## Screenshot

![Task Tracker main menu showing 5 options: Add Task, View Tasks, Mark Complete, Delete Task, and Exit](https://via.placeholder.com/600x300.png?text=Task+Tracker+Menu)
`````

**Part 3: Try a Relative Path (Local Image)**

In AI-native development, AI agents often create images (diagrams, charts) and save them locally. Practice referencing a local image:

1. Create an `images/` folder in your project
2. Add any image file (or create an empty placeholder)
3. Reference it with a relative path:

`````text
## Architecture Diagram

![Data flow diagram showing user input going to Task class then to file storage](./images/architecture.png)
`````

This prepares you for when AI generates diagrams and saves them to your project folder.

:::tip[Pro-Tip: Descriptive Alt Text]
Write alt text that describes what the image SHOWS, not just what it IS. "Task Tracker menu" is vague. "Task Tracker main menu showing 5 options" tells the reader (and AI) exactly what to expect.
:::

### Validation Checklist

Check your completed specification:

1. Has at least one working link to external documentation
2. Links use proper syntax: `[text](url)` with no spaces in URL
3. Link text is descriptive (not "click here" or "link")
4. Has at least one image with descriptive alt text
5. Image uses proper syntax: `![alt text](url)` with `!` at the start
6. Alt text describes what the image shows, not just what it is
7. (Bonus) Includes a relative path image reference like `./images/diagram.png`

---

## Why This Matters for AI

When you use links and images correctly in specifications, AI agents can:

1. **Follow documentation links** - Some AI tools fetch linked pages for additional context
2. **Understand resource relationships** - Link text tells AI what each resource provides
3. **Parse alt text for image context** - Since AI can't see images, descriptive alt text is critical
4. **Generate appropriate placeholders** - When AI creates documentation, it follows your link/image patterns

:::warning[AI Limitation]
Most AI agents cannot view images directly. They only see the alt text and filename. Always write alt text as if describing the image to someone who can't see it—because that's exactly what AI does.
:::

---

## Your First Complete Specification

**Congratulations!** You've now built a complete specification across Lessons 2-5.

Your Task Tracker App specification now has everything an AI agent needs to understand and implement your project:

- **Clear structure** (headings)
- **Organized requirements** (lists)
- **Concrete examples** (code blocks)
- **Supporting resources** (links)
- **Visual context** (images)

### What's Next?

In the **Chapter Quiz**, you'll test your markdown knowledge. Then you'll be ready to write specifications for your own projects—and have AI agents help you build them.
