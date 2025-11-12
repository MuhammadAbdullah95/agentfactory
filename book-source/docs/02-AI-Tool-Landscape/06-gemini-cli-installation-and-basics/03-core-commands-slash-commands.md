---
sidebar_position: 3
title: "Understanding Gemini CLI Commands: Slash Commands Explained"
duration: "20-25 min"
---

# Understanding Gemini CLI Commands: Slash Commands Explained

In Lesson 2, you learned how to install Gemini CLI and start a conversation. Now let's learn the special commands that help you control your conversations and keep Gemini working smoothly.

You don't need to memorize these commands. You just need to understand what they do and when to use them.

---

## What Are Slash Commands? (Start Here If New)

**Slash commands are special instructions that start with a `/` character.** They control how Gemini CLI behaves, rather than being questions you ask.

Think of them like this:
- **Regular question**: "What is Python?" → Gemini answers your question
- **Slash command**: `/help` → Gemini shows you what commands are available

**Why this matters:** Slash commands let you manage your conversation, check your limits, and control your session—without asking questions.

---

## The Three Most Important Commands

In daily use, you'll use three slash commands most often. Let's learn them:

### Command 1: /help

**What it does:** Shows you every command available in Gemini CLI

**When to use:** Whenever you forget what a command does or want to discover new commands

**How to use:**

Type this inside Gemini CLI:

```
gemini> /help
```

**What you'll see:**

A list of all available commands with descriptions:

```
Available commands:
  /help             Show this help message
  /stats            Check your token usage
  /memory show      Show what Gemini remembers
  /chat save        Save your conversation
  /chat resume      Bring back a saved conversation
  /quit             Exit Gemini CLI
  ... (and more)
```

**Pro tip:** If you ever get stuck or forget what to do, `/help` is your answer.

---

### Command 2: /stats

**What it does:** Shows you how many questions you've asked and how many you can ask today

**Why this matters:** Gemini CLI gives you 1,000 questions per day (on the free tier). `/stats` helps you understand your "budget."

**How to use:**

Type this inside Gemini CLI:

```
gemini> /stats
```

**What you'll see:**

```
Daily usage statistics:
  Questions asked today: 45
  Daily limit: 1,000 questions
  Questions remaining: 955
  Session duration: 1 hour 23 minutes
```

**What this means:**
- You've asked 45 questions so far today
- You can ask up to 1,000 per day (free tier limit)
- You have 955 questions left before hitting today's limit
- You've been using Gemini CLI for 1 hour 23 minutes

**Real-world example:**
```
You: [Working and asking questions all morning]

gemini> /stats
Daily usage statistics:
  Questions asked today: 127
  Daily limit: 1,000 questions
  Questions remaining: 873

You: Great! I still have plenty of questions left for the rest of the day.
```

---

### Command 3: /quit

**What it does:** Exits Gemini CLI and returns you to your regular terminal

**When to use:** When you're done using Gemini CLI

**How to use:**

Type this inside Gemini CLI:

```
gemini> /quit
```

**What happens:**

You'll exit Gemini CLI and see your regular terminal prompt again:

```
gemini> /quit
Goodbye!

$
```

**Alternative:** You can also press Ctrl+C twice to exit.

---

## Commands for Saving and Resuming Conversations

As you use Gemini CLI more, you'll start having longer conversations. Sometimes you'll want to save your progress so you can pick it back up later.

### Command 4: /chat save

**What it does:** Saves your current conversation so you can bring it back later

**When to use:**
- When you finish working on something
- Before starting a completely different topic
- At the end of the day (so you can continue tomorrow)

**How to use:**

Type this inside Gemini CLI:

```
gemini> /chat save my-project
```

The name after `/chat save` is your choice. Make it descriptive so you remember what you were working on.

**What you'll see:**

```
gemini> /chat save my-project
✓ Conversation saved as "my-project"
```

**Real-world example:**

Let's say you've been learning about files and folders, and you want to save your work:

```
gemini> I want to organize my computer. Can you help me understand file systems?

Gemini: [Long conversation about files, folders, and organization]

gemini> /chat save learning-file-system
✓ Conversation saved as "learning-file-system"
```

Now, whenever you want to continue this conversation, you can bring it back.

---

### Command 5: /chat resume

**What it does:** Brings back a saved conversation

**When to use:** When you want to continue a previous conversation

**How to use:**

Type this inside Gemini CLI:

```
gemini> /chat resume my-project
```

**What you'll see:**

```
gemini> /chat resume my-project
✓ Resuming conversation "my-project"

[Shows your previous conversation history]
```

**Real-world example:**

The next day, you want to continue learning about file systems:

```
gemini> /chat resume learning-file-system
✓ Resuming conversation "learning-file-system"

[Your previous conversation appears]

You: Now that I understand files and folders, how do I actually
create a folder on my computer?

Gemini: You can use the mkdir command...
```

Gemini remembers everything from your previous conversation and continues naturally.

---

## Commands for Managing Your Memory

Gemini CLI can remember facts about you and your work. These commands manage that memory.

### Command 6: /memory show

**What it does:** Shows everything Gemini currently remembers about you

**When to use:** When you want to see what context Gemini has

**How to use:**

Type this inside Gemini CLI:

```
gemini> /memory show
```

**What you'll see:**

```
Current memory/context:
  - User prefers learning with examples
  - User is a complete beginner
  - User likes clear explanations without jargon
```

**Why this matters:** Gemini uses this information to tailor its answers to YOU. If you told Gemini "I'm a beginner," it remembers that and explains things simply.

---

### Command 7: /memory add

**What it does:** Teaches Gemini a fact about you or your work

**When to use:** When you want Gemini to remember something important

**How to use:**

Type this inside Gemini CLI:

```
gemini> /memory add I prefer learning with real-world examples
```

**What you'll see:**

```
gemini> /memory add I prefer learning with real-world examples
✓ Added to memory
```

**Real-world example:**

```
gemini> /memory add I like explanations that start simple, then get more detailed

✓ Added to memory

You: Now explain what a database is

Gemini: A database is like a filing cabinet for digital information...
[Starts simple, building to more detail - exactly as you specified]
```

---

## Commands for Clearing and Fresh Starts

Sometimes you want to start completely fresh, without Gemini remembering your previous conversation.

### Command 8: /clear

**What it does:** Clears your current conversation and starts fresh

**When to use:** When you want to start learning about something completely different

**How to use:**

Type this inside Gemini CLI:

```
gemini> /clear
```

**What you'll see:**

```
gemini> /clear
✓ Conversation cleared

gemini>
```

**Important warning:** `/clear` erases your current conversation. If you want to keep it, use `/chat save` first!

**Safe workflow:**

```
gemini> /chat save old-topic
✓ Conversation saved as "old-topic"

gemini> /clear
✓ Conversation cleared

gemini> [Now you can start fresh on a new topic]
```

---

## Other Useful Commands

### /chat list

Shows all your saved conversations

```
gemini> /chat list
Saved conversations:
  - learning-file-system
  - my-project
  - python-basics
```

---

### /about

Shows information about Gemini CLI (version, etc.)

```
gemini> /about
Gemini CLI version 0.4.0
```

---

## Practical Command Workflow Example

Let me show you a realistic workflow using these commands:

### Day 1: Learning Python Basics

```
$ gemini

gemini> What is a variable in Python?

Gemini: A variable is like a labeled box...
[Long conversation about variables]

gemini> /chat save python-basics-variables
✓ Conversation saved as "python-basics-variables"

gemini> /stats
Daily usage: 32 questions remaining: 968

gemini> /quit
Goodbye!
```

### Day 2: Continuing Python

```
$ gemini

gemini> /chat resume python-basics-variables
✓ Resuming conversation "python-basics-variables"
[Your previous conversation reappears]

You: Now that I understand variables, what's a data type?

Gemini: Good progression! A data type tells Python what kind of information...
[Continues naturally from yesterday]

gemini> /chat save python-basics-data-types
✓ Conversation saved

gemini> /quit
```

---

## Key Principle: Commands Are Optional

**You don't have to use any of these commands if you don't want to.**

You can just ask questions directly:

```
gemini> What is a loop in Python?
```

Commands are tools that help when you need them:
- Need to see your daily limit? Use `/stats`
- Want to save your conversation? Use `/chat save`
- Forgotten a command? Use `/help`

But simple questions? Just ask!

---

## Try With AI: Practice Commands

Inside Gemini CLI, let's practice using these commands.

### Exercise 1: Explore /help (3 minutes)

Type:

```
gemini> /help
```

**What to look for:** Scroll through the list. Notice there are more commands than we covered. That's okay—you only need the main ones for now.

**Reflection:** "I see there are many commands, but I only use a few regularly. That's normal."

---

### Exercise 2: Check Your /stats (2 minutes)

Type:

```
gemini> /stats
```

**What to look for:** Your daily question count. If you haven't asked many questions yet, the number should be small.

**Reflection:** "I now understand my daily budget. I can ask 1,000 questions per day."

---

### Exercise 3: Save a Conversation (5 minutes)

Have a short conversation:

```
gemini> Explain what the internet is

Gemini: [Explains internet]

gemini> That was helpful. Let me save this.

gemini> /chat save understanding-internet
✓ Conversation saved as "understanding-internet"

gemini> /quit
```

---

### Exercise 4: Resume That Conversation (5 minutes)

Next time you run Gemini CLI:

```
$ gemini

gemini> /chat resume understanding-internet
✓ Resuming conversation "understanding-internet"

[Your previous conversation reappears]

You: Now explain how websites work

Gemini: [Builds on your previous conversation about the internet]
```

**What you learn:** Your conversation persists across sessions. Gemini remembers what you discussed.

---

## Common Beginner Questions

**Q: Do I have to save my conversations?**

A: No. If you don't save, they disappear when you exit. But saving is useful if you want to continue learning about the same topic later.

---

**Q: What if I forget the name I saved a conversation under?**

A: Use `/chat list` to see all saved conversations.

---

**Q: If I use `/clear`, can I get my conversation back?**

A: Only if you saved it with `/chat save` first. If you just used `/clear` without saving, it's gone.

---

**Q: Does `/memory add` change how Gemini works for everyone?**

A: No, it only affects YOUR sessions. Other people using Gemini won't see your personal preferences.

---

## Key Terms Review

**Slash command:** A command that starts with `/` to control Gemini CLI (like `/help` or `/quit`).

**/stats:** A command that shows you how many questions you've asked today and how many you have left.

**/chat save:** A command that saves your current conversation so you can continue it later.

**/chat resume:** A command that brings back a saved conversation.

**/memory add:** A command that teaches Gemini something about you or your preferences.

**/clear:** A command that erases your current conversation and starts fresh.

**/help:** A command that shows you all available commands and what they do.

**Daily limit:** The maximum number of questions you can ask in one day (1,000 on the free tier).

---

**Ready for Lesson 4?** Next, you'll learn about special files called GEMINI.md that help Gemini remember permanent information about your projects and preferences.
