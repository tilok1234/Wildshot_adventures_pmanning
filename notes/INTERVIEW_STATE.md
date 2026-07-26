# Interview State — ALWAYS CURRENT

> **This file is the single source of truth for where the guided design interview stands.**
> Any session (human or AI) continuing the interview MUST read this file first,
> and MUST update + commit it after every approved answer. If this file and chat
> memory disagree, this file wins.

**Last updated:** 2026-07-26 (refinement batch recorded — see below)

## Active question

**CORE-36 — How does combat intensity vary across the game?**

*Consider: Weak overworld creatures, ordinary packs, dangerous packs, elites, dungeons,
bosses, and optional expert content.*

No answer has been accepted yet. NOTE: this is partially pre-answered — the experience/
intensity curve is already locked at a coarse level (open world laid-back → dungeons and
world bosses faster and more demanding → endgame bosses/raids relentlessly intense but
readable; CORE-31 intensity curve + GDD §8 experience curve). CORE-36's job is the finer
ladder: weak creatures vs ordinary packs vs dangerous packs vs elites vs rare enemies vs
dungeon trash vs bosses vs superbosses, and how density/speed/pattern complexity step up
across those tiers. Constraints: stable authored difficulty, no scaling (CORE-29); every
pattern dodgeable by movement alone (CORE-33); no ability ever required (CORE-34).

## Question status table

| Range | State |
|---|---|
| CORE-01 through CORE-16 | Answered. CORE-14 remains provisional/test-gated. |
| CORE-17 | Open. Frame as **first character's journey to endgame**, not "campaign". No numerical duration locked. |
| CORE-18 | Open. Constrained by CORE-24's locked endgame direction. |
| CORE-19, CORE-20 | Open, unanswered. |
| CORE-21 through CORE-35 | Approved and integrated into the GDD. |
| **CORE-36** | **ACTIVE — no accepted answer.** |
| CORE-37 onward | Unanswered. |

The designer chose to continue past CORE-35 while CORE-17 through CORE-20 remain open.
Continue at CORE-36 unless the designer chooses to return to an earlier open question.

### CORE-35 — answered 2026-07-26 [CUT]

Focus targeting is cut entirely: no selection, lock-on, marking, focused-enemy state, or
hover focus on any input method; nothing is ever tied to a focused enemy. Enemy info
(names, health, boss casts) comes through general interface presentation (overhead bars,
boss presentation, bestiary — implementation deferred to interface/knowledge questions).
Controller aim assistance, if retained, must work without a focus system and stays
quarantined from M+K play and encounter design.

### CORE-34 — answered 2026-07-26 [L/P]

Exactly one active ability per character, granted by an equipped ability item; each class
has its own large pool of ability-equips, so ability variety and build identity come from
the loot hunt (weapon = primary pattern, ability item = active, armor = stats). Abilities
run on mana; the item defines behaviour and cost. The skill tree grants no actives — it is
passives/resource/specialization with a binding condition that meaningful nodes change
behaviour, not just numbers (including modifying equipped ability items). Max-level
capstone that supercharges the equipped item = open design space [P]. No mandated role
checklist. No encounter may require a specific ability item, or any ability, to be
survivable — movement stays sufficient (designer: "awesome boss fights where movement is
enough, just like RotMG").

### CORE-33 — answered 2026-07-26 [L/P]

Purely movement-based dodging, RotMG tradition. Universal kit = movement + free aim only;
no universal dash, roll, blink, sprint, block, parry, shield, or i-frame action. Binding
consequences recorded: honest dodgeability by movement alone (at the least mobile class's
baseline), movement speed as a premier tuned stat, readability/traceable deaths even more
load-bearing, death design must account for no escape action. Class-specific mobility or
defensive abilities may exist as class tools [P]; never required by encounters; roles and
counts belong to CORE-34.

### Refinement batch — 2026-07-26 (approved, recorded, committed)

Out-of-order refinements approved after a coherence review; integrated into the GDD,
Decision Register, and Living Questionnaire:

1. **Dry-streak mitigation [P]** (CORE-16): no pity ever; reward breadth instead —
   cosmetic/collection drops from bosses, recorded straight into the collection menu.
2. **Controller worst case [P]** (CORE-13/12): controller may end up as the relaxed
   grinding input only; endgame expects M+K; Steam Deck demoted to "where it survives".
3. **Variation bounds [P]** (CORE-27): authored *where*, pooled *what* — fixed arenas
   with 3–4 possible bosses; roaming rares patrol authored zone+route; pooled locations
   share key rewards or stay variety-only.
4. **Pets cosmetic-only [P]** (CORE-25): no combat/stat benefit of any kind, if included.
5. **Raid structure [P/T]** (CORE-16 raid scope): wings as the unit of commitment;
   player-controlled persistence, no time-based lockouts, free instant reset;
   deterministic skip baseline (mastery shortcuts or trophy tokens) [T]; rare skips
   only as luxury on top; within-wing checkpoints test-gated.

## Note-taking protocol (the fix for lost notes)

After **each** approved answer, in the same working session, before moving to the next question:

1. Record the approved decision with its status tag ([L]/[P]/[T]/[U]/[CUT]/[LATER]) in
   `docs/10-LIVING_DESIGN_QUESTIONNAIRE.md` (fill the question's answer slot).
2. Update `docs/08-DECISION_REGISTER.md` with the concise decision entry.
3. Integrate the decision into `docs/01-GAME_DESIGN_DOCUMENT.md` where it belongs.
4. Update the **Active question** and **status table** in this file to the next question.
5. Append a short entry to today's file in `notes/sessions/`.
6. `git commit` all of the above and push. **One approved answer = one commit.**

Never batch multiple answered questions into a deferred "I'll write it up later" step —
that is exactly how notes were lost before this repo existed.

## Working method (established, unchanged)

- Ask one focused question at a time and finish it before moving on.
- Consolidate the designer's natural answer into clear design language; get approval before recording.
- Keep straightforward decisions concise; expand when a decision has real design, balance, technical, or production consequences.
- Use existing answers before asking for a decision again.
- Challenge material design or production risks honestly.
- Treat purposeful, targetable repetition as an intended strength.

## Source hierarchy

1. `docs/10-LIVING_DESIGN_QUESTIONNAIRE.md` — authoritative detailed interview record.
2. `notes/INTERVIEW_STATE.md` (this file) — current position and continuation instructions.
3. `docs/08-DECISION_REGISTER.md` — concise decision status.
4. `docs/01-GAME_DESIGN_DOCUMENT.md` — readable integrated design overview.
5. `docs/04-OPEN_QUESTIONS.md` — unresolved questions and deferred details.
6. `docs/11-HANDOFF_2026-07-21_HISTORICAL.md` — historical provenance only; its CORE-21 marker is intentionally outdated.
