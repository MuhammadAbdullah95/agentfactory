---
sidebar_position: 5
chapter: 6
lesson: 5
title: "Search & Discovery Workflow"
description: "Direct Claude Code to find files by description rather than memorizing search commands—because you know what you're looking for, not where it is"
duration_minutes: 25

skills:
  - name: "Descriptive File Search"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can describe files to find by characteristics rather than exact names"

  - name: "Search Refinement Direction"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can narrow search results through conversational refinement"

  - name: "Pattern Recognition Request"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can ask agent to find similar files based on discovered examples"

learning_objectives:
  - objective: "Direct Claude Code to find files by description instead of filename"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student locates a file by describing its content or purpose"

  - objective: "Refine search results through conversation"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student narrows from many candidates to the target file"

  - objective: "Request discovery of similar files"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student asks agent to find related files based on a found example"

  - objective: "Observe combined bash tools in agent workflow"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student identifies how agent combines find, grep, and pipes"

cognitive_load:
  new_concepts: 3
  concepts_list:
    - "Descriptive search (describing what, not how)"
    - "Search refinement (narrowing through conversation)"
    - "Pattern-based discovery (find similar files)"
  assessment: "3 concepts within A2 limit of 5"

differentiation:
  extension_for_advanced: "Ask Claude Code to create a search report showing all tax-related documents from the past 3 years, organized by year"
  remedial_for_struggling: "Start with a simple search: 'Find any PDF files in my Documents folder.' Then gradually add constraints like date or content."
---

# Search & Discovery Workflow

You downloaded a tax document last year. You know it exists. You just can't find it.

It's somewhere in your files. Maybe Downloads? Maybe Documents? The filename was something the bank generated automatically—`statement_2023_Q4_final_v2.pdf` or maybe `1099-DIV-2023.pdf`. You're not sure. You just know it was a tax document from 2023 and it had something about dividends.

You could click through folders for 20 minutes. Or you could describe what you're looking for to a General Agent and let it search.

---

## The Conversation

Open Claude Code. Describe the problem.

```
You: I'm looking for a tax document from 2023. It was a PDF, something
about dividends or 1099. I think I downloaded it from my bank. Can you
help me find it?
```

Watch what Claude Code does.

```
Claude Code: I'll search for that tax document. Let me check common
locations for downloaded PDFs related to taxes.

[Runs: find ~/Downloads ~/Documents -name "*.pdf" -newer "2023-01-01" ! -newer "2024-01-01" 2>/dev/null]
[Runs: find ~/Downloads ~/Documents -iname "*1099*" -o -iname "*tax*" -o -iname "*dividend*" 2>/dev/null]

I found several candidates:

| File                                | Location              | Modified    |
|-------------------------------------|-----------------------|-------------|
| 1099-DIV-2023-Fidelity.pdf          | ~/Downloads           | 2023-02-14  |
| 1099-INT-2023-Chase.pdf             | ~/Downloads           | 2023-01-28  |
| Tax-Summary-2023.pdf                | ~/Documents/Taxes     | 2023-04-12  |
| dividend-statement-Q4-2023.pdf      | ~/Downloads           | 2023-10-15  |
| W2-2023-Employer.pdf                | ~/Documents/Taxes     | 2023-02-01  |

The most likely match for "dividends or 1099" is:
  ~/Downloads/1099-DIV-2023-Fidelity.pdf

Is this the one you're looking for?
```

That's a lot of results. Let's narrow it down.

```
You: It was from my bank, not Fidelity. I think it was Chase or
Bank of America.
```

```
Claude Code: Let me narrow the search to bank-related documents.

[Runs: find ~/Downloads ~/Documents -iname "*chase*" -o -iname "*bofa*" -o -iname "*bankofamerica*" 2>/dev/null | xargs grep -l -i "1099\|dividend" 2>/dev/null]

Found these bank-related tax documents:

| File                               | Location      | Content Match          |
|------------------------------------|---------------|------------------------|
| 1099-INT-2023-Chase.pdf            | ~/Downloads   | Contains "1099-INT"    |
| Chase-Tax-Statements-2023.pdf      | ~/Documents   | Contains "dividend"    |

The Chase 1099-INT document looks like your best match.
Want me to open it so you can verify?
```

That's the one.

```
You: That's it! Actually, can you find all my Chase tax documents?
I want to see what else I have from them.
```

```
Claude Code: I'll find all Chase-related tax documents.

[Runs: find ~ -iname "*chase*" -type f \( -iname "*.pdf" -o -iname "*.PDF" \) 2>/dev/null]
[Runs: grep -r -l -i "chase.*1099\|chase.*tax\|chase.*statement" ~/Documents ~/Downloads 2>/dev/null]

Here's everything I found from Chase:

TAX DOCUMENTS:
  ~/Downloads/1099-INT-2023-Chase.pdf         (2023)
  ~/Downloads/1099-INT-2022-Chase.pdf         (2022)
  ~/Documents/Taxes/Chase-Year-End-2023.pdf   (2023)
  ~/Documents/Taxes/Chase-Year-End-2022.pdf   (2022)

OTHER CHASE FILES:
  ~/Downloads/Chase-Statement-Dec-2023.pdf    (statement)
  ~/Downloads/Chase-Statement-Nov-2023.pdf    (statement)

You have 4 tax documents and 2 regular statements from Chase.
Would you like me to organize these into a Chase-Taxes folder?
```

You went from "I can't find that tax document" to "here's everything from Chase" in three exchanges.

---

## What Just Happened?

You witnessed two principles working together.

**Principle 1: Bash is the Key.** Did you notice the commands the agent ran? It used `find` to locate files by name patterns, `grep` to search inside files for content, and `xargs` to pipe results between tools. You didn't need to know any of this syntax. The agent picked the right tools because bash commands are the universal interface for file operations.

**Principle 7: Observability.** The agent didn't just hand you a filename. It showed you the search process—what it searched for, where it looked, what it found. You could see the table of candidates and understand why it narrowed to certain files. The search was transparent.

Here's what made this different from a file browser search:

| Traditional Search         | Agent-Directed Search                    |
| -------------------------- | ---------------------------------------- |
| Type exact filename        | Describe what you're looking for         |
| One folder at a time       | Search multiple locations simultaneously |
| Match filename only        | Match content inside files               |
| Get list, you filter       | Agent filters and explains why           |
| You refine with new search | Agent refines through conversation       |

---

## The Pattern

Here's what made this work:

```
"Find files that match [description] from [time period]"
```

This pattern tells the agent:

1. What characteristics to look for (description)
2. When the file was created or modified (time period)
3. That you don't know the exact location

The agent will search broadly and then narrow based on your criteria.

The second key pattern:

```
"Find all similar files to this one"
```

Once you find one example, this request triggers a pattern-based search. The agent identifies characteristics of the found file and looks for others that match.

Together, these patterns turn "I can't find it" into "here's everything related."

---

## Why Description Beats Commands

Consider the mental load difference:

| Approach       | What You Need to Know            |
| -------------- | -------------------------------- |
| Manual `find`  | Exact syntax, flags, regex       |
| Manual `grep`  | Pattern matching, file piping    |
| Combined tools | How to chain commands with xargs |
| Agent-directed | What you're looking for          |

The agent knows `find -iname "*pattern*" -newer "date"`. The agent knows `grep -l -i "content"`. You know "it was a tax document from 2023 about dividends."

Your knowledge is valuable. The agent's command syntax knowledge is mechanical. The combination is powerful.

---

## Try It Yourself

Pick a search problem from your own files.

**Option 1: Lost Receipt**

```
I bought something online a few months ago and need the receipt for
a return. It was probably a PDF in my Downloads or email attachments.
The order was from Amazon, sometime in the last 6 months.
```

Watch how the agent searches both locations and looks for Amazon-related content.

**Option 2: Old Project Files**

```
I worked on a project last year that had "budget" in the filename.
It was probably a spreadsheet or document. Can you find all files
related to budget planning from 2023?
```

See how the agent handles multiple file types and date ranges.

**Option 3: Photo Hunt**

```
I took photos at a birthday party. They'd be JPG or PNG files from
sometime in March this year. Can you find large image files from
that time period?
```

Notice how the agent might use file size as an additional filter for photos.

---

## The Key Requests

Remember these phrases for search tasks:

| What You Want       | What to Say                                        |
| ------------------- | -------------------------------------------------- |
| Find by description | "Find files that match [description]"              |
| Add time constraint | "...from [time period]"                            |
| Search inside files | "...that contain [text]"                           |
| Find similar files  | "Find all similar files to this one"               |
| See search process  | "Show me where you're searching and what you find" |
| Narrow results      | "It was specifically from [source/context]"        |

You're not learning `find -mtime -30 -name "*.pdf" | xargs grep -l "pattern"`. You're learning how to describe what you need.

---

## What You're Building

By now in this chapter, you've learned:

| Lesson                    | Pattern                            | Principle                  |
| ------------------------- | ---------------------------------- | -------------------------- |
| 1. First Workflow         | "Help me understand"               | P7: Observability          |
| 2. Safety First           | "Back up before changing"          | P6: Constraints and Safety |
| 3. Categorize with Rules  | "Write rules first"                | P5: Persisting State       |
| 4. Batch Operations       | "Show me first, create a script"   | P2: Code as Interface      |
| **5. Search & Discovery** | **"Find files that match [desc]"** | **P1: Bash is the Key**    |

Each pattern expands your capability. You understand your files. You protect them with backups. You document your rules. You automate repetitive tasks. Now you find anything by describing it.

In the next lesson, you'll combine all these patterns into a complete file processing toolkit.

---

## Try With AI: Extended Practice

**Prompt 1: Multi-Criteria Search**

```
I need to find a document that meets multiple criteria:
- It's a PDF
- It contains the word "invoice" somewhere in the file
- It's from 2024
- The amount was over $500 (if you can search for that)

Show me your search strategy before running it.
```

**What you're practicing**: Complex search specification. You're asking the agent to combine multiple filters—file type, content, date, and even numeric values. Watch how it approaches an ambitious search request.

**Prompt 2: Search Report Generation**

```
Create a report of all tax-related documents I have, organized by year.
Include the filename, location, file size, and which year it's from.
Save the report so I can reference it later.
```

**What you're practicing**: Turning search into documentation. This request combines search (finding tax documents) with state persistence (saving a report). You're applying Principle 5 to search results.

**Prompt 3: Duplicate Detection**

```
I think I have duplicate files—the same document saved in multiple
places. Can you find files that might be duplicates based on name
similarity or identical file sizes?
```

**What you're practicing**: Advanced discovery. This asks the agent to find patterns across your filesystem, not just specific files. Watch how it approaches the comparison task.
