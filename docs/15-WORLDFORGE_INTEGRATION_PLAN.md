# Wildshot Adventures — WorldForge Integration Plan

**Doc:** 15-WORLDFORGE_INTEGRATION_PLAN
**Status:** **APPROVED** (2026-07-27) — planning-pass output; direction
approved in session ("ye should we do this"), and the four §4 decision
points decided the same day per the assistant's recommendations ("ye go
with your recommendations on all 4"). Written from a docs-review session;
the live build and interview sessions own their protocols as usual.
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
| 1 | Designer ratifies the pack contract + decision points (§4) | ✅ **DONE 2026-07-27** |
| 2 | WorldForge implements `export-game-pack` + authored-placement recipe extension | ✅ **DONE 2026-07-27** (WorldForge behavior 36; both proven end-to-end: pinned landmark + per-recipe stamp + cell override exported as a validated pack; 170 tests green; Godot half of the verify chain pending a desktop session — settlement pins deferred to a follow-up behavior, see the WorldForge plan doc §5 notes) |
| 3 | `addons/worldforge_importer/` in the game repo (validate → TileMapLayers + bitgrid + POI/spawn data) | **RE-RULED 2026-07-28 [P]:** the *consumer-prep half* (validating importer + walkability→bitgrid decode + manifest/hash parity, fixture-proven, importing nothing real, no lab surface changes) is pulled forward — rationale: M0–M5 landed ~5 weeks ahead of the docs/12 schedule, and the fixture-first playbook integrated two packs in under an hour each on 2026-07-27. The *consumption half* (TileMapLayers render, picker scenario, POI/spawn use) still waits for a real pack + its own generated-test-arena ruling, post-Gate-1 by default |
| 4 | Slice-zone drafting: WorldForge candidates → designer curation via pinned placements / stamps / cell overrides → export → import | Phase B+ / slice preparation; needs the dusk package export (designer TileForge task) |

Nothing lands in the game repo before Gate 1; Phase A scope is guarded.
Steps 1–2 cost the lab nothing and de-risk the slice.

## 4. Designer decision points — DECIDED 2026-07-27 [P]

All four decided per the assistant's recommendations, approved as a batch
("ye go with your recommendations on all 4"):

1. **Theme pin [P]:** WorldForge re-pins to a *dusk* package export at
   Phase 2 start (pinned-package changes are designer-authority under
   WorldForge's AGENTS rules; the lock keys on manifest `sourceCommit`;
   the dusk export is a TileForge-side task like the `sourceCommit`
   precedent). Slice-zone drafts ship dusk-first.
2. **Resolution ownership [P]:** packs ship WorldForge-resolved layers;
   the game never re-implements mask/blob47 logic (keeps the M1 deferral
   honest: that derivation lands in WorldForge, once).
3. **Importer timing [P]:** post-Gate-1, per docs/12 §6 deferrals; may be
   revisited only if a lab milestone explicitly wants a generated test
   arena (that would be its own ruling).
4. **Authored-placement vocabulary [P]:** approved as drafted in the
   companion doc — pinned placements, per-recipe stamps, warn-only-capped
   cell overrides — making the registered handcrafted-rule contract
   mechanical: curated geography is authored, reproducible, and diffable;
   progression-critical placement (portals, dungeons, quest beats,
   secrets) is hand-decided by construction (CORE-20 consequence 2,
   CORE-27 authored-where).

## 5. Constraints this plan honors

- **One approved decision = one commit** — the §4 batch approval is
  recorded here and in the Decision Register's Tooling contracts entry in
  a single commit, matching the established batch-approval precedent.
- The register's WorldForge entry (drafts, not authored geography;
  curation is the authoring pass) is implemented, not amended.
- WorldForge's boundaries stay intact: TileForge read-only; the game repo
  is only touched as a separately scoped task; the engine-neutral
  artifact remains the boundary for every consumer.
- Phase A scope guard: the lab imports nothing from WorldForge until the
  designer schedules step 3.
