---
title: "Links and Images"
description: "Adding hyperlinks and images to markdown documents for richer communication"
sidebar_label: "Links and Images"
sidebar_position: 5
chapter: 2
lesson: 5
duration_minutes: 30
proficiency: "A2"
concepts: 2

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

learning_objectives:
  - objective: "Create working hyperlinks to documentation and external resources"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Exercise includes at least one valid link that renders correctly"

  - objective: "Add images to markdown documents for visual communication (screenshots, diagrams, logos)"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Exercise includes at least one properly formatted image"

cognitive_load:
  new_concepts: 2
  assessment: "2 new concepts: (1) link syntax with text and URL, (2) image syntax with alt text and URL. Well within A2 limit of 7."
  mitigation_strategy: "Image syntax mirrors link syntax (just adds !), reducing cognitive load through pattern recognition."

differentiation:
  extension_for_advanced: "Research URL encoding for special characters in links; explore relative vs absolute image paths in project repositories"
  remedial_for_struggling: "Practice link syntax with provided URLs before finding own; use placeholder image services to avoid path issues"
---

# Links and Images

## Connecting Documents to the World

You've learned how to structure documents with headings, organize information with lists, and show code with fenced blocks. Now you'll learn two more elements that make your markdown documents truly useful: **links** to connect to external resources, and **images** to show what things look like.

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

```markdown
[link text](url)
```

- **link text** = what the reader sees and clicks
- **url** = where the link goes

Example:

```markdown
Read the [Python documentation](https://docs.python.org/) for help.
```

That renders as: Read the [Python documentation](https://docs.python.org/) for help.

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

```markdown
![alt text](image-url)
```

- **alt text** = description of the image (shown if image doesn't load, read by screen readers)
- **image-url** = where the image is located (web URL or local file path)

Example:

```markdown
![Python logo](https://www.python.org/static/community_logos/python-logo.png)
```

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

**What you're learning:** How to identify which resources deserve links and how to format them clearly.

### Prompt 2 (Images Practice):

```
Now add an "Architecture" section to my weather app README. Include a placeholder
image showing the data flow (user → app → API → response). Use proper markdown
image syntax with descriptive alt text.
```

**What you're learning:** How to use images to communicate system design visually.

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

**What you're learning:** How to spot and fix common link/image syntax errors — bare URLs without link formatting, and images missing the `!` prefix.
