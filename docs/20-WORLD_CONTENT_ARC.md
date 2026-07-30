# 20 — The world-content arc: directed worlds, by hand first, then the importer

STATUS: ACCEPTED direction (designer, in-session 2026-07-30).
This is sequencing doctrine for how world_filler's director output
reaches the game. The importer's own spec is deliberately NOT in
this doc — it gets written and ratified at its planning session
(step 3 below), which the designer already holds the reservation
for (wf docs/IMPORTER_READINESS.md).

## The question this answers

Should the game import world_filler content packs (danger bands,
boss/dungeon placements, spawn territories) directly — and when do
we build that importer?

## The answer: yes, in three steps

1. **REHEARSE BY HAND** (test overworld, b72 base). world_filler
   directs the world: recipe pinned to the world identity → plan →
   place → territories → validate (nine gates) → designer
   lock/reroll/paint rounds in the viewer → export publishes the
   content pack as a GitHub release. A game session then consumes
   it **as reference only** — hand-authors spawn tables and a boss
   site or two from the director output, mapping wf's placeholder
   rosters onto real enemy defs, with dodgeability proofs re-run
   on every authored pull per game doctrine. No new machinery
   anywhere.

2. **FEEL VERDICT** (designer plays). Does directed placement feel
   right — the danger ramp, the boss spots, the territory texture?
   Feels good → step 3 automates a pipeline already proven by
   hand. Feels wrong → we learned it cheaply; iterate the mapping
   or the recipe, not code.

3. **BUILD THE IMPORTER** (its own planning session). Scoped to
   the minimal consuming surface: bands, placements, territories →
   the game's spawn representation. Authoring metadata (locks,
   paint layers, audit internals) is explicitly out of scope.
   Proofs run over imported placements exactly as the battery runs
   over imported worlds. The hand-pass mapping from step 1 IS the
   spec input — the mapping gets designed from evidence, not in
   the abstract.

## Why we believe the import will work (evidence, not faith)

- wf's dual-verifier battery already validates content packs
  inside REAL headless Godot — the "will the engine read the
  format" risk is retired before the importer exists.
- The game's intake culture is proven at this task class:
  verify-everything-before-drop, replicate-the-source-algorithm,
  refuse loudly (the b71 intake, sl-0036, is the exemplar).
- The consuming side exists since Loop v1: tiers, defs, spawn
  semantics, dodgeability proofs.
- Content-pack formats are frozen, hash-sealed, and pin their base
  world by generation identity — cross-repo drift gets caught at
  intake, not in play (the behavior-47→71 parity finding proved
  those gates work on the very first styled world).

## The honest uncertainty

Not feasibility — **feel**. Rosters are placeholders; wf's danger
model is not the game's tuning. Step 2 exists precisely to answer
this before any importer code is written.

## Why build it at all

Hand-authoring was right for b65 (small), is feasible-but-costly
for the test overworld, and becomes untenable for the real world.
The importer is what makes directed worlds cheap and repeatable —
direct in wf, import, play. That is its payoff; the test world is
just the rehearsal stage.

## The end-state this arc serves (designer, in-session 2026-07-30)

Designer's words, near-verbatim: work toward "pretty pristine and
customized world_filler generation specifically directed at this
game — and when we got that going, go over and hand-carve it to a
pristine feel-good shape." The production model in one line:
**generation does the heavy lifting, hand-carving does the soul.**
wf grows from a generic director into one tuned for Wildshot —
its real enemy vocabulary, its danger-as-geography doctrine, its
loop rules — producing worlds that arrive mostly right; the
designer then carves the finishing layer by hand.

Three standing notes on that path:

- **The hand-carve layer is above all AUTHORIAL, not geometric**
  (designer clarification, same conversation): placing NAMED
  bosses within the lore and the small storytelling details no
  generator can invent. Generation proposes scored sites — "a
  boss-shaped challenge here, tier 4, guarding the east approach";
  the designer gives the site identity and meaning — WHO lives
  there and WHY. This is doctrine, not garnish: the locked loop
  frame rules that specials/uniques come ONLY from authored named
  challenges (docs/19), so the lore layer is where the loot
  economy's top end lives — every named boss placed in the lore is
  a unique drop entering the game (the Bone Reliquary King →
  Reliquary Coil pattern, across the 13 and beyond).
- The mechanical carve kit for the rest already exists: wf's
  authoring loop (lock / reroll / paint — designer shaping
  SURVIVES rerolls) plus WorldForge terrain polish, used at
  finishing intensity.
- "Customized at this game" starts DATA-FIRST: game-specific
  recipes and a roster vocabulary speaking real enemy defs instead
  of placeholders — no wf format changes; the step-1 rehearsal
  mapping is the seed of exactly this vocabulary. And that
  vocabulary should carry IDENTITY, not just stats — the mapping
  layer is where "boss site" becomes a named boss with lore.
  Feature-level wf customization only if the rehearsal shows
  data-first cannot reach pristine — decided then, on evidence,
  not now.

## Gates in front of step 1 (live at writing)

- sl-0037: wf segmentation fix (sl-0026, ruled) + behavior-71/72
  walkability adoption scoping → designer ratifies the adoption
  (every wf verb refuses b71/b72 until then).
- sl-0035: b72 game intake (the base the content pack will pin).

## Pointers

docs/19 §2.5 (the mine-the-data doctrine — step 1 is it, made
literal) · docs/17 (current consumption basis: world packs only)
· wf docs/IMPORTER_READINESS.md (the prepared game-side surface)
· session record notes/sessions/2026-07-30.md, Addenda 21–23.
