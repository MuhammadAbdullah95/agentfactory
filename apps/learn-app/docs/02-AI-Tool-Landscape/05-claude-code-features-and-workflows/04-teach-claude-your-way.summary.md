# Lesson 4 Summary: Teach Claude Your Way of Working

## Key Concepts

### 1. The Repetition Problem
Every time you re-explain preferences to Claude, you lose time and context. Skills eliminate this by encoding your style once, permanently.

### 2. Skills = Your Personal Style Guide
A skill captures how YOU approach specific tasks—your tone, structure, and preferences—so Claude creates output that sounds like you.

**Simple definition**: A skill is a folder of instructions that teaches Claude your way of doing things.

### 3. Generic vs. Personalized Output
- **Without skills**: "Here's a LinkedIn post about learning AI." (generic)
- **With skills**: "Here's a LinkedIn post that matches your friendly-professional tone, includes 2-3 emojis, and ends with an engagement question." (YOUR style)

### 4. Two Ways Skills Activate

| Method | How It Works | When to Use |
|--------|--------------|-------------|
| **Automatic** | Claude recognizes when your style applies | Normal workflow—just ask naturally |
| **Explicit** | You say "Use [skill-name]..." | When you want a specific skill for sure |

Both work! Explicit invocation is great for learning; automatic activation is convenient once you're comfortable.

### 5. Skills Are NOT Saved Prompts
- **Prompts**: Commands WHAT you want ("Write a blog post")
- **Skills**: Encode HOW you think about a task (your structure, preferences, quality criteria)

Prompts get you *a* result. Skills get you *your* result.

### 6. Python Requirements

| Category | Python Required? | Examples |
|----------|------------------|----------|
| **Communication Skills** | **No** | `internal-comms`, `brand-guidelines` |
| **Document Skills** | **Yes** | `docx`, `pdf`, `pptx`, `xlsx` |

Document skills run Python scripts locally on your machine. Without Python, use `internal-comms` and `brand-guidelines`—they work perfectly without any extra setup.

### 7. Skills Beyond Code
Skills work for any repeated task:
- Social media posts
- Study notes organization
- Email templates
- Meeting notes
- Project status updates

---

## Mental Models

### The Personal Assistant Model
- **Generic assistant**: Helps with anything but uses a default approach
- **Personal assistant who knows you**: Applies YOUR preferences automatically

Skills transform Claude from generic assistant to personal assistant.

### The Procedure Identification Test
If you've explained the same thing to Claude more than twice, and it's stable enough to document, it's a skill candidate.

---

## Hands-On: Skills Lab

1. Go to [github.com/panaversity/claude-code-skills-lab](https://github.com/panaversity/claude-code-skills-lab)
2. Click green **Code** button → **Download ZIP**
3. Extract and open folder in terminal
4. Run `claude`

**Try without a skill:**
> "Write a LinkedIn post about learning how to build software with AI Agents."

**Try with a skill:**
> "Use internal-comms and write a LinkedIn post about learning how to build software with AI Agents."

**Notice the difference**: The skill-enhanced output has personality, strategic emojis, and an engagement question.

**Skills to try now** (no Python needed):
- `internal-comms` — Status reports, newsletters, LinkedIn posts
- `brand-guidelines` — Apply brand colors and typography

**After installing Python** (Chapter 16):
- `docx`, `pdf`, `pptx`, `xlsx` — Document creation and manipulation

---

## Real Example: Study Notes Assistant

A skill that transforms messy lecture notes into structured study materials:

1. Ask for lecture topic
2. Request text content (typed notes, slide text, transcript)
3. Extract key concepts and definitions
4. Create summary with main points
5. Generate practice questions
6. Create quick review section
7. Save as organized markdown file

**The payoff**: 15 minutes after each lecture instead of hours before exams.

---

## Common Mistakes to Avoid

1. **Thinking skills are "saved prompts"** — Skills encode reasoning patterns, not just text to paste
2. **Only considering coding tasks** — Skills work for any repeated procedure
3. **Overcomplicating** — "LinkedIn posts: friendly tone, 2-3 emojis, end with question" is enough
4. **Fear of Python requirements** — Start with `internal-comms` and `brand-guidelines`, add document skills later

---

## Preparation for Next Lesson

Before the next lesson, identify one procedure you want to encode:

1. **When do I do this?** (trigger)
2. **How do I like it?** (your style)
3. **What makes it 'me'?** (distinctive elements)
4. **What should others know?** (pro tips)

Document your answers. This becomes raw material for your first skill.

---

## Quick Reference

**Skill**: Your personal style guide that Claude loads automatically (or on request)

**Key insight**: Prompts encode WHAT. Skills encode HOW.

**Two activation modes**: Automatic (Claude decides) or Explicit (you name it)

**Start now**: `internal-comms`, `brand-guidelines` (no Python needed)

**Add later**: `docx`, `pdf`, `pptx`, `xlsx` (after Chapter 16)
