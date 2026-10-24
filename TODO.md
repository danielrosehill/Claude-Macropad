# To Do

## Later: configuration and management tool (`claude-macropad`)

A host-side CLI that owns the pad's configuration, so changes do not mean
re-flashing or hand-editing firmware keymaps. Added 2026-10-24.

1. **Config parameters.** Read and edit `~/.config/claude-macropad/config.yaml`,
   starting with `repos_dir` (key 8, "Go to repos", default `~/repos`).
   - e.g. `claude-macropad set repos_dir ~/repos/github`, `claude-macropad get repos_dir`.
2. **Remap shortcuts onto keys.** Treat the shortcuts in `key-layout.md` and
   `ideated-shortcuts.md` as a library, and assign any library entry to any pad
   key.
   - e.g. `claude-macropad list` (library), `claude-macropad assign 12 resume`,
     `claude-macropad show` (current layout).
   - Needs the library moved into a machine-readable file (YAML/JSON: id,
     label, icon, action type, text/keys, submit) that the docs are generated
     from or link to.
3. **Push the layout to the pad.** Depends on the pad chosen
   (`specs/linux-macropads.md`):
   - QMK/VIA pads: pad keys send `F13`–`F24`; the tool registers host
     shortcuts that perform the mapped action (so remapping never touches
     firmware).
   - Generic CH57x pads: generate a `ch57x-keyboard-tool` YAML and upload it.
   - Stream Deck: write a StreamController page.
   - Virtual Macropad: write `~/.config/virtual-macropad/config.yaml`.
4. **Injection.** Reuse the backend logic from
   `linux-desktop/Virtual-Macropad` (`virtual_macropad/inject.py`: wtype /
   ydotool / xdotool, plus `layout_pin` for the Hebrew-layout problem) rather
   than rewriting it.

Open: whether this lives in this repo or in Virtual-Macropad, which already has
a config file, injection backends and a macro format.
