### Core Concept
**Terminal sessions die when you disconnect—tmux keeps them alive.** tmux creates persistent sessions on the server that survive SSH disconnections, laptop sleep, and connection timeouts. Your long-running agent tasks continue even when you're not connected.

### Key Mental Models
- **Sessions Independent of Connection**: tmux runs on the server, not your laptop. SSH is just a "view" into the tmux session. When SSH dies, tmux continues running.
- **Detach vs Exit**: Detach (`Ctrl+b`, then `d`) leaves session running in background. Exit (`exit` or closing terminal) can kill processes. Always detach before closing terminals.
- **Panes as Layouts**: Split terminal windows into multiple panes to see everything at once—logs, main process, debug terminal—without switching windows.
- **Named Sessions as Contexts**: Each project gets its own named session. Switch sessions = switch projects. Each maintains its own layout, directory, and running processes.
- **Automation with Scripts**: Save complex pane layouts as shell scripts. One command recreates your entire monitoring dashboard instantly.

### Critical Patterns
- **Create Named Sessions**: `tmux new-session -d -s session-name` creates background session. Attach with `tmux attach-session -t session-name`. List all with `tmux list-sessions`.
- **Detach Safety**: Always detach with `Ctrl+b`, then `d` before closing terminal windows. This ensures session continues running.
- **Split Panes for Monitoring**: `Ctrl+b`, `%` splits vertically (left-right); `Ctrl+b`, `"` splits horizontally (top-bottom). Navigate with `Ctrl+b`, `o`.
- **Session Switching**: Create multiple named sessions for different projects (`voice-learning`, `customer-support`, `notes`). Jump between them instantly—each maintains independent state.
- **Layout Automation**: Create shell scripts that build complex pane layouts automatically. Send commands to specific panes with `tmux send-keys -t session:pane 'command' Enter`.

### Common Mistakes
- **Closing Without Detaching**: Closing terminal window without detaching can kill processes. Always `Ctrl+b`, `d` before closing.
- **Losing Track of Sessions**: Creating sessions without names makes them hard to manage. Always use `-s session-name` when creating sessions.
- **Pane Navigation Confusion**: Forgetting which pane is active leads to typing in wrong place. Use status bar (bottom line) to identify current session and window.
- **Session Clutter**: Creating too many sessions without cleanup leads to confusion. Kill unused sessions with `tmux kill-session -t session-name`.
- **Forgetting Persistence**: Not all terminal state survives tmux detach. Background processes started without proper process management (nohup, systemd) may still die.
