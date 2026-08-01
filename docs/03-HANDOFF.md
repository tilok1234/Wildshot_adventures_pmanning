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

# CURRENT HANDOFF — 2026-08-01 (STAT-TALK SEAM, ~10:45Z; the fresh chat's job is THE TALK)

**This section supersedes everything below it.** The full story is
`notes/sessions/2026-07-31.md` (the fresh-account marathon; its tail
HANDOFF mirrors this section). **The fresh session's first moves, in
order:**

1. Read this section + that session-file tail HANDOFF.
2. Verify the board vs GitHub (planning tree clean and synced; game
   at SERIAL 14 / b77 / both packs vendored; wf_filler at behavior
   24, export designer-held) and **ARM THE SWEEP WATCHER** —
   persistent Monitor, the proven v2 lanes: `tools/sync_log.json`
   working-tree dirt (the append lane), LOCAL-HEAD moves
   (producer sessions commit planning themselves — ~10 clean
   instances this session), planning-origin ahead, WF/TF newest
   release by `max_by(.published_at)`. Sweep duty = verify vs
   GitHub → commit → resolve → next paste. Append at the FILE
   TAIL only (anchor on the actual tail; a mid-array insert
   happened once and was self-caught); validate count+dupes
   before every commit; a GitHub 404 on a fresh game commit is
   usually push-timing — check the LOCAL clone before calling
   incident.
3. **THE STAT TALK.** The designer hands over TEN deep researches
   (two engines; the five commissioned topics + five more). ASSESS
   THEM FIRST, properly and unhurried: digest into docs/22
   Appendix A — per research: what it says, what applies, what
   contradicts our locked constraints (research is REFERENCE; the
   design authority stays this repo). THEN open docs/22 block 1
   and run the nine blocks ONE AT A TIME: short brief →
   planning's concrete recommendation → the designer's verdict →
   fill the RULING slot → docs/08 row where register-worthy →
   ONE COMMIT PER BLOCK. The slice bill is the customer
   (sl-0082/0087): 4 zones bracketed Green 1–7 / Dry Reach 8–15 /
   Wetlands 16–22 / Snow Country 23–30, T1–T5 exists in art,
   movement caps are CORE-33-critical, block 9's calculator lands
   as a game paste at the end.
4. Method: plain names first, ids in parentheses (standing
   designer rule); one focused block at a time; honest pushback;
   their informal typos are normal — ask only when truly
   ambiguous.

Board at this seam:

- **THE WORLD IS PLAYABLE THE DESIGNER'S WAY:** b77 overworld
  intaken (road joints + carpet/canopy walkability) and **THE FIT
  RULE is live** (SERIAL 14: props block what the ART shows, the
  player body = the sprite's feet, projectiles share the truth,
  combat hurtbox byte-untouched). **THE WALK IS FORMALLY ACCEPTED
  (sl-0097, 2026-08-01, the designer's words: "like playing
  another game, very good") — sl-0067 RESOLVED, the fit-rule
  acceptance discharged.**
- **THE LOOP BAR is ruled in the designer's own words** (docs/19
  §1, sl-0082) and **SLICE V0.1 is the named next milestone [P]:**
  4 zones with ruled brackets (Green Country 1–7 / Dry Reach 8–15 /
  Wetlands 16–22 / Snow Country 23–30, cap 30 — sl-0087), a dungeon
  per zone, 1–3 world bosses per zone with uniques, simple
  fishing/foraging/skill trees, ~5 quests/zone. **SIX PILLARS**
  since the deck deal (docs/01 §5.5 zones-intertwine + §5.6
  villager-reason; sl-0071).
- **THE REHEARSAL (sl-0041) is deep in designer rounds** (through
  round 11, wf behaviors 22–23): zone frame + danger chapters +
  settlement belts + slice dungeons/bosses recipe-locked + 16
  reason-tagged giver slots + 24 gather spots. **ROUND 12: both
  hand-places LANDED (Green boss at the designer's SE mud pocket;
  Wetlands den designer-locked) — THE SLICE CONTENT SET IS
  COMPLETE: 4 bosses + 4 dungeons, all eight recipe-locked
  (sl-0090). THE EXPORT GO LANDED 2026-08-01 ~11:19Z (sl-0093):
  release wildshot-overworld-pack-dusk-content-c0bf28638648
  shipped b77-pinned, planning-verified (tag→6be201e = the
  embedded sourceCommit; GitHub digest = the logged zip sha
  13e0759d…) — 127 placements / 92 territories / all eight locks
  held / 9-of-9 gates + both consumption verifiers green.
  world_filler is DONE with docs/20 step 1. **THE GAME INTAKE +
  REFERENCE PASS EXECUTED HANDS-FREE same hour (sl-0094, game
  447b681, planning-verified; the producer committed planning
  itself — 4264668, eleventh instance, interleave clean):**
  vendored + passport + b77 pairing mechanized as the 22nd fixed
  gate; FIVE hand-authored picker scenarios on real pack cells,
  all proof-PASSED (battery 28→33); the cold finding recorded
  (no activation leash yet — the importer's core question;
  orbit-vs-point openness). The doc-17 NONE placeholder is now
  the FIRST real game←world_filler pin. **STEP 2 IS ARMED: the
  designer's feel session on the five scenarios (danger ramp,
  boss spot, territory texture — their words).**
- **PACKS HOME:** icons v0.1 (470 glyphs 16×16, intaken sl-0085,
  gate-guarded, UNWIRED until the Loop acceptance) · the NPC slice
  roster (32 characters, **RELEASED wildshot-npc-slice-v1@bf6269c —
  the assembler's first release — and INTAKEN, sl-0092, game
  9192cbf: end-to-end provenance proven publish-guard→release→
  consumer, all shipped hashes verified, 21st fixed gate, scale
  FULLY consistent with the enemy pack**). Both packs home.
  **WIRING HOLD LIFTED (sl-0098, the world-is-the-test ruling):
  both packs wire INTO the Slice v0.1 build** — the separate Loop
  gate dissolved; nothing wires until the slice build starts.
- **THE STAT TALK IS COMPLETE (2026-08-01, this session):** the
  TEN researches assessed into docs/22 Appendix A (skeleton
  survived contact — two recommendations independently confirmed
  by both engines), then ALL NINE BLOCKS designer-ruled, one
  commit each: the lean seven + boring regens · THE damage
  formula (flat−armor, 20% floor) + the no-sponge rider · tier
  DPS budgets + the pattern-fairness gate · per-slot budgets
  (weapon +40%/tier, defense enemy-anchored, T5 = late-Snow
  capstones — the sl-0082 T5 question CLOSED) · levels ⅓
  survivability-weighted, no auto damage, flat-stepped XP ·
  movement bases 100/105/110 + the +15% integrator cap
  (feel-gated [P/T]) · the six-pair tradeoff grammar · the
  one-break unique whitelist + easy swapping [P] · the balance
  calculator (approved; ask sl-0095; PASTE staged in the session
  file — paper-first, no sim change). docs/22 = the standing
  authority; register rows on CORE-37/39/40/41 + the Bot-testing
  contract.
- Opens: sl-0067 (the walk) · sl-0087 (hand-places) · sl-0089 (NPC
  intake paste out) · sl-0041 (rehearsal; export held) · sl-0005
  (TF gate art + hedge, partial — road-band third satisfied).
  **sl-0003 CLOSED at the 2026-08-01 staleness audit** (doc 16's
  hand table removed; the lock is the only pin truth). Feel menu:
  **THE LOOP RUN** (the big one) · b65 city walk · audio-in-play ·
  M2 close + six-ordinaries · Hell Engine V2 · music seam · weekly
  GIF · a glance at the four crosshair styles.
- **Designer-gated items now on the plate** (sweep as they land):
  **the SLICE BUILD GO** (docs/23 staged: S0 foundations → Green
  first; the go fires the S0 paste) · the Hell Engine V2
  exact-file listen (RF session) · the icon tool's source push
  from the other PC. **THE FEEL SESSION IS DONE (sl-0099):**
  all five scenarios played — directed placement PASSES, one
  finding (density low) self-dispositioned as slice tuning =
  the same work item as the S0 leash. **sl-0041 RESOLVED — the
  whole rehearsal arc closes** (rehearse → reference pass →
  feel verdict ✓; the importer is doc-23 S0 work).
  (Resolved this session: THE WALK formally ACCEPTED sl-0097
  ("like playing another game") — sl-0067 closed · the rehearsal
  EXPORT GO sl-0093/0094 · the CALCULATOR built hands-free, five
  gates green, sl-0095/0096 · **THE LOOP GATE DISSOLVED by the
  world-is-the-test ruling sl-0098** — b65 retired with honor as
  the mechanism proof, pack wiring unblocked into the slice.)
- Authorities: docs/19 · docs/20 · doc 18 · doc 16 +
  `tools/ecosystem.lock.json`. Planning's mainline is the standing
  branch `claude/questionnaire-note-taking-9vl2sl` (no main by
  design).

---

# PRIOR HANDOFF — 2026-07-31 (account-switch seam; superseded by the 2026-08-01 section above, kept as history)

**This section supersedes everything below it.** Full detail:
the tail HANDOFF of `notes/sessions/2026-07-30.md` (the
three-day story; Addenda 26–44) **plus
`notes/sessions/2026-07-31.md`** (the fresh-account session:
b76 swept, the game-intake paste verbatim, the icon-set
round). Board, all verified and pushed:

- **THE ROAD ARC IS BUILT, END TO END.** TileForge shipped TWO
  gated cuts today: `@e2699cc` (roadType 4 "street") and the
  arc-closing **`@9b8b2a2`** (roadTypes 1–8 + the roadjoint
  family — 84 hand-authored transitions, 21 class pairs × 4
  orientations, auto-rendered at class switches). WorldForge
  built and released **b75** (street band; no diagonal roads;
  ladder-braid wart closed), designer-look-approved.
- **sl-0058 EXECUTED (2026-07-31 ~21:38Z, hands-free; both
  watcher lanes caught it minutes after publish):** WF re-pinned
  **9b8b2a2** (imported dusk-9b8b2a2-seed103991, WF 4291f79) and
  released **b76** — planning-verified (GitHub digest = logged
  zipSha 98c3170d…; tag→4291f79 on main; world byte-identical
  to b75 modulo identity, 47-cell render diff all class
  switches). **b76 SUPERSEDES b75 PRE-INTAKE and IS THE INTAKE
  TARGET**; b75 stays archive only (sl-0060 resolved).
- **b76 INTAKEN (sl-0064, game e71b6c6+0dae664, ~22:43Z,
  hands-free; planning-verified):** paired 9b8b2a2 bundle landed
  — FIRST explicit game←tileforge pin, TILEFORGE_PACKAGES
  registry (b65/THE LOOP byte-untouched), path 0..3 accepted
  zero-code, porosity 60 held (±2 typed), the 47 joint cells
  DRAW (probe-proven), pretester ALL GREEN 16.9 min. b74
  superseded in place. **WALKED + LOOK APPROVED (designer,
  ~22:51Z, first impressions: "very nice … this looks ghreat")
  — sl-0064 RESOLVED; the sl-0052/sl-0053 street-look arc
  closes on screen. Deeper-walk findings, if any, open their
  own items.**
- **b77 INTAKEN (sl-0067, game 89aa034, ~23:53Z, hands-free;
  planning-verified):** walkability-only delta, 100% typed —
  the four carpet species sum EXACTLY to the 1044 opened cells
  (stump 509 / fallen_log 490 / bone_pile 44 / loot_pile 1);
  flood 46493 exact; porosity pin 60 stands on a zero-diff
  route set; canopy walk-under PROVEN on screen at pixel level
  (0/8525 in-mask diffs, evidence PNGs committed; 2,352 crown
  cells live). b76 superseded in place; TF pairing pin carries.
  **THE THING NOW: the designer's NAVIGATION WALK on b77 — the
  "getting blocked" complaint is the acceptance test (sl-0067 =
  the open line). The sl-0065 dev map is still queued and would
  make the walk nicer.**
- **Standing rule (designer, today): NO DIAGONAL ROADS for the
  moment** — road lanes orthogonal-only everywhere, direction
  changes are L-step pairs (docs/08 Tooling contracts;
  sl-0059). WF implemented it structurally (turn-cost routing).
- **Icon-set round closed (2026-07-31 late):** taxonomy approved
  + seat ruled [P] — a one-time in-repo generated set in the
  GAME repo (the projectiles-sphere-v0 precedent), NOT the
  assembler, NOT a new ecosystem repo. Plan:
  `docs/21-ICON_SET_PLAN.md`; register docs/08 Tooling contracts
  + sl-0062. Ranked strictly behind M-FX; nothing routed.
  **ARRIVED + ASSESSED PASS (sl-0083, 2026-08-01 ~09:05Z):**
  wildshot-icons-proto_0.1.0 — 470 glyphs ALL 16×16, manifest
  parity perfect, semantic ids per the docs/21 sketch, T1–T5
  complete (doesn't force the slice's T4/T5 call), CORE-50
  colorblind proof sheets shipped IN-PACK, coverage inside plan
  estimates across all kinds (stat = exactly 9). Watch-items
  for wiring only: some skill-node rows abstract at 16px; a few
  charm tiers color-first (designer: one glance at the deutan
  sheet). **Four faction NAME CANDIDATES captured [P]: the
  Wardens, the Prospectors, the Circle, the Free Company.**
  **INTAKEN (sl-0085, game d7fbc16 local-verified push-pending):
  vendored byte-true + passport per-file hashes + a
  negative-tested 20th fixed gate + the first game←icon-forge
  lock pin; UNWIRED until the Loop acceptance.** Tool-source
  push from the other PC = the one open item on this thread.
- **NPC slice roster APPROVED + RELEASED (sl-0089, ~10:02Z):**
  32 characters (13 named + 10 zone givers + 9 ambient; the four
  faction reps) from the assembler per the sl-0084 seat —
  designer-approved ("good for the slice rosters... we will get
  to see if it suffices" [P] on-screen taste pending);
  **wildshot-npc-slice-v1@bf6269c = the assembler's FIRST
  release**, published by planning on the designer's go, digest
  byte-verified; the sl-0045 publish gate's provenance proved
  clean pushed source (the b7eae05f wound structurally healed).
  Game intake paste with the designer (raw drop, verify
  manifest hashes, scale-consistency report, NO WIRING until
  slice build).
- **Props/solid-navigation round ROUTED — sl-0063 (2026-07-31
  ~22:39Z, designer: "i will do this in wf now"):** W-13 fired —
  WF converts prop walkability (carpet/canopy/solid, DO NOT
  thin), re-exports as the next behavior; paste with the
  designer's WF session (verbatim in
  `notes/sessions/2026-07-31.md` + sl-0063). Fired while the b76
  intake runs game-side — no collision (immutable tags; the
  conversion becomes the game's NEXT intake after b76). TF stays
  an art sidecar via sl-0005 only if the round finds needs.
  Planning sweeps the delivery.
- **Stat-system design pass QUEUED (designer, ~00:35Z 2026-08-01):**
  "plan out how we do stats… simple but somewhat fancy… connect
  combat and gear together in regards of balance" — the pass the
  designer pre-announced at the loop build ("more structure around
  it later when I plan", docs/19). Planning-repo design session,
  designer-heavy, best AFTER the Loop acceptance run. Scope = the
  loop-era stat frame: finalize the lean sheet (7 stats + 2 regen
  candidates), ONE transparent damage/mitigation formula, T1–T5
  per-slot budgets, movement-speed sources/caps (CORE-33-critical),
  tradeoff grammar for armor/rings, authorized unique rule-breaks,
  and a deterministic balance calculator (TTK/TTD per zone band) —
  explicitly NOT the endgame balance pass (curves re-derive against
  real content, test-gated per house style). **AGENDA STAGED**
  (designer: "lets sert up a plan on how we will plan this out") —
  nine dependency-ordered blocks in the session file; fires any
  fresh morning.
- **Dev map LIVE (sl-0069 resolving sl-0065; game 87bdc15 +
  471fa8c, planning-verified):** press **N** on any pack world —
  corner minimap → fullscreen → off; player dot + facing tick;
  **THE LOOP got the map free** (b65 ships a minimap). Dev-gated
  + negative-tested; 18th fixed gate + CI row; proven on
  committed captures. Acceptance = the designer's first N-press
  (rides the walk). Part II player map stays deferred (doc 13
  §3).
- **Placement rehearsal RENDERS DELIVERED (sl-0041, review round
  live):** first draft on screen — 3 world bosses (clearance-
  proven, named), 10 dungeons bound to existing structures, 57
  route-preferring encounter sites, honest budget-failure X's,
  and a 7-tier damage zoning. Planning's review delivered
  in-chat (~01:10Z): concept right; seams must snap to
  GEOGRAPHY not generator math (villager test); tier count needs
  a deliberate answer vs the 5 gear tiers (planning lean: 5 core
  + safe halo + endgame-pocket band); out-of-gradient islands
  must be typed deliberate-or-artifact. Feedback paste staged in
  the session file; designer drives lock/reroll/paint; export
  gated.
- **Crosshair styles + size LIVE (sl-0080 resolving sl-0077;
  game 4b4c6ec, planning-verified):** four silhouettes (ratified
  classic byte-pinned as default / dot / ring / cross-x) × odd
  sizes 9–15, both profiles, options rows persisted; zero sim
  impact proven; 19th fixed gate + preview sheet committed;
  AUDIO_CUE_MAP eyes-closed slot WRITTEN (deck hand-off
  discharged). Designer-eyes on the styles rides natural play —
  no nag. Icon Tier-0 still sequenced after the Loop acceptance.
- **THE FIT RULE IS LIVE (sl-0081 resolving sl-0078; game
  549e587, SERIAL 14, planning-verified):** props block what
  the art shows (7,560 b77 prop cells → art-measured discs;
  b65/THE LOOP carry it), player body = the ranger sprite's
  10px feet, projectiles share the truth, hurtbox
  byte-untouched, enemies stay grid (asymmetry proven), goldens
  ×10 + 28/28 re-baseline + forest_walk FAIL→PASS as the
  deliberate-change signature; pretester green. **The game sits
  RELAUNCHED — the acceptance is the designer's walk on their
  own three red-line screenshots (provably crossable: desert
  t=51, worst oak pinch t=23).** b78 stays parked (WF park line
  still owed if that session is open).
- Opens: **sl-0067 (b77 walk — the fit-rule walk IS its
  acceptance now)** · **sl-0041 (rehearsal, designer-driven,
  through round 7: 4-zone frame accepted; TEST SLICE confirmed
  (sl-0076); zonal danger CHAPTERS — Green Country [1,2] → Dry
  Reach [3,4] → Wetlands [5,6] → Snow Country [7,8] (behavior
  19); sanctuaries shrunk designer-directed with buildings as
  the floor (behavior 20). **Snow boss flag RESOLVED by the
  designer's rounds — THREE ringed bosses staged (dry_grass /
  mud / snow locks); go = lock → verify byte-stable → gated
  b77-pinned export. Slice-quantity + light quest-giver-anchor
  ask ROUTED (sl-0086, paste with the designer): 4 slice
  dungeons; Green Country's boss count = the designer's open
  call; giver-slot layer skip-if-costly; level brackets land in
  the export record — RULED sl-0087: cap 30 EVEN split, Green
  1–7 / Dry Reach 8–15 / Wetlands 16–22 / Snow 23–30; Green
  Country GETS a world boss, designer HAND-PLACES it soon
  (~lvl 8–10; generation blocked there — the hand-place is the
  doctrinally correct path). **THE STAT TALK RUNS IN A FRESH
  CHAT**: the designer hands over FIVE deep researches at talk
  start (mitigation formulas, movement-speed itemization,
  progression pacing, behavioural skill trees, evergreen boss
  uniques — two engines); the fresh session opens on docs/22's
  skeleton + those. )** · standing sl-0003/sl-0005. Resolved this seam additionally: sl-0065
  (dev map via sl-0069), sl-0070 (diagnosed via sl-0072),
  sl-0073 (executed as behavior 17).
  Resolved today: sl-0053–sl-0058, sl-0060 (superseded
  pre-intake), sl-0061 (intaken), sl-0063 (b77 shipped), sl-0064
  (walked + look approved), sl-0066 (intaken).
- **SWEEP DUTY NEEDS A REAL WATCHER** (learned tonight): repo
  sessions push hands-free lines and releases without the
  designer relaying them — arm a persistent Monitor on
  planning's origin + producer releases. GitHub's `/releases`
  list is NOT newest-first (use `max_by(.published_at)`; the
  by-tag endpoint is authoritative), and appends may sit
  UNCOMMITTED in the working tree — check `git status` too.
- **DECK DEALT + SWEPT (2026-08-01 ~00:50Z; sl-0071):** TWO NEW
  PILLARS (docs/01 §5.5 zones-intertwine + §5.6 villager-reason
  purposefulness), Gate-1 rewrite RATIFIED (docs/08 bot-testing
  nit fixed), loop frame RATIFIED (docs/19 stamped), night/
  weather law, aliveness test, icon seat confirmed, crosshair
  closed (note spawns LATER: selectable styles + size setting).
  **Loop bar deliberately open — the designer's own words owed.**
  Evidence captured: eyes-closed audio (game AUDIO_CUE_MAP slot
  owes the write, next game session).
- **THE LOOP BAR IS RULED (sl-0082, 2026-08-01 morning):** the
  designer's own three sentences (docs/19 §1 rewritten; the open
  deck card discharges) — know your goals and want them / enough
  content to not go stale / hard but fair, effort = progression;
  run mechanism + week test retained beneath. **SLICE V0.1 =
  the named next milestone [P]** (the designer's bill: 4 zones /
  dungeon each / 1–3 world bosses each w/ uniques / simple
  fishing+foraging+skill trees / ~5 quests each / levels 1–30
  zone-bracketed / T1–T4; refinement rounds open; build
  chapter-by-chapter, Green Country first). Zone order confirmed
  by the designer's labeled map (Green Country → Dry Reach →
  Wetlands → Snow Country = the rehearsal's own ranking). The
  stat session's first customer is this bill.
- **Feel menu remaining:** THE LOOP acceptance run (judgeable →
  L2 clock; now judged against the RULED bar) · the fit-rule
  walk (red lines) · b65 city walk · audio-cues-in-play · M2
  close + six-ordinaries · Hell Engine V2 listening · music seam
  merge · weekly GIF.

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
- **Ids are for the record, not the designer (2026-08-01 feedback: "its just so hard for me to remember what for example b77 anbd sl-0065"):** lead with plain-language names — "the map task", "the props round", "the current overworld" — with b-numbers/sl-ids in parentheses once. Board answers in ≤5 plain lines. "What's live?" is always a welcome question.
- They write informally (typos normal — ask when ambiguous rather than guess). They value momentum, honest pushback, and concrete recommendations to react to over open-ended questions. Batch approvals arrive as a short "ye sounds good"; offer 1–3 well-chosen additions, never a flood.
- Challenge material design or production risks honestly — they explicitly want this (the day-job amendment and floor-as-claim-under-test exist because of it).
- Status tags: [L] locked / [P] provisional / [T] test-gated / [U] unknown / [CUT] / [LATER]. Get approval before recording; commit after recording.

## Recommended opening prompt for the new session

> **(For build sessions — start the chat in `C:\Users\headc\Documents\Wildshot-Adventures`.)** Continue building **Wildshot Adventures**. Your CLAUDE.md is the standing contract — the milestone tracker in it says exactly where the build stands (currently: M2 in progress with a full remaining-work list). The planning repo at `C:\Users\headc\Documents\Wildshot_adventure_final_planning` is the design authority — consult `docs/12-PHASE_A_LAB_BUILD_PLAN.md` for the plan and record milestone completions + design decisions there per its `notes/INTERVIEW_STATE.md` protocol (one approved decision = one commit + push, both repos). Log hours via `tools/hourslog.ps1`. Keep the established method: one focused task at a time, honest opinions, concrete recommendations, commit everything.
>
> (For design/interview sessions — start in the planning repo and read `notes/INTERVIEW_STATE.md` first, as before.)
