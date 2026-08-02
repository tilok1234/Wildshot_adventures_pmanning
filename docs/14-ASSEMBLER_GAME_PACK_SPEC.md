# Wildshot Adventures — Assembler Game-Pack Export Spec

**Doc:** 14-ASSEMBLER_GAME_PACK_SPEC
**Status:** **APPROVED by the designer 2026-07-27** ("i approve to change
to the other sprite pack i think it will be way better") — binding. The
§0 amendment is applied to docs/12 §2.14 as Amendment v2. The designer
is building the exporter against this spec; the game repo integrates on
pack drop, before M5 enemy work. Ranked behind nothing: this unblocks the
actor-source switch the designer is leaning toward, and the cheap window
closes at M5 (enemy rendering).
**Tool:** `8-bit sprite assembler` (repo `tilok1234/8-bit-sprite-assembler`).
**Consumer:** the game repo's `addons/` importer + view-layer library, the
slice test, and CI — exactly the TileForge / Sprite Forge / UI-kit
pattern: raw drop in `assets/`, validating importer, frozen contract.

---

## 0. §2.14 amendment — APPLIED (docs/12 Amendment v2; heading truthed 2026-08-02, was "Pending … designer to approve")

> **Amendment v2 (proposed):** the 8-bit sprite assembler's game-pack
> export supersedes the Sprite Forge full pack as the actor/effects
> source. Rationale: it is the actively maintained tool (equipment
> compositor, 259-enemy catalog, readability regression suites), and
> switching before M5 costs a morning; switching after Gate 1 costs an
> integration plus re-acceptance. The Sprite Forge pack stays in-repo as
> fallback until the assembler pack passes the slice test and renders
> the player + first two enemies (M5 acceptance); then it is removed.
> Contract rule unchanged: ids, layout, and manifest shape FREEZE at
> pack v1; polish passes change pixels, never the contract.

## 1. What the assembler must add (tool-side work, in priority order)

1. **A `cast` animation** (player-critical): the CORE-34 ability slot
   needs a cast read distinct from attack. Suggested: 3–4 frames, all
   four directions, same 24 px cells. Enemies can reuse `attack` as
   their windup — no enemy cast art needed for Phase A.
2. **A `death` animation** (wanted, not blocking): 3–4 frames. Until it
   exists, the game covers deaths with its kill-flash — acceptable at
   greybox fidelity, so this may ship in pack v2 without breaking the
   contract (new columns append; ids stay).
3. **A deterministic "Export game pack" action** (one click / one CLI
   command — NOT hand-assembled zips): writes the folder layout of §2
   with byte-stable output for identical inputs. The exporter must
   refuse to write if validation (§4) fails.
4. **Export at native 1× (24 px cells).** The current asset-pack sheets
   are 4× (96 px cells) — wasted memory and import time; the engine
   scales. If 1× is disruptive tool-side, record the scale in the
   manifest and the game will divide, but 1× is preferred.

## 2. Export folder layout

```
assembler-pack/
  manifest.json
  players/<id>.png        (one sheet per exported loadout)
  enemies/<id>.png
  effects/projectiles/<id>.png
  effects/impacts/<id>.png
  effects/trails/<id>.png
  effects/statuses/<id>.png
  LICENSE                 (self-produced declaration, PROD-03)
```

Dropped into the game repo at `assets/assembler-pack/` (gdignored raw
drop, committed, like every other forge).

## 3. manifest.json shape

```json
{
  "pack": "wildshot-assembler",
  "version": 1,
  "generated": "YYYY-MM-DD",
  "tool_commit": "<git short hash of the assembler at export time>",
  "cell": 24,
  "export_scale": 1,
  "frame_contract": {
    "dirs": ["down", "left", "right", "up"],
    "anims": [
      { "id": "idle",   "frames": 2, "ms": 420 },
      { "id": "walk",   "frames": 4, "ms": 150 },
      { "id": "attack", "frames": 4, "ms": 115 },
      { "id": "cast",   "frames": 4, "ms": 130 },
      { "id": "hurt",   "frames": 2, "ms": 140 }
    ],
    "layout": "rows = dirs in order; columns = anims in order, frames left to right"
  },
  "actors": [
    {
      "id": "ranger",
      "category": "players",
      "sheet": "players/ranger.png",
      "spec": { "<the exact assembler loadout that regenerates this sheet>": "..." }
    },
    {
      "id": "goblin-scout",
      "category": "enemies",
      "sheet": "enemies/goblin-scout.png",
      "tags": ["chaser"],
      "spec": { "...": "..." }
    }
  ],
  "effects": [
    {
      "id": "arrow",
      "category": "projectiles",
      "sheet": "effects/projectiles/arrow.png",
      "frames": 2,
      "ms": 120,
      "anchor": [12, 12],
      "directional": false
    }
  ]
}
```

Rules the consumer relies on:

- **Everything derives from `frame_contract`** — sheet width must equal
  `Σ frames × cell × export_scale`, height `dirs × cell × export_scale`.
  The game importer computes this from the manifest and never hardcodes
  12 columns; adding `death` later just extends `anims` and the sheets.
- **`spec` per actor = deterministic regeneration** (the assembler
  loadout/enemy def + any seed), same promise as the other forges: a
  polish pass re-exports the same ids from stored specs.
- `tool_commit` makes every pack traceable to the assembler state that
  produced it — the lab's replay data-hash discipline, applied to art.
- Effects carry their own frame counts + anchor (hotspot) — projectile
  sprites rotate around the anchor in the game renderer.
- ids are filenames are ids: lowercase-kebab, stable forever.

## 4. Exporter validations (refuse to export on failure)

1. Every sheet's dimensions match the frame contract exactly.
2. Frame 0 of idle/walk/attack/cast is non-empty for every actor
   (hurt may share attack frames if that is the tool's model — then say
   so in the manifest, don't special-case silently).
3. Binary alpha if that remains the tool's compositing model.
4. Every manifest entry's file exists; every exported file has a
   manifest entry (no orphans either way).
5. manifest.json is valid JSON, UTF-8 **without BOM** (a BOM already
   bit the game repo once today).

## 5. What the game repo does on its side (assistant work, ~half a day)

1. `addons/assembler_importer/` — validates per §4 again (trust but
   verify), copies the roster named in `data/actor_sheet_map.tres` into
   the project, roster-filtered manifest (same flow as spriteforge).
2. View library v2: builds SpriteFrames from the (dir-rows × anim-span
   columns) grid; AnimatedActor's `walk-down` names map 1:1, so the
   actor code barely changes. Render scale from `cell`/`export_scale`.
3. Slice test v2 (manifest-driven, CI) replaces the spriteforge one for
   mapped actors.
4. Player swaps first; the M5 enemies land directly from this pack.
   Sprite Forge pack removed once M5 acceptance passes on the new one.

## 6. Phase A scope guard

The lab imports ONLY the mapped roster (player shell + 6 enemies + 1
elite + the effect sprites the M-FX curation picks). The other ~250
actors stay in the assembler — same scope tripwire as every pack.
