# Wildshot — Project Notice: Biggest Issues (2026-07-28)

Snapshot after the full seven-repo assessment. Engineering is ~10 weeks ahead
of the docs/12 schedule (M0–M6 complete, M7 done except export.ps1). Every
issue below is what stands between here and Gate 1, ranked by risk.
**Nothing here is code-blocked — the critical path is decisions and calendar
time, not engineering.**

---

## P1 — The tester pipeline hasn't started (the real Gate 1 risk)

The plan's own words: the constraint is **tester turnaround, not designer
hours**. Strangers show up on calendar time — this is the one thing that
can't be compressed the way the build was.

- itch page, devlog thread, bare Discord: **still not stood up** (open since
  M3; the plan moved them early specifically to give recruitment a runway).
- Weekly GIF cadence: GIF #1 posted, **GIF #2 open** — fresh material exists
  (Warden fight, M6 pack in the dusk town, generated world).
- Tester recruitment sizing (10–16 candidates, ≥4 strangers per cycle,
  ≥5 reserved for cycle 2): **the one original plan ruling never made**.

**Next action (designer):** stand up the three channels, post GIF #2, rule
on recruitment sizing. ~1 evening total.

## P2 — The decision/ratification backlog (all designer-owned)

Everything engineering-side is gated on your word:

1. **Four-ruling menu** (one line each): grass slits · reactive as policy of
   record (closes ledger #11, dissolves first_contact adjudication) ·
   Warden HP 8.4s-vs-575 · six-ordinaries ratification ("Approved : not
   done" still needs the word).
2. **Verdict/testing system ruling** — parked until you're home. Decides
   whether your in-session verdicts count (two-tier proposal drafted in
   chat). This one *unlocks* most of item 3.
3. **The rested ratification bundle** (now large): M2 movement close (open
   since July!), six ordinaries, Warden full fight + [T] values, sphere
   set/§2.6, three arenas, 9-row eye rows, eyes-closed audio test, CORE-34
   no-ability clear. Recommend 2–3 short rested sessions, not one marathon —
   or the two-tier verdict ruling shrinks this list sharply.

**Next action (designer, when home):** verdict-system ruling first, then the
four one-liners, then schedule the rested pass(es).

## P3 — Cross-repo integrity risks (cheap now, expensive later)

- **8-bit-sprite-assembler: the pack the game consumes is unreproducible
  from any repo we can see.** Game pack was built from tool commit
  `b7eae05f…` — that commit exists in no branch of the checkout (local HEAD
  is 2026-07-17, 41 families; the game consumes 57 families/202 variants).
  The exporter work lives on an unpushed machine/branch. If that machine is
  lost, the actor pipeline breaks. Also still missing tool-side: **cast**
  animation (CORE-34 ability slot wants it) and death animation.
  → *Push that commit from wherever it lives.*
- **WorldForge: unmerged behaviors-49/50 branch** with an explicit merge
  runbook in HANDOFF.md §1a; the dusk game pack **must be re-exported after
  the merge** (identity bytes shift). Until merged, the game is pinned to a
  pack the merge will orphan.
  → *Run the merge runbook, re-export, re-run the game intake battery.*
- **world_filler: format-1 freeze is provisional with credible verifier
  holes.** The adversarial review was cut off (4/5 lenses, zero
  verification); claimed criticals: neither reference verifier reads
  `report.json` (an `ok:false` pack passes), empty `manifest.files` makes
  hash checks vacuous, and TS-vs-GDScript diverge on row-crossing
  territories (wrap vs refuse).
  → *Fix the verifiers BEFORE any game-side importer copies them.*

## P4 — Engineering remainder (small, known)

- `tools/export.ps1` dev + tester profiles + the export step on the
  pre-tester checklist (design already staged in
  notes/EXPORT_PIPELINE_DESIGN.md). Last M7 item.
- M8 items untouched by design (laptop pass, tester onboarding, feedback
  bundle, tester-profile lockdown verification) — correctly sequenced after
  the rulings.

## P5 — Process drift (quiet, compounding)

- **Hours log (PROD-01):** only ~8.5 h formally closed against ~2 days of
  heavy work; repeated missed stops; the 16-hour Jul-28 session barely
  logged. The 40 h/week floor check and the 60–150 h Phase A actuals are
  only as good as this file. → *Backfill honestly once, then log going
  forward.*
- **Stale state docs:** `INTERVIEW_STATE.md` (self-declared source of truth)
  still says "M2 IN PROGRESS" — five milestones behind. `docs/03-HANDOFF`
  same. A cold-start session following the repo's own reading order would be
  badly misled. → *One truth-up commit.*
- **Verdict capture:** designer verdicts given as chat one-liners land as
  PROVISIONAL notes — the system that fixes this is P2 item 2.

## P6 — Watch item: scope discipline at high velocity

All creep so far was designer-approved and proof-covered (three arenas vs
"one greybox arena"; WorldForge consumption pulled forward twice), and the
movement-bug saga came directly from out-of-bill content. Being 10 weeks
ahead is exactly when the tripwire matters most. Not a problem yet — keep
the refuse-and-ledger reflex.

---

## Suggested "when I get home" agenda (in order)

1. Rule on the verdict system (two-tier / strict / all-count).
2. The four one-liner rulings.
3. Push the missing assembler exporter commit from the other machine.
4. Stand up itch/devlog/Discord + post GIF #2.
5. Schedule rested session #1 (movement close + six ordinaries — the
   biggest unlock, ~30 min).
6. Green-light the housekeeping batch (WorldForge merge, world_filler
   verifier fixes, docs truth-up, export.ps1) — all engineering-side, can
   run while you sleep.
