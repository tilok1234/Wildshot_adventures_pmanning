# Wildshot Adventures — Handoff for a New Chat, Account, or Work Session

> **ECOSYSTEM POINTER (2026-07-29, designer-accepted doc 16).** This
> planning repo is the DESIGN AUTHORITY over a seven-repo project. The
> shared map — what each repo owns, its authority docs, and the hard
> cross-repo rules — lives at `docs/16-ECOSYSTEM_MAP.md` in this repo.
> Read it before working in ANY Wildshot repo.

> **SYNC-LOG HOOK (doc 18, ACCEPTED 2026-07-30).** At session end, with
> the handoff update, append a line to `tools/sync_log.json` for every
> cross-repo event the session caused (delivery, intake, ask, incident,
> pin change). No event, no entry. Protocol: `docs/18-AGENT_SYNC_PROTOCOL.md`;
> mainlines + pins: `tools/ecosystem.lock.json`.

---

# CURRENT HANDOFF — 2026-07-31 (restart seam; PC restarting, all local sessions ended)

**This section supersedes everything below it.** Full detail +
the in-flight WF paste: the tail HANDOFF of
`notes/sessions/2026-07-30.md` (now the three-day story; Addenda
26–35 = the 07-30 evening + the rested 07-31 day). Board at this
seam, all verified and pushed:

- **The b74 overworld is live in-game** (banded settlement
  streets era; game pin b74, porosity 60). The crosshair scales
  with the viewport now (0a7d69d; size/contrast call still open).
- **TileForge shipped its FIRST gated cut** —
  `tileforge-dusk-complete@e2699cc`, planning-verified: NEW
  roadType 4 "street" (10px sett town band), roadTypesLegacy
  gone, registry non-empty (sl-0055).
- **THE CHAIN IN FLIGHT: WF re-judge sl-0053** (re-pin e2699cc,
  settlement webs → street type 4, ortho L-step diagonal fix,
  renders → designer → export). **The paste lives in the
  session-file HANDOFF — send it to a WF session first.** The
  game intake after is a PAIRED DROP (world pack + e2699cc
  package together — world_builder refuses mismatched identity).
- Opens: sl-0053 (WF — paste UNSENT, confirmed vs GitHub after
  the restart: WF main + newest release both predate the seam),
  sl-0054 + sl-0056 (TF extension rounds RENDERED + preserved
  in-repo at TF 275e5da; designer judgement is the ONLY pending
  step — transitions verdict already recorded, nothing to
  re-render), sl-0055 (resolves on WF adoption), sl-0041
  (director loop), standing sl-0003/sl-0005.
- **Rested-day items still legal today:** THE LOOP acceptance
  run (judgeable → L2 clock) · deck payloads (worldshape 5,
  gate1 2, loop 4 + bar wording) · b65 city walk · audio pass ·
  M2 close + six-ordinaries · Hell Engine V2 listening · music
  seam merge.

Authorities unchanged: docs/19 · docs/20 · doc 18 · doc 16 +
`tools/ecosystem.lock.json`. Sweep duty per incoming logbook
line: verify vs GitHub → commit → resolve → next paste.

---

# PRIOR HANDOFF — 2026-07-30 (workday seam; superseded)

**Superseded by the 2026-07-31 section above; kept as history.** Full detail: the
tail HANDOFF of `notes/sessions/2026-07-30.md` — and that whole
file is the two-day story (doc 18 RATIFIED; publish-gate +
releases-as-transport rollout COMPLETE across all five producers;
**LOOP V1 BUILT** — town → Bone Reliquary King, every gate green;
the overworld arc through b72). Board at this seam:

- **Loop v1 built + swept** (sl-0033; game main 88d2b27). The
  designer's acceptance RUN is pending; L2's clock starts only on
  their "judgeable".
- **b71 intaken; b72 released + verified — game intake PENDING**
  (sl-0035, paste with the designer).
- **world_filler adopted b72 walkability** (sl-0040): b65
  canonical + b72 imported parity-green. **Director-loop ask
  sl-0041 OPEN** (paste with the designer) — mob/boss placement
  over the test overworld as the game's authoring reference
  (docs/20 step 1; export gated on designer approval).
- Opens: sl-0035, sl-0041, standing sl-0003/sl-0005.
- Authorities: docs/19 (loop) · **docs/20 (NEW — world-content
  arc: rehearse by hand → feel verdict → importer; end-state =
  customized generation + authorial hand-carve)** · doc 18 ·
  doc 16 + `tools/ecosystem.lock.json`.

Phone sessions: pull first. Planning's mainline is the standing
branch `claude/questionnaire-note-taking-9vl2sl` (no main by
design). If forced onto a new branch, leave a merge note for the
next PC seam. Sweep duty for incoming logbook lines: verify vs
GitHub → commit → resolve → next paste (mechanics in the
session-file HANDOFF).

## EVENING ADDENDUM — 2026-07-30 (the forklift world-shape session; designer home, PC seam next)

**MERGE NOTE (per the phone-session rule above):** this addendum and
everything it references live on the forced task branch
`claude/operator-protocols-guidelines-ruyu4q` — exactly 3 commits
ahead of the standing mainline, 0 behind, ALL new files (zero
conflict risk). PC seam: fast-forward the standing branch onto it
(`git merge --ff-only origin/claude/operator-protocols-guidelines-ruyu4q`).

- **THE WORLD SHAPE, RECONNECTED (Tier 1, designer):** "rethink as
  Erenshor zones" resolved as a RECONNECTION, not a pivot — the
  Part I persistent zoned world (CORE-16 onward: fractal zone bands,
  city-fee death, geographic quests, living hubs, collectathon) IS
  the game; the Loop milestone is its FIRST MILE, not a separate
  run-game. No CORE amendments needed. Full record + the W-1..W-14
  aliveness/world direction set (two pillar candidates, night/weather
  guardrail, the aliveness test, prop-walkability conversion ask):
  `notes/sessions/2026-07-30-worldshape-forklift.md`. Deck payload
  staged: `tools/decision_deck_items_2026-07-30-worldshape.json`
  (5 confirmation cards). Sequencing flag: world_filler consumption
  likely moves UP (zone-authoring engine).
- **Operator guide v1 + perishable queue snapshot** live at
  `notes/operator-guide/` (derived digests, dated, regenerable).
- Board unchanged from the workday seam: **sl-0035 (b72 game intake)
  and sl-0041 (world_filler dusk-overworld direction) still OPEN**;
  the morning phone WF session died unpushed (verified — nothing
  lost, nothing done).
- Doc-state audit (this seam): docs/08 CORE-53/55 amended rows ✓,
  docs/12 supersession banner ✓, docs/19+20 current ✓, lock truthed
  at workday seam ✓. Nits for later: docs/08 §Bot-testing tail still
  says "Gates 1/2 judged by fresh outside human testers" (pre-rewrite
  phrasing; amended rows govern); the GAME repo CLAUDE.md still
  flags "docs/08+12 truth-up owed planning-side" — that flag is
  itself stale, clear it in passing during a game session.

---

# PRIOR HANDOFF — 2026-07-28 (assessment session close)

**Superseded by the 2026-07-30 section above; kept as history.** The 2026-07-27 handoff
body is kept as history but is FIVE MILESTONES STALE (it says "M2 in
progress"); a full truth-up of it and `notes/INTERVIEW_STATE.md` is a
queued go-item, not yet authorized.

**True position:** M0–M6 engineering complete; M7 complete except
`export.ps1`. The authoritative running record is the game repo's
CLAUDE.md milestone block. A full seven-repo assessment was recorded this
session — read `notes/PROJECT_NOTICE_2026-07-28.md` first (ranked issues +
agenda), then `docs/16-ECOSYSTEM_MAP.md` (all seven repos, DRAFT pending
designer approval), then the game repo's `notes/DESIGNER_QUEUE.md`.

**How this seam works:** the designer is now at their PC and will trigger
items from the queue below one at a time. **Do nothing from this queue
until the designer says so.**

**Branch note (clarified after a PC-session flag):**
`claude/repo-assessment-planning-u6fkjy` was the REMOTE assessment
session's designated branch — it exists only in this planning repo and
holds the assessment artifacts (notice, ecosystem map draft, test deck,
this handoff section). The game repo received NO commits from that
session. Local PC sessions keep their standing branch discipline
(planning: `claude/questionnaire-note-taking-9vl2sl`; game: `main`) and
simply merge/pull the assessment branch's content in — do not create new
branches for this seam, and do not treat the remote branch name as a rule.

**Decision register (adopted 2026-07-28, late seam):** the
designer-built **Decision Deck** (a Claude-design export; the design
session is its source) is THE decision-register UI:
`tools/decision_deck.html` — double-click, fully offline, verified
(no external requests, decisions persist with option + note +
timestamp). Real-queue payload: `tools/decision_deck_items_2026-07-28.json`
(25 cards compiled from the four-ruling menu, this queue, the game
DESIGNER_QUEUE, and the notice). **Designer flow:** open the deck →
PASTE FROM AI → paste the payload file's contents → REPLACE (kills
any sample/test entries in one step) → deal cards. **Convention:**
after a deck session, EXPORT and hand the JSON to the session (paste
or file); it gets committed as `tools/decision_deck_register.json`
and the session sweeps decided items into the planning log + decision
register and executes authorized go-items. Git is the register; the
deck is the UI. Deck FEEL verdicts count per the verdict-system
ruling (queue item 1); rulings/acceptance/go-no-go/evidence need no
tier. `tools/test_deck.html` is retired by this adoption (queue item
2 below is superseded). **Queued after the burn-down
(designer-requested):** a backlog-prevention protocol session —
standing rules so decisions get made at the seam instead of pooling.

**POST-BURN-DOWN UPDATE (2026-07-29 ~01:20):** the queue below was
largely EXECUTED via the Decision Deck register (20 decisions swept —
see `notes/sessions/2026-07-29.md` + game CLAUDE.md tracker). Still
live: the Godot-gated engineering chain (reactive re-baseline → Warden
575 → export.ps1 → v50 dusk-pack intake; note the WorldForge merge
itself was found ALREADY DONE, `ae924e3`), the rested feel cards (M2
close, six ordinaries, audio-in-play), eyes-closed audio evidence,
grass-slits clarification, hours-backfill numbers, Discord link.

## The queue (designer triggers each; listed in leverage order)

1. **Verdict-system ruling** — two-tier / strict / all-count, PLUS the
   shift-work amendment to the fresh-hands rule: the designer works a
   15:00–23:00 shift, so "rested day-start" must key on hours-into-their
   -waking-day and hours-into-session, never wall-clock ("home at midnight"
   is their 17:00). Provisional triggers that STAY regardless of ruling:
   marathon-length sessions and dirty runs (god/slow-mo/runtime edits).
   On ruling: write the planning decision entry, seed the verdict
   register from the provisional backlog (quotes + evidence links), and
   amend the game repo CLAUDE.md fresh-hands digest.
2. **Deck pass (SUPERSEDED → Decision Deck)** — see the Decision
   register note above: `tools/decision_deck.html` + the 2026-07-28
   payload replace `test_deck.html`. The zero-gameplay rulings still
   lead the deal (the three weight-5 cards: verdict system, reactive
   as record, recruitment sizing).
3. **Remaining rulings** (now IN the deck as cards): tester recruitment
   sizing (10–16, ≥4 strangers/cycle — unblocks the Gate 1 calendar and
   is the single highest-leverage one-liner), ledger #12 grandfather
   note, hours-log backfill ruling.
4. **Go-items batch** (each needs an explicit word; all engineering-side):
   - WorldForge: merge the behaviors-49/50 lane per HANDOFF.md §1a, then
     RE-EXPORT the dusk game pack (identity bytes shift) and re-run the
     game intake battery.
   - world_filler: fix the reference verifiers BEFORE any game importer
     copies them (report.json unread; empty manifest.files vacuous;
     TS-vs-GDScript territory wrap-vs-refuse divergence).
   - Docs truth-up: this file's stale body + notes/INTERVIEW_STATE.md.
   - Game repo: `tools/export.ps1` dev/tester profiles + checklist step
     (design staged in game notes/EXPORT_PIPELINE_DESIGN.md).
   - Ecosystem map approval → then pointer blocks at the top of all seven
     repos' agent-facing docs.
5. **Designer-machine task (not agent-doable):** push the sprite-assembler
   exporter commit `b7eae05f…` from wherever it lives — the actor pack the
   game consumes is currently reproducible from NO known repo. Cheapest
   insurance in the project.
6. **Standing designer items:** itch page + devlog + Discord (open since
   M3), weekly GIF #2 (fresh material: Warden fight, M6 pack in the dusk
   town, generated world).

---

# HISTORICAL HANDOFF BELOW (2026-07-27 — stale, kept for record)

**Handoff date:** 2026-07-27, late-night session close (supersedes all earlier handoffs; written for an account switch — the new session may have no memory of anything below)  
**Project stage:** Pre-production planning **CLOSED**. **Build phase RUNNING — M0 and M1 completed and designer-approved 2026-07-27 late night** (M1: pixel-match + net16 acceptance green locally and in CI; dusk arena with an honest bitgrid; Law-6 floor and wall-stub obstacles approved). **M2 in progress** — remaining work list in the game repo CLAUDE.md. **Build sessions run rooted in the game repo now**; this repo stays the design authority.  
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

> **(For build sessions — start the chat in `C:\Users\headc\Documents\Wildshot-Adventures`.)** Continue building **Wildshot Adventures**. Your CLAUDE.md is the standing contract — the milestone tracker in it says exactly where the build stands (currently: M2 in progress with a full remaining-work list). The planning repo at `C:\Users\headc\Documents\Wildshot_adventure_final_planning` is the design authority — consult `docs/12-PHASE_A_LAB_BUILD_PLAN.md` for the plan and record milestone completions + design decisions there per its `notes/INTERVIEW_STATE.md` protocol (one approved decision = one commit + push, both repos). Log hours via `tools/hourslog.ps1`. Keep the established method: one focused task at a time, honest opinions, concrete recommendations, commit everything.
>
> (For design/interview sessions — start in the planning repo and read `notes/INTERVIEW_STATE.md` first, as before.)
