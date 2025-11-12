---
sidebar_position: 6
title: "Extensions: Giving Gemini New Superpowers"
duration: "10-15 min"
---

# Extensions: Giving Gemini New Superpowers

So far, you've learned how to use Gemini CLI to have conversations and save your work.

But what if you want Gemini to do more? For example:
- Browse the web and read current information
- Connect to databases or services
- Integrate with tools your school or company uses

**Extensions are how you give Gemini these superpowers.**

---

## What is an Extension? (Start Here If New)

**An extension is a tool or plugin that you can connect to Gemini to expand what it can do.**

Think of extensions like apps on your phone:
- Your phone is useful by itself (calls, texts, camera)
- But when you add apps (maps, games, email), it becomes much more powerful
- Each app adds new capabilities

**Extensions work the same way with Gemini:**
- Gemini is useful by itself (conversations, answering questions)
- When you add extensions, it gains new powers (web browsing, database access, etc.)

---

## Real-World Examples

### Example 1: Web Browsing Extension

**Without extension:**
```
gemini> Find me the price of iPhone 16 at Best Buy

Gemini: I can't browse the web right now. I don't have
current pricing information.
```

**With web browsing extension:**
```
gemini> Find me the price of iPhone 16 at Best Buy

Gemini: [Uses web extension to search Best Buy]
The iPhone 16 is currently $799 at Best Buy.
```

The extension lets Gemini actually browse the web!

---

### Example 2: Database Extension

**Without extension:**
```
gemini> How many customers do we have?

Gemini: I can't access your database. I don't have that information.
```

**With database extension:**
```
gemini> How many customers do we have?

Gemini: [Uses database extension to query your system]
You have 15,342 active customers as of today.
```

The extension connects Gemini to your school or company's database!

---

## How Extensions Help You Learn

For beginners learning to code, extensions can be helpful because:

1. **They let Gemini access current information**
   - Instead of relying on Gemini's training data, it can look up current tutorials, documentation, or examples

2. **They let you practice with real tools**
   - You learn to use Google Search, GitHub, APIs—all through Gemini
   - Gemini acts as a helper while you practice real-world skills

3. **They make Gemini more useful for projects**
   - Working on a project that needs web data? Use the web extension
   - Want to automate file organization? Use the file system extension

---

## Built-In Extensions in Gemini CLI

Gemini CLI comes with some basic extensions already:

### Extension 1: Web Search

Lets Gemini search the internet for current information

```
gemini> Use web search to find how to learn Python for beginners

Gemini: [Searches the web]
Here are the top resources for learning Python...
```

---

### Extension 2: Web Fetching

Lets Gemini read content from web pages

```
gemini> Go to python.org and explain their learning resources

Gemini: [Fetches and reads python.org]
Python.org offers: Official documentation, tutorials...
```

---

### Extension 3: File System

Lets Gemini read files on your computer (safely)

```
gemini> Read my README.md file and suggest improvements

Gemini: [Reads your README.md]
Good structure! Here are improvements...
```

---

## How to Use an Extension

Extensions are simple to use. You don't need to "install" anything—they're built in!

### Method 1: Ask Gemini Directly

Just ask Gemini to use an extension:

```
gemini> Search the web for "best Python learning resources"
```

Gemini will use its web search extension automatically.

---

### Method 2: Check What Extensions Are Available

```
gemini> /tools
```

This shows you all available extensions/tools.

---

## Important: Extensions Are Optional

**You don't have to use extensions.** Gemini works great without them!

Extension are helpful when you:
- Need current information (stock prices, weather, latest tutorials)
- Want to connect to services you use (databases, APIs, file systems)
- Are building real-world projects

But for learning basic concepts, regular conversations are perfect.

---

## Safety First: Be Careful With Extensions

When you use extensions, Gemini may:
- Read files on your computer
- Search the internet
- Connect to services

**Always verify:**
- Is this website/service safe?
- Do I trust Gemini with this information?
- Is this information sensitive (passwords, secrets, etc.)?

**Never give extensions access to:**
- Passwords or API keys
- Personal financial information
- Company secrets

---

## Try With AI: Experience an Extension

Let's practice using a simple extension.

### Exercise 1: Web Search

In Gemini CLI:

```
gemini> Search the web for "what is HTML"

Gemini: [Uses web search extension]
[Shows search results about HTML]
```

**What you learn:** Gemini can fetch current information from the internet.

---

### Exercise 2: List Available Tools

```
gemini> /tools
```

You'll see all available extensions/tools.

---

### Exercise 3: Fetch a Web Page

```
gemini> Go to the Python.org website and tell me about their
learning section

Gemini: [Reads the page]
[Summarizes what it found]
```

**What you learn:** Gemini can read and understand web content.

---

## Key Terms Review

**Extension:** A tool that expands what Gemini can do (web browsing, database access, file reading, etc.)

**Web search:** An extension that lets Gemini search the internet

**Web fetching:** An extension that lets Gemini read content from web pages

**File system:** An extension that lets Gemini read files on your computer (safely)

**/tools:** A command that shows all available extensions

---

**Ready for Lesson 7?** In the final lesson, we'll wrap up everything you've learned about Gemini CLI and look ahead to what's next!
