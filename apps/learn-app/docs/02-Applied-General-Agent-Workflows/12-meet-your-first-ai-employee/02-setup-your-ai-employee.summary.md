### Core Concept
Setup your AI Employee in under 60 minutes with three components: OpenClaw CLI, a free LLM provider (Kimi K2.5 recommended), and Telegram for messaging. The pairing system ensures only you can access your employee.

### Key Mental Models
- **Three LLM Paths**: Kimi K2.5 (best quality, 1.5M tokens/day free), Gemini (easiest OAuth setup), Ollama (fully local, unlimited)
- **Gateway as Hub**: The gateway process connects everything—your Telegram bot, LLM provider, and AI Employee logic
- **Pairing = Access Control**: First-time users receive a code you must approve, preventing unauthorized use of your API credits

### Critical Patterns
- Install: `curl -fsSL https://openclaw.ai/install.sh | bash` (requires Node 22+)
- Configure LLM: `openclaw onboard --auth-choice moonshot-api-key` (or google-gemini-cli, or Ollama setup)
- Set Telegram token: `openclaw config set channels.telegram.botToken "YOUR_TOKEN"`
- Start gateway: `openclaw gateway run --port 18789 --verbose`
- Approve pairing: `openclaw pairing approve telegram <CODE>`

### Common Mistakes
- Forgetting to reload shell after installation (`source ~/.bashrc`)
- Running Node version below 22 (OpenClaw requires Node 22+)
- Not copying the full Telegram token (must include both number and letter parts)
- Trying to message before approving the pairing code

### Connections
- **Builds on**: Understanding AI Employee concept (Lesson 1)
- **Leads to**: Putting your AI Employee to work (Lesson 3)
