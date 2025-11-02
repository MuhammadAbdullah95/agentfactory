---
sidebar_position: 2
title: "The Safety-First Dialogue Pattern"
chapter: 7
lesson: 2
duration_minutes: 35

skills:
  - name: "AI Communication Safety Protocols"
    proficiency_level: "A1"
    category: "Soft"
    bloom_level: "Understand"
    digcomp_area: "Safety"
    measurable_at_this_level: "Learner can identify and name the 5 steps of the safety pattern; understands sequence without applying yet"

  - name: "Verification and Validation Thinking"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Safety"
    measurable_at_this_level: "Learner can apply the pattern to a new task with AI guidance; asks clarifying questions before execution"

  - name: "Dialogue Comprehension"
    proficiency_level: "A1"
    category: "Soft"
    bloom_level: "Understand"
    digcomp_area: "Communication"
    measurable_at_this_level: "Learner can identify dialogue elements and recognize when conversation is following (or skipping) the pattern"

learning_objectives:
  - objective: "Identify the 5 steps of the safety pattern (Ask, Explain, Understand, Verify, Execute) in a provided dialogue"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Identification task: label steps in example dialogue; identify which step is missing in flawed example"

  - objective: "Apply the 5-step pattern to a new bash task with AI guidance"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Real dialogue with AI: follow all 5 steps in a new, unfamiliar task; demonstrate pausing for Explain and Verify"

  - objective: "Ask clarifying questions that reveal safety concerns before execution"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Question-writing exercise: generate 3+ valid clarifying questions that a learner should ask"

cognitive_load:
  new_concepts: 4
  assessment: "4 new concepts (5-step pattern, dialogue structure, safety verification, clarifying questions) within A1→A2 transition limit of 6 ✓"
---

# The Safety-First Dialogue Pattern

## The Most Important Skill You'll Learn This Lesson

Your AI companion is powerful and helpful. But power without safety is dangerous. This lesson teaches you a pattern that keeps you safe: a structured dialogue that ensures understanding BEFORE your AI executes anything.

This isn't about memorizing commands. It's not about understanding bash syntax. It's about having conversations that prevent mistakes.

Think of it this way: A surgeon doesn't just operate—they verify the patient is prepped correctly, they confirm the surgical site, they brief the team on the plan. This lesson teaches you to do the same before your AI takes any action.

By the end, you'll have a habit: **Never execute. Always understand first.**

---

## The 5-Step Safety Pattern

Every time you ask your AI to perform a bash operation, follow these 5 steps in order:

### Step 1: Ask
You make a request in plain, natural language. No bash syntax. No command flags. Just explain what you want to accomplish.

**Example**: "I want to back up my project files before I reorganize them."

### Step 2: Explain
Your AI explains what it WILL DO before executing anything. The explanation should include:
- What commands it will run
- What those commands will do
- What files or folders they'll affect
- Whether anything is being created, modified, or deleted

**Example from AI**: "Here's my plan: I'll create a backup folder called `my-project-backup`, copy all your project files into it, check that the copy worked, and then you can delete the original if you want."

### Step 3: Understand
You confirm: "I understand what you're about to do, and the plan makes sense to me."

If you DON'T understand any part, you don't say "yes." You move to Step 4 instead.

**Example**: "Okay, I get it. You're making a copy first, not moving the files. That's good."

### Step 4: Verify
You ask clarifying questions BEFORE your AI executes anything. This is where you catch problems.

Good questions to ask:
- "What does this flag do?" (if you don't understand a bash command)
- "Will this affect any other files?" (safety check)
- "Is there a way to undo this?" (escape route)
- "How long will this take?" (expectation setting)
- "Are you sure about the file path?" (double-check critical details)

**Example**: "Before we copy, tell me what `-r` means in that command. And how will I know the copy is successful?"

### Step 5: Execute
ONLY after Steps 1-4 are complete, your AI runs the command. You already understand the plan, so you can review the output with confidence.

**Example**: Your AI runs the commands, shows you the results, and confirms: "Done. You now have a backup folder with all your files."

---

## Real Dialogue: All 5 Steps Working Together

Here's a real conversation showing all 5 steps. Pay attention to where each step begins and ends.

**Step 1: You Ask (plain language, no commands)**

> You: "I want to delete the old test files from my project, but I need to be careful not to delete anything important. How would you do this safely?"

**Step 2: AI Explains (plan before execution)**

> Agent: "Here's what I'd do. First, I'd show you which files are called `test_*.py` or `*_test.py`—these are typically test files. I'd list them so you can see exactly what's there. Then I'd show you the file sizes so you confirm they're not important. Only after you approve, I'd delete those specific files. Sound good?"

**Step 3: You Understand (confirm)**

> You: "Yes, that makes sense. Show me the test files first so I can verify they're the ones I want to delete."

**Step 4: You Verify (ask safety questions)**

> Agent shows the list:
> ```
> test_auth.py (2.1 KB)
> test_database.py (3.4 KB)
> utils_test.py (1.2 KB)
> ```

> You: "Wait—I see `test_database.py`. Before we delete it, tell me if there's any code in there that I might need for reference. And can I recover these files if I change my mind later?"

> Agent: "`test_database.py` contains tests but not production code—the actual database logic is in `database.py` which we'll keep. The files will go to your Trash/Recycle Bin, so you can recover them within 30 days if needed."

> You: "Perfect. Now I'm confident. Let's delete them."

**Step 5: Execute (run commands)**

> Agent: "Deleting those 3 test files now..."
> ```
> $ rm test_auth.py test_database.py utils_test.py
> ```
> Agent: "Done. The test files have been deleted. You still have `database.py` and your production code intact."

---

## Key Principles for Each Step

The 5-step pattern above is your foundation. Here are critical principles to remember:

**Step 1 (Ask)**: Describe WHAT you want, not which commands to use. Let your AI decide the approach.

**Step 2 (Explain)**: Demand both words AND commands. If your AI says "I'll just handle it," that's a red flag.

**Step 3 (Understand)**: Make an active choice. If you don't understand, say so—that's not failure, it's smart.

**Step 4 (Verify)**: Ask safety questions about the command, about side effects, about recovery options. This is your most powerful step.

**Step 5 (Execute)**: Only after all 4 previous steps. And stay engaged—watch the output and confirm it matches the plan.

---

## What Happens When You Skip Steps?

Let's see what goes wrong when you don't follow the pattern.

### Example: Skipping Steps 2, 3, and 4 (Dangerous!)

**You**: "Delete everything in my old-projects folder."

**Agent** (skipping Explain, Understand, Verify): "Deleting... done."

```
$ rm -rf old-projects/
```

**Oh no!** What if `old-projects` contained important files? What if you meant a different folder? What if there was a subdirectory with something critical?

**If you'd followed the pattern**:

**You**: "Delete everything in my old-projects folder."

**Agent** (Step 2 - Explain): "I'll remove the entire old-projects directory using `rm -rf old-projects/`. This will delete the folder and everything in it permanently."

**You** (Step 3 - Understand): "I understand—you're deleting the whole folder."

**You** (Step 4 - Verify): "Wait, before you do that, show me what files are in there. I want to make sure there's nothing important."

**Agent**: Lists the contents, shows you what will be deleted.

**You**: "Actually, I see `important_data.csv` in there. Don't delete that. Let me move it first."

**You saved important data** just by asking questions before executing.

---

## Exercise 1: Identify the Pattern in a Dialogue

Read this dialogue and label which of the 5 steps are present. Which step is MISSING?

---

**You**: "I want to organize my Python files into a folder called `my-scripts`."

**Agent**: "I can help with that. I'll create a folder called `my-scripts` and move all your `.py` files into it."

**You**: "Okay, sounds good."

**Agent**: "Great. Running the commands now..."

```
$ mkdir my-scripts
$ mv *.py my-scripts/
$ ls my-scripts/
```

---

**Which steps are present?**
- Step 1 (Ask): ✓ Yes, you asked to organize files
- Step 2 (Explain): ✓ Yes, agent explained the plan
- Step 3 (Understand): ✓ Yes, you confirmed you understood
- Step 4 (Verify): ✗ **MISSING** — You didn't ask any clarifying questions
- Step 5 (Execute): ✓ Yes, the commands ran

**What's the problem with skipping Step 4?**

You didn't ask:
- "Will this move ALL `.py` files, including test files and configuration files I don't want moved?"
- "What if some `.py` files are in subfolders—will this affect them?"
- "Can I undo this if I change my mind?"

**Better dialogue with Step 4**:

> **You** (Step 4): "Before you move the files, tell me: will this move EVERY `.py` file in this folder, or just the ones in the current directory? And what if I have `.py` files in subfolders—will those move too?"

> **Agent**: "Good question. `mv *.py` will only move `.py` files in the current folder, not in subfolders. If you have Python files nested in subfolders, they'll stay where they are."

> **You**: "Hmm, I want to move all Python files including the ones in subfolders. What command would do that?"

> **Agent**: "For that, I'd use `find . -name "*.py" -exec mv {} my-scripts/ \;` which recursively finds all `.py` files and moves them."

> **You**: "Okay, use that command instead."

By asking Step 4 questions, you caught the problem and got a better solution.

---

## Exercise 2: Write Clarifying Questions

Here's an operation your AI suggests. You're at Step 4 (Verify). Write 3 clarifying questions you should ask BEFORE your AI executes the command.

---

**AI Suggests**: "I'll reorganize your project structure by renaming folders and moving files around."

**Write 3 questions you should ask**:

1. (Example answer): "Which folders are you planning to rename, and what are the new names? Show me the before and after."

2. Your question:

3. Your question:

4. Your question:

---

**Good questions to ask might include**:
- "Show me exactly which folders you'll rename and what the new names are."
- "How will this affect any existing code or imports that reference the old folder names?"
- "Can I undo this if it breaks something?"
- "Will this affect any configuration files or scripts that reference the old paths?"
- "How long will this take, and will I be able to work while you're doing it?"

**Bad questions (not safety-focused)**:
- "Why did you choose this structure?" ← Philosophical, not safety
- "Is this the best way?" ← Subjective

---

## Exercise 3: Build the Full Pattern

You want to accomplish this: **"Create backup of my code before I make changes"**

Write how the 5-step pattern should play out. What should happen at each step?

---

**Step 1 - You Ask**:
> Your request in plain English:

**Step 2 - Agent Explains**:
> What should the agent tell you?

**Step 3 - You Understand**:
> What would you say to confirm?

**Step 4 - You Verify**:
> What questions should you ask?

**Step 5 - Agent Executes**:
> What should happen?

---

**Model Answer**:

**Step 1**: "Make a backup of my entire project code. I want to be able to go back to this version if something breaks."

**Step 2**: "I'll create a timestamped folder like `project-backup-2025-11-02`, copy all your code files into it, and verify the copy completed successfully. I won't touch your original files."

**Step 3**: "Yes, I understand. You're creating a copy, not moving anything. I can still work with my original code."

**Step 4**:
- "Which files and folders will you copy? Will you include hidden configuration files?"
- "How big will the backup be? Is there enough disk space?"
- "If I need to restore from this backup later, how would I do that?"

**Step 5**: Agent executes the copy commands, shows the backup was created, and confirms success.

---

## Assessment

### Formative Check (During Lesson)

Answer these questions to check your understanding:

1. **What are the 5 steps in order?**
   - A) Ask, Explain, Understand, Verify, Execute
   - B) Ask, Verify, Explain, Understand, Execute
   - C) Ask, Execute, Verify, Explain, Understand
   - D) Execute, Ask, Explain, Understand, Verify

2. **Which step is MOST important to never skip?**
   - A) Ask (because you need to make a clear request)
   - B) Explain (because you need to understand the plan before executing)
   - C) Verify (because you need to ask safety questions)
   - D) All are equally important

3. **In Exercise 1, what problem did we catch by using Step 4?**
   - A) The AI doesn't know how to organize files
   - B) The command would move all files, including nested files the user might not want moved
   - C) The AI can't create folders
   - D) The user asked the wrong question

4. **When should you ask Step 4 (Verify) questions?**
   - A) During Step 2, while the agent is explaining
   - B) After Step 3, before the agent executes
   - C) After the agent executes, if something went wrong
   - D) You shouldn't ask questions; just trust the AI

### Summative Assessment (Practice with AI)

Follow the 5-step pattern in a real conversation with your AI tool:

1. Ask your AI to help you with a **file organization task** (create folders, move files, backup data—something real from your own work)
2. Have your AI explain the plan in detail
3. Confirm you understand
4. Ask at least 3 clarifying questions
5. Only after all 4 steps, have your AI execute

**Success criteria**:
- You explicitly go through all 5 steps
- Your Step 4 questions address safety concerns (can I undo? what will it affect? etc.)
- You demonstrate understanding by asking thoughtful follow-up questions
- You don't skip any steps, even if it feels like "extra work"

The pattern itself is more important than the specific task. You're building a habit that will protect you in every bash operation going forward.

---

## Try With AI

**Tool**: Claude Code, ChatGPT Code Interpreter, Gemini CLI, or your preferred AI tool

**Prompt 1** (Easy): "I want to clean up old files from my project. Use the 5-step pattern: Ask, Explain, Understand, Verify, Execute. Don't run anything until I've asked questions and confirmed I understand."

**Expected Outcome**: Your AI explains what it will do step-by-step. It pauses at Step 2 and waits for you to confirm (Step 3) before moving to Step 4. You ask at least 2-3 clarifying questions. Only after you approve does it execute.

---

**Prompt 2** (Medium): "Help me back up this project safely. Before you run any commands, walk me through the 5-step pattern. I'll ask questions at Step 4."

**Expected Outcome**: Your AI clearly labels each step. The dialogue reads naturally. You can see where you're pausing to ask questions before execution.

---

**Prompt 3** (Challenge): "I want to reorganize my project structure, but I'm worried about breaking things. Use the 5-step pattern. At Step 4, help me identify what safety questions I should ask."

**Expected Outcome**: Your AI doesn't just explain the plan—it helps you think about what could go wrong and what questions you should ask before proceeding.

---

**Optional Stretch**: Try the 5-step pattern with a task that feels risky or important to you. The goal is to build the habit so thoroughly that you naturally pause and verify before your AI executes anything.

**Safety Note**: This pattern exists because AI agents are powerful and can make mistakes. By asking questions before execution, you're not doubting your AI—you're being professional. Real software engineers verify before deploying to production. You're learning the same habit for your own work.

