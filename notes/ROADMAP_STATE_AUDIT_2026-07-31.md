# Roadmap-State Audit — six repos (2026-07-31, ~22:00Z 07-30 UTC)

Commissioned by the designer at the evening seam ("i might want to
finish some on the roadmaps first before doing more important
stuff"). Method: six parallel READ-ONLY agents, one per repo, each
comparing the repo's own roadmap/tracker docs against git reality
and against planning's records; drift findings verified
planning-side against GitHub (`gh api`) before being recorded here.
No repo was modified. Local clone paths and mainlines per
`tools/ecosystem.lock.json`.

The audit ran while the game's b72-intake session was LIVE; both of
its hands-free lines landed mid-audit and were swept (sl-0043 b72
intake, game `dde3101`; sl-0044 crosshair fix, game `0a7d69d` —
sl-0035 and sl-0042 RESOLVED; lock game pin b71→b72, porosity 64).
The tail-append compare-and-swap caught the concurrent sl-0044
append — the id rule's fourth live save.

---

## 1. THE FINDING: the assembler has no publish gate (sl-0014 corrected, sl-0045 opened)

sl-0014 (2026-07-29, hands-free from the Codex assembler session)
recorded the publish gate implemented and exercised. The audit
searched assembler main's FULL history and both checkouts: **no
publisher script; no publish-gate / SHA-256 / immutable-artifact
vocabulary anywhere**. GitHub verified planning-side: **zero
releases, no `established-boss-pack-13-v1` tag, only `main` on the
remote.** The line's no-release half was honestly disclosed at the
time; the implementation itself evidently ran and died inside the
Codex sandbox without ever being committed.

Consequences, all recorded in the logbook:
- `|| CORRECTION` appended to sl-0014.
- **Doc 18 rollout truth: four of five producers gated** (tileforge,
  worldforge, world_filler, resonance_forge) — Addendum 6's
  "rollout COMPLETE" overstates by one.
- **Ask sl-0045 opened** (planning → assembler): implement the gate
  per doc 18 §4's letter; next boss-sheet delivery must ride it; no
  pending delivery blocks today (the 13-boss pack is pre-gate,
  grandfathered).
- Protocol lesson for the doc 18 edit pass: a hands-free
  implementation claim is verifiable only if its line carries a
  commit sha; sl-0014 carried none, and nobody noticed for a day.

Also assembler-side: **main sits 2 commits ahead of origin,
UNPUSHED** (`fe831a2` + `8bb18a6`, boss direction authoring
checkpoints, 2026-07-30 ~14:05 local) — exactly the pattern the
gate exists to catch. Push rides sl-0045's session start.

## 2. Corrections to planning's own records (owed-list truth-ups)

1. **`.gitattributes` game ask: ALREADY DONE** — file at game repo
   root, committed 2026-07-30 (hours-log line + HANDOFF gotcha #21).
   Drop from the owed list.
2. **"Eight-holds round-12 review" is mislabeled** — the +6 shifted
   holds landed via the b71 grading fix applied on ROUND-18 state
   (flood 182730→182736), not round 12 (round 12 was the
   harbor-docks/WYSIWYG ratification). The +6 exists only in commit
   `6363271`'s message, not in any persisted WF doc. Correct
   framing: "b71-grading holds review (+6 moss re-rolls vs round-18
   state)".
3. **Assembler "README 960×48 typo" ask: MISROUTED, ALREADY FIXED**
   — the typo lived in the GAME repo's boss-pack README and was
   fixed there 2026-07-30 (game `322066c`). The assembler README
   never contained it. Drop.
4. **Assembler "wip/19-boss-review keep/discard": relabel** — the
   branch name lies; its parking commit (`fb4b664`) contains
   shield / effect-compositor / transparent-tile work exclusively,
   zero boss content (it forked pre-boss-merge). The old checkout
   is now CLEAN (state was committed into the parking commit). The
   designer call is really "keep/discard the parked
   effect-compositor+shield lane".
5. **Music seam merge: rescoped** — main is now **15 commits
   behind** the working line, not just the 5 of
   `codex/approved-audio-export`. The line is a pure superset
   chain: approved-audio-export (+5, publish gate + the shipped
   release) → phase8 Arcade Overdrive V1→V3 (+5) → Hell Engine
   V1→V2 (+5, current checkout, clean, pushed, deliberate
   work-break checkpoint). One rejected dead-end sibling
   (`…-melody-flow`). Seam task: merge the current line → main with
   the gates (npm test in apps/desktop + cargo test -p audio-core
   --lib). Catalog/route integration of Phase-8 slices stays a
   separate deliberate decision.

## 3. Per-repo state and what actually remains

### game (`Wildshot-Adventures`, main — audited mid-intake; now at `0a7d69d`)
DONE: M1–M7 closed (M8 exited by supersession — no explicit banner,
Gate-1 rewrite retired its remainder); Loop v1 complete; b65 + b72
(b71 retired in place) + audio v1 intaken; export pipeline live.
REMAINING:
- **Route THE LOOP onto the overworld** — the next natural
  engineering arc (scenario line + fresh gradient authoring +
  proofs; harbor capital as the better town). Ask-able any time.
- L2 daily-play tuning — clock starts on the designer's
  "judgeable".
- Ledger #16 (replay character block; rides L2).
- Designer-eyes checklists: CORE-50 render pass, nine-row row 7
  (audio, accumulates organically), M2 formal close +
  six-ordinaries (rested).
- Nits: README.md milestone framing stale vs CLAUDE.md (still
  M-track/vacation-sprint era); CLAUDE.md stale "docs/08+12
  truth-up pending planning-side" flag (queued for clearing).

### worldforge (main `38b3f5e`, clean, no live session)
DONE: W0–W9 + behaviors 1–72; 14/28 scenery compositions shipped;
publish lane live; releases b65/b70/b71/b72 all real on GitHub.
REMAINING (the biggest finishable content backlog):
- **11 unshipped catalog compositions**: boardwalk shore, seawall
  front, lighthouse point, windmill hill, watermill reach,
  battlefield (tone-gated on §4 answers), processional way,
  hot-spring glade, geyser field, corrupt grove, hermit garden.
  +3 note-don't-schedule arcs (underground layer, temple precinct,
  new climates).
- **World detail rounds parked**: ruined city + world tree off the
  north edge, farm settlement (recipeSha changes → baseline
  re-record after).
- Engine-ready-when-wanted: ferry routing; zone-crop preview
  tooling (last zone-arc item).
- Designer-gated: tops+ramps contract ruling; §4 dusk-canon tone
  questions; windowed playthrough + formal baseline (original
  roadmap closure items); W-13 prop-walkability ask (drafted
  planning-side, NOT yet handed — zero footprint in WF).
- TileForge upstream art asks recorded in WF HANDOFF (temple/church
  art, overhang-row field, ruined-road band option, road-band art,
  open-plank pier).
- Nits: docs/ROADMAP.md frozen at 2026-07-26 (knows nothing after
  behavior 35); SCENERY_COMPOSITIONS cookfire listed both "remaining"
  and "used" (§1 vs §3); HANDOFF §6 BATCH-6 bullet lists four
  already-shipped compositions as "remaining leaders"; HANDOFF's
  "launch.json viewer-b UNCOMMITTED" claim is false (committed in
  `4497729`).

### world_filler (main `cbb6dbf`, clean, no live session)
DONE: F0–F9 complete; formats 1–3; behavior 14 (b72 ladder);
b65 canonical + b72 imported parity-green; refusing viewer;
publish gate live. **Nothing mechanical left on its roadmap.**
REMAINING (all gated by design):
- sl-0041 directed overworld (designer-driven, OPEN).
- Game-side importer: docs/IMPORTER_READINESS.md prepared, five
  decision points, waits for its own planning session (docs/20
  step 3).
- Conditional: canonical-world regen check at bb7832f (reopen
  verdict loop only if canonical content moves).
- Beyond-first-arc backlog list (minibosses/patrols, factions,
  treasure nodes, quest hooks, interiors, AI recipe authoring…).
- Nits: HANDOFF §1e stale-in-place (says ladder adoption "not yet
  ratified"; §1h shows it executed same file); docs/ROADMAP.md
  opening still says first cross-platform CI run pending; local
  branch `claude/freeze-review-resolution-tf6bkf` (16 unique
  commits, remote deleted) + the non-git sibling snapshot folder —
  keep/delete designer call someday.

### tileforge (master `ce15155`, dirt = known parked scratch only)
DONE: all waves complete (0–9, T, Q, R, S, A, RD); road
restoration `0b0b1f5` verified at code level; publish gate live in
the CLI; pin truth-up `a6b2281`.
REMAINING: exactly two unchecked tracker boxes, both gated — REF3
v3 promotion (designer visual approval) and the Unity importer
(if-Unity-ever). Plus: 30-second pane smoke check (extension was
disconnected); 208b791 bare-corridor display doctrine question
(designer); first real pack cut through the gate (only when a
consumer asks; drops stale `roadTypesLegacy`); ashpile under-edge
ruling; scratch delete/keep. Nits: two stale orphaned worktree
registrations (prune whenever); on-disk pack-docs/ stale by
doctrine (guide.js is truth).

### assembler (main local `8bb18a6` = origin+2 UNPUSHED)
DONE: Phases 1–4 complete; Phase 5 at 33 slices (32 done); boss
lane: 14 direction entries (12 approved), 10 animation corpora
(7 visually accepted, 3 static-only by design).
REMAINING:
- **Publish gate (sl-0045)** — see §1. Push main first.
- Phase-5 slice 33 (open): Goblin War-Crown, Furious Depraved
  Rhino, Gunslinger Boar Rider animation corpora + the Rhino
  direction redesign + Eclipse Unicorn Sovereign — all
  approval-gated visual candidates; HANDOFF "Exact Next Step" =
  Eclipse Unicorn direction review.
- Wildshot game-pack export completion: still refuses without
  approved license text + compact effect-pack contract; writer /
  editor action / consumer handoff slices pending. No export
  button/CLI yet.
- Phase 6 Windows release: deferred until a distribution identity
  + deliberate release checkpoint.
- Effect/shield compositor: ON ICE (the parked wip lane, §2.4).
- Nits: HANDOFF archive-tag prose narrower than reality (four
  tags exist; merged `codex/enemy-outlines` has none); branch
  name/content mismatch on wip/19-boss-review.

### resonance_forge (checkout on `codex/phase8-hell-engine-subtle-variation-v2` `5726e37`, clean, deliberate checkpoint)
DONE: Phases 0–7 closed (G7 + the shipped release verified
exact-match vs planning); Arcade Overdrive V3 slice approved.
REMAINING (the most genuine roadmap runway):
- **Hell Engine V2 exact-file listening verdict** — the one open
  README box. FEEL/audio → rested rule.
- Phase 8 continuation: Celestial War, The Void (unstarted
  concepts; decide Hell Engine first per MASTER_PLAN §17).
- Phase 9 beta hardening + gate G8: not started (perf, stability,
  migration, backup/restore, installer, docs, completed test-game
  pack).
- §8.2 launch SFX domains beyond the six approved families
  (explosions, movement, environmental, stingers) — no
  checkpoints yet.
- **Seam merge → main (15 commits, §2.5)** with the gates.
- Nit: hub UI still labels Arcade Overdrive / Hell Engine 'DRAFT'
  (cosmetic; integration withheld deliberately).

### planning (this repo)
Standing docs current at this seam. Own queue: doc 18 edit pass
(memory-held list + today's sl-0014 sha-rule lesson), docs/08
bot-testing tail annotation, docs/03 historical-body truth-up
(queued go-item), doc 17 timing re-anchor at next touch.

## 4. The finish-first menu (designer-facing synthesis)

Mechanical, agent-executable now (pastes exist or are one line):
1. **Assembler publish gate + push** — sl-0045, paste ready.
2. **Music seam merge → main** — 15 commits, gates green expected.
3. **TileForge pane smoke** — 30 seconds with the extension up.

Designer-taste production loops (the real "finish the roadmaps"
meat — each proven, each lands through its gate):
4. **WF scenery compositions** — 11 candidates, your verdict loop.
5. **Assembler boss lane** — 3 animation corpora + Eclipse
   Unicorn, one-at-a-time approvals.
6. **RF Phase 8** — Hell Engine verdict (rested), then Celestial
   War / The Void.

Designer-word-only gates (no work behind them, just your call):
tops+ramps ruling · 208b791 display doctrine · REF3 promotion ·
ashpile under-edge · §4 tone questions · scratch/branch
keep-discard calls.

Deliberately NOT roadmap-finishing (the "more important stuff",
untouched by this audit's ordering): THE LOOP acceptance run,
loop→overworld routing, sl-0041 direction pass, deck
ratifications, importer planning session.
