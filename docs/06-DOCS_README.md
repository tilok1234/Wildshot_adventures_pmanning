# Wildshot Adventures — Project Documentation

**Documentation snapshot:** 2026-07-26; header truthed + map extended 2026-08-02.  
**Project stage:** Slice v0.1 BUILD — the world is the test (S0 + S1 engineering complete, Green days open). The live board is `docs/03-HANDOFF.md`'s CURRENT section.  
**Current questionnaire position:** **Part I complete — CORE-01 through CORE-55 all answered** (CORE-14 remains provisional/test-gated). The interview era is over; rulings now land as designer word during the build (`docs/22` is the stat authority, `docs/23` the slice plan). `notes/INTERVIEW_STATE.md` is the interview-era record.

This documentation set lives in the project git repository, which is the source of truth (the live position: `docs/03-HANDOFF.md` CURRENT; the interview-era record: `notes/INTERVIEW_STATE.md`). The July 21 handoff is retained as a historical provenance record. The living documents integrate all approved Part I answers — CORE-01 through CORE-55 — as of 2026-07-26, amended in place as later rulings land.

## Source hierarchy

When documents disagree, use this order:

1. `10-LIVING_DESIGN_QUESTIONNAIRE.md` — authoritative detailed interview record; Part I (CORE-01–55) fully answered.
2. `03-HANDOFF.md` — current continuation state and interview instructions.
3. `08-DECISION_REGISTER.md` — concise record of locked, provisional, test-gated, and open decisions.
4. `01-GAME_DESIGN_DOCUMENT.md` — readable current design overview.
5. `04-OPEN_QUESTIONS.md` — unresolved questions and deferred decisions.
6. `11-HANDOFF_2026-07-21_HISTORICAL.md` — preserved historical provenance record; its old CORE-21 marker is intentionally not the current interview state.
7. Other numbered planning documents — working interpretations, risks, and test plans, not new locked decisions.

## Status tags

- **[L] Locked:** committed direction; other systems may depend on it.
- **[P] Provisional:** current preference; safe to discuss and prototype, but open to revision.
- **[T] Test:** must be decided through implementation, calculation, or playtesting.
- **[U] Unknown:** not yet answered.
- **[CUT] Excluded:** outside the current direction.
- **[LATER] Deferred:** relevant later, but not required for the next milestone.

## Document map

- `01-GAME_DESIGN_DOCUMENT.md` — integrated high-level game design through CORE-32.
- `02-RISK_REGISTER.md` — major design, technical, scope, and production risks.
- `03-HANDOFF.md` — current continuation instructions for a fresh chat or work session.
- `04-OPEN_QUESTIONS.md` — unanswered CORE questions and deferred implementation details.
- `05-PREPRODUCTION_ROADMAP.md` — recommended order of design and implementation.
- `06-DOCS_README.md` — this inventory, source hierarchy, and current status.
- `07-PROTOTYPE_SPEC.md` — proposed combat laboratory, reward-loop tests, and early co-op feasibility gate.
- `08-DECISION_REGISTER.md` — exact decision status through CORE-32 and the current interview position.
- `09-SYSTEMS_MAP.md` — system responsibilities, dependencies, and critical interactions.
- `10-LIVING_DESIGN_QUESTIONNAIRE.md` — authoritative detailed interview record.
- `11-HANDOFF_2026-07-21_HISTORICAL.md` — unchanged July 21 provenance source.
- `12-PHASE_A_LAB_BUILD_PLAN.md` — approved Phase A lab build plan (2026-07-27): Godot architecture bundle [P], v0 tuning hypotheses [T], 12 milestones with the vacation-sprint split, slip ladder, session workflow. (Executed ahead of schedule; tester prose superseded — see its Gate-1 banner.)
- `13-UI_STYLE_KIT_SPEC.md` — UI chrome kit contract (shipped + consumed; frozen ids, 12×12 chrome).
- `14-ASSEMBLER_GAME_PACK_SPEC.md` — the sprite-assembler enemy-pack contract (pack intaken; pins in the lock file).
- `15-WORLDFORGE_INTEGRATION_PLAN.md` — WorldForge→game integration plan (EXECUTED — see its banner; b77 is the live overworld).
- `16-ECOSYSTEM_MAP.md` — seven-repo ownership, authority docs, and cross-repo rules (never status or pins).
- `17-WORLD_FILLER_INTEGRATION_PLAN.md` — world_filler→game integration plan (EXECUTED end to end — see its banner).
- `18-AGENT_SYNC_PROTOCOL.md` — the cross-repo sync protocol: sync log + ecosystem lock (ACCEPTED 2026-07-30).
- `19-LOOP_MILESTONE_SPEC.md` — the Gate-1 rewrite: the loop bar + world-is-the-test (deck-ratified 2026-08-01).
- `20-WORLD_CONTENT_ARC.md` — the world_filler content arc (COMPLETE end to end).
- `21-ICON_SET_PLAN.md` — the icon-set plan (pack delivered, WIRED since S0 seam 4).
- `22-STAT_SYSTEM.md` — **THE STANDING STAT AUTHORITY** (all nine blocks ruled 2026-08-01).
- `23-SLICE_BUILD_PLAN.md` — **Slice v0.1 build plan (ACTIVE — the era's governing doc).**

## Current integration summary

Part I of the interview is complete: CORE-01 through CORE-55 are all answered, with CORE-14 remaining prototype-gated. The 2026-07-26 session recorded the combat core (movement-only dodging, one item-granted active ability, focus targeting cut, the intensity ladder, pack grammar, readability laws), the item and stat architecture (four-slot loadout, lean stat set, equipment as the build system), progression (level purpose, points-deep tree, faction direction, 40–80-hour first journey, collectathon endgame), loot and death rules, quests and hubs, accessibility, the full vertical-slice bill, the ranked risks, both continuation gates, and the production constraints (solo AI-orchestrated developer, Godot [P], no deadline). See `03-HANDOFF.md` for the one-screen decision summary and `08-DECISION_REGISTER.md` for the per-question record.

## Working method

Continue one focused question or task at a time. Straightforward decisions are summarized briefly; important risks get honest challenge and alternatives. Use existing answers before asking again and preserve status tags.

After an answer is approved, update the Living Questionnaire, Decision Register, GDD, and affected companion documents, then **commit and push** — one approved answer, one commit. The git repository is the working source of truth; a ZIP is only ever a transfer convenience.
