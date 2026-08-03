# Wildshot Adventures — Doc 23: Slice v0.1 Build Plan

**Doc:** 23-SLICE_BUILD_PLAN
**Status:** ACTIVE — the build GO fired 2026-08-01 (sl-0100); S0 +
S1 engineering COMPLETE; GREEN DAYS OPEN under the way-forward
ruling below (the S2 gate bar governs). The shape, the six
dispositions, and the class call are the designer's (sl-0098 seam).
**Authority:** planning repo; the game repo consumes and never
amends.
**The milestone:** Slice v0.1 — THE WORLD IS THE TEST (sl-0098):
a small-scale of the full game on the dusk overworld. Four zones,
cap 30 (Green 1–7 / Dry Reach 8–15 / Wetlands 16–22 / Snow 23–30,
sl-0087), a dungeon per zone, 1–3 world bosses per zone with
uniques, simple fishing/foraging/skill trees, ~5 quests/zone
(sl-0082). **The bar:** docs/19 §1 as re-aimed — the three
sentences, judged by the designer LIVING in the built slice daily
for a week, then 2–3 warm watched first-touches.
**Standing frames consumed:** docs/22 (the stat system, all nine
blocks ruled + the calculator green at game 7ff3fd1) · the shipped
content pack (sl-0093/0094, first game←world_filler pin) · both
packs cleared to wire (icons 470 / NPCs 32, sl-0098) · six pillars ·
readability laws · determinism/proof discipline throughout.

## The designer's six dispositions (2026-08-01, verbatim gist)

1. **Enemy rosters:** split all enemy mobs into FOUR groups — each
   zone owns one group, and its dungeon draws from the same group
   (dungeon variants = denser/faster, never sponges — CORE-36).
   **THE SPLIT IS RULED (designer, 2026-08-01, "yeah this seems
   very good", off the sprite montage
   `notes/evidence/2026-08-01-slice-enemy-groups-proposal.png`)**
   — all 57 families / 202 variants assigned, and **ALL VARIANTS
   PLAY within their zone** (the designer's variability ruling —
   ~45–54 distinct looks per zone, zero new assets):
   - **Green Country (14):** slime · goblin · boar · wolf · bat ·
     shroom · wasp · beetle · moth · snail · porcupine ·
     scarecrow · treant · bandit (the roads' humans)
   - **Dry Reach (14):** scorpion · snake · kobold · gnoll ·
     harpy · minotaur · cyclops · golem · imp · bigcat ·
     gargoyle · eyemonster · mantis · mole
   - **Wetlands (14):** frog · crocodile · turtle · jellyfish ·
     anglerfish · octopus · crab · centipede · carniplant ·
     lizardfolk · ratfolk · troll · zombie · spider
   - **Snow Country (15):** bear · griffin · drake · elemental ·
     worm (frost wyrm) · orc · ogre · dwarf · elf · skeleton
     (incl. the crowned variant — the Bone Reliquary King's kin) ·
     ghost · cultist · demon · puppet + mimic (the ruined city's
     own)
   Combat ROLES ride archetype data rows per family (CORE-44
   grammar) — the split assigns identity, not behaviour; S1–S4
   consume it chapter by chapter.
2. **Living-world plumbing:** keep it simple (ruled on planning's
   recommendation, below) — v1 is four small pieces, built FIRST.
3. **Bosses:** every boss feels SPECIAL — an engaging fight, never
   a task. Distinct pattern kit + phases + telegraphs per boss; the
   proven Warden three-phase recipe is the floor, a stat wall is
   never the answer. Boss identity/lore stays the designer's act.
4. **Uniques:** basic concepts for the slice ("this is just a test
   slice") — the block-8 whitelist governs; deepen later at will.
5. **Quests:** generic quests first (kill/fetch/visit off the giver
   slots, each carrying its slot's reason tag — the villager-reason
   pillar for free); hand-author closer only where it feels needed.
6. **Wiring:** yes — NPCs + icons land in S0.

**BOSS IDENTITIES (the designer's naming act, 2026-08-01 — name ·
what it is · why it's there · basic unique concept [one
whitelist break each, numbers at build]):**
- **GREEN COUNTRY (ruled):** world boss = **OLD TUSK** — the
  great scarred boar of the SE mud pocket (the hand-placed site),
  the countryside's own monster; every farmer tells the story,
  the Wardens nail warnings to the trees. Unique concept: **Old
  Tusk's Hide** (armor; over-budget defense WITH a real paired
  speed cost — break (c); the souvenir: his stubbornness).
  Dungeon = **THE WARREN**, boss **KING GRUBB** — the goblin
  tunnel-maze under the meadows; the fat little king every
  surface goblin answers to (pack fights in tight rooms = the
  dungeon grammar; explains the zone's goblins).

- **DRY REACH (ruled):** world boss = **THE LAST SENTINEL** — an
  ancient golem in the open sand, still guarding a doorway to
  whatever the Seekers want dug up (slow, huge, geometric
  patterns; the Seekers' whole story in one fight). Unique
  concept: **the Sentinel's Beam** (staff; PATTERN REPLACEMENT —
  fires his slow sweeping line; the souvenir rule). Dungeon =
  **THE SEALED TOMB**, boss **THE MINOTAUR** — the buried maze
  the Seekers cracked open and regretted; the bull walks its
  corridors (labyrinth grammar; "Karn" parked as a name candidate
  if he ever needs one — "the Minotaur" carries its own weight).
  Dungeon-boss uniques stay open for chapter build (the ~8–12
  budget governs; each break distinct in kind — the Hide took the
  armor-budget break, the Beam takes pattern replacement).

- **WETLANDS (ruled, "1 and 1"):** world boss = **THE DEEP MAW** —
  an anglerfish horror in the black pool; its lure is the only
  light in the fight (light-in-the-dark spectacle; the Rovers pole
  wide around that water). Dungeon = **THE BEAST DEN** (the
  designer-locked mud site), boss **LONGJAW** — the great
  crocodile the den literally belongs to; the den promises a
  beast, the den delivers THE beast.

- **SNOW COUNTRY (ruled, "1 and 1") — the finale pair:** world
  boss = **THE FROST WYRM** — the white wyrm under the western
  snowfields, the thing even the Keepers won't name
  (burrow-and-erupt spectacle; the west finale destination).
  Dungeon = **THE BONE RELIQUARY**, boss **THE BONE RELIQUARY
  KING** — CANONIZED: the loop's proven first boss becomes real
  content; the reliquary his name promised is IN the ruined city,
  the crowned skeleton variant is his sprite, the Keepers' whole
  purpose points at his door, and he keeps the loop's first
  unique. **THE PUPPETEER IS GREENLIT (designer, same session: "we
  could do that it sounds cool") — boss #9, the ruined city's
  SECOND boss:** the marionette-master holding court over the
  haunted puppets in the streets the king doesn't walk (the
  sl-0091 sanctioned one-round lock-lane addition, ACTIVATED).
  Executes as ONE directed world_filler round (site inside the
  ruins box, recipe-locked, gated export = the next content-pack
  version); the game re-intakes the updated pack BEFORE S4 builds
  Snow — zero S0–S3 impact. Slice cast = 9 bosses; the ~8–12
  unique budget holds. The wf paste is staged in the session
  file; the designer fires it at any convenient wf session.
- **Unique-concept sketches so far [P], one distinct break each:**
  Old Tusk's Hide (armor over-budget w/ paired cost) · the
  Sentinel's Beam (staff pattern replacement) · the Deep Maw's
  Lure (rule-bending utility — light/aggro trickery, concept
  open) · a Frost Wyrm piercing break (b-family, concept open) ·
  the Bone Reliquary King's = the loop's first unique, carried.
  Remainder land at chapter build inside the ~8–12 budget.

**THE NAMING ACT IS COMPLETE (2026-08-01): 4 factions + all 8
slice bosses named, every one explainable by a villager in one
sentence. S1–S4 consume these as the chapters open.**

**THE BOSS-SPRITE ROSTER RULING (2026-08-02, Green-days batch #1
finding 3, sl-0122):** the designer's 13-boss assembler pack
(intaken at the game's `assets/assembler-boss-pack`; only
bone-reliquary-king wired until now — the live S1 bosses drew
enemy-family variants) IS the slice's boss art wherever it fits
(the designer: "yyeah it works"):
- **Rebinds:** King Grubb → boss:goblin-war-crown (now, sl-0122) ·
  Longjaw → ancient-mirejaw (at the Wetlands chapter) · the Bone
  Reliquary King already exact.
- **Small-sheet bosses render SCALED:** where a boss keeps an
  enemy-family sheet, it renders a little bigger (per-def render
  scale [T]; the designer: "we just got to scale them up alittle
  when we render them in game") — Old Tusk stays the scarred
  blood boar, scaled; sim/hurtbox bytes untouched.
- **THE DEALING [P]** (extra world bosses, landing per chapter via
  directed world_filler rounds — the Puppeteer precedent): Green +
  dryad-of-nature · Dry Reach + scorpion-empress +
  cyclops-forge-titan · Wetlands + abyssal-crown-kraken +
  tide-man-the-blue · Snow + sun-crown-griffin +
  royal-night-elf-prince. Every zone lands at 2–3 world bosses —
  inside the bill's 1–3. Identities/names extend the naming act
  at each chapter.
- **HELD post-slice:** living-pyre · lava-core-colossus ·
  pit-fiend-juggernaut (the hellish three; no slice zone owns
  them honestly).
- **No automatic uniques for dealt bosses** — the ~8–12 budget
  stays law; uniques only where a concept earns one.

**THE FOUR FACTIONS ARE NAMED (designer, 2026-08-01, supersedes
the [P] candidates from the icon round):** **the Wardens** (Green
Country — the line between the farms and the roads' bandits) ·
**the Seekers** (Dry Reach — they go after what's buried) ·
**the Rovers** (Wetlands — the marsh roads' freelancers) · **the
Keepers** (Snow Country — they keep the dead down and the ruins'
secrets kept). One parallel shape, designer-structured; "the
Waders" rejected for audible collision with "the Wardens" (the
readability instinct, applied to names). Each name binds its
faction rep in the NPC roster at seam-4 wiring; faction XP/vendor
mechanics stay the locked CORE-39/46 frame, later.

**Class call (designer, same session): ALL THREE classes from the
start** — bow / staff / sword ("we got all the infrastructure
completed for it": three ruled base curves, calculator-generated
budgets, icon vocabulary). CORE-38's one-class posture is
superseded for this slice (register row). SCOPE GUARD against the
multiplication risk CORE-38 feared: per-class content stays LEAN —
~2–3 weapon frames + 2–3 ability items per class in-slice, patterns
shared-tech wherever honest.

**Dungeon truth (designer flag, same session):** the pack places
dungeon ENTRANCES — four slice-marked bindings at real existing
structures (incl. the designer-locked Wetlands beast den).
INTERIORS (committed instance, rooms, boss arena) are chapter work
by design: each chapter opens its zone's dungeon as a simple
stand-in interior + boss first ("place them there for now, fix it
later" — the designer's disposition); quality passes iterate.

**Working principle (designer, same session): MANAGEABLE SLICES
ALL THE WAY DOWN** — the chapters bound the top level, and within
each phase work lands as SMALL SEALED SEAMS: one system per seam,
all gates green before the next seam opens, never a big-bang
chapter drop. Quality stays up because nothing unproven stacks on
anything unproven (the house one-thing-per-commit discipline,
applied to build sequencing). Boss craft gets designer ROUNDS by
design (the rehearsal pattern) — feel iteration is scheduled work,
not scope creep.

## Living-world plumbing v1 (the S0 core; planning's recommendation, designer-accepted)

Four deterministic pieces, NOTHING more (no schedules, no ecology —
full-game later):
- **(a) Activation leash:** sites spawn dormant; wake at radius R;
  reset beyond R + hysteresis (answers the sl-0094 cold finding).
- **(b) Territory tether:** mobs wander near their site and leash
  back; nobody migrates.
- **(c) Depth-keyed respawn:** per-site timer — lazy in Green, fast
  in Snow (W-3) — ticking only while the player is away; nothing
  ever pops in the player's face.
- **(d) The importer:** reads the shipped pack's placements/
  territories directly as spawn tables — no new authoring format;
  the game-side b77 pairing gate already pins the data.

## Build order (chapter-by-chapter, Green first — the ruled order)

- **S0 — FOUNDATIONS (once, world-wide):** plumbing v1 (a–d) ·
  overworld death = CORE-43 (respawn at settlement + gold slice +
  the walk back; mechanism proven in the retired b65 loop) · THE
  STAT FRAME ENTERS THE SIM (docs/22 blocks 1–8 become code;
  deliberate SERIAL/goldens re-baseline per house discipline; the
  calculator's data file is the tuning source) · NPCs stationed in
  settlements (W-8 presence) · icons into the UI where cheap.
  **Gate:** pretester + proofs green; Green Country alive and
  walkable with the stat frame underneath.
- **S1 — GREEN COUNTRY (the first mile):** Green's group live at
  its sites via the importer · T1 drops + levels 1–7 · the
  hand-placed world boss made special (kit pass) + the first
  unique(s) · the Green dungeon + boss · 3–5 reason-tagged generic
  quests · fishing/foraging v1 (basic) · all three classes
  playable. **SEAM 6 AMENDED (sl-0105, the designer's word
  mid-S1): fishing v1 → STARHOOK v1 — the rift fight replaces the
  fishing minigame (capture + dispositions in
  notes/2026-08-02-starhook-idea.md); foraging v1 unchanged.**
  **S1 ENGINEERING COMPLETE 2026-08-02** (six seams + the
  parallel battery in one overnight, game 91b1037..b2167a2, all
  swept + pushed; the post-S1 Green-days era — interact verb, UI
  family, inventory, the starhook soul re-route — lives in the
  sync log sl-0106–0119 and notes/reference/starhook-proto2/
  INDEX.md, which is the starhook LAW).
  **Gate:** the designer lives in Green a few days — the
  three sentences' first honest read while fixing is cheap.
  **The gate's bar is RULED (2026-08-02) — see THE WAY-FORWARD
  RULING below: Green days end at SYSTEMS-COMPLETE, not
  Green-perfect.**
- **S2 — DRY REACH · S3 — WETLANDS · S4 — SNOW COUNTRY:** the same
  chapter recipe (zone group + boss/es + dungeon + ~5 quests + tier
  bracket), faster each time; Snow adds the T5 capstone pieces and
  the two finale destinations (west boss / east ruins).
- **S5 — THE BAR:** the designer's week living in the whole small
  world → 2–3 warm watched first-touches → Gate 1 verdict per
  CORE-55 as amended.

## THE WAY-FORWARD RULING (designer-agreed 2026-08-02 — governs the S1→S5 arc)

Refinement is TWO different things with two different right times
(planning's recommendation; the designer: "yeah i agree"):

- **Structural refinement — missing systems, wrong shapes — happens
  NOW, in Green.** Green is the template: anything structural fixed
  here is built correctly three more times for free; anything broken
  carried forward duplicates into four zones and gets re-fixed four
  times. The designer's own bar: "we should get everything
  funcitoning like we do starhookingf bwefore we move on".
- **Number tuning + polish waits for ONE whole-game refinement pass
  after S4** — the 1–30 curve runs across all four zones and only
  tunes when the whole curve exists. Green-days tuning goes only as
  deep as "roughly right where it blocks fun"; every number stays
  [T] meanwhile.

**The S2 gate bar, concrete: Green days end at SYSTEMS-COMPLETE,
not Green-perfect** — the designer can play Green start to finish
and never hit "this system doesn't exist yet." The known
systems-complete queue (updated 2026-08-03, the menu-pass
landing): the starhook soul seam LANDED + refined
(sl-0115/0123/0125) · THE INVENTORY FAMILY LANDED (the bag
sl-0116+0128 · loot bags sl-0129 · the bank sl-0130 · vendors v1
sl-0131) · the view/feel batch LANDED (sl-0119/0120/0121/0122/
0132) · **THE MENU PASS v2 LANDED 2026-08-03 (sl-0159–0167, on
the designer's own v2 UI package): the two-tab C menu (slot-grid
bag + paper-doll + proper-info errands log w/ track+abandon) ·
the offer dialogue (accept-as-decision, Later-only) · stations
F-open + Esc-menu-first · bars left · options/toast restyles ·
the boss-unique reveal · the interactability audit** ·
REMAINING: the STARHOOK-GEAR SEAM (the designer's post-land
clarification, verbatim: "we put in gear for starhooking" —
THIS seam is the RIFT lane only; the OVERWORLD gear lane is
separate, loop-era, and was ALREADY LIVE before Green days:
tiered weapon/armor/ring/ability drops + boss uniques from
normal enemies since Loop v1/S1 — untouched today) — ROUTED
2026-08-03 evening, sl-0177,
the designer's two shaping words in: charter-shaped rifter gear
(rod + chest + helm; RODS = STARHOOKING WEAPONS with SEVERAL
per level tier, sl-0178 — the rift lane's weapon family, each
rod a fight identity; per-family patterns vs stat flavors =
the drop session's word), acquisition BOTH ways (the TACKLE VENDOR
v1 lives in the HARBOR CAPITAL, priced in FISH via the
starhook_fish{} per-species counts; rare catches DROP the
special pieces, in-sim rng_loot), FUNCTIONAL-FIRST by the
designer's word ("ye lets do it functionally now and visually
later. just some placeholder for now") — real stats + slots +
placeholder looks; the visibly-worn modular armor layers ride
the designer's prototype handoff whenever it arrives; every
number [T]; BUILT 2026-08-03 AT SERIAL 26 (sl-0177/0178
resolved at the game seam's close — the sl-0168 reservation
amended exactly as written: the gear seam built first and took
26; foraging takes the next free number) · simple
class trees v1 (the slice-tree scope below) · the FORAGING build
(split from the menu pass onto three designer words — ALL THREE
ANSWERED 2026-08-03, Tier 1, sl-0168: F-press → short gather bar
[~0.5–1 s, T] interrupting on move/hit → a LOOT BAG drops (sl-0129
machinery); yield = forage MATERIALS as per-species profile
currency on the starhook_fish{} doctrine, cosmetic trade-in sink a
future round; nodes SPAWN AMBIENTLY like starhook rifts (capped,
rng_misc, consumed on gather — the everywhere-forage's ~1.9k
standing cells retire as direct gather cells; session lean [P]:
they become the spawner's candidate pool so nodes sit on real
props) — SPEC COMPLETE, builds at the next free SERIAL (27 —
the gear seam took 26) at the next build slot) · whatever
further Green notes surface as missing
systems. Then S2–S4 run at full speed on stable
systems (content stamping), then THE REFINEMENT PASS (whole game,
whole curve) leads into S5's bar week.

## THE STARHOOK EXPANSION CHARTER (designer rulings, 2026-08-03 at-work chat session; sl-0170)

The designer's framing, opening the arc: starhooking is the idea
"we really can make bank on" — original, instantly explainable,
and worth sustained refinement. The intent re-anchored hard
mid-session: starhooking is NOT an economy system and never a
money sink — it is **a bullet-hell minigame with its own
character**; the bait is not a resource, THE BAIT IS THE FIGHTER
("the bait is kind of the fighter, at least visually"); the
rifter is a real second progression lane. Rulings, in order:

1. **THE PLAYFUL-SPACE CHARTER [RULED]:** rifts may break the
   main game's STYLE laws — wild pattern vocabularies, densities,
   and mechanics the overworld would never allow. The FAIRNESS
   FLOOR never relaxes: deaths explainable, patterns
   deterministic and honestly dodgeable, no-strobe/
   photosensitivity absolute. Rider: the rift doubles as pattern
   R&D — a rift pattern that proves great may graduate into
   main-game boss work later.
2. **RIFTER GEAR = 3 SLOTS [RULED]: rod + chest armor + helm.**
   Real gear, not abstract upgrades; a MODULAR armor system on
   the code-drawn layered bait fighter (pieces = drawn layers,
   cheap by construction, visibly worn). The designer has
   ALREADY STARTED building the modular armor system on their
   side — expect a prototype handoff that becomes the law of the
   build (the starhook-proto2 INDEX precedent).
3. **GEAR ACQUISITION = BOTH [RULED]:** a tackle vendor sells
   the tiered rod/armor ladder priced in FISH (the per-species
   currency is the money — the loop stays self-contained; the
   small gold trickle to the main wallet stays flavor), while
   rare catches DROP the special pieces; unique rods (pattern
   deviants, the uniques law applied inside the pond) = the
   future chase.
4. **NO DEPTH DIMENSION [RULED — the metaphor correction]:**
   "this is not fishing" — there is no down. Rift danger RIDES
   THE ZONE the rift tears open over: Green rifts hold
   Green-grade fish, Snow rifts hold monsters. The overworld IS
   starhooking's progression geography, soft-gated by danger
   exactly like the world itself (no level locks on access; a
   brave low rifter can try a Wetlands rift and the fish is the
   lock). Rod unlocks may stay the one leveled ladder.
5. **RIFT TYPES WITH CONTENT POOLS [RULED]:** a few distinct
   rift kinds, each with a chance to spawn an encounter or
   dungeon from its respective pool; the cast draws in-sim
   (rng_loot, deterministic). Type-ladder sketch [P]: the common
   CATCH rift (today's single fish fight) · a SHOAL/swarm rift
   (playful-space license) · a DUNGEON rift (the Warren
   committed-instance machinery in galaxy skin) · rare strange
   kinds (twin-fish / unstable / wandering legendary) as event
   spice.
6. **TYPES ARE VISIBLE AT THE TEAR [RULED]:** each kind wears
   its own look at the portal — informed risk, the readability
   soul; the surprise lives inside the pool, never in what you
   walked into.
7. **RIFTS ARE RARE [RULED]:** rare enough that a sighting is an
   event ("oooooo rift") — never ambient furniture. Testable by
   feel: if you see one and don't detour, it spawns too often.
   All cadence/spawn numbers [T].

Zone-flavored species rosters, per-species pattern identities,
legendary fish naming, and the tackle vendor's home are OPEN
threads for the designer's continued refinement; every number
throughout stays [T] for Green days. The S1 starhook build
(sl-0115/0123/0125) stands as-is — this charter directs the
FUTURE rounds, no immediate re-work implied.

## Class trees v1 — the ruled shape (designer, 2026-08-03 at-work chat session; sl-0169)

- **THE PATTERN LAW (the session's defining correction):** tree
  choices are STAT TRADES + BEHAVIOR RIDERS ONLY — trees NEVER
  touch firing patterns. The designer's own words: pattern
  deviation from the tiered norm "is THE job of uniques" (a bow
  that fires 2 instead of 1, a 4-wide arc) "and we don't wanna
  modify how they already deviate from the norm." Tiered weapons
  = the norm; uniques = the deviants; a tree pick must never do
  a unique's job. (The session's earlier pattern-shaping lean
  was superseded in-flight and never recorded anywhere.)
- **Skeleton:** three pick-1-of-2 choice points at levels
  5 / 15 / 25 ("reasonable without being excessive").
- **RESPECCABLE** (designer: "this is gonna be a long game so we
  don't want to lock in potential mistakes") — session lean [P]:
  respec rides the existing vendor/station infrastructure, gold
  price, all picks reset together; every number [T].
- **Sword level-5 pair RULED:** Ironside (+armor +max hp /
  −move speed — the wade-in tank) vs Skirmisher (+move speed /
  −max hp — hit-and-run). Numbers [T]; the block-9 validator
  prices the pairs at build.
- **Everything else OPEN pending the designer's testing rounds**
  (their word: "I wanna do some more testing before doing these
  questions") — sword 15/25 drafts exist in the session record;
  staff/bow rows unstarted. The build waits.

## Deferred by name (the tripwire has teeth)

Full skill trees (slice trees = 2–3 real choices per class, the
block-7 grammar) · bespoke endgame balance (calculator bands govern;
curves re-derive against real content later) · co-op · raids ·
trading/economy **(NARROWED 2026-08-02 by the designer's word,
sl-0131: vendor INFRASTRUCTURE + simple v1 vendors pull INTO
Green-days scope — sell-to-vendor gold sink + small fixed stock;
the FULL economy, fish species-currency pricing, and faction
vendors stay deferred)** · ~~vendors beyond W-8 presence~~
**(SUPERSEDED by sl-0131 — simple vendors land in Green)** ·
cosmetics/collection log · Part II modules · anything the six
pillars don't need for the bar.

## Parked direction — THE FURNISHED-WORLD ROUND (designer finding from the S0 test, 2026-08-01; NOT scheduled)

The S0 walk surfaced a pipeline gap (designer: "world forge should
kind of build camps and dungeons etc from the positions world
filler makes" — "a result from the test"): the pipe is one-way, so
camps are spawn data on bare ground — no tents, no dungeon mouths,
no arena dressing. RECORDED SHAPE (planning's recommendation,
designer-acknowledged, act-later): (1) world_filler exports a
FURNITURE PLAN (positions + kinds only, from the locked content —
it keeps owning WHERE); (2) WorldForge consumes it as a pinned
input layer and builds the physical camps/entrances/dressing into
the next world version (it keeps owning HOW IT LOOKS); (3) the
cycle-trap is handled as a staged waterfall — furniture changes
walkability, so world_filler RE-VERIFIES its placements against
the furnished ground (walk laws hold: no sealed lanes, arena boxes
clear, W-13 relocate-never-delete) and the game re-intakes the
furnished world with the SAME content pack. One new pinned edge,
no domain crossing, road-joints-arc discipline pointed the other
way. **Timing lean: after S1, before S2** (one furnished zone's
re-verification is cheap; tents matter less than Old Tusk this
week). Fires only on the designer's word; pastes get staged at
that moment (labeled → WORLD_FILLER and → WORLDFORGE).

## Tooling lane (no sim semantics; designer-approved 2026-08-01 evening)

- **PARALLELIZE THE BATTERY (routed → game):** the full gate's
  ~45 min is machine time but the designer "is starting to feel
  it"; the runs are independent replays — run N-wide, byte-
  identical verdicts to serial proven once, coverage untouchable
  (the 45 min bought the ringer finding on day one — trimming
  coverage is never the lever). Target full gate ≲10 min +
  per-run timing table. **WORKER POLICY ASSESSED + RULED
  (designer "max 10 … lets asses" → planning on the real
  hardware, Ryzen 8745HX 8c/16t/31GB): default = physical core
  count (8 here, auto-detect), HARD CAP 10 (the designer's
  ceiling), longest-rows-first scheduling; RAM immaterial;
  expected full gate ~6–8 min.**
- **MODEL SEATS (designer-asked, planning's recommendation):**
  game build = Fable 5 max (sim surgery) · planning = Fable 5 ·
  producer rounds = Opus 5 · mechanical runs = Sonnet 5. Rule:
  the stronger the gates around a seat, the cheaper its model
  can safely be; design-heavy rounds bump to Fable for the day.
- **MORE-PARALLEL-AGENTS: LOOK FIRST (designer: "lets look some
  more at that first")** — the examination when wanted: the
  exclusive-seam law under more writers · shared-file pressure
  (the sync-log id-guard's four catches) · planning's sweep as
  the serialization point. A session-sized think, parked.

## Open at staging (both EXECUTED — kept as record)

- The **build GO** — FIRED 2026-08-01 (sl-0100; S0 routed as four
  sealed seams, complete same day).
- The **feel session** verdict — PASSED 2026-08-01 (sl-0099;
  density finding folded into the S0 leash tuning; sl-0041
  resolved).
