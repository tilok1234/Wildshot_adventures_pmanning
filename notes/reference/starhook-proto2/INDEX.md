# Starhook Prototype #2 — planning's reconciliation (2026-08-02 morning)

Built by the designer overnight (done before bed; clips at 04:40 +
04:42 in Videos\Screen Recordings; the half-typed handoff message
finished after waking — the designer fell asleep sending it).
Delivered as `C:\Users\headc\Downloads\Starhook Prototype Build.zip`
— a self-contained HTML/JS build (engine.js, 30Hz fixed sim, a
__shk debug API for automated testing) using the game's own font,
sprites, and data values. The three docs preserved here VERBATIM
(DESIGN.md / TUNING.md / HANDOFF.md) are the prototype's own
spec, tuning sheet, and Godot handoff notes. Every value is
tagged [repo] (verbatim from Wildshot-Adventures data — the
prototype VALIDATES the built kit's numbers) or [proto] (its own
tuning, flagged for the designer's eye — all land as [T]).

## The law order

PROTOTYPE DOCS > the canonical paragraph > everything earlier.
The prototype is the designer's newest artifact and supersedes
where they conflict.

**CALIBRATION (the designer, on delivery):** "this is just the
overall concept of it and just a prototype i made in a haste so
we will have to do some refining to it." Read: the prototype
rules the SHAPE — the verbs, the split, the living line, the
undertow, kill-then-reel, biomes — while EVERY NUMBER is [T] and
refinement rounds are expected, scheduled work (the boss-round
pattern). The seam builds the shape faithfully so the designer's
refining happens on the real thing, in Green hands, not on paper.

## Ruled BY the prototype (supersessions, all the designer's own)

1. **Split = 50/50** (supersedes the 2/3–3/4 lean; the line
   crossing both panes is the star — sag ↔ taut, red under
   tension, a spark travelling rod→portal).
2. **The cast is INSTANT** — interact at the portal starts the
   fight; no stillness wind-up, no bite-wait ("the cast IS the
   aggro").
3. **Line stability = HP = 60** — one resource: bullet hits,
   passive drain 0.4/s (the session clock), deep-edge strain
   +2.2/s; 0 = snap, dive lost.
4. **Kill THEN reel** — resolves the canonical either/or: damage
   wins the fight (boss to 0 → bullets clear → hooked), the REEL
   wins the catch (hold +28/s in calm, thrash bursts punish
   greed at 6 stability/s; the pull strengthens ×1.35 while
   hooked; 100 = banked).
5. **The deep edge replaces depth bands** — depth became spatial:
   the far strip strains the line.
6. **Every cast is a fight** — the big-hook-only escalation did
   not survive; fish VARIETY lives in the biome tables instead.
7. **Three biomes** (Nebula Drift / Hollow Void / Comet Field):
   arena flavor + pattern-parameter twists + named fish tables
   (3 commons + 1 rare each). Rolled at cast; the portal shows
   its biome.
8. **Four rods** (Cane + Splitwillow [repo] · Heavyline + Twinreed
   [proto] — two new weapon_frame data rows, same schema), R to
   swap, autofire holds the trigger only — aim is never
   automated.

## Still-live canonical items the prototype didn't cover ([T] later)

- Node drift/despawn (school rules) — static nodes stand.
- Rifter gear (rods/lines/charms) + the celestial tree — the
  recorded destination; the standing sequencing rulings govern.
- Normal water fishing (sl-0111) — releases after the soul seam,
  reusing its cast/reel machinery.

## Merge notes for the seam (planning's flags)

- **Overworld speed 4.2 t/s is [proto] convenience and does NOT
  ride** — the game's speed law (3.6 anchor, sl-0102/0103)
  stands.
- **The Starlit Cast cosmetic stays** — the prototype omitted it;
  the repo keeps it (variants doctrine).
- **Keys map to the game's bindings**: cast = F (the interact
  verb at the portal — the prototype's E), autofire = E (already
  ratified), rod swap = R [T].
- **Arena vs split (HANDOFF §3)**: the built 15×12 arena_rift
  shrinks or the rift camera guarantees full-arena visibility —
  Law 1, no off-screen bullets ever.
- **Tick-rate conversion (HANDOFF §7)**: prototype sims 30 t/s
  treating repo tick counts 1:1 — re-check cadence math against
  the game's rate before porting numbers.
- The constant pull in the arena is a NEW system (player ×1.0 /
  boss ×0.3 / bullets ×0.15, oscillating ±25° ~26s) — "worth a
  real .tres."

## Deck-tap refinements (the designer's taps, swept ~12:20 — ride this seam)

1. **THE LINE HAS THREE LIVES** (shk1loss: "Line durability pays
   (line ×3)" + "if we go for three lives … make them pretty
   hard"): a dive survives up to three snaps; each line is HARD
   to lose (per-line stability generous [T]). Refines the
   prototype's single-pool snap — the seam builds lives ×3 [T].
2. **RIFTS SPAWN ANYWHERE, ANYTIME** (shk3spwn: "a chance to
   spawn anywhere while traveling or fighting … special rare
   encounters down the line"): an ambient spawn chance [T] joins
   the authored nodes; rare-encounter variants are future
   material.
3. **THE ZONE CONTENT TARGET: 4–6 unique starhook boss fights
   per zone** (the designer's scaling word; the kit recipe makes
   rift kits cheap, so the target is honest). v1 ships one kit +
   biome twists; the target governs the chapters.
4. **FISH ARE SPECIES-CURRENCY ITEMS** (shk2ctch note): city
   vendors will someday price goods in specific fish ("30 fish X,
   50 fish Z, 10 fish Y for a cool mount"). Fish persist
   PER-SPECIES from this seam on; vendors/mounts are a future
   chapter's system.
5. Locked by tap: the name is STARHOOKING · the rifter v1 = one
   fixed micro character (cosmetics + weapons down the line) ·
   ring swap decided during Green days (the bag supersedes) ·
   the dungeon hand-author pass lands after Green days, beside
   S2.

## The designer's grasp-check corrections (~12:45 — these override everything above where they touch)

1. **The protagonist is the BAIT FIGHTER, not the line** — "the
   little guy that is used as bait at the end of the line" (the
   designer's own name: THE BLUBBER BAIT GUY). The line is his
   tether and the tension-teller; HE is the star. Presentation
   emphasis follows him. (This overrides the prototype DESIGN.md's
   "the line is the star of the show.")
2. **He renders SMALLER than the prototype shows** — "just a
   simple fighter": a small, simple sprite [T size].
3. **STARHOOKING HAS NOTHING TO DO WITH WATER** — rifts/portals
   spawn on LAND (anywhere, per the deck tap). The water-fishing
   base (sl-0111) is PARKED by this word — revive only on the
   designer's say. The canonical paragraph's "layered on top of
   normal fishing" line is superseded.
4. **The two-portal topology is load-bearing**: the line goes
   INTO the world-side rift and comes OUT of the galaxy-side
   rift. Always drawn that way, both panes.
5. **Rifter gear is IN the design — the deferral is superseded:
   rods AND very-simple equipment DROP from starhook bosses;
   starhook LEVELS gate their use.** The soul seam stays as
   scoped (rods by level, per the prototype); the GEAR SEAM rides
   next, routed when the soul lands.
6. **The small starhook skill tree is CONFIRMED** — behavior-
   first: it "improves or changes the way the bait fighter
   behaves" (the prototype's STARHOOK SELF tree is the
   reference). Scheduling stays post-class-trees unless the
   designer calls it earlier.
7. **THE ARENA PART HAS NO NAME — at all** (the designer, twice):
   the boss-fight part of starhooking is not a named thing — no
   coined title, and no coined replacement either. It is just
   part of starhooking: write "the arena", "the galaxy view",
   "the boss fight", and describe the pull plainly ("the rift
   pulls on the line"). A fishing minigame doesn't get its own
   brand name. Where any older text (the canonical paragraph,
   the prototype's DESIGN.md, the sl-0115 ask) uses the old
   word, read it as plain description — and never carry it into
   player-facing text, UI, identifiers, or docs.

## Evidence

- Clips: `Screen Recording 2026-08-02 044051.mp4` (46s, the full
  loop: cast → fight → tension → snap at casts 8/snaps 2) and
  `044205.mp4` (22s). Frames verified by planning: the split, the
  living line (white slack → orange taut), the portal ring, the
  starfield + wisps/crystals, biome label ("NEBULA DRIFT RIFT —
  E = CAST THE STARHOOK"), boss + LINE bars, rod chip, counters.
