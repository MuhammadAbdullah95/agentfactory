---
title: "Summary: Setup Your AI Employee (Free)"
sidebar_label: "Summary"
sidebar_position: 2.5
---

# Summary: Setup Your AI Employee (Free)

## Key Concepts
- **Onboarding Wizard**: Interactive CLI that configures your LLM provider, gateway port, and channels in one pass
- **Gateway**: Local server (port 18789) that routes messages between channels and the LLM provider
- **Pairing Flow**: Security mechanism requiring you to approve each new Telegram user before they can chat
- **Localhost Binding**: Gateway defaults to 127.0.0.1 so only your machine can access the admin interface
- **Universal Setup Pattern**: Install runtime, configure intelligence, connect I/O channels, verify end-to-end, secure the boundary

## Key Commands
- `openclaw onboard --install-daemon` -- run the onboarding wizard
- `openclaw gateway status` -- check if gateway is running
- `openclaw dashboard` -- open the Control UI in your browser
- `openclaw pairing list telegram` / `openclaw pairing approve telegram <code>` -- manage Telegram pairing
- `openclaw logs --follow` -- stream live gateway logs for debugging

## Common Mistakes
- Forgetting to close and reopen the terminal after install (PATH not updated)
- Using Node.js below version 22 (OpenClaw requires 22+)
- Not approving the Telegram pairing request (bot silently ignores messages)
- Binding gateway to `0.0.0.0` without authentication (exposes agent to the network)

## Quick Reference

| Bind Address | Who Can Access | Safe? |
|---|---|---|
| `127.0.0.1` (default) | Only your machine | Yes |
| `0.0.0.0` without auth | Anyone on network | **Never** |
| `0.0.0.0` with token | Anyone with the token | Yes (remote servers) |
