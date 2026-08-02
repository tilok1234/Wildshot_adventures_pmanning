# STARHOOK — prototype

> **PRESERVED VERBATIM — the prototype's own doc. READ INDEX.md
> FIRST:** the INDEX's corrections block is LAW over everything in
> this file. Known superseded content below: the retired word
> "undertow" (never use it anywhere), the reel/"HOOKED" win (the
> reel is CUT — win = the kill), the entity drag (cut — the pull
> lives in the line only), and the prototype's reversed keys
> (game truth: F = cast/interact, E = autofire).

A playable prototype of **starhooking** for Wildshot Adventures: fishing rifts that spawn anywhere on land — cast your line into one and the screen splits 50/50, your body stays in the world while your star-projected self fights the catch in another galaxy.

**Play:** open `Starhook Prototype.dc.html` in a browser. Everything is client-side; progress saves to localStorage.

## Controls
| Input | Action |
|---|---|
| WASD / arrows | Move (and fight the undertow in the rift) |
| Mouse | Aim (always manual — no auto-aim) |
| LMB (hold) | Fire rod / **reel** when hooked |
| E | Cast at a rift · dismiss catch card |
| R | Swap rod (Cane, Splitwillow, Heavyline, Twinreed) |
| F | Autofire toggle (trigger only; aim stays on the mouse) |
| T | Reshuffle world/rifts · P pause |

## The loop
1. Find a rift portal (3 up at any time: nebula / void / comet).
2. `E` casts the starhook — screen splits, fight begins in the undertow arena.
3. Beat the Rift Catch through 3 phases (spray → ring → intercept darts) while the undertow drags you toward the deep. Your **line stability is your health**; it also drains slowly over time and fast at the deep edge.
4. At 0 HP the catch is **HOOKED** — hold LMB to reel during calm, ease off during thrashes.
5. Banked: fish + gold to your bag, portal collapses, a new one surfaces. Snapped line: you lose the dive, find another rift.

## Files
- `Starhook Prototype.dc.html` — entry point + tweak-panel definitions
- `engine.js` — the whole game (sim, boss, rendering, save)
- `assets/` — sprites/font cut from the Wildshot-Adventures repo (read-only source; nothing in the repo was modified)
- `docs/` — design + handoff documentation

## Docs
- [docs/DESIGN.md](docs/DESIGN.md) — mechanics, arena, boss, biomes, fish tables
- [docs/TUNING.md](docs/TUNING.md) — every number, its value, and where it came from
- [docs/HANDOFF.md](docs/HANDOFF.md) — porting notes for the Godot implementation
