---
sidebar_position: 2
title: "Getting Claude Code on Your Computer"
duration: "20-25 min"
---

# Getting Claude Code on Your Computer

You learned about Claude Code in Lesson 1—your new learning companion that lives in the terminal. Now it's time to bring it to your computer so you can actually start using it.

Think of this lesson like buying a book, opening the box, and taking it out of the packaging. It's three simple steps: install the software, log in so it recognizes you, and test that it works. By the end, Claude Code will be ready to answer your first question.

---

## What Will We Do in This Lesson?

By the end of 20 minutes, you'll have:

1. ✅ Downloaded and installed Claude Code (the application)
2. ✅ Logged in with a Claude account (so it knows who you are)
3. ✅ Tested that it works (asked Claude your first real question)

**You don't need any special knowledge** for these steps. All you need is:
- A computer (Windows, Mac, or Linux)
- An internet connection
- 20 minutes
- One question you want to ask Claude

---

## What Do We Mean by "Install"?

**Installation** means: downloading software and putting it on your computer so you can use it.

You've probably done this before:
- Download an app on your phone → tap "Install" → now you can use it
- Download software on your computer → run the installer → now you can use it

**Claude Code installation** works the same way. We'll download it and set it up in about 5 minutes.

---

## Step 1: Do You Already Have Node.js?

Before we install Claude Code, we need to check one thing: **Does your computer have Node.js?**

**What is Node.js?** It's software that helps other applications (like Claude Code) run. Think of it like an engine that powers an app.

**Do you have it?** Open your terminal and type this:

```bash
node --version
```

**What you'll see:**

**If you see a version number** (like `v18.0.0` or higher):
```
v18.17.0
```
Great! You already have Node.js. Skip to "Step 2: Choose an Installation Method" below.

**If you see "command not found":**
```
command not found: node
```
Don't worry. You need to install Node.js first. It takes about 5 minutes:

1. Go to https://nodejs.org
2. Download the "LTS" version (LTS means "long-term support"—it's the stable, recommended version)
3. Run the installer and follow the steps (just keep clicking "Next" if you're unsure)
4. Open a new terminal and type `node --version` again to confirm

**Why this matters:** Node.js is the engine that powers Claude Code. We need it first.

---

## Step 2: Choose an Installation Method

Claude Code can be installed in different ways. **Pick the ONE that matches your computer and comfort level:**

| Your Situation | Use This Method |
|---|---|
| You're on Mac or Linux and want the easiest way | Native Installer |
| You're on Windows | Windows Native Installer |
| You already use Homebrew for other software (Mac/Linux) | Homebrew |
| You're comfortable with npm and Node.js | npm |

---

## Installation Method: Native Installer (Easiest for Most People)

This is the most straightforward way. Copy-paste this command into your terminal and press Enter:

**On Mac or Linux:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**On Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**What just happened?** You downloaded and ran a special installer that automatically:
- Downloaded Claude Code
- Put it in the right place on your computer
- Made it available from your terminal

**How long does it take?** About 2-3 minutes, depending on your internet.

---

## Step 3: Verify the Installation Worked

Let's check that Claude Code is ready. Type this:

```bash
claude --version
```

**What you should see:**
```
2.0.35 (Claude Code)
```

(The version number might be different—that's fine. You just want to see a version number.)

**If you see a version number:** Perfect! Claude Code is installed. Go to Step 4.

**If you see "command not found":**
- Wait 1 minute (sometimes the terminal needs a moment to recognize the new software)
- Close your terminal completely
- Open a new terminal window
- Type `claude --version` again

---

## Step 4: Create a Claude Account (If You Don't Have One)

Claude Code needs to know who you are. This means you need a **Claude account**—think of it like logging into an app.

**Do you already have a Claude account?** Check here:
- Go to https://claude.ai
- Does it remember you (show "Signed in")? Yes → Skip to Step 5
- Does it ask you to sign in? No → Create a free account by clicking "Sign up"

**Creating a free account takes 2 minutes:**
1. Go to https://claude.ai
2. Click "Sign up"
3. Enter your email address
4. Follow the steps (they'll send you a confirmation email)
5. Done! You now have a Claude account

---

## Step 5: Log In Claude Code

Now we need to tell Claude Code: "Hey, use MY account to talk to Claude."

Type this in your terminal:

```bash
claude
```

**What you'll see:**
```
Select login method:
❯ 1. Claude account with subscription
  2. Anthropic Console account
```

**What this means:** Claude Code is asking: "Do you want to use your Claude.ai account, or do you have a different account?"

**What to do:** Press the down arrow until you see `Claude account with subscription` highlighted, then press Enter. (Or just type `1` and press Enter.)

**What happens next:**
- Your browser opens automatically
- You see a page asking: "Claude Code wants permission to use your account. Allow?"
- Click the big blue "Allow" or "Authorize" button
- A message appears saying "Success! You can close this window and go back to your terminal"

**Back in your terminal:**
- You should see: `Logged in as your-email@example.com`
- Press Enter when it asks you to

**Congratulations!** Claude Code now recognizes you. You're logged in.

---

## Step 6: Ask Claude Your First Question

Let's test that everything works. Think of ONE question you want to ask Claude. It can be anything:
- "What is a computer file?"
- "How do I organize folders?"
- "Explain this error message I found"
- "What should I learn next?"

Type this in your terminal:

```bash
claude "Your question here"
```

Example:
```bash
claude "What is a computer file?"
```

**Press Enter and wait.**

Claude will type out an answer, explaining your question in simple language. You might see Claude's answer appear one word at a time—that's normal.

**What just happened?**
1. You typed a question
2. Claude Code sent it to the Claude AI servers
3. Claude thought about your question
4. Claude sent back an answer
5. Claude Code showed you the answer in your terminal

This is your first real conversation with Claude as your learning companion.

---

## Troubleshooting: Common Issues

### Issue: "I get an error about permissions" (Windows)

**Error message might say:** `cannot be loaded because running scripts is disabled`

**Fix:** Copy this and paste it into PowerShell, then press Enter:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try the installation command again.

**Why this happens:** Windows is being extra careful about security. This tells Windows: "It's okay to run the installer from trusted sources."

---

### Issue: "The installation doesn't finish" or "Stuck for 10+ minutes"

**Fix:**
1. Press `Ctrl+C` (Control and C together) to stop the installation
2. Wait 10 seconds
3. Try the installation command again
4. If it still doesn't work, check your internet connection by opening a web browser and going to google.com

**Why this happens:** Sometimes the download gets interrupted by internet hiccups. It's safe to try again.

---

### Issue: "I typed `claude` but nothing happens"

**Fix:**
1. Make sure you closed and reopened your terminal after installation
2. Make sure you logged in (ran `claude` and went through the login steps)
3. Try typing just the command `claude` by itself to see what happens

---

## Pause and Reflect

**You've done it!** You installed Claude Code, logged in, and asked your first question. That's the hard part.

**Think about this:**
- In Lesson 1, you read about Claude Code
- Now, you have Claude Code actually on your computer
- In the next lesson, you'll learn how to use it as a true learning companion

**Before moving to Lesson 3**, take a moment to:
1. Ask Claude another question (about anything)
2. Notice how Claude responds to you personally
3. Think about: "What would I like to learn about technology?"

---

## Try With AI

You've installed and logged in. Now let's have your first real learning conversation.

### Prompt Set

**Prompt 1: Get to know your learning companion**

```bash
claude "I just installed you and I'm learning about computers/coding. What's ONE concept you think I should understand first? Explain it as simply as possible."
```

**What to expect:** Claude will suggest a foundational concept and explain it clearly for a beginner.

---

**Prompt 2: Ask about your own situation**

```bash
claude "I'm a complete beginner. What's the most important thing I should know before I start learning?"
```

**What to expect:** Claude will give you encouragement and guidance based on what beginners usually struggle with.

---

**Prompt 3: Practice asking questions**

Think of something you're curious about and ask:

```bash
claude "Explain [your topic] to someone who knows nothing about it"
```

Example topics:
- "What is the internet?"
- "How do websites work?"
- "What is programming?"
- "What's a database?"

**What to expect:** Claude explains the topic clearly without using confusing jargon.

---

### Safety Reminder

**Remember:** Claude is a tool you control. At any time, you can:
- Ask a new question (just type a new `claude` command)
- Close the terminal and start fresh
- Ignore a suggestion from Claude if it doesn't feel right

You're always in control.

---

## What's Next?

In Lesson 3, you'll learn:
- How to ask Claude questions that actually help you learn
- How Claude "sees" the files and folders on your computer
- How to work WITH Claude as a learning partner (not just asking questions)

Before Lesson 3, just keep using Claude to ask questions about things you're curious about. The more you practice asking, the better you'll get.

---

## Key Terms Review

**Terminal:** A text window where you type commands instead of clicking buttons.

**Install:** Download software and set it up so you can use it.

**Node.js:** Software that helps other applications run (like the engine in a car).

**Claude Account:** Your login identity that tells Claude who you are.

**Authenticate/Log In:** Telling a program "I'm [your name]" so it remembers you.

---

**Ready for Lesson 3?** Let's learn how to really work WITH Claude as your learning partner.