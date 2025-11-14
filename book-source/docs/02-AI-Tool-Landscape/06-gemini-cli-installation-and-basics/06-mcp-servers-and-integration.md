---
sidebar_position: 6
title: MCP Servers & Integration
---

# MCP Servers & Integration

**Duration**: 20 minutes

> **A Word Before We Begin**
>
> Imagine hiring an incredibly smart assistant who can write code, answer questions, and solve problems—but they're locked in a room with no phone, no internet, and no access to your company's systems. That's Gemini CLI without MCP servers. In this lesson, you'll see the problem firsthand, then learn how MCP (Model Context Protocol) transforms Gemini from isolated intelligence into a connected powerhouse.

---

## The Problem: AI in Isolation

Let's start with a real demonstration. Launch Gemini CLI:

```bash
gemini
```

Now try this request:

```
I need to check the latest release of React on GitHub. Show me:
1. The latest version number
2. Release date
3. Key changes in the changelog

Use whatever tools you have available.
```

**What happens** (Gemini CLI v0.15.0 without MCP):

Gemini will use its **built-in web fetch tool** to try getting this information:

```
🔧 Using tool: web_fetch
   URL: https://github.com/facebook/react/releases/latest

📄 Fetching...

I can see the GitHub releases page, but I'm getting the static HTML only.
The actual release data (version, date, changelog details) is loaded
dynamically via JavaScript, which the basic web fetch tool cannot execute.

Here's what I found in the static HTML:
- Page title mentions "Releases · facebook/react"
- There are some navigation elements
- The actual release content area is empty: <div id="repo-content-turbo-frame"></div>

The release information you need is rendered client-side by JavaScript,
so I cannot access it with the current tools.

**What you can do instead:**
1. Visit https://github.com/facebook/react/releases manually
2. Use GitHub CLI: gh release view --repo facebook/react
3. Use npm: npm view react version
4. Use the GitHub API directly with curl

Would you like me to help you with any of these alternatives?
```

**The limitation**: Gemini tried to help using its web fetch tool, but:
- ✅ It attempted to fetch the URL
- ❌ Only got static HTML (no JavaScript execution)
- ❌ Modern websites load content dynamically
- ❌ Can't interact with the page (click buttons, scroll, wait for loading)
- ❌ No direct GitHub API access

**The reality**: Gemini is brilliant but **limited by built-in tools**. It can't:
- ❌ Execute JavaScript on web pages (static HTML only)
- ❌ Access authenticated APIs (like GitHub API)
- ❌ Query databases directly
- ❌ Browse websites with modern dynamic content
- ❌ Interact with forms, buttons, or dynamic elements

### What Gemini CAN Do (Out of the Box)

The built-in tools from Lesson 3 give you:

✅ **File operations**: Read/write files on your local computer
✅ **Shell execution**: Run terminal commands (`ls`, `git status`, etc.)
✅ **Web fetching**: Simple HTTP GET requests (static HTML only)
✅ **Search**: Google Search results (metadata, not full content)

These are **local, static capabilities**—perfect for many tasks, but limited when you need:
- Real-time external data
- Advanced browser interactions (JavaScript, forms, authentication)
- Database queries
- API integrations
- Custom tool connections

### The Gap in Your Workflow

**Real-world scenario**: You're researching competitors.

**What you need**:
1. Browse 10 competitor websites
2. Navigate to pricing pages (which load dynamically via JavaScript)
3. Extract pricing tiers and features
4. Compare side-by-side in a table
5. Save results to a spreadsheet

**What Gemini's built-in tools can do**:
- Web fetch retrieves HTML (but JavaScript content doesn't load)
- You see raw HTML source code
- Pricing info is hidden in JavaScript (`<div id="pricing"></div>` with no content)
- You manually visit each site, copy-paste data
- **Time: 1-2 hours**

This is the **isolation problem**.

---

## The Solution: Model Context Protocol (MCP)

**MCP** (Model Context Protocol) is the **universal bridge** that connects AI tools to external systems.

Think of MCP like **USB for AI**:
- Before USB: Every device needed a custom cable (keyboard cable, mouse cable, printer cable)
- After USB: One standard port connects everything

**Before MCP**:
- ChatGPT builds custom GitHub integration
- Claude builds its own GitHub integration
- Gemini builds yet another GitHub integration
- Result: Duplication, incompatibility, vendor lock-in

**After MCP**:
- One GitHub MCP server works with ChatGPT, Claude, Gemini, and any future AI tool
- Developers build once, use everywhere
- Community creates hundreds of MCP servers (databases, APIs, browsers, custom tools)

### How MCP Works: The Technical View

MCP servers are **small programs** that:
1. Expose capabilities (tools) through a standard protocol
2. Run locally (your computer) or remotely (cloud API)
3. Handle authentication, data fetching, and responses
4. Return structured data Gemini can understand

**Example**: GitHub MCP Server

```typescript
// Simplified structure (you don't write this—you just install it)
interface GitHubMCPServer {
  name: "github";

  tools: [
    {
      name: "list_pull_requests",
      description: "Fetch open PRs from a repository",
      parameters: {
        repo: "tensorflow/tensorflow",
        status: "open",
        since: "2025-01-08"
      }
    },
    {
      name: "create_issue",
      description: "Create a new GitHub issue",
      parameters: { title: string, body: string, labels: string[] }
    }
  ];
}
```

**When you ask Gemini** to show pull requests:
1. Gemini recognizes it needs GitHub data
2. Gemini calls the `list_pull_requests` tool on GitHub MCP server
3. MCP server authenticates with GitHub, fetches data, returns JSON
4. Gemini formats the data into a readable response

### MCP Server vs Built-In Tools

| Capability | Built-In Tools | MCP Servers |
|-----------|----------------|-------------|
| **File operations** | ✅ Read/write local files | ✅ Same |
| **Shell commands** | ✅ Run `ls`, `git`, `npm` | ✅ Same |
| **Web fetching** | ✅ Static HTML only | ✅ **Full browser automation** (Playwright MCP) |
| **Search** | ✅ Google Search metadata | ✅ **Real-time doc access** (Context7 MCP) |
| **GitHub** | ❌ No access | ✅ **Full API access** (GitHub MCP) |
| **Databases** | ❌ No access | ✅ **SQL queries** (PostgreSQL MCP) |
| **Custom APIs** | ❌ No access | ✅ **Any API** (custom MCP servers) |

### Real-World Example Revisited

**Scenario**: Analyze 10 competitor websites for pricing.

**Without MCP** (built-in web fetch only):
1. Fetch each URL → get static HTML
2. JavaScript-rendered prices don't load
3. Manually visit sites, copy-paste
4. **Time: 1-2 hours**

**With Playwright MCP**:
```
Use Playwright to browse these 10 competitor sites, navigate to
pricing pages, extract all pricing tiers and features, and create
a comparison table.
```

Gemini:
1. Launches headless browser via Playwright MCP
2. Navigates to each site, waits for JavaScript to load
3. Clicks "Pricing" links, scrolls, extracts data
4. Returns structured table
5. **Time: 5-10 minutes**

---

## Why MCP Is a Breakthrough

Before MCP, every AI tool built isolated integrations:

```
ChatGPT ───> Custom GitHub Plugin (vendor-locked)
           └> Custom Notion Plugin
           └> Custom Slack Plugin

Claude Code ───> Custom GitHub Integration (incompatible)
               └> Custom Notion Integration
               └> Custom Slack Integration

Gemini CLI ───> Custom GitHub Integration (duplicate work)
              └> Custom Notion Integration
              └> Custom Slack Integration
```

**Problems**:
1. **Duplication**: Same integrations built 3+ times
2. **Vendor lock-in**: Switch AI tools → lose all integrations
3. **Limited coverage**: Small teams can't build 100+ integrations
4. **Maintenance burden**: Updates break across multiple codebases

### The MCP Standard

With MCP, **one server works everywhere**:

```
                    GitHub MCP Server
                           ↑
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
   ChatGPT          Claude Code          Gemini CLI

                    Notion MCP Server
                           ↑
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
   ChatGPT          Claude Code          Gemini CLI
```

**Benefits**:
1. ✅ **Build once, use everywhere**: GitHub MCP works with all AI tools
2. ✅ **Community-driven**: Anyone can build MCP servers for any service
3. ✅ **No vendor lock-in**: Switch AI tools without losing integrations
4. ✅ **Open standard**: Not controlled by one company
5. ✅ **Rapid growth**: 100+ MCP servers already exist

#### 💬 AI Colearning Prompt
> "Why do you think MCP is called 'Model Context Protocol' and not 'Model Tool Protocol'? What does 'context' imply about how AI uses these connections?"
>
> **Hint**: Think about the difference between a one-time tool use vs. ongoing context the AI maintains throughout a conversation.

---

## Seeing the Difference: Before and After MCP

Let's make this concrete with real examples you can try.

### Example 1: The Same Task with MCP (The "After" Picture)

Let's see what happens when you have MCP servers installed. Using the **exact same prompt** as the opening example:

**Prompt**:
```
I need to check the latest release of React on GitHub. Show me:
1. The latest version number
2. Release date
3. Key changes in the changelog

Use whatever tools you have available.
```

**With Playwright MCP Server** (after installation in Part 2):

```
🔧 Using tool: playwright_navigate
   URL: https://github.com/facebook/react/releases

🌐 Launching browser...
📄 Waiting for page to load (including JavaScript)...
✅ Page loaded successfully

Latest Release: React 19.0.0
Released: December 5, 2024

Key Changes:
• Actions: New API for handling form submissions and data mutations
• Document Metadata: Built-in support for <title>, <meta>, and <link> tags
• Asset Loading: Improved preloading and loading strategies
• Web Components: Better integration with custom elements
• React Compiler: New optimization features (experimental)

Breaking Changes:
- Removed: Legacy Context API (use createContext instead)
- Changed: StrictMode now runs effects twice in development
- Updated: Error boundary behavior for async errors

Migration Guide: https://react.dev/blog/2024/12/05/react-19

📊 Downloads: 25M+ per week on npm
🔗 Full changelog: https://github.com/facebook/react/releases/tag/v19.0.0

Would you like me to:
1. Check compatibility with your current dependencies?
2. Show migration steps for your project?
3. Compare with the previous version (18.3.0)?
```

**The transformation**:
- ✅ **Real browser automation** (JavaScript executes fully)
- ✅ **Accurate, real-time data** from the actual page
- ✅ **Structured extraction** of version, date, changelog
- ✅ **Follow-up actions** suggested based on context
- ✅ **Time saved**: From "go do this manually" → complete answer in seconds

### Example 2: Multi-Step Workflow (Competitive Research)

**Scenario**: Research pricing for 3 AI API providers.

**Without MCP** (manual process):
```
You: "Compare pricing for OpenAI, Anthropic, and Google AI APIs"

Gemini: "I can provide general guidance, but pricing changes frequently.
You should visit:
1. https://openai.com/pricing
2. https://anthropic.com/pricing
3. https://cloud.google.com/vertex-ai/pricing

And manually compare the tiers."

Your manual work:
1. Visit 3 websites
2. Navigate to pricing pages
3. Copy-paste into spreadsheet
4. Format and compare
⏱️ Time: 15-20 minutes
```

**With Playwright MCP** (automated):
```
You: "Use Playwright to browse OpenAI, Anthropic, and Google AI pricing
pages, extract current pricing for their flagship models, and create a
comparison table."

Gemini: ✅ Launching Playwright...
        ✅ Browsing openai.com/pricing...
        ✅ Browsing anthropic.com/pricing...
        ✅ Browsing cloud.google.com/vertex-ai/pricing...

| Provider   | Model          | Input ($/1M tokens) | Output ($/1M tokens) |
|------------|----------------|---------------------|----------------------|
| OpenAI     | GPT-4 Turbo    | $10.00              | $30.00               |
| Anthropic  | Claude 3 Opus  | $15.00              | $75.00               |
| Google AI  | Gemini Pro     | $0.50               | $1.50                |

Notes:
- OpenAI offers volume discounts (>$100k/month)
- Anthropic has academic pricing (50% off with .edu email)
- Google AI pricing effective as of Jan 2025

⏱️ Time: 2 minutes
```

### The Key Insight

**MCP transforms Gemini from**:
- 🔒 **Advisor** (tells you what to do) →
- 🔓 **Executor** (does it for you)

**Without MCP**: "Here's how you could solve this manually..."
**With MCP**: "Done. Here are the results. What's next?"

#### 🎓 Expert Insight
> The real power of MCP isn't just speed—it's **removing context switching**. Without MCP, you stop your AI conversation, open 5 browser tabs, manually gather data, return to AI, paste results, and continue. With MCP, you stay in one continuous conversation while AI handles the data gathering. This is the difference between **assisted** development (you do the work) and **AI-driven** development (AI does the work).

---

## Part 2: CLI MCP Management Commands

The modern way to add MCP servers is **CLI commands**—not manual JSON editing.

### Adding MCP Servers

```bash
# Add stdio MCP server (local Python/Node.js)
gemini mcp add my-server python server.py --port 8080

# Add HTTP MCP server (remote API)
gemini mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer abc123"

# Add SSE MCP server (streaming)
gemini mcp add --transport sse events-api https://api.example.com/sse
```

**Transport types**:
- **Stdio**: Local process (Python script, Node.js server)
- **HTTP**: Remote HTTP server
- **SSE**: Server-Sent Events (real-time streaming)

### Listing MCP Servers

```bash
gemini mcp list
```

**Output**:
```
Connected MCP Servers:
- playwright (stdio) - connected
- context7 (http) - connected
- my-database (stdio) - connecting...
```

Shows status (connected/disconnected/connecting).

### Removing MCP Servers

```bash
gemini mcp remove server-name
```

Removes the server from your configuration.

### CLI vs Manual Configuration

**CLI approach** (recommended for beginners):
```bash
gemini mcp add playwright npx @playwright/mcp@latest
```

Simple, clear, immediate feedback.

**Manual JSON editing** (advanced):
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

More control, but error-prone for beginners. The previous lesson ([Configuration & Settings](./05-configuration-and-settings.md)) covered `settings.json` structure and environment variables if you need manual configuration.

---

## Part 3: OAuth for MCP Servers

Some MCP servers need **authentication**—API keys, cloud credentials, or OAuth tokens. Gemini CLI handles this automatically.

### Why OAuth Matters

**Problem**: External APIs need credentials to verify you.
- Database API key
- Google Drive access token
- Cloud service authentication

**Solution**: OAuth lets you authenticate securely without exposing secrets.

### Using OAuth: `/mcp auth`

```bash
/mcp auth
```

Lists servers that need authentication.

```bash
/mcp auth my-database-server
```

Authenticates with specific server:
1. Browser opens to OAuth provider (Google, GitHub, etc.)
2. You log in
3. Tokens stored automatically in `~/.gemini/mcp-oauth-tokens.json`
4. Tokens auto-refresh when needed

**Key point**: You never manage tokens manually. Gemini CLI handles it.

### When to Use OAuth

**You need OAuth when**:
- MCP server accesses user's Google Drive
- API requires authentication (GitHub, Stripe, etc.)
- Cloud service needs credentials
- Database access is controlled

**You don't need OAuth when**:
- Public APIs (most web browsing)
- Local tools (no external access)
- Open documentation (Context7)

---

## Part 4: Business Workflows

### Workflow 1: Competitive Research (Playwright)

**Goal**: Compare 5 competitors' pricing and features.

**Setup**:
```bash
gemini mcp add playwright npx @playwright/mcp@latest
```

**Prompt**:
```
Use the Playwright MCP server to analyze these 5 competitors:
1. https://competitor-a.com
2. https://competitor-b.com
3. https://competitor-c.com
4. https://competitor-d.com
5. https://competitor-e.com

For each site:
- Find their pricing page
- Extract all pricing tiers
- List key features per tier
- Note any current promotions

Create a comparison table.
```

**Result**: Structured competitive intelligence in minutes.

### Workflow 2: API Documentation Research (Context7)

**Goal**: Understand a new API before integration.

**Setup**:
```bash
gemini mcp add context7 npx -y @upstash/context7-mcp
```

**Prompt**:
```
Use Context7 to research Stripe's API:
1. What are the main endpoints?
2. What's the authentication method?
3. What are rate limits?
4. What's the most recent major version change?
5. Are there breaking changes I should know about?

Give me a summary suitable for a technical decision-maker.
```

**Result**: Current, accurate documentation without manually reading docs.

### Workflow 3: Multi-Tool Combination

**Goal**: Analyze market trends across multiple sources.

```
1. Use Playwright to browse 5 market research sites
2. Use shell to analyze local data files
3. Use Context7 to fetch industry documentation
4. Compile a market analysis report

Combine all three MCP capabilities in one workflow.
```

**Key insight**: MCP servers chain together. One prompt can use multiple capabilities.

---

## Red Flags to Watch

### "MCP server connection failed"
- Check server is running: `gemini mcp list`
- Verify command syntax: `gemini mcp add --help`
- Try manual configuration (see [Configuration & Settings](./05-configuration-and-settings.md) for `settings.json` structure)

### "Authentication failed: Invalid token"
- Re-authenticate: `/mcp auth server-name`
- Check browser OAuth flow completed
- Verify no extra spaces in configuration

### "Playwright timeout: Browser not responding"
- Website may be slow or blocking automation
- Try shorter timeout: Check [Configuration & Settings](./05-configuration-and-settings.md) for timeout configuration
- Test website manually first

### "Context7 not finding documentation"
- Verify MCP server connected: `gemini mcp list`
- Search term may not match indexed docs
- Try more specific queries

---

## Try With AI

### Prompt 1: Setting Up Your First MCP Server
```
I want to add the Playwright MCP server to browse websites.
Walk me through:
1. Exact command to add it
2. How to verify it's working
3. A test prompt to make sure it's connected
4. What to do if the connection fails
```

**Expected outcome**: Step-by-step setup with verification commands.

### Prompt 2: Choosing the Right MCP Server
```
I have this business need: [describe your need]

Examples:
- "Research 20+ competitor websites"
- "Stay current with API documentation"
- "Access our company database"

Which MCP server should I use? Why? How do I set it up?
```

**Expected outcome**: Specific recommendation with setup instructions.

### Prompt 3: Multi-Tool Workflow Design
```
I need to combine multiple MCP servers for this task: [describe]

Design a workflow that uses:
1. Which MCP servers? (Playwright, Context7, custom, etc.)
2. In what order?
3. How do they work together?
4. What's the exact prompt I give you?
5. What's the expected output?
```

**Expected outcome**: Complete workflow architecture.

### Prompt 4: Troubleshooting MCP Issues
```
I'm getting this error: [your error message]

After running: [your command]

Debug this for me. What's wrong? How do I fix it?
```

**Expected outcome**: Specific debugging steps for your error.

---

## Summary

MCP (Model Context Protocol) is **the bridge between Gemini CLI and the outside world**.

**Three transport types**:
- **Stdio**: Local tools (Python, Node.js)
- **HTTP**: Remote APIs
- **SSE**: Real-time streaming

**Key commands**:
- `gemini mcp add` - Connect new server
- `gemini mcp list` - View connected servers
- `gemini mcp remove` - Disconnect server
- `/mcp auth` - Handle OAuth authentication

**Real-world benefits**:
- Competitive research (Playwright)
- Current documentation (Context7)
- Database access
- Custom integrations

**Relationship with Configuration & Settings**:
- Previous lesson ([Configuration & Settings](./05-configuration-and-settings.md)): How to configure Gemini CLI globally (theme, model, auth, checkpointing)
- This lesson: How to extend Gemini CLI with external capabilities (MCP servers)

Both lessons work together—Configuration provides the infrastructure, MCP extends it with custom capabilities.

---

## Next Lesson

**Lesson 7: Custom Slash Commands** teaches you how to create your own `/` commands to automate repetitive tasks and workflows.

**Lesson 8: Extensions, Security & IDE Integration** teaches you how to bundle MCP servers into extensions, filter tool access for security, and integrate with your IDE for seamless development.
