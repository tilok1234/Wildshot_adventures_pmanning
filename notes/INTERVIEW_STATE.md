# Interview State — ALWAYS CURRENT

> **This file is the single source of truth for where the guided design interview stands.**
> Any session (human or AI) continuing the interview MUST read this file first,
> and MUST update + commit it after every approved answer. If this file and chat
> memory disagree, this file wins.

**Last updated:** 2026-07-26 (refinement batch recorded — see below)

## Active question

**CORE-39 — What is the purpose of character levels?**

*Consider: Broad power, access, skill unlocks, talent points, equipment eligibility, or
another function.*

No answer has been accepted yet. Partially pre-answered: levels grant skill points and
broad advancement (CORE-03 / GDD §9 table); dungeons, raids, and selected instances use
explicit minimum-level entry requirements (CORE-28). Remaining to decide: whether levels
also grant direct statistics (and how that interacts with gear-driven stats from
CORE-37); whether equipment has level requirements; whether skill-tree tiers are
level-gated (the CORE-34 capstone concept implied a max-level unlock); and level-cap
philosophy (hard cap as an endgame marker — "reaching endgame is a transition" per
CORE-24). Constraint: no content scales to level (CORE-29); level gates only permit
attempts (CORE-28).

## Question status table

| Range | State |
|---|---|
| CORE-01 through CORE-16 | Answered. CORE-14 remains provisional/test-gated. |
| CORE-17 | Open. Frame as **first character's journey to endgame**, not "campaign". No numerical duration locked. |
| CORE-18 | Open. Constrained by CORE-24's locked endgame direction. |
| CORE-19, CORE-20 | Open, unanswered. |
| CORE-21 through CORE-38 | Approved and integrated into the GDD. |
| **CORE-39** | **ACTIVE — no accepted answer.** |
| CORE-40 onward | Unanswered. |

The designer chose to continue past CORE-38 while CORE-17 through CORE-20 remain open.
Continue at CORE-39 unless the designer chooses to return to an earlier open question.

### CORE-38 — answered 2026-07-26 [P]

Vertical slice: one class — provisionally the Archer — with ~3–5 distinct weapon frames,
~3–4 ability items (covering at least mobility/defense/burst), 2–3 build directions.
Proves the locked combat pillar (movement-only dodging, single active, weapon-owned
patterns, honest bosses, armor/ring tradeoffs). Full game: three classes locked;
per-class content counts explicitly deferred until CORE-20. Rationale: class-exclusive
item families multiply content — prove one class deeply first.

### CORE-37 — answered 2026-07-26 [L/P]

Ownership map confirmed. Class = eligibility + identity (base stats, tree, exclusive
weapon/ability-item families — gear-driven unique playstyle per class). Weapon = pattern
+ damage/attack speed/range. Ability item = the single active, may carry stats. Armor and
ring = classic RPG stats. Four-slot loadout [L/P]: weapon, ability, armor, ring; all
pieces may carry stats. Armor uses give-and-take archetypes (light/high-dmg vs
heavy/low-dmg etc.). Ring anti-degeneracy rule: no universally correct ring (no mandatory
HP ring). Uniques in any slot may carry behaviours beyond stats [P]. Deferred: stat set,
per-slot budgets, class stat spreads, ring class-binding.

### CORE-36 — answered 2026-07-26 [L/P]

Tiered intensity ladder confirmed: fodder → ordinary packs → dangerous packs/pockets →
elites → rare/named roamers → world bosses → dungeon enemies → dungeon bosses → raid
wings → optional superbosses. Escalation axis [L]: projectile density, speed, pattern
complexity, and composition — never HP sponging; health stays honest. Fractal rule [L]:
the open-world ladder repeats inside every zone at that zone's authored band (relaxed
outskirts through genuine danger in each zone); bands don't trivially overlap.

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
