# Wildshot Adventures — Handoff for a New Chat, Account, or Work Session

**Handoff date:** 2026-07-27, late-night session close (supersedes all earlier handoffs; written for an account switch — the new session may have no memory of anything below)  
**Project stage:** Pre-production planning **CLOSED**. **Build phase RUNNING — M0 and M1 completed 2026-07-27 late night** (M1: pixel-match + net16 acceptance green locally and in CI; dusk arena builds with an honest bitgrid). Open designer confirmations on M1: Law-6 floor eyeball; obstacle-stub deviation ruling (§3.1 2×2 pillars → 3-cell wall stubs — every 2×2 option lied about collision). Next milestone: M2.  
**Interview position:** Part I complete (CORE-01–55, 2026-07-26). Part II production trio answered 2026-07-27 (PROD-01, PROD-03, scope menu). Remaining Part II modules deliberately deferred behind lab evidence.

## The single most important instruction

**This git repository is the source of truth.** Do not rely on chat memory, ZIPs, or summaries. Read `notes/INTERVIEW_STATE.md` first — it holds the live position and the note-taking protocol. After every designer-approved decision: update the questionnaire, decision register, GDD, and interview state, then **commit and push before moving on**. One approved answer = one commit. Never batch write-ups for later — that is how notes were lost before this repo existed.

## Read first, in this order

1. `notes/INTERVIEW_STATE.md` — live position and protocol.
2. `docs/08-DECISION_REGISTER.md` — fastest complete picture of what is decided (including the Tooling contracts section).
3. `docs/12-PHASE_A_LAB_BUILD_PLAN.md` — **the approved build plan**; the next work happens here.
4. `docs/07-PROTOTYPE_SPEC.md` — the Phase A lab's design-level definition.
5. `notes/sessions/2026-07-27.md` — the full log of the session that closed planning.
6. `docs/01-GAME_DESIGN_DOCUMENT.md` and `docs/10-LIVING_DESIGN_QUESTIONNAIRE.md` — when depth or exact wording matters.

## Where things stand (one screen)

**All three external-review blockers closed 2026-07-27:**

- **PROD-01 [P/T], amended same evening:** a **day job exists** — Wildshot is the primary project alongside it. Stated schedule ~8 h/weekday + up to 16 h/weekend-day (≈72 ceiling). **Planning floor 40 h/week — explicitly a claim under test**: hours are logged from Phase A day one; any 4-week rolling average below 40 resets the floor and re-derives the roadmap. No decision depends on 40 holding (measured ~20 still lands the slice at ~8–17 months).
- **PROD-03 [P]:** cash is not a constraint — AI subs ample, Steam fee trivial, music/SFX and store art **self-produced**. The audio pipeline inherits the forge rule: readability Law 7 + the CORE-50 audio baseline encoded from the start. Sustainability backed by employment income; falsifier recorded.
- **Scope menu — Option 4:** the full game as specced stays the target; horizon accepted in writing. **Gate 2 "viable" is defined:** remaining bill at measured slice velocity ≤ 5 years at the then-current floor, else the pre-registered cut order auto-triggers (slice-as-v1.0 → shrink the bill).

**Asset platform (verified by direct inspection 2026-07-27):** designer-built forges, **drops now versioned in the game repo at `assets/`**. **TileForge** — shipping, current release (road-layer retirement, 31,431 tiles × 80 families per theme, 4 themes): `assets/tileforge/` incl. reference pack (GAME-GUIDE.md, FORMATS.md, scenes, flagships). The shipped Godot importer is GDScript (`tileforge_importer.gd`, an EditorScript — the game repo's `addons/tileforge_importer/run_import.gd` drives it headless); the bundled C# file is the Unity path (known-limited, dropped from the project copy). **Sprite Forge** (2026-07-27, **supersedes Actor Forge v2.3**) — 231-actor manifest-driven pack (12 player kits, 128 enemies, 34 bosses, 20 projectiles, 15 effects incl. telegraphs; 28-row rig, 64 px cells, deterministic cfg regen; placeholder-fidelity by design, polished swaps later under the frozen contract): `assets/spriteforge/`. **WorldForge** — third forge, WIP (completion committed): whole-zone drafts from TileForge packages under the handcrafted-rule contract (generated worlds are drafts; curation makes geography authored; progression-critical placement always hand-decided). **The asset gap, rescoped 2026-07-27:** M-FX = curate + gap-fill — player-vs-hostile family assignment, shared hostile signature treatment, hazard arm-progress indicators — needed by ~M5.

**The approved build plan (`docs/12`, approved 2026-07-27):** pure sim core at fixed 60 Hz with replay + state-hashing from week 1; no Godot physics (custom SoA collision, M2 stress-rig escape hatch); zero-RNG player fire path; three-tier DodgeBot + mandatory human lowest-speed confirmation; two-profile builds (testers never get debug tools); **Godot 4.6.2 pinned** (verified at `~/bin/godot`); 12 milestones — 9 pre-vacation (incl. the M-FX effects track) + M8 and **two Gate 1 cycles inside the ~6-week vacation sprint from ≈ early October 2026**; pre-registered slip ladder; CI addendum (staged GitHub Actions jobs, replay/bot jobs on Windows runners per the determinism scope).

**Six designer rulings deliberately open** (ruled on as they come due): sprites-in-lab vs greybox capsules for Gate 1; the Longbolt 6.5-tile cap vs extending enemy envelopes; slip-ladder ordering; end-of-M5 effects-pack deadline; Blast Rune replacing Snare Trap; tester recruitment sizing (10–16 candidates, ≥4 strangers/cycle).

**The game repo is live — M0 complete 2026-07-27:** https://github.com/tilok1234/Wildshot-Adventures, cloned at `C:\Users\headc\Documents\Wildshot-Adventures` (branch `main`). Scaffolded per the build plan §4 M0 + §5: CLAUDE.md contract (binding-constraint digest + session rules), directory skeleton, hours tooling live with the first real entry, CI lint green (banned-RNG grep + gdformat), tech-debt ledger seeded, Godot 4.6.2 pinned and boot-verified. This planning repo remains the design authority; the game repo never amends it. **The next action is M1**: TileForge importer + §4 pixel-match acceptance test green in the game project + greybox arena (theme zip → GAME-GUIDE.md → prove the renderer against `map-reference.png` first).

## Machine-local facts a fresh session needs

- Planning repo clone: `C:\Users\headc\Documents\Wildshot_adventure_final_planning`, branch `claude/questionnaire-note-taking-9vl2sl` (the only branch). Git identity tilok1234 / headchained@gmail.com; push over HTTPS works.
- Game repo clone: `C:\Users\headc\Documents\Wildshot-Adventures`, branch `main`; push works; `gh` CLI authenticated (CI status checks work).
- Godot 4.6.2 stable: `~/bin/godot.exe` (+ `godot_console.exe` for CLI output; also on Desktop).
- Asset drops: **canonical copies live in the game repo at `assets/`** (tileforge + spriteforge, committed 2026-07-27). Designer's originals: `C:\Users\headc\Desktop\Adventures_assets\` (and the older TileForge exports at `Documents\Semantic tile generator design\exports\`). M1 integration path: integrate per the theme package's GAME-GUIDE.md, prove the renderer via the pixel-match acceptance test before anything else.

## How to work with the designer (unchanged, learned over many sessions)

- One focused question or task at a time; finish before moving on.
- They write informally (typos normal — ask when ambiguous rather than guess). They value momentum, honest pushback, and concrete recommendations to react to over open-ended questions. Batch approvals arrive as a short "ye sounds good"; offer 1–3 well-chosen additions, never a flood.
- Challenge material design or production risks honestly — they explicitly want this (the day-job amendment and floor-as-claim-under-test exist because of it).
- Status tags: [L] locked / [P] provisional / [T] test-gated / [U] unknown / [CUT] / [LATER]. Get approval before recording; commit after recording.

## Recommended opening prompt for the new session

> Continue work on **Wildshot Adventures**. The git repo at `C:\Users\headc\Documents\Wildshot_adventure_final_planning` is the source of truth — read `notes/INTERVIEW_STATE.md` first, then `docs/03-HANDOFF.md`, and follow the note-taking protocol (one approved decision = one commit + push). Planning is closed; the approved Phase A build plan is `docs/12-PHASE_A_LAB_BUILD_PLAN.md`; the build phase has started — M0 is complete in the game repo at `C:\Users\headc\Documents\Wildshot-Adventures` (read its CLAUDE.md before working there). Ask me whether to start M1 (TileForge importer + pixel-match + greybox arena) or work on something else (effects pack, WorldForge, open rulings), and keep the established method: one question at a time, honest opinions, concrete recommendations, commit everything.
