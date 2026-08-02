# Starhook — tuning sheet

Sim runs at **30 ticks/s**, 1 tile = 32 px, internal canvas 640×360. `t/s` = tiles per second.
**[repo]** = verbatim from Wildshot-Adventures data files · **[proto]** = my tuning, flagged for designer eyes.

## Rifter
| Value | Amount | Source |
|---|---|---|
| Stability (HP) | 60 | [repo] balance_frame.json starhook.rifter.base_hp |
| Move speed (rift) | 3.6 t/s | [repo] starhook.rifter.speed_tiles |
| Move speed (overworld) | 4.2 t/s | [proto] |
| Hurtbox | r 3.5 px | [proto] bullet-hell-small |
| I-frames | 15t (0.5s) | [proto] |
| Passive stability drain | 0.4/s (×1.4 hooked) | [proto] session clock |
| Deep-edge extra drain | +2.2/s | [proto] |

## Undertow
| Value | Amount | Source |
|---|---|---|
| Base pull | 1.35 t/s (× tweak) | [proto] |
| Oscillation | ±25°, ~26s period | [proto] |
| While hooked | ×1.35 | [proto] |
| On bullets / boss | ×0.15 / ×0.3 | [proto] |

## The Catch
| Value | Amount | Source |
|---|---|---|
| HP common / rare | 260 / 420 (× tweak) | [repo] rift_catch.tres / rare step [proto] |
| Phases | 66% / 33% | [repo] |
| Move speed | 2.2 t/s (×1.3 in P3) | [repo] / [proto] |
| Keep-range | 4–6 tiles (P3: ~4.5) | [repo] range_min/max |
| Hurtbox | r 16 px (0.5t body) | [repo] body_radius |
| Contact damage | 0 | [repo] |
| Rare cooldown mult | ×0.85 | [proto] "denser" |

### Emitters (telegraph / cooldown / recover, ticks)
| Pattern | P1 | P2 | P3 | Source |
|---|---|---|---|---|
| star_spray 24/·/16 | cd 96 | 84 | 72 | [repo] |
| rift_ring 36/·/20 | — | 168 | 168 | [repo] |
| star_dart 40/·/18 | — | — | 150 | [repo] |

### Shots
| Pattern | Shots | Speed | Dmg | TTL | Source |
|---|---|---|---|---|---|
| star_spray | 4 × 45° arc, aimed | 5.5 t/s | 10 | 50t | [repo] |
| rift_ring | 10 × 36° | 4.0 | 10 | 60t | [repo] |
| star_dart | 2 × ±7°, intercept (lead 40t, ½ applied) | 8.0 | 12 | 48t | [repo] |
| void ring twist | 12 shots, 3.4 t/s | | | | [proto] |
| comet twists | spray 6.3 t/s · dart cd ×0.8 | | | | [proto] |

## Rods
| Rod | Cadence | Shots | Dmg | Speed | Source |
|---|---|---|---|---|---|
| Cane | 22t | 1 | 6 | 14 t/s | [repo] dmg/speed; cadence 30→22 [proto] to hit the "~9 dps ≈ half-minute fight" note in rift_catch.tres |
| Splitwillow | 26t | 3 (±12°) | 4 | 12 | [repo] pattern; cadence 36→26 [proto] same ratio |
| Heavyline | 44t | 1 | 16 | 9 | [proto] |
| Twinreed | 14t | 2 (±3°) | 3 | 15 | [proto] |

## Reel
| Value | Amount |
|---|---|
| Reel rate (calm, holding) | +28/s of 100 |
| Decay (not holding) | −4/s |
| Thrash cost (holding) | 6 stability/s × drain tweak |
| Calm / thrash duration | 55–95t / 34t |

## Economy
| Value | Amount | Source |
|---|---|---|
| Gold common / rare | 30–60 / 80–150 | [repo] catch_gold |
| Rare chance | 0.2 (tweak) | [proto] |
| Bag cap | 60 | [proto] |

## Tweaks → engine mapping
| Tweak | Effect |
|---|---|
| undertowStrength (0–2.5) | multiplies undertow pull |
| stabilityDrainMult (0.25–3) | multiplies ALL stability loss (hits, passive, thrash) |
| bossHpMult (0.25–3) | catch max HP at spawn |
| rareChance (0–1) | rare roll per cast |
| biomeOverride | forces the biome at cast time |
| rod / autofire | live-sync with R / F keys |
| showHitboxes | debug circles |
