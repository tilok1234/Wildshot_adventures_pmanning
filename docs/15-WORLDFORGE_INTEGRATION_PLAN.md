# Wildshot Adventures — WorldForge Integration Plan

**Doc:** 15-WORLDFORGE_INTEGRATION_PLAN
**Status:** **PROPOSED** (2026-07-27) — planning-pass output, direction
approved by the designer in session ("ye should we do this"); the contract
details and the §4 decision points await explicit designer approval before
anything is recorded as decided. Written from a docs-review session; the
live build and interview sessions own their protocols as usual.
**Tool:** WorldForge (repo `tilok1234/WorldForge`), third forge — see the
Decision Register, Tooling contracts.
**Companion:** `WorldForge/docs/GAME_INTEGRATION_PLAN.md` holds the full
contract drafts (pack layout, manifest, walkability grid, CLI, authored
placement extension). This doc is the game-side view.

---

## 1. Why now

- WorldForge's variety arc is complete (behaviors through 35): sizes tiny
  64² → large 1024², five climates, three densities, landmark stamps, POIs,
  15+ approved worlds, two consumer lanes with cell-exact walkability
  parity, 155 green tests. The generator is no longer the bottleneck —
  *consuming its worlds* is.
- The register already pre-registers its first production use: **drafting
  the slice zone** under the handcrafted-rule contract.
- M1 left a marker pointing here: full blob47 mask derivation was
  explicitly deferred "to WorldForge integration (post-lab)".
- Integration follows the pack pattern this repo already trusts three
  times over (TileForge theme, Sprite Forge, doc-14 assembler pack): raw
  drop in `assets/`, validating importer, manifest contract frozen at v1.

## 2. What the game will consume

One **WorldForge game pack** per world (full contract in the companion
doc):

- `world.json` — the engine-neutral semantic artifact (settlements,
  routes, POIs, landmarks, regions, chunked layers), hash-versioned.
- `resolved/` — TileForge-resolved TMJ + map-data, produced by the same
  adapter the parity tests already prove against both consumer lanes.
- `walkability.json` — a precomputed collision bitgrid (base64-bitpacked)
  with a flood count + spawn cell, derived from the public walkability
  ladder. **This feeds the lab's SoA collision world directly** — the sim
  core never re-derives walkability from tile art, honoring the bitgrid
  discipline from docs/12 §2.3.
- `manifest.json` — base-artifact hash, adapter + generator versions,
  pinned TileForge identity, per-file hashes. Byte-stable; refuses to
  export unvalidated worlds.

## 3. Sequencing against the build plan

| Step | What | When |
|---|---|---|
| 1 | Designer ratifies the pack contract + decision points (§4) | any time; paper only |
| 2 | WorldForge implements `export-game-pack` + authored-placement recipe extension | WorldForge sessions; parallel to lab work, zero game-repo cost |
| 3 | `addons/worldforge_importer/` in the game repo (validate → TileMapLayers + bitgrid + POI/spawn data) | **post-Gate-1**, per docs/12 §6 deferrals; ~the same shape as the doc-14 importer, est. 1–2 sessions |
| 4 | Slice-zone drafting: WorldForge candidates → designer curation via pinned placements / stamps / cell overrides → export → import | Phase B+ / slice preparation |

Nothing lands in the game repo before Gate 1; Phase A scope is guarded.
Steps 1–2 cost the lab nothing and de-risk the slice.

## 4. Designer decision points (open, [U])

1. **Theme pin [U]:** lab runs *dusk*; WorldForge pins *forest*
   (`forest-a5baf52`). Recommended: re-pin WorldForge to a dusk package
   export before `export-game-pack` lands (pinned-package changes are
   designer-authority under WorldForge's AGENTS rules; the lock keys on
   manifest `sourceCommit`, and the dusk export is a TileForge-side task
   like the `sourceCommit` precedent).
2. **Resolution ownership [U]:** recommended — packs ship
   WorldForge-resolved layers; the game never re-implements mask/blob47
   logic (keeps the M1 deferral honest: that derivation lands in
   WorldForge, once).
3. **Importer timing [U]:** confirm post-Gate-1 (recommended) or pull
   earlier if a lab milestone wants a generated test arena.
4. **Handcrafted-rule mechanics:** the curation pass becomes *recipe
   input* — pinned placements, per-recipe stamps, sparse cell overrides —
   so curated geography is authored, reproducible, and diffable, and
   progression-critical placement (portals, dungeons, quest beats,
   secrets) is hand-decided by construction (CORE-20 consequence 2,
   CORE-27 authored-where). No approval needed on the principle (already
   registered); the vocabulary shape is in the companion doc for review.

## 5. Constraints this plan honors

- **One approved decision = one commit** — this doc records *no*
  decisions; it stages them.
- The register's WorldForge entry (drafts, not authored geography;
  curation is the authoring pass) is implemented, not amended.
- WorldForge's boundaries stay intact: TileForge read-only; the game repo
  is only touched as a separately scoped task; the engine-neutral
  artifact remains the boundary for every consumer.
- Phase A scope guard: the lab imports nothing from WorldForge until the
  designer schedules step 3.
