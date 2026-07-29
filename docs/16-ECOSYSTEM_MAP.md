# Wildshot Ecosystem Map (ACCEPTED 2026-07-29 — Decision Deck register; pointer blocks live in all seven repos; branch hygiene swept 2026-07-30)

**Read this first, in any repo, before doing anything.** This is the one
document that names every repo in the project, what it owns, what it may
never do, and where its plan lives. If you (human or agent) are working in
one of these repos and have not read its "authority docs" row below, stop
and read them.

Once the designer approves this map, a short pointer block goes at the TOP
of each repo's agent-facing doc (CLAUDE.md / AGENTS.md / HANDOFF.md) so no
session can miss it. Until then this file is the draft under review.

---

## The pipeline (who feeds whom)

```
tileforge ──► WorldForge ──► world_filler ──► Wildshot-Adventures (the game)
 (tiles)      (worlds)       (content packs)        ▲        ▲
                                                    │        │
              8-bit-sprite-assembler ───────────────┘        │
                   (actor packs)                             │
              music_soundeffects (Resonance Forge) ──────────┘
                   (music/SFX — future importer, Phase 6)

 Wildshot_adventures_pmanning (planning repo) = DESIGN AUTHORITY over all of it
```

Universal contract pattern: **frozen versioned pack + validating importer
that refuses bad packs + manifest that never changes shape.** Downstream
repos never edit upstream artifacts; problems flow upstream as recorded
asks, never as local patches.

---

## Repo register

### 1. Wildshot_adventures_pmanning — planning repo (THE AUTHORITY)
- **Owns:** all design decisions, the build plan, the decision register,
  session records. Conflicts anywhere in the ecosystem resolve HERE, never
  in an implementing repo.
- **Authority docs:** `docs/12-PHASE_A_LAB_BUILD_PLAN.md` (build plan),
  `docs/07-PROTOTYPE_SPEC.md` (SPEC-A), `docs/08-DECISION_REGISTER.md`,
  `docs/15-WORLDFORGE_INTEGRATION_PLAN.md`, `notes/sessions/` (daily truth).
- **State (2026-07-30):** M0–M7 closed; M8 engineering exhausted —
  remaining M8 is designer-side (taste answers, copy pass, laptop pass,
  itch publish, recruitment). Critical path is designer items + calendar.
- **Doc debt:** cleared 2026-07-29 (03-HANDOFF + INTERVIEW_STATE truthed).

### 2. Wildshot-Adventures — the game (Godot 4.6.2, pinned)
- **Owns:** implementation only. Never reinterprets design.
- **Authority docs:** `CLAUDE.md` (repo contract — binding constraint
  digest, no-RNG rule, determinism scope), `notes/DESIGNER_QUEUE.md`,
  `notes/TECH_DEBT_LEDGER.md`, `notes/HANDOFF.md`, `notes/PACK_INTAKE_RUNBOOK.md`.
- **Consumes:** tileforge (in-project importer), WorldForge packs
  (`addons/worldforge_importer`, packFormat 1), assembler actor pack
  (`assets/assembler-pack`, docs/14 contract), projectile sphere pack,
  placeholder audio. world_filler content packs: NOT yet consumed.
- **Hard rules for any session:** no RNG under `sim/`; every pack intake
  runs the battery; gates read exit codes; scope tripwire → ledger.

### 3. tileforge — tile compiler (root of the visual chain)
- **Owns:** 32×32 tile families, themed packages, Godot/Tiled exports.
- **Authority docs:** `HANDOFF.md` (current truth), `ROADMAP.md` (complete —
  all waves closed), `DOCS.md`.
- **State:** feature-complete, consumption phase. 31,431 tiles/theme,
  0 fail/0 warn. Gates run LOCALLY only (private repo, no CI).
- **Pins/versions:** clean packages at `ae1eecb`; **WorldForge deliberately
  still pins the older `a5baf52` forest package** (locks by sourceCommit).
- **Open:** REF3 v2 promotion is user-gated (and blocks the sprite-forge
  start); active interface-improvement thread; 4 recorded upstream asks
  from WorldForge (temple art, roof-overhang field, ruined-road band, dock
  pass-cells).

### 4. WorldForge — world generator
- **Owns:** deterministic world planning → engine-neutral artifact →
  game packs (packFormat 1) with reachability gate.
- **Authority docs:** `HANDOFF.md` (account-switch #6, includes the merge
  runbook §1a), `AGENTS.md`, `docs/GAME_INTEGRATION_PLAN.md`.
- **State (truthed up 2026-07-29):** behaviors 49–50 MERGED (`ae924e3`,
  full §1a duty executed: 226 tests green, goldens drift-free, both
  consumers verified); behavior 56, artifact format 8. The dusk game
  pack was RE-EXPORTED under the v50 identity (flood unchanged 34556,
  byte-stable double export) — **the game-side intake of that
  re-export is the remaining step** (Godot-gated, in the armed queue).
- **Open:** the-eight-holds round-3 verdict, slit-seal ruling, moss-as-solid
  semantic ruling (designer), ferry routing decided-but-unbuilt.

### 5. world_filler — world director / content compiler (newest)
- **Owns:** content decisions WorldForge refuses to make (bosses, spawns,
  territories, danger bands) → content pack format 1.
- **Authority docs:** `HANDOFF.md`, `docs/ROADMAP.md` (F0–F8),
  `docs/FREEZE_REVIEW_FINDINGS.md` (**read before trusting the freeze**).
- **State (re-ruled 2026-07-30, janitor session):** mainline is
  **`main`** (GitHub default) = the designer's approval line — first
  arc F0–F9 COMPLETE, **all visual verdicts approved** (rounds 1–4,
  F2–F5, F8) at behavior 12, 135 tests green on a byte-exact checkout,
  format-2 work (encounter sites) in development. **Content pack
  format 1 FINAL** stays the consumption basis (docs/17). The parallel
  `freeze-review-resolution-tf6bkf` line (its own 38/38 freeze fix,
  dual-verifier battery, 149 tests) is archive-tagged; porting its
  battery onto main is a recorded ask. Old area-share banding verdict
  SUPERSEDED by rounds 1–4 (designer, 2026-07-30). Game-side
  consumption plan: planning docs/17 (ACCEPTED — post-Gate-1).
- **Windows env warning:** repo has no `.gitattributes` and hash-pins
  fixtures — checkouts with `autocrlf=true` break ~30 tests falsely.
  Recorded ask: add `.gitattributes` (LF) + fix the one
  separator-naive guard test.
- **Env notes:** canonical 256² pack not committed (regenerate); Node ≥24.15.

### 6. 8-bit-sprite-assembler — actor sprite tool
- **Owns:** 24×24 actor sheets, player assembly + enemy catalog, the game
  actor pack (docs/14 in the planning repo is the BINDING pack spec,
  designer-approved 2026-07-27 — assembler supersedes Sprite Forge).
- **Authority docs:** `ROADMAP.md`, `ARCHITECTURE.md`; the pack contract
  lives in planning `docs/14-ASSEMBLER_GAME_PACK_SPEC.md`.
- **State drift RESOLVED (2026-07-30 janitor session):** `main` is now
  the consolidated line (`c6dcdc5` — all four codex branches merged,
  build gate green); the game pack's source commit `b7eae05f` is in
  main's history on GitHub. The actor pipeline is reproducible from the
  repo again. Known env nit: `npm run check` requires local review-draft
  PNGs that are not tracked — it cannot pass from a clean clone
  (recorded ask: skip missing review drafts).
- **Open tool work per the spec:** cast animation (CORE-34 needs it), death
  animation, one-command validated "Export game pack" (no hand-zips).

### 7. music_soundeffects — Resonance Forge (audio workstation)
- **Owns:** procedural music + SFX, quality/rights gates, future Godot
  audio packs (Phase 6 importer unbuilt; current Godot piece is a stress
  scene preview only).
- **Authority docs:** `MASTER_PLAN.md` (product contract), `CLAUDE.md`
  (non-negotiables: human listening gate, rights policy), `HANDOFF.md`
  (**do-not-regress taste profile**: 138 BPM F mixolydian, no vibrato,
  sparse fragmented lead — 9 iterations to find, fragile).
- **State:** G1+G2 passed on human listening; UI M0–M6 done; Phases 3–9 ahead.
- **Env landmines:** don't edit store modules while Vite runs; hidden panes
  throttle timers.

---

## Cross-repo rules (bind every session in every repo)

1. **Authority flows one way:** planning repo → game → (asks upstream to
   tools). No implementing repo amends a design decision.
2. **Pack boundaries are hard:** consumers validate and refuse; producers
   version and freeze; nobody hand-edits an exported artifact.
3. **Pins are deliberate:** a repo pinning an older upstream version
   (WorldForge→a5baf52, game→dusk-ae1eecb) is a recorded choice — check the
   pin's doc before "helpfully" upgrading it.
4. **Session end = handoff current:** update the repo's HANDOFF/state doc
   before closing; stale state docs are how agents miss plans (this file
   exists because of that).
5. **Verdicts are designer-only** and follow the verdict system (ruling
   pending — see planning repo once recorded).
6. **All work on designated branches; commit+push before the container/
   session dies.** Unpushed work on a dev machine is issue-class (see
   assembler drift).

---

## Current pinned-version snapshot (2026-07-28)

| Producer | Artifact | Consumer expects |
|---|---|---|
| tileforge | package `dusk-ae1eecb-seed103991` | WorldForge (game-pack lane) |
| tileforge | package `a5baf52` (forest, older, deliberate) | WorldForge (reference lane) |
| WorldForge | packFormat 1, artifact format 8 | game importer + world_filler |
| world_filler | content pack format 1 FINAL (format 2 in dev on main) | (no consumer yet; docs/17 post-Gate-1) |
| assembler | game pack v0, tool commit `b7eae05f…` (57/202, 1×; in main since 2026-07-30) | game `assets/assembler-pack` |
| game | SERIAL 12, goldens current | — |
