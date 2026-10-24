# Off-the-Shelf Macropads for the 11-Key Draft (Linux)

Pads that can carry the 11-key draft in [`../key-layout.md`](../key-layout.md)
(so 12+ keys) and work on Linux. Researched 2026-10-24 from web search and
project pages; nothing here was bought or tested.

**Prices are approximate**: retailer listings of unknown date, in the currency
found, converted roughly to USD. Re-check before buying, and add shipping and
the 17% Israeli VAT above ~$75 (see `bom.md`).

## Requirements that matter for this layout

1. **12+ keys.** 11 committed plus 1 spare.
2. **Programmable without Windows.** QMK/VIA (configured in the browser at
   usevia.app, stored on the pad) is the gold standard: nothing runs on the host.
3. **Real key hold for the push-to-talk key.** QMK/VIA pads send a plain held
   `Space`, which is what Claude Code's hold mode needs. Stream Deck-style pads
   generally send taps, so they need `/voice tap` or a rebound key (see
   `key-layout.md`).
4. **Text macros with Return** (`/compact` ⏎). VIA has a macro editor; QMK
   does it in the keymap; Stream Deck software does it natively.

## Candidates

| Pad | Keys | Programming on Linux | Approx. price | Fit |
|-----|------|----------------------|---------------|-----|
| **Adafruit MacroPad RP2040** (starter kit) | 12 (3×4) + encoder + OLED | QMK (`keyboards/adafruit/macropad` exists upstream), CircuitPython, Arduino | ~$50 kit; bare board $34.95 ([Adafruit](https://adafruit.com/product/5100), [Pi Hut](https://thepihut.com/collections/adafruit-accessories/products/adafruit-macropad-rp2040-starter-kit-3x4-keys-encoder-oled-adabox019-essentials) £48) | **Best match.** Exactly 3×4, per-key RGB for the status idea, encoder push can take Rewind, OLED can show Claude state. Kit was out of stock at two retailers. Adafruit's page says QMK isn't supported, but the QMK repo has the board; CircuitPython is the safe path. |
| **Work Louder Creator Micro** | 12 + 2 scroll wheels, 4 layers | VIA; vendor says it works on Linux ([Drop Q&A](https://drop.com/buy/work-louder-creator-micro/questions)) | Not found (Drop hides it); likely $150+ | Same maker as OpenAI's Codex Micro. Premium, low-profile switches. |
| **DOIO KB16** | 16 + 3 knobs (some listings say 4) | QMK/VIA | ~$65–80 (¥10,000 in Japan; ~$79 listed) ([review](https://green-keys.info/en/doio-kb16-macro-pad-review%ef%bd%9cexplanation-of-effective-use/)) | 5 spare keys; knobs useful for scrolling. Wired only. Check the knob count on the listing. |
| **Binepad BNK-16** | 16 | QMK/VIA | from ~$99 ([mechanicalkeyboards.com](https://mechanicalkeyboards.com/collections/QMK-VIA-Compatible-Keyboards?page=6)) | CNC aluminium, solid. Room to grow. |
| **Keychron Q0 Max** | 21 (numpad layout) + knob | QMK/VIA, wireless | ~$110 ([Keychron](https://www.keychron.com/collections/bts-2026-max-k-qmk-series)) | Numpad legends and odd key sizes; fine with custom caps. Overkill for 11. |
| **Generic AliExpress 12-key + 2–3 knob pad** (CH552/CH57x) | 12 + knobs | Not QMK. Open-source [`ch57x-keyboard-tool`](https://github.com/pferreir/ch57x-keyboard-tool) (Rust, `cargo install`) writes the keymap from a YAML config; may need sudo | ~$15–30 (typical listing, not verified) | **Cheapest.** Stores simple keys/combos; text macros are limited, so text keys would send `F13`–`F24` and let a host tool type the text. Check the USB ID against the tool's supported list before buying. |
| **Elgato Stream Deck MK.2** | 15 LCD keys | [StreamController](https://github.com/StreamController/StreamController) (official Linux app, community) | ~$150 MSRP ([listing](https://global.channelonline.com/acme/ccs/Products/overview/M023478422)), €137 on deal | Per-key icons (Claude logo, mic) with no keycap printing. Tap-style keys, so push-to-talk needs tap mode. StreamController lists Original, Mini, XL, Plus, Neo and others; MK.2 assumed under "Original" (not confirmed). |
| **Ajazz AKP153** (Stream Deck clone) | 15 LCD keys | Vendor lists Windows and Mac only; not on StreamController's list (which has Mirabox 293S and Ulanzi D200 as experimental) | ~$40–57 (Walmart) | Cheap, but **no confirmed Linux route.** Skip. |

Too small for the draft: Stream Deck Mini (6), Neo (8), Binepad BNK9 (9).

## Recommendation

- **First pick: Adafruit MacroPad RP2040**, about $50. Exact fit, open
  firmware, RGB and OLED for the status-LED idea, so it can later grow into the
  Tier 2 build without changing pads.
- **If you want labels without printing caps: Stream Deck MK.2** with
  StreamController, accepting tap-mode push-to-talk.
- **Cheapest test of the concept:** a generic 12-key AliExpress pad with
  `ch57x-keyboard-tool`, paired with the host-side tool in [`../TODO.md`](../TODO.md).
