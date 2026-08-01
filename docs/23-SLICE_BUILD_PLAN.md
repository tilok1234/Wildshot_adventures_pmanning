# Wildshot Adventures — Doc 23: Slice v0.1 Build Plan

**Doc:** 23-SLICE_BUILD_PLAN
**Status:** STAGED [P] 2026-08-01 — the shape, the six dispositions,
and the class call are the designer's (this session, sl-0098 seam);
the build GO fires the S0 paste. **Authority:** planning repo; the
game repo consumes and never amends.
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
  playable. **Gate:** the designer lives in Green a few days — the
  three sentences' first honest read while fixing is cheap.
- **S2 — DRY REACH · S3 — WETLANDS · S4 — SNOW COUNTRY:** the same
  chapter recipe (zone group + boss/es + dungeon + ~5 quests + tier
  bracket), faster each time; Snow adds the T5 capstone pieces and
  the two finale destinations (west boss / east ruins).
- **S5 — THE BAR:** the designer's week living in the whole small
  world → 2–3 warm watched first-touches → Gate 1 verdict per
  CORE-55 as amended.

## Deferred by name (the tripwire has teeth)

Full skill trees (slice trees = 2–3 real choices per class, the
block-7 grammar) · bespoke endgame balance (calculator bands govern;
curves re-derive against real content later) · co-op · raids ·
trading/economy · vendors beyond W-8 presence · cosmetics/collection
log · Part II modules · anything the six pillars don't need for the
bar.

## Open at staging

- The **build GO** (fires the S0 paste) — the designer's word.
- The **feel session** verdict on the five scenarios (docs/20 step
  2, running at staging time) — findings fold into S0/S1 tuning.
