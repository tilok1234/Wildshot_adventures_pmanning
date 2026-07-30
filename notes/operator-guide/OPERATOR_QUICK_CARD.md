# Wildshot Operator — Quick Card

> **What this is:** the one-glance version of how you run the seven-repo
> machine. It is a DERIVED digest, not an authority — on any conflict the
> planning docs and the Decision Deck win. Full detail: OPERATOR_MANUAL.md
> beside this file. Snapshot date: **2026-07-30**. Regenerate after any
> ruling that changes protocol.

---

## 1. The five golden rules

- **One repo per session.** Open the repo where the change will land.
  Game sessions keep the game + planning pair; planning/decision sessions
  start in planning.
- **Nothing ships that you didn't rule.** Agents implement; decisions are
  yours — chat one-liners and deck taps count immediately (Tier 1).
- **Feel is yours alone, and only rested.** Bots never judge feel. Dirty
  runs (god, slow-mo, runtime edits) stay PROVISIONAL no matter how good
  it felt at hour 14.
- **Everything between repos moves as a recorded event.** Packs travel by
  GitHub release + hash check. Needs become asks. Problems become
  incidents. Never hand-carry zips, never hand-edit an exported artifact.
- **Push before you stop.** Unpushed work on one machine is how the
  assembler drift happened. "Pushed" is verified, not assumed.

## 2. Starting any session

1. `tools/hourslog.ps1 start` — before ANY project work (code, art,
   design, planning — all of it).
2. Tell the agent the goal in a line or two. It reads the repo contract,
   checks the branch, and skims the sync log itself — that's its ritual,
   not yours.
3. If it flags a conflict with planning docs: that's a **stop**. Rule it
   in planning, never in the implementing repo.

## 3. Ending any session

1. The agent updates HANDOFF, appends sync-log entries for real
   cross-repo events, commits, pushes, and **confirms the push landed**.
   Your job: make sure it said so.
2. Deal any new deck cards it staged. If you tapped decisions in the deck
   app, EXPORT the JSON and hand it to the next session for the sweep.
3. `tools/hourslog.ps1 stop`.

## 4. Making decisions (the Decision Deck)

- **Tier 1:** your in-session calls (chat one-liners, deck taps) are
  decisions immediately.
- **Tier 2:** *feel* items additionally get ONE rested ratification pass
  before they're final.
- **"Rested" keys on YOUR day, not the clock.** You work 15:00–23:00 —
  home at midnight is your ~17:00, which is *not* rested. Day-start,
  fresh, clean build.
- Deck flow: open `tools/decision_deck.html` → PASTE FROM AI (append) →
  deal → decide (note optional) → EXPORT JSON → hand to the next session.

## 5. Recording verdicts in-game

Console (` key):

    verdict <dodgeability|feel> <rested-human|bot-proof> <text>

- `feel` REJECTS bot sources by design — that's correct behavior.
- God mode, slow-mo, or a runtime edit auto-stamps later verdicts
  PROVISIONAL. Honor the stamp; re-record on a clean rested run.
- Dodgeability accepts {rested-human, bot-proof}. Feel accepts rested
  humans only.

## 6. Packs moving between repos (your part)

- Producers ship via **GitHub release**; the consuming agent verifies
  hashes before the drop touches anything. If origin can't be verified:
  refuse + incident — no exceptions, even from yourself.
- The sync-log app's top board answers the three questions: **deliveries
  waiting for intake / open problems / open asks.** Skim it, mark things
  resolved with a one-line note, EXPORT, commit (or tell the next agent).
- **Pins are deliberate.** A repo holding an older upstream version is a
  recorded choice. Never "helpfully" upgrade one without a ruling.

## 7. Playtesting law (quiet lab)

- Watched first-touches are **silent**: no coaching, no prompting, no
  explaining — you observe, never guide.
- CORE-54 evidence = **unprompted** quotes only (Discord/itch/feedback
  channels, verbatim). Debrief answers to your questions get marked
  "prompted". The in-build comments box never counts as CORE-54.
- **The Loop bar:** play THE LOOP daily. Fun for a week = the bar holds →
  only then schedule the 2–3 warm watched first-touches.

## 8. Weekly cadence (never skips)

- **One 30–60 s GIF** per week: `G` dumps the ring buffer →
  `tools/gif.ps1` → post to the devlog + one community.
- `tools/hours_report.ps1` weekly. A 4-week rolling average under
  40 h/week triggers the PROD-01 floor reset and the slip ladder — by
  rule, not mood.

## 9. Keys (dev keyboard, no F-row)

| Key | Does | Key | Does |
|---|---|---|---|
| Esc | pause (full freeze) | M | density meter |
| O | options / remap | H | hitbox display |
| I | interp A/B | T | reseed reset |
| `[` `]` | speed presets 3.0 / 4.0 | ` | debug console |
| G | GIF ring-buffer dump | Space | ability |
| R | replay dump | | |

## 10. Hard stops — call it, don't work around it

- Repo contradicts planning docs → stop; resolve in planning.
- Artifact origin unverifiable → refuse intake; incident entry.
- Branch deletion / force-push → **you click**, never an agent.
- Janitor sessions are mechanical only — merge conflicts and "which line
  wins" escalate to you.
- New protocol/tool/system idea → **talk-before-build**: walk it through
  in chat end-to-end, THEN say build.
- Never edit sim data while a battery runs. Never run gates while a Godot
  editor holds the same project open.

## 11. What's open on you

This card stays evergreen on purpose — your **live queue is the
Decision Deck**, and a dated snapshot of open items lives in
`OPERATOR_QUEUE_SNAPSHOT.md` / `WILDSHOT_QUEUE_SNAPSHOT.pdf` beside
this file, grouped by where you can actually do each item (phone /
at the machine / rested day-start). Any session that changes the
queue refreshes the snapshot; this card never rots with it.
