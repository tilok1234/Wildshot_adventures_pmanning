# Agent Sync Protocol — cross-repo events, logging homes, and the Sync Log

**Doc:** 18-AGENT_SYNC_PROTOCOL
**Status:** **DRAFT, REVIEWED — pending Deck ratification.** Drafted
2026-07-29 on designer direction (phone chat); independently re-derived
and agreed point-for-point in the 2026-07-29 remote design session
(back-and-forth, designer-approved direction — see
`notes/sessions/2026-07-29-remote-repo-structure-planning.md` §2); its
three requested edits are folded in (§0 session recipe as page 1, the
janitor exception, the handoff hook), plus the 2026-07-30 janitor
session's live evidence (§0.4, §12). Ratification payload:
`tools/decision_deck_items_2026-07-30.json`. Until the Deck accepts,
this doc changes NOTHING — doc 16's rules stand as written.
**Authority:** extends `docs/16-ECOSYSTEM_MAP.md`; on any conflict, doc 16
wins until this doc is accepted and doc 16 is amended to reference it.

---

## 0. Which repo do I open? (the session recipe — page 1 on purpose)

1. **Open the repo where the changes will land. One repo per session.**
2. The planning repo only needs to exist on disk (readable by path); it
   does not need to be "open". Two exceptions:
   - **Game sessions keep the game+planning pair** — code lands in the
     game repo, decisions/records land in planning.
   - **Planning/decision sessions start in the planning repo.**
3. Cross-repo needs become recorded asks or ready-to-paste prompts for
   that repo's own agent — never work done out-of-lane (the lane rule,
   game CLAUDE.md Authority section, now ecosystem-wide).
4. **Exception — the janitor session (git hygiene only).** A
   planning-rooted session MAY do cross-repo git housekeeping: default
   branches, fast-forwards, merging finished work to main, deleting
   fully-merged husks. Guardrails, all mandatory (all exercised live
   2026-07-30):
   - **(a) Archive tags first:** every branch tip slated for merge or
     delete gets an `archive/<branch>` tag pushed BEFORE anything moves.
     Tags make every later step reversible — moving or deleting a
     branch name never destroys a tagged snapshot.
   - **(b) Gates before pushes:** that repo's own test/validate gates
     run green before any push. Not green — or not runnable — means no
     push without the designer's explicit word.
   - **(c) Mechanical only:** merge conflicts, verdict salvage, and
     "which line wins" questions STOP and escalate to the designer or
     that repo's own session.
   - **(d) Live-session check:** before touching any branch, fetch and
     look at tip age + running agent processes. A branch another
     session is actively working is hands-off (this check caught the
     music repo mid-commit, 6 minutes fresh, on 2026-07-29).
   - **(e) Destructive ref operations are designer-clicked:** branch
     deletion and force-pushes are executed by the designer (agent
     stages the exact command), never by the agent. The permission
     layer enforces this anyway; the protocol adopts it as design.

## 1. Why this exists

The 2026-07-29 seven-repo review found five sync failures, none of them
in the pack-contract layer (which held perfectly), all of them in the
human-mediated layer between repos:

1. The game consumes an assembler pack whose sourceCommit (`b7eae05f`)
   exists on no branch of the assembler's GitHub remote.
2. The world_filler local clone sat ~12 commits behind the ruled
   mainline, and the repo's GitHub default branch is an obsolete lane.
3. Doc 16's pinned-version snapshot table had already drifted from
   reality within a day.
4. A newer WorldForge dusk export sat finished but unhanded-over, with
   delivery depending on someone remembering.
5. WorldForge's recorded upstream asks to TileForge were not visible
   anywhere in TileForge's own queue.

Common root: everything machine-checked at a pack boundary works;
everything that relies on a human carrying state between repos silently
rots. This protocol makes every cross-repo event **machine-recorded,
once, in one known place**, and gives agents fixed rituals so the
recording is not optional diligence but part of the job.

## 2. Where information lives (one home per kind — never duplicate)

| Kind of information | The ONE home | Written by |
|---|---|---|
| Design decisions / rulings / sign-offs | Decision Deck register (`planning tools/decision_deck_register.json`) | designer (deck taps), swept by sessions |
| Daily narrative (what happened and why) | `planning notes/sessions/<date>.md` | the session's agent |
| Per-repo current state ("where am I") | that repo's `HANDOFF.md` | that repo's agent, at session end (doc 16 rule 4) |
| **Cross-repo events** (deliveries, intakes, asks, pin changes, incidents) | **`planning tools/sync_log.json`** (NEW — §8) | any agent, at the moment the event happens |
| Version pins (who consumes what, exactly) | **`planning tools/ecosystem.lock.json`** (NEW — §10) | the consuming repo's agent, during intake |
| Tech debt | the owning repo's ledger (game: `notes/TECH_DEBT_LEDGER.md`) | that repo's agent |
| Mechanical evidence (proofs, batteries, reports) | the producing repo's `reports/` | tooling; never re-homed, only linked |

Cross-references are by path/id, never by copying content. Doc 16's
prose pin table becomes a *rendering* of the lock file once this doc is
accepted (regenerate, don't hand-edit).

## 3. Session rituals (every agent, every repo)

**Session start:**
1. Read the repo's contract docs (CLAUDE.md / AGENTS.md / HANDOFF.md) —
   existing rule, unchanged.
2. Verify the checkout is on the repo's **ruled mainline** (or the
   session's designated branch) and is **not behind its remote**
   (`git fetch` + `git status -sb`). A stale or wrong-lane checkout is
   a STOP: log an `incident` entry, fix or flag, never build on it.
3. Skim `sync_log.json` for open entries touching this repo (unresolved
   incidents, asks, deliveries awaiting intake).
4. If this repo consumes packs: confirm the lock file's entries for
   those packs still describe what's on disk.

**Session end:**
1. Update the repo's HANDOFF.md (existing rule, unchanged).
2. **The handoff hook:** writing the handoff IS the moment to ask "does
   this session owe the logbook a line?" — the two habits are one
   ritual. Append `sync_log.json` entries for every cross-repo event
   this session caused (see §8 event types). No event, no entry — the
   log is events, not diary. Every repo's contract doc carries this
   one-line rule so the hook survives account switches.
3. Commit and push; then **verify the push landed**
   (`git status -sb` shows the branch level with its remote). The
   assembler drift happened because "pushed" was assumed, not checked.
4. Planning-side sessions: session record as usual.

## 4. Delivery protocol (producer repos: tileforge, WorldForge, world_filler, assembler, Resonance Forge)

1. **Publish gate:** an export/pack build REFUSES to run if the working
   tree is dirty or HEAD is not present on the remote
   (`git status --porcelain` empty; `git branch -r --contains HEAD`
   non-empty). This is the check that would have caught incident 1 at
   the source. Each producer's exporter grows this guard (its own
   repo's work, per the lane rule — recorded as asks, §6).
2. The pack manifest carries `sourceCommit` + content hashes (already
   standard in WorldForge/tileforge; assembler and Resonance Forge
   adopt it when their exporters next change).
3. Log a `delivery` entry in the sync log: artifact id, sourceCommit,
   hash, where the consumer should pick it up.
4. *(Tier 2, once ruled)* Upload the pack zip as a **GitHub release
   asset** tagged with the artifact id — the registry replaces
   desktop-zip/chat transport; consumers fetch by tag and verify the
   hash. Until ruled, the current directory-drop transport stands.

## 5. Intake protocol (consumer repos — today: the game)

1. Validate the drop with the repo's existing intake machinery
   (validators + battery + runbook — unchanged; they are the strength
   of the current system).
2. Verify the manifest's `sourceCommit`/hash against the delivery's
   sync-log entry. Mismatch = `incident` entry + STOP; never intake an
   artifact whose origin can't be confirmed.
3. Update `ecosystem.lock.json`'s pin for this artifact.
4. Log an `intake` entry referencing the delivery entry's id.

A delivery entry with no later intake entry for the same artifact is,
by definition, **waiting** — the log app surfaces these automatically,
which retires "someone remembers to carry the directory over".

## 6. Ask protocol (upstream needs)

The lane rule stands: no repo executes another repo's work. What
changes is where the ask *lives*:

1. Log an `ask_opened` entry (asking repo, target repo, plain-language
   ask). This is the mandatory minimum from day one of this protocol.
2. *(Once ruled)* Also open a GitHub issue on the **target** repo,
   labeled `upstream-ask` — so the receiving repo's next session sees
   it without being told. The sync-log entry links the issue.
3. Resolution (delivered, declined, superseded) logs `ask_resolved`
   referencing the opening entry.

## 7. Incident protocol

Anything that violates doc 16's cross-repo rules or this protocol —
drift discovered, artifact from an unverifiable commit, stale clone,
wrong default branch, hand-edited export — gets an `incident` entry at
discovery time, `status: "open"`. Review sessions sweep open incidents
first. Resolution flips `status` to `resolved` with a note. Incidents
are facts, not blame; the log exists so the third repetition of a
failure mode is impossible, not embarrassing.

## 8. The Sync Log register (`tools/sync_log.json`)

Append-only JSON, committed like the deck register. Schema:

```json
{
  "formatVersion": 1,
  "entries": [
    {
      "id": "sl-0007",
      "ts": "2026-07-29T15:40:00Z",
      "type": "delivery | intake | ask_opened | ask_resolved | pin_change | incident | handoff | ruling | note",
      "repo": "worldforge",
      "target": "game",
      "title": "plain-language one-liner (designer reads this in the app)",
      "detail": "optional longer context",
      "artifact": { "id": "small-cold-coastal-pack-dusk@b63", "sourceCommit": "…", "hash": "…" },
      "refs": ["sl-0004", "notes/sessions/2026-07-29.md", "issue: tileforge#12"],
      "status": "open | resolved",
      "by": "agent | designer"
    }
  ]
}
```

Rules: ids sequential and never reused; `title` obeys the standing
plain-language rule (zero repo jargon — the designer reads these);
`artifact` required on delivery/intake/pin_change; `status` required on
incident/ask entries; entries are never edited except to flip `status`
and append to `refs`/`detail`. `ruling` entries only *point at* deck
register items — the deck stays the decision authority.

## 9. The log program (`tools/sync_log.html`)

Single-file offline app, same conventions as the Decision Deck: open in
a browser, no install, localStorage persistence, IMPORT/EXPORT JSON,
paste-from-AI append. It is a **viewer and triage surface**, not a
second source of truth — the committed JSON is the record; the app's
import/export is the sync step.

Views: a **status board** (deliveries waiting for intake, open
incidents, open asks — computed from the entries, nothing hand-kept), a
filterable **timeline** (by repo, type, search), and one designer
action: mark an incident/ask **resolved** with a note, then export the
JSON for commit.

## 10. The lock file (`tools/ecosystem.lock.json`)

Machine-readable successor to doc 16's prose snapshot table: per repo,
the ruled mainline branch; per consumed artifact, exactly what the
consumer currently holds (id, sourceCommit, hash, intake date, sync-log
ref). Written only during intakes (§5) or mainline rulings. Any tool or
agent that wants to know "what should be where" reads this file; any
mismatch between the lock and reality is an automatic `incident`.

## 11. What needs a ruling before any of this binds

One deck card per line (drafted for paste-in when asked):

1. **Adopt the protocol** (this doc; doc 16 gains a pointer + rule 7:
   "GitHub default branch = ruled mainline, every repo").
2. **Publish gates** in the four producer exporters (asks to each repo).
3. ~~**Fix world_filler's default branch**~~ ✅ DONE 2026-07-30 (janitor
   session: `main` created, default flipped, then re-ruled to the
   designer's approval line).
4. *(Tier 2)* **GitHub releases as pack transport**, replacing
   directory/zip drops.
5. *(Tier 2)* **Drift check cadence** — a script or scheduled agent
   comparing lock vs latest deliveries, report-only.
6. **Talk-before-build rule** (from the 2026-07-29 phone-break lesson,
   proposed by the designer's own callout): for new protocol/tool/
   system ideas, the design conversation happens in chat FIRST; agents
   draft nothing until the designer has walked through the idea and
   said build.

Ratification payload: `tools/decision_deck_items_2026-07-30.json`
(cards for 1, 2, 4, 5, 6 — item 3 already done).
Until ruled: agents MAY write sync-log entries (recording facts harms
nothing and the seed log already exists); everything else waits.

## 12. Repo hygiene baseline (added 2026-07-30, janitor evidence)

- **Hash-pinned repos ship `.gitattributes` from day one.** Any repo
  that byte-hashes text artifacts (fixtures, goldens, packs) must pin
  LF line endings — Windows checkouts with `autocrlf=true` otherwise
  rewrite files at checkout and fail hash-verified tests falsely
  (world_filler: ~30 false fails, diagnosed and evidenced 2026-07-30;
  byte-exact re-checkout took both lines to green/one-benign-fail).
- **Self-checks must pass from a clean clone.** A check that reads
  untracked local artifacts (assembler review drafts) can never gate a
  fresh checkout and silently stops gating anything.
- **One living branch per repo** (plus the planning repo's standing-
  branch exception); GitHub default = ruled mainline (doc 16 rule 7
  once this doc is accepted). Finished side branches merge at their own
  session's seam and die; the 2026-07-30 sweep is the reference state.
