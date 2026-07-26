# Wildshot Adventures — Project Documentation

**Documentation snapshot:** 2026-07-26  
**Project stage:** Guided concept definition / early pre-production  
**Current questionnaire position:** CORE-01 through CORE-17 and CORE-20 through CORE-55 answered; CORE-14 remains provisional/test-gated; only CORE-18 and CORE-19 remain open; CORE-18 is the active question. (For the live position, `notes/INTERVIEW_STATE.md` is authoritative.)

This extracted project folder converts the guided design interview into project-facing documents that are easier to carry between chats and eventually into development tools or a repository. The July 21 handoff is retained as a historical provenance record. The current living documents integrate the approved CORE-21 through CORE-32 answers and advance the active question to CORE-33.

## Source hierarchy

When documents disagree, use this order:

1. `10-LIVING_DESIGN_QUESTIONNAIRE.md` — authoritative detailed interview record, integrated through CORE-55 except CORE-18/19, with CORE-18 marked active.
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

CORE-16 is locked: the game does not prescribe one normal session duration or require a guaranteed upgrade for a session to be worthwhile; targeted reward attempts use independent RNG without escalating chance or banked pity; active single-player play is pausable; and an ordinary dungeon is one committed instance that ends when abandoned. Exact raid commitment and checkpoint structure remain deferred.

CORE-21 through CORE-24 are locked. Ordinary level-appropriate combat uses a flexible engage/fight/resolve/loot loop whose ten-second frame is representative rather than a required fight duration. Ten-minute and one-hour play remain self-directed and may focus on one pursuit or mix activities naturally, without guaranteeing completion or an upgrade. The main long-term objective is the rise from an unknown adventurer into a legendary endgame hero, with endgame treated as a substantial core continuation rather than post-story cleanup.

CORE-25 through CORE-30 define the supporting-activity and world foundation. Fishing and foraging are optional leveled collection systems; limited crafting deterministically produces known non-combat rewards; housing, player-managed settlement growth, and broad professions are not currently planned. The world uses large connected outdoor zone maps, handcrafted foundations, controlled procedural variation, mostly soft outdoor gates, stable authored difficulty without player scaling, and selective paid teleportation that preserves special manual routes.

CORE-31 and CORE-32 lock real-time, seamless, spatial free-aim combat and the primary-attack baseline. No selected target is ever required. Tap, hold, and toggle autofire all use current free aim. Ordinary attacks consume no resource, preserve predictable movement and aiming, use deterministic weapon-defined patterns, collide clearly with terrain, and use readable impact feedback.

CORE-17 remains open and should be framed as the **first character's journey to endgame** or **initial zero-to-hero journey**, not a fixed first campaign. CORE-18 retains open structural questions while respecting CORE-24's locked endgame direction. CORE-19 and CORE-20 remain unanswered. The designer chose to continue at CORE-33.

## Working method

Continue the questionnaire one focused question at a time. Straightforward decisions should be summarized briefly. Important risks deserve honest challenge and alternatives. Use existing answers before asking again and preserve status tags.

After an answer is approved, update the current GDD, Decision Register, Living Questionnaire, and any affected companion documents; then verify the actual text and active marker in those exact files. Do not treat a separately saved copy as though a Project attachment automatically refreshed.

The documentation set remains extracted for normal use. A ZIP may be supplied only as a convenient transfer package; it is not the working source of truth.
