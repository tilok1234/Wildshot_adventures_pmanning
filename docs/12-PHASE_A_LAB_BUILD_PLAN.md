# Wildshot Adventures — Phase A Lab Build Plan

**Doc:** 12-PHASE_A_LAB_BUILD_PLAN
**Status:** Assistant-drafted 2026-07-27 from the adjudicated architecture synthesis; revised same day against the full verification pass (all blocker/major/minor findings applied — see Verification notes); **approved by the designer 2026-07-27** (the six flagged rulings remain open and are ruled on as they come due; M0 start deliberately deferred by the designer at approval time — **executed later the same night; M0 complete**). Tags: [P] proposed for register, [T] test hypothesis the lab exists to answer. Nothing here is [L].
**Amendment 2026-07-27 (designer-approved, same night):** Sprite Forge supersedes Actor Forge v2.3 as the actor/effects source — §2.14 rewritten to the manifest-driven 28-row contract, §4 M-FX rescoped to curate + gap-fill, and the asset drops now live in the game repo at `assets/` (tileforge + spriteforge, `.gdignore`d raw drops).
**Authority:** This planning repo remains the design source of truth. The game repo consumes this plan; it never amends it. Conflicts resolve here, in the register (docs/08), never in game-repo commits.
**Scope contract:** exactly the Phase A minimum content bill (docs/07 §Phase A) — one greybox arena, one class shell, three deterministic weapon frames, 5–6 enemy behaviors, one elite, one equipped-ability test slot, heavy debug tooling, **zero rewards** (CORE-55). Anything beyond this list is out of scope until Gate 1 passes.

> **GATE 1 REWRITTEN 2026-07-30 — supersession notice.** This plan's
> tester/recruitment prose (the two recruited Gate-1 cycles, the
> vacation tester window, §4 M8 recruitment items, the zero-reward
> law) is SUPERSEDED: cold recruitment is retired with cause, the
> LOOP BAR precedes human contact, warm watched first-touches replace
> recruited cohorts, and the zero-reward law is lifted for loop work.
> The M0–M8 execution record below stands as history. Forward scope:
> `docs/19-LOOP_MILESTONE_SPEC.md` (+ docs/08 CORE-53/55 amended
> rows; session 2026-07-30 addenda 9/11/12; deck ratification staged).

---

## 1. Purpose

Build the Phase A solo combat laboratory: a no-reward combat-feel test judged by fresh outside testers (CORE-53), passing only on Gate 1 criteria (CORE-55). The lab simultaneously proves the asset pipeline (CORE-20: TileForge **and** Sprite Forge), the determinism/replay spine (CORE-32), movement-only dodging (CORE-33), and the readability laws (CORE-51) at greybox fidelity — while deliberately keeping the three gate-failure fallback systems (movement verbs, determinism parameters, weapon-frame roster) data-driven and cheaply revisable (register: pre-registered gate-failure consequences).

Two Gate 1 cycles are budgeted inside the ~6-week vacation sprint (~early Oct 2026). Tester turnaround, not designer hours, is the planning constraint (TOOLING: Phase A build window; PLAN-vacation) — so the tester pipeline is primed early (§4 M3) and both cycles' cohorts are recruited deliberately (§4 M8, cycle 1).

---

## 2. Architecture decisions [P]

Adopted as a bundle from the adjudicated three-proposal synthesis (2026-07-27). Each item carries its binding constraints. Approving this doc records the whole bundle [P] in the decision register.

### 2.1 The spine (settled)

- **Pure sim core, engine-decoupled.** `SimWorld` (RefCounted; plain typed-GDScript objects — no Nodes, no Godot physics, no engine clock) owns all gameplay state: actors, SoA projectile pool, telegraphs, hazards, ability/mana state, RNG streams, tick counter. Mutated only by ordered systems inside `step(input_frame)`. `dt = 1/60` compile-time constant; the integer tick is the only clock. (CORE-32, CORE-31, GDD-16/CORE-14)
- **Drivers:** `RealtimeDriver` (accumulator in `_process`, never `_physics_process`; catch-up capped at 5 ticks/frame then slew, logged), `ReplayDriver`, `BotDriver` (flat-out, render optional). Pause = driver stops stepping; nothing gameplay exists outside ticks, so full freeze with zero queued actions is structural (CORE-31, CORE-50). Slow motion = driver divisor; dt never changes, so slow-mo runs stay replay-valid.
- **Stable monotonic u32 entity IDs**, never reused per run; `serialize()`/`state_hash()` from week 1; all damage/spawn/despawn through one resolution path emitting typed events; views consume events and never mutate sim. `SimWorld.players` is an array (length 1 in Phase A); **zero player singletons or `get_player()` globals anywhere** — enemy AI/aggro reads the player list (GDD-16/CORE-14).
- **InputFrame/InputSource port:** human, replay, and bot input are indistinguishable at the sim boundary (SPEC-A instrumentation, PLAN-bots, TECH-12, GDD-16).

### 2.2 Engine / language (TECH-01) [P]

Godot 4.6.2 stable (verified installed on the build machine 2026-07-27; satisfies the importer's 4.3+ floor), exact minor pinned in project.godot and README; upgrades only between Gate 1 cycles. Typed GDScript only; no middleware. C#/GDExtension recorded as escape hatch **confined to the sim module**, triggered only if the M2 stress scene fails budget. (CORE-20, PLAN-vacation)

### 2.3 Collision [P]

No Godot physics in gameplay. Sim-owned custom collision: projectiles = circles in SoA packed arrays; terrain = swept-circle/segment DDA over a solid-tile bitgrid baked from the TileForge walls layer at load; actors = circle bodies, axis-separated slide on the same grid; projectile-vs-actor = brute-force circle tests. **Spatial hash deferred**, upgrade path documented, validated or falsified by the M2 600-projectile stress scene. Collision grid IS the visible wall tiles, so "collision matches visible geometry" is true by construction; corner-snag logging is a one-line DDA hook. Pure overlap = hit; no rolls anywhere (CORE-31, CORE-40, CORE-32, SPEC-A, TECH-04).

### 2.4 Determinism (CORE-32) [P]

- Scope recorded honestly: same build + same platform (Windows) + same scenario/seed/input log ⇒ identical per-tick state hashes. Cross-platform float identity out of Phase A scope.
- **Zero RNG in the player fire path**: spawn pos/angle/formation = pure function of (aim vector, player sim position, weapon resource, cadence phase/volley index, tick). Enforced three ways: module boundary (weapons module sees no entity lists, no RNG), grep lint in the pre-tester-build script, replay hashing.
- RNG: hand-rolled PCG32, serializable, **named streams** owned by SimWorld — `rng_enemy` (authored variation only), `rng_misc`; `rng_vfx` lives outside the sim so cosmetics can never perturb gameplay. Global `randi()`/`randf()` banned under `sim/` via lint.
- InputFrame quantized at sample time: move {-1,0,1}+normalize flag, aim to 1/4096, fire_held, autofire_toggle_edge, ability_pressed, weapon_select.
- Stable-ID iteration order everywhere; single-threaded sim; no dictionary-order gameplay.
- State hash: FNV-1a over canonical full-state serialization every 30 ticks (serialization includes the projectile hit-registries, §2.6). Replay file: header {build hash, scenario id, seed, data-definitions hash, config snapshot incl. movement speed} + InputFrame stream + hash checkpoints. **Golden replays per weapon frame** live in `tests/`, hash-verified headless before every tester build — the standing CORE-32 regression test; replays double as death-recap evidence and bot-failure repros. (REGISTER gate-failure order: determinism parameters live in data/replay config.)

### 2.5 Project structure / draw order [P]

- Directory: `assets/` (raw forge drops, `.gdignore`d — importers consume them), `addons/tileforge_importer` (kept green), `addons/spriteforge_importer` (§2.14), `autoload/`, `data/` (weapons, enemies, patterns, abilities, scenarios, actor_sheet_map, budgets.tres), `sim/` (systems/, collision/), `input/` (human_sampler, replay_source, bot/), `game/` (main.tscn, render_layers.gd, views/ incl. animated_actor.gd), `ui/`, `tests/` (pixel_match, actor_sheet_slice, replay_fixtures, bot_scenarios, run_tests.gd), `tools/` (export.ps1, gif.ps1, hourslog.ps1, hours_report.ps1).
- **Exactly four autoloads, none holding gameplay state:** Config, Telemetry, DebugHub, BootArgs. The sim lives in the Main scene, never an autoload. Sim events flow through the tick event queue, never a global bus.
- **Draw order (CORE-51 Laws 1/2/6):** named z-band constants in `render_layers.gd`, laws cited in comments. Bands, low to high:
  1. floor (deliberately low-contrast greybox)
  2. friendly ground decals (incl. friendly placed zones)
  3. **hostile ground-hazard FILL** (spatial grounding only — the fill is redundant signal, never the sole threat indicator)
  4. actors
  5. player projectiles + ALL player VFX
  6. damage numbers (non-occluding default, §2.10)
  7. **hostile projectiles**
  8. **hostile ground-telegraph RIMS/outlines + arm-progress indicators + hostile windup/cast telegraphs + hostile impact flashes**
  9. HUD
  10. debug overlay
  Every hostile telegraph's threat-carrying element (rim, outline, arm indicator) renders **above every friendly/player band** — Law 1 holds by construction even when the hazard fill is buried under Scattercast spam. Load-time assertions: (a) no view node violates its declared band; (b) **no player-VFX node may be assigned to any ground band**; (c) hostile and friendly projectiles render from **separate nodes**, so content cannot violate layering structurally. A stress-density occlusion screenshot audit (hazard rim + arm indicator legible under maximum player VFX) is an acceptance line at M5 (projectiles) and M6 (hazards).
- The effects pack is accepted against this table (CORE-20, PLAN-prelab-assets). No targeting UI exists anywhere in the tree (CORE-35).

### 2.6 Projectile system [P]

Fixed-capacity SoA pool (pos, vel, radius, damage, ttl_ticks, faction, pattern_id, pierce_left, motion_program, spawn_tick, **hit_registry**), preallocated to 1024; free-list despawn with typed reasons emitted as events. **Hit registry:** per-projectile fixed array of 8 (entity_id, pass_count) slots for pierce/return weapons (Wheelblade's max-2-passes rule); deterministic overflow rule — when all 8 slots are used, unregistered targets take no damage (emitted as DamageBlocked, reason `registry_full`); registries are part of serialization and the state hash so replays stay valid. Motion programs = enum + params, **pure functions of ticks-since-spawn** (straight, decelerate, sine, boomerang-return) — what makes the dodge bot's closed-form projection possible. `WeaponFrame.tres` = cadence_ticks + volley of ShotDefs; the three frames are three data files, zero code (REGISTER: frame roster = .tres edits). Enemy PatternDefs are the same resource family, reused in Phase B. Rendering: MultiMeshInstance2D per sprite family per faction.

**Hostile signature (Law 3, operationalized):** the effects vocabulary defines **one shared hostile signature** — a common silhouette/outline/motion trait (v0 placeholder: bright 1px rim + hard core on every hostile shot) carried by ALL hostile projectiles across all six families and the elite, and absent from ALL player projectiles. Families then differ from each other by **shape/pattern, never color alone** (CORE-50). The M6 Law 3 acceptance row tests hostile-vs-friendly discrimination at stress density, not just family-vs-family.

Visuals strictly split from damage behind the swappable **EffectLibrary** interface — the designer's effects pack drops in by editing one resource; placeholders never leak into sim (TECH-04, CORE-20). **EffectLibrary honors the CORE-50 effect-density/opacity settings on cosmetic and friendly channels only; hostile projectiles, telegraphs, and hazard markers are exempt — clamped at full visibility at every setting** (an accessibility option must never manufacture Law 1/Law 8 violations). F5 hot-reloads all .tres mid-run; any live mutation marks the run replay-dirty.

**Stress budgets (TECH-03 [P/T], stored in `data/budgets.tres`, enforced by the density meter):** hostile projectiles ≤150 ordinary / ≤300 elite; combined live ceiling 600; ≤24 live enemies; ≤150 active effect instances; damage-number instances counted against the effect budget; 60 FPS sustained on dev baseline. (CORE-51 Law 5, CORE-36) **Scenario-composition rule:** worst-case sustained hostile projectiles per scenario, computed from the §3.4 table (Σ volley × TTL / cooldown across the roster), must fit the ordinary ceiling; checked by the density meter in a standing worst-case scenario.

### 2.7 Enemy behavior [P]

Data-composed, **no behavior trees**. `EnemyDef.tres` = lean CORE-40 stats + MovementPolicy resource (chaser / keep-range strafer / orbit / anchor / flanker) + N EmitterSlots {PatternDef, trigger: cooldown ticks / range gate / phase index, telegraph_ticks}. Runtime = explicit 5-state machine (idle/reposition/windup/fire/recover), all timers in ticks, all decisions in-tick from world state + `rng_enemy` only. Schema reserves shield/healer/support slots for Phase B (CORE-44). Elite = ordered PhaseList resource swapping policy + emitter sets on HP%/timer — **pattern complexity, never HP** (CORE-36), density meter as proof. Every EnemyDef auto-generates a bot dodgeability-proof scenario, and **each EnemyDef lands with its passing proof in the same milestone that authors it** (TECH-09, PLAN-bots; §4 M5–M6).

### 2.8 Input [P]

Godot InputMap actions for everything including autofire_toggle and debug keys; fully remappable day one via options screen persisting through Config (CORE-50 "from start"; persistence lands with the remap UI at M3). Three equal InputSources produce identical InputFrames: HumanSampler (mouse-to-world aim snapshotted per tick), ReplaySource, BotSource — one split serving co-op insurance, bot contract, and replay contract at once (GDD-16, TECH-12). Tap = fire edge (cadence-gated); hold = sustained cadence; autofire = latched **sim-side** flag toggled by the frame's toggle edge, so it appears in replays and the HUD indicator reads sim state (SPEC-A instrumentation). The autofire path reads only the aim vector — enemy awareness is structurally impossible (CORE-32 fire input model; CORE-35). Movement/aim/fire are three independent InputFrame channels end to end; firing writes no movement modifiers (CORE-32 independence). M+K authoritative; zero aim-assist code exists; controller is a later sampler-level addition (CORE-13, CORE-50).

### 2.9 Camera / pixel targets (TECH-02 lab subset) [P]

Base render 640×360 (~20×11 tiles — RotMG-style readability radius; vertical half-view ≈ 5.6 tiles), project stretch mode "viewport" + integer scale, texture filter Nearest, letterbox on non-integer displays. Camera2D fixed zoom, no smoothing; view positions rounded to whole base-res pixels **view-side only** (sim floats untouched). Targets [P]: 60 Hz sim + 60 FPS render at stress budget on the dev machine, plus one mid-tier laptop sanity pass before tester release. (CORE-20 32×32 contract, CORE-51 Law 6)

### 2.10 Debug / instrumentation (first-class scheduled scope) [P]

DebugHub + quake-style console + tabbed overlay, 1:1 with the SPEC-A list:

- Spawn/reset: scenario .tres picker (arena + enemy set + seed), spawn-any-EnemyDef, one-key reseeding reset, seed logged. **Lowest-intended-speed loadout is a first-class one-click preset — and in tester builds it is also a tester-visible selectable loadout on the scenario/start screen, not a debug-panel-only artifact** (CORE-53, CORE-33 human confirmation).
- Slow motion (replay-valid), god/invulnerability sim flag — logged, so no verdict launders through it.
- Hitbox/collision display drawn from sim shapes; the same renderer restyled IS the CORE-50 player-facing optional hitbox indicator.
- Projectile count/density meter vs budgets.tres: live count, 5 s peak, per-faction split, sustained-worst-case readout (§2.6 composition rule), red-line thresholds — doubles as the CORE-51 Law 5 stress meter and CORE-36 elite-honesty check.
- Input/autofire state readout from sim state.
- Capture/replay panel: record/save/load/hash-verify; golden replays run headless pre-tester-build.
- Terrain-collision/corner-snag JSONL log (tile coord, impact normal, segment; near-corner flagged).
- Feedback toggles per channel (impact/immunity/blocked/kill/damage-numbers incl. reduce/off), presentation-only, sim ignorant. **Damage-number default is non-occluding:** small, offset above the target, alpha-faded, hard cap on simultaneous instances (counted against budgets.tres), rendered **below hostile projectiles and telegraphs** (§2.5 band 6). **No screen shake or global hit-stop in default feel** (CORE-32 feedback clause).
- Event console over the minimal TECH-07 skeleton: AttackStarted, ProjectileSpawned, ProjectileDespawned(reason), HitLanded, DamageApplied, DamageBlocked, DamageImmune, EntityKilled, TelegraphStarted, HazardArmed, **AbilityCast, ResourceSpent (mana delta, new value), ResourceRegen** — covering SPEC-A's damage/**resource** log line; proc logs are structurally absent until Phase C (noted in §7 TECH-07). Presentation, logs, and bots consume this one queue. (No crit event exists — CORE-40.)
- **Death recap:** freeze-frame + last-5-seconds incoming-hit trace with killing projectile's origin, pattern name, telegraph timing; auto-appended to session log (CORE-51 Law 8; Gate 1 explainable-deaths evidence).
- Runtime stat editor exposing exactly the lean CORE-40 set (movement speed most prominent), edits routed through sim commands, run marked replay-dirty.
- **Fresh-hands guard mechanized:** any runtime edit auto-stamps subsequent feel notes PROVISIONAL. The console verdict command is **split by verdict type**: dodgeability verdicts accept sources {rested-human, bot-proof}; **feel verdicts accept {rested-human} only and reject any bot source** (bots verify mechanics, never feel — TOOLING bot contract). Verdict source is logged with each verdict. (PLAN-fresh-hands.) Data, not willpower.
- GIF pipeline: F9 dumps last ~10 s frame ring buffer to PNG sequence; `tools/gif.ps1` (ffmpeg) converts — the weekly PIPE-testers deliverable (tooling lands at M3).

**Tester-build debug profile (CORE-50, CORE-55 evidence integrity):** `export.ps1` produces two profiles. **Dev** = everything above. **Tester** = sim-mutating tools (god/invulnerability, runtime stat editor, slow motion, arbitrary spawn, F5 hot-reload) are compiled out or locked behind a `--dev` flag that itch zips never ship with. The tester-facing surface is a whitelist: scenario select, lowest-speed loadout, accessibility options, hitbox indicator, feedback toggles, input remapping, replay recording, feedback-bundle export. There is no global difficulty setting, and the stat editor cannot become one by shipping. Defense in depth: if any debug mutation is somehow reachable, Telemetry automatically marks the session segment **excluded-from-gate-evidence**.

### 2.11 Headless / bot mode [P]

`godot --headless` with BootArgs CLI (`--bot=dodge_proof --scenario=X --speed=lowest --runs=N --seeds --ticks --out=report.json`). BotDriver instantiates SimWorld with no presentation, steps flat-out.

- **DodgeBot** (the mechanized half of the CORE-53 lowest-speed proof): movement-only, **fire AND ability disabled** (CORE-33/34 proofs must not lean on them). Primary policy: per tick, enumerate 16 directions + stay, project all hostile projectiles/hazards forward k ticks closed-form, pick safest reachable cell; orbit and axis-strafe baselines as secondary policies. PASS = N seeded runs × M minutes, zero hits. **Proof coverage is three-tier:** (1) per authored pattern, (2) per elite phase AND the elite full fight across phase transitions, (3) **per shipped scenario composition** — the full enemy set on the actual arena geometry including the corner pocket, because testers face compositions, not isolated EnemyDefs, and overlapping fire can be undodgeable even when every component passes solo (CORE-33 honesty; Law 5/8 are per-encounter). Proofs re-run on every pattern/scenario change. Any hit auto-dumps a .wsr repro for human adjudication. Reports include near-miss distances and positional heatmap. **A pattern or scenario ships to testers only with a current passing proof attached; "every tester-reachable scenario carries a passing composition proof" is a line on both the M7 pre-tester-build checklist and the M8 Gate-1-ready checklist.**
- **Proofs are speed-stamped:** every proof records the speed it ran at. If any config or edit sets a candidate baseline below the proven floor, the harness flags ALL proofs stale and blocks tester export until re-proof at the new floor (see §3.2 band clamp).
- **Bot proofs are the mechanized half only.** CORE-33's lab binding is "mechanized via the bot harness, **confirmed by human testers**": a rested-session human pass per pattern at the lowest-intended speed precedes tester build v1 (M8), and each Gate 1 cycle includes tester play at the lowest-speed loadout as logged gate evidence (§4).
- **Calibration canaries:** at least one deliberately undodgeable pattern the bot MUST fail and one trivially fair pattern it MUST pass, kept in `tests/bot_scenarios`. Bot proofs are necessary-not-sufficient.
- **SoakBot:** hours of seeded rotating scenarios; watches crashes, NaNs, pool exhaustion, replay-hash drift. **TTKBot:** per weapon frame vs each EnemyDef (CORE-36 sponge check).
- Hard guard honored in plumbing: bot output lands in `reports/`, labeled "mechanical verification"; **no gate-tracking code reads it** — Gate 1 verdicts come exclusively from fresh outside humans (TOOLING bot contract, CORE-53).
- Schedule note: the primary DodgeBot policy + both canaries land at **M5** (they need only the sim, BootArgs, and closed-form projection — all M3 products), so proofs accompany enemy authoring instead of piling up at M7 (§4).

### 2.12 Hours + session logging (day-one deliverables) [P]

- `tools/hourslog.ps1 start|stop|note` appends to repo-committed `notes/hours.csv`; `tools/hours_report.ps1` prints the 4-week rolling average vs the 40 h floor and flags a breach (the PROD-01 floor-reset trigger). **Both scripts exist before the first lab commit (M0)** — the report is trivial CSV aggregation and must be operative when the first 4-week window closes at end of week 4, not at M4. Dev hours ≠ game-running hours: design, art, and planning time is logged too.
- Tester-side Telemetry: JSONL to `user://sessions/` — build ID (git describe, stamped on HUD and every log line), session start/end and re-engagement segments (CORE-55 20-minute evidence), voluntary-restart count, time-in-combat, all death recaps, per-weapon-frame telemetry (time equipped, mean engagement distance at fire, movement heatmap — evidences "frames change how testers fight"), debug-contamination flags (§2.10 tester profile), and an optional end-of-session **generic open comments box**.
- **CORE-54 evidence discipline:** the market-test signal is how testers describe the game **unprompted** (PIPE-testers). The in-build comments box is labeled supplementary; any game-description it happens to contain is logged "prompted — not CORE-54 evidence." The actual CORE-54 record is a separate log (`notes/core54_log.md`) of verbatim unprompted descriptions harvested from Discord/itch/reddit/feedback bundles, each entry marked prompted vs unprompted if a direct question was ever asked in a debrief.
- **Local files only, one-click zip-feedback bundle — no auto-network telemetry.** Because stranger return rates for manual uploads are poor, a low-friction fallback exists: at session end the build displays (and copies to clipboard) a short human-readable **summary code** — build ID, active-combat minutes, re-engagement count, deaths — that a tester can paste into Discord or itch comments. Onboarding text includes an explicit bundle-return step; each cycle schedules a mid-cycle reminder ping.

### 2.13 Save/config stub [P]

One `user://settings.cfg` (ConfigFile, `config_version` int): input remaps (persisted from M3), hold/toggle fire prefs, accessibility set (effect density/opacity, flash reduction, damage-number mode incl. off, hitbox indicator, UI/text scale, per-channel audio with key-threat channel separate), window scale, feedback toggles, debug prefs, lowest-speed preset. **Every option here has a named implementing milestone (§4): none may exist as a dead key.** Effect-density/opacity and flash reduction are implemented by EffectLibrary at M6 and act on cosmetic/friendly channels only (hostile channels clamped — §2.6); UI/text scaling is applied to HUD/menus at M4. Nothing else persists — the lab is zero-reward by law, so there is deliberately no save system to build or corrupt (CORE-55; TECH-11 deferred).

### 2.14 Actor rendering — Sprite Forge contract (CORE-20) [P]

**Amendment v2, 2026-07-27 (designer-approved: "i approve to change to the other sprite pack"): the 8-bit sprite assembler's game-pack export supersedes the Sprite Forge full pack as the actor/effects source.** Contract, prerequisites (cast anim, deterministic 1× export, manifest, no-BOM), and the game-repo integration plan are in `docs/14-ASSEMBLER_GAME_PACK_SPEC.md` (now binding). Rationale recorded in the 2026-07-27 session log: the assembler is the actively maintained tool (equipment compositor, 259-enemy catalog, readability regression suites), and switching before M5 costs a morning; after Gate 1 it costs an integration plus re-acceptance. The Sprite Forge pack stays in-repo as FALLBACK until the assembler pack passes the slice test and renders the player + first two enemies (M5 acceptance); then it is removed. Everything below this line describes the superseded v1 source and remains as fallback documentation.

**Amended 2026-07-27 (designer-approved): Sprite Forge supersedes Actor Forge v2.3 as the actor/effects source.** The lab consumes the Sprite Forge full pack (in-repo at `assets/spriteforge/`), not stand-in capsules: greybox fidelity applies to environment, but actors ship real sheets because proving the asset pipeline is a stated lab goal. Sheets are placeholder-fidelity by design — polished versions swap in later **under the same ids and contract** (the contract is frozen across the polish pass; the manifest's per-actor cfg gives deterministic regeneration).

- **Contract (verified against pixels 2026-07-27):** manifest-driven sheets. Humanoid rig = 28 rows (idle/walk/attack/cast/dash × down/left/right/up, then block/hurt/death/spawn/sit/work/carry/lean); cell 32 logical × 2 scale = 64 px cells; frames left-to-right, rows top-to-bottom, transparent background. `manifest.json` declares per-actor id, category, cell, sheet path, row layout (label + frame count), rate, flags, and the regeneration cfg. Projectiles and effects are single-loop-row sheets (20 + 15 shipped — see §4 M-FX rescope).
- `addons/spriteforge_importer`: reads `manifest.json` and slices sheets from it; `tests/actor_sheet_slice` verifies each imported actor's sheet dimensions match its declared rows × frames × cell — **manifest-driven, never hard-coded**, so the polish pass and future rig additions cannot silently break the test.
- View-layer `AnimatedActor` component (in `game/views/`): plays the sheet's animation sets; **facing derived view-side from sim velocity (movement) and aim (attacks)** — the sim knows nothing about facing or frames; animation state is presentation, driven by sim events (AttackStarted, HitLanded, EntityKilled) and never feeds back. The lab uses the rig subset it needs (idle/walk/attack/cast/hurt/death); civic rows (sit/work/carry/lean) are ignored until hubs exist.
- `data/actor_sheet_map.tres` assigns the lab roster hand-picked from the 231-actor pack: player shell (candidate: `ranger` — Archer-appropriate) + six roster enemies + Yard Warden. The pack's remaining actors stay untouched by the lab (scope tripwire).
- Milestones unchanged: player renders from its sheet at M2; the first two enemies at M5; the remaining roster + elite at M6. Acceptance lines in §4.

---

## 3. v0 tuning hypotheses [T]

Every number below is a starting hypothesis the lab exists to tune. All live in `data/*.tres`, hot-reloadable, and change without code. Units: tiles and ticks (1 tile = 32 px world scale; 60 ticks = 1 s).

### 3.1 World / presentation

| Parameter | v0 | Tag |
|---|---|---|
| Tile size | 32 px | [P] (Sprite Forge/TileForge logical contract, CORE-20; Sprite Forge sheets are authored at ×2) |
| Base render | 640×360, integer scale ×2/×3/×4, Nearest | [P] |
| Sim rate | 60 Hz fixed; render 60 FPS target | [P] |
| Arena | 48×32 tiles greybox; 1-tile walls; five 3-cell wall-stub obstacles (**amended from 2×2 pillars, designer-approved 2026-07-27** — every 2×2 art option underfilled its blocked footprint; straight wall runs are pixel-honest, Law 8); two corridor walls; one corner pocket; open center ~16×12 for density testing. **Amendments 2026-07-27 (designer, session log):** (a) detail pass — the SAME arena gained data-driven props/decals/floor-patch dressing (dungeon-room reference style) with the §3.1 skeleton and open center preserved; (b) a SECOND, natural-setting readability testbed (`data/arena_forest.json`, Forest Walk scenario) was approved as a SPEC-A addendum — zero rewards, no mechanics, actors/projectiles judged in nature per the sprite-pack doctrine; scenarios now name their arena | [T] — layout is itself a line-of-fire/corner test asset (SPEC-A); built at M1 as `data/arena_lab.json` |
| Render interpolation | toggle built; tester-build default is the **output of the §6 item 1 A/B on a high-refresh display**, not a foregone conclusion; if snap wins, tester builds force 60 Hz vsync so snap and refresh align | [T] |

### 3.2 Player (temporary class shell)

| Parameter | v0 | Tag |
|---|---|---|
| HP | 100; out-of-combat regen 5/s after 5 s untouched (keeps sessions flowing without a health economy); HP bar on HUD (M4) | [T] |
| Mana | 100, regen 5/s — **exists only for the CORE-34 ability slot**; primary fire costs nothing ever (CORE-32); mana bar on HUD (M4) | [T] |
| Move speed, baseline | 4.0 tiles/s | [T] — premier tunable stat (CORE-33/40) |
| **Move speed, lowest-intended** | **3.0 tiles/s** — the dodgeability-verification speed; first-class preset AND tester-visible loadout; every pattern/scenario proof runs here; human rested passes run here (CORE-53) | [T] |
| Move speed tuning band | **3.0–5.5 tiles/s, clamped at the proven floor.** Tuning below 3.0 requires first re-running the entire proof suite at the new floor — proofs are speed-stamped and auto-staled by any candidate baseline below the proven floor; tester export blocks until re-proof (§2.11) | [T] |
| Player body radius | 0.35 tiles; hitbox indicator optional (CORE-50) | [T] |
| Defensive verbs | **none** — movement + free aim only (CORE-33) | [P] |

### 3.3 Weapon frames (three .tres files; deterministic, zero RNG — CORE-32)

| | A "Longbolt" (accurate long-range) | B "Scattercast" (short spread) | C "Wheelblade" (piercing-returning) |
|---|---|---|---|
| Volley | 1 shot, straight | 5 shots, 50° fan | 1 shot, boomerang program |
| Projectile speed | 14 tiles/s | 11 tiles/s | 8 tiles/s out, decelerate, return |
| Range / lifetime | **6.5 tiles ≈ 28 ticks** | 4 tiles ≈ 22 ticks | apex 5 tiles, total 90 ticks |
| Radius | 0.15 tiles | 0.12 tiles | 0.20 tiles, pierces (hit-registry, max 2 passes/target — §2.6) |
| Damage | 12 | 4 per pellet (20 point-blank) | 9 per pass (max 2 passes/target) |
| Cadence | 24 ticks (2.5/s) | 30 ticks (2.0/s) | 48 ticks (1.25/s) |
| v0 DPS shape | 30 sustained at range | 40 point-blank, decaying with spread | 11–22.5, line/lane control |

All [T]. Intent: A pulls fights long and thin, B pulls them close and brave, C owns lanes and retreats — the spatial distinction Gate 1 must detect ("frames change where and how the player fights", SPEC-A). Firing applies zero movement modifiers in all three (CORE-32 independence).

**Range invariant (survives retuning):** no player weapon's effective range may exceed **6.5 tiles** (≈ the 5.6-tile vertical half-view + ~1 tile of aim lead — no routine off-screen kills), and **at least two hostile threat envelopes must exceed the longest player range** (v0: Leadshot 10 tiles, Fanmaw 7.5 tiles) so no frame can fight everything from beyond all threat. Checked in pattern review alongside the Law 4 ordering check.

### 3.4 Enemy roster v0 (role-grammar instances — CORE-44, CORE-21 spread)

| Behavior (role) | HP | Body r | Speed (t/s) | Attack | Dmg | Shot speed / r | Shot range / TTL | Telegraph | Cooldown |
|---|---|---|---|---|---|---|---|---|---|
| Rusher (chaser fodder) | 20 | 0.30 | 2.7 (kiteable at 3.0) | ~~contact~~ **3-shot 50° slash arc (amended 2026-07-27)** | 8/shot (point-blank can stack all 3) | 5 t/s / 0.22 | ≈1.1 tiles (ttl 10) | 10 ticks | 36 ticks |
| Husk Archer (aimed shot, keep-range 5–6) | 40 | 0.35 | 2.2 | aimed single | 10 | 7 t/s / 0.18 | 7 tiles ≈ 60 ticks | 12 ticks | 90 ticks |
| Leadshot (predictive shot, flanker) | 45 | 0.35 | 2.4 | intercept-aimed | 12 | 9 t/s / 0.18 | 10 tiles ≈ 67 ticks | **40 ticks** | 120 ticks |
| Fanmaw (fan/cone, anchor) | 60 | 0.45 | 1.8 | 5-shot 60° fan | 8 | 6 t/s / 0.20 | 7.5 tiles ≈ 75 ticks | 30 ticks | 150 ticks |
| Ringer (radial burst, slow chaser) | 55 | 0.40 | 1.6 | 12-shot radial | 7 | 5 t/s / 0.20 | 6 tiles ≈ 72 ticks | 36 ticks | 180 ticks |
| Blightcaster (delayed ground hazard, keep-range) | 50 | 0.35 | 2.0 | 1.5-tile hazard circle, arms 45 ticks, lingers 120 ticks | 12 | — | — | 45 ticks (= full arm time) | 150 ticks |

**Amendment 2026-07-27 (designer, session log):** every enemy attack is a
visible telegraphed pattern (projectile/arc) — silent contact-only damage is
retired from the roster (the sim mechanism remains, unused). The Rusher row
above reflects it; Law-4 ordering stays monotone (slash 10 < Husk 12 < Fanmaw
30 < Ringer 36 < Leadshot 40 < Blightcaster 45).

All [T]. Spread check (CORE-21): Rusher/Husk die head-on (2 and 4 Longbolt hits); Fanmaw/Ringer/Blightcaster demand positioning; Leadshot punishes straight-line kiting and now **outranges Longbolt** (§3.3 invariant).

**Law 4 compliance is checked, not asserted:** v0 danger ranking (damage × dodge difficulty): Blightcaster ≥ Leadshot > Ringer > Fanmaw > Husk; telegraph durations 45 > 40 > 36 > 30 > 12 rise monotonically with it (the earlier draft's Leadshot inversion — 20 ticks on the roster's most dangerous shot — is retuned to 40). **Pattern-review procedure includes a one-line Law 4 ordering check:** sort the roster by ranked danger, assert telegraph prominence order matches; future tuning cannot silently reintroduce an inversion. Telegraph prominence scales with danger (CORE-51 Law 4); hostile shots all carry the shared hostile signature and differ per family by shape/pattern, never color alone (Law 3, CORE-50).

**Sustained-density check (from the new TTL/cooldown columns):** worst case is 24 Ringers → 24 × (12 × 72/180) ≈ 115 sustained hostile projectiles < 150 ordinary ceiling; the density meter's standing worst-case scenario verifies the computed bound (§2.6 composition rule).

### 3.5 Elite v0 — "Yard Warden"

- HP **575** [T] — raised from 400 by Decision Deck ruling 2026-07-29: TTKBot measured the current Longbolt killing 400 in 8.38 s vs this line's ~13 s intent (the prose had matched an older statline); 575 restores ~12 s. Honest, not sponge (CORE-36); TTKBot verifies.
- Phases on HP% (PhaseList resource): P1 (100–66%) aimed triples + fan; P2 (66–33%) rotating radial + ground hazards; P3 (33–0%) predictive volleys + fan + chase bursts. All [T].
- Peak hostile projectiles ≤ 300 (budgets.tres); density meter proves complexity-not-density escalation (CORE-36, CORE-51 Law 5).
- Every phase pattern carries a passing DodgeBot proof at 3.0 tiles/s **with ability unused**, **plus a full-fight proof across phase transitions**, before any tester sees it (CORE-33/34, PLAN-bots, §2.11).

### 3.6 Ability test slot (CORE-34; hard-coded, ledgered under TECH-20)

Built at **M4** (mana pool/regen sim-side, AbilityDef loader, ability HUD element; §4). Three swappable test abilities [T], hot-swappable from the scenario/debug panel:

- **Nova Burst** — radial damage 15, mana 30.
- **Quickdraw** — attack speed +50% for 4 s, mana 25. Implemented as a hard-coded cadence multiplier — **no stat pipeline** (TECH-08 stays deferred); named M0 ledger entry.
- **Blast Rune** — placed zone, arms 30 ticks, 18 damage in a 1.5-tile circle, mana 20. Replaces the earlier Snare Trap draft: a slow zone smuggled in an enemy status/stat-modifier mechanism (TECH-08/TECH-07 deferrals); Blast Rune is status-free and reuses the hazard mechanism on the friendly faction.

No encounter may require any of them (CORE-34) — verified at M6 by a full arena clear with the ability never used; all dodgeability proofs run ability-disabled. AbilityCast/ResourceSpent/ResourceRegen events make the slot observable in logs (§2.10).

---

## 4. Build milestones

Window per PLAN-vacation / TOOLING: **~10 evening/weekend weeks now (M0–M7 + the M-FX art track), then the ~6-week vacation sprint (M8 + two Gate 1 cycles)**. Target: tester-ready at vacation start; hard commitment: build in testers' hands by vacation week 3.

**Effects-pack reality check:** this is a solo project — there is no free "parallel" track. The pack gets an explicit hour budget as milestone **M-FX** below, and that budget is subtracted from coding capacity when sizing M3–M6. M6 integrates the pack behind EffectLibrary or ships law-compliant placeholders; the pack-vs-placeholder call for the tester build is **pre-registered for end of M5 (~week 7)**, not left to drift (PLAN-prelab-assets: ad-hoc placeholder shapes invalidate readability testing, so placeholders must themselves pass the 9-row acceptance).

**Pre-registered slip ladder (checked at the week 5–6 hours_report checkpoint, and whenever the 4-week rolling average breaches the floor):**
1. SoakBot + TTKBot + secondary DodgeBot policies slide to M8.
2. Behaviors 5–6 (Ringer, Blightcaster) + elite P2/P3 authoring slide to vacation week 1 (the pre-registered roadmap position, docs/05).
3. Render-interpolation A/B is cut (snap + forced 60 Hz vsync ships).
**Hard floor:** the M3 determinism spine and the M7 export/dodge-proof path are done pre-vacation; only M5/M6 *content* items may enter M8. Slip beyond that invokes the register's scope ladder, by rule, not mood.

### Pre-vacation (evenings/weekends, weeks 1–10)

**M0 — Repo, contract, skeleton (week 1).**
Game repo created; CLAUDE.md contract per §5; Godot 4.6.2 pinned; CI skeleton green on first push (lint job per the CI addendum); directory layout per §2.5; `tools/hourslog.ps1` **and `tools/hours_report.ps1`** + `notes/hours.csv` live **before the first code commit** (PROD-01) — first weekly report scheduled for end of week 4, when the first rolling window closes; `notes/TECH_DEBT_LEDGER.md` opened, seeded with named entries: hard-coded ability effects (incl. Quickdraw's cadence multiplier — no stat pipeline), fixed class-shell stats, arena-only spawning, placeholder EffectLibrary entries, brute-force actor collision, PNG-sequence GIF path.
*Accept:* repo builds an empty window; hours log has entries; `hours_report.ps1` runs against them; ledger committed.

**M1 — TileForge proven (weeks 1–2).**
TileForge importer integrated; **§4 pixel-match acceptance test green in this project**; greybox arena scene assembled from TileForge tiles (dungeon-room set), walls layer baked to the collision bitgrid; low-contrast floor confirmed against Law 6.
*Accept:* pixel-match test passes headless; arena loads; bitgrid matches visible walls by construction.

**M2 — Sim core + movement + camera + Sprite Forge player + stress scene (weeks 2–3).**
SimWorld spine per §2.1; RealtimeDriver; player kinematics with grid slide; camera per §2.9; runtime stat editor (movement speed first); prev/curr position storage + interpolation toggle; **Sprite Forge importer + AnimatedActor component, player rendering from its sheet (§2.14)**; **minimal projectile stress rig pulled into M2 explicitly** — SoA arrays + straight-line motion + brute-force circle collision + one MultiMeshInstance2D renderer, no weapons/patterns/despawn reasons; **this rig is the seed of the M3 pool, not throwaway** — so the **600-projectile stress scene and the spatial-hash / C#-port escape-hatch verdict genuinely happen at M2. Do not let this verdict drift past M2.**
*Accept:* 60 FPS sustained at 600 live rig projectiles + 24 actor stand-ins on dev machine; player renders from the Sprite Forge sheet with correct facing from sim velocity; actor-sheet slice test green; movement feels responsive at 3.0 and 4.0 tiles/s; full-freeze pause works (CORE-31).

**M3 — Aim/fire/autofire + deterministic projectiles + public channel (weeks 3–5).**
InputFrame/InputSource port; tap/hold/autofire with sim-side latch + HUD indicator; all three WeaponFrame.tres files (Longbolt at the §3.3 capped range); SoA pool finalized from the M2 rig + motion programs incl. boomerang + hit-registry; DDA terrain collision + corner-snag log; **replay capture + FNV-1a hashing + first golden replays** (landed with the second weapon frame, before any enemy exists — determinism is cheapest to prove on an empty arena); RNG lint in place; input remap UI **with settings.cfg persistence of remaps** (CORE-50 "from start" honestly met); **F9 ring-buffer GIF capture + `tools/gif.ps1`**; **itch page, devlog thread, and bare Discord stood up** (hours of work, moved here from M7 so the tester-recruitment pipeline gets the full pre-vacation runway — PIPE-testers, docs/05).
*Accept:* golden replay per frame hash-verifies across 10 consecutive headless runs; tap/hold/autofire all follow free aim into empty space; remaps persist across restart; zero movement modifiers while firing; **first weekly GIF posted to the devlog + one community** (r/rotmg or an indie/bullet-hell community) — the weekly cadence starts here and never stops.

**M-FX — Effects pack: curate + gap-fill (art track, weeks 4–8, rescoped 2026-07-27, designer-approved).**
The Sprite Forge pack already ships 20 projectile and 15 effect sheets — including telegraph rings/cones/beams (`telering`/`telecone`/`telebeam`), charge-up, muzzle, and impact effects (`assets/spriteforge/projectiles|effects`) — so M-FX is **curation + gap-fill, not author-from-scratch**. Remaining authored work: (1) assign **player-vs-hostile families** from the 20 projectile shapes (per-family shape language, Law 3); (2) apply the **shared hostile signature** as a rendering treatment across ALL hostile shots (§2.6 — a treatment, not a sprite); (3) author hazard **arm-progress indicators** (§2.5 band 8). Sequenced after M3 so real projectile motion exists to curate against; the (reduced) budget is still subtracted from M3–M6 coding capacity. **Pre-registered decision, end of M5 (~week 7): curated pack or law-compliant placeholders for the tester build.** The nine-row acceptance (§ M6) is unchanged and applies to whichever ships.
*Accept:* curated set delivered against the EffectLibrary interface (families assigned, hostile signature applied, arm indicators authored), or the placeholder decision is recorded with a date.

**M4 — Debug/instrumentation layer + ability slot + HUD (weeks 5–6).**
Console + overlay; density meter vs budgets.tres (incl. sustained-worst-case readout); feedback toggles incl. the non-occluding damage-number default; event skeleton (§2.10 list incl. AbilityCast/ResourceSpent/ResourceRegen); death recap **plus a one-off debug hostile-pattern emitter** (a PatternDef fired from the debug spawner) so the recap is testable before enemies exist; god/slow-mo; spawn/reset + scenario picker; lowest-speed preset; remaining settings.cfg keys; **UI/text scaling applied to HUD and menus** (CORE-50); **player HP + mana HUD elements** alongside the autofire indicator; **the CORE-34 ability slot: sim-side mana pool/regen, AbilityDef loader, all three test abilities hot-swappable, ability HUD element**; fresh-hands PROVISIONAL stamping with the **split verdict command** (§2.10).
*Accept:* every SPEC-A instrumentation line demonstrable; a self-play death against the debug emitter produces a complete recap naming pattern and telegraph timing; all three abilities cast, spend mana, and appear as AbilityCast/ResourceSpent in the event console; HP/mana HUD reads sim state; text-scale option visibly changes the HUD at runtime.

**M5 — First enemies + dodge proofs + collision at density (weeks 6–7).**
Chaser + aimed shooter from EnemyDef.tres; 5-state machine; overhead HP bars (general presentation, no targeting — CORE-35); **both enemies rendering from Sprite Forge sheets**; TTK event logging; density meter exercised with live hostiles; hostile-vs-friendly draw-order assertions active; **DodgeBot primary policy + both calibration canaries land here** (headless CLI minimal), so each EnemyDef ships with its proof in the milestone that authors it.
*Accept:* both behaviors killable without any target selection; deaths explainable via recap; both enemies render from Sprite Forge sheets with correct facing from sim velocity/aim; **stress-density screenshot audit: hostile shots legible above maximum player VFX and above damage numbers** (Laws 1/2); Rusher + Husk carry passing 3.0 tiles/s ability-off proofs; canaries behave correctly (undodgeable fails, trivial passes).

**M6 — Full roster + elite + effects/audio/accessibility integration (weeks 8–9).**
Remaining four behaviors, **each landing with its passing proof**; Yard Warden PhaseList with per-phase + full-fight proofs; EffectLibrary interface finalized **including the effect-density/opacity scaler (cosmetic/friendly channels only, hostile channels clamped — §2.6) and the flash-reduction mode**; **effects-pack acceptance run — a written NINE-row checklist:** the eight CORE-51 laws **plus a photosensitivity row** (no element exceeding ~3 flashes/s, no full-screen luminance flips, on defaults; flash-reduction option verified to further reduce whatever passes) — applied to whichever ships, pack or placeholders; acceptance exercised in a stress-density scenario at the budgets ceiling with the density meter on, **including damage-number spam, the hazard-rim-under-max-player-VFX occlusion audit, a minimum-density render pass (hostile channels still fully visible at the lowest density setting), and the Law 3 hostile-vs-friendly discrimination test at stress density**. Acceptance is an event with a record, not a vibe. **Audio cue map** written (each key threat class → distinct placeholder cue → bus) + eyes-closed sanity test in pattern review (Law 7, CORE-50); placeholder WAVs wired. **Law 4 ordering check** run as part of pattern review (§3.4). **CORE-34 verification: one full arena clear with the ability never used.**
*Accept:* all six behaviors + elite spawnable from scenario picker, all rendering from Sprite Forge sheets; every pattern + elite phase + elite full fight carries a current passing proof; elite peak density ≤ 300 with meter proof; 9-row acceptance record committed; density/opacity/flash-reduction options demonstrably change friendly/cosmetic rendering while hostile channels stay clamped; cue map exists and key threats are audibly distinct eyes-closed; no-ability full clear logged.

**M7 — Full bot harness + composition proofs + export pipeline (weeks 9–10).**
SoakBot, TTKBot, secondary DodgeBot policies (orbit, axis-strafe), reporting polish; **composition proofs for every shipped scenario** (full enemy set on the actual arena incl. corner pocket) and the elite full fight (§2.11); `tools/export.ps1` with **dev and tester profiles** (§2.10), versioned Windows zip, butler push unlisted itch; pre-tester-build checklist script assembled.
*Accept:* full pre-tester-build checklist passes end-to-end: pixel-match, actor-sheet slice, golden replays headless, RNG lint, per-pattern + per-scenario composition proofs (incl. canaries behaving correctly), tester-profile export produces a zip a clean Windows machine runs without dev setup **with no sim-mutating debug tool reachable** (CORE-53, CORE-50).

### Vacation sprint (~6 weeks from ~early Oct 2026)

**M8 — Gate-1-ready hardening + release + recruitment (weeks 1–2).**
Buffer for pre-vacation slip (per the slip ladder — only M5/M6 content items may legitimately land here); laptop sanity pass; tester onboarding text (no coaching content; includes the bundle-return step + summary-code instructions); feedback-bundle zip flow; re-engagement and **fresh-tester** operational definitions locked (§6 item 6); **rested-session human pass per pattern at 3.0 tiles/s** (fresh-hands rules apply) — the human half of CORE-33's "mechanized AND confirmed by humans"; **tester build v1 (tester profile) published unlisted on itch**. **Recruitment: over-recruit 10–16 candidates — floor of ≥4 strangers per cycle (attrition buffer above the ≥3-strangers-per-gate-playtest standing rule) — and hold ≥5 candidates (incl. ≥3 strangers) in reserve, untouched by cycle 1, as the cycle-2 cohort** (PIPE-testers, CORE-53).
*Accept — the Gate-1-ready checklist, mapped to CORE-53/55:*
- Zero rewards present anywhere in the build (CORE-55).
- Session/re-engagement logging produces the 20-minute evidence per tester; summary-code fallback works.
- Every death produces an explainable recap (Law 8).
- Every pattern + elite phase + elite full fight + **every tester-reachable scenario composition** carries a current passing lowest-speed proof (CORE-53, §2.11).
- Human rested pass at 3.0 logged per pattern; **lowest-speed loadout selectable on the tester-facing start screen**.
- **Tester debug profile verified:** no god/stat-editor/slow-mo/arbitrary-spawn reachable in the itch zip; contamination auto-exclusion tested.
- **Every CORE-50 baseline option demonstrably changes runtime behavior in the tester build** (remaps, hold/toggle, density/opacity, flash reduction, damage-number modes, hitbox indicator, text scale, audio channels).
- Controls evidence: golden replays green, corner-snag log clean on the arena tour route, autofire HUD state correct in replay.
- Per-frame telemetry distinguishes the three frames in the builder's own sessions (engagement distance + heatmap separate visibly).
- Build runs on a non-dev Windows machine from the itch zip.

**Gate 1 cycle 1 (weeks 3–4):** build in testers' hands week 3 (≥4 strangers in the cohort); **each tester's protocol includes at least one session segment on the lowest-speed loadout, logged as gate evidence** (CORE-33 human confirmation); mid-cycle bundle-return reminder ping; collect bundles + summary codes; harvest unprompted descriptions into the CORE-54 log; **standing weekly task: continue recruiting the cycle-2 cohort (≥3 new never-exposed strangers, target 4+) via the itch/Discord/community pipeline while cycle-1 feedback is processed**; iterate with the pre-registered failure order as the iteration path — CORE-33 movement verbs first, then CORE-32 determinism details, then frame roster — all three are data-file changes, not rewrites (REGISTER).

**Gate 1 cycle 2 (weeks 5–6):** revised build to the reserve cohort — **≥3 new strangers who have never played any prior build**; returning cycle-1 testers may play and **inform iteration only**; **formal Gate 1 evaluation evidence (re-engagement minutes, feel verdicts, explainable-deaths, lowest-speed segments) counts fresh-tester sessions exclusively** (CORE-53); formal evaluation before block end. Pass ⇒ Phase B starts inside the block. Repeated failure ⇒ the register's pivot/stop ladder. Builder feel verdicts never close the gate (CORE-53).

---

## 5. Session workflow

**Game-repo CLAUDE.md contract** (committed at M0):
- Design authority is the planning repo (this repo). The game repo implements; it never reinterprets. On any conflict, stop and flag.
- The binding-constraint digest (CORE-31/32/33/34/35/36/40/44/50/51/53/55, GDD-16, SPEC-A) is embedded verbatim; every session works under it.
- **No-RNG rule** restated where the AI will see it: nothing under `sim/` calls global RNG; the player fire path calls no RNG at all.
- **Quiet-lab rule for gate sessions:** during tester playtests, no coaching, prompting, explaining, or watching-over-shoulder commentary; testers play unattended. **CORE-54 evidence is unprompted only:** descriptions harvested verbatim from Discord/itch/feedback channels go to the CORE-54 log; the in-build comments box is supplementary and its contents are never logged as CORE-54 evidence; any debrief answer to a direct question is marked "prompted" (CORE-54, PIPE-testers).
- **Fresh-hands rule:** feel and dodgeability verdicts count only per the split verdict command (§2.10) — dodgeability from {rested-human, bot-proof}; **feel from rested humans only, never a bot**; the PROVISIONAL stamp is honored, never overridden by enthusiasm at hour 14 (PLAN-fresh-hands). Feel-verdict sessions scheduled at day start.
- Scope tripwire: any work item outside the SPEC-A minimum content bill is refused and ledgered.

**Hours-log rule (PROD-01):** `hourslog.ps1 start` before any project work — code, art, design, planning; `stop` after. `hours_report.ps1` (live from M0) run weekly, **first run end of week 4 when the first rolling window closes**; a 4-week rolling average below 40 h triggers the floor reset, the §4 slip ladder, and roadmap re-derivation by rule, not by mood. Phase A actuals replace the pre-registered 60–150 h effort band.

**Weekly GIF cadence (PIPE-testers):** from first playable (M3), one 30–60 s GIF per week via F9 ring buffer + `gif.ps1`; posted to the devlog and one community — **the channels exist from M3, so this cadence has somewhere to land from day one**. This is a deliverable, not content marketing garnish — it is the tester-recruitment pipeline being primed, and both gate cycles draw their stranger cohorts from it.

---

## 6. Explicitly deferred

Cross-platform/cross-build replay determinism • netcode/rollback (shape preserved, nothing built) • render-interpolation final choice ([T] #1 below) • spatial hash and C#/GDExtension port (profiling-gated at M2) • controller support (sampler-level later; M+K authoritative for Gate 1 — CORE-13) • TECH-06 item/skill composition (ability slot hard-coded, ledgered) • TECH-08 stat pipeline (flat stats; only debug exposure ships; Quickdraw's multiplier hard-coded and ledgered) • TECH-11 real saves • TECH-16 content validation • TECH-18 localization • TECH-19 mod stance (recorded default: no commitment; data-driven definitions keep the door open) • TECH-14 non-bot balance tools (drop-rate percentile sim is Phase D) • CI/nightly infrastructure (pre-tester-build checklist script instead) • audio middleware (Godot buses + placeholder WAVs; music deliberately absent) • Steam Deck/console/memory/loading targets • Steam page/wishlists (wait for slice-quality footage [LATER]).

**Open [T] items the lab itself must answer:**
1. [T] Render interpolation vs pixel-snap — rested-session A/B **run specifically on a high-refresh (120–165 Hz) display**, since a 60 Hz sim snap-rendered on testers' common high-refresh panels produces judder that reads as "controls don't feel dependable" (a literal Gate 1 criterion). The tester-build default is the A/B's output, not a foregone conclusion; if snap wins, tester builds force 60 Hz vsync so snap and refresh align (CORE-55 latency sanctity).
2. [T] GDScript throughput at the 600-projectile ceiling — M2 stress rig; escape hatches contained by the sim boundary.
3. [T] DodgeBot adequacy — canary calibration standing; proofs (pattern, phase, full-fight, composition) are necessary-not-sufficient; failures ship .wsr repros for human adjudication; humans confirm at lowest speed per §2.11/M8.
4. [T] Audio cue map sufficiency — eyes-closed test per pattern review (Law 7).
5. [T] Effects-pack acceptance — 9-row checklist (8 laws + photosensitivity) + stress-density scenario before placeholders are replaced.
6. [T] Operational definitions, locked before tester cycle 1 so evidence is comparable across testers and cycles (CORE-55, CORE-53): **re-engagement** — a re-engagement event = starting a new combat scenario after a death/exit without prompting; 20+ minutes = summed active-combat time, idle-trimmed. **Fresh tester** — a tester who has never played any prior build of the game; cycle-2 formal gate evidence counts fresh-tester sessions exclusively.

---

## 7. TECH questionnaire mapping

| ID | Status via this plan | Content |
|---|---|---|
| TECH-01 | **[P] answered** | Godot 4.6.2 pinned; typed GDScript; no middleware; C#/GDExtension escape hatch sim-contained (§2.2) |
| TECH-02 | **[P] lab subset** | 60 Hz sim / 60 FPS render; 640×360 integer-scaled Nearest; dev baseline + laptop pass (§2.9). Deck/console/memory/loading open |
| TECH-03 | **[P/T] answered** | 150/300 hostile ordinary/elite; 600 combined; 24 enemies; 150 effects (damage numbers counted); `data/budgets.tres` + scenario-composition rule (§2.6). Loot counts open (Phase D) |
| TECH-04 | **[P] answered** | Pooled SoA sim incl. hit-registry, grid-DDA + circle collision, visuals/damage split behind EffectLibrary with hostile-channel visibility clamp (§2.3, §2.6) |
| TECH-05 | **[P] lab subset** | Weapons/enemies/patterns/abilities/scenarios/actor-sheet-map/budgets as .tres, F5 hot-reload (§2.6–2.7, §2.14). Item/status/quest/loot open (Phases C–D) |
| TECH-06 | open | Ability slot hard-coded + ledgered; answer before Phase C/D item system |
| TECH-07 | **[P] minimal** | 13-event skeleton incl. AbilityCast/ResourceSpent/ResourceRegen (§2.10); no crit event (CORE-40). SPEC-A's damage/resource logs covered for the lab via the ability slot; **proc logging is the deferred remainder** (procs structurally absent until Phase C) |
| TECH-08 | open | Flat stats in lab; only debug exposure ships via TECH-13 tooling; Quickdraw multiplier hard-coded, ledgered |
| TECH-09 | **[P] answered** | MovementPolicy + EmitterSlots over 5-state machine; elite PhaseList (§2.7) |
| TECH-10 | **[P] lab subset** | Scenario resources + spawn/reset panel (§2.10). Full encounter/dungeon authoring open (Stages 3–7) |
| TECH-11 | open | Settings.cfg stub only (§2.13); real save model at the slice |
| TECH-12 | **[P] answered** | InputFrame/InputSource port; M+K authoritative; no aim assist (§2.8) |
| TECH-13 | **[P] lab set** | The §2.10 list incl. tester-build debug profile. Loot forcing / world-state toggles open |
| TECH-14 | **[P] bot subset** | Dodge-proof (pattern/phase/full-fight/composition, speed-stamped)/soak/TTK harness (§2.11). Drop-rate/XP/currency/travel tools open |
| TECH-15 | **[P] lab stance** | Pixel-match + actor-sheet slice + golden replays + RNG lint + proof suite via pre-tester-build script (§4 M7). Full suites open at production scale |
| TECH-16 | open | No content scale in the lab; answer before Stage 6–8 |
| TECH-17 | **[P] lightweight** | Single-branch git; no LFS until the effects pack proves heavy; tagged tester builds via export.ps1 (dev/tester profiles); heavy CI open |
| TECH-18 | open | Only CORE-50 UI/text scaling touches the lab (implemented at M4) |
| TECH-19 | recorded default | No commitment; data-driven definitions keep the door open; answer before architecture lock |
| TECH-20 | ledger open | `notes/TECH_DEBT_LEDGER.md` from M0 with named seed entries (§4 M0); formal answer is a read-out after the combat prototype |

---

## Verification notes

All blocker, major, and minor findings from the 2026-07-27 verification pass were applied; none were rejected. Interpretation choices where a finding offered alternatives:

1. **Damage numbers:** applied both halves of the fix — band moved below hostile projectiles/telegraphs AND a non-occluding capped default specified, with spam added to the M6 stress scenario.
2. **Longbolt range:** chose the cap option (6.5 tiles ≈ vertical half-view + ~1 tile of lead) and additionally kept two hostile envelopes (Leadshot 10, Fanmaw 7.5) beyond the longest player range; both halves recorded as a standing §3.3 invariant.
3. **Snare Trap:** chose the swap option (Blast Rune, status-free, reuses the hazard mechanism) rather than ledgering a one-off slow; Quickdraw's cadence multiplier is the remaining hard-coded exception and is a named M0 ledger entry.
4. **Ability-slot milestone:** implementation extended into M4 as the finding suggests; the CORE-34 "full clear with ability unused" verification runs at M6 because no enemy roster exists at M4 — the debug hostile emitter covers M4-era recap testing instead.
5. **M2 stress ordering:** chose the pull-rig-into-M2 option so the escape-hatch verdict genuinely stays at M2 (the alternative re-dating option was not used).
6. **Leadshot telegraph:** set to 40 ticks, above the finding's 30–36 floor, so the Law 4 ordering is strictly monotone above Ringer's 36 rather than tied.
7. **Speed band:** applied both offered mechanisms — band clamped at 3.0 AND proofs speed-stamped with auto-stale + export block, since the stat editor's dev profile could otherwise still dip below the floor.

## CI addendum (added 2026-07-27, designer-approved) [P]

GitHub Actions on the game repo, jobs activating as their producing milestone lands — CI is the scheduler for verification machinery this plan already specifies headless-first:

| Active from | Job | Catches |
|---|---|---|
| M0 | Lint: banned-RNG grep under `sim/` (the §2.4 fire-path guard), format check | Determinism leaks at commit time |
| M1 | TileForge §4 pixel-match, headless | Renderer/import regressions |
| M4 | **Golden-replay hash gate** on every push (`tests/replay_fixtures/`) | Any CORE-32 determinism break, immediately |
| M7 | Nightly DodgeBot tier-1 pattern proofs at the 3.0 floor | Dodgeability regressions, unattended |
| M8 | Tester-profile export built **only** by CI | Two-profile rule enforced structurally — debug tooling cannot leak into a tester build by hand-packaging |

**Runner constraint (binds via §2.4):** the determinism scope is same-build/same-platform (Windows), so every replay-hash and bot job runs on a **Windows runner** — Linux runners would produce false hash alarms from float drift. Staging: cloud `windows-latest` first (note: 2× Actions-minute multiplier on a private repo, 2,000 free min/month); switch the heavy jobs (nightly bots, soak runs) to a **self-hosted runner on the dev machine** when minutes pinch or at M7, whichever first — free, exact platform match, and overnight soaks run on the hardware the determinism scope is defined against. Switch point left open [P]. Lint/format may run on Linux runners (no sim execution).
