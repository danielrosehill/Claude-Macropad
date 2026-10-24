# Keycap Printing Options (ABS)

How to get 12 legended or icon keycaps (see [`../key-layout.md`](../key-layout.md); legend files in [`../keycaps/`](../keycaps/))
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

## Artwork requirements (checked 2026-10-24)

No vendor found publishes a print-area size, safe margin or minimum stroke for
a 1u UV legend. What is published:

- **Krome Keycaps** (UV-printed custom 1u caps, OEM/DSA/Cherry/MA profiles,
  PBT): upload an SVG/vector file or a high-resolution image in the product
  builder; mock-up in 1–3 working days
  ([builder](https://kromekeycaps.com/products/create-your-own-custom-keycap),
  [DSA](https://www.kromekeycaps.com/products/create-your-own-custom-dsa-keycap)).
  Price not read (page rate-limited). A second candidate vendor for route 2.
- **GMK** wants `.svg` for any new legend and does extra colours by UV print
  ([guidelines PDF](https://gmk.net/fileadmin/user_upload/faq/Guidelines_for_Custom_GMK_Keycap_Set_14.pdf));
  group-buy scale, not a one-off.
- **General UV print** (not keycap-specific): vector with text converted to
  outlines, or raster at 300 dpi or more at print size
  ([Markertek](https://www.markertek.com/attachments/customforms/markertek-logo-requirements-for-uv-printing.pdf)).
- **Double-shot cutter limits** quoted on Deskthority (molded legends, not UV;
  the thread notes the source has errors): line width 0.012–0.025 in
  (0.3–0.6 mm), gaps 0.020–0.035 in (0.5–0.9 mm)
  ([thread](https://deskthority.net/workshop-f7/fixing-signature-plastics-shift-key-legends-digitally-t11522-150.html)).
  Used here as a conservative floor: the legends in `keycaps/` use 0.78 mm strokes.
- **Adafruit relegendable caps**: cap is 18.0 × 18.0 × 8.0 mm; the window under
  the clear cover is not specified, so measure before cutting
  ([AF-5039](https://www.adafruit.com/product/5039): $4.95 at 1–9 units, $4.46 at 10–99).

So: send `keycaps/outlined/*.svg` (fonts outlined) and keep `keycaps/png/` as
the raster fallback; ask the vendor for their template before ordering.

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
