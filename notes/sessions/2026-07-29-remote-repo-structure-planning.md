# HANDOFF — remote planning session 2026-07-29 (repo structure + branch audit)

**Written for the designer's PC session picking up the same evening.**
This was a remote, PLANNING-ONLY session on branch
`claude/project-docs-gandoff-review-kia64i`. **Nothing was changed in any
repo** — the only artifact is this file. Everything below is either an
agreed plan (designer + assistant, full back-and-forth) or a read-only
finding verified against the GitHub remotes this session.

---

## 1. What this session was

The designer restarted the repo-organization conversation that a
2026-07-29 phone-break session began (that session's output survives —
see §3, the single most important recovery item). This time the design
was done the right way: back and forth, plan before build. The designer
explicitly ruled: **nothing gets built until planned properly.**

## 2. The agreed design (planning-level, pending Deck ratification)

Designer-approved direction in this chat, in plain terms:

1. **Keep all 7 repos exactly as they are.** No merging, no
   restructuring. The pack contract layer (frozen packs + validating
   importers + deliberate pins) is the proven strength; the failures
   are all in the human transport layer between repos.
2. **One shared logbook** ("delivery ledger" / sync log) in the
   planning repo. One line per cross-repo event: what shipped, from
   which repo + commit, when, content fingerprint (hash), who intook it
   and whether its checks passed. This file IS how the repos "know
   about each other."
3. **Passport rule for all imports** — no pack enters a repo without a
   small provenance file (source repo, source commit, date, version,
   hash). Receiving repo validates (existing machinery), stores the
   passport, writes the logbook line.
4. **Producer keeps the original** — every shipped pack becomes a
   tagged GitHub release on the producer repo. Consumers keep passport
   + hash, not fat binaries accumulating in git history.
5. **Logbook writing hooks into the existing end-of-session handoff
   habit** (the designer always asks for a handoff — the rule "handoff
   = check if a logbook line is owed" gets written into every repo's
   agent-facing contract docs). Writing stays with the agent
   (machines can't write meaningful lines); **forgetting** gets caught
   mechanically: (a) importers refuse packs without passports,
   (b) a check script compares packs-on-disk vs logbook entries —
   gates read exit codes, not prose.
6. **The overview program comes later, data first** — run the logbook
   as a plain JSON file; if it earns its keep, build a Deck-style
   offline HTML viewer over it. Do not build the tool before the data
   habit exists.
7. **Session protocol ("which repo do I open?"):** open the repo where
   the changes will land, one repo per session. Planning repo needs
   only to exist on disk (readable by path), not be "open" — except:
   game sessions keep the game+planning pair (decisions recorded in
   planning), and planning/decision sessions start in the planning
   repo. Cross-repo needs become asks / ready-to-paste prompts, never
   work done out-of-lane. This recipe should be page 1 of doc 18.
8. **NEW exception to record in doc 18: the "janitor session"** — a
   planning-rooted session may perform cross-repo **git hygiene only**
   (default branches, fast-forwards, merging finished work to main,
   deleting fully-merged husks). Guardrails: (a) every merge runs THAT
   repo's own test/validate gates before any push — not green, no
   push; (b) mechanical only — any judgment call (merge conflicts,
   verdict salvage) STOPS and escalates to the designer or that repo's
   own session. The lane rule's spirit (no content/design decisions
   for another repo) stands untouched.

## 3. CRITICAL RECOVERY: draft doc 18 already exists on a stranded branch

Planning repo branch **`claude/progress-review-rd22i8`** (2 commits
ahead of the standing branch, 0 behind):

- `65d85fd` — **`docs/18-AGENT_SYNC_PROTOCOL.md` (DRAFT)** + tools
  (`sync_log.json`/`.html`, `ecosystem.lock.json`)
- `5b02dbb` — session addendum 17 (the phone-break session record:
  five cross-repo sync failures found, the rushed-build lesson, the
  broken chat)

That draft and this session's independently-derived design **match
almost point for point** (sync log = logbook; delivery/intake protocol
= passport; one-home-per-information-kind table; session rituals;
releases as transport tier-2). Two draft ideas this session endorses
adopting: **exporters refuse to build from a dirty tree or unpushed
HEAD** (would have prevented the assembler scare at the source), and
the **ecosystem lock file** (machine-readable pin registry replacing
doc 16's hand-edited prose table). Addendum 17 records honestly that
the draft was built without back-and-forth and the designer called it
out; this session WAS that back-and-forth, and the conclusions agree.

**First action on the PC: merge/pull `claude/progress-review-rd22i8`
into the standing branch** (`claude/questionnaire-note-taking-9vl2sl`),
then review doc 18 against §2 above (small edits: add the §2.7 session
recipe as page 1, the §2.8 janitor exception, the handoff-hook rule),
then ratify via the Decision Deck.

## 4. Branch audit — all 7 repos, verified against GitHub this session

### Clean (nothing to do)
- **Wildshot-Adventures** — `main` only, default. ✅
- **tileforge** — `master` only, default. ✅

### world_filler — the confirmed mess (designer's suspicion was right)
- **No `main` exists.** GitHub default = `claude/world-director-planning-vvvudl`
  (obsolete: ends at the pre-resolution freeze salvage `ddcb22c`).
- Four branches, all forking at `ddcb22c`, three sessions unaware of
  each other:
  - `claude/freeze-review-resolution-tf6bkf` (`d8bdeef`) — **the RULED
    mainline** (freeze resolved, format 1 final, importer workflow,
    Director Studio, F9 A+B, ecosystem pointer).
  - `claude/project-docs-handoff-8vdssn` — a **duplicate, independent
    freeze-review resolution** (`f9a464d` "fix all 15 confirmed
    defects") + `b9cb315` **"F3 verdict adoption: area-share danger
    banding (behavior 6, plan rules 2)"** — a designer verdict living
    only on this orphan.
  - `claude/world-filler-repo-focus-9fmr60` — third parallel line
    (5 own commits: analysis-2 region subdivision, danger render,
    walkable-cliffs gap note, **"Bands verdict recorded: behavior-12
    danger map approved"** — another orphaned designer verdict,
    "first arc closed / game-side importer prepared (docs only)").
- **Fix:** create real `main` from `tf6bkf`, set it as GitHub default;
  then VERDICT SALVAGE (designer judges, one-liners): show the diffs of
  the two orphans vs main, carry over what is real (at minimum the two
  recorded verdicts need a decision: adopt into the mainline record or
  mark superseded), then archive/delete the orphans. Note the two
  orphan lines numbered their behaviors independently (behavior 6 vs
  behavior 12 vs mainline numbering) — reconcile by content, not number.
- Stale-doc warning: the HANDOFF.md on the old default still says the
  freeze is provisional — misleads every fresh clone (it misled this
  session's own container checkout).

### 8-bit-sprite-assembler — main frozen in mid-July, real work on side branches
- `main` is stale (2026-07-17 state, 41 families).
- `codex/form-shading`: **121 commits ahead of main — contains
  `b7eae05f`**, the exact commit the game's consumed actor pack (57
  fam/202 var) was built from, plus the 48×48 boss direction pilots.
  **So the pack source IS on GitHub — not lost** (the phone-session's
  "on no branch" finding is outdated/wrong as of this check).
- Also ahead of main: `codex/optional-sprite-outlines` (52),
  `codex/weapon-readability-bow` (40), `codex/windows-release` (41).
- **Fix:** merge codex branches into `main` — but these four lines may
  conflict with each other, and choosing whose art/behavior wins is NOT
  janitor work. Expect this to possibly become its own assembler
  session; fine if it doesn't finish tonight. Priority: get
  `form-shading` (the pack-source line) into main first.

### music_soundeffects — minor
- `main` healthy + default. `codex/g3-g5-production` is **3 commits
  ahead** (G3–G5 production work). Merge (run `npm test` in
  apps/desktop + `cargo test -p audio-core --lib` before push), delete.

### WorldForge — husks only
- `main` healthy + default.
- `claude/world-forge-mobile-eiqrr3`: 0 ahead — delete.
- `claude/worldforge-game-review-yzllne`: 0 ahead (absorbed at
  `ae924e3`, HANDOFF says never cherry-pick again) — delete.
- `claude/project-docs-review-il5lzb`: shows 24 "ahead" but the content
  (behaviors 36+ / game-integration phases) was re-landed into main via
  the mobile-arc merge — different hashes, same work. One-glance
  confirm nothing unique remains, then delete.

### Planning repo — one live branch, two husks (+ this session's)
- Standing branch `claude/questionnaire-note-taking-9vl2sl` is default.
  Correct per the one-branch rule (no main by design).
- `claude/progress-review-rd22i8`: **2 ahead — RECOVER (§3), do not
  delete until merged.**
- `claude/repo-assessment-planning-u6fkjy`: 0 ahead — delete.
- `claude/project-docs-review-il5lzb`: 20 ahead / 50 behind, but the
  content (doc 15 arc) already lives on the standing branch — confirm,
  then delete.
- `claude/project-docs-gandoff-review-kia64i` (THIS session): carries
  only this handoff file. Merge it in, then it too becomes a husk.

## 5. Tonight's work order (agreed with the designer, cheapest→riskiest)

Run as ONE janitor session from the planning repo on the PC, guardrails
per §2.8. Log hours (PROD-01).

1. Planning: merge `progress-review-rd22i8` (recovers doc 18) and this
   branch (recovers this handoff) into the standing branch.
2. music: merge `codex/g3-g5-production` → main (gates first), delete.
3. WorldForge + planning: confirm-and-delete the husks listed above.
4. world_filler: create `main` from `tf6bkf`, flip GitHub default,
   then the verdict salvage WITH the designer (their calls, one-liners),
   then archive/delete orphans, de-stale its HANDOFF.md.
5. assembler: merge `codex/form-shading` → main first (it has the pack
   source); attempt the other three; STOP on real conflicts and let it
   become its own session if needed.
6. Then (or next session): doc 18 review + Deck ratification per §3.

## 6. Open decisions for the Deck (plain-language cards)

1. Accept doc 18 (the rulebook for how repos share info) after the §3
   review — includes the logbook, the passport rule, the session
   recipe, the janitor exception.
2. Packs as GitHub releases (the "producer keeps the original" rule) —
   the draft doc has it as tier-2; decide now-or-later.
3. Exporters refusing dirty/unpushed builds — adopt as a standing rule
   for all producer repos (each implements in its own lane as asks).
4. world_filler orphan verdicts (danger-band approvals) — adopt into
   the mainline record or mark superseded (needed during step 4 above).

## 7. Standing designer context (unchanged, for whoever reads this cold)

The wider project state is NOT this session's subject: game M0–M7
closed, M8 engineering exhausted, Gate 1 unblocked on designer-side
items. See the game repo CLAUDE.md milestone block and
`notes/HANDOFF.md` (2026-07-29 marathon seam) — still accurate.
This session changed none of it.
