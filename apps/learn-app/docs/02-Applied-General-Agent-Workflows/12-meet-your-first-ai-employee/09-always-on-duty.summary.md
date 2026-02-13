### Core Concept
Your AI Employee can operate 24/7 through two approaches: PM2 for local always-on operation (your computer stays on), or Oracle Cloud Free Tier for true remote operation ($0 permanent compute). This transforms your AI Employee from a work-hours assistant into an always-available team member.

### Key Mental Models
- **Local vs Remote Trade-off**: PM2 is simpler but requires your computer; Oracle Cloud provides independence but has setup complexity
- **Process Management**: PM2 handles crashes, restarts, and boot persistence—you configure once, it maintains availability
- **Zero-Trust Networking**: Tailscale provides secure access without exposing ports; VCN rules block everything except Tailscale traffic

### Critical Patterns
- PM2 ecosystem file: `module.exports = { apps: [{ name: "openclaw-gateway", script: "openclaw", args: "gateway run --port 18789", autorestart: true }] }`
- Persist across reboots: `pm2 save && pm2 startup` (then run the command it outputs)
- Oracle Cloud setup: Enable user lingering (`sudo loginctl enable-linger ubuntu`), use `systemctl --user restart openclaw-gateway`
- Health monitoring: `openclaw health`, `openclaw status --all`, `openclaw logs --follow`
- Tailscale access: `https://openclaw.YOUR-TAILNET.ts.net/` provides automatic HTTPS without SSH tunnels

### Common Mistakes
- Starting with Oracle Cloud before confirming PM2 works locally (always test simple path first)
- Forgetting `pm2 startup` command—processes won't survive reboot without it
- Exposing gateway ports publicly instead of using Tailscale for secure access
- Not enabling user lingering on Oracle—services stop when SSH session ends
- Ignoring "out of capacity" errors on Oracle (retry during off-peak hours or different availability domain)

### Connections
- **Builds on**: HITL approval workflows (Lesson 8) ensure safe autonomous operation
- **Leads to**: Chapter Assessment (Lesson 10) for certification
