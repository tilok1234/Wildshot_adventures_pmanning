# Wildshot Adventures — Icon Set Assessment & Plan (the "icon forge" round)

**Doc:** 21-ICON_SET_PLAN
**Status:** Assessment designer-requested 2026-07-31 ("help me asses all the different kinds of icons for like item tooltips and skills and all of that cause im working on planning an icon forge"). **Taxonomy approved** same evening ("and all of those icons sounds good ye"). **Seat ruling [P]** recorded below. Sizes and phasing are staged recommendations — consuming them is the ruling, same as every forge contract (frozen once the game consumes v1). Register: docs/08 Tooling contracts + sync log sl-0062.
**v0.1 ARRIVED (2026-08-01 staleness-audit stamp):** the designer
BUILT the set — `wildshot-icons-proto` 0.1.0, 470 glyphs, all
16×16, T1–T5 complete, CORE-50 proof sheets shipped in-pack —
assessed PASS against §3–§6 of this plan (sl-0083), intaken and
gate-guarded game-side (sl-0085), and WIRED since S0 seam 4
(2026-08-01: the atlas lives in the HUD + creation screen; the
Loop-acceptance hold dissolved with sl-0098; quest icons extend
use via sl-0121). Known dormant glyph: item.unique.undertow
carries a retired word — never bound, tripwired game-side,
purges at the next icons release. The "Tier 0 could ship as uikit v2" path in §7 is
SUPERSEDED by the real pack; §3's table now serves as the coverage
checklist it was assessed against. Watch-items for wiring: skill-
node readability in the real tree UI; a deutan-sheet glance.
**Consumer:** the game repo, at two horizons — a tiny Tier-0 set the Loop's minimal equip surface can consume near-term, and the Part II interface module (inventory/tooltips, skill trees, maps, collection book) post-Gate 1.
**Ranking:** strictly behind M-FX and all Gate-1-critical work, exactly like the UI kit (doc 13). Planning is free; building waits.

---

## 1. Seat ruling [P] (designer, 2026-07-31)

The icon set is **NOT** built inside the sprite assembler ("i dont
think i should risk messing up sprite assembler by putting it in
there") and is **NOT** a new repo in the ecosystem ("im not gonna
put it in our repo collecction either i think cause icons is more a
1 time set thing like projectiles i think").

**It follows the `wildshot-projectiles-sphere-v0` precedent** (the
lock's only "producer: game (in-repo generator)" entry): a
deterministic generator living in the game repo, producing a
one-time-ish versioned set (`assets/wildshot-icons-v0/`-style raw
drop, `.gdignore`d) with full regen capability. No doc 16 repo
registration, no lock lane, no sync-protocol lane — in-repo
producer entries in the lock only, at consumption time.

Consequences: no cross-repo transport (no releases/tags needed);
the "forge" is a game-repo tool + config; contract freezes at first
consumption like every forge (ids/manifest frozen, pixels
swappable).

## 2. What already exists (do not re-author)

- **Chrome icons are DONE:** the doc 13 UI kit shipped and is
  consumed (12×12 set: gear/keyboard/mouse/audio/eye/warning/
  close/arrow_down + autofire on/off + export/replay). That
  contract stands untouched.
- **Sprite Forge renders cover creatures:** bestiary entries, boss
  presentation, and collection-book creature imagery derive from
  the 231-actor pack (128 enemies, 34 bosses) — icon-sized crops/
  renders of existing actors, never hand-re-authored glyphs.
- **World-space stays sprite territory:** ground drops, portal
  objects, overhead markers are Sprite Forge/actor assets. The icon
  set owns SCREEN-SPACE glyphs only.
- **No consumable system exists in the spec** (no potions, ammo,
  combat consumables by crafting rule). Zero icons budgeted; a new
  category only if the design ever adds one.

## 3. The taxonomy (approved 2026-07-31)

| # | Kind | Shows up in | Driver | Rough count | Horizon |
|---|------|-------------|--------|-------------|---------|
| 1 | Weapon frames | inventory, tooltips, vendor, stash | class-exclusive frames; arsenal open | ~12–24 base | Loop has T1–T5 drops now (placeholder) |
| 2 | Ability items | same + HUD ability slot | "large pool per class"; the loot-hunt identity slot | ~50–90 | few now; pool post-Gate 1 |
| 3 | Armor | inventory/tooltips | archetype give-and-take × class | ~9–18 base | few now |
| 4 | Rings | inventory/tooltips | situational-tradeoff family | ~8–15 base | later |
| 5 | Uniques (all slots) | tooltips, collection | one-off authored identity per named source | ~20–40 launch, grows | first unique is in the loop spec |
| 6 | Access & quest items | inventory, gate prompts | dungeon portals, keys, raid skip-trophies, quest items | ~15–30 | portals early |
| 7 | Currency / meta | HUD, vendor, death recap | gold; attempt counter etc. | ~3 | gold in the loop now |
| 8 | Stat icons | tooltips, character sheet | lean stat set: 7 + 2 regen candidates | 9 | with the first real tooltip |
| 9 | Skill-tree nodes | 3 class trees | large point-by-point tree, behaviour-changing nodes | ~90–180 | Part II interface module |
| 10 | HUD status | in-run HUD | guard/immunity/protection, casts, boss presentation | ~10–20 | gated on COMBAT-21 |
| 11 | Map & travel markers | world/zone map, minimap | hubs, auto-travel lock states, dungeons, world bosses, quests, landmarks, fishing/foraging | ~15–25 | post-Gate 1 |
| 12 | Collection book | the endgame horizon UI | fish + flower species, cosmetics, skins, mounts, pets, trophies/titles | ~80–160, grows forever | post-Gate 1; longest tail |
| 13 | Quest & faction | journal, NPC overheads | categories/states + one emblem per faction | ~15–20 | Part II |
| 14 | Chrome/system | options, panels | **shipped** (doc 13 uikit) | done | — |
| 15 | Input glyphs | tutorials, remapping | TECH-18 (deferred); kb/mouse (+controller?) | ~40–80 or a CC0 set | UI finalization |

**Launch-scope total: roughly 350–600 authored glyphs** before
tier/theme variants (which the generator derives, §5). The
identity-critical hard 40%: ability items, skill nodes, uniques —
each glyph must *communicate behaviour* (§4). Armor/ring/tier
ladders are the mechanical easy 60%.

## 4. Binding rules the set inherits (no new rulings needed)

1. **1× authoring in the 640×360 viewport, integer scale only,
   binary alpha** (doc 13 ground rules; forge compositing model).
2. **CORE-50 — never hue-alone:** tier/rarity/state distinctions
   carry a shape/value marker (frame pips, corner notches); color
   is garnish. Survives colorblind simulation.
3. **CORE-19 — no casino aesthetics:** no gold-burst rarity
   frames, no slot-glow. Rarity language is quiet and shape-first.
4. **Law 6 for HUD-visible glyphs** (ability slot, status pips):
   chrome band discipline — never competing with telegraphs.
   Menu-only glyphs are freer.
5. **"Behaviour communicated before it's farmed"** (docs/01 §9):
   ability-item and unique glyphs say what the thing DOES.
6. **Forge doctrine:** manifest-driven, deterministic regen,
   frozen id contract at first consumption, placeholder-fidelity
   first with polished swaps under the same ids.

## 5. The generation model (what makes this generator-shaped)

The design already specs composability: **"tier upgrades preserve a
familiar style while improving numerically"** + T1–T5 locked in the
loop frame. So:

1. **Base glyph** — the identity (hand-authored or parametric).
   Authored ONCE per identity.
2. **Material/tier ramp** — T1–T5 recolors, generated (the theme-
   remap trick the forges already use, role-keyed palette).
3. **Frame/rarity treatment** — shape-marked, quiet, generated.
4. **States** (locked/disabled/cooldown/invested) — **runtime
   treatments in the game, never authored variants** (the doc 13
   state model: value step, dim, outline; cooldown sweep is a
   shader). Keeps the atlas linear, not combinatorial.

Species sets (fish, flowers) are parametric families — authored
bounds, generated variation, exactly the "the where is authored,
the what varies in a known pool" philosophy.

## 6. Size system (recommendation, consumed = frozen)

**One new canonical size: 16×16** for all item/skill/collection
glyphs. 12×12 chrome stands (shipped contract). Optional 8×8
micro-pips for map dots/status only if needed. Tooltips/collection
reuse the same 16×16 asset integer-scaled (2× hero render in a
detail pane) — never a second authored size; every extra size
multiplies the entire §3 bill.

## 7. Phasing

- **Tier 0 (cheap, near-term):** ~15–25 glyphs the Loop's equip
  surface consumes as placeholders today — loop weapon frames,
  armor, ring, ability item, gold, portal, the first unique, the
  9 stat icons. Could ship as **uikit v2** under the existing
  manifest before any generator exists.
- **Tier 1 (the set proper):** equipment pools + skill trees +
  HUD status — sits on Part II interface answers (COMBAT-21,
  UX-14, inventory/tooltip layout).
- **Tier 2:** maps, collection book, quest/faction, input glyphs.
- **Ranking:** strictly behind M-FX / Gate-1-critical work.

## 8. Contract sketch (for the eventual build session)

Game-repo generator (projectiles precedent) → versioned raw drop
`assets/wildshot-icons-v0/` with `manifest.json`: set id, version,
palette roles (dusk first), and per-glyph entries
`{ id, file, size, kind, tier?, family? }` with semantic ids
(e.g. `item.weapon.<class>.<frame>.t<1-5>`, `skill.<class>.<node>`,
`stat.<name>`, `map.<marker>`). Importer builds the atlas/Theme
additions; a slice test asserts dimensions + manifest completeness.
**TECH-16 becomes mechanical:** an importer test asserts every
item/skill/content id resolves to an icon id — the "missing icons"
validation the questionnaire anticipates.

## 9. Open questions this plan deliberately sits on

COMBAT-21 (HUD vs world info → status set) · UX-14 (whether icons
are the ONLY equipment visualization — if yes their identity job
heavies) · TECH-18 (input glyphs; CC0 set is a legal option under
PROD-03) · faction count · fish/flower species counts · exact
inventory/tooltip cell layout (Part II). None block Tier 0.
