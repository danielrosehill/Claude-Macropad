# Keycap Printing Options (ABS)

How to get 14–16 legended or icon keycaps (see [`../key-layout.md`](../key-layout.md))
for an MX-compatible pad. Researched 2026-10-24 from web sources; prices are as
reported by those sources and not re-checked on vendor sites unless stated.

## Legend methods on ABS

| Method | On ABS? | Durability | Backlight | Fit for a one-off set of ~16 |
|--------|---------|------------|-----------|------------------------------|
| **UV printing** | Yes | Ink sits on the surface; wears with heavy use | Opaque caps | **Good.** Cheap per key, full colour, any icon (Claude logo, mic). |
| **Laser etching** (coated translucent ABS) | Yes | Moderate; coating can shine or wear | **Shine-through** | Good if you want the status RGB to light the legend. |
| **Double-shot** | Yes (common) | Legend never wears | Can be shine-through | **No.** Needs a mould per legend; bulk only. |
| **Dye-sublimation** | **No**, PBT only | Very durable | Opaque | Only if switching to PBT. |
| **Pad printing** | Yes | Wears easily | Opaque | Not worth it. |

ABS takes dyes and coatings easily but develops shine from finger oil over
time; PBT resists shine. For a pad with 16 keys you will replace if the layout
changes, ABS + UV print is the sensible default.

## Routes

1. **Relegendable caps (cheapest, re-doable).** Two-piece caps with a clear
   cover over a paper or sticker insert. Adafruit 10-pack, off-white
   [AF-5039](https://www.adafruit.com/products/5039) ($4.95 listed) or
   [black](https://www.adafruit.com/product/5662) ($7.50), roughly 18×18×8 mm,
   DSA-like. Print the icons on paper at home. **Best fit while the layout is
   still changing**, since every key here is still subject to change.
2. **Custom UV-printed ABS from a vendor.** WASD Keyboards prints custom
   legends on ABS by direct UV print; reported at about $6–7 per keycap
   ([Drop thread](https://drop.com/talk/21332/custom-printed-keycaps),
   [TechRepublic](https://www.techrepublic.com/pictures/you-really-need-these-custom-keycaps-right-now/)).
   No front printing. About $100 for 16 keys. Current pricing not confirmed.
3. **Laser-etched shine-through ABS.** Pairs with per-key RGB: the
   "awaiting feedback" colour shows through the legend. Max Keyboard did custom
   shine-through sets historically; no current one-off service was confirmed.
   AliExpress custom laser-etch sellers exist but were not checked.
4. **3D-printed caps.** Sources agree **FDM ABS is poor at keycap scale**:
   layer lines show through, raised legends go blocky. Resin is the better
   choice for detail but more brittle and needs post-processing; stem fit has to
   be within a fraction of a millimetre
   ([guide](https://stacksheriff.com/3d-printing/3d-printed-keycaps/),
   [JLC3DP](https://jlc3dp.com/es/blog/how-to-create-3d-printed-keycaps-for-your-keyboard)).
   Viable for one sculpted novelty cap (e.g. an oversized mic key, or the
   Claude figurine idea in `esp32-ott.md`), not for the whole set.

## Recommendation

- **Now:** relegendable caps (route 1) while the layout settles.
- **Final:** UV-printed ABS (route 2) for the set, or laser-etched shine-through
  (route 3) if the build has per-key RGB.
- **Push-to-talk key:** consider a distinct shape or colour (2u, or a
  resin-printed cap) so it can be found without looking, matching the
  "oversized, distinctive PTT keycap" line in `esp32-ott.md`.

Sources not cited inline: [Wikipedia: Keycap](https://en.wikipedia.org/wiki/Keycap)
(dye-sub is PBT-only), [Dygma: how keycaps are made](https://dygma.com/blogs/product-development/how-keycaps-are-made),
[MonsGeek on keycap plastics](https://www.monsgeek.com/kjw1).
