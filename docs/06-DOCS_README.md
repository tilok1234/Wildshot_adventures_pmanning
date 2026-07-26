# Wildshot Adventures — Project Documentation

**Documentation snapshot:** 2026-07-26  
**Project stage:** Guided concept definition / early pre-production  
**Current questionnaire position:** **Part I complete — CORE-01 through CORE-55 all answered** (CORE-14 remains provisional/test-gated). The interview proceeds to Part II modules alongside the Phase A combat laboratory. (For the live position, `notes/INTERVIEW_STATE.md` is authoritative.)

This documentation set lives in the project git repository, which is the source of truth (see `notes/INTERVIEW_STATE.md` for the live position and note-taking protocol). The July 21 handoff is retained as a historical provenance record. The living documents integrate all approved Part I answers — CORE-01 through CORE-55 — as of 2026-07-26.

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

## Current integration summary

Part I of the interview is complete: CORE-01 through CORE-55 are all answered, with CORE-14 remaining prototype-gated. The 2026-07-26 session recorded the combat core (movement-only dodging, one item-granted active ability, focus targeting cut, the intensity ladder, pack grammar, readability laws), the item and stat architecture (four-slot loadout, lean stat set, equipment as the build system), progression (level purpose, points-deep tree, faction direction, 40–80-hour first journey, collectathon endgame), loot and death rules, quests and hubs, accessibility, the full vertical-slice bill, the ranked risks, both continuation gates, and the production constraints (solo AI-orchestrated developer, Godot [P], no deadline). See `03-HANDOFF.md` for the one-screen decision summary and `08-DECISION_REGISTER.md` for the per-question record.

## Working method

Continue one focused question or task at a time. Straightforward decisions are summarized briefly; important risks get honest challenge and alternatives. Use existing answers before asking again and preserve status tags.

After an answer is approved, update the Living Questionnaire, Decision Register, GDD, and affected companion documents, then **commit and push** — one approved answer, one commit. The git repository is the working source of truth; a ZIP is only ever a transfer convenience.
