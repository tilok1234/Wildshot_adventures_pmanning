# Wildshot Adventures — UI Style Kit Spec (optional art task)

**Doc:** 13-UI_STYLE_KIT_SPEC
**Status:** Pre-registered optional art task, designer-committed 2026-07-27 ("i could make ui style kit i suppose"). **Ranked strictly behind M-FX (the effects pack)** — M-FX is on the Gate 1 critical path; UI chrome is not. If kit evenings would eat M-FX evenings, the kit waits and the lab ships engine-default grey UI (acceptable — zero Gate 1 evidence depends on UI looks).
**Consumer:** the game repo wires the kit into a Godot Theme resource at M3 (options screen) and M4 (HUD, death recap); M8 tester start screen reuses the same pieces. If the kit is absent at M3, Godot defaults ship and the kit drops in later as a pure swap.
**Contract rule (same as Sprite Forge / TileForge):** piece ids, file names, 9-slice margins, and manifest shape are FROZEN once the game repo consumes v1. Polish passes change pixels, never the contract.
**2026-08-01 stamp:** the kit shipped and is consumed; this 12×12 chrome contract stands unchanged. The ICON SET arrived as its own pack (docs/21, `wildshot-icons-proto` — 16×16, separate manifest). **2026-08-02 truth-up:** §3's out-of-scope hold is no longer current — the slice era reached those screens: inventory + the equipment pane routed (sl-0116/0128), loot-bag panel (sl-0129), bank (sl-0130), vendors v1 (sl-0131), the C sheet is the live quest log with the quest-pull kit building (sl-0121), and boss + line bars are live in play. Collection book and the skill-tree screen remain future. New surfaces reuse this kit's chrome + the icon pack under the frozen contract.

---

## 1. Ground rules (binding, from the register)

1. **Authoring resolution is 1× base-res pixels.** The UI renders inside the 640×360 viewport and integer-scales with the game. Author every piece at 1×: body font ~7–9 px cap height, button rows ~14–16 px tall, icons 12×12. No fractional sizes anywhere.
2. **Law 6 applies to chrome.** The kit is *quiet*: dusk-neutral values (dark violet-greys from the dusk theme palette), at most **two accent hues**, and the whole chrome value range stays visibly dimmer than the hostile-telegraph channel. The HUD sits one band below the debug overlay and above telegraphs (docs/12 §2.5 band 9) — it must never compete with them for the eye.
3. **States never differ by hue alone** (CORE-50 colorblind rule, applied to UI): hover = value step, pressed = 1 px content inset, disabled = dimmed, focus = a drawn 1 px outline. Shape/value first, color as garnish.
4. **No animated or flashing UI.** Static textures only; no luminance flips (photosensitivity baseline).
5. **Binary alpha** — a pixel is fully opaque or absent (matches the forge compositing model). Shadows, if any, are solid dark or dithered, never soft alpha.
6. **No casino aesthetics** anywhere in the kit's visual language (CORE-19) — no gold-burst frames, no slot-machine glow. Heroic fantasy with bite, clean.
7. **Font must be OFL or CC0 licensed** (self-produced-only budget, PROD-03); license file ships inside the kit and the manifest records it. Latin basic coverage is enough (localization is deferred, TECH-18).

## 2. Deliverable — Tier 1 (what M3/M4 actually consume)

| Piece | File(s) | Size / notes |
|---|---|---|
| Panel (standard) | `panel.png` | 9-slice, ≥12×12 px, ~4 px corner margins; the options/death-recap background |
| Panel (dark inset) | `panel_inset.png` | 9-slice; for list wells and the recap hit-trace area |
| Button ×5 states | `button_normal.png`, `button_hover.png`, `button_pressed.png`, `button_disabled.png`, `button_focus.png` | 9-slice, row height 14–16 px at 1×; pressed reads as 1 px inset; focus is an outline style usable OVER other states |
| Checkbox | `check_on.png`, `check_off.png` | 12×12; the ON state carries a drawn check mark (shape, not color) |
| Slider | `slider_track.png` (9-slice, ~6 px tall), `slider_grabber.png`, `slider_grabber_focus.png` (~10×14) | volume / effect-density / opacity / text-scale rows |
| Focus outline | `focus_ring.png` | 9-slice 1 px bright outline; keyboard navigation must be visible on every control |
| Font | `font/<name>.ttf` + `font/LICENSE` | pixel font, ~7–9 px cap height, clean at integer multiples only |
| Pointer cursor | `cursor_pointer.png` | 16×16, hotspot (0,0) recorded in manifest |
| Aim crosshair | `cursor_crosshair.png` | 9×9 or 11×11 (odd — true center pixel), hotspot center; light core + 1 px dark rim so it survives every floor in the dusk arena |
| HP bar | `bar_frame.png` (9-slice), `bar_fill_hp.png` | frame ~64×8 at 1×; fill is a tileable strip |
| Mana bar | `bar_fill_mana.png` | same frame; HP vs mana differ by position + icon, and the fills should also differ by subtle pattern, not hue alone |
| Autofire indicator | `icon_autofire_on.png`, `icon_autofire_off.png` | 12×12; ON/OFF differ by shape (e.g. filled vs hollow), not color |
| Icon set (8) | `icon_gear.png`, `icon_keyboard.png`, `icon_mouse.png`, `icon_audio.png`, `icon_eye.png`, `icon_warning.png`, `icon_close.png`, `icon_arrow_down.png` | 12×12 each, 1-bit-ish silhouettes that read at 1× |

## 3. Deliverable — Tier 2 (M8 tester screen; make only if Tier 1 was cheap)

Tabs (selected/unselected styleboxes) for the options categories · dropdown (reuses button states + `icon_arrow_down` + a popup panel + item-hover stylebox) · vertical scrollbar (track + grabber) · LineEdit normal/focus (comments box, seed field) · tooltip panel · `icon_export.png`, `icon_replay.png`.

**Explicitly OUT of kit scope (post-Gate 1, interface module):** map screen, minimap, collection book, inventory/equipment, skill tree, quest journal, vendor/crafting screens, boss bars. Do not design these yet — they sit on undecided Part II questions. *(2026-08-02: this hold is SPENT for inventory/equipment, quest log/tracker, vendor, bank, and boss bars — routed or live in the slice (sl-0116/0128/0129/0130/0131/0121). Map screen, minimap, collection book, and the skill-tree screen remain future.)*

## 4. Manifest (machine-readable, ships in the kit root)

```json
{
  "kit": "wildshot-ui",
  "version": 1,
  "generated": "YYYY-MM-DD",
  "scale": 1,
  "theme": "dusk",
  "palette": { "chrome_dark": "#..", "chrome_mid": "#..", "chrome_light": "#..", "accent_1": "#..", "accent_2": "#.." },
  "font": { "file": "font/<name>.ttf", "license": "OFL", "size_px": 9, "line_px": 12 },
  "pieces": [
    { "id": "panel", "file": "panel.png", "kind": "nineslice", "margins": [4, 4, 4, 4], "min_size": [12, 12] },
    { "id": "cursor_crosshair", "file": "cursor_crosshair.png", "kind": "cursor", "hotspot": [5, 5] },
    { "id": "button_normal", "file": "button_normal.png", "kind": "nineslice", "margins": [3, 3, 3, 3] }
  ]
}
```

Every piece appears in `pieces[]` with real margins/hotspots — the game repo's Theme importer reads the manifest, never guesses. Palette entries are **role-keyed** so forest/autumn/winter variants later are a palette remap under the same ids (exactly the Sprite Forge theme model). One `theme` per kit export; dusk first (it's the lab arena).

## 5. Acceptance checklist (run before handing the kit over)

1. A mock options screen at 1× in a 640×360 viewport is fully legible, and again at ×2 UI scale — integer multiples only, no blur (CORE-50 UI/text scaling).
2. Every interactive state pair distinguishable under color-blindness simulation (any common simulator): state changes survive with hue removed.
3. Screenshot the HUD pieces composited over the dusk arena preview (game repo `tests/pixel_match/arena_preview.png`): chrome stays quieter than the wall band; nothing in the kit is the brightest thing on screen (Law 6 / band sanity).
4. No animated pieces; no pure-white or saturated-flash fills.
5. All alpha binary; no soft edges against transparency.
6. `manifest.json` lists every shipped file; ids follow the table above; font LICENSE present.

## 6. Integration path (game repo, M3 — for the build session)

`addons/uikit_importer/` reads `manifest.json` → builds `res://ui/theme.tres` (StyleBoxTexture per 9-slice piece, FontFile, icons) + registers the cursors. Kit lives at `assets/uikit/` (raw drop, `.gdignore`d, same as the other forges). A `tests/` slice check verifies each piece's PNG dimensions ≥ its margins and every manifest file exists. If no kit is present, M3 ships Godot defaults — the importer is written either way, so the kit drops in whenever it lands.
