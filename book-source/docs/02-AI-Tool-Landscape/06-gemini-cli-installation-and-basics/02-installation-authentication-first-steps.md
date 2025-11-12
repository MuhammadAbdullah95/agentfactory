---
sidebar_position: 2
title: "Installing Gemini CLI and Having Your First Conversation"
duration: "25-30 min"
---

# Installing Gemini CLI and Having Your First Conversation

You've learned what Gemini CLI is and why you might want to use it. Now it's time to actually get it on your computer and have your first real conversation with your AI learning companion.

This lesson is similar to Chapter 5's installation lesson—we'll download the software, set it up, and make sure everything works. If you already completed Chapter 5, much of this will feel familiar!

---

## What is Node.js? (Start Here If New)

Before we can install Gemini CLI, we need to install something called **Node.js**. Let's clarify what that is.

**Node.js is software that helps other programs run on your computer.**

Think of it like this:
- Your computer has a core language it understands: zeros and ones (binary)
- Node.js is a translator that converts programmer instructions into things your computer can do
- Many modern tools (including Gemini CLI) need Node.js to run

**Why this matters:** Just like you need Java to play certain games, or .NET to run certain programs, we need Node.js to run Gemini CLI. It's not complicated—it's just a prerequisite.

**Do you already have Node.js?** Let's check in the next section.

---

## What You Need Before Starting

Let's verify you have everything needed. This takes 2 minutes.

### Requirement 1: Node.js

**What is it?** The translator software mentioned above—it lets Gemini CLI run on your computer.

**Do you have it?** Open your terminal and type:

```bash
node --version
```

**What you'll see:**

**If you see a version number** (like `v18.0.0` or `v20.0.0`):
```
v20.17.0
```

Great! You have Node.js. Skip the installation step below and go to "Step 1: Install Gemini CLI."

**If you see "command not found":**
```
command not found: node
```

Don't worry—we'll install it. See the installation instructions below.

### Installing Node.js (If You Don't Have It)

1. Go to https://nodejs.org
2. Download the **LTS version** (LTS stands for "Long-Term Support"—it's the stable, recommended version)
3. Run the installer and follow the steps (just click "Next" and "Install" for each step)
4. Restart your computer
5. Open a new terminal and type `node --version` again to confirm

**That's it!** Node.js is now installed.

---

### Requirement 2: Internet Connection

**What is it?** You need to be connected to the internet to download Gemini CLI and to authenticate.

**Do you have it?** If you're reading this, you do. ✓

---

### Requirement 3: Google Account

**What is it?** An email account from Google (Gmail). This is how Gemini CLI will know who you are.

**Do you have it?** If you have Gmail, YouTube, or Google Drive, you already have one. You can use any of these.

**Don't have one?** Go to https://accounts.google.com/signup and create one (takes 5 minutes).

---

## Step 1: Open Your Terminal

We're about to download and install Gemini CLI using a terminal command.

**Where is your terminal?**

**Windows:** Search "PowerShell" in your Start menu and open it

**macOS:** Press Cmd+Space, type "Terminal", press Enter

**Linux:** Press Ctrl+Alt+T (works on most Linux distributions)

Once you see the text prompt (like `$` or `>` at the end), you're ready.

---

## Step 2: Install Gemini CLI

Type this command into your terminal and press Enter:

```bash
npm install -g @google/gemini-cli
```

**What's happening?**
- `npm` is the installer program (came with Node.js)
- `install` means "download and set up"
- `-g` means "globally" (make it available from anywhere)
- `@google/gemini-cli` is the name of what we're installing

**What you'll see:**
Text will scroll by. This is normal. Wait for it to finish (usually 30-60 seconds). You'll see something like:

```
npm notice created a lockfile as package-lock.json
npm notice
npm notice
+ @google/gemini-cli@0.4.0
added 150 packages in 45.3s
```

**If you see "command not found: npm":**
Your Node.js installation didn't work correctly. Try these steps:
1. Restart your computer
2. Try `node --version` again
3. If it still doesn't work, ask your AI: "I installed Node.js but npm isn't available. How do I fix this?"

---

## Step 3: Verify Installation Worked

Let's check that Gemini CLI is ready:

```bash
gemini --version
```

**What you should see:**
```
0.4.0
```

Or:

```
Gemini CLI version 0.4.0
```

**What this means:** ✅ Installation successful! Gemini CLI is on your computer.

**If you see "command not found: gemini":**
- Wait 30 seconds (sometimes the terminal needs a moment)
- Close your terminal completely
- Open a new terminal window
- Try `gemini --version` again

Still not working? Ask your AI: "I installed Gemini CLI but get 'command not found'. What should I do?"

---

## Step 4: Start Gemini CLI

Now let's actually launch Gemini CLI. Type:

```bash
gemini
```

Press Enter and wait a moment.

---

## What Happens Next: The First-Time Setup

When you run Gemini CLI for the first time, it will ask you some questions. Don't worry—these are just setup choices.

### Question 1: Choose a Theme

```
Select theme:
  > Light
    Dark
    Solarized
```

Choose whichever you like. Use your arrow keys to move up/down, then press Enter to select.

**What this is:** This just changes the colors in your terminal. It doesn't affect how the AI works. You can change it later if you want.

---

### Question 2: Choose How to Log In

```
Choose authentication method:
  > Google login (free tier)
    Gemini API Key (requires setup)
```

**Select "Google login"** (the free option). Just press Enter—it's already selected.

**What this is:** This tells Gemini CLI how to recognize you. Using your Google account is the easiest way.

---

### Question 3: Complete Login in Your Browser

Your web browser will open automatically. You'll see Google's login page.

1. Enter your Google email address
2. Enter your password
3. You'll see a page that says "Gemini CLI wants to access your account"
4. Click the blue "Allow" or "Authorize" button

**Why this is safe:** Google is asking your permission. You're not giving Gemini CLI your password—you're just giving it permission to use your Google account. You can revoke this permission anytime.

---

## You're In!

After you click "Allow," your terminal will show:

```
Welcome! You're authenticated as: your-email@gmail.com

Type a question or use / for commands.

gemini>
```

The `gemini>` prompt means you're inside an interactive conversation with Gemini CLI. **You made it!**

---

## What You Can Do Now

You have three main abilities inside Gemini CLI:

### 1. Ask Questions

Just type normally. For example:

```
gemini> What is Python?
```

Gemini will explain Python in simple language. No special syntax needed—just ask.

---

### 2. Use Slash Commands (Starting with /)

Slash commands control your session. For example:

```
gemini> /stats
```

This shows how many questions you've asked and how many you can ask before hitting your limit.

---

### 3. Exit Anytime

Type:

```
gemini> /quit
```

Or press Ctrl+C twice to exit.

---

## Your First Real Conversation: Three Ways AI Helps

Let's understand the three different roles AI can play while helping you learn. Inside Gemini CLI, try asking these three different kinds of questions:

### Role 1: AI as Teacher (Teaching You New Things)

Ask Gemini to teach you something:

```
What is the difference between a file and a folder? Explain it like I've
never heard these terms before.
```

**What happens:** Gemini explains the concept clearly, probably with an analogy or example.

**What you learn:** Gemini is teaching you something new—this is AI as teacher.

---

### Role 2: AI as Student (You Teaching AI Your Preferences)

Tell Gemini how you like to learn:

```
I learn best through examples. When you answer my questions, please:
1. Give the main answer first
2. Then give a real-world example
3. Then tell me one thing that might trip me up

Can you do that?
```

**What happens:** Gemini says "Yes, I'll remember this" (or similar).

**What you learn:** You just taught AI your learning style, and AI is adapting to you. This is AI as student—it learns from you.

---

### Role 3: AI as Co-Worker (Working Together)

Work with Gemini to solve a problem:

```
I want to learn how to organize my computer's files. Let's work together:
1. First, explain why file organization matters
2. Then, ask me about my situation (how many files do I have?)
3. Based on my answer, suggest a system
4. Help me verify the system works

Let's talk through all of this together.
```

**What happens:** Gemini asks you questions, listens to your answers, and tailors suggestions to YOUR situation.

**What you learn:** This is AI as co-worker—neither commanding you nor just following orders, but working together as partners.

---

## Important: Three Slash Commands to Know

While you're in Gemini CLI, you can use slash commands to control your session. Here are the three most useful ones:

### Command 1: /help

```
gemini> /help
```

Shows every command available. Use this whenever you forget what you can do.

---

### Command 2: /stats

```
gemini> /stats
```

Shows how many questions you've asked and how many you can ask today. This helps you understand your "budget."

Example output:
```
Today's usage: 45 questions
Daily limit: 1,000 questions
Remaining: 955 questions
```

---

### Command 3: /quit

```
gemini> /quit
```

Exits Gemini CLI and returns you to your terminal. (Or just press Ctrl+C twice.)

---

## Common Issues and How to Fix Them

### Issue 1: "I typed `gemini` but nothing happened"

**Fix:**
1. Make sure you completed the installation (try `gemini --version` again)
2. Try restarting your terminal
3. If still stuck, ask your AI: "Gemini CLI won't start. What should I check?"

---

### Issue 2: "The login doesn't work—browser doesn't open"

**Fix:**
1. Copy the URL from the terminal into your browser manually
2. Complete the login
3. The terminal should recognize you after that

**Still stuck?** Ask your AI: "My Gemini CLI login isn't working. What's the issue?"

---

### Issue 3: "I got a permission error during installation"

**Fix:** Restart your terminal and try the installation command again. If it persists, ask your AI: "I got a permission error installing Gemini CLI. What's safe?"

---

## Before You Move to Lesson 3

You've now:
- ✅ Downloaded and installed Gemini CLI
- ✅ Logged in with your Google account
- ✅ Started your first conversation with Gemini
- ✅ Learned about three roles AI can play

**Before moving on**, try these two things:

**Activity 1: Ask Your Own Question**
Think of something you're curious about. Ask Gemini in the terminal. Notice how it explains things to you.

**Activity 2: Practice One Slash Command**
Try `/stats` or `/help`. Notice what information appears. This helps you understand how commands control your session.

---

## Try With AI: Your First Gemini CLI Learning Session

You're inside Gemini CLI now. Let's practice everything in one learning session.

### Exercise 1: Experience AI as Teacher (5 minutes)

Inside Gemini CLI, ask:

```
Explain what a "terminal" is. Use an analogy—what's a real-world
equivalent that would help me understand it?
```

**What you're learning:** How to ask for analogies helps you understand new concepts faster.

---

### Exercise 2: Experience AI as Student (5 minutes)

Now teach Gemini your learning style:

```
I'm a complete beginner learning about technology. When you help me:
1. Don't use technical jargon without explaining
2. Use real-world examples from everyday life
3. Ask me clarifying questions if I'm unclear

Will you remember this for our future conversations?
```

**What you're learning:** AI can be trained by you. Your preferences matter.

---

### Exercise 3: Experience AI as Co-Worker (5 minutes)

Work with Gemini on something practical:

```
I need to understand the difference between Gemini CLI and ChatGPT.
Let's work together:
- First, ask me: How much do I care about cost? Privacy? Learning?
- Then, based on my answers, recommend which tool fits better
- Explain your reasoning

Walk me through your thinking—don't just list answers.
```

**What you're learning:** This is how professional developers use AI—as a thinking partner, not just an answer machine.

---

### Safety Reminder

**Trust but verify.** When Gemini suggests something:
- Read it carefully
- Ask "Does this make sense?"
- Ask for clarification if you don't understand
- Verify it actually works

This habit keeps you safe and builds your critical thinking skills.

---

## Key Terms Review

**Terminal:** The text window where you type commands. Also called "command line" or "CLI."

**Node.js:** Software that helps programs like Gemini CLI run on your computer.

**npm:** The installer program that downloads and sets up software.

**Installation:** Downloading software and setting it up so you can use it.

**Authentication:** Telling Gemini CLI who you are (by logging in with your Google account).

**Slash command:** A command that starts with `/` to control your session (like `/help` or `/quit`).

**Context:** Everything Gemini remembers from your conversation.

---

**Ready for Lesson 3?** Next, you'll learn how to ask Gemini better questions and how to use special shortcuts to make your conversations more productive.
