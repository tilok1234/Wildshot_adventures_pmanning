# The seven-repo docs staleness audit — 2026-08-02 (~17:00)

**What this is.** The designer asked for a full, extensive audit of all
seven repos' project docs for stale/outdated content. Planning ran FIVE
parallel read-only auditors (planning · game · assembler · tileforge+
worldforge · world_filler+resonance_forge), each judged against a
verified truth snapshot of today's state. Rule applied throughout:
**marked history is NOT staleness** — only outdated facts presented AS
CURRENT in a doc a fresh agent would trust.

This file holds (1) what planning FIXED in its own repo, (2) what is
STILL OWED planning-side, and (3) the six ready-to-copy per-seat
pastes for the other repos. Nothing here is lost if a chat dies.

---

## 1. FIXED planning-side (2026-08-02, this sweep)

- **`tools/ecosystem.lock.json` — the incident (sl-0133).** Serialization
  entry read SERIAL 13 / Loop v1 through SIX deliberate re-baselines →
  truthed to **SERIAL 22** with the full chain recorded and a standing
  maintenance rule (every deliberate bump updates the entry in the same
  sweep). Also truthed: icons pin + NPC pin "unwired by ruling" → WIRED
  since S0 seam 4; world_filler content pin "REFERENCE ONLY - no
  importer" → CONSUMED, importer live since S0; b77 pin's navigation
  walk → ACCEPTED (sl-0097); boss-pack artifact string → wiring OPENED
  (sl-0122). `updated` → 2026-08-02.
- **`docs/16-ECOSYSTEM_MAP.md` — restructured to its own lesson.** The
  map now states OWNERSHIP + AUTHORITY DOCS + CROSS-REPO RULES only and
  never restates status or pins (the repo-7 pattern applied to all
  seven). Fixed: the draft-under-review line (it is ACCEPTED), the
  pipeline diagram's "future importer, Phase 6" for audio, the game's
  "world_filler content packs: NOT yet consumed" (HIGH — consumed
  2026-08-01), planning/tileforge/worldforge/world_filler/assembler
  state rows (all one-to-two eras stale), rule 3's dead example pins,
  rule 5's "verdict system (ruling pending)" → ruled 2026-07-29.
- **`docs/20-WORLD_CONTENT_ARC.md`** — ARC COMPLETE stamp added (the
  newest stamp still said "EXPORT IS DESIGNER-HELD"; the export fired,
  intake landed, feel verdict passed, importer live; next pack version
  = the staged-not-fired Puppeteer round).
- **`docs/21-ICON_SET_PLAN.md`** — "UNWIRED until the Loop acceptance"
  → WIRED since S0 seam 4 (+ the dormant `item.unique.undertow` glyph
  recorded as never-bound/tripwired/purges-next-release).
- **`docs/22-STAT_SYSTEM.md`** — Status "DRAFT SKELETON … nothing is
  decided" → THE STANDING STAT AUTHORITY, all nine blocks ruled
  2026-08-01 (the header contradicted the doc's own body).
- **`docs/23-SLICE_BUILD_PLAN.md`** — Status "STAGED [P] … the build GO
  fires the S0 paste" → ACTIVE (GO fired sl-0100; S0+S1 complete; Green
  days open); "Open at staging" → both items EXECUTED, kept as record.
- **`notes/2026-08-02-green-days-round-list.md`** (HIGH — the designer's
  own agenda): the starhook bullet listed **"the feature's real name"**
  as open — a live collision with the no-coined-names law; all its
  other "nobody's-ruled" questions were ruled too (loss = three hard
  lives, land-only + ambient spawns, catch = gold + species-currency
  fish + rare cosmetics). Replaced with the ruled truth + the feel-only
  remainder. Also: boss-art bullet → sl-0122 ruling; walk-over equip
  [T] → retired by the interact era + the bag.
- **`notes/reference/starhook-proto2/INDEX.md`** — corrections
  renumber fallout fixed (#8→#7 for the reel cut), "below"→"above" in
  #9, and the "still-live canonical items" list struck against
  corrections #3/#5/#7 (water fishing PARKED with no reel machinery to
  reuse; gear IN and re-sequenced after the inventory family).
- **`notes/reference/starhook-proto2/README.md`** — banner added: the
  prototype's own doc, read INDEX first; names its three retired
  contents explicitly (undertow, the reel win, reversed keys).

## 2. STILL OWED planning-side (next session picks up here)

Ranked. None are blocking; all are truth-up work. **Progress
(2026-08-02 evening, the fresh seat): ALL NINE ITEMS DONE — the
planning-side owed list is CLEAR. Two commit waves (1–4, then
5–9), each verified + pushed; the sl-0121 seam sweep landed
between them. Remaining from this audit: only §3's six per-seat
pastes (designer hands them over as each seat opens) and the
optional operator manual/quick-card regeneration (on ask).**

1. **DONE (evening seat).** **`docs/08-DECISION_REGISTER.md`** — CORE-25 row still says "the four
   current design pillars remain the only pillars" (SIX since
   2026-08-01, recorded in this same file's deck bullet); CORE-52 row
   carries the old one-zone/one-class slice bill with NO amendment
   (doc 23 governs; CORE-38 got its amendment, CORE-52 didn't); the
   "Do not infer as decided" list still offers as open: exact stat
   values/growth curves, movement caps, the regeneration decision,
   equipment formulas — ALL ruled 2026-08-01 (docs/22); header line
   still says "the interview proceeds to Part II modules alongside the
   Phase A combat laboratory".
2. **DONE (evening seat; docs/10 deliberately untouched — interview
   transcript = marked history).** **Fishing → starhooking
   supersession notes** across the design set:
   `docs/01` §13 (primary — fishing still described as the water-based
   progression system; "starhook" appears nowhere in the GDD), plus
   one-line notes in `docs/02`, `docs/04` line 64, `docs/05` line 114,
   `docs/07`, `docs/08` (CORE-25/48/cross-rules), `docs/09` lines
   53/99/110. Standard note: *"fishing is now STARHOOKING — land
   rifts, the starhook INDEX is law; water fishing (sl-0111) is
   parked."*
3. **DONE (evening seat — rebooted on doc 03 CURRENT + the Slice
   v0.1 era; interview material demoted to a History note).**
   **Root `README.md`** — the front door is two eras stale: "guided
   concept definition / early pre-production", "read
   notes/INTERVIEW_STATE.md first", "next steps are the Part II combat
   modules and/or building the Phase A combat laboratory". Should boot
   on doc 03 CURRENT + name the Slice v0.1 era.
4. **DONE (evening seat).** **`docs/09-SYSTEMS_MAP.md` line 103** — "One small optional pet may
   provide a modest passive benefit" → superseded 2026-07-26 (pets are
   purely cosmetic, no benefit of any kind).
5. **DONE (evening seat — top banners, doc-12 pattern).** **Executed-plan banners** (the doc-12 pattern): `docs/15` §3/§5
   ("nothing lands in the game repo before Gate 1" — b65…b77 all
   intaken) and `docs/17` §4/§5 ("no game-side world_filler code before
   Gate 1" — executed end to end).
6. **DONE (evening seat).** **`docs/13-UI_STYLE_KIT_SPEC.md`** — its 2026-08-01 stamp says "§3's
   out-of-scope list remains correct — those screens are still Part
   II"; inventory/equipment/quest-log/vendor/bank surfaces are now live
   or routed.
7. **DONE (evening seat — new 2026-08-02 top block, era declared over; next-steps menu marked SPENT).** **`notes/INTERVIEW_STATE.md`** — top "ALWAYS CURRENT" block is one
   era behind (SERIAL 14, stat talk "about to answer"); "Next steps"
   still offers "start building the Phase A combat laboratory".
8. **DONE (evening seat — RETIRED, not refreshed: the refresh rule failed two eras running; the live board is doc 03 CURRENT + the deck register; body kept as the era's record; manual/quick card stay as digests, regenerate on ask).** **`notes/operator-guide/OPERATOR_QUEUE_SNAPSHOT.md`** — marked
   PERISHABLE with a refresh rule that has been violated two eras; its
   "Right now" still says to send the sl-0058 WF re-pin paste and run
   the Loop acceptance. Refresh or retire. (The manual + quick card are
   marked digests; regenerate when convenient — the era added laws.)
9. **DONE (evening seat — all nine nits).** **Header/era nits:** `docs/04` line 10, `docs/05` Stage 2 (the
   October vacation lab sprint + retired recruited cycles) and Stage 9,
   `docs/06` header + document map (inventories only docs 01–12 — docs
   13–23 including the ruling authorities are missing), `docs/07`
   vertical-slice scope (DONE — superseded banner added with items
   1–4), `docs/14` §0 "pending amendment" vs its own
   applied status, `docs/18` §2 tail (doc 16's pin table "becomes a
   rendering" — it was abolished), `docs/19` status block vs §1 (the
   loop bar IS ruled; deck card a1zgppav is the open item),
   `notes/2026-08-02-starhook-idea.md` title still says "PARKED" while
   its status block correctly says HISTORY,
   `notes/PROJECT_NOTICE_2026-07-28.md` needs a one-line historical
   banner.

---

## 3. THE PER-SEAT PASTES (ready to copy; each names its repo first)

### → GAME repo (the slice chat)

```
Docs-staleness follow-up from planning's seven-repo audit. Your own sweep
(02920c8) was good but missed these — fix when a seam boundary allows,
they are documentation-only:

1) notes/HANDOFF.md §4 goldens ritual says "next bump is 22" — SERIAL IS
   22 now; next bump is 23 (the file's own header/§0 say 23). A fresh
   agent following §4 would re-use the live SERIAL.
2) notes/HANDOFF.md §4 one-command gate says "79-run battery (41 floor +
   38 cap)" and "~12.5 min" → 43 rows / 83 runs, ~15 min (your §1 has it
   right two sections earlier).
3) notes/HANDOFF.md gotcha 5's current-keys list says "R replay" → R is
   ROD SWAP; replay-save is J (input_map_defaults.gd confirms) — J is
   missing from the list entirely.
4) notes/HANDOFF.md top state + §3 say "NOTHING ROUTED" / "routed and
   waiting: sl-0121 + sl-0122" → the live routed wave is sl-0119, 0120,
   0121, 0122, 0116+0128 (the bag), 0129 (loot bags), 0130 (bank), 0131
   (vendors v1), 0132 (NPC anim desync). Either enumerate or point at
   the planning queue.
5) notes/HANDOFF.md battery-matrix header still stamps "post-S1 …
   SERIAL 21" → post-starhook, SERIAL 22. And §0 says the sync log runs
   "through sl-0114" → it runs past sl-0133 (or drop the number).
6) CLAUDE.md "Weekly GIF cadence (from M3)" says "F9 ring buffer +
   tools/gif.ps1" → the key is G (start/stop) and the recorder is
   start-to-finish since 098a679; F-row keys violate the repo's own
   no-F-row law.
7) notes/AUDIO_CUE_MAP.md telegraph_melee row says melee_patterns = [11]
   → data/audio_cue_map.tres has [11, 22] (Old Tusk's sweep joined at S1
   seam 3); the written map no longer mirrors the machine version it
   claims to document. Same file: "walk-over loot pickups DO exist" →
   retired by the interact era (gold only).
8) Framing alignment: HANDOFF §2/§3 and notes/DESIGNER_QUEUE.md's banner
   invite batched NUMBER TUNING now → planning's way-forward ruling
   (doc 23) defers number tuning to ONE whole-game pass after S4; Green
   days collect SYSTEMS feedback. Also both still list "b65 city walk"
   as live designer work (b65 retired with honor, sl-0098).
9) LOW: README.md's S1 paragraph says "50/50 split" → since sl-0125 the
   ratio is a live-flippable options row; TECH_DEBT_LEDGER #16's
   amendment chain stops at SERIAL 18–21 → SERIAL 22 added fields
   (per-species fish, rod-by-id, ambient rift state, rift catches);
   notes/PACK_INTAKE_RUNBOOK.md says 43/83 "since S1" → since sl-0115.
```

### → ASSEMBLER repo (8-bit-sprite-assembler)

```
Docs-staleness follow-up from planning's seven-repo audit (audited at
f5476a2). Documentation-only:

1) HIGH — README.md "Validate the project", plus HANDOFF.md "Validation
   Evidence" and ROADMAP.md Phase 1 exit criteria: all three present
   `npm run check` as the universal/fresh-checkout validation path, but
   the known open ask (recorded in planning's ecosystem lock) is that it
   CANNOT pass from a clean clone — it reads untracked review drafts. No
   doc acknowledges this. Add the caveat (and, if you want it closed:
   skip-missing-review-drafts is the recorded fix direction).
2) HANDOFF.md "Current Boss Review State" / "Frozen Boundaries" + README
   boss sections: the designer lifted the game-side hold today (planning
   sl-0122) — the game now wires boss:goblin-war-crown (King Grubb
   rebind) and deals the rest per chapter. Your docs still hold that
   corpus as an unaccepted candidate and are silent on the pack's
   game-side status. Reconcile with one line: game-side wiring consumes
   the SHIPPED pack bytes; assembler visual acceptance is a separate
   lane that stays open.
3) asset-pack/README.md documents the legacy 12-column / 1152x384
   contract as THE layout, with no "deliberate legacy fixture baseline"
   label and no pointer to the current 20-column / 480x96 public actor
   contract — a consumer reading only that file gets the wrong contract.
4) WEAPON_READABILITY_PLAN.md "Deferred Continuation": says the default
   view still composes modular combat effects (they are Off by default
   and forced Off at start) and names SHADE_RENDERING_PLAN as the active
   next lane (shade completed 2026-07-26; the active lane is
   ENEMY_EXPANSION_PLAN). Its review instructions still say "all 12
   animation frames" / 3,600 cases → 20 columns / 6,000.
5) EQUIPMENT_OUTLINE_ASSESSMENT.md L18 and EQUIPMENT_READABILITY_PLAN.md
   L216 call 7,680 shield / 3,600 weapon / 11,280 combined the CURRENT
   gate → current is 12,800 shield / 6,000 weapon; relabel those as
   historical 12-column totals. Same for SHADE_RENDERING_PLAN.md's
   present-tense "implemented format versions … preset v11 / Kit-Pack
   v11" (now v12 / packs v3) and TRANSPARENT_TILE_REPAIR_PLAN.md's
   "next planned feature is SHADE_RENDERING_PLAN".
6) Also owed from the designer, not a doc fix: ENEMY_EXPANSION_PLAN.md
   correctly flags that the source intake text ended mid-sentence
   ("Families that may wor…") — the tail is owed before those
   qualifications become requirements.
```

*(Accounting 2026-08-02 ~22:20, corrected ~22:55: f5476a2 — the
commit this paste was audited AT — hit main at 15:07 local (events
API; the earlier "pushed 22:11 by a dying session" read was wrong)
and is the BASE of a LIVE enemy-expansion branch lane: codex/en-e02
@ 9836a31, EN-F00 → EN-E01 → EN-E02 Idle approved, 12 ahead / 0
behind main. Items 1–6 still owed AS WRITTEN AGAINST MAIN; the
branch rewrites HANDOFF/README/ARCHITECTURE and may have fixed some
organically — re-check when the lane merges. The seat is OPEN and
LIVE — the paste can drop into it any time; full story: the session
file's THE ENEMY-EXPANSION LANE SURFACES section.)*

### → TILEFORGE repo

```
Docs-staleness follow-up from planning's seven-repo audit (audited at
master b906797). Documentation-only:

1) HIGH — review/road-extension-candidates/README.md and
   review/road-transition-candidates/README.md still say "AWAITING THE
   DESIGNER'S JUDGEMENT" / "NOTHING is in the engine yet" with live
   resume loops. Both were judged and SHIPPED 2026-07-31: gravelway/
   flagway/corduroy/threshold at c18a52d, the roadjoint family (84
   codes) at 9b8b2a2, the sl-0054 arc CLOSED (do not reopen unbidden),
   and the road-slab question closed too. Stamp both CLOSED/graduated —
   that also makes HANDOFF's claim "their READMEs say what graduated"
   true.
2) HANDOFF.md + exports/README.md still frame the WorldForge re-pin as
   pending ("supersedes that pin when their look-ruling round settles",
   "sl-0058 APPENDED only") → the re-pin EXECUTED 2026-07-31; WF, b76/
   b77, and the game all run dusk-9b8b2a2. b77 is the current world.
3) HANDOFF.md environment block: `npm run validate` expectation 31,463 →
   31,759 since the roadjoint family (an agent would read the correct
   result as drift). Same file's publish-gate bullet says the release
   step is "UNEXERCISED — no delivery has shipped through it yet" → two
   gated cuts shipped as releases and were consumed downstream.
4) HANDOFF.md's "W6 (the TileForge adapter) is IN PROGRESS" block
   (dated 2026-07-26, unmarked) and the "the user's sprite forge starts
   after REF3 promotion" claims → WF is at behavior 77; the actor tool
   is the 8-bit-sprite-assembler (supersedes Sprite Forge) and has
   already shipped three packs to the game. Mark superseded.
5) LOW: three "80 families" headers (README intro, DOCS §3,
   exports/README) → 86 families / 31,759 tiles; ROADMAP's "Wave R
   (ACTIVE)" / "runs now" / "first unchecked box: Q0" markers → all
   waves closed (real unchecked: REF3 promotion, Unity importer);
   review/audit-2026-07/report.md "every item awaits a user ruling" →
   all 47 closed by Wave A.
```

### → WORLDFORGE repo

```
Docs-staleness follow-up from planning's seven-repo audit (audited at
main 5caac4c). Documentation-only:

1) HIGH — docs/GAME_INTEGRATION_PLAN.md §1 says "no game consumes a
   WorldForge world yet" and §5 Phase 4 says rendering/consumption is
   "deferred post-Gate-1" → the game consumes AND renders WorldForge
   worlds now: b65 intaken 2026-07-30, b77 intaken 2026-08-01 and it is
   the dusk overworld in play (Slice v0.1, canopy render proven on
   screen). The doc is otherwise maintained through b76, which makes
   that stale phase row read as live status.
2) README.md project status says "Current state (2026-07-31): behavior
   76" → behavior 77; b77 is released AND game-intaken (b76 archive).
3) HANDOFF.md pointer open item (2) "world_filler re-pin (sl-0041 in
   flight)" → executed 2026-08-01 as sl-0068 (wf c431143, b77 adopted,
   188 tests green).
4) HANDOFF.md §1 still says "THE SCENERY LOOP IS THE ACTIVE ARC" with
   "batch 3 candidates: harbor row / chicken run+vineyard / logging
   camp / battlefield" → batches 3–9 shipped (b63–b70) and §6 correctly
   says the loop is PAUSED at eleven ratified compositions; an agent
   could start already-shipped work. Same section: 257 tests → 260, and
   "pushed through the b76 handoff commit" → through b77 + the park
   commit.
5) HANDOFF.md §6 says the coastal dusk pack is "READY FOR HANDOVER" →
   delivered and intaken 2026-07-30 (game 5cb0e3b); its upstream asks
   "improved road-band art" and "optional live ruined-road band" are
   both satisfied (the road arc shipped; ruinedroad is first-class since
   sl-0029). §2's "PENDING VERDICT (round 11): the-eight-holds" label
   contradicts its own record of rounds 12–19 ruled positive.
   docs/ROADMAP.md's only status line is frozen at 2026-07-26 ("W7/W8
   functionally complete … remaining: windowed playthrough, polish
   round, formal visual approval") while README sends every agent
   there → W0–W9 closed, production era.
6) LOW: docs/SCENERY_COMPOSITIONS.md §1 lists cookfire as remaining
   (rostered by b69) and §4's walls+gates question (answered by b62 via
   settlementStyle.cityWalls); docs/ZONE_COMPOSITION_ASSESSMENT.md
   "arc open" → shipped (behaviors 40–46), only zone-crop preview
   tooling remains.
```

### → WORLD_FILLER repo

```
Docs-staleness follow-up from planning's seven-repo audit (audited at
main 7eadf30). Documentation-only — the whole repo's doc set still
describes the pre-export era:

1) HIGH — HANDOFF.md title says "dusk rehearsal rounds 1–5 LIVE at
   behavior 18" → its own §1j records rounds to R13 at behavior 24 with
   the export EXECUTED (release c0bf28638648).
2) HIGH — HANDOFF.md §0 "Next milestone" (direct → gated export → the
   game consumes AS REFERENCE ONLY → feel verdict → importer follows),
   README.md's status chronicle ending, and docs/ROADMAP.md's status
   block all describe steps that are ALL COMPLETE: exported, intaken
   (planning sl-0094), feel verdict PASSED (sl-0099), and the game-side
   importer BUILT and live since S0 (planning docs/20 arc complete;
   sl-0041 resolved). ROADMAP's "no game-repo changes made" is now
   false.
3) HIGH — HANDOFF.md §2 + docs/IMPORTER_READINESS.md still carry the
   hold "PREPARED 2026-07-29, awaiting the user's plan — make NO
   game-repo changes" → spent; the importer exists. Mark
   IMPORTER_READINESS historical.
4) MED — HANDOFF.md §6 versions: "behavior 18 · plan 7, placement 6,
   territory 4, validate 3" → behavior 24 · plan 9 / placement 7 /
   territory 5 / validate 4 (per your own §1j and the shipped
   manifest). Test count "193 green (191 clean clone)" is frozen at the
   R5 point — R6–R13 added units.
5) MED — the actual next milestone is recorded nowhere: the PUPPETEER
   directed round is STAGED but NOT FIRED (boss #9's site inside the
   ruined-city box, recipe-locked, gated export = the next content-pack
   version; the game re-intakes before S4 Snow). The paste is with the
   designer.
6) LOW — docs/ROADMAP.md standing risk 5 (segmentation "must become
   walkability-aware") → resolved 2026-07-30 (sl-0026 + the moss rung);
   docs/IMPORTER_READINESS §5.2 "dusk@b72, which the game has already
   intaken" → the game pairs b77; VISION/ARCHITECTURE "Draft, planning
   stage" statuses and ARCHITECTURE's "Godot consumption … none of this
   is built" note.
   (Planning verified the old verifier-fix queue item is DONE, not
   dropped: defects 1–3 were fixed 2026-07-28 with tamper batteries in
   both lanes before the importer was built. Nothing owed there.)
```

### → RESONANCE FORGE repo (music_soundeffects)

```
Docs-staleness follow-up from planning's seven-repo audit (audited at
main 435b7e6). The root cause is structural, not clerical:

1) THE ONE ACT THAT FIXES MOST OF IT — the queued music-seam merge.
   codex/approved-audio-export (5 commits, unmerged) already carries the
   v1 release record, G7 CLOSED (G7_SAFE_EXPORT_APPROVAL.md), the
   publish gate COMMITTED, and the pickups / ui_feedback /
   boss_telegraphs APPROVALS. Merge it to main at that session's own
   gates (npm test in apps/desktop + cargo test -p audio-core --lib) and
   most findings below resolve themselves.
2) HIGH — HANDOFF.md "Complete Godot audio export" still names the
   pre-release local zip (SHA AB5B8CEF…) as the delivered artifact →
   what shipped and was game-intaken is the RELEASE
   resonance-forge-godot-audio-v1-23a6c659199b, zip F786126B… (release
   digest = planning's intake record). Verifying a delivery against
   main's hash fails wrongly. Same file records nothing about the
   package becoming a release or being INTAKEN by the game (planning
   sl-0021/0022; consumed through the game's own cue map — the RF
   autoload is deliberately NOT enabled).
3) HIGH — HANDOFF.md "Suggested next steps" #2/#3 still say pickups /
   ui_feedback / boss_telegraphs "remain draft_unreviewed until explicit
   user approval" and to continue the perceptual-warnings slice → all
   approved 2026-07-30 and the slice landed (on the unmerged branch).
   Following main re-spends a designer listening session. Replace with
   the real open items: the Hell Engine V2 exact-file listen, the seam
   merge itself, Phase 8 status.
4) MED — README.md "conservative perceptual-similarity warnings remain
   before G7 can close" and the two Phase-7 checkpoints' "G7 remains
   open" → G7 is closed on the branch;
   docs/checkpoints/PHASE7_COMPLETE_GODOT_AUDIO_EXPORT.md's "listening
   approval still pending … do not promote" → landed.
5) MED/LOW — CLAUDE.md's ecosystem pointer says "(future audio packs for
   the game, Phase 6 importer unbuilt)" → the v1 pack shipped and the
   game consumes it, middleware-less by ruling; MASTER_PLAN.md still
   says "Draft for user review, Version 0.1" → it has been the enforced
   product contract since 2026-07-27.
6) HYGIENE FLAG (not a doc): the local clone sits on a local-only
   branch with ~19 modified files and an unpushed V4–V10 hell-engine
   branch stack. Ecosystem rule 6 makes unpushed work on a dev machine
   issue-class — push or archive-tag when that session is done.
```
