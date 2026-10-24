# Shopping Spec — Macropad

Reference checklist for buying a pad for the 11-key draft in
[`../key-layout.md`](../key-layout.md). The rule is **QMK firmware, configurable
with VIA (or Vial)**: it is the route with the best Linux compatibility, since
the keymap lives on the pad and nothing vendor-specific runs on the host.
Written 2026-10-24.

## Must have

| # | Requirement | Why | How to check |
|---|-------------|-----|--------------|
| 1 | **QMK firmware** | Open, documented, Linux-native toolchain; needed later for the status LED (Raw HID) | Board has a folder in [`qmk_firmware/keyboards`](https://github.com/qmk/qmk_firmware/tree/master/keyboards), or the seller publishes the source |
| 2 | **VIA or Vial support** | Remap and record text macros in the browser, no compiling | Listing says VIA/Vial; board is auto-detected at [usevia.app](https://usevia.app), or seller supplies the VIA JSON |
| 3 | **12+ keys** | 11 committed + 1 spare | 3×4 is ideal |
| 4 | **1u keys for the 11** | Custom keycaps (`keycap-printing.md`) are all 1u; numpads have 2u `0`/`+`/`Enter` keys that need special caps | Look at the layout photo |
| 5 | **MX-compatible hot-swap sockets** | Swap switches and fit standard MX keycaps | "Hot-swap", "MX", 3- or 5-pin |
| 6 | **Wired USB-C** | Reliable on Linux; wireless is optional extra | — |
| 7 | **Real key hold** | Push-to-talk key must send a held `Space` | Automatic with QMK; not with "macro software" pads |

## Nice to have

- **Per-key RGB** or a spare LED, for the "Claude is waiting" status idea.
- **Rotary encoder with push**, to carry Rewind and free a key.
- **Documented bootloader entry** (reset button or `QK_BOOT`) for flashing a
  custom keymap later.
- **OLED**, for showing Claude's state as text.

## Red flags — skip the listing

- "Programmable" with **no mention of QMK, VIA or Vial**. These are generic
  CH552/CH57x pads configured by a Windows `.exe` (often a Google Drive link).
  Open-source `ch57x-keyboard-tool` can program some of them on Linux, but they
  fail requirements 1, 2 and 7 (limited text macros).
- **Windows-only driver/software** as the only way to configure.
- **Bluetooth-only** with no USB data.
- Stream Deck clones (LCD keys) without a confirmed Linux app.

## Linux setup notes (QMK/VIA)

- VIA runs in Chrome/Chromium (WebHID); Firefox does not support WebHID.
- On Linux the browser needs access to the pad's `hidraw` device. If VIA
  cannot see the board, add a udev rule (replace the IDs with the pad's, from
  `lsusb`):

  ```
  # /etc/udev/rules.d/92-via.rules
  KERNEL=="hidraw*", SUBSYSTEM=="hidraw", ATTRS{idVendor}=="xxxx", ATTRS{idProduct}=="yyyy", MODE="0660", TAG+="uaccess"
  ```

  then `sudo udevadm control --reload && sudo udevadm trigger`. (Standard VIA-on-Linux
  fix, not yet run on this machine.)

## Known-good picks (from `linux-macropads.md`)

| Pad | Keys | Meets all must-haves? | ~Price |
|-----|------|-----------------------|--------|
| Adafruit MacroPad RP2040 | 12 + encoder + OLED | Yes (QMK in upstream repo; VIA keymap not confirmed, Vial/CircuitPython alternatives) | ~$50 |
| DOIO KB16 | 16 + 3 knobs | Yes | ~$65–80 |
| Binepad BNK-16 | 16 | Yes | ~$99 |
| Work Louder Creator Micro | 12 + 2 wheels | Yes (VIA), low-profile switches so check keycap fit | $150+ |

## AliExpress scan (2026-10-24)

Searched AliExpress (`12 key macro pad`, `via qmk macro pad`,
`qmk 12 keys macropad`; prices in ILS as shown to an Israeli session). Product
pages need JavaScript and were not opened, so everything here is from the
search-results page only.

**Finding: no 12-key QMK/VIA pad turned up.** The 12-key listings are all
generic "programmable" pads (fail the spec). The QMK/VIA hits are numpads or
too small:

| Listing | Keys | QMK/VIA (per title) | Price | Verdict |
|---------|------|---------------------|-------|---------|
| [QMK VIA mechanical numpad](https://he.aliexpress.com/item/1005004563790468.html) | 20/21/23/24 | QMK + VIA | ₪112 | Passes 1–3; fails 4 (numpad 2u keys) and 5 (not hot-swap). Workable if you only use the 1u keys. |
| [ZUOYA GMK26 numpad](https://he.aliexpress.com/item/1005007511694093.html) | numpad (count not shown) | QMK + VIA | ₪96–117 | Hot-swap, 1,000+ sold across listings. Same 2u caveat. Best AliExpress QMK option. |
| [Magic-Force MF34 numpad](https://he.aliexpress.com/item/1005011786272306.html) | 34 | QMK + VIA | ₪210 | Hot-swap; oversized. |
| [CV09 macropad](https://he.aliexpress.com/item/1005012102415159.html) | 9 | QMK + VIA | ₪50 | Too few keys. |
| [SAYODEVICE 12-key](https://he.aliexpress.com/item/1005011840638840.html) | 12 | Neither | ₪60 | Own firmware with a web configurator (WebHID); Linux use plausible but unverified. Outside the spec. |
| Generic 12-key + knobs ([e.g.](https://he.aliexpress.com/item/1005009972727737.html)) | 12 | Neither | ₪50–100 | Fails the spec. |

**Implication:** for an exact 3×4 QMK pad, buy outside AliExpress (Adafruit,
DOIO via Amazon/official store, Binepad). On AliExpress, the ZUOYA GMK26 is the
compromise: QMK/VIA and cheap, at the cost of numpad key sizes.
