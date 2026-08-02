# 2026-08-02 — STARHOOK (designer idea capture, PARKED)

Captured by planning from the designer's ~01:50 message (the old
planning seat died mid-answer — account swap; this capture is the
resumed seat's first act) plus the designer's recording
`Screen Recording 2026-08-02 014852.mp4` (65s, Videos\Screen
Recordings).

PROVENANCE (corrected by the designer's word, then code-verified):
the recording shows a build WITH the fight in it — and none of
its fight strings (RIFTER / "fight the fish" / "the white core is
your true hitbox" / Splitwillow) exist in the June
`starhooking_sim\starhook_simulator` code. The June folder proves
the starhook NAME and fishing-shell theme predate tonight; THE
FIGHTING IS THE DESIGNER'S NEW INVENTION (the night of
2026-08-02). The recorded build's home is unconfirmed
(starhooking_sim, prompt_spriter, the queue launcher, and
generated games all checked and ruled out) — pin the path here
when the designer names it. Either way the recording proves the
kernel is playable outside Wildshot.

## The designer's words (~01:50, lightly condensed)

Fishing into PORTALS that spawn around the world like resource
nodes. Hooking one splits the screen: half stays the world, half
becomes GALAXY VIEW, where a second portal spawns and the fishing
line comes out of it. The galaxy half is a small ARENA for a
little fighter attached as BAIT on the starhook rod. Starhook
levels = that bait fighter's level, not a fishing stat. The
minigame is a "simple" boss fight scaled by rarity. The bait
fighter could have a skill tree + equipment as somewhat-rare
drops from starhook fish. "i just got this idea rn so we can prob
refine it."

## What the recorded prototype already proves (read from the frames)

- Split screen live: world left (shore, cast, line), THE RIFT
  right — a starfield arena where the RIFTER (LV 1→3 across the
  clip) dodges red orb patterns + yellow bolts and fights back
  along the line; fish-boss with hp bar; "the white core is your
  true hitbox" (bullet-hell readability grammar already present).
- Portal nodes ("✦ rift", node: ACTIVE) spawn in the world —
  including on LAND, not only water; "the line sinks into the
  rift…".
- The pitch line is literally on screen: "7 · STARHOOK — level
  the RIFTER, not your fishing stat". Controls: SPACE cast, WASD
  dodge, LMB fight back, T skills, E rod.
- A six-node skill tree "STARHOOK SELF": Greed Reel (+25% reel
  speed) → Iron Line (+1 line durability) → Deep Pockets
  (celestial catches pay ×3); Rod: Splitwillow (3-bolt fan rod);
  Quickhand (+30% fire rate) → Rod: Old Thornreel (heavy rod,
  dmg 2). RODS AS TREE UNLOCKS = the rifter's weapon classes —
  the best structural idea in the prototype.
- Rod swapping live ([E], "SPLITWILLOW equipped", CANE ROD
  baseline), fish counter (188), line ×3 durability, and a
  five-color rarity pip row (grey/green/blue/purple/gold).

## Planning's honest assessment

**The kernel is right for Wildshot specifically.** Most games'
fishing is a timing bar nobody loves. Wildshot's entire language
is telegraphed bullet-dodging — making the catch a miniature
arena fight means fishing runs on the engine's best muscle
instead of a bolted-on minigame. Rarity→fight-difficulty maps
onto the existing tier/budget frame. Portal nodes give overworld
walking another payoff (same pillar as gather spots). CORE-48
safe: this is the most active fishing system conceivable.

**The chronology is the argument for it.** In June the fight
could not have been built in Wildshot's language — the game had
no boss grammar yet. The fighting half arrived the same week the
boss recipe went three-deep (Warden → Old Tusk → King Grubb): the
idea completed itself when its missing half came true. It also
means the fight is the UNPROVEN half as well as the best half —
so the design round's first act is standing up ONE rift kit in
the house grammar (a rift fight is a boss kit at small scale; the
recipe makes that cheap) and tasting it before anything else gets
built.

**The expensive part is the second progression universe.** Rifter
levels + rifter tree + rifter equipment from fish drops = a
parallel stat frame, parallel validator budgets, parallel item
grammar — the whole block-4/block-8 apparatus twice. And the MAIN
classes' trees don't exist yet (the 20-minute designer sketch is
still owed). v1 shape that keeps the fun and defers the cost: the
rifter runs ON the existing stat frame (a fixed mini-class row),
starhook drops feed the MAIN economy in the one item grammar
(starhook-flavored), "starhook level" = the rifter's row leveling
on the same frame. If the fight is fun naked, it earns its own
tree later — after the player trees exist.

**Wildshot already built starhooking's skeleton this week — the
Warren.** Portal = a walk-on door (seam 4's door language). The
rift = a committed instance (a tiny arena with a boss at the
bottom). The rifter = the actor swap at transition. Boss kits =
the proven recipe (Warden floor → Old Tusk → King Grubb). Nothing
in the kernel needs machinery the game doesn't have.

**The one architectural ruling the design round must make: one
sim or two.** If the world half stays LIVE during a rift fight,
that is two sims at once — replay, battery, determinism, and the
byte gate all pay for it. If casting parks the body safely and
the world half becomes a vignette (paused or view-only), it is
ONE sim and every existing gate keeps working. The split-screen
LOOK survives either way. Planning's recommendation: one sim,
non-negotiable at v1.

**Smaller honest notes:**
- "Simple boss fight by rarity" should be a small FIXED cast of
  rift kits at v1 (the boss recipe exists), not a generator.
- The rift needs its own readability audit: the CVD-ratified hue
  map + one-lead-per-pattern law apply on a starfield background
  too.
- Drops: reward breadth, no pity — the coil precedent already
  answers dry streaks.
- Scope magnet warning: rods, tree, rarities, celestial
  currencies each invite growth; the seam law ("one sealed seam
  at a time") is the containment.

## Designer dispositions (2026-08-02, the post-capture exchange)

The designer read planning's assessment and ruled, in their
words: "we could wait and see if we wanna introduce gear later,
but we could just do it super simpel, and then we could also have
cosmetic gear for the RIFTER" + "fishing rods acts like weapons
with different bullet patterns kind of". Recorded as:

- **v1 is SUPER SIMPLE** (the designer's word). Functional rifter
  gear DEFERRED — wait and see; planning's second-progression-
  universe pushback accepted.
- **COSMETIC gear for the RIFTER instead, first.** This rides the
  seam-1 VARIANTS pattern exactly (view-only, deterministic pick,
  zero sim bytes): rifter skins/cosmetics as fish drops give the
  collection joy with no parallel stat universe. The machinery
  exists as of this week.
- **RODS ACT LIKE WEAPONS with different bullet patterns** — the
  rod IS the rifter's class. The prototype already shows the
  split (Cane starter / Splitwillow 3-bolt fan / Old Thornreel
  heavy dmg-2 = spread vs heavy, the sword/staff/bow feel at rift
  scale). Mechanism: a rod = a data row on the rifter's attack
  def — the new-ordinaries-are-data-rows doctrine applied
  player-side.

**Planning's effort read, updated:** "very little effort" is now
an honest claim for THIS v1 shape, because the slice built the
parts without knowing it: portal = walk-on door (seam 4), rift =
committed instance (seam 4), rift fight = boss kit on the recipe
(seams 3–4), drops = the loot machinery + one grammar (seam 2),
cosmetics = the variants system (seam 1), starhook level = a
stat-frame row, rods = attack-def data rows. Genuinely NEW code
is short: the cast/reel verb, the split-screen view, node
spawning. A week ago none of that was true.

## Status: PARKED

No sync_log ask opened. NOT S1 — seam 6 stays the basic
fishing/foraging verb exactly as routed in sl-0104. One optional
seam-6 nudge (designer's call to paste): build the fishing verb
portal-agnostic — spots are placed nodes, the cast targets a
node, catch resolution sits behind one interface — same basic
yields, zero scope change, keeps the door open. Starhooking
itself fires only on the designer's word after Green days; strong
candidate to headline a future chapter (the star chapter).
