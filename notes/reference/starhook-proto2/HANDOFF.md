# Starhook — Godot handoff notes

The prototype is a browser feel-check for the starhook slice (S1 seam 6, sl-0105). Nothing in the Wildshot-Adventures repo was modified; assets were copied out read-only.

## What maps straight back to the repo
- **Data rows already exist**: `data/enemies/rift_catch.tres` (phases/emitters), `data/enemies/patterns/{star_spray,rift_ring,star_dart}.tres`, `data/weapons/{rod_cane,rod_splitwillow}.tres`, `data/balance_frame.json → starhook` (rifter row, catch_gold). The prototype reads as a validation of those numbers — deltas are flagged [proto] in TUNING.md.
- **New rods**: Heavyline / Twinreed are two more weapon_frame data rows (same shot_def schema: cadence_ticks, angle_offset_deg, speed, radius, damage, ttl_ticks). No new systems.
- **Arena**: prototype uses ~9.4×10.6 tiles fully-visible instead of the repo's 15×12 `arena_rift.json`, because the split here is 50/50 (viewport 640×360 → 10 tiles of width per pane). If the 50/50 split is kept, the arena JSON should shrink or the rift camera needs to guarantee full-arena visibility (Law 1: no threat under an overlay/off-screen).

## Deviations / decisions to review
1. **Cast is instant** (E at the portal) — the stand-still "stillness cast" from gather_step.gd was cut per design direction: portal interaction starts the fight, no hooking minigame.
2. **Stability = HP + clock**: passive drain (0.4/s) + deep-edge strain gives the dive a soft timer. New vs repo; tune via stabilityDrainMult.
3. **Undertow**: arena-wide current (1.35 t/s, oscillating) affecting player 100% / boss 30% / bullets 15%. New system, the arena's identity — worth a real .tres if adopted.
4. **Reel finisher**: calm/thrash state machine replaces "kill = win". Numbers in TUNING.md §Reel.
5. **Biome twists** are pattern-parameter overrides only (void ring 12×3.4, comet spray 6.3 / dart cd ×0.8) — expressible as per-biome pattern .tres variants.
6. **Rarity**: rare = 420 HP + cooldowns ×0.85 + gold 80–150 + gold skin. The repo's 35% Starlit Cast cosmetic drop is NOT in the prototype.
7. **Tick rate**: prototype sims at 30 t/s and treats repo tick counts 1:1. If the game runs 60Hz physics, telegraph/cooldown tick values here read as *half-seconds×60* — re-check cadence maths (cane 30t was retuned to 22t here to match the "~9 dps" comment).

## Presentation notes (worth porting)
- The line is drawn across both panes: sag ↔ tension, red at high tension, a spark travelling from rod to portal. Body-side portal pulses while a fight is live.
- Bullets render ABOVE actors; telegraphs: cone (spray), contracting ring (ring), dashed lead-line + box (dart).
- Split transition: rift pane slides in over ~11 ticks; divider is a glowing seam with a travelling spark.
- Deep edge = biome-accent shimmer strip; undertow direction shown by drifting edge arrows + flow particles.

## Asset provenance (assets/)
| File | Repo source |
|---|---|
| character-ranger.png | assembler/players/ (24px frames, 12 cols: idle 0-1, walk 2-5, attack 6-9, hurt 10-11; rows down/left/right/up) |
| props.png, grass_on_soil.png, soil_base.png, dirt_path.png, tall_grass_overlay.png | tileforge/ (32px art on 36px pitch: margin 2, spacing 4) |
| bolt.png, pellet.png, orb-*.png | assets/wildshot-projectiles-sphere-v0/sprites/ |
| panel.png, tooltip_panel.png, bar_*.png, cursor_crosshair.png | assets/uikit/ |
| wildshot_pixel.ttf | assets/uikit/font/ |
| crystal_field_decal.png, rune_circle_decal.png | tileforge/ (copied, unused so far) |

## Prototype architecture (for reading, not porting)
`engine.js` single module: fixed 30Hz sim + rAF render, state machine `title → world → rift → collapse`, pre-rendered ground/arena backgrounds, y-sorted talls, `window.__shk` debug API (cast(), setBossHp(), hook(), snap(), tick(n)…) for automated testing.
