### Core Concept
Install OpenClaw CLI, configure a free LLM provider (Kimi K2.5, Google Gemini, or Ollama), connect Telegram, and launch a working AI Employee in 45-60 minutes. The wizard-based onboarding combines all steps into one interactive flow.

### Key Mental Models
- **Three LLM Paths**: Kimi K2.5 (best quality free, 1.5M tokens/day), Google Gemini (easiest OAuth, no key management), Ollama (fully local, unlimited, requires 16GB+ RAM)
- **Gateway as Orchestrator**: The gateway process bridges Telegram messages to your LLM provider and back—it must stay running for your AI Employee to receive messages
- **Pairing as Security**: First message triggers a pairing code you approve in the terminal, preventing unauthorized access to your API credits

### Critical Patterns
- Install: `curl -fsSL https://openclaw.ai/install.sh | bash` (requires Node.js 22+)
- Verify installation: `openclaw doctor` (shows configuration status and what's missing)
- Configure everything at once: `openclaw onboard` (walks through LLM and Telegram setup)
- Start gateway: `openclaw gateway run --port 18789` (foreground) or `openclaw gateway start` (background) or `openclaw gateway install` (system service)
- Approve pairing: Type `y` in the terminal gateway window when pairing code appears

### Common Mistakes
- Not reloading shell after installation (`source ~/.bashrc` on Linux/WSL or `source ~/.zshrc` on macOS)
- Running Node version below 22 (check with `node --version`)
- Incomplete Telegram token copy (must include numeric prefix AND letter suffix after colon)
- Trying to message bot before first pairing code is approved
- Gateway not running when sending Telegram messages
- Closing the gateway terminal window (stops the AI Employee from receiving messages)

### Connections
- **Builds on**: Why AI Employees matter (Lesson 1)
- **Leads to**: Putting your AI Employee to work on real tasks (Lesson 3)
