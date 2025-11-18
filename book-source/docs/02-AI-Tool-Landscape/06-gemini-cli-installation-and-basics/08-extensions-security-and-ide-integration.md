---
sidebar_position: 8
chapter: 6
lesson: 8
duration_minutes: 35
title: "Gemini CLI Extensions"
cefr_level: A2
proficiency: Beginner
teaching_stage: 2
stage_name: "AI Collaboration"
cognitive_load:
  concepts_count: 6
  a2_compliant: true
learning_objectives:
  - id: LO1
    description: "Explain what extensions are and why they simplify sharing complete setups"
    bloom_level: "Understand"
    digcomp: "1.3 Managing data, information and digital content"
  - id: LO2
    description: "Install extensions from GitHub repositories using gemini extensions install"
    bloom_level: "Apply"
    digcomp: "3.1 Developing digital content"
  - id: LO3
    description: "Manage installed extensions using list, update, disable, and uninstall commands"
    bloom_level: "Apply"
    digcomp: "1.2 Evaluating data, information and digital content"
  - id: LO4
    description: "Understand extension structure (gemini-extension.json, commands/, GEMINI.md)"
    bloom_level: "Understand"
    digcomp: "1.3 Managing data, information and digital content"
  - id: LO5
    description: "Create a basic extension using gemini extensions new command"
    bloom_level: "Create"
    digcomp: "3.2 Integrating and re-elaborating digital content"
  - id: LO6
    description: "Evaluate when extensions are useful versus individual component setup"
    bloom_level: "Evaluate"
    digcomp: "5.2 Identifying needs and technological responses"
---

# Gemini CLI Extensions

You've built the perfect Gemini CLI setup over the past few weeks: Playwright MCP for web research, Context7 for documentation, three custom learning commands, and a GEMINI.md file with your study approach. Your study partner asks: "Can I get your setup?" You realize you'd need to send them a 15-step installation guide. In this lesson, you'll learn how extensions package everything into a single installable bundle—turning complex setup sharing into one command.

---

## The Problem: Setup Sharing is Complex

Imagine you've crafted an effective Gemini CLI learning environment. You want to share it with your study group (5 people).

### What Your Setup Contains

```
Your Gemini CLI Setup:
├── MCP Servers
│   ├── Playwright (for web research)
│   └── Context7 (for documentation)
├── Custom Commands
│   ├── /learn (explain topics simply)
│   ├── /quiz (generate practice questions)
│   └── /research (structured web searches)
├── GEMINI.md (learning context and standards)
└── Settings (configuration preferences)
```

### The Manual Sharing Process

**What you'd need to send your study partner**:

```markdown
SETUP GUIDE - FOLLOW CAREFULLY

Step 1: Install Playwright MCP
Run: gemini mcp add @playwright/mcp

Step 2: Install Context7 MCP
Run: gemini mcp add context7

Step 3: Create commands directory
Create folder: .gemini/commands/

Step 4: Download learn.toml
Copy this code → save as .gemini/commands/learn.toml
[paste 20 lines of TOML]

Step 5: Download quiz.toml
Copy this code → save as .gemini/commands/quiz.toml
[paste 25 lines of TOML]

Step 6: Download research.toml
Copy this code → save as .gemini/commands/research.toml
[paste 30 lines of TOML]

Step 7: Create GEMINI.md
Copy this → save as .gemini/GEMINI.md
[paste 50 lines of context]

Step 8: Restart Gemini CLI
Run: gemini
```

### What Goes Wrong

Reality check for your 5 study partners:

**Person 1**: Misses Step 3 (creates commands in wrong folder) → commands don't work
**Person 2**: Copies TOML with formatting errors → syntax errors
**Person 3**: Forgets to install Context7 → documentation commands fail
**Person 4**: Completes all steps but has older MCP versions → inconsistent behavior
**Person 5**: Succeeds but it takes 45 minutes → frustrated

**Two weeks later**: You improve the `/research` command. Now you need to send an update guide to all 5 people.

**The problems**:
- ❌ **Time-consuming**: 15+ manual steps per person
- ❌ **Error-prone**: Easy to miss steps or make typos
- ❌ **Version drift**: Everyone ends up with slightly different setups
- ❌ **Update nightmare**: Sharing improvements requires resending everything
- ❌ **Lost productivity**: Your group spends time on setup instead of learning

---

## The Solution: Extensions Package Everything

What if your study partners could get your entire setup with one command?

```bash
gemini extensions install https://github.com/yourname/study-tools
```

**That's exactly what extensions do.**

### What is a Gemini CLI Extension?

An **extension** is a **complete package** containing:

- ✅ **MCP servers** (with configurations)
- ✅ **Custom slash commands** (all `.toml` files)
- ✅ **Persistent context** (GEMINI.md files)
- ✅ **Settings** (environment variables, preferences)
- ✅ **Documentation** (how to use everything)

**Think of it like this**:
- **MCP server alone**: Single capability (e.g., web browsing)
- **Custom command alone**: One reusable prompt
- **Extension**: Complete, shareable environment (MCP servers + commands + context + settings)

### The Transformation

**Before extensions** (manual setup):
```
Time: 45 minutes per person
Errors: 60% of people hit issues
Updates: Resend entire guide
Result: Frustration, inconsistency
```

**With extensions**:
```bash
gemini extensions install https://github.com/yourname/study-tools
```

```
Time: 2 minutes per person
Errors: Near zero (automated installation)
Updates: gemini extensions update study-tools
Result: Everyone has identical, working setup
```

**The transformation**: 45 minutes → 2 minutes (22x faster), near-zero errors, instant updates.

---

## Part 1: Working with Extensions

### Installing Extensions

Extensions can be installed from GitHub repositories or local directories.

#### Install from GitHub

The most common way to install extensions:

```bash
gemini extensions install https://github.com/username/extension-name
```

**What happens**:
1. Downloads the extension from GitHub
2. Installs all MCP servers listed in the extension
3. Adds custom commands to your Gemini CLI
4. Loads GEMINI.md context files
5. Applies settings and configurations

**Example - Installing a learning tools extension**:
```bash
gemini extensions install https://github.com/learning-tools/ai-study-kit
```

**Success message**:
```
✓ Extension 'ai-study-kit' installed successfully
✓ Installed 2 MCP servers (playwright, context7)
✓ Added 3 custom commands (/learn, /quiz, /research)
✓ Loaded context from GEMINI.md

Restart Gemini CLI to use the extension.
```

#### Install from Local Directory

If you're developing an extension or have it downloaded locally:

```bash
gemini extensions install /path/to/extension-directory
```

This creates a copy in your extensions directory.

#### Advanced Installation Options

**Install specific version**:
```bash
gemini extensions install https://github.com/user/extension --ref v1.2.0
```

**Enable auto-updates**:
```bash
gemini extensions install https://github.com/user/extension --auto-update
```

**Include pre-releases**:
```bash
gemini extensions install https://github.com/user/extension --pre-release
```

**Skip confirmation prompt**:
```bash
gemini extensions install https://github.com/user/extension --consent
```

### Listing Installed Extensions

See all extensions you currently have:

```bash
gemini extensions list
```

**Example output**:
```
Installed Extensions:

1. ai-study-kit (v1.0.0)
   Location: ~/.gemini/extensions/ai-study-kit
   Status: Enabled
   MCP Servers: playwright, context7
   Commands: /learn, /quiz, /research

2. python-helpers (v2.1.0)
   Location: ~/.gemini/extensions/python-helpers
   Status: Disabled
   MCP Servers: python-executor
   Commands: /run-python, /test-code

3. web-dev-tools (v1.5.2)
   Location: ~/.gemini/extensions/web-dev-tools
   Status: Enabled (workspace only)
   MCP Servers: browser-tools
   Commands: /preview, /validate-html
```

**You can also list extensions from within Gemini CLI**:
```
/extensions list
```

This shows the same information in your active session.

### Updating Extensions

#### Update Single Extension

```bash
gemini extensions update ai-study-kit
```

**What this does**:
- Checks for new version in the original source (GitHub/local)
- Downloads the latest version
- Updates MCP servers, commands, and context
- Shows what changed

**Example output**:
```
Updating 'ai-study-kit'...
✓ Updated from v1.0.0 to v1.1.0

Changes:
+ Added new command: /flashcards
✎ Improved /quiz command with difficulty levels
✓ Updated Playwright MCP to latest version

Restart Gemini CLI to use updates.
```

#### Update All Extensions

```bash
gemini extensions update --all
```

Updates every installed extension to the latest version.

**When to update**:
- Extension creator announces new features
- Bug fixes are released
- MCP servers need updating
- You see "Update available" message

### Disabling Extensions

Sometimes you want to temporarily disable an extension without uninstalling it.

#### Disable Everywhere

```bash
gemini extensions disable ai-study-kit
```

The extension stays installed but won't load in any session.

#### Disable in Current Workspace Only

From inside your project directory:

```bash
gemini extensions disable ai-study-kit --scope workspace
```

**Use case**: "I want the study extension for personal learning, but not when working on client projects."

### Enabling Extensions

Re-enable a disabled extension:

```bash
gemini extensions enable ai-study-kit
```

Or enable just for current workspace:

```bash
gemini extensions enable ai-study-kit --scope workspace
```

### Uninstalling Extensions

Remove an extension completely:

```bash
gemini extensions uninstall ai-study-kit
```

**What gets removed**:
- ✓ The extension directory
- ✓ MCP servers installed by the extension (if not used elsewhere)
- ✓ Custom commands from the extension

**What stays**:
- ✓ Any work you created using the extension
- ✓ Your personal GEMINI.md files (not part of the extension)
- ✓ Your settings.json configurations

---

## Part 2: Understanding Extension Structure

When you install an extension, it creates a directory with a specific structure. Let's understand what's inside.

### Extension Directory Layout

```
ai-study-kit/
├── gemini-extension.json    ← Configuration (what's included)
├── GEMINI.md                 ← Context for AI (optional)
├── commands/                 ← Custom slash commands
│   ├── learn.toml
│   ├── quiz.toml
│   └── research/             ← Nested commands
│       └── web.toml          ← Creates /research:web
├── docs/                     ← Documentation (optional)
│   └── README.md
└── .env                      ← Settings (created on install)
```

### The Configuration File: `gemini-extension.json`

This is the heart of every extension. It tells Gemini CLI what to install and how.

**Basic example**:
```json
{
  "name": "ai-study-kit",
  "version": "1.0.0",
  "description": "Tools for learning with AI assistants",

  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  },

  "contextFileName": "GEMINI.md"
}
```

**What each part means**:

**`name`** (required): The extension's unique identifier
- Must be lowercase with dashes (not spaces or underscores)
- How users refer to the extension
- Example: `"ai-study-kit"` not `"AI Study Kit"`

**`version`** (required): Current version number
- Format: `"1.0.0"` (major.minor.patch)
- Used for update checking
- Increment when you make changes

**`description`** (optional): What the extension does
- Brief explanation for users
- Shows in extension lists

**`mcpServers`** (optional): MCP servers to install
- Each server has a name (key) and configuration (value)
- Server configuration includes:
  - `command`: How to run the server
  - `args`: Arguments to pass
  - `cwd`: Working directory (optional)

**`contextFileName`** (optional): Context file to load
- Defaults to `GEMINI.md` if present
- Can specify different name: `"contextFileName": "LEARNING_CONTEXT.md"`

### MCP Server Configuration

Extensions can include multiple MCP servers:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "context7": {
      "command": "npx",
      "args": ["context7"]
    },
    "filesystem": {
      "command": "node",
      "args": ["${extensionPath}${/}server${/}filesystem.js"],
      "cwd": "${extensionPath}"
    }
  }
}
```

**Using variables**:
- `${extensionPath}`: Full path to the extension directory
- `${workspacePath}`: Full path to current workspace
- `${/}` or `${pathSeparator}`: Path separator (/ on Mac/Linux, \ on Windows)

**Example variable usage**:
```json
"args": ["${extensionPath}${/}dist${/}server.js"]
```

On Mac/Linux becomes: `/Users/you/.gemini/extensions/ai-kit/dist/server.js`
On Windows becomes: `C:\Users\you\.gemini\extensions\ai-kit\dist\server.js`

### Custom Commands

Extensions automatically include any `.toml` files in the `commands/` directory.

**Flat structure**:
```
commands/
├── learn.toml      → /learn
├── quiz.toml       → /quiz
└── research.toml   → /research
```

**Nested structure**:
```
commands/
├── study/
│   ├── plan.toml   → /study:plan
│   └── review.toml → /study:review
└── code/
    ├── debug.toml  → /code:debug
    └── test.toml   → /code:test
```

**Command naming**:
- Top-level files: `/commandname`
- Nested in folders: `/folder:commandname`

### The GEMINI.md Context File

Extensions can include a `GEMINI.md` file that provides persistent context to the AI.

**Example - Learning extension context**:
```markdown
# AI Study Tools Context

You are helping a student learn new topics. When using commands from
this extension, follow these guidelines:

## For /learn command:
- Explain concepts in simple, beginner-friendly language
- Use analogies and real-world examples
- Include 3-4 practical examples
- Avoid jargon unless you explain it first

## For /quiz command:
- Generate 5 multiple-choice questions
- Include questions at different difficulty levels
- Provide explanations for correct answers
- Encourage learning from mistakes

## For /research command:
- Use Playwright to browse actual documentation
- Summarize key information clearly
- Include links to original sources
- Highlight what's most relevant for beginners
```

**When this loads**: The AI will follow these guidelines automatically when you use extension commands.

### Extension Settings

Extensions can request settings from users during installation.

**In `gemini-extension.json`**:
```json
{
  "settings": [
    {
      "name": "API Key",
      "description": "Your API key for the documentation service",
      "envVar": "DOCS_API_KEY",
      "sensitive": false
    }
  ]
}
```

**On installation**, Gemini CLI prompts:
```
Extension 'doc-tools' requires settings:

API Key: Your API key for the documentation service
Enter value: [user types key]

✓ Settings saved to ~/.gemini/extensions/doc-tools/.env
```

**The `.env` file**:
```bash
DOCS_API_KEY=your-key-here
```

---

## Part 3: Creating Your First Extension

Now that you understand extensions, let's create one. Gemini CLI includes templates to get started quickly.

### Using the Template Generator

Gemini CLI provides example templates to start from:

```bash
gemini extensions new /path/to/my-extension [template]
```

**Available templates**:
- `context`: Extension with just a GEMINI.md file
- `custom-commands`: Extension with example commands
- `mcp-server`: Extension with an MCP server
- `exclude-tools`: Extension that restricts tool access

### Creating a Simple Learning Extension

Let's create an extension for your personal learning workflow.

**Step 1: Generate the template**

```bash
mkdir ~/my-learning-extension
cd ~/my-learning-extension
gemini extensions new . custom-commands
```

**What this creates**:
```
my-learning-extension/
├── gemini-extension.json
├── commands/
│   └── example.toml
└── package.json
```

**Step 2: Edit the configuration**

Open `gemini-extension.json`:

```json
{
  "name": "my-learning-tools",
  "version": "1.0.0",
  "description": "Personal AI learning commands"
}
```

**Step 3: Create your first command**

Create `commands/explain.toml`:

```toml
description = "Explain a topic in simple terms with examples"

prompt = """
Explain {{args}} in simple, beginner-friendly language.

Include:
1. What it is (one sentence)
2. Why it matters (practical benefits)
3. How it's used (3-4 real examples)
4. Common misconceptions (what beginners often misunderstand)

Use analogies and avoid jargon. If you must use technical terms, define them first.
"""
```

**Step 4: Test locally**

Link the extension for testing:

```bash
gemini extensions link .
```

Restart Gemini CLI:
```bash
gemini
```

Try your new command:
```
/explain APIs
```

**Step 5: Add more commands**

Create `commands/summarize.toml`:

```toml
description = "Summarize documentation clearly"

prompt = """
I'm reading about {{args}}.

Please:
1. Summarize the key concepts (3-5 bullet points)
2. Identify what's most important for beginners
3. Note any prerequisites I should learn first
4. Suggest 2-3 hands-on ways to practice

Keep it concise and actionable.
"""
```

**Step 6: Share with others**

Once you're happy with your extension:

1. Create a GitHub repository
2. Push your extension files
3. Share the install command:
   ```bash
   gemini extensions install https://github.com/yourname/my-learning-tools
   ```

### Creating an Extension with MCP Server

Let's create a more advanced extension that includes an MCP server.

**Step 1: Generate MCP template**

```bash
gemini extensions new ~/research-extension mcp-server
```

**What you get**:
```
research-extension/
├── gemini-extension.json
├── example.ts              ← TypeScript MCP server code
├── package.json
└── tsconfig.json
```

**Step 2: Review the configuration**

`gemini-extension.json`:
```json
{
  "name": "research-extension",
  "version": "1.0.0",
  "mcpServers": {
    "nodeServer": {
      "command": "node",
      "args": ["${extensionPath}${/}dist${/}example.js"],
      "cwd": "${extensionPath}"
    }
  }
}
```

**Step 3: Build the server**

```bash
cd ~/research-extension
npm install
npm run build
```

This compiles `example.ts` → `dist/example.js`

**Step 4: Link and test**

```bash
gemini extensions link .
```

Restart Gemini CLI and the MCP server will be available.

### Updating Your Extension

When you make changes to a linked extension:

**Option 1: Already linked** (changes apply immediately after restart)
```bash
# Edit your files
# Restart Gemini CLI - changes are live
gemini
```

**Option 2: Installed (not linked)**
```bash
gemini extensions update my-learning-tools
```

---

## Part 4: When to Use Extensions

Extensions are powerful, but not always necessary. Here's when they make sense.

### ✅ Use Extensions When:

**Sharing with multiple people**:
- Study group needs same setup (5+ people)
- Course providing standard environment for students
- Team wants consistent tooling
- Open source project recommending configurations

**Example**: "Our Python course uses 3 MCP servers and 8 custom commands. Instead of a 20-step setup guide, students run one install command."

**Complex setup with many components**:
- 3+ MCP servers
- 5+ custom commands
- Specific context requirements
- Environment settings needed

**Example**: "My web development setup has Playwright MCP, browser tools, 10 HTML/CSS commands, and framework-specific context. Extension packages it all."

**Need version control and updates**:
- Setup will improve over time
- Users need updates easily
- Want to track changes
- Need rollback capability

**Example**: "I improve my learning commands every week. Extension users get updates with one command instead of re-downloading files."

**Collaboration with specific context**:
- AI needs domain-specific instructions
- Special prompting guidelines
- Consistent behavior across team
- Shared knowledge base

**Example**: "Our research team needs AI to follow specific citation formats and source evaluation criteria. The extension's GEMINI.md ensures consistency."

### ❌ Don't Use Extensions When:

**Simple, exploratory setup**:
- Trying one MCP server
- Testing a single command
- Experimenting with configurations
- Personal, changing workflow

**Example**: "I'm trying different MCP servers to see which I like. I'll install them individually for now."

**Solo user, no sharing**:
- Only you will use it
- No collaboration planned
- Setup rarely changes
- Don't need version control

**Example**: "These commands are just for me and I change them frequently based on my current projects."

**Temporary/one-time use**:
- One-off project
- Short-term experiment
- Testing before committing
- No maintenance needed

**Example**: "I need Playwright MCP for this one research project. I'll install it directly."

---

## Common Questions

### Can I use multiple extensions together?

Yes! Extensions compose nicely:

```bash
gemini extensions install https://github.com/user/study-tools
gemini extensions install https://github.com/team/code-helpers
gemini extensions install https://github.com/org/research-kit
```

All three work simultaneously, combining:
- All MCP servers from each
- All commands from each
- All context files (merged)

### What if extensions conflict?

**Command name conflicts**:
If two extensions define `/learn`, the second one wins. You can:
- Disable one extension
- Ask extension creator to rename command
- Access first extension's command via: `/extension-name.learn`

**MCP server conflicts**:
If two extensions configure the same MCP server name, your `settings.json` wins (takes precedence over extensions).

### How do updates work?

**For GitHub extensions**:
```bash
gemini extensions update extension-name
```
- Checks GitHub for new version
- Downloads if version number increased
- Applies changes automatically

**For local extensions**:
```bash
gemini extensions update extension-name
```
- Copies latest files from original location
- Updates if `version` field increased

**Auto-update** (if enabled during install):
- Checks for updates on Gemini CLI startup
- Prompts to update if new version available

### How do I know what an extension does?

Before installing:

1. **Visit the GitHub repository**
2. **Read the README.md** (extension documentation)
3. **Check `gemini-extension.json`**:
   - What MCP servers it installs
   - What commands it provides
   - What context it loads

**Ask AI** (if you trust the source):
```
I'm considering installing this extension: [URL]
What capabilities would it add to you? What MCP servers and commands are included?
```

### Can I modify an extension after installing?

Extensions install to `~/.gemini/extensions/extension-name/`

**But**: Changes get overwritten on update.

**Better approach**:
1. **Fork the extension** on GitHub
2. **Make your changes** in your fork
3. **Install from your fork**:
   ```bash
   gemini extensions install https://github.com/yourname/forked-extension
   ```

Or:

1. **Keep extension as-is**
2. **Add personal overrides** in workspace:
   - Project-specific GEMINI.md (adds to extension context)
   - Additional commands in `.gemini/commands/`
   - Settings in workspace `settings.json`

---

## Troubleshooting

### "Extension installation failed"

**Check**:
1. Is the GitHub URL correct?
   - Format: `https://github.com/username/repo`
   - Not: `github.com/username/repo` (missing https://)
2. Is the repository public or do you have access?
3. Is your internet connection working?
4. Do you have `git` installed?

**Install git if needed**:
- Mac: `brew install git`
- Ubuntu: `sudo apt install git`
- Windows: Download from git-scm.com

**Try again**:
```bash
gemini extensions install <url> --consent
```

### "Extension installed but commands not working"

**Check**:
1. Did you restart Gemini CLI after installing?
   ```bash
   # Exit current session, start new one
   gemini
   ```

2. Is the extension enabled?
   ```bash
   gemini extensions list
   # Look for "Status: Enabled"
   ```

3. Are you typing the command correctly?
   ```bash
   /learn Python    ← Correct
   /learn python    ← Might work (case insensitive)
   learn Python     ← Won't work (missing /)
   ```

4. Check available commands:
   ```
   /help
   # Scroll to bottom - extension commands listed
   ```

### "MCP server from extension not available"

**Restart required**: MCP servers load on startup, not mid-session.

```bash
# Exit and restart
gemini
```

**Check installation**:
```
/extensions list
```

Look for "MCP Servers: [server-name]"

**Check MCP server itself**:
```bash
gemini mcp list
```

Should show the MCP server from the extension.

### "Extension update does nothing"

**Version must increase**: Update only works if the extension's `version` field increased.

**Check current version**:
```bash
gemini extensions list
```

**Check if source has newer version**: Look at the extension's `gemini-extension.json` on GitHub.

**Force reinstall**:
```bash
gemini extensions uninstall extension-name
gemini extensions install <url>
```

---

## Try With AI

Now let's practice working with extensions collaboratively. These prompts guide you through understanding, evaluating, and creating extensions with AI as your co-learner.

### 🔍 Understanding Extension Structure

Use this to explore what's inside an extension and how it works:

> "I'm looking at a Gemini CLI extension repository. Here's its `gemini-extension.json`:
>
> ```json
> {
>   "name": "research-tools",
>   "version": "2.0.0",
>   "mcpServers": {
>     "playwright": {
>       "command": "npx",
>       "args": ["@playwright/mcp@latest"]
>     },
>     "context7": {
>       "command": "npx",
>       "args": ["context7"]
>     }
>   },
>   "contextFileName": "RESEARCH_GUIDE.md"
> }
> ```
>
> Walk me through what this extension provides:
> 1. What MCP servers will be installed?
> 2. What capabilities will you gain?
> 3. What happens with RESEARCH_GUIDE.md?
> 4. Is there anything I should verify before installing?
>
> Then, help me understand: if I install this and later find an extension with better research tools, can I uninstall this one safely?"

**Expected outcome**: Clear explanation of extension components, installation effects, and management implications.

**Three Roles in action**:
- 🎓 **AI teaches**: Explains each part of the configuration
- 📚 **You teach AI**: Provide your specific use case (research needs)
- 🤝 **Co-work**: Together evaluate if this extension suits your needs

---

### 🛠️ Creating Your Personal Extension

Use this to design and build a custom extension for your workflow:

> "I want to create a personal learning extension for studying Python. My workflow includes:
> - Researching topics on official Python docs
> - Creating study plans for new concepts
> - Generating practice exercises
> - Reviewing code examples
>
> Help me design an extension step-by-step:
>
> **Step 1**: What should I name it (remember naming rules)?
>
> **Step 2**: Which MCP servers would be useful? (I'm thinking Playwright for browsing docs and Context7 for getting latest documentation)
>
> **Step 3**: What custom commands should I include? Help me design 3 commands:
> - One for research (with web browsing)
> - One for study planning
> - One for practice exercises
>
> **Step 4**: What should go in my GEMINI.md context file to make you better at helping me learn Python?
>
> **Step 5**: Write the complete `gemini-extension.json` file for me.
>
> **Step 6**: Write one of the command `.toml` files (your choice of which would be most useful).
>
> As we go, explain your choices so I understand the design decisions."

**Expected outcome**: Complete, functional extension design tailored to your learning needs with explanations for each component.

**Three Roles in action**:
- 🎓 **AI teaches**: Suggests best practices for extension design
- 📚 **You teach AI**: Describe your specific learning workflow and preferences
- 🤝 **Co-work**: Iteratively refine the extension design together

---

### 📊 Evaluating Extension vs. Manual Setup

Use this to decide whether creating an extension makes sense for your situation:

> "I have a decision to make. Here's my situation:
>
> **Current setup**:
> - 2 MCP servers (Playwright, filesystem)
> - 4 custom commands I created
> - A GEMINI.md file with my learning preferences
>
> **Context**:
> - I'm in a study group with 3 other people
> - We meet weekly and work on similar projects
> - We often ask each other "how did you configure that?"
> - We're all learning together (beginners)
>
> **Question**: Should I create an extension for my study group, or is it overkill?
>
> Help me think through:
> 1. What are the benefits of creating an extension for us?
> 2. What are the downsides or complexity costs?
> 3. How much time would it save the group?
> 4. What's the alternative approach?
> 5. Given we're beginners, what would you recommend and why?
>
> Give me a clear recommendation with reasoning."

**Expected outcome**: Thoughtful analysis of trade-offs with a clear recommendation based on your specific context.

**Three Roles in action**:
- 🎓 **AI teaches**: Explains decision framework for extensions
- 📚 **You teach AI**: Provide context about your group and skill levels
- 🤝 **Co-work**: Together evaluate the best path forward

---

### 🚀 Publishing and Sharing Your Extension

Use this when you're ready to share your extension with others:

> "I've created a Gemini CLI extension for Python learning called 'python-study-tools'. It's working great on my machine and I want to share it with my study group (5 people).
>
> Walk me through the publishing process:
>
> **Part 1**: How do I prepare it for sharing?
> - What files must be included?
> - What should I document?
> - How do I test that it will work for others?
>
> **Part 2**: How do I publish it?
> - Do I need to create a GitHub repository?
> - What should the README include?
> - Are there any specific repository settings needed?
>
> **Part 3**: How do my study partners install it?
> - What exact command should I give them?
> - What should they expect to see?
> - How do they verify it worked?
>
> **Part 4**: How do updates work?
> - When I improve the extension, how do I release updates?
> - How do they get the updates?
> - What's the version numbering convention?
>
> Give me a step-by-step checklist I can follow."

**Expected outcome**: Complete publishing workflow from preparation through ongoing maintenance, with specific commands and best practices.

**Three Roles in action**:
- 🎓 **AI teaches**: Explains GitHub workflow and extension distribution
- 📚 **You teach AI**: Describe what you want users to experience
- 🤝 **Co-work**: Create documentation and installation instructions together

---

### 🔧 Debugging Extension Installation

Use this when you or others encounter installation problems:

> "My study partner is trying to install my extension but getting errors. Here's what happened:
>
> **What they ran**:
> ```bash
> gemini extensions install https://github.com/myname/python-study-tools
> ```
>
> **Error message**:
> ```
> Error: Failed to install extension 'python-study-tools'
> Could not find gemini-extension.json in repository
> ```
>
> **What I need**:
> 1. What does this error mean?
> 2. What probably went wrong?
> 3. How do I check my repository to verify the structure?
> 4. What should my study partner do now?
> 5. How can I prevent this for other people?
>
> Also, create a troubleshooting checklist I can add to my README so others can self-diagnose common issues."

**Expected outcome**: Root cause analysis, immediate fix, and preventive measures documentation.

**Three Roles in action**:
- 🎓 **AI teaches**: Explains common extension installation errors
- 📚 **You teach AI**: Provide specific error details and repository structure
- 🤝 **Co-work**: Debug together and create user-facing documentation

---

## What You've Learned

In this lesson, you've discovered how Gemini CLI extensions transform setup sharing:

**Core Concepts**:
- ✅ **Extensions package complete environments**: MCP servers + commands + context + settings in one bundle
- ✅ **Installation is simple**: One command (`gemini extensions install`) vs. 15-step manual setup
- ✅ **Management is straightforward**: List, update, disable, enable, and uninstall with clear commands
- ✅ **Structure is understandable**: `gemini-extension.json` + `commands/` + `GEMINI.md` + optional settings
- ✅ **Creation is accessible**: Templates (`gemini extensions new`) help you start quickly
- ✅ **Sharing is powerful**: GitHub distribution enables instant setup for teams and study groups

**Practical Skills**:
- Installing extensions from GitHub repositories
- Managing multiple extensions (enabling/disabling per workspace)
- Understanding extension configurations and structure
- Creating basic extensions using templates
- Deciding when extensions are valuable vs. overkill

**Key Insight**:
Extensions aren't just about bundling—they're about **maintaining consistency** across collaborators and **evolving setups** without resending files. The transformation from 45-minute manual setup to 2-minute installation isn't just about speed; it's about removing friction from learning and collaboration.

---

## What's Next

You've completed Chapter 6: Google Gemini CLI. You now understand:
- Why Gemini CLI matters (Lesson 1)
- How to install and authenticate (Lesson 2)
- Built-in tools for file operations, shell, and web (Lesson 3)
- Context and memory management (Lesson 4)
- Configuration and settings hierarchy (Lesson 5)
- MCP server integration for extended capabilities (Lesson 6)
- Custom slash commands for automation (Lesson 7)
- **Extensions for packaging and sharing complete setups (Lesson 8)** ← You are here

**Next chapter**: Chapter 7 - Bash Essentials for AI-Driven Development

You'll learn the command-line fundamentals that make you effective with AI coding tools: file operations, process management, environment variables, and shell automation. These skills amplify everything you've learned about Claude Code and Gemini CLI.
