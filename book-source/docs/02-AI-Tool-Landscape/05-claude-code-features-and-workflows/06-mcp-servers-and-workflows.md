---
sidebar_position: 6
title: "MCP Servers and Secure External Integration"
chapter: 5
lesson: 6
learning_objectives:
  - "Understand what MCPs are and when they extend AI capabilities beyond local development"
  - "Apply security evaluation framework to assess MCP trustworthiness before configuration"
  - "Configure trusted MCPs securely in Claude Code settings"
  - "Verify MCP behavior matches security expectations using validation tests"
  - "Make strategic decisions about MCP adoption based on value vs. complexity tradeoffs"
estimated_time: "45-60 minutes"
skills_taught:
  - name: "MCP Security Evaluation"
    cefr_level: "A2"
    description: "Evaluate MCP trustworthiness using data access, provider trust, and compliance criteria"
  - name: "Secure Configuration"
    cefr_level: "A2"
    description: "Configure and verify MCPs in Claude Code with security validation checkpoints"
  - name: "Trust Decision-Making"
    cefr_level: "B1"
    description: "Make strategic decisions about which MCPs to adopt for your workflow"
generation_metadata:
  generated_by: "lesson-writer-agent"
  source_spec: "specs/021-audit-chapter5-claude-code/spec.md"
  created: "2025-11-12"
  last_modified: "2025-11-12"
  git_author: "Claude Code Lesson Implementation"
  workflow: "full-regeneration-security-first"
  version: "2.0.0-security-first"
---

# MCP Servers and Secure External Integration

## Introduction: When Claude Needs to Reach Beyond Your Computer

You've learned how Claude Code reads your files, executes bash commands, and helps you write code. Within your local project—within your terminal, your file system, your immediate environment—Claude is powerful and in complete control.

But much of what you actually need exists *outside* your computer:
- Real-time information beyond Claude's training cutoff (current weather, market prices, breaking news)
- Your company's database with customer data
- Websites you need to test or scrape
- APIs specific to your organization
- GitHub repositories and issue trackers

Claude Code is isolated from all of this—by design. It can't browse the web. It can't query your database. It can't access your private APIs. This isolation is actually a *security feature*. But it also means Claude is limited.

**This is where MCP comes in.**

MCP (Model Context Protocol) is how Claude Code safely connects to external tools, databases, and APIs. Think of MCPs as specialized team members Claude can consult:

- "Playwright MCP, open this website and test the login form"
- "Postgres MCP, query our user database for signups in the last 24 hours"
- "GitHub MCP, create a pull request with these changes"
- "Context7 MCP, fetch the latest documentation for React 19"

But here's the critical question that this entire lesson answers: **How do you trust these external connections?**

Unlike local commands, MCPs give Claude access to external systems, data, and credentials. An untrustworthy or misconfigured MCP could:
- Leak sensitive data
- Expose API credentials
- Access data it shouldn't
- Violate compliance requirements (GDPR, HIPAA, PCI-DSS)

**This lesson teaches you to think like a security engineer: What data does this MCP touch? Whose code is it? Does it meet our compliance requirements?**

Your ability to make informed security decisions is what makes you valuable. AI can install MCPs; you decide *which* MCPs are safe.

---

## What Are MCP Servers?

**MCP (Model Context Protocol)** is an open standard that lets Claude Code connect to external tools, databases, and APIs. It's Claude's way of saying: "I need to reach beyond my local sandbox and access external resources safely."

### Three Roles in MCP Integration

**Claude as Co-Worker**: Uses MCPs as specialized tools (just like you use git, curl, or npm)

**MCP as Domain Specialist**: Provides capabilities Claude doesn't have natively (Playwright for browsers, Postgres for databases, GitHub for version control APIs)

**You as Orchestrator**: Decide which MCPs to trust, when Claude should use them, and how much external access is appropriate for your work

### Key Distinctions

**Native Claude Code capabilities** (no MCP needed):
- Read and write files on your computer
- Execute bash commands
- Run local scripts
- Search within your project

Why? Zero external dependencies. Full security control. No trust decisions needed.

**MCP capabilities** (external access):
- Browse websites (Playwright MCP)
- Query databases (Postgres, MySQL MCPs)
- Call APIs (GitHub, Slack, custom APIs)
- Search documentation (Context7 MCP)
- Access cloud services

Why? Requires external access, external dependencies, and security evaluation.

### When MCPs Add Clear Value

1. **Real-time data needs**: Market data, weather, current news, live APIs that Claude's training data can't access
2. **Browser-based testing**: UI automation, form filling, screenshot capture, scraping
3. **Database queries**: Analytics, user data retrieval, application-specific queries
4. **API integration**: GitHub workflows, Slack notifications, internal tool access
5. **Documentation lookup**: Current library docs, API references that change frequently

### When MCPs Add Unnecessary Complexity

1. **Tasks solvable with native capabilities**: File operations, code generation, local bash scripts
2. **High-security environments**: PCI-DSS, HIPAA, SOC2 systems where external tools need formal security review
3. **Simple projects**: Setup overhead exceeds benefit (don't add Postgres MCP to a bash script)
4. **Rarely-used integrations**: Configuration complexity vs. value-add ratio doesn't justify inclusion

**This is specification-first thinking (Principle 3)**: Specify WHAT you need (real-time data? browser automation? database queries), then decide IF an MCP is the right tool, and WHICH MCP to trust.

---

#### 💬 AI Colearning Prompt: Identify Your MCP Needs

Before configuring anything, work with your AI to identify whether you actually need MCPs:

```bash
claude "I work on [describe your projects: web apps, data analysis, API services, etc.].
Analyze whether I would benefit from MCPs. For each potential use case:
(1) What capability I'm missing without it?
(2) Could I achieve this with native bash/curl/file operations instead?
(3) Is the setup complexity worth the value-add?
(4) Your recommendation: Use MCP, use native approach, or skip entirely?"
```

**Key point**: This exercise helps you distinguish "nice to have" from "actually need." Experienced developers are ruthless about this—every tool adds configuration overhead, security surface, and debugging complexity.

---

## Security Considerations First: Evaluating MCP Trust

**This section is foundational. Read it before configuring ANY MCP.**

MCPs have access to:
- Your file system (files Claude reads and processes)
- External networks (the internet, your database servers, your API endpoints)
- Your credentials and secrets (API keys, database credentials, tokens)
- System resources (memory, CPU, network bandwidth)

**The Security Question**: *Do you trust this MCP provider with this level of access?*

This isn't paranoia. It's **Principle 5 (Validation-First Safety)** from the constitution: "Never trust, always verify."

### Security Evaluation Framework: Three Questions

Before you configure ANY MCP, answer these three questions. They form your security decision-making foundation.

---

#### Question 1: What Data Does This MCP Access?

Different MCPs have different risk profiles based on what they can access.

| MCP Type | Data Accessed | Examples | Risk Level |
|----------|---------------|----------|------------|
| **Read-only web/docs** | Public web data, documentation | Context7 MCP (fetch docs), search MCPs | **LOW** |
| **Browser control** | URLs you visit, page content, screenshots | Playwright MCP | **MEDIUM** |
| **Database access** | Database credentials + all queryable data | Postgres MCP, MySQL MCP | **HIGH** |
| **API integrations** | API tokens, private repositories, channels | GitHub MCP, Slack MCP, custom API MCPs | **HIGH** |
| **File system (beyond project)** | System files, user home directory, sensitive paths | MCPs with broad filesystem access | **HIGH** |

**Your action**: Look up the MCP you're considering. Identify exactly what data it accesses. If it's HIGH risk (databases, API credentials, private repositories), proceed with extra caution and verify provider trustworthiness carefully.

---

#### Question 2: Is the Provider Trustworthy?

Research the MCP provider. Don't just install and hope for the best.

**Green Flags (Higher Trust):**
- ✅ **Official MCP from Anthropic**: Published under @anthropic-ai namespace on npm (e.g., @anthropic-ai/playwright-mcp)
- ✅ **Open-source with active maintenance**: 100+ stars on GitHub, recent commits (within last 3 months), responsive maintainers who answer issues
- ✅ **Corporate backing**: Maintainer is an established company (Microsoft, Google, Anthropic, etc.) with reputation at stake
- ✅ **Published security audits**: Documentation mentioning penetration tests, SOC2 certification, or independent security reviews
- ✅ **Clear contribution guidelines**: Code review process, security policy, transparency about changes

**Red Flags (Lower Trust):**
- ⚠️ **Closed-source code**: You can't inspect what it does. Requires complete trust in provider (rare, usually not worth it)
- ⚠️ **Abandoned project**: Last commit >6 months ago, unanswered issues piling up, single maintainer with no backup
- ⚠️ **Anonymous or single-person maintainer**: No verifiable track record, no organization backing
- ⚠️ **Excessive permissions**: Requests file system access when only web access is needed. Asks for credentials it doesn't use.
- ⚠️ **No documentation**: Can't understand what it does, how it works, or what data it accesses
- ⚠️ **Negative security history**: Known vulnerabilities, data leaks, or published security concerns

**Your action**:
1. Find the MCP's GitHub repository
2. Check: Is it actively maintained? Do maintainers respond to issues?
3. Look for security info: SOC2 badge, security audit results, CVE history
4. For HIGH risk MCPs (databases, APIs): Only use providers you'd trust with production access

---

#### Question 3: Does This Meet Compliance Requirements?

If your work is subject to compliance frameworks, MCP data access matters legally.

**Common compliance requirements**:
- **GDPR** (Europe): Data protection, consent for data processing
- **HIPAA** (Healthcare): Protected health information (PHI) handling
- **PCI-DSS** (Payment systems): Credit card data protection
- **SOC2** (Enterprise): Audit, logging, access controls
- **FedRAMP** (US Government): Federal system standards
- **CCPA** (California): Consumer data rights

**If your work requires compliance**:
1. **Review MCP data handling**: Does it log data? Store it? Where? For how long? Is it encrypted?
2. **Check compliance documentation**: Does the MCP provider publish SOC2/ISO27001/HIPAA certification?
3. **Get formal approval**: For HIGH risk MCPs in regulated environments, consult your security team or compliance officer
4. **Document the decision**: Why this MCP? What data does it access? Who approved it? (Creates audit trail)

**Beginner note**: If you're working on personal projects or internal tools without compliance requirements, this is less critical. But developing security-conscious habits NOW prepares you for professional environments where this is mandatory.

---

##### 🎓 Expert Insight: Security as Specification

**Security evaluation is specification-first thinking applied to trust.**

When you evaluate an MCP, you're specifying:
- **What access** is acceptable (read-only documentation vs. write access to production database)
- **What providers** are trustworthy (Anthropic official vs. random GitHub repo)
- **What validation** is required (code review, compliance checks, test in sandbox before production)

This isn't separate from development—it's the foundation. In professional environments:
- Enterprise security teams maintain *approved MCP registries* (typically 5-10 trusted MCPs)
- Unapproved MCPs require formal security review before use
- Data access is logged and audited
- Security decisions are documented and signed off

**Why this matters for your career**: Your ability to evaluate trust is what makes you valuable. AI can install MCPs; humans decide which MCPs are safe. This security judgment is increasingly in demand.

---

#### 🤝 Practice Exercise: Apply the Security Framework

Choose ONE MCP you're considering (Playwright for browser automation, Context7 for documentation search, Postgres for database queries, or another from your domain).

**Write down your answers**:

1. **Data Access Assessment**:
   - What data will this MCP access? (file paths, web URLs, database credentials, API tokens)
   - Risk level: LOW / MEDIUM / HIGH
   - Why? (explain your reasoning)

2. **Provider Trust Evaluation**:
   - Who maintains this MCP? (name, organization)
   - Is the code open-source? (yes/no, link to GitHub repo if yes)
   - Recent activity? (check last commit date, issue response time)
   - Green flags count: ___
   - Red flags count: ___
   - Overall trust assessment: HIGH / MEDIUM / LOW

3. **Compliance Considerations** (if applicable):
   - Does your work require compliance? (GDPR, HIPAA, PCI-DSS, etc.)
   - Does the MCP meet those requirements? (check documentation)
   - Approval needed? YES / NO / CONSULT TEAM

4. **Final Decision**:
   - Proceed with configuration? YES / NO / CONSULT TEAM
   - Why? (1-2 sentence justification based on your evaluation)

**Reflection**: This exercise is security specification—defining your trust boundaries before granting access. Professional security engineers follow this exact pattern before every external tool integration.

---

## Configuring Trusted MCPs Securely

**You've evaluated an MCP and decided to proceed.** Now let's configure it with security checkpoints at each step.

### Understanding Your Tier: Configure, Don't Build Custom

Following the **Graduated Teaching Pattern (Principle 13)**:

- **Tier 1** (Book teaches): What MCPs are, security evaluation ← Previous sections
- **Tier 2** (AI Companion): Configuring trusted MCPs ← **You are here**
- **Tier 3** (AI Orchestration): Building custom MCPs (advanced, requires protocol knowledge)

**For Part 2**: Focus on configuration. Building custom MCPs is Tier 3—you'll get there later with AI guidance. Right now, learn to configure trusted MCPs securely.

---

### Configuration Process (4 Steps with Security Checkpoints)

#### Step 1: Install the MCP

Most MCPs are distributed via npm (Node Package Manager):

```bash
npm install -g @anthropic-ai/playwright-mcp
```

Why `npm install -g` (global)? Claude Code needs MCPs accessible from any directory, not just your project.

**Security checkpoint**:
- Verify you're installing from the correct npm namespace
- Official Anthropic MCPs use `@anthropic-ai/` prefix
- Third-party MCPs should use `@[organization]/` or explicit package name
- Example: `@anthropic-ai/playwright-mcp` ✅ vs `playwright-mcp` (could be unofficial) ⚠️

**Common MCPs and correct installation**:
```bash
# Official Anthropic MCPs
npm install -g @anthropic-ai/playwright-mcp        # Browser automation
npm install -g @anthropic-ai/postgres-mcp          # PostgreSQL access
npm install -g @anthropic-ai/github-mcp            # GitHub integration

# Popular third-party MCPs
npm install -g @context7/context7-mcp              # Documentation search
npm install -g @anthropic-ai/web-search-mcp        # Web search
```

---

#### Step 2: Configure in Claude Code Settings

MCPs are registered in Claude Code's configuration file:

**Project-level**: `.claude/settings.json` (affects one project)
**Global**: `~/.claude/settings.json` (affects all projects)

For most use cases, **project-level is better** (clearer audit trail, project-specific).

##### Example: Playwright MCP Configuration

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/playwright-mcp"],
      "env": {
        "PLAYWRIGHT_HEADLESS": "true"
      }
    }
  }
}
```

**What each field specifies**:
- **`"playwright"`**: Server name (how Claude refers to it in prompts)
- **`"command": "npx"`**: How to start the MCP (npx runs npm packages)
- **`"args"`**: Package to execute; `-y` skips confirmation prompts
- **`"env": {"PLAYWRIGHT_HEADLESS": "true"}`**: Run browser invisibly (security: no visual window stealing focus)

**Security considerations in configuration**:
- ✅ Never hardcode secrets in settings.json (use environment variables instead)
- ✅ Use minimal permissions (PLAYWRIGHT_HEADLESS=true is more secure than running visible)
- ✅ Document WHY each MCP is configured (add comments in settings.json)

##### Example: Postgres MCP Configuration (High-Risk)

For database MCPs, extra care is needed:

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/postgres-mcp"],
      "env": {
        "DATABASE_URL": "${DATABASE_URL}"
      }
    }
  }
}
```

**Security pattern**:
- Database credentials come from environment variable `DATABASE_URL`
- Environment variable is set in your shell or `.env.local` (not in settings.json)
- Claude can read the env var but never sees the actual password in config

**How to set environment variable**:
```bash
# Option 1: Export in terminal (this session only)
export DATABASE_URL="postgresql://user:pass@localhost:5432/mydb"
claude code

# Option 2: Use .env.local (persistent for this project)
echo "DATABASE_URL=postgresql://user:pass@localhost:5432/mydb" > .env.local
# Then Claude automatically loads .env.local

# Option 3: Use system keychain (most secure)
# Different per OS, but Claude Code handles this automatically for many MCPs
```

---

#### Step 3: Grant Permissions (Verify, Don't Just Accept)

When Claude Code first uses an MCP, you'll be prompted:

```
Claude wants to use the MCP server "playwright" to:
- Open and navigate URLs
- Click elements on pages
- Fill forms and submit
- Take screenshots

Allow? [Yes] [No] [Always for this project]
```

**This is your second security checkpoint.** Read carefully.

**Good permission requests look like**:
- ✅ Specific actions (not "access everything")
- ✅ Limited scope (browser automation, not file system)
- ✅ Tied to MCP purpose (Playwright should handle browser, not database)

**Problematic permissions**:
- ⚠️ "Access all files" (why does Playwright need file system?)
- ⚠️ "Use all environment variables" (should be specific variables only)
- ⚠️ Vague permissions ("do anything")

**Your action**:
- If permissions match your security evaluation, proceed
- If they exceed expected scope, DENY and investigate
- Ask: "Does Playwright really need to read my entire home directory?"

---

#### Step 4: Verify Behavior (Trust But Verify)

After configuration, test the MCP with a low-risk task:

```bash
claude "Use the playwright MCP to open https://example.com and tell me the page title"
```

**Expected behavior**:
1. Claude invokes Playwright MCP
2. Browser opens (headless, invisible)
3. Page loads
4. Claude reports back the title

**Verification checklist**:
- ✅ Did the MCP do ONLY what you asked?
- ✅ No unexpected network calls to external servers?
- ✅ No file access outside the MCP's scope?
- ✅ No credentials leaked in logs or output?

**This is Validation-First Safety (Principle 5)**: Trust your configuration, but verify actual behavior.

**Common verification test for database MCPs**:
```bash
claude "Use the postgres MCP to query how many users are in the database. Only return the count, no user details."
```

Check:
- Did it return only what you asked? (count, not user details)
- Did it query the correct database?
- Were credentials not exposed?

---

## Practical MCP Examples: Playwright and Context7

You've learned the security framework and configuration process. Now let's see it in practice with two commonly-used MCPs.

### Example 1: Playwright MCP (Browser Automation)

**Use Case**: Test web applications, scrape public data, automate browser workflows, verify UI changes

**Security Assessment**:
- **Data Access**: URLs you visit, page content, form data you enter, screenshots (MEDIUM risk)
  - What it CAN'T do: Access your local files, run arbitrary code on your machine
  - What it CAN do: See everything on the webpage you're automating
  - Compliance note: If automating forms with PII, this tool is handling sensitive data
- **Provider Trustworthiness**: Anthropic official (HIGH trust, backed by OpenAI/Google/Anthropic)
- **Open Source**: Yes, on GitHub (can inspect code)
- **Security Considerations**: Browser logs may contain URLs and page content; review if testing sensitive systems

**Installation & Configuration**:

```bash
# Install globally
npm install -g @anthropic-ai/playwright-mcp

# Add to .claude/settings.json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/playwright-mcp"],
      "env": {
        "PLAYWRIGHT_HEADLESS": "true"
      }
    }
  }
}
```

**Verification Test** (low-risk):

```bash
claude "Use Playwright to open https://example.com, take a screenshot, and describe what you see"
```

Expected: Claude opens the site, reports what's visible, shows screenshot. No unexpected access.

**Real-World Workflow Example**:

```bash
claude "Use Playwright MCP to:
1. Go to my company's login page
2. Fill in the login form with test credentials
3. Click submit
4. Verify the dashboard loads
5. Take screenshots of the dashboard
Report any errors you encounter."
```

**Common Issues & Troubleshooting**:
- **"Playwright not found"**: Verify global npm install: `npm install -g @anthropic-ai/playwright-mcp`
- **"Permission denied to open browser"**: Browser install issue; try: `npx playwright install`
- **Headless mode fails**: Set `PLAYWRIGHT_HEADLESS: false` for debugging (visible browser)
- **Slow page loads**: Increase timeout; some sites load slowly; Claude handles this automatically
- **Form fills not working**: Some sites have JavaScript validation; Claude adapts to each site

---

### Example 2: Context7 MCP (Documentation Search)

**Use Case**: Fetch current, up-to-date documentation for libraries and APIs, get real-time examples, find recent changes without hunting across websites

**Security Assessment**:
- **Data Access**: Searches public documentation and tech resources (LOW risk)
  - What it accesses: Public web documentation, API references, library docs
  - What it does NOT access: Your private code, database, credentials
  - Compliance note: Lowest risk of the MCPs in this lesson
- **Provider Trustworthiness**: Context7 is maintained by documentation specialists (HIGH trust)
- **Open Source**: Yes, verifiable and inspectable
- **Security Considerations**: Minimal; it only reads public documentation

**Installation & Configuration**:

```bash
# Install globally
npm install -g @context7/context7-mcp

# Add to .claude/settings.json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/context7-mcp"]
    }
  }
}
```

**Verification Test** (low-risk):

```bash
claude "Use Context7 MCP to fetch the latest official documentation about React hooks. Summarize the top 5 hooks and their purpose."
```

Expected: Claude fetches current React docs, summarizes hooks, includes links to official sources.

**Real-World Workflow Example**:

```bash
claude "Use Context7 MCP to:
1. Fetch the latest FastAPI documentation
2. Find best practices for error handling
3. Show me 3 examples of custom exception handlers
4. Include links to the official docs"
```

**Advantages vs. Manual Search**:
- ✅ Always up-to-date (even if Claude's training is old)
- ✅ Includes links to official sources
- ✅ Combines multiple docs seamlessly
- ✅ Saves 10-15 minutes of manual browsing per question

**Common Issues & Troubleshooting**:
- **"Library docs not found"**: Some newer or private libraries aren't indexed; try alternative documentation
- **Outdated results**: Context7 caches results; results usually update daily
- **Rate limiting**: If using heavily, may hit search limits; space out requests or upgrade Context7 plan

---

## Strategic MCP Adoption: The 80/20 Principle

You now understand security evaluation, configuration, and two practical MCPs. Before you start installing everything, understand this: **MCPs are powerful but costly.**

### The 80/20 Breakdown

**80% of your development work**: Native Claude Code capabilities
- File operations (reading, writing, searching)
- Bash commands (automation, running scripts)
- Code generation and refactoring
- Local testing and debugging

**Why use native?** Zero MCP overhead, maximum security control, no configuration needed.

**20% of your development work**: Requires external integration
- Real-time data (current weather, market prices, breaking news)
- Browser testing (UI automation, screenshot verification)
- Database queries (analytics, user data)
- API integration (GitHub, Slack, internal tools)

**Why use MCPs here?** External tools save significant time and prevent you from building integrations manually.

### Strategic MCP Adoption Rules

1. **Start with zero MCPs**
   - Use native capabilities first
   - Identify actual limitations (not theoretical ones)
   - Document what you need: "I need to automate browser testing" not "I should use Playwright"

2. **Add ONE MCP when you hit a clear blocker**
   - "I need to test this in a real browser" → Playwright MCP
   - "I need current documentation that changes daily" → Context7 MCP
   - "I need to query production analytics" → Database MCP

3. **Evaluate ROI (Return On Investment)**
   - Does this MCP save >30 min/week?
   - Does it prevent you from manual work?
   - If not, remove it (complexity cost > benefit)

4. **Limit your MCP library to 3-5 MCPs maximum**
   - Each MCP adds configuration overhead
   - Each MCP adds security surface area
   - Each MCP adds debugging complexity
   - Professional teams are ruthless: 5-10 approved MCPs max per organization

### Professional Context: Enterprise MCP Governance

In enterprise environments, MCP adoption follows strict processes:
- **MCP registry**: Approved list of trusted MCPs (usually 5-10)
- **Security review**: Every new MCP requires formal approval
- **Audit logging**: All MCP access is logged and reviewed
- **Compliance checking**: Data access must align with compliance requirements
- **Update management**: MCP versions are tested before deployment

**You're learning this mindset now, at the foundation.** This skill is increasingly valuable in professional roles.

---

##### 🎓 Expert Insight: Your Value in the MCP Era

**AI can install MCPs. You decide which MCPs are safe.**

This creates a critical professional distinction:

| Activity | AI Does This | You Decide |
|----------|--------------|-----------|
| Install MCP | ✅ Yes (CLI command) | ❌ No |
| Research provider trustworthiness | ✅ Yes (Google, GitHub research) | ❌ No |
| **Approve MCP for use** | ❌ No (too risky) | ✅ **Yes (your judgment)** |
| Configure securely | ✅ Yes (follows best practices) | ❌ No |
| **Verify against compliance** | ✅ Yes (check docs) | ❌ No |
| **Decide if ROI is worth it** | ✅ Yes (analyzes time savings) | ❌ No |
| **Make final decision: use or skip?** | ❌ No (business/security call) | ✅ **Yes (your judgment)** |

The bolded items are where you create value. These are strategic decisions requiring business context, security awareness, and judgment. This is what makes developers valuable in an AI-driven world.

---

#### 💬 AI Colearning Prompt: MCP Security Review Practice

Work with your AI to practice security evaluation on any MCP:

```bash
claude "I'm considering adding [MCP name] to my Claude Code setup.
Walk me through the Security Evaluation Framework:
(1) What data does this MCP access?
(2) Assess the provider's trustworthiness (check GitHub, maintainers, reviews).
(3) What are the compliance implications for [my industry/context: healthcare, fintech, SaaS, etc.]?
(4) Your assessment: Is this MCP safe for my use case? What cautions should I take?"
```

This demonstrates **AI as Teacher** (guiding your evaluation) and **you as Student** (learning to think like a security engineer).

---

## Practice Exercise: Configure Your First MCP Securely

This is hands-on: configure one MCP from start to finish, with security verification at each step.

**Choose**: Playwright, Context7, or another MCP from your domain

**Follow this checklist**:

### Step 1: Security Pre-Check
- [ ] I've answered all three security questions (Data? Provider? Compliance?)
- [ ] I've determined the risk level (LOW/MEDIUM/HIGH)
- [ ] I'm comfortable proceeding (yes/no)

### Step 2: Install
- [ ] Navigate to terminal
- [ ] Run: `npm install -g [mcp-package-name]`
- [ ] Verify success: `npm list -g [mcp-package-name]`

### Step 3: Configure
- [ ] Create or edit `.claude/settings.json` in your project
- [ ] Add MCP configuration following the examples above
- [ ] Double-check: spelling, paths, environment variables correct
- [ ] Save file

### Step 4: Permission Review
- [ ] Start Claude Code in your project
- [ ] Trigger the MCP (try a simple task: "Use [MCP name] to [simple action]")
- [ ] When prompted for permissions, PAUSE and read carefully
- [ ] Ask yourself: Do these capabilities match my security evaluation?
- [ ] Grant or deny

### Step 5: Verify Behavior
- [ ] Execute a low-risk test task
- [ ] Observe: Did the MCP do ONLY what you asked?
- [ ] Check: Any unexpected network activity? File access beyond scope?
- [ ] Confirm: No credentials exposed in output or logs

### Step 6: Document Decision
In your project's README or `.claude/settings.md`, document:
```markdown
## Configured MCPs

### Playwright MCP
- **Use Case**: Browser automation for UI testing
- **Data Access**: URLs, page content, form data
- **Risk Assessment**: MEDIUM (browser automation is safe if used for testing)
- **Provider Trust**: Anthropic official (HIGH)
- **Compliance**: Compliant with [your compliance requirement]
- **Approved By**: [Your name/team]
- **Date**: [Date configured]
```

This creates an audit trail for your team (or future you).

### Step 7: Reflection Questions
- [ ] How did the MCP's actual behavior compare to expectations?
- [ ] Would you configure this MCP on another project? Why/why not?
- [ ] What would you do differently next time?

---

## Key Takeaways

**What You've Learned**:

1. **MCPs extend Claude's capabilities** to external systems (browsers, databases, APIs) beyond local file access
2. **Security evaluation BEFORE configuration** is non-negotiable (three-question framework: Data? Provider? Compliance?)
3. **Configuration process has built-in security checkpoints** (verify namespaces, review permissions, test behavior)
4. **Strategic MCP adoption**: 80% native capabilities, 20% MCPs where they add clear value
5. **Your security judgment is valuable**: AI installs MCPs; you decide which MCPs are safe (this is your competitive advantage)

**Why This Matters for Your Career**:
In professional environments, security judgment determines team productivity and compliance. Developers who think like security engineers are in high demand. You're learning this mindset now.

**What's Next**:
- **Lesson 7** (Hooks): Automate MCP usage with hooks (e.g., "always use Playwright for .spec.ts files")
- **Lesson 8** (Plugins): Orchestrate multiple MCPs + hooks + skills for complex workflows
- **Part 6 onwards**: Advanced MCP patterns, custom MCP development (Tier 3)

**Remember This**:
Every external integration is a trust decision. Every time you evaluate an MCP, you're practicing security engineering. Make informed choices, document your reasoning, and continuously verify behavior.

**Security-conscious developers build trustworthy systems. This makes you valuable.**

---

## Try With AI

MCPs are partnerships between Claude and external tools. Your AI companion helps you use them safely and strategically.

### Prompt 1: Claude as Teacher (Security Education)

```bash
claude "Teach me how to evaluate MCP security.
Choose a popular MCP (like Playwright, Context7, or GitHub MCP) and walk me through the three-question security framework:
(1) What data does it access?
(2) Is the provider trustworthy? (Show me where to find this information on GitHub)
(3) What are compliance considerations for my context?
Explain where to find each answer."
```

**What you'll learn**: How to research MCP security independently. This is **Principle 5 (Validation-First Safety)** in practice—learning to trust but verify.

**Expected outcome**: Claude walks you through research process (GitHub repo analysis, maintainer verification, security documentation), teaching you to evaluate independently.

---

### Prompt 2: Claude as Student (Learning Your Security Requirements)

```bash
claude "Interview me about my security and compliance requirements.
Ask me questions about my work (regulated industry? sensitive data? government/healthcare/financial?).
Based on my answers, create a personalized 'MCP Trust Policy' for my projects.
Recommend which types of MCPs are appropriate for my context, and which I should avoid."
```

**What you'll learn**: How to articulate YOUR security boundaries. Claude adapts recommendations to YOUR specific context, not generic advice.

**Expected outcome**: Claude creates a custom MCP policy reflecting your security posture (conservative for healthcare, balanced for SaaS, minimal restrictions for personal projects).

---

### Prompt 3: Claude as Co-Worker (Collaborative Configuration)

```bash
claude "I want to use [MCP name] for [use case: browser testing, database queries, etc.].
Help me with the full secure adoption workflow:
(1) Apply the three-question security framework to this MCP;
(2) Walk me through installation and configuration step-by-step;
(3) Create a low-risk verification test I should run first;
(4) Help me document this decision for my team."
```

**What you'll learn**: End-to-end MCP adoption with security verification at each step. This is **Three-Role AI Partnership (Principle 18)**: Claude teaches (security framework), learns (your specific use case), and works alongside you (collaborates on configuration).

**Expected outcome**: Complete, security-conscious MCP setup with documentation and verification tests.
