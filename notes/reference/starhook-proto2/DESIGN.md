# Starhook — design doc

## Concept
Starhooking is Wildshot's fishing: portals ("rifts") spawn anywhere on land. Casting into one is instant — no bite-wait minigame. The cast IS the aggro: the moment the line crosses, the fight is on. The screen splits 50/50 — **left: your body holding the rod in the overworld; right: the undertow arena in another galaxy**. The line is the star of the show: it crosses both panes, sags when slack, snaps taut and red under tension.

## The undertow (the arena)
- 300×340 px fighting space, fully visible in the right pane — no off-screen bullets, ever.
- A constant current pushes the rifter away from the portal mouth toward the **deep edge** (right side, shimmering). Direction oscillates slowly (±25°). WASD fights it; bullets and the boss also drift slightly with it.
- Standing in the deep edge overstretches the line: stability drains fast there.
- **Line stability = HP** (60). Bullet hits cost their damage; a passive drain (0.4/s) is the session clock. Stability 0 → the line snaps: dive lost, portal collapses.

## The Catch (boss)
One rift kit at two rarity steps (common 260 HP / rare 420 HP, 20% base). Star-fish rendered from a pixel map, tinted per biome, gold when rare. No contact damage — pure bullet hell.

Phases by HP (66% / 33%):
1. **THE DRIFT** — keep-range star sprays (4-shot 45° aimed arc).
2. **THE COIL** — the rift ring joins (10 shots × 36°; the gaps are the answer).
3. **THE THRASH** — hunts closer + intercept star darts aimed at where you're *going*; change direction during the telegraph.

Telegraphs: sprays show an aim cone, rings a contracting circle, darts a dashed intercept line to the locked point.

## Hooked → reel
Boss at 0 HP: bullets clear, the catch is on the line. Hold LMB to reel (progress bar). The fish alternates **calm drift** (reel: +28/s) and telegraphed **thrash bursts** (reeling then costs 6 stability/s — ease off). Undertow strengthens ×1.35 while hooked. Reel to 100 → banked.

## Rods (R to swap)
| Rod | Pattern | Cadence | Notes |
|---|---|---|---|
| Cane Rod | 1 bolt, 6 dmg, 14 t/s | 22t | repo baseline |
| Splitwillow | 3-bolt 12° fan, 4 dmg | 26t | repo baseline |
| Heavyline | 1 sinker, 16 dmg, 9 t/s | 44t | prototype extrapolation; hitstop + shake |
| Twinreed | 2 needles ±3°, 3 dmg | 14t | prototype extrapolation |

Autofire (F) holds the trigger only — **aim is never automated**.

## Biomes & fish tables
Roll at cast; portals show their biome. Rarity roll is per-cast (tweakable).

| Biome | Arena flavor | Pattern twist | Common fish (45/35/20) | Rare |
|---|---|---|---|---|
| Nebula Drift | violet wisps, crystals | baseline | Emberwisp Koi · Dustfin Drifter · Pulsar Gulper | Novaback Leviathan |
| Hollow Void | near-empty, runestones | ring: 12 shots, slower (3.4) | Hollow Angler · Umbral Eel · Silence Carp | Event Horizon Maw |
| Comet Field | streaks, glow mounds | spray 6.3 t/s, dart cd ×0.8 | Icetail Darter · Streakfin Herring · Cinder Sprat | Harbinger Pike |

Gold: common 30–60, rare 80–150 (repo `catch_gold`). Length roll is cosmetic flavor on the catch card.

## Persistence
`localStorage["starhook_proto_v1"]`: gold, bag (≤60), casts/catches/snaps, rod, autofire.

## Tweaks panel (design surface)
undertowStrength · stabilityDrainMult · bossHpMult · rareChance · biomeOverride · rod · autofire · showHitboxes — all live; see TUNING.md.
