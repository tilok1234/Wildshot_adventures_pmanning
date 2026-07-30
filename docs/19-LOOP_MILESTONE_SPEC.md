# Wildshot Adventures — Doc 19: The Loop Milestone (Gate-1 forward scope)

**Status:** ACCEPTED in-session 2026-07-30 (the Phase 0 design
conversation, designer present — session record
`notes/sessions/2026-07-30.md` addenda 9/11/12). Deck ratification
staged: `tools/decision_deck_items_2026-07-30-gate1.json` (the rewrite
+ the bar) and `...-loop.json` (this spec's four rulings). **The bar's
final wording is the designer's — owed to the staged card; the draft
below stands until then.**
**Authority:** planning repo. The game repo consumes this spec
(ask sl-0025); it never amends it. Supersedes docs/12's tester-cycle
prose as the forward scope (docs/12 §banner; docs/08 CORE-53/55
amended rows carry the same provenance).
**World-frame context (2026-07-30 evening, Tier 1):** the loop is the
FIRST MILE of the Part I persistent zoned world (CORE-16 onward), not
a standalone run-game — designer reconnection ruling, record in
`notes/sessions/2026-07-30-worldshape-forklift.md`. The bar's meaning
re-aims accordingly ("is the first mile of my world worth walking
daily"); the staged wording card absorbs this when the designer words
it.

## 1. The bar (draft standing in for the designer's words)

An unguided complete run: spawn in the b65 town → walk out → fight
through rising danger where loot actually drops and matters → reach
the first boss or die trying → death costs something real → dying
pulls you to retry immediately. The bar holds when that run exists
and stays fun for the DESIGNER playing it daily for a week. Then —
and only then — 2–3 warm, WATCHED first-touches judge it (silent
watching; the quiet-lab law holds).

## 2. Rulings (designer, Tier 1, 2026-07-30 — deck cards staged)

1. **Death.** Permadeath is a TOGGLE chosen at new-character creation
   (hardcore opt-in — "best of both worlds; this is a singleplayer
   game mostly"). NORMAL-mode death: respawn in town + a gold cost
   (percentage; exact rate [T]) + the run-back itself — dying deep is
   its own spatial price. Equipment is never taken in normal mode.
   Hardcore death: the character is gone.
2. **Loot frame.** Five equipment tiers, **T1–T5**. Tiered gear drops
   mainly from normal enemies; bosses may also drop it (docs/01
   already binds this). Uniques per docs/01 §Unique equipment:
   boss-only, each unique tied to a specific boss (aimed grinding), a
   boss may carry several uniques in its table; rates "obtainable
   with effort" (CORE-49 percentile guardrails at tuning time; rolls
   independent, NO pity — reward breadth is the dry-streak answer).
   Tiered gear = world progression; uniques = the goal to grind for.
3. **Levels + XP are IN** ("we have planned for levels and exp so we
   should probably include it"). v1 minimal: kill XP, a level curve,
   lean-sheet stat growth. Class skill points/trees stay deferred.
4. **First boss = BONE RELIQUARY KING** (name changeable later): the
   proven three-phase Yard Warden kit reskinned with the 13-boss
   pack's sheet. Bespoke boss kits come later. He carries the loop's
   first unique(s), per the locked named-challenge rule.
5. **Danger gradient v1 = HAND-AUTHORED** outward from the town,
   mining world_filler's pack data as the authoring guide (wf is more
   than danger rings; its game-side intake machinery stays deferred
   until hand-authoring runs thin).

## 3. v1 scope — the L1 "skeleton run"

Run lifecycle (town spawn → out → death → town respawn; retry
friction ~zero) with the permadeath toggle at character creation;
gold as droppable currency + the normal-death percentage cost [T];
minimal XP/levels; T1–T5 tier plumbing + drop tables on EnemyDef
(deterministic — a NEW named serialized PCG32 stream for loot);
ground drops + pickup + a minimal equip surface under the readability
laws (quiet floors; threat above beauty); the hand-authored spawn
gradient using the existing six-ordinary roster (new ordinaries are
data rows on existing archetypes when needed); the Bone Reliquary
King wired (48×48 sheet on the Warden kit — render scale only, the
24px hurtbox untouched, per the parked honesty note) at one authored
boss site on the gradient's edge; the first unique item (designer
specs it; an honest [T] placeholder is acceptable).

## 4. Deferred by name (so the scope tripwire has teeth)

The fuller loot-structure pass ("more structure around it later when
I plan" — designer), exact gold/drop rates (CORE-49 percentile sim
later), skill trees, dungeons/portals, world_filler intake machinery,
bespoke boss kits, cosmetics/collection log, classes beyond the
Archer, trading/economy, co-op.

## 5. Constraints carried forward (unchanged law)

No RNG outside named serialized streams — loot included; battery +
pretester stay green and proofs never weaken; test scenes accrete
into game content; the tester-zip pipeline + lockdown stay a standing
gate; CORE-33/34 (movement sufficiency, no required ability),
CORE-50/51 (accessibility + readability laws); quiet-lab silence
during watched runs; two-tier verdicts (loop FEEL calls get one
rested ratification).

## 6. Landing order

**L1** skeleton run (§3) → **L2** daily-play tuning (the bar clock
starts when the designer says the skeleton is judgeable; weekly GIFs
fall out free) → **L3** scale via world_filler intake ONLY if
hand-authoring runs thin → the bar holds a week → 2–3 warm watched
first-touches → Gate 1 verdict per CORE-55-as-amended.
