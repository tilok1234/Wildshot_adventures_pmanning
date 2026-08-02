# Wildshot Ecosystem Map (ACCEPTED 2026-07-29 — Decision Deck register; pointer blocks live in all seven repos; branch hygiene swept 2026-07-30)

**Read this first, in any repo, before doing anything.** This is the one
document that names every repo in the project, what it owns, what it may
never do, and where its plan lives. If you (human or agent) are working in
one of these repos and have not read its "authority docs" row below, stop
and read them.

The map is ACCEPTED and pointer blocks live at the TOP of every repo's
agent-facing doc (CLAUDE.md / AGENTS.md / HANDOFF.md) so no session can
miss it. STRUCTURAL RULE (learned twice, sl-0003 + the 2026-08-02 audit):
this map states OWNERSHIP, AUTHORITY DOCS, and CROSS-REPO RULES only —
it never restates a repo's implementation status or pins; those live in
each repo's own HANDOFF and in `tools/ecosystem.lock.json`.

---

## The pipeline (who feeds whom)

```
tileforge ──► WorldForge ──► world_filler ──► Wildshot-Adventures (the game)
 (tiles)      (worlds)       (content packs)        ▲        ▲
                                                    │        │
              8-bit-sprite-assembler ───────────────┘        │
                   (actor packs)                             │
              music_soundeffects (Resonance Forge) ──────────┘
                   (music/SFX — v1 pack delivered + consumed)

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
- **Authority docs:** `docs/03-HANDOFF.md` CURRENT section (the live
  boot), `docs/08-DECISION_REGISTER.md`, `docs/23-SLICE_BUILD_PLAN.md`
  (the running milestone), `docs/22-STAT_SYSTEM.md`, `docs/19` + `docs/20`,
  `notes/sessions/` (daily truth). `docs/12` = the retired lab plan
  (supersession-bannered history); `docs/07` = SPEC-A record.
- **State:** LIVE IN `docs/03-HANDOFF.md`'s CURRENT section — this map
  does not restate planning status (the repo-7 lesson, applied at the
  2026-08-02 audit: this row was still M8/Loop-era while the Slice v0.1
  era ran).

### 2. Wildshot-Adventures — the game (Godot 4.6.2, pinned)
- **Owns:** implementation only. Never reinterprets design.
- **Authority docs:** `CLAUDE.md` (repo contract — binding constraint
  digest, no-RNG rule, determinism scope), `notes/DESIGNER_QUEUE.md`,
  `notes/TECH_DEBT_LEDGER.md`, `notes/HANDOFF.md`, `notes/PACK_INTAKE_RUNBOOK.md`.
- **Consumes:** tileforge (in-project importer), WorldForge packs
  (`addons/worldforge_importer`), assembler packs (enemy catalog +
  NPC slice + boss pack, docs/14 contract), the icons proto pack,
  projectile sphere pack, resonance_forge audio v1 (via the game's
  own cue map), and world_filler content packs (the importer is LIVE
  since S0). Live pin truth: `tools/ecosystem.lock.json` only.
- **Hard rules for any session:** no RNG under `sim/`; every pack intake
  runs the battery; gates read exit codes; scope tripwire → ledger.

### 3. tileforge — tile compiler (root of the visual chain)
- **Owns:** 32×32 tile families, themed packages, Godot/Tiled exports.
- **Authority docs:** `HANDOFF.md` (current truth), `ROADMAP.md` (complete —
  all waves closed), `DOCS.md`.
- **State:** LIVE IN THE REPO'S OWN HANDOFF (road arc closed; art-sidecar
  consumption era). Gates run LOCALLY only (private repo, no CI). Pins:
  the lock only. Standing designer rule: NO diagonal roads (sl-0059).
- **Open:** REF3 v2 promotion (user-gated) · sl-0005 partial (gate art +
  hedge; the road-band third satisfied).

### 4. WorldForge — world generator
- **Owns:** deterministic world planning → engine-neutral artifact →
  game packs (packFormat 1) with reachability gate.
- **Authority docs:** `HANDOFF.md` (account-switch #6, includes the merge
  runbook §1a), `AGENTS.md`, `docs/GAME_INTEGRATION_PLAN.md`.
- **State:** LIVE IN THE REPO'S OWN HANDOFF (b77 = the current world,
  game-intaken + walk-accepted; b78 free; scenery loop paused at eleven
  ratified compositions). Pins: the lock only.
- **Open:** see the repo HANDOFF; planning-side, the furnished-world
  round is PARKED (doc 23) and fires only on the designer's word.

### 5. world_filler — world director / content compiler (newest)
- **Owns:** content decisions WorldForge refuses to make (bosses, spawns,
  territories, danger bands) → content pack format 1.
- **Authority docs:** `HANDOFF.md`, `docs/ROADMAP.md` (F0–F8),
  `docs/FREEZE_REVIEW_FINDINGS.md` (**read before trusting the freeze**).
- **State:** LIVE IN THE REPO'S OWN HANDOFF (mainline `main` = the
  designer's approval line, re-ruled 2026-07-30). The content pack
  shipped + is game-consumed (the importer is live; docs/20 arc
  COMPLETE end-to-end); the next milestone is the staged-NOT-fired
  Puppeteer directed round (boss #9 → the next pack version, before
  S4 Snow). Pins: the lock only.
- **Env notes:** canonical 256² pack not committed (regenerate); Node ≥24.15.

### 6. 8-bit-sprite-assembler — actor sprite tool
- **Owns:** 24×24 actor sheets, player assembly + enemy catalog, the game
  actor pack (docs/14 in the planning repo is the BINDING pack spec,
  designer-approved 2026-07-27 — assembler supersedes Sprite Forge).
- **Authority docs:** `ROADMAP.md`, `ARCHITECTURE.md`; the pack contract
  lives in planning `docs/14-ASSEMBLER_GAME_PACK_SPEC.md`.
- **State:** LIVE IN THE REPO'S OWN HANDOFF + ENEMY_EXPANSION_PLAN.md
  (the active lane: the 80-proposal expansion, plan-only, per-slice
  designer gates). Three packs shipped and game-consumed (enemy
  catalog / NPC slice v1 with real cast+death rows / the 13-boss pack
  — wiring opened sl-0122). Pins: the lock only.
- **Open:** the clean-clone `npm run check` ask (reads untracked review
  drafts) · the designer's cut-off intake sentence ("Families that may
  wor…") owed to the expansion plan.

### 7. music_soundeffects — Resonance Forge (audio workstation)
- **Owns:** procedural music + SFX, quality/rights gates, Godot audio
  packs (the v1 pack is DELIVERED and game-consumed — see the lock's
  game←resonance_forge pin).
- **Authority docs:** `MASTER_PLAN.md` (product contract), `CLAUDE.md`
  (non-negotiables: human listening gate, rights policy), `HANDOFF.md`
  (**do-not-regress taste profile**: 138 BPM F mixolydian, no vibrato,
  sparse fragmented lead — 9 iterations to find, fragile).
- **State:** LIVE IN THE REPO'S OWN HANDOFF — this map does not
  restate implementation status (the 2026-08-01 audit lesson: status
  prose here drifts exactly like the pin table did; an RF session
  caught this row still describing the G2 era while G1–G7 + UI M0–M6
  were long complete). Ownership + authority docs + the cross-repo
  rules below remain this map's lane; current phase/milestone truth
  is `HANDOFF.md` in the repo itself.
- **Env landmines:** don't edit store modules while Vite runs; hidden panes
  throttle timers.

---

## Cross-repo rules (bind every session in every repo)

1. **Authority flows one way:** planning repo → game → (asks upstream to
   tools). No implementing repo amends a design decision.
2. **Pack boundaries are hard:** consumers validate and refuse; producers
   version and freeze; nobody hand-edits an exported artifact.
3. **Pins are deliberate:** a repo pinning an older upstream version is
   a recorded choice — read `tools/ecosystem.lock.json` (the only pin
   truth) before "helpfully" upgrading anything.
4. **Session end = handoff current:** update the repo's HANDOFF/state doc
   before closing; stale state docs are how agents miss plans (this file
   exists because of that).
5. **Verdicts are designer-only** and follow the verdict system (RULED
   2026-07-29 via the Decision Deck — docs/08 + the deck register carry
   it; NO feel verdicts from agents, ever).
6. **All work on designated branches; commit+push before the container/
   session dies.** Unpushed work on a dev machine is issue-class (see
   assembler drift, resolved 2026-07-30).
7. **GitHub default branch = ruled mainline, every repo** (doc 18,
   accepted 2026-07-30). The full cross-repo operating protocol —
   sync-log logbook, pack passports, session recipe, janitor rules,
   publish gates, releases-as-transport — is
   `docs/18-AGENT_SYNC_PROTOCOL.md`; read it alongside this map.

---

## Pinned versions — LIVE IN THE LOCK (section superseded 2026-08-01; incident sl-0003 CLOSED here)

The hand-maintained snapshot table that lived here drifted within a
day of being written (incident sl-0003, opened 2026-07-29) and was
found badly drifted again at the 2026-08-01 staleness audit (it
still named a tileforge package three re-pins old and SERIAL 12
against a live SERIAL 14). The lesson is structural, not clerical:
**a second hand-written copy of pin truth always drifts.**

**The single live source of pinned versions is
`tools/ecosystem.lock.json`** — written during intakes and mainline
rulings per doc 18 §10, verified at every planning sweep, and any
mismatch between the lock and reality is an automatic incident.
Read pins there; never restate them here or anywhere else.
