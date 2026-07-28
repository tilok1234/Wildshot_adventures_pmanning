# 17 — world_filler Integration Plan (DRAFT — pending designer approval)

Drafted 2026-07-29 on designer request ("plan out properly how we gonna
use it"). Sources read this session: world_filler HANDOFF.md (2026-07-28,
freeze review RESOLVED), docs/VISION_AND_SCOPE.md, docs/CONTENT_PACK_FORMAT.md
(format 1 FROZEN), consumers/godot_addon/worldfiller_importer/README.md.
Remote branch `claude/freeze-review-resolution-tf6bkf` verified to exist
on `tilok1234/world_filler` (7bc73db). Nothing here is implementation
authorization — this doc plans; the scope ladder in §5 gates building.

## 1. What world_filler is (state as read, 2026-07-29)

The **world director**: reads a finished WorldForge world pack plus a
user-authored DirectorRecipe and compiles the gameplay-structure layer —
world bosses on clearance-proven arenas, dungeon bindings on the world's
own POIs, spawn territories with rosters, per-region danger bands and
budgets — into a **content pack (format 1, FINAL)** the game composes
with the terrain. Deterministic by contract (byte-stable, no timestamps,
hierarchical seed channels, per-region rerolls that cannot move other
regions), validated by a nine-gate audit, inspectable in a single-file
viewer, lockable placement by placement.

State: F0–F8 complete, 140 tests green. The F7 adversarial freeze review
the assessment flagged as cut-off was **resolved 2026-07-28 in a
follow-up web session**: all 38 salvaged findings empirically confirmed
via tamper experiments and fixed; both reference verifiers (TypeScript +
headless Godot 4.6.2) now enforce the full blessed-check battery and
agree refusal-for-refusal on a 20-case cross-battery. Pre-fix and
post-fix exports are byte-identical, so format 1 needed no bump.

**Consequence for the Decision Deck:** the go-item card
"world_filler verifier fixes" is SUPERSEDED — the holes named in the
notice (report.ok unread, vacuous manifest.files, TS-vs-GDScript wrap
divergence) are all closed upstream. When the card deals, mark it done
with a note pointing here.

**Machine state caveat:** the local copy at
`Documents\world_filler\world_filler-claude-freeze-review-resolution-tf6bkf`
is a no-.git web-session export. The work IS pushed (branch verified),
but the machine has no proper clone, and the repo has four `claude/*`
branches and no declared mainline. Housekeeping precedes everything
in §5.

## 2. What the game would consume

A content pack is five canonical-JSON files beside a world pack:
`manifest.json` (identity + hashes, written last — the commit record),
`content-plan.json` (per-region danger bands + budgets),
`placements.json` (rules `world_boss.v1` | `dungeon_binding.v1`, arena
origin/side, exclusion radii, lock report), `territories.json`
(run-encoded cell sets; roster entries `{enemyId, weightPercent,
nightOnly}`; packSize, maxActive, respawnPressure, elitePermille,
dangerBand), `report.json` (the audit that authorized export).

Importer obligations are frozen and numbered (format doc §"Importer
obligations"): refuse wrong pack/format ids, hash-verify exactly four
payload files, verify payload format pins, **cross-check base identity
against the world pack it loads beside** (mismatched pair refuses at
import), require `report.ok == true`, require manifest self-consistency,
treat closed-enum surprises as errors and open-vocabulary surprises as
data. A reference Godot 4 addon exists
(`consumers/godot_addon/worldfiller_importer`, `class_name`, refusal
messages, decoded cells, point queries) and the format doc + verifiers
are declared sufficient to build an importer without reading worldfiller
source. This matches our worldforge_importer doctrine exactly:
validating importer, refuse-don't-coerce, pack boundaries hard.

## 3. The Wildshot mapping (the design work this plan exists for)

- **`enemyId` is OUR vocabulary.** The recipe's content library ships
  placeholder enemies; the game supplies real ones. Integration means
  authoring a Wildshot content library whose ids are the roster we
  actually have (the six ordinaries + elite tier), so territories carry
  rosters the game can instantiate from EnemyDefs. This is
  designer-authored recipe data, not code.
- **Danger bands map to CORE-44, not to stats.** Bands are structure
  ("how hard is this region"); Wildshot difficulty is composition
  (pressure count, pattern complexity — never density alone, never HP
  sponging per CORE-36). The mapping table (band → allowed pressure
  combinations / roster tiers) is a designer artifact this plan
  deliberately leaves open.
- **Runtime spawning must be sim-lawful.** Territories define structure;
  the game owns live spawning. Any roster draw (weightPercent,
  elitePermille) is randomness → it MUST ride a named serialized PCG32
  stream owned by SimWorld (rng_enemy or a new dedicated stream), never
  global RNG (the sim/ ban is absolute). `nightOnly` has no Phase A
  meaning (no day/night) — carried, ignored. `respawnPressure` likewise
  has no meaning in zero-reward lab scenarios; it becomes real when
  persistence exists (kill-state deltas keyed by stable pack ids, per
  the importer README — a Phase B concern by definition).
- **Scenario plumbing mirrors WorldForge:** `ScenarioDef.worldforge_pack`
  already routes scenarios onto worlds; consumption adds a sibling
  (e.g. `worldfiller_content`) that loads the content pack beside the
  world pack, cross-checked by the importer's base-identity obligation.
  Serialization impact expected minimal (spawned enemies are ordinary
  EnemyStates; territory/placement data is static, excluded from
  serialize like other static pack data).
- **Vendor, don't fork:** copy the reference addon under `addons/` per
  its install pattern; game-side wrapper stays thin. Contract-as-built
  notes go upstream (the WorldForge §3.3a precedent).

## 4. What Phase A already proves (why nothing is urgent)

The lab already consumes a real WorldForge world (world_walk) with
walkability-verbatim collision and battery-proven composition on it.
That is the entire Phase A ambition for generated content: prove the
combat lab works on generated terrain. Bosses-on-worlds, territories,
and danger progression are overworld-structure concerns — Phase B
material by the plan's own shape (SPEC-A bill: one greybox arena, zero
rewards; the arenas beyond it were explicit designer-approved
additions). **The scope tripwire applies: no game-side world_filler
code before Gate 1** unless the designer deliberately re-scopes in this
repo. Engineering lean: don't — the deck's decision backlog and the
tester pipeline are the critical path, and world_filler consumption
competes with neither.

## 5. Sequencing ladder (each step gated on the one before)

1. **Housekeeping (any time, cheap):** designer picks world_filler's
   mainline lane (four claude/* branches, no main — same one-branch
   question the planning repo answered); proper git clone lands on this
   machine replacing/beside the no-git export; ecosystem map row
   updates (freeze RESOLVED, F8 done).
2. **world_filler's own user-side exits (designer, in that repo):**
   F2–F5 visual verdicts on the delivered 8x renders; the canonical
   256² world run + design verdict (needs a WorldForge checkout per its
   fixtures/README).
3. **WorldForge behaviors-49/50 merge first** (already a deck go-item):
   merge → dusk re-export → game intake battery. Only then does
   world_filler adopt the new base (upstream doctrine: explicit logged
   decision, regenerate fixtures, re-record coverage). Building a game
   importer against the pre-merge base would target bytes the merge
   orphans.
4. **Gate 1 passes.** (The tripwire line. Everything above this line is
   designer verdicts and upstream repo work; nothing touches the game.)
5. **Post-Gate-1, on explicit go:** direct a Wildshot world (recipe with
   our enemy vocabulary + the band→CORE-44 mapping), export + verify;
   vendor the addon; ScenarioDef sibling field; spawn system on a named
   sim stream; battery + goldens per the standing rituals. Scoped as
   its own milestone when we get there.

## 6. Designer decisions this plan surfaces (deck cards)

1. **Approve this plan** (acceptance) — ratifies the mapping stance
   (§3) and the ladder (§5), builds nothing.
2. **world_filler mainline ruling** (ruling) — which branch is the
   lane; unblocks §5.1 housekeeping.
3. Already carded: WorldForge merge (go/no-go), the superseded verifier
   card (mark done when dealt, note → this doc).
4. Deferred by design: the band→CORE-44 mapping table and the directed
   Wildshot world's recipe — authored at §5.5, not before.
