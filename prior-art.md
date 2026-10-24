# Prior Art

Has anyone already built a Claude Code macropad? Checked 2026-10-24 by web search
(no hands-on testing of any of these).

**Short answer: no dedicated Claude Code hardware pad was found.** The closest
thing is OpenAI's pad for Codex; on the Claude side there are Stream Deck
profiles and plugins, not hardware.

| Project | What it is | Relevance |
|---------|------------|-----------|
| **OpenAI Codex Micro** (with Work Louder) | Dedicated agent macropad: 13 mechanical keys, rotary encoder, touch sensor, joystick; USB-C / Bluetooth; Mac and Windows; reported at $230. One of its six agent keys shows live status (idle, thinking, done, needs input, error). [Write-up](https://pasqualepillitteri.it/en/news/7163/openai-codex-micro-work-louder-hardware) | The direct analogue of this project, for a different agent. Validates the status-LED idea. One blogger calls it a Work Louder Creator Micro with a custom keyset and firmware profile ([alternatives](https://www.adityabawankule.io/blog/openai-codex-micro-alternatives)). No Linux mentioned. |
| **streamdeck-claude** ([GitHub](https://github.com/JulienCr/streamdeck-claude)) | Stream Deck plugin: one key per running Claude Code session, showing working / idle / awaiting permission / awaiting plan, pulsing when it needs you | Same hook-driven status idea as `hardware-directions.md`, on Stream Deck. Focus-jump targets Warp on macOS/Windows. |
| **Elgato "Claude Code Shortcut" profile** ([Elgato](https://www.elgato.com/de/en/explorer/products/stream-deck/control-claude-with-stream-deck-for-faster-workflows/)) | Free Stream Deck profile, 57 shortcuts in 8 categories, including Esc-Esc rewind and dials for permission mode and history | Useful as a checklist of candidate keys. |
| **yolodeck** ([post](https://bubbles.town/entry/44752158)) | Stream Deck button to grant or block Claude Code permissions (Windows fork of a macOS project) | Approve/deny as a physical key. |
| **configure-macro-keyboard** skill ([listing](https://skillselion.com/skills/terrylica/cc-skills/configure-macro-keyboard)) | Claude Code skill for configuring a macro keyboard, macOS | Software only. |

## What is still unclaimed

- A **Linux / KDE** Claude Code pad (everything above is Mac/Windows or Stream Deck).
- **Physical push-to-talk for Claude Code voice dictation** (key 2 in
  [`key-layout.md`](key-layout.md)). None of the above mentions it.
- Open hardware: Codex Micro is a closed product; nobody has published a
  Claude-specific QMK keymap or PCB.
