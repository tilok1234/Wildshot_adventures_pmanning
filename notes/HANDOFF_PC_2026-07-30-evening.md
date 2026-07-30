# PC Handoff — 2026-07-30 evening (designer home, running Claude Code from terminal)

**Who this is for:** the designer's first PC terminal session(s)
tonight, and any agent they open. Read top to bottom; it's ordered.
Everything referenced was pushed to planning branch
`claude/operator-protocols-guidelines-ruyu4q` by the forklift session.

---

## 0. Before anything (designer, 2 minutes)

1. `tools/hourslog.ps1 start` — the evening block is project work.
2. In the planning repo:
   ```
   git fetch origin
   git checkout claude/questionnaire-note-taking-9vl2sl
   git merge --ff-only origin/claude/operator-protocols-guidelines-ruyu4q
   git push
   ```
   Clean fast-forward — the task branch is mainline + 3 commits, all
   new files, verified 0 behind. If `--ff-only` refuses, a mainline
   push landed after 23:00 UTC-ish; STOP and let a planning session
   reconcile (don't force anything).
3. Optional but worth it: today's session record is
   `notes/sessions/2026-07-30-worldshape-forklift.md` — the world
   got its shape back today; five minutes of reading pays for itself.

## 1. Tonight's order (from the refreshed queue snapshot §T)

1. **Game session → b72 intake** (closes sl-0035, open since this
   morning's "off to work mid-intake"). Standard runbook
   (`game notes/PACK_INTAKE_RUNBOOK.md`); b72 supersedes b71 as the
   target; release-transport verification as always. Expect
   flood/porosity re-pins per per-drop doctrine.
2. **b72 country-road look** — WF-side verdict pending; big screen;
   Tier 1 taste ruling ("country roads as band lines").
3. **Decision Deck:** PASTE FROM AI →
   `tools/decision_deck_items_2026-07-30-worldshape.json` — 5 cards,
   all confirmation taps of the designer's own forklift calls.
4. **Next WorldForge session:** paste the W-13 prop-walkability ask
   (text in the session record §3 — three walkability classes,
   convert-don't-delete). THAT session logs the `ask_opened` entry
   (the forklift session deliberately did not allocate a sync-log id
   — collision avoidance; cite the record file in refs).
5. **If energy:** sl-0041 — direct world_filler over the dusk
   overworld (docs/20 step 1, designer in the loop). Bring W-14's
   villager test: for every proposed placement, "what is this doing
   here?" must have an answer a villager could give.

**Two-tier reminder:** designer is post-shift — NO feel verdicts
tonight (no M2 close, no six-ordinaries ratification, no loop
judgeable call). Intakes, taste rulings, direction, render checks:
all fine.

## 2. Doc-state audit results (this seam — what's current, what's not)

Audited by the forklift session before this handoff:

| Doc | State |
|---|---|
| docs/03-HANDOFF | CURRENT — workday seam section + tonight's evening addendum (incl. this merge note) |
| docs/08 CORE-53/55 | CURRENT — amended rows carry the Gate-1 rewrite properly |
| docs/12 | Annotated-stale BY DESIGN — supersession banner at top points to docs/19 |
| docs/19 | CURRENT + new world-frame context line (loop = first mile of the Part I world) |
| docs/20 | CURRENT (new this seam) |
| doc 16 pin table | Prose table is a RENDERING of `tools/ecosystem.lock.json` now; lock truthed at the workday seam |
| INTERVIEW_STATE | CURRENT (2026-07-30 amendment blocks present) |
| notes/operator-guide/ | NEW — quick card + manual (evergreen) + queue snapshot (perishable, evening-refreshed) |

**Known nits (small, do in passing, right lane):**
- GAME repo CLAUDE.md still says "docs/08+12 prose truth-up pending
  planning-side" — that flag is stale (the truth-up exists as
  amendment blocks + banner). Clear it in a game session's next
  CLAUDE.md touch.
- docs/08 §Bot-testing tail still reads "Gates 1/2 are judged by
  fresh outside human testers" — pre-rewrite phrasing; the amended
  CORE-53/55 rows govern. One-line annotation whenever a planning
  session is in that file anyway.

## 3. Open cross-repo board (verified against the log this seam)

- **sl-0035 OPEN** — b72 delivered, game intake pending (tonight #1).
- **sl-0041 OPEN** — world_filler directed-overworld rehearsal
  (tonight #5 / whenever).
- Standing: sl-0003, sl-0005.
- W-13 walkability ask: DRAFTED, not yet opened (tonight #4).

## 4. Today in one paragraph (context for any fresh agent)

The designer proposed "rethink the game — Erenshor-style zones"; the
interview record showed the persistent zoned world IS the recorded
Part I design (CORE-16 onward), so the ruling landed as a
reconnection: the Loop milestone is the first mile of that world, no
CORE amendments needed. Fourteen world/aliveness directions (W-1..14)
were recorded — headlines: camps-as-organic-places prerequisite,
intertwined zones with cross-band pockets (pillar candidate), the
purposefulness rule ("a villager could tell you why it's here",
pillar candidate), night/weather may never tax visibility or
framerate (guardrail), and the designer's own aliveness test (organic
enemies → loot worth reading → sound you don't mute; RF music already
passed the never-mute bar). Also shipped: operator guide v1 + the
perishable queue snapshot. Hours: ~1 h scattered phone time,
designer's call on logging (recommendation on record: log 1.0 h).
